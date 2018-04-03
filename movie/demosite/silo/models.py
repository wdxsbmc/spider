from django.db import models

# Create your models here.


class TestScrapy(models.Model):
    iAutoId = models.AutoField(primary_key=True, default=None)
    title = models.CharField(max_length=1024, default=None)

    class Meta:
        app_label = 'silo'
        db_table = 'dg_spider_django1'