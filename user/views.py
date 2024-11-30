from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, views, authenticate
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView

from django.utils.decorators import method_decorator
from .forms import UserRegistrationForm, UserLoginForm, UserEditForm
from .models import User


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('landing_page')

    def form_valid(self, form):
        # Save user and hash the password
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return redirect(self.success_url)


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'user/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(data=request.POST)

        form.errors.clear()

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing_page')
            else:
                form.add_error(None, "Invalid username or password.")

        return render(request, 'user/login.html', {'form': form})


@method_decorator(views.login_required, name='dispatch')
class UserEditView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'user/profile_edit.html'
    success_url = reverse_lazy('user:profile')

    def get_object(self):
        return self.request.user


@views.login_required
def logout_view(request):
    logout(request)
    return redirect('landing_page')


@views.login_required
def user_profile(request):
    return render(request, 'user/profile_detail.html', {'user': request.user})


@views.login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('landing_page')
    return render(request, 'user/profile_delete.html')
