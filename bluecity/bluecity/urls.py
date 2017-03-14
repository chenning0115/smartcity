"""bluecity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
import ourbluecity.views as views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bluecity/home$',views.gethome),
    url(r'^bluecity/analyse_time$',views.analyse_time),
    url(r'^bluecity/analyse_factor$',views.analyse_factor),
    url(r'^bluecity/decisionsupport$', views.decisionsupport),
    # url(r'^bluecity/getqualitydata', views.getresponsejson),
    url(r'^bluecity/quaryaqi$',views.quaryaqi),
    url(r'^bluecity/statetranmat$',views.getTranProData),
    # url(r'^bluecity/aqitrend/griddata$',views.getTrendGrid),
    url(r'^factorGrid/',views.getFactorGrid),
    url(r'^bluecity/bestpath$',views.bestpath),
    url(r'^blockFactor/',views.getBlockFactor),
    url(r'^bluecity/realtimefineprediction$',views.realtimefineprediction),
    url(r'^bluecity/analyse_time/statetranmat$',views.getTranProData),

    # 时间密度图
    url(r'^bluecity/analyse_time/analysis_temporaldensity$',views.analysis_temporaldensity),
    url(r'^bluecity/analyse_time/temporaldensity$',views.temporaldensity),
    url(r'^bluecity/analyse_time/yearline$',views.yearline),
    url(r'^bluecity/analyse_time/yearpie$',views.yearpie),
    url(r'^bluecity/analyse_time/analysis_aqihistory$',views.analysis_aqihistory),
    url(r'^bluecity/analyse_time/aqihistory$',views.aqihistory),
    url(r'^bluecity/analyse_time/analysis_dashboard$',views.analysis_dashboard),
    url(r'^bluecity/analyse_time/dashboard$',views.dashboard),
    url(r'^bluecity/analyse_time/analysis_duidietu1$',views.analysis_duidietu1),
    url(r'^bluecity/analyse_time/duidietu1$',views.duidietu1),
    url(r'^bluecity/analyse_factor/analysis_parallel1$',views.analysis_parallel1),
    url(r'^bluecity/analyse_factor/parallel1$',views.parallel1),
    url(r'^bluecity/analyse_factor/analysis_greycorr$',views.analysis_greycorr),
    url(r'^bluecity/analyse_factor/greycorr$',views.greycorr),
]
