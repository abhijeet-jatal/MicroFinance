from django import forms
from home.models import Enquiry
from .models import Client
from .models import Guarantor
from .models import Previus_loan

from .models import Salaried_Details
from .models import Address, Permenent_Address
from .models import Bank
from .models import Selfemployed
from .models import Documents, SanctionedLoan

'''ClientDetails'''


class DateInput(forms.DateInput):
    input_type = 'date'


class ClientForm(forms.ModelForm):
    gender = (
        ('male', "MALE"),
        ('female', "FEMALE"),
        ('other', "OTHER"),
    )

    gender = forms.ChoiceField(choices=gender, widget=forms.RadioSelect(), label="GENDER")

    class Meta:
        model = Client
        exclude = ['status', 'cibil_score']
        widgets = {
            # "client_id": forms.TextInput(attrs={'placeholder': "ex.1"}),
            "date_of_birth": DateInput(),
            "first_name": forms.TextInput(attrs={'placeholder': "ex.Akshay"}),
            "middle_name": forms.TextInput(attrs={'placeholder': "ex.Vijay"}),
            "last_name": forms.TextInput(attrs={'placeholder': "ex.Sharma"}),
            "fathers_full_name": forms.TextInput(attrs={'placeholder': "ex.Vijay Raj Sharma"}),
            "spouse_name": forms.TextInput(attrs={'placeholder': "ex.Anushka Akshay Sharma"}),
        }
        labels = {
            # "client_id": "CLIENT ID",
            "first_name": "FIRST NAME",
            "middle_name": "MIDDLE NAME",
            "last_name": "LAST NAME",
            "fathers_full_name": "FATHER'S FULL NAME",
            "date_of_birth": "DATE OF BIRTH",
            "gender": "GENDER",
            "maritual_status": "MARITUAL STATUS",
            "spouse_name": "SPOUSE NAME",
            "email_id": "EMAIL ID",
            "aadhar_number": "AADHAR NUMBER",
            "pan_number": "PAN NUMBER",
            "contact_no": "CONTACT NUMBER",
            "alternate_contact_no": "ALTERNATE CONTACT NUMBER",
            # "loan_amount": "LOAN AMOUNT",
            "occupation": "OCCUPATION",
            "annual_income": "ANNUAL INCOME",
            "cibil_score": "CIBIL SCORE",
            "status": "STATUS",
        }

    def clean_maritual_status(self):
        select_marry = self.cleaned_data['maritual_status']
        if select_marry == "select":
            raise forms.ValidationError("Please Select Maritual status Options")
        return select_marry

    def clean_occupation(self):
        select_occp = self.cleaned_data['occupation']
        if select_occp == "select":
            raise forms.ValidationError("Please Select Occupation Options")
        return select_occp

    def clean_aadhar_number(self):
        aadhar = self.cleaned_data['aadhar_number']
        if aadhar < 1 or len(str(aadhar)) != 12:
            raise forms.ValidationError('Please Enter Valid Addhar Number')
        return aadhar

    def clean_pan_number(self):
        pan = self.cleaned_data['pan_number']
        if len(pan) != 10:
            raise forms.ValidationError('Please Enter Valid Pan Number')
        return pan


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'

        labels = {
            'first_name': 'FIRST NAME ',
            'middle_name': 'MIDDLE NAME',
            'last_name': ' LAST NAME',
            'email_id': ' EMAIL ID',
            'contact_no': 'MOBILE NUMBER',
            'loan_amount': 'LOAN AMOUNT',
            'Occuption': 'OCCUPTION',
            'Pan_number': 'PANCARD NUMBER'

        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name ', 'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'placeholder': ' Middle Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': ' Last Name', 'class': 'form-control'}),
            'email_id': forms.TextInput(attrs={'placeholder': ' @gmail.com', 'class': 'form-control'}),
            'contact_no': forms.NumberInput(attrs={'placeholder': ' Mobile Number', 'class': 'form-control'}),
            'loan_amount': forms.NumberInput(attrs={'placeholder': ' Loan Amount', 'class': 'form-control'}),
            'Pan_number': forms.TextInput(attrs={'placeholder': ' Pancard No', 'class': 'form-control'}),
        }

    def clean_first_name(self):
        n1 = self.cleaned_data['first_name']
        var = n1.istitle()
        if var != True:
            raise forms.ValidationError('First letter should be Capital')
        return n1

    def clean_middle_name(self):
        n2 = self.cleaned_data['middle_name']
        a = n2.istitle()
        if a != True:
            raise forms.ValidationError('Middle name First letter should be Capital')
        return n2

    def clean_last_name(self):
        n2 = self.cleaned_data['last_name']
        a = n2.istitle()
        if a != True:
            raise forms.ValidationError(' First letter should be Capital')
        return n2

    def clean_Pan_number(self):
        pan = self.cleaned_data['Pan_number']
        if len(pan) != 10:
            raise forms.ValidationError('Please Enter Valid Pan Number')
        return pan

    def clean_contact_no(self):
        no = self.cleaned_data['contact_no']
        if len(str(no)) != 10:
            raise forms.ValidationError('Please Enter Valid Pan Number')
        return no


