from django.contrib import admin
from TestModel.models import book_info,user_info

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'book_name', 'book_purchase_time')
    search_fields = ('book_id', 'book_name')

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_pwd', 'user_type', 'user_alias')
    search_fields = ('user_name', 'user_alias')

# Register your models here.
# admin.site.register([book_info, user_info])
admin.site.register(book_info, BookInfoAdmin)
admin.site.register(user_info, UserInfoAdmin)

