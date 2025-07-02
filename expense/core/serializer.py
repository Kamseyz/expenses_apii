from rest_framework import serializers
from .models import Category, Expense

# ADD CATEGORY
class SerializedAddCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
    def create(self, validated_data):
        user = self.context['request'].user
        return Category.objects.create(user = user , **validated_data)
    
    def validate(self, attrs):
        name = attrs.get('name')
        if len(name) < 3:
            raise serializers.ValidationError('Category title must be less than 3 character')
        elif len(name) >= 50:
            raise serializers.ValidationError("Cateogry can't be greater than 50 character")
        return attrs
    
    
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
    class Meta:
        model = Expense
        fields = [
            'title',
            'amount',
            'description'
        ]
        
        read_only_fields = ['category']
        
    def create(self, validated_data):
        user = self.context['request'].user
        return Expense.objects.create(user = user , **validated_data)
    
    def validate_amount(self, value):
        if not isinstance(value, (int, float)):
            raise serializers.ValidationError('Amount must be a number')
        if value <= 0:
            raise serializers.ValidationError('Amount must be greater than 0')
        return value

        
        
# UPDATE CATEGORY + EXPENSES(NESTED)

class SerializedUpdateExpenses(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'title',
            'amount',
            'description'
        ]
        
        read_only_fields = ['category']
        
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    
    def validate_amount(self, value):
        if not isinstance(value, (int, float)):
            raise serializers.ValidationError('Amount must be a number')
        if value <= 0:
            raise serializers.ValidationError('Amount must be greater than 0')
        return value

