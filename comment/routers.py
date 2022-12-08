from rest_framework.routers import DefaultRouter
from .views import (
    CommentViewset,
    ReplyViewset,
)


router = DefaultRouter()
router.register("comment", CommentViewset,basename="comments")
router.register("comment-reply",ReplyViewset,basename="reply")
