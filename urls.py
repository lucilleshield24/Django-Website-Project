from django.urls import path
from . import views

urlpatterns = [
    path('recent', views.recent, {'pagename': 'recent'}, name = 'recent'),
    path('', views.index, {'pagename': ''}, name = 'home'),
    path('<str:pagename>', views.index, name = 'index'),
    path('category/<str:hierarchy>', views.show_category, name = 'category'),
    ]
