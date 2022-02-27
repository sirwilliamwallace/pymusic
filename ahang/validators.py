from django.core.exceptions import ValidationError
exts = [
        ".mp3",
        ".wav",
        ".pcm",
        ".aiff",
        ".aac",
        ".ogg",
        ".wma",
        ".flac",
        ".wma",
        ]
def validate_file(value):
    value = str(value)
    for i in exts:
         if (value.endswith(i) != True):
            raise ValidationError('Yo this file format is not supported')
         return value
