"""trydjango URL Configuration

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

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    improved_view,
    image_view,
    learnmore_view,
    about_view,
    instructions_view,
)

urlpatterns = [
    path("", improved_view),
    path("about/", about_view),
    path("learnmore/", learnmore_view),
    path("instructions/", instructions_view),
    path("integral/image", image_view),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
