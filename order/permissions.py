from rest_framework.permissions import BasePermission

class IsObjectOwner(BasePermission):
    def has_object_permission(self, request,view,obj):
        if obj.user==request.user:
            return True
        return False