'''AddressDetails'''


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

        labels = {
            'address_line1': 'ADDRESS LINE1',
            'address_line2': 'ADDRESS LINE2',
            'city': 'CITY',
            'pincode': 'PINCODE',
            'landmark': 'LANDMARK',
            'district': 'DISTRICT',
            'state': 'STATE',
            'country': 'COUNTRY',
        }

        widgets = {
            'address_line1': forms.TextInput(
                attrs={
                    'placeholder': 'eg.LINE1 ADDRESS'
                }
            ),
            'address_line2': forms.TextInput(
                attrs={
                    'placeholder': 'eg.LINE2 ADDRESS'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'eg.KARVE-NAGAR,PUNE'
                }
            ),
            'pincode': forms.NumberInput(
                attrs={
                    'placeholder': 'eg.413212'
                }
            ),
            'landmark': forms.TextInput(
                attrs={
                    'placeholder': 'eg.NEAR CITYMALL,PUNE'
                }
            ),
            'district': forms.TextInput(
                attrs={
                    'placeholder': 'eg.PUNE'
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'placeholder': 'eg.MAHARASHTRA'
                }
            ),
            'country': forms.TextInput(
                attrs={
                    'placeholder': 'eg.India'
                }
            )

        }


class permenent_addrForm(forms.ModelForm):
    class Meta:
        model = Permenent_Address
        fields = '__all__'

        labels = {
            'paddress_line1': 'ADDRESS LINE1',
            'paddress_line2': 'ADDRESS LINE2',
            'pcity': 'CITY',
            'ppincode': 'PINCODE',
            'plandmark': 'LANDMARK',
            'pdistrict': 'DISTRICT',
            'pstate': 'STATE',
            'pcountry': 'COUNTRY',
        }

        widgets = {
            'paddress_line1': forms.TextInput(
                attrs={
                    'placeholder': 'eg.LINE1 ADDRESS'
                }
            ),
            'paddress_line2': forms.TextInput(
                attrs={
                    'placeholder': 'eg.LINE2 ADDRESS'
                }
            ),
            'pcity': forms.TextInput(
                attrs={
                    'placeholder': 'eg.KARVE-NAGAR,PUNE'
                }
            ),
            'ppincode': forms.NumberInput(
                attrs={
                    'placeholder': 'eg.413212'
                }
            ),
            'plandmark': forms.TextInput(
                attrs={
                    'placeholder': 'eg.NEAR CITYMALL,PUNE'
                }
            ),
            'pdistrict': forms.TextInput(
                attrs={
                    'placeholder': 'eg.PUNE'
                }
            ),
            'pstate': forms.TextInput(
                attrs={
                    'placeholder': 'eg.MAHARASHTRA'
                }
            ),
            'pcountry': forms.TextInput(
                attrs={
                    'placeholder': 'eg.India'
                }
            )

        }


