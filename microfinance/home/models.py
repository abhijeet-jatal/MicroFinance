from django.db import models
from django.core.validators import FileExtensionValidator

loan = (
    ('PERSONAL LOAN', 'PERSONAL LOAN'),
    ('EDUCATION LOAN', 'EDUCATION LOAN'),
    ('CAR LOAN', 'CAR LOAN'),
    ('PROPERTY LOAN', 'PROPERTY LOAN'),
)

TYPES = (
    ('self employed', 'SELF EMPLOYED'),
    ('salaried', 'SALARIED'),

)


class Enquiry(models.Model):
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email_id = models.EmailField()
    contact_no = models.CharField(max_length=10)
    loan_amount = models.FloatField()
    Occupation = models.CharField(max_length=40, choices=TYPES, default=None)
    Pan_number = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


class Client(models.Model):
    married_status = (
        ('select', "SELECT OPTION"),
        ('married', "MARRIED"),
        ('unmarried', "NOT MARRIED"),
    )
    """
    occupation = (
        ('select', "SELECT OPTION"),
        ('salary',"SALARIED"),
        ('selfemployed',"SELF EMPLOYED"),
    )
    """

    # id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    # client_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fathers_full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    maritual_status = models.CharField(max_length=15, choices=married_status, default="select")
    spouse_name = models.CharField(max_length=100, null=True, blank=True)
    email_id = models.EmailField()
    aadhar_number = models.BigIntegerField(unique=True)
    pan_number = models.CharField(unique=True, max_length=100)
    contact_no = models.CharField(max_length=10)
    alternate_contact_no = models.CharField(max_length=10, null=True, blank=True)
    # loan_amount = models.FloatField()
    # occupation = models.CharField(max_length=20, choices=occupation, default="select")
    annual_income = models.FloatField()
    cibil_score = models.CharField(max_length=100, default=" ")
    status = models.CharField(max_length=100, default=" ")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


'''AddressDetails'''


class Address(models.Model):
    address_line1 = models.CharField(max_length=60)
    address_line2 = models.CharField(max_length=60)
    city = models.CharField(max_length=40)
    pincode = models.IntegerField()
    landmark = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.address_line1}--{self.address_line2}--{self.city}--{self.pincode}--{self.landmark}--{self.district}--{self.state}--{self.country}'


class Permenent_Address(models.Model):
    paddress_line1 = models.CharField(max_length=60)
    paddress_line2 = models.CharField(max_length=60)
    pcity = models.CharField(max_length=40)
    ppincode = models.IntegerField()
    plandmark = models.CharField(max_length=40)
    pdistrict = models.CharField(max_length=40)
    pstate = models.CharField(max_length=40)
    pcountry = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.paddress_line1}--{self.paddress_line2}--{self.pcity}--{self.ppincode}--{self.plandmark}--{self.pdistrict}--{self.pstate}--{self.pcountry}'


'''OccuptionalDetails'''

"""
class Occupation(models.Model):
    TYPES = (
        ('SELECT','SELECT OPTION'),
        ('PRIVATE LIMITED COMPONY', 'PRIVATE LIMITED COMPONY'),
        ('PATNERSHIP', 'PATNERSHIP'),
        ('SOLE PROPRIETORSHIP', 'SOLE PROPRIETORSHIP'),
        ('PUBLIC LIMITED COMPANY', 'PUBLIC LIMITED COMPANY'),
        ('LIMITED LIABLITY COMPANY', 'LIMITED LIABLITY COMPANY'),
        ('JOIN VENTURE', 'JOIN VENTURE'),
    )
    company_type = models.CharField(choices= TYPES,default=None,max_length=100)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    employee = (
         ('SELECT','SELECT OPTION'),
         ('FULL TIME','FULL TIME'),
         ('PART TIME','PART TIME'),
         ('GOVERMENT EMPLOYEE','GOVERMENT EMPLOYEE')
    )
    Employment_type =models.CharField(choices=employee,default=None,max_length=100)
    profile = models.CharField(max_length=100)
    experience = models.IntegerField()
    address= models.OneToOneField(Address,on_delete=models.CASCADE ,primary_key=True)

    def __str__(self):
        return self.company_name

"""

'''SalarisedDetails'''


class Salaried_Details(models.Model):
    Designation = models.CharField(max_length=50, default=None, null=True)
    Experience = models.IntegerField(default=None, null=True)
    # Joining_Date = models.DateField(default=True, null=True)
    Monthly_Income = models.IntegerField(default=None, null=True)
    Company_Name = models.CharField(max_length=100, default=None, null=True)
    Company_Address = models.CharField(max_length=500, default=None, null=True)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.Designation


