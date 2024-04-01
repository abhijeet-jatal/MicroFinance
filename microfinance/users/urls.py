from django.urls import path
from .views import (
    register,
    login_view,
    logout_view,
    operational,
    relation,
    customer,
    index
)

urlpatterns = [
    path('index/', index, name='index'),
    path('reg/', register, name='adduser'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('operational/', operational, name='operational'),
    path('customer/', customer, name='customer'),
    path('relation/', relation, name='relation')
]
