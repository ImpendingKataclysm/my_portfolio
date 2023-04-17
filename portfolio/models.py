from django.db import models


class EmailForm(models.Model):
    sender_name = models.CharField(max_length=80)
    sender_email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"From {self.sender_name} ({self.sender_email}): {self.message}"
