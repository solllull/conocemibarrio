import threading

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.conf import settings

from .forms import (RegistrationForm,
                    LogInForm,
                    JoinNeighborhoodForm)
from .models import Neighborhood, UserNeighborhood

UserModel = get_user_model()


class EmailThread(threading.Thread):

    def __init__(self, email_message):
        self.email_message = email_message
        threading.Thread.__init__(self)

    def run(self):
        self.email_message.send()


def home(request):
    args = {}
    if request.user.is_authenticated:
        users_neighborhoods = UserNeighborhood.objects.all()
        if users_neighborhoods is not None:
            for user_neighborhood in users_neighborhoods:
                if user_neighborhood.user == request.user:
                    args['neighborhood'] = user_neighborhood

    return render(request, 'base.html', args)


def location(request):
    return render(request, 'location.html')


def registration(request):
    args = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            if request.POST.get('barrio'):
                neighborhood_id = request.POST.get('barrio')
                n = Neighborhood.objects.get(pk=neighborhood_id)
                user_neighborhood = UserNeighborhood()
                user_neighborhood.user = user
                user_neighborhood.neighborhood = n
                user_neighborhood.save()

            current_site = get_current_site(request)
            message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            email_subject = 'Activa tu cuenta'
            to_email = form.cleaned_data.get('email')
            email_message = mail.EmailMessage(
                email_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )

            EmailThread(email_message).start()
            messages.add_message(request, messages.SUCCESS, "El link para activar tu cuenta fue enviado.")

            return HttpResponseRedirect('/')
    else:
        neighborhoods = Neighborhood.objects.filter(is_active=1)
        form = RegistrationForm()
        args['neighborhoods'] = neighborhoods
    args['form'] = form

    return render(request, 'registration.html', args)


def activation(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.signup_confirmation = True
        user.save()
        messages.success(request, 'Usuario registrado con éxito. Inicie sesion.')
        return HttpResponseRedirect('/login')
    else:
        messages.warning(request, 'Link de activacion inválido.')
        return HttpResponseRedirect('/')
    return render(request, 'base.html', {})


def logIn(request):
    args = {}
    valueNext = request.POST.get('next')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if valueNext:
                        return HttpResponseRedirect(valueNext)
                    else:
                        return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/home')
    else:
        form = LogInForm()

    args['form'] = form

    return render(request, 'login.html', args)


def logOut(request):
    logout(request)
    return HttpResponseRedirect('/')

    return render(request, 'base.html', {})


def joinNeighborhood(request):
    args = {}
    user = request.user
    if request.method == 'POST':
        form = JoinNeighborhoodForm(request.POST)

        if form.is_valid():
            if request.POST.get('barrio'):
                neighborhood_id = request.POST.get('barrio')
                n = Neighborhood.objects.get(pk=neighborhood_id)
                user_neighborhood = UserNeighborhood()
                user_neighborhood.user = user
                user_neighborhood.neighborhood = n
                user_neighborhood.save()

            return HttpResponseRedirect('/')
    else:
        neighborhoods = Neighborhood.objects.filter(is_active=1)
        form = JoinNeighborhoodForm()
        args['neighborhoods'] = neighborhoods
    args['form'] = form

    return render(request, 'join_neighborhood.html', args)
