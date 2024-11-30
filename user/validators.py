from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

username_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9](?!.*__)[a-zA-Z0-9_]*$',
    message=(
        "Username can only contain letters, numbers, and underscores, "
        "and cannot start with an underscore."
    )
)


def password_validator(value):
    import re
    if len(value) < 8:
        raise ValidationError("At least 8 characters.")
    if not re.search(r'[A-Za-z]', value):
        raise ValidationError("Must include a letter.")
    if not re.search(r'\d', value):
        raise ValidationError("Must include a number.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        raise ValidationError("Must include a special character.")
    return value
