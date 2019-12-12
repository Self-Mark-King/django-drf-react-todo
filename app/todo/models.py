from django.db import models
# Create your models here.

# add this
class person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    Person = models.ForeignKey(person, on_delete=models.CASCADE)

    def _str_(self):
        return self.title


