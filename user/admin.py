from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.utils.translation import gettext_lazy as _

from user.models import User
from common.utils import get_post_model

Post = get_post_model()

class HasPostsFilter(admin.SimpleListFilter):
    title = _('Has Posts')
    parameter_name = 'has_posts'

    def lookups(self, request, model_admin):
        return (
            ('yes', _('Yes')),
            ('no', _('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(id__in=Post.objects.values_list('user_id', flat=True).distinct())
        elif self.value() == 'no':
            return queryset.exclude(id__in=Post.objects.values_list('user_id', flat=True).distinct())
        return queryset

class UserAdmin(BaseUserAdmin):

    list_display = ('username', 'email', 'is_active', 'is_admin', 'is_staff')
    list_filter = ('is_active', 'is_admin', 'is_staff', HasPostsFilter)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)