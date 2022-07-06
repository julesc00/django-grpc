
from django.contrib import admin
from django.urls import path

from blog.handlers import grpc_handlers as blog_grpc_handlers

urlpatterns = [
    path('admin/', admin.site.urls),
]


def grpc_handlers(server):
    blog_grpc_handlers(server)
