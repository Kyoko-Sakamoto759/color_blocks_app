from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from app.blocks.views import HomeView


def healthcheck(_request):
    return HttpResponse('ok')


urlpatterns = [
	path('admin/', admin.site.urls),
	path('', LoginView.as_view(template_name='blocks/login.html'), name='login'),
    path(('logout/'), LogoutView.as_view(next_page='/'), name='logout'),
    path('home/', TemplateView.as_view(template_name='blocks/home.html'), name='home'),
]
