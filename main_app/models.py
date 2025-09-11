from django.db import models
from django.urls import reverse
# Create your models here.


# A tuple of 2-tuples added above our models
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('cat-detail', kwargs={'cat_id': self.id})
  

class Feeding(models.Model):
  date = models.DateField('Feeding date')
  meal = models.CharField(
      max_length = 1,
      choices = MEALS,
      default = MEALS[0][0] # set the default value for meal to be 'B'
      )
  
  cat = models.ForeignKey(Cat, on_delete=models.CASCADE) #When a cat is deleted, it will delete the meals associated with that cat

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("toy-detail", kwargs={"pk": self.id})
  