'''OccuptionalDetails'''
"""
class OccupationForm(forms.ModelForm):
    class Meta:
        model = Occupation
        fields = "__all__"
        labels = {
            'company_type': 'COMPANY TYPE',
            'company_name': 'COMPANY NAME',
            'company_address': 'COMPANY ADDRESS',
            'Employment_type': 'EMPLOYMENT TYPE',
            'profile': 'PROFILE',
            'experience': 'EXPERIENCE'
        }

    def clean_experience(self):
        exp = self.cleaned_data['experience']
        exp = int(exp)
        if exp < 0:
            raise forms.ValidationError('experience is not in negative no .ex -1')
        return exp

"""

'''salaried'''


class SalariedDetailsForm(forms.ModelForm):
    class Meta:
        model = Salaried_Details
        fields = "__all__"

        labels = {
            'Designation': 'DESIGNATION',
            'Experience': 'EXPERIENCE',
            'Joining_Date': 'JOINING DATE',
            'Monthly_Income': 'MONTHLY INCOME',
            'Company_Name': 'COMPANY NAME',
            'Company_Address': 'COMPANY ADDRESS'

        }
        widgets = {
            'Designation': forms.TextInput(
                attrs={
                    'placeholder': 'student',

                }
            ),
            'Experience': forms.NumberInput(
                attrs={
                    'placeholder': '3'
                }
            ),
            'Joining_Date': forms.DateInput(
                attrs={
                    'placeholder': '2/03/2022'
                }
            ),
            'Monthly_Income': forms.NumberInput(
                attrs={
                    'placeholder': 'eg-200000 '
                }
            ),
            'Company_Name': forms.TextInput(
                attrs={
                    'placeholder': 'xyz'
                }
            ),
            'Company_Address': forms.TextInput(
                attrs={
                    'placeholder': 'Karvenagar, Pune, 440024'
                }
            )

        }


class SelfemployedForm(forms.ModelForm):
    class Meta:
        model = Selfemployed
        fields = '__all__'

        labels = {
            'firm_type': 'FIRM TYPE',
            'firm_name': 'FIRM NAME',
            'address': 'ADDRESS',
            'annual_turnover': 'ANNUAL TURNOVER',
            'gst_no': 'GST NO'
        }


'''Bank Details'''


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'
        labels = {
            'cid': 'Client',
            'bname': 'BANK NAME',
            'aname': 'ACCOUNT HOLDER NAME',
            'anum': 'Account Number',
            'confirmanum': 'Confirm Account Number',
            'atype': 'Account Type',
            'ifsc': 'IFSC Code',
            'brname': 'Branch Name',
            'brcode': 'Branch Code'
        }


'''PreviousLoanDetails'''


class previous_loanForm(forms.ModelForm):
    class Meta:
        model = Previus_loan
        fields = '__all__'
        labels = {
            'client': 'CLIENT ',
            'loan_type': 'LOAN TYPE',
            'loan_amount': ' LOAN AMOUNT',
            'account_number': ' YOUR ACCOUNT NUMBER',
            'finance_bank': 'BANK NAME',
            'tenure': 'TENURE'
        }

        widgets = {
            # 'client':forms.TextInput(attrs={'placeholder':'Client ','class':'form-control'}),
            'loan_amont': forms.TextInput(attrs={'placeholder': ' Your your amount', 'class': 'form-control'}),
            'aacount_number': forms.TextInput(attrs={'placeholder': ' Your Account Number', 'class': 'form-control'}),
            'finance_bank': forms.TextInput(attrs={'placeholder': ' Bank Number', 'class': 'form-control'}),
        }


'''Guarentor'''


class DateInput(forms.DateInput):
    input_type = 'date'


