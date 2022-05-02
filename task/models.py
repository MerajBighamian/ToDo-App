from django.db import models


# Create your models here.

class Task(models.Model):
    """
        represent Task table for tasks in todo app
    """
    
    class Meta:
        verbose_name = 'کار ها' # verbose name of model in admin panel

    # title of task
    title = models.CharField(max_length=200)

    # status of task
    complate = models.BooleanField(default=False)

    # date and time of created task
    created = models.DateTimeField(auto_now_add=True)

    # if we get object return value in this below function
    def __str__(self):
        return self.title
