from django.forms import ModelForm
from django import forms
from .models import CommentDb, Ahang
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    name = forms.CharField(
        label="اسم ",
        label_suffix="",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )
    email = forms.EmailField(
        label=" ایمیل",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={"placeholder": "ایمیل ", "class": "form-control"}
        ),
        required=True,
    )
    body = forms.CharField(
        label="متن اهنگ",
        label_suffix="",
        widget=forms.Textarea(
            attrs={"placeholder": "متن", "class": "form-control"}
        ),
        required=True,
    )

    class Meta:
        model = CommentDb
        fields = ('name', 'email', 'body')


class AhangUplaodingForm(ModelForm):
    """ let user upload a music """
    author = forms.CharField(
        label="Author's name",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"placeholder": "Author's name", "class": "form-control"}
        ),
        required=True,
    )
    description = forms.CharField(
        label="Lyrics",
        label_suffix="",
        widget=forms.Textarea(
            attrs={"placeholder": "Lyrics", "class": "form-control"}
        ),
        required=True,
    )
    ahang_esm = forms.CharField(
        label="Song's name",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"placeholder": "Song's name", "class": "form-control"}
        ),
        required=True,
    )
    ahang_file = forms.FileField(
        label="Song's file",
        label_suffix="",
        widget=forms.FileInput(
            attrs={"placeholder": "Song's file", "class": "form-control-file"}
        ),
        required=True,
    )

    class Meta:
        model = Ahang
        fields = ("author", "description", "ahang_esm", "ahang_file",)


class SignUpForm(UserCreationForm):
    """ register's a user """
    first_name = forms.CharField(
        label="name ",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"placeholder": "name ", "class": "form-control"}
        ),
        required=True,
    )
    username = forms.CharField(
        label="username",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"placeholder": "username", "class": "form-control"}
        ),
        required=True,
    )
    email = forms.EmailField(
        label="email address",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={"placeholder": "email address", "class": "form-control"}
        ),
        required=True,
    )
    password1 = forms.CharField(
        label="password",
        label_suffix="",
        widget=forms.PasswordInput(
            attrs={"placeholder": "password", "class": "form-control"}
        ),
        required=True,
    )

    password2 = forms.CharField(
        label="password confirmation",
        label_suffix="",
        widget=forms.PasswordInput(
            attrs={"placeholder": "password confirmation", "class": "form-control"}
        ),
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "username",
            "email",
            "password1",
            "password2",
        )
        help_texts = {
            "username": None
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="username",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"placeholder": "username", "class": "form-control"}
        ),
        required=True,
    )
    password = forms.CharField(
        label="password",
        label_suffix="",
        widget=forms.PasswordInput(
            attrs={"placeholder": "password", "class": "form-control"}
        ),
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )
