from rest_framework.permissions import IsAdminUser,BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request,view):
        if request.method=='GET':
            return True
        if request.user.is_anonymous or request.user.role==2:
            return False
        if request.user.role==1 or request.user.is_admin:
            return True
    