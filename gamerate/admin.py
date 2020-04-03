from django.contrib import admin
from gamerate.models import UserProfile, Category, Game, Review, Favourite

class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
#    list_display = ('name','category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Favourite)
# Register your models here.
