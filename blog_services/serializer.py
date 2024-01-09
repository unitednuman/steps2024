from .models import Reporter
from rest_framework import serializers

class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = '__all__'