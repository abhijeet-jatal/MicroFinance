from django.shortcuts import render, redirect
from .forms import EnquiryForm, Enquiry
from django.contrib import messages
from home.models import Client
from home.forms import ClientForm
from random import randint
from .forms import DocumentsForm, Documents
from django.http import HttpResponse
from .forms import previous_loanForm, Previus_loan
from .models import Guarantor
from home.forms import GuarantorFrom
# from .forms import OccupationForm
# from .models import Occupation
from .forms import SalariedDetailsForm
from .models import Salaried_Details
from .forms import AddressForm, permenent_addrForm
from .models import Address, Permenent_Address
from .forms import Client, ClientForm
from .forms import Client, ClientForm, Bank, BankForm
from .forms import SelfemployedForm
from .models import Selfemployed
from .models import SanctionedLoan
from .forms import RSanctionedLoanModelForm, SanctionedLoanModelForm
from users.decorators import operational_relation_required
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')


def enquiry(request):
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your request has been successfully submitted, Our executive will contact you shortly')
            return redirect('base')
        else:
            # return JsonResponse({"error": True, 'errors': 'Invalid Data'})
            messages.error(request, 'Please Enter Valid Data')
    context = {'form': form}
    return render(request, 'home/enquiry.html', context)


def enquiry_data(request):
    obj = Enquiry.objects.all()
    return render(request, 'home/enquiry_data.html', {'data': obj})


'''ClientDetails'''


@login_required()
def clientView(request):
    form = ClientForm()
    template_name = "home/clientform.html"
    cibl_score = randint(300, 900)
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.cibil_score = cibl_score
            form.save()
            return redirect('address_url')

    context = {'form': form}
    return render(request, template_name, context)


def showClientView(request):
    data = Client.objects.all()
    template_name = "home/showclient.html"
    context = {'data': data}
    return render(request, template_name, context)


'''Address Details'''


@login_required()
def AddressView(request):
    form1 = AddressForm()
    form2 = permenent_addrForm()
    template_name = 'home/addressview.html'
    context = {'form1': form1, 'form2': form2}
    if request.method == 'POST':
        form1 = AddressForm(request.POST)
        form2 = permenent_addrForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()

            form2.save()

            return redirect('occupation_url')
    return render(request, template_name, context)


def showaddress(request):
    obj = Address.objects.all()
    obj1 = Permenent_Address.objects.all()
    template_name = 'home/showaddress.html'
    context = {'data': obj, 'data1': obj1}
    return render(request, template_name, context)


"""Occupation"""


@login_required()
def occupationView(request):
    template_name = "home/occupationform.html"
    context = {}
    return render(request, template_name, context)


'''OccuptionalDetails'''
"""
def occupationView(request):
    form = OccupationForm()
    template_name = 'home/occupationform.html'
    if request.method == 'POST':
        form = OccupationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('salary_url' )
    context = {'form': form}
    return render(request, template_name, context)


def showoccupationView(request):
    data = Occupation.objects.all()
    template_name = 'app1/showoccupation.html'
    context = {'data': data}
    return render(request, template_name, context)
"""

'''Salarised'''


@login_required()
def Salaried(request):
    form = SalariedDetailsForm()
    template_name = "home/salaried.html"

    if request.method == "POST":
        form = SalariedDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank_url')
    context = {'form': form}
    return render(request, template_name, context)


@login_required()
def showSalariedView(request):
    obj = Salaried_Details.objects.all()
    template_name = 'home/show_salaried.html'
    context = {'data': obj}
    return render(request, template_name, context)


@login_required()
def SelfemployedView(request):
    form = SelfemployedForm()
    template_name = 'home/selfemployedview.html'
    context = {'form': form}
    if request.method == 'POST':
        form = SelfemployedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank_url')
    return render(request, template_name, context)


@login_required()
def showselfemployed(request):
    obj = Selfemployed.objects.all()
    template_name = 'app1/showselfemployed.html'
    context = {'data': obj}
    return render(request, template_name, context)


@login_required()
def ClientView(request):
    form = ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('bank')

    template_name = 'home/client.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required()
def BankView(request):
    form = BankForm()

    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('previousloan_url')

    template_name = 'home/bankdetails.html'
    context = {'form': form}
    return render(request, template_name, context)


def ShowView(request):
    bnk = Bank.objects.all()
    template_name = 'home/show.html'
    context = {'bank': bnk}
    return render(request, template_name, context)


