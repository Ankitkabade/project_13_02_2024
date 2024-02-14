from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format = '%y-%m-%d %H:%M:%S',read_only=True)
    created_by = serializers.HiddenField(default = serializers.CurrentUserDefault())
    author = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'
    
    def get_author(self,obj):
        return obj.created_by.username