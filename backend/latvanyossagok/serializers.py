from rest_framework import serializers
from .models import Orszag, Telepules, Latvanyossag, Hozzaszolasok

class OrszagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orszag
        fields = '__all__'

class TelepulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telepules
        fields = '__all__'

class LatvanyossagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Latvanyossag
        fields = '__all__'
        depth = 2

class HozzaszolasokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hozzaszolasok
        fields = '__all__'

        