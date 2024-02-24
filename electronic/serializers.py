from rest_framework import serializers, viewsets

from electronic.models import Supplier
from rest_framework import permissions


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class IsActiveEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        # Проверка, является ли пользователь активным сотрудником
        return request.user.is_active_employee


# Пример настройки прав доступа для представлений
class SupplierViewSet(viewsets.ModelViewSet):
    permission_classes = [IsActiveEmployee]


class SupplierUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ('debt',)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierUpdateSerializer

