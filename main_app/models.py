from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    start = models.DateField()
    due = models.DateField(blank=True, null=True)
    lang = models.CharField(max_length=50, blank=True, null=True)
    STATUS_CHOICES = [
        ('Ideation', 'Ideation'),
        ('Planned', 'Planned'),
        ('In Progress', 'In Progress'),
        ('On Hold', 'On Hold'),
        ('Refactoring', 'Refactoring'),
        ('Testing', 'Testing'),
        ('Deployed', 'Deployed'),
        ('Completed', 'Completed'),
        ('Archived', 'Archived'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    link = models.URLField(blank=True, null=True)
    img = models.URLField(blank=True, null=True)

def __str__(self):
    return self.name