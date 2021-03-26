from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuarios
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#admin.site.register(Usuarios,UserAdmin)

@admin.register(Usuarios)
class UsuariosAdmin(UserAdmin):
    
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email','telefono','biografia','ultima_modificacion')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email','telefono','biografia','url_perfil')}),
        ('Permisos', {'fields': ('is_superuser',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2','telefono','biografia','url_perfil'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()



















#admin.site.register(Perfil)

"""Esta es la forma mas facil de registrar un modelo en admin"""
#@admin.site.register(Perfil)
#admin.site.register(Usuarios)

"""
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    
    Esto es para organizar la informacion en admin
    list_display = ('user','telefono','imagen_perfil','biografia','fecha_creacion','ultima_modificacion')
    
    Esto es para volver url la informacion
    list_display_links = ('user',)


    Esto es para editar los campos
    list_editable =('telefono','imagen_perfil')


    Para buscar algo

    #Se escribe user__email para indicar que email viene de la clase User
    search_fields = ('user__email',
        'user__username',
        'telefono')


    Para filtrar las busquedas
    list_filter = (
        'fecha_creacion',
        'user__username',
        'telefono'
    )

    Esto es para organizar el formulario en grupos de campos
    fieldsets = (
        ('Probandojajajja', {
            'fields': ('user', 'telefono'),
        }),
    )



class PerfilInline(admin.StackedInline):
    model: Perfil
    can_delete =False
    verbose_name_plural = 'Perfiles'


class UserAdmin(BaseUserAdmin):
    inlines =(PerfilInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
"""