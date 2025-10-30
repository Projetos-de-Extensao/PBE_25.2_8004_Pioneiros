
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('.api_urls')),  # URLs da API

]

# usuario: admin3
# senha: 123456