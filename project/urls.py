"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from .view import CategoryAutocompleteView, PostAutocompleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^categories-autocomplete/$', CategoryAutocompleteView.as_view(),
        name='autocomplete_category_list'),
    url(r'^posts-autocomplete/$', PostAutocompleteView.as_view(),
        name='autocomplete_post_list'),
]
