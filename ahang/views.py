from django.shortcuts import render, get_object_or_404, redirect
from .models import Ahang, CommentDb
from .forms import LoginForm, CommentForm, AhangUplaodingForm, SignUpForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout


def index(request):
    ahangha = Ahang.objects.all().order_by('-id')
    context = {
        "ahangha": ahangha,
        "title": "Home",
    }
    return render(request, 'main/index.html', context)


# def ahang_detail(request,id=None):
#     ahang = get_object_or_404(Ahang,id=id)
#     esme_ahang = f"{ahang.author}\t-\t{ahang.ahang_esm}"

#     # comment's
#     if request.method == "POST":
#         nazar = request.POST.get("cm")
#         CommentDb(comment=nazar).save()
#         #print (request.POST.get("cm"))
#     nazarat = CommentDb.objects.all()
#     context = {
#          "ahang":ahang,
#          "nazarat": nazarat,
#          "title":esme_ahang,
#     }
#     return render(request,'main/ahang_detail.html',context)

def ahang_detail(request, id=None):
    ahang = get_object_or_404(Ahang, id=id, isAgreed=True)
    esme_ahang = f"{ahang.author}\t-\t{ahang.ahang_esm}"

    comments = ahang.comments.filter(active=True)

    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current ahang to the comment
            new_comment.ahang = ahang
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        "ahang": ahang,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
        "title": esme_ahang
    }
    return render(request, 'main/ahang_detail.html', context)


def upload_music_form(request):
    # ISSUE: file not uploading
    if request.method == "POST" and request.user.is_authenticated:
        form = AhangUplaodingForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Your music has uploaded successfully and after confirmation it will be published on the website")
            form = AhangUplaodingForm()
            context = {
                "form": form
            }
            return render(request, "main/upload.html", context)
        context = {
            "form": form
        }
        return render(request, "main/upload.html", context)
    form = AhangUplaodingForm()
    context = {
        "form": form
    }
    return render(request, "main/upload.html", context)


def search(request):
    # gets q in address bar
    query = request.GET.get('q')
    button = request.GET.get('submitbutton')
    if query is not None:
        lookup = Q(author__icontains=query) | Q(description__icontains=query) | Q(ahang_esm__icontains=query)
        result = Ahang.objects.filter(lookup, isAgreed=True).distinct()
        context = {
            "result": result,
            "submit": button
        }
        return render(request, "main/search.html", context)
    return render(request, "main/search.html")


def register(request):
    """ handles user creation form """
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            this_username = form.cleaned_data.get("username")
            this_password = form.cleaned_data.get("password1")
            user = authenticate(username=this_username, password=this_password)
            login(request, user)
            messages.success(request, f"ًSuccessfully Registered as {this_username}")
            form = SignUpForm()
            return redirect("music:home")
        else:
            messages.error(request, "Unfortunately, we couldn't register you try again ...")
            form = SignUpForm()

    return render(request, "main/signup.html", {"form": form})


def login_view(request):
    """ handle's User Login """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            messages.success(request, f"Welcom  {username} :)")
        else:
            messages.error(request, f"try again  {username} if you are not registered yet, please register first or contact the admin")
            form = LoginForm()
            return render(request, 'main/login.html', {"form": form})

    form = LoginForm()
    return render(request, 'main/login.html', {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("music:home")
