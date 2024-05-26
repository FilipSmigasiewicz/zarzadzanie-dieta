from django.shortcuts import render, get_object_or_404, redirect
from .models import Meal, DietPlan
from .forms import MealForm, DietPlanForm

def list_meals(request):
    meals = Meal.objects.all()
    return render(request, 'list_meals.html', {'meals': meals})

def create_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_meals')
    else:
        form = MealForm()
    return render(request, 'create_meal.html', {'form': form})

def edit_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('list_meals')
    else:
        form = MealForm(instance=meal)
    return render(request, 'edit_meal.html', {'form': form})

def delete_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    meal.delete()
    return redirect('list_meals')

def create_diet_plan(request):
    if request.method == 'POST':
        form = DietPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_diet_plans')
    else:
        form = DietPlanForm()
    return render(request, 'create_diet_plan.html', {'form': form})

def list_diet_plans(request):
    diet_plans = DietPlan.objects.all()
    return render(request, 'list_diet_plans.html', {'diet_plans': diet_plans})

def delete_diet_plan(request, plan_id):
    diet_plan = get_object_or_404(DietPlan, pk=plan_id)
    if request.method == 'POST':
        diet_plan.delete()
        return redirect('list_diet_plans')
    return render(request, 'dieta/confirm_delete.html', {'diet_plan': diet_plan})

def view_diet_plan(request, plan_id):
    diet_plan = get_object_or_404(DietPlan, pk=plan_id)

    # Inicjalizacja sum makroskładników
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0

    # Zliczanie makroskładników dla śniadania
    if diet_plan.breakfast:
        total_calories += diet_plan.breakfast.calories
        total_protein += diet_plan.breakfast.protein
        total_carbohydrates += diet_plan.breakfast.carbohydrates
        total_fat += diet_plan.breakfast.fat

    # Zliczanie makroskładników dla lunchu
    if diet_plan.lunch:
        total_calories += diet_plan.lunch.calories
        total_protein += diet_plan.lunch.protein
        total_carbohydrates += diet_plan.lunch.carbohydrates
        total_fat += diet_plan.lunch.fat

    # Zliczanie makroskładników dla kolacji
    if diet_plan.dinner:
        total_calories += diet_plan.dinner.calories
        total_protein += diet_plan.dinner.protein
        total_carbohydrates += diet_plan.dinner.carbohydrates
        total_fat += diet_plan.dinner.fat

    context = {
        'diet_plan': diet_plan,
        'total_calories': total_calories,
        'total_protein': total_protein,
        'total_carbohydrates': total_carbohydrates,
        'total_fat': total_fat,
    }

    return render(request, 'dieta/view_diet_plan.html', context)

def view_meal(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    return render(request, 'view_meal.html', {'meal': meal})
