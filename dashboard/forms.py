from django import forms
from dashboard.models import Register, Profile, HomePage

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username', 'email', 'password', 'first_name', 'last_name', ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'user123',
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'user123@example.com'
            }),
            'password': forms.PasswordInput(attrs={
                'class':'form-control',
            }),
            'first_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Last Name'
            })
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio' ]
        widgets = {
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'bio': forms.Textarea(attrs={
                'rows':2,
                'class':'form-control'
            })
        }


class HomePageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = ['title', 'pic', ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Post Title',
            }),

            'pic': forms.FileInput(attrs={
                'class': 'form-control',
            })
        }