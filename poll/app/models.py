from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField()
    choice1 = models.CharField(max_length=50)
    choice2 = models.CharField(max_length=50)
    choice1_count = models.IntegerField(default=0)
    choice2_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} {self.question} {self.choice1} {self.choice2} {self.choice1_count} {self.choice2_count}'
