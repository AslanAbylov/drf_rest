import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser

from .models import Women
from rest_framework.renderers import JSONRenderer


class WomenSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = '__all__'