class GuarantorFrom(forms.ModelForm):
    class Meta:
        model = Guarantor
        fields = '__all__'

        labels = {
            'full_name': 'GUARANTOR FULL NAME',
            'date_of_birth': 'DATE OF BIRTH',
            'address_line1': 'ADDRESS LINE 1',
            'address_line2': 'ADDRESS LINE 2',
            'city': 'CITY',
            'state': 'STATE',
            'pin_code': 'PINCODE',
            'gender': 'GENDER',
            'designation': 'DASIGNATION',
            'company_name': 'COMPANY NAME',
            'company_address': 'COMPANY ADDRESS',
            'experience': 'WORK EXPERIENCE',
            'salary_slip': 'SALARY SLIP',
            'photo': 'GUARANTOR PHOTO',
            'pan': 'UPLOAD PAN IMAGE',
            'aadhar': 'UPLOAD AADHAR IMAGE',
            'bank_statement': 'UPLOAD BANK STATEMENT',
            'declaration': 'UPLOAD DICLARATION'
        }

        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'eg. Joe Biden'
                }
            ),
            'date_of_birth': DateInput(),

            'address_line1': forms.TextInput(
                attrs={
                    'placeholder': 'House no. ,Street name'
                }
            ),
            'address_line2': forms.TextInput(
                attrs={
                    'placeholder': 'Area/village/city'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'eg. Nagpur'
                }
            ),
            'designation': forms.TextInput(
                attrs={
                    'placeholder': 'eg. Manager'
                }
            ),
            'company_name': forms.TextInput(
                attrs={
                    'placeholder': 'eg. TCS'
                }
            ),
            'company_address': forms.TextInput(
                attrs={
                    'placeholder': 'eg. MIHAN, Nagpur'
                }
            ),
            'experience': forms.NumberInput(
                attrs={
                    'placeholder': 'eg. 1 '
                }
            ),
            'pin_code': forms.NumberInput(
                attrs={
                    'placeholder': 'eg. 441005 '
                }
            )
        }

    def clean_experience(self):
        exp = self.cleaned_data['experience']
        exp = int(exp)
        if exp < 1:
            raise forms.ValidationError('experience is not in negative no .ex -1')
        return exp

    def clean_full_name(self):
        name = self.cleaned_data['full_name']
        var = name.istitle()
        if var != True:
            raise forms.ValidationError('First alphabet should be in capital ')
        return name

    def clean_pin_code(self):
        pin = self.cleaned_data['pin_code']
        if len(str(pin)) != 6:
            raise forms.ValidationError('Enter Valid pin code')
        return pin


'''DocumentDetails'''


class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = '__all__'


"""Sanctioned Loan"""


class RSanctionedLoanModelForm(forms.ModelForm):
    class Meta:
        fields = ['client', 'required_loan']
        model = SanctionedLoan
        labels = {
            "required_loan": "Required Loan",
        }


class SanctionedLoanModelForm(forms.ModelForm):
    class Meta:
        fields = ['client', 'required_loan', 'approved_loan', 'tenure', 'interest']
        model = SanctionedLoan
        labels = {
            "required_loan": "Required Loan",
            "approved_loan": "Approved Loan",
            "tenure": "Tenure(in months)",
            "interest": "Interest Rate(annual)",
            "emi": "EMI",
            "is_approved": "Approval",
        }

    def clean_approved_loan(self):
        approved_loan = self.cleaned_data['approved_loan']
        if approved_loan <= 50000:
            raise forms.ValidationError('Approved Loan should be Greater than 50000')
        elif approved_loan > 1500000:
            raise forms.ValidationError('Approved Loan should not be Greater than 15 Lacs')
        else:
            return approved_loan

    def clean_tenure(self):
        tenure = self.cleaned_data['tenure']
        if tenure <= 12:
            raise forms.ValidationError('Tenure should be Greater than 12 months')
        elif tenure > 60:
            raise forms.ValidationError('Tenure should not be Greater than 60 months')
        else:
            return tenure

    def clean_interest(self):
        interest = self.cleaned_data['interest']
        if interest <= 10.49:
            raise forms.ValidationError('interest should be Greater than 10.49%')
        elif interest > 24:
            raise forms.ValidationError('Interest should not be Greater than 24%')
        else:
            return interest
