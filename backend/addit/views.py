from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.db.models.functions import Lower
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.defaults import page_not_found
from django.views.generic import DetailView, ListView

from addit.models import Quote


class RandomQuoteMixin:
    @staticmethod
    def post(*args, **kwargs):
        quote = Quote().get_random_quote()
        return redirect("addit:quote-detail", quote.slug)


class LandingPage(LoginRequiredMixin, RandomQuoteMixin, ListView):
    template_name = "addit/index.html"
    login_url = reverse_lazy("addit:login")
    queryset = Quote.objects.none()

    def get_queryset(self):
        if {"search", "filter"} <= self.request.GET.keys():
            if self.request.GET.get("filter") in ["content", "topic", "handle"]:
                qs_filter = {f'{self.request.GET.get("filter")}__icontains': self.request.GET.get("search")}
                return Quote.visible.filter(**qs_filter).order_by(Lower("topic"))


class LoginView(DjangoLoginView):
    template_name = "addit/login.html"


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy("addit:landing-page")


class QuoteView(LoginRequiredMixin, RandomQuoteMixin, DetailView):
    template_name = "addit/index.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Quote, slug=self.kwargs.get("slug"))


def custom_page_not_found(request, exception=None):
    return page_not_found(request, exception, template_name="addit/404.html")
