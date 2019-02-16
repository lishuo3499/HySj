"""HySj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views as api
from consumer import views as consumer
from rest_framework.documentation import include_docs_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('uploadfile/', api.uploadfile),
    path('videoindex/', api.videoindex),

    # 用户

    path('RegistrationValidation/', consumer.RegistrationValidation),
    path('loginValidation', consumer.loginValidation),
    path('userLogout/', consumer.userLogout),
    path('ResetPassword/', consumer.ResetPassword),
    path('RegisterationCode/', consumer.RegisterationCode),  #验证码
    path('docs/', include_docs_urls(title='b'))
    
    
]
