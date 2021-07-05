from rest_framework import serializers
from .models import Dress

class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dress
        fields = ['name','rental','security','size','productID','color','material','neck_design','sleeves','designer']