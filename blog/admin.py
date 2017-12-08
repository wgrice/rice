from django.contrib import admin
from blog.models import Users, UserMeta, Posts, PostMeta, Comments, CommentMeta, Categorys, Tags


class UsersAdmin(admin.ModelAdmin):
    #list_display = ('序号', '用户名', '密码', '昵称', '邮箱', '站点', '注册时间', '用户状态')
    list_display = ('id', 'username', 'nickname', 'email', 'website', 'registered', 'status')


admin.site.register(Users, UsersAdmin)
admin.site.register(UserMeta)
admin.site.register(Posts)
admin.site.register(PostMeta)
admin.site.register(Comments)
admin.site.register(CommentMeta)
admin.site.register(Categorys)
admin.site.register(Tags)