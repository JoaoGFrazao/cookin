from django.urls import path, include
from usuarios.views import login, cadastro, logout

urlpatterns =[
    path("cadastro", cadastro, name='cadastro'),
    path("login", login, name='login'),
    path("logout", logout, name='logout'),
    # path('', include('usuarios.urls')),
    # path('accounts/', include('allauth.urls')),
]
