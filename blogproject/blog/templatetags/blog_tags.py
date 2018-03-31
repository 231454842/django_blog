from ..models import Post,Category
from django import template

register=template.Library()
# 右侧最新文章列表
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by("-create_time")[:num]
#右侧归档目录
@register.simple_tag
def archives():
    return Post.objects.dates('create_time','month',order='DESC')


#分类类表
@register.simple_tag
def get_categories():
    return Category.objects.all()
