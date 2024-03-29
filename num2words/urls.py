# urls.py
from django.urls import path
from api.views import landing_page, num_to_english

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('num_to_english', num_to_english),
    path('test/', num_to_english, name='test_view'),
]
