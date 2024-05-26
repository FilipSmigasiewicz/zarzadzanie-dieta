from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='meal_images/')
    calories = models.IntegerField()
    protein = models.IntegerField()
    carbohydrates = models.IntegerField()
    fat = models.IntegerField()
    recipe = models.TextField()

    def __str__(self):
        return self.name

class DietPlan(models.Model):
    name = models.CharField(max_length=255)
    breakfast = models.ForeignKey(Meal, related_name='breakfast_meals', on_delete=models.SET_NULL, null=True, blank=True)
    lunch = models.ForeignKey(Meal, related_name='lunch_meals', on_delete=models.SET_NULL, null=True, blank=True)
    dinner = models.ForeignKey(Meal, related_name='dinner_meals', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def total_calories(self):
        return sum(meal.calories for meal in [self.breakfast, self.lunch, self.dinner] if meal)

    @property
    def total_protein(self):
        return sum(meal.protein for meal in [self.breakfast, self.lunch, self.dinner] if meal)

    @property
    def total_carbohydrates(self):
        return sum(meal.carbohydrates for meal in [self.breakfast, self.lunch, self.dinner] if meal)

    @property
    def total_fat(self):
        return sum(meal.fat for meal in [self.breakfast, self.lunch, self.dinner] if meal)
