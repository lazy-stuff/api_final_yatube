from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied


class IsAuthorOrReadOnly(BasePermission):
    """
    Проверяет уровень доступа пользователя к чтению, изменению и удалению
    данных.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            if obj.author != request.user:
                raise PermissionDenied(
                    'Доступ к редактированию чужого контента закрыт.'
                )
        return True
