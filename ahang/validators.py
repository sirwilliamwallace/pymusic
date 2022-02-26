from django.core.exceptions import ValidationError

def validate_file(value):
    value = str(value)
    if (value.endswith(".mp3") != True and value.endswith(".wav") != True and value.endswith(".pcm") != True and value.endswith(".aiff") != True and value.endswith(".aac") != True and value.endswith(".ogg") != True and value.endswith(".wma") != True and value.endswith(".flac") != True and value.endswith(".wma") != True):
        raise ValidationError("ِYo this file format is not supported")
    return value