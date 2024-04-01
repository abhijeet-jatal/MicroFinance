from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='base'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('enquiry_data/', views.enquiry_data, name='enquiry_data'),

    path('cv/', views.clientView, name='client_url'),
    path('av/', views.AddressView, name='address_url'),
    path('ov/', views.occupationView, name='occupation_url'),
    path('sv/', views.Salaried, name='salary_url'),
    path('se/', views.SelfemployedView, name='selfemployed_url'),
    path('bank/', views.BankView, name='bank_url'),
    path('pl/', views.previous_loanview, name='previousloan_url'),
    path('gv/', views.addGuarantorView, name='gaurantor_url'),
    path('dv/', views.create_document_view, name='documents_url'),
    path('showsanctionloan/', views.show_sanctionedoan_view, name='show_sanction'),
    path('create/<int:i>/', views.create_sanctionedoan_view, name='create_sanction'),
    path('updatesanctionloan/<int:i>/', views.update_sanctionedoan_view, name='update_sanction'),
    path('deletesanction/<int:id>/', views.delete_sanctioned, name="delete_sanctioned"),
]
