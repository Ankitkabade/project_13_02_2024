from rest_framework import permissions

class IsOwnerOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
    
        if request.user and request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return(request.user == obj.created_by)