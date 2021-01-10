from django import forms

class RegistrationForm(forms.Form):
    firstname = forms.CharField(
        label="Enter your first name",
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your first name'
            }
        )
    )

    lastname = forms.CharField(
        label="Enter your last name",
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your last name'
            }
        )
    )
    username = forms.CharField(
        label="Enter your user name",
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your user name'
            }
        )
    )
    password = forms.CharField(
        label="Enter your password",
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your password'
            }
        )
    )
    mobile= forms.IntegerField(
        label="Enter mobile field",
        widget= forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile number'
            }


        )
    )
    email= forms.EmailField(
        label="Your email id",
        widget= forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email id'
            }
        )
    )
    GENDER_CHOICES = (
        ('Male','MALE'),
        ('Female','FEMALE')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=GENDER_CHOICES,
        label="Select your gender"
    )
    y= range(1960,2020)
    date_of_birth = forms.DateField(
        widget=forms.SelectDateWidget(years=y),
        label="Enter your date of birth"

    )

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Enter your user name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your user name'
            }
        )
    )
    password = forms.CharField(
        label="Enter your password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your password'
            }
        )
    )