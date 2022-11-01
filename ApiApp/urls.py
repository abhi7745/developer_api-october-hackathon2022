from django.urls import path

from .views import *

urlpatterns = [
    path('', api, name='api'),
    path('advocates/', advocate_list, name='advocate_list'),
    path('advocates/<str:username>/', advocate_detail, name='advocate_detail'),


    path('checker/', checker, name='checker'),
    path('advocatesclass/', AdvocatesDetail.as_view(), name='advocate_detail_class'),
]