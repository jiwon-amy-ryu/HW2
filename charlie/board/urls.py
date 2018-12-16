from django.urls import path
from .views import IndexView, DetailView, PostCreateView

urlpatterns = [
    path('', IndexView.as_view()),
    path('detail/<int:id>/', DetailView.as_view()),
    path('posts/create/', PostCreateView.as_view()),
]
