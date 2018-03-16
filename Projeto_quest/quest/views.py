from django.shortcuts import render
from quest.forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def register(request):

    if request.method == 'POST':

        user_form = UserForm( data=request.POST )

        if user_form.is_valid():

            user = user_form.save()

            user.set_password( user.password )
            user.save()
            return HttpResponseRedirect('/quest/')
        else:
            print( user_form.errors )

    else:
        user_form = UserForm()

    return render( request, 'quest/register.html',
                   {'user_form': user_form} )


def home(request):
    return render( request, 'quest/home.html' )

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            login(request,user)
            return HttpResponseRedirect('/quest/')


    else:

        return render(request,'quest/login.html',{})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/quest/')