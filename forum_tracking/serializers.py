from rest_framework import serializers


class ForumTrackingSerializer(serializers.Serializer):
    """Serializer for providing users following a specific forum"""
    user = serializers.CharField(max_length=50)
    mark_time = serializers.DateTimeField()
