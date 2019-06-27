from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        # inside classes, you gotta path self to make a function
        return self.body[:200] + "..."

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
