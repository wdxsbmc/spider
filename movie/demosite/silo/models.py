from django.db import models

# Create your models here.
iAutoId = models.AutoField(primary_key=True, default=None)
title = models.CharField(max_length=1024, default=None)