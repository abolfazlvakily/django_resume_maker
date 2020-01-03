from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from ckeditor.fields import RichTextField
from .enums import Priorities, PRIORITIES


class Skill(models.Model):
    # هرکاربر سیستمی می تواند چندین مهارت داشته باشد
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='has', db_column='user_id',
                                verbose_name=_('end_user'))
    title = models.CharField(max_length=150, db_column='title', verbose_name=_('title'))
    description = RichTextField()
    priority = models.IntegerField(choices=PRIORITIES, default=Priorities.Medium, db_column='priority',
                                   verbose_name=_('priority'))
    image = models.ImageField(db_column='image', verbose_name=_('image'), upload_to='Images')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_date']
        verbose_name = _('CV')
        verbose_name_plural = _('CVs')
        db_table = 'CVs'
