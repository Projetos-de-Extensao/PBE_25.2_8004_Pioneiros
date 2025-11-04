from django.contrib import admin
from django.urls import path, include
from appofc.api import CadastroAlunoView
from appofc.api_urls import router
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/cadastro/', CadastroAlunoView.as_view()),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
]
