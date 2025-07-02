from django.urls import path
from .views import (
    CreateCategory,
    EditCategory,
    DeleteCategory,
    ListExpenses,
    EditExpenses,
    DeleteExpenses,
)

urlpatterns = [
    #List and create cateogry
    path('create_category/', CreateCategory.as_view(), name='create_category'),
    #update category
    path('update/<int:pk>/category/', EditCategory.as_view(), name='update_category'),
    #delete category
    path('delete/<int:pk>/category/', DeleteCategory.as_view(), name='delete_category'),
    
    #List and create expenses
    path('create_expenses/', ListExpenses.as_view(), name='list_expenses'),
    #Edit expenses
    path('edit/<int:pk>/expenses/', EditExpenses.as_view(), name='edit_expenses'),
    #Delete expenses
    path('delete/<int:pk>/expenses/', DeleteExpenses.as_view(), name='delete_expenses'),
]