class Selfemployed(models.Model):
    firm_type = models.CharField(max_length=40, default=None, null=True)
    firm_name = models.CharField(max_length=40, default=None, null=True)
    address = models.CharField(max_length=60, default=None, null=True)
    annual_turnover = models.BigIntegerField(default=None, null=True)
    gst_no = models.IntegerField(default=None, null=True)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.firm_name


'''Bank Details'''


class Bank(models.Model):
    Account_Type_Choises = (('Saving Account', 'Saving Account'),
                            ('Current Account', 'Current Account'),
                            ('Demat Account', 'Demat Account'))

    # cid = models.OneToOneField(Client, on_delete=models.CASCADE)
    bname = models.CharField(max_length=200)
    aname = models.CharField(max_length=200)
    anum = models.IntegerField()
    confirmanum = models.IntegerField()
    atype = models.CharField(max_length=200, choices=Account_Type_Choises)
    ifsc = models.CharField(max_length=200)
    brname = models.CharField(max_length=200)
    brcode = models.CharField(max_length=200)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.bname


'''Previous Loan Model'''


class Previus_loan(models.Model):
    # client = models.CharField(max_length=40)
    loan = (
        ('PERSONAL LOAN', 'PERSONAL LOAN'),
        ('EDUCATION LOAN', 'EDUCATION LOAN'),
        ('CAR LOAN', 'CAR LOAN'),
        ('PROPERTY LOAN', 'PROPERTY LOAN'),
    )
    loan_type = models.CharField(max_length=40, choices=loan, default=None, )
    loan_amount = models.CharField(max_length=40)
    account_number = models.IntegerField()
    finance_bank = models.CharField(max_length=100)
    tenure = models.CharField(max_length=100)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.client},{self.loan_type},{self.loan_amount},{self.account_number},{self.finance_bank},{self.tenure}'


state_choices = (
    ('select state', 'select state'),
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh ", "Arunachal Pradesh "),
    ("Assam", "Assam"), ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Delhi", "Delhi"),
    ("Goa", "Goa"), ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir ", "Jammu and Kashmir "),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Ladakh", "Ladakh"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"),
    ("Daman and Diu", "Daman and Diu"),
    ("Lakshadweep", "Lakshadweep"),
    ("Puducherry", "Puducherry")
)
gender_choice = (
    ('select gender', 'select gender'),
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
)


class Guarantor(models.Model):
    full_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=150)
    state = models.CharField(choices=state_choices, default='select state', max_length=150, null=True)
    pin_code = models.IntegerField()
    gender = models.CharField(choices=gender_choice, default='select gender', max_length=20, null=True)
    # designation = models.CharField(max_length=150)
    # company_name = models.CharField(max_length=150)
    # company_address = models.CharField(max_length=250)
    # experience = models.IntegerField()
    # salary_slip = models.FileField(null=True, default='gb salary slip',validators=[FileExtensionValidator( ['pdf'] ) ])
    photo = models.ImageField()
    pan = models.ImageField()
    aadhar = models.ImageField()
    # bank_statement = models.FileField(null=True,default='gb statement', validators=[FileExtensionValidator( ['pdf'] ) ])
    declaration = models.FileField(null=True, default='gb decleration', validators=[FileExtensionValidator(['pdf'])])
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.full_name}'


'''DocumentDetails'''

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)
STATUS = (
    ("Married", "Married"),
    ("Unmarried", "Unmarried"),
)
RELIGION = (
    ("Hinduism", "Hinduism"),
    ("Islam", "Islam"),
    ("Christianity", "Christianity"),
    ("Sikhism", "Sikhism"),
    ("Other", "Other"),
)


class Documents(models.Model):
    pan_card = models.FileField(upload_to='files', default='pancard')
    aadhar_card = models.FileField(upload_to='files', default='adhar card')
    # voter_id = models.FileField(upload_to='files', default='voter card')
    bank_statment = models.FileField(upload_to='files', default='bank statement')
    photo = models.ImageField(upload_to='image', default='photo')
    signature = models.ImageField(upload_to='image', default='sign_image')
    salary_slip = models.FileField(upload_to='files', default='salary')
    # bank_noc = models.FileField(upload_to='files', default='bank_noc')
    declaration = models.FileField(upload_to='files', default='declaration')
    # loan_agreement = models.FileField(upload_to='files', default='loan agreement')
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.pan_card}'


"""Sanctioned Loan"""


class SanctionedLoan(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    required_loan = models.IntegerField(default=None)
    approved_loan = models.IntegerField(null=True)
    tenure = models.IntegerField(null=True)
    interest = models.FloatField(null=True)
    emi = models.FloatField(null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client}"
