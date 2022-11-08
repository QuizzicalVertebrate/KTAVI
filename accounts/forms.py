from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = get_user_model()
        fields = ('username', 'email')

#meta is djangos way of allowing you to change the basic parts of a class
# get_user_model which looks to our AUTH_USER_MODEL config in settings.py. 



class CustomUserChangeForm(UserChangeForm):
    pass