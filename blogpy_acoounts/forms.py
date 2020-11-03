from django import forms


class LoginForm(forms.Form):
    user_name = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام کاربری خود را وارد کنید"}))

    password = forms.CharField(
        label='کلمه ی عبور',
        widget=forms.PasswordInput(attrs={"placeholder": "لطفا رمز عبور خود را وارد کنید"}))
