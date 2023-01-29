import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from v1.models.base import BaseCreateUpdateTimeModel
from v1.constance import Constance


class AbstractJobSeeker(BaseCreateUpdateTimeModel):
    id = models.UUIDField(
        verbose_name=_("ID"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    job_ads = models.ForeignKey(
        "v1.JobAds",
        on_delete=models.PROTECT,
        related_name="job_ads",
        verbose_name=_("求人広告記事"),
    )
    first_name = models.CharField(
        verbose_name=_("名"),
        max_length=100,
        null=True,
    )
    last_name = models.CharField(
        verbose_name=_("姓"),
        max_length=100,
        null=True,
    )
    first_name_kana = models.CharField(
        verbose_name=_("メイ"),
        max_length=100,
        null=True,
    )
    last_name_kana = models.CharField(
        verbose_name=_("セイ"),
        max_length=100,
        null=True,
    )
    mail = models.EmailField(
        verbose_name=_("メールアドレス"),
        unique=True,
        max_length=256,
        null=True,
    )
    gender = models.CharField(
        verbose_name=_("性別"),
        max_length=16,
        choices=Constance.GENDER,
    )
    career = models.TextField(verbose_name=_("経歴"))
    memo = models.JSONField(
        verbose_name=_("メモ"),
        default=list,
        blank=True,
    )
    assign = models.ForeignKey(
        "v1.User",
        on_delete=models.SET_NULL,
        related_name="assign",
        verbose_name=_("担当者"),
        null=True,
    )

    class Meta:
        abstract = True


class JobSeeker(AbstractJobSeeker):
    class Meta:
        verbose_name = _("求職者")
