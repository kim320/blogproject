from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
  if request.method == 'POST':
      if request.POST['pwd1'] == request.POST['pwd2']:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['pwd1'])
        auth.login(request, user)
        return redirect('blog')
  return render(request, 'signup.html')

def login(request):
  if request.method == 'POST':
      username = request.POST['username']
      pwd = request.POST['pwd']
      user = auth.authenticate(request, username=username, password=pwd)
      if user is not None:
          auth.login(request, user)
          return redirect('blog')
      else:
          return render(request, 'login.html', {'error': 'username or password is incorrect.'})
        
  else:
    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('blog')
    return render(request, 'login.html')