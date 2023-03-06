from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def str(self):
        return self.title





   