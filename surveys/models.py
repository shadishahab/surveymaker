from django.db import models
from people.models import Person

class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        Person,
        related_name = 'surveys',
        on_delete = models.CASCADE,
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title