from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=50, unique=True)  # 用户名
    password = models.CharField(max_length=128)  # 密码
    nickname = models.CharField(max_length=50, blank=True, null=True)  # 昵称
    email = models.EmailField(blank=True, null=True)  # 邮箱
    website = models.URLField(blank=True, null=True)  # 站点
    registered = models.DateTimeField(auto_now_add=True)  # 注册时间，自动填充
    status = models.IntegerField(blank=True, null=True)  # 用户状态

    def __str__(self):
        return self.username


class UserMeta(models.Model):
    user = models.ForeignKey(Users)
    key = models.CharField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return self.key


class Categorys(models.Model):
    name = models.CharField(max_length=20)
    description =models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    parent = models.IntegerField(blank=True, null=True)  # 父类别id

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class tagship(models.Model):
#     post = models.ForeignKey(posts)
#     tag = models.ForeignKey(tags)
#
#     # def __str__(self):
#     #     return 'tagship'


class Posts(models.Model):
    author = models.ForeignKey(Users)
    title = models.CharField(max_length=50)  # 标题
    excerpt = models.CharField(max_length=200, blank=True, null=True)  # 摘要
    content = models.TextField()  # 正文
    status = models.CharField(max_length=20, blank=True, null=True) # 文章状态

    publish_time = models.DateTimeField(auto_now_add=True)  # 发表时间
    update_time = models.DateTimeField(auto_now=True)  # 更新时间

    comment_status = models.CharField(max_length=20, blank=True, null=True)  # 文章评论状态
    comment_count = models.IntegerField(blank=True, null=True)  # 文章评论数

    tags = models.ManyToManyField(Tags)  # 文章标签
    category = models.ForeignKey(Categorys)  # 文章类别

    def __str__(self):
        return self.title


class PostMeta(models.Model):
    post = models.ForeignKey(Posts)
    key = models.CharField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return self.key


class Comments(models.Model):
    post = models.ForeignKey(Posts, verbose_name='tht post comments in')
    author = models.CharField(max_length=50, null=True, blank=True)  # 评论者
    author_email = models.EmailField(null=True, blank=True)  # 评论者邮箱
    author_url = models.URLField(null=True, blank=True)  # 评论者网址
    author_IP = models.GenericIPAddressField(null=True, blank=True)  # 评论者IP
    date = models.DateTimeField(auto_now_add=True)  # 评论时间
    user= models.IntegerField(blank=True, null=True)  # 评论者id 不一定存在

    approved = models.NullBooleanField(default=False)  # 评论批准

    parent = models.IntegerField(null=True, blank=True)  # 父评论id

    def __str__(self):
        return self.author


class CommentMeta(models.Model):
    comment = models.ForeignKey(Comments, verbose_name='related post')
    key = models.CharField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return self.key


