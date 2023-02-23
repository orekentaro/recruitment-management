import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from v1.models.base import BaseCreateUpdateTimeModel

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, name, password, **other_fields):

        other_fields.setdefault("is_superuser", True)

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")
        return self.create_user(email, name, password, **other_fields)

    def create_user(self, email, name, password, **other_fields):
        if not email:
            raise ValueError(_("Please provide an email address"))
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseCreateUpdateTimeModel):
    id = models.UUIDField(
        verbose_name=_("ID"), primary_key=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(verbose_name=_("名前"), max_length=100)
    email = models.EmailField(verbose_name=_("メールアドレス"), unique=True, max_length=256)
    new_email = models.EmailField(_("変更確認前のメールアドレス"), null=True, blank=True)
    password = models.CharField(verbose_name=_("パスワード"), max_length=100)
    miss_count = models.IntegerField(_("ログイン失敗回数"), default=0)

    objects = CustomAccountManager()
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("ユーザー")
