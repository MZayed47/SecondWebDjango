from rest_framework import serializers      # Serializers is a class that can convert python data to any type of data
from .models import Stock                   # (like JSON), in which I want to transfer the data.


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        # fields = ('ticker', 'volume')
        fields = '__all__'
