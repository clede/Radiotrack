from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

class UserCreationFormTZ(UserCreationForm):
    tz = forms.ChoiceField(choices=UserProfile.TZ_CHOICES,
        initial='America/Los_Angeles',
        # Time zone label DOES work here.
        label='Time zone')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'tz']
        labels = {'tz': 'Time zone',}
        # Time zone label doesn't work here, presumably because this field is
        # from a different model. What I think I need to do is to use two
        # separate forms: 1. User, 2. UserProfile.
        # I can use the template to simply display both forms simultaneously.
        #
        # I think this will help: http://stackoverflow.com/a/11101917/1325678

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("""Can't create User and UserProfile
                without database save""")
        user = super(UserCreationFormTZ, self).save(commit=True)
        userprofile = UserProfile(user=user, tz=self.cleaned_data['tz'])
        userprofile.save()
        return user, userprofile
