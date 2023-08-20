from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import ProfileForm
from .models import Profile

class HomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
           return redirect('profiles')
        return render(request, 'index.html')

    
@method_decorator(login_required, name='dispatch')
class ProfileListView(View):
    def get(self, request, *args, **kwargs):
        profile = request.user.profiles.all()
        context = {
            'profiles': profile,
        }
        return render(request, 'profileList.html', context)


@method_decorator(login_required, name='dispatch')
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        context = {
                'form': form,
            }
        return render(request, 'profileCreate.html', context)
    

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            profile = Profile.objects.create(form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)

                return redirect('profiles')
        context = {
                'form': form,
            }
        return render(request, 'profileCreate.html', context)