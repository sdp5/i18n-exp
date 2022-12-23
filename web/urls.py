"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import (
    SPECParseReportsView, CompTransPkgingView, SBSizeCountReportsView,
    WSSizeCountReportsView, SRVSizeCountReportsView, RHConfigPatchReportsView,
    GettextReportsView, SOSSummaryView, GettextComparisonReportsView
)

report_urls = [
    path('translation-packages', SPECParseReportsView.as_view(), name="reports-trans-pkg"),
    path('translation-packaging', CompTransPkgingView.as_view(), name="comp-trans-pkg"),
    path('size-count/sb', SBSizeCountReportsView.as_view(), name="reports-size-count-sb"),
    path('size-count/ws', WSSizeCountReportsView.as_view(), name="reports-size-count-ws"),
    path('size-count/srv', SRVSizeCountReportsView.as_view(), name="reports-size-count-srv"),
    path('patch/rh-rpm-config', RHConfigPatchReportsView, name="reports-rh-config-patch"),
    path('gettext/deps', GettextReportsView.as_view(), name="reports-gettext"),
    path('gettext/comp', GettextComparisonReportsView.as_view(), name="reports-gettext-comparison"),
]

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('localization', TemplateView.as_view(template_name="localization.html"), name="localization"),
    path('packaging', TemplateView.as_view(template_name="rpm-sub-pkg.html"), name="sub-pkg"),
    path('ux', TemplateView.as_view(template_name="ux.html"), name="ux"),
    path('gettext', TemplateView.as_view(template_name="gettext.html"), name="gettext"),
    path('sos', SOSSummaryView.as_view(), name="sos"),
    path('reports/', include(report_urls)),
    path('admin/', admin.site.urls),
]
