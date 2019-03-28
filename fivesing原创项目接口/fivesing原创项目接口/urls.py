"""fivesing原创项目接口 URL Configuration

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
from fivesing.views import YunachuangfenleiView,YuanchuangcontentView,GedancontentinfoView,GedaninfoView,BanzoufenleiView
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^yunachuangfenlei/$',YunachuangfenleiView.as_view()),
    url(r'^yunachuangfenlei/(?P<pk>[a-zA-Z_0-9]+)/$',YunachuangfenleiView.as_view(),name='yunachuangfenleiDetail'),


    url(r'^yuanchuangcontent/$',YuanchuangcontentView.as_view()),
    url(r'^yuanchuangcontent/(?P<pk>[a-zA-Z_0-9]+)/$',YuanchuangcontentView.as_view(),name='yuanchuangcontentDetail'),

    url(r'^gedancontentinfo/$',GedancontentinfoView.as_view()),
    url(r'^gedancontentinfo/(?P<pk>[a-zA-Z_0-9]+)/$',GedancontentinfoView.as_view(),name='gedancontentinfoDetail'),

    url(r'^gedaninfo/$',GedaninfoView.as_view()),
    url(r'^gedaninfo/(?P<pk>[a-zA-Z_0-9]+)/$',GedaninfoView.as_view(),name='gedaninfoetail'),

    url(r'^banzoufenlei/$',BanzoufenleiView.as_view()),
    url(r'^banzoufenlei/(?P<pk>[a-zA-Z_0-9]+)/$',BanzoufenleiView.as_view(),name='banzoufenleiDetail')
]
