#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
@author: wgrice
@contact: 13s101042@hit.edu.cn
@file: initdb.py
@time: 2017/12/9 13:22
@desc:
'''

from blog.models import User, UserMeta, Post, PostMeta, Comment, CommentMeta, Category, Tag


# 插入数据

# 方式 1
Category.objects.create(name='未分类', description='没有设置类别的')
Category.objects.create(name='我的笔记', description='私人笔记')
Category.objects.create(name='我的日记', description='私人日记')
Category.objects.create(name='我的收藏', description='微信，网页收藏')
Category.objects.create(name='我的生活', description='生活点滴')

# 方法 2
# cate = Category(name="我的笔记", description='私人笔记')
# cate.save()

# 方法 3
# cate = Category()
# cate.name = "我的日记"
# cate.description = "私人日记"
# cate.save()

# 方法 4，首先尝试获取，不存在就创建，可以防止重复
# Category.objects.get_or_create(name="我的收藏", description="微信，网页收藏")
# Category.objects.get_or_create(name="我的生活", description="生活点滴")
# 返回值(object, True/False)

# Category分类初始化
Category.objects.create(name='未分类', description='没有设置类别的')
Category.objects.create(name='我的笔记', description='私人笔记')
Category.objects.create(name='我的日记', description='私人日记')
Category.objects.create(name='我的收藏', description='微信，网页收藏')
Category.objects.create(name='我的生活', description='生活点滴')

# Tag标签初始化
Tag.objects.create(name='Python')
Tag.objects.create(name='C/C++')
Tag.objects.create(name='Java')
Tag.objects.create(name='Linux')
Tag.objects.create(name='Shell')

# User用户初始化
User.objects.create(username='wg', password='wangu', nickname='小米饭', email='wgrice@163.com', website='www.littlerice.com', status=1)
User.objects.create(username='yq', password='yangqian', nickname='小米粥', email='yqrice@163.com', website='www.onerice.com', status=2)

# Post文章初始化


