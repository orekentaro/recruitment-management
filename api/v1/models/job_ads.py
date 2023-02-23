import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractJobAds(models.Model):
    id = models.UUIDField(
        verbose_name=_("ID"), primary_key=True, default=uuid.uuid4, editable=False
    )
    job_master = models.ForeignKey(
        "v1.JobMaster",
        on_delete=models.PROTECT,
        related_name="job_ads",
        verbose_name=_("求人媒体"),
    )
    publication_start = models.DateField(verbose_name=_("公開日"))
    publication_end = models.DateField(verbose_name=_("掲載終了日"))
    title = models.TextField(verbose_name=_("タイトル"))
    contents = models.TextField(verbose_name=_("内容"))
    views = models.PositiveIntegerField(verbose_name=_("閲覧数"), default=0)
    cost = models.PositiveIntegerField(verbose_name=_("単発掲載費用"))

    class Meta:
        abstract = True


class JobAds(AbstractJobAds):
    class Meta:
        verbose_name = _("求人広告")
