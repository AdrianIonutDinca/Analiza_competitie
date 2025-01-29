from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import OperatorProfile
from .models import Categ, Produs, Magazin
from viewer.models import SelectedData
from .models import IncentiveProduct

# Register your models here.

admin.site.register(Categ)
admin.site.register(Produs)
admin.site.register(Magazin)
admin.site.register(SelectedData)

admin.site.unregister(User)

class OperatorProfileInline(admin.StackedInline):
    model = OperatorProfile
    can_delete = False
    verbose_name_plural = 'Operator Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (OperatorProfileInline,)
    def has_add_permission(self, request, obj=None):
        """Împiedică adăugarea unui nou profil dacă utilizatorul are deja unul"""
        if obj and hasattr(obj, 'operatorprofile'):
            return False  # Nu permite adăugarea unui nou profil
        return True


admin.site.register(User, CustomUserAdmin)

@admin.register(IncentiveProduct)
class IncentiveProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
