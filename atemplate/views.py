from django.http import HttpResponse
from django.views.generic.base import View

from django.shortcuts import render

# Create your views here.


# 创建一个类视图
class CreateTemplate(View):

    def get(self,request):

        content = {
            'name':'老王',
            'age':30,
            'siblings':['小涵','小芬','小芳'],
            'data':'<a href=www.baidu.com>百度链接</a>'
        }

        # 返回render函数
        return render(request, 'template_index.html', context=content)
