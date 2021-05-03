from django.urls import path
from .views import EBookSignupView

urlpatterns = [
    path('ebook-signup', EBookSignupView.as_view()),
]
