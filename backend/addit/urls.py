from django.urls import path
from django.conf import settings

from addit.views import LandingPage, LoginView, LogoutView, QuoteView, custom_page_not_found

app_name = "addit"

urlpatterns = [
    path("", LandingPage.as_view(), name="landing-page"),
    path("quote/<slug:slug>/", QuoteView.as_view(), name="quote-detail"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]

if settings.DEBUG:
    urlpatterns += [path("error/", custom_page_not_found, name="error")]
