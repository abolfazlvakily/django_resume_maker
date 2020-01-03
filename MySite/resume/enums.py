from django.utils.translation import ugettext as _


class Priorities(object):
    High = 1
    Medium = 2
    Low = 3


PRIORITIES = (
    (Priorities.High, _('High priority')),
    (Priorities.Medium, _('Medium priority')),
    (Priorities.Low, _('Low priority'))
)
