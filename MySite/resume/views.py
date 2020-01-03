from django.views.generic import ListView
from .models import Skill


class Resume(ListView):
    model = Skill
