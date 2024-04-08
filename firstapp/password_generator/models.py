from django.db import models


# Create your models here.

class GeneratedPassword(models.Model):
    website_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def set_password(self, raw_password):
        self.password_hash = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password_hash)

    def __str__(self):
        return self.website_name