'''PreviousLoan'''


@login_required()
def previous_loanview(request):
    form = previous_loanForm
    template_name = 'home/pre_loan.html'

    if request.method == 'POST':
        form = previous_loanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gaurantor_url')
    context = {'form': form}
    return render(request, template_name, context)


def show_Preloanview(request):
    obj = Previus_loan.objects.all()
    temolate_name = 'home/show_preloan.html'
    context = {'data': obj}
    return render(request, temolate_name, context)


'''GuarentorDetails'''


@login_required()
def addGuarantorView(request):
    form = GuarantorFrom()
    template_name = 'home/guarantor.html'

    if request.method == "POST":
        form = GuarantorFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('documents_url')
    context = {'form': form}
    return render(request, template_name, context)


def showGuarantorView(request):
    guar = Guarantor.objects.all()
    template_name = 'home/showguarantor.html'
    context = {'guar': guar}
    return render(request, template_name, context)


def detailGuarantorView(request, id):
    guar = Guarantor.objects.get(id=id)
    template_name = 'home/detailguarantor.html'
    context = {'guar': guar}
    return render(request, template_name, context)


@login_required
@operational_relation_required
def showEnquiry(request):
    obj = Enquiry.objects.all()
    template_name = 'app1/showenquiry.html'
    context = {'data': obj}
    return render(request, template_name, context)


'''DocumentDetails'''


@login_required()
def create_client(request):
    form = ClientForm()
    template_name = 'client/addclient.html'

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('showclient')
    context = {'form': form}
    return render(request, template_name, context)


@login_required
@operational_relation_required
def show_client(request):
    client = Client.objects.all()
    template_name = 'client/showclient.html'
    context = {'client': client}
    return render(request, template_name, context)


@login_required()
def create_document_view(request):
    form = DocumentsForm()
    template_name = 'home/documents.html'

    if request.method == 'POST':
        form = DocumentsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            if request.user is not None and request.user.is_customer:
                return redirect('customer')

            elif request.user is not None and request.user.is_relation:
                return redirect('relation')

            return redirect('base')

    return render(request, template_name, {'form': form})


"""Santioned Loan"""


@login_required()
def create_sanctionedoan_view(request, i):
    customer = Client.objects.get(id=i)
    form = RSanctionedLoanModelForm(initial={'customer': customer})
    if request.user.is_operational == True:
        form = SanctionedLoanModelForm()
    if request.method == 'POST':
        form = RSanctionedLoanModelForm(request.POST)
        if request.user.is_operational == True:
            form = SanctionedLoanModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')
    template_name = 'home/sanctioned_loan.html'
    context = {'form': form}
    return render(request, template_name, context)


def show_sanctionedoan_view(request):
    sanction_obj = SanctionedLoan.objects.all()
    template_name = 'home/show_sanctioned_loan.html'
    context = {'sanction_obj': sanction_obj}
    return render(request, template_name, context)


@login_required
@operational_relation_required
def update_sanctionedoan_view(request, i):
    sanction_obj = SanctionedLoan.objects.get(id=i)
    form = SanctionedLoanModelForm(instance=sanction_obj)
    if request.method == 'POST':

        form = SanctionedLoanModelForm(request.POST, instance=sanction_obj)
        if form.is_valid():
            form.save()
            loan = SanctionedLoan.objects.get(id=i)
            loan.is_approved = True
            loan.emi = calculate_emi(loan)
            print(loan)
            print(loan.is_approved)
            loan.save()
            return redirect('operational')
    template_name = 'home/sanctioned_loan.html'
    context = {'form': form}
    return render(request, template_name, context)


def get_data(loan):
    data = {
        "app_no": loan.customer.id,
        "amount": loan.approved_loan,
        "interest": loan.interest,
        "tenure": loan.tenure,
        "emi": loan.emi,
        "email": loan.customer.email,
        "mobile": loan.customer.mobile,
        "name": loan.customer.full_name,
    }
    return data


def calculate_emi(loan):
    print(loan.tenure)
    tenure = loan.tenure
    interest = loan.interest / 12 / 100
    amount = loan.approved_loan
    i = (interest + 1) ** tenure
    p = i - 1.0
    emi = amount * interest * (i / p)
    emi = round(emi, 2)
    return emi


@login_required
@operational_relation_required
def delete_sanctioned(request, id):
    data = SanctionedLoan.objects.get(id=id)
    data.delete()
    return redirect("operational")
