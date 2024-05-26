from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/meals', permanent=False)),
    path('meals/', views.list_meals, name='list_meals'),
    path('meals/create/', views.create_meal, name='create_meal'),
    path('meals/<int:meal_id>/edit/', views.edit_meal, name='edit_meal'),
    path('meals/<int:meal_id>/delete/', views.delete_meal, name='delete_meal'),
    path('meals/<int:meal_id>/', views.view_meal, name='view_meal'),
    path('diet_plans/', views.list_diet_plans, name='list_diet_plans'),
    path('diet_plans/create/', views.create_diet_plan, name='create_diet_plan'),
    path('diet_plans/<int:plan_id>/', views.view_diet_plan, name='view_diet_plan'),
    path('diet_plans/<int:plan_id>/delete/', views.delete_diet_plan, name='delete_diet_plan'),
]
