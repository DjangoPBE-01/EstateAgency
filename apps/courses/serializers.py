from rest_framework import serializers
from .models import Category

class CategoryListSerializer(serializers.ModelSerializer):
    
    count_courses = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at', 'count_courses')
        
        
    def get_count_courses(self, obj):
        
        return obj.courses.count()