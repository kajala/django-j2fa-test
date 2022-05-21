from j2fa_test.models import UserProfile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserProfileInlineAdmin(admin.StackedInline):
    model = UserProfile
    can_delete = False
    min_num = 1
    max_num = 1
    fields = (
        'phone',
        'last_modified',
        'require_2fa',
    )
    readonly_fields = (
        'last_modified',
    )


class CustomUserAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'phone',
        'is_staff',
        'is_active',
        'require_2fa',
    )
    inlines = (
        UserProfileInlineAdmin,
    )

    def require_2fa(self, obj: User):
        return obj.profile.require_2fa
    require_2fa.boolean = True

    def phone(self, obj: User):
        return obj.profile.phone if obj.profile else ''
    phone.short_description = 'phone'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
