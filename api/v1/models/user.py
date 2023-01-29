import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from v1.models.base import BaseCreateUpdateTimeModel


class User(AbstractBaseUser, PermissionsMixin, BaseCreateUpdateTimeModel):
    id = models.UUIDField(
        verbose_name=_("ID"), primary_key=True, default=uuid.uuid4, editable=False
    )
    first_name = models.CharField(verbose_name=_("名前"), max_length=100)
    email = models.EmailField(verbose_name=_("メールアドレス"), unique=True, max_length=256)
    new_email = models.EmailField(_("変更確認前のメールアドレス"), null=True, blank=True)
    password = models.CharField(verbose_name=_("パスワード"), max_length=24)
    miss_count = models.IntegerField(_("ログイン失敗回数"), default=0)

    objects = UserManager()
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("ユーザー")
