from django.contrib import admin

from .models import Blog, BlogComment, BlogTopSection

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display =['title', 'created_date','modified_date']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['title',]

admin.site.register(Blog, BlogAdmin)



class BlogCommentAdmin(admin.ModelAdmin):
    list_display =['blog','name', 'email', 'phone' ,'created_date']


admin.site.register(BlogComment, BlogCommentAdmin)

admin.site.register(BlogTopSection)