from rest_framework import serializers
from app1.serializers import BlogSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id','username','email','password','blogs')
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
