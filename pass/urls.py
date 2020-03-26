from django.urls import path
from .views import PassView,PassCreateView,PassUpdateView,PassDeleteView

urlpatterns = [
    path('',PassView.as_view(),name="pass_list"),
    path('new/',PassCreateView.as_view(),name="pass_create"),
    path('update/<int:pk>',PassUpdateView.as_view(),name="pass_update"),
    path('delete/<int:pk>',PassDeleteView.as_view(),name="pass_delete"),
]
