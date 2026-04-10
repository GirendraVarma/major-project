"""crypto_currency_market_financial_risk_management  URL Configuration

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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.contrib import admin
from Remote_User import views as remoteuser
from crypto_currency_market_financial_risk_management  import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static


from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', remoteuser.login, name="login"),  # Removed regex (^$)
    path('Register1/', remoteuser.Register1, name="Register1"),
    path('predict_crypto_currency_financial_risk_type/', remoteuser.predict_crypto_currency_financial_risk_type, name="predict_crypto_currency_financial_risk_type"),
    path('ViewYourProfile/', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    path('serviceproviderlogin/', serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    path('View_Remote_Users/', serviceprovider.View_Remote_Users, name="View_Remote_Users"),
    re_path(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts, name="charts"),  # This requires regex, so keep re_path
    re_path(r'^charts1/(?P<chart_type>\w+)', serviceprovider.charts1, name="charts1"),  # This requires regex
    re_path(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),  # This requires regex
    path('Find_Crypto_Currency_Financial_Risk_Type_Ratio/', serviceprovider.Find_Crypto_Currency_Financial_Risk_Type_Ratio, name="Find_Crypto_Currency_Financial_Risk_Type_Ratio"),
    path('Train_Test_DataSets/', serviceprovider.Train_Test_DataSets, name="Train_Test_DataSets"),
    path('View_Prediction_Crypto_Currency_Financial_Risk_Type/', serviceprovider.View_Prediction_Crypto_Currency_Financial_Risk_Type, name="View_Prediction_Crypto_Currency_Financial_Risk_Type"),
    path('Download_Trained_DataSets/', serviceprovider.Download_Trained_DataSets, name="Download_Trained_DataSets"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

