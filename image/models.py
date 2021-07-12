from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.dispatch import receiver
from django.core.exceptions import ValidationError, ObjectDoesNotExist

# Create your models here.

class ImageFile(models.Model):
    image_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image_name = models.CharField(max_length=400, blank=True, help_text='Name of image.')
    image_file = models.FileField(upload_to='img', max_length=900)
    publication_date = models.DateTimeField(default=timezone.now)

    def clean(self, *args, **kwargs):
        # Prevents image from being overwritten.
        try:
            obj = ImageFile.objects.get(pk=self.pk)
            if not obj.image_file == self.image_file:
                self.image_file = obj.image_file
                raise ValidationError({
                'image_file': 'You cannot change the image once image object has been created. Delete image object and create new image.'
                })
        except ObjectDoesNotExist:
            pass
    
    def get_absolute_url(self):
        return reverse('images:file_detail', kwargs={'file_id': self.pk})

    def __str__(self):
        if self.image_name:
            return self.image_name
        else:
            return self.image_file.name

# Handles deletion on S3
@receiver(models.signals.post_delete, sender=ImageFile)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.image_file.delete(save=False)