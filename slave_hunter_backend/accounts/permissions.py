from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Доступ на редактирование только владельцу. Остальные могут только читать.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешить GET, HEAD, OPTIONS для всех
        if request.method in SAFE_METHODS:
            return True

        # Изменять может только владелец
        return obj.owner == request.user
