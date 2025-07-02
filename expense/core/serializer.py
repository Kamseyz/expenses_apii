from rest_framework import serializers
from .models import Category, Expense



# ADD CATEGORY
class SerializedAddCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
    
    #create category    
    def create(self, validated_data):
        user = self.context['request'].user
        return Category.objects.create(user = user , **validated_data)
    
    #validate category
    def validate(self, attrs):
        name = attrs.get('name')
        if len(name) < 3:
            raise serializers.ValidationError('Category title must be less than 3 character')
        elif len(name) >= 50:
            raise serializers.ValidationError("Cateogry can't be greater than 50 character")
        return attrs
    
    #Check if category already exists
    
    def validate_name(self, value):
        if Category.objects.filter(name = value).exists():
            raise serializers.ValidationError("Category already exists")
        else:
            return value
    
# UPDATE CATEGORY
class SerializedUpdateCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
    
# ADD CATEGORY + EXPENSES (NESTED)
class SerializedAddExpenses(serializers.ModelSerializer):
    date = serializers.DateField()
    class Meta:
        model = Expense
        fields = [
            'id',
            'title',
            'amount',
            'category',
            'date',
            'description'
        ]
        
        
    def create(self, validated_data):
        user = self.context['request'].user
        return Expense.objects.create(user = user , **validated_data)
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError('Amount must be greater than 0')
        return value

    def validate(self, attrs):
        description = attrs.get('description')
        if len(description) < 3:
            raise serializers.ValidationError("description character can't be less than 3 ")
        elif len(description) >= 200:
            raise serializers.ValidationError("description cannot excess 200 lines")
        return attrs
        
        
# UPDATE CATEGORY + EXPENSES(NESTED)

class SerializedUpdateExpenses(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'title',
            'amount',
            'category',
            'description'
        ]
        
        
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError('Amount must be greater than 0')
        return value

