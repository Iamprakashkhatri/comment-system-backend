from django.db import models
from user.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


    def __str__(self):
        return f"{self.user.email}"

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reply")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="comment_reply")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Reply"
        verbose_name_plural = "Reply"


    def __str__(self):
        return f"{self.user.email}"