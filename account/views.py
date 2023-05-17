from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token



from .forms import RegistrationForm
from django.shortcuts import redirect
# Create your views here.
def account_register(request):
    

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user=registerForm.save(commit=False)
            user.email=registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active=False
            user.save()

            current_site=get_current_site(request)
            subject='Activate your account'
            message=render_to_string('account/registration/account_activation_email.html',{

                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            user.email_user(subject=subject,message=message)
    else:
        registerForm=RegistrationForm()
    return render(request,'account/registration/register.html',{'form':registerForm})

            