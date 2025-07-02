from django.urls import path
from .views import CreateCategory,EditCategory

urlpatterns = [
    #List and create cateogry
    path('create_category/', CreateCategory.as_view(), name='create_category'),
    #update category
    path('update/<int:pk>/category/', EditCategory.as_view(), name='update_category'),
    #delete category
]
