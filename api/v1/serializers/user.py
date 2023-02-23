from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from v1.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """ユーザー登録シリアライザ"""

    confirmation_password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        exclude = ["miss_count"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data: dict[str, str]) -> dict[str, str]:
        if (password := data["password"]) != data["confirmation_password"]:
            raise ValidationError(_("確認用パスワードが一致しません"))
        if len(password) < 8:
            raise ValidationError(_("パスワードは8文字以上で設定してください"))
        return data

    def create(self, validated_data: dict[str, str]) -> User:
        validated_data.pop("confirmation_password")
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
