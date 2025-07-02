from .serializer import SerializedAddCategory,SerializedUpdateCategory
from rest_framework import generics
from rest_framework import permissions
from .models import Category, Expense
from rest_framework import status
# Create your views here.


# CREATE CATEGORY AND LIST CATEGORY
class CreateCategory(generics.ListCreateAPIView):
    serializer_class = SerializedAddCategory
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Category.objects.filter()
    
    
# EDIT CATEGORY
class EditCategory(generics.RetrieveUpdateAPIView):
    serializer_class = SerializedUpdateCategory
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Category.objects.filter(user = self.request.user)
    

# DELETE CATEGORY

# LIST EXPENSES + CATEGORY

# ADD EXPENSES + CATEGORY (NESTED + VIEW)

# EDIT EXPENSE + CATEGORY

# DELETE EXPENSE + CATEGORY

