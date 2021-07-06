from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from forum_tracking.serializers import ForumTrackingSerializer
from machina.apps.forum_tracking.models import ForumReadTrack


class ForumTrackingView(ListAPIView):
    """View for providing users following a specific forum"""
    serializer_class = ForumTrackingSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        forum_name = self.request.query_params.get('forum_name')
        return ForumReadTrack.objects.filter(forum__name=forum_name)


