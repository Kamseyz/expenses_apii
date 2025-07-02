from .serializer import SerializedAddCategory,SerializedUpdateCategory,SerializedAddExpenses,SerializedUpdateExpenses
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
class DeleteCategory(generics.RetrieveDestroyAPIView):
    queryset = Category
    serializer_class = SerializedAddCategory
    
    def get_queryset(self):
        return Category.objects.filter(user = self.request.user)
    

# LIST EXPENSES + ADD CATEGGORY
class ListExpenses(generics.ListCreateAPIView):
    queryset = Expense
    serializer_class = SerializedAddExpenses
    permission_classes =[permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Expense.objects.filter(user = self.request.user)
    


# EDIT EXPENSE + CATEGORY

class EditExpenses(generics.RetrieveUpdateAPIView):
    queryset = Expense
    serializer_class = SerializedUpdateExpenses
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Expense.objects.filter(user = self.request.user)
    

# DELETE EXPENSE + CATEGORY

class DeleteExpenses(generics.RetrieveDestroyAPIView):
    queryset = Expense
    serializer_class = SerializedAddExpenses
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Expense.objects.filter(user = self.request.user)