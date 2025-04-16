from django.db import models

class SiteContent(models.Model):
    name = models.CharField(max_length=100, help_text="For internal reference like 'about section'")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name