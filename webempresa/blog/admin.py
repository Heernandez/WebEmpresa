from django.contrib import admin
from .models import Category,Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
admin.site.register(Category,CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','author','published','post_categories')
    ordering = ('author',)
    search_fields = ('title','author__username','categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')

    def post_categories(self,category):
        #para metodos no llamables en list_display como categories
        return ",".join([c.name for c in category.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"

admin.site.register(Post,PostAdmin)