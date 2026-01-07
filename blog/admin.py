from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}

    def __str__(self):
        return self.title


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published',)

    def __str__(self):
        return self.title


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'location',
        'pub_date',
        'is_published',
        'created_at',
    )
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'pub_date')
    search_fields = ('title', 'text')
    list_select_related = ('author', 'category', 'location')
    date_hierarchy = 'pub_date'

    def __str__(self):
        return self.title
