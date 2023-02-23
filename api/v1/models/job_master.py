import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractJobMaster(models.Model):
    id = models.UUIDField(
        verbose_name=_("ID"), primary_key=True, default=uuid.uuid4, editable=False
    )
    job_offer_name = models.CharField(
        verbose_name=_("求人媒体"),
        max_length=100,
    )
    subscription_cost = models.PositiveIntegerField(
        verbose_name=_("月額"),
    )
    detail = models.TextField(
        verbose_name=_("特筆事項"),
    )

    class Meta:
        abstract = True


class JobMaster(AbstractJobMaster):
    class Meta:
        verbose_name = _("求人媒体")
