from django.urls import path
from .views import Resume
from django.conf.urls.static import static
from django.conf import settings

app_name = 'resume'
urlpatterns = [
                  path('', Resume.as_view(), name='skill_list'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
