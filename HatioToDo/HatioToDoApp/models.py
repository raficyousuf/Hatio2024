from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class TodoItem(models.Model):
    project = models.ForeignKey(Project, related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
