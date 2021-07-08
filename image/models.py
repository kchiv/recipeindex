from django.db import models
from django.utils import timezone
from django.dispatch import receiver

# Create your models here.

class ImageFile(models.Model):
    image_name = models.CharField(max_length=400, blank=True, help_text='Name of image.')
    image_file = models.ImageField(upload_to='img')
    publication_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.image_file

# Handles deletion on S3
@receiver(models.signals.post_delete, sender=ImageFile)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.image_file.delete(save=False)