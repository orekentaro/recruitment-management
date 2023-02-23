from django.db import models
from django.utils.translation import ugettext_lazy as _

from v1.constance import Constance


class Progress(models.Model):
    job_seeker = models.ForeignKey(
        "v1.JobSeeker",
        on_delete=models.CASCADE,
        related_name="job_seeker",
        verbose_name=_("求職者"),
    )
    progress = models.CharField(
        verbose_name=_("進捗"),
        max_length=100,
        choices=Constance.PROGRESS,
    )
    implementation_at = models.DateField(verbose_name=_("実施日"))
    author = models.ForeignKey(
        "v1.User",
        on_delete=models.SET_NULL,
        related_name="author",
        verbose_name=_("作成者"),
        null=True,
    )
    is_implementation = models.BooleanField(verbose_name=_("実施"))

    is_result = models.BooleanField(verbose_name=_("結果"))

    class Meta:
        verbose_name = _("進捗情報")
