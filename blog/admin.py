from django.contrib import admin
from blog.models import User, UserMeta, Post, PostMeta, Comment, CommentMeta, Category, Tag


class UsersAdmin(admin.ModelAdmin):
    #list_display = ('序号', '用户名', '密码', '昵称', '邮箱', '站点', '注册时间', '用户状态')
    list_display = ('id', 'username', 'nickname', 'email', 'website', 'registered', 'status')


admin.site.register(User, UsersAdmin)
admin.site.register(UserMeta)
admin.site.register(Post)
admin.site.register(PostMeta)
admin.site.register(Comment)
admin.site.register(CommentMeta)
admin.site.register(Category)
admin.site.register(Tag)