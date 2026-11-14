from django.db import models
from django.utils.translation import gettext_lazy as _


class DeletedReason(models.TextChoices):
    I_THOUGH_ABOUT_IT = "I thought about it", _('I_THOUGH_ABOUT_IT')
    The_INFORMATION_WAS_ENTERED_INCORRECTLY = "The information was entered incorrectly", _('The_INFORMATION_WAS_ENTERED_INCORRECTLY')
    They_FORCED_ME = "They forced me", _('They_FORCED_ME')