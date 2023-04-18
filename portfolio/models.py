from django.db import models


class EmailForm(models.Model):
    """
    Defines the table in which emails are stored
    """
    sender_name = models.CharField(max_length=80)
    sender_email = models.EmailField()
    date_sent = models.DateTimeField(null=True)
    message = models.TextField()

    def __str__(self):
        return f"From {self.sender_name} ({self.sender_email}) on {self.date_sent}: {self.message}"
