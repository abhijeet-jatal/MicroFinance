from http import client
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from home.models import SanctionedLoan
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from home.models import Client

from home.models import Client, Enquiry
from users.decorators import relation_required, operational_required


# Create your views here.


def index(request):
    return render(request, 'users/index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form1 = form.save(commit=False)
            role = form.cleaned_data['role']
            print(role)
            if role == 'Operational Manager':
                form1.is_operational = True
                form1.save()
            elif role == 'Relation Manager':
                form1.is_relation = True
                form1.save()
            elif role == 'Customer':
                form1.is_customer = True
                form1.save()

            '''user = form.save()
            msg = f'{user} created'
            '''
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # print(client)

            user = authenticate(username=username, password=password)
            if user is not None and user.is_operational:
                login(request, user)
                return redirect('operational')
            elif user is not None and user.is_customer:
                login(request, user)
                client = Client.objects.filter(email_id__iexact=username)
                for i in client:
                    print(i.email_id)
                    # if i.email_id == username :
                    return redirect('customer')

                return redirect('client_url')
            elif user is not None and user.is_relation:
                login(request, user)
                return redirect('relation')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'

    return render(request, 'users/login.html', {'form': form, 'msg': msg})


@login_required
@operational_required
def operational(request):
    cli = Client.objects.all()
    enq = Enquiry.objects.all()
    sanct = SanctionedLoan.objects.all()

    context = {'client': cli, "enquiry": enq, "sanct": sanct}
    return render(request, 'users/operational.html', context)


@login_required
def customer(request):
    client = Client.objects.filter(email_id__iexact=request.user.username)

    for i in client:
        x = i.id
        sanct = SanctionedLoan.objects.filter(client_id__exact=i.id)

    context = {"client": client, "sanct": sanct, "x": x}
    return render(request, 'users/customer.html', context)


@login_required
@relation_required
def relation(request):
    cli = Client.objects.all()
    enq = Enquiry.objects.all()
    sanct = SanctionedLoan.objects.all()
    context = {'client': cli, "enquiry": enq, "sanct": sanct}

    return render(request, 'users/relation.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


"""
def layoutView(request):
    template_name = 'users/layout1.html'
    context = {}
    return render(request, template_name, context)

"""
