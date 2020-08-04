from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



#class SignupForm(UserCreationForm):
#   fields = ('username', 'email', 'password1', 'password2')
    #those fields are default for UserCreationForm - https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
    #below we customize those field names to be more user friendly




class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Account Name'
        self.fields['email'].label = 'E-mail Address'





def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = self.request.POST.get('password', None)
            authenticated = authenticate(
                username=user.username,
                password=password
            )
            if authenticated:
                login(request, authenticated)
                return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {
        'form': form
    })