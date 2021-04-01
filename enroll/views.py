from django.shortcuts import render
from enroll.forms import LoginForm

# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        fm=LoginForm(request.POST)
        if fm.is_valid():
            print('Form Validated')
            print('Name:',fm.cleaned_data['name'])
            print('Password:',fm.cleaned_data['password'])
            print('Re-type-password',fm.cleaned_data['rpassword'])
    else:
            fm=LoginForm()    
    
    return render(request,'enroll/loginform.html',{'form':fm})

