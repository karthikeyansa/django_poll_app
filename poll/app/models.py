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


# relationship
'''
One to one
one to many
many to many
'''

'''
# CREATE TABLE Users (
    ID int not null unique auto_increment,
    username char(50) not null unique,
    primary key(id)
);

# insert into Users(username) values("karthikeyan"); 

class Users(models.Model):
    username = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.username

class Posts(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    body = models.TextField(null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)

    def get_username(self):
        return self.author.username

'''