from rest_framework import permissions

class UpdateProfilePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class AddTodoStuffPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # if request.method in permissions.SAFE_METHODS:
        #     return obj.todo_stuffs.username == request.user.username

        return obj.user.id == request.user.id
