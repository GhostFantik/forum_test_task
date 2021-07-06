from django.urls import path
from forum_tracking.views import ForumTrackingView

urlpatterns = [
    path('forumreadtrack/', ForumTrackingView.as_view())
]
