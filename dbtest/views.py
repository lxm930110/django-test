from datetime import date

from django.db.models import F, Q, Max,Sum,Min,Avg
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from dbtest.models import BookInfo, HeroInfo


class SaveData(View):
    def get(self, request):
        # 添加 save()
        book = BookInfo(
            btitle='西游记',
            bpub_date=date(1990,1,1)
        )
        book.save()
        # 添加 create()
        BookInfo.objects.create(btitle='三国',bpub_date=date(1980,1,1))
        # 删除 delete()
        book = BookInfo.objects.get(id=5)
        book.delete()
        # 删除 delete()
        BookInfo.objects.get(id=6).delete()
        # 修改 save()
        book = BookInfo.objects.get(id=2)
        book.btitle='天龙'
        book.save()
        # 修改 update （注意update后面需要是querySet）
        BookInfo.objects.filter(id=2).update(btitle='天龙八部')
        # 查询
        BookInfo.objects.filter(id=3)

        BookInfo.objects.filter(id__in=[1,2])

        BookInfo.objects.filter(id__gte=1)

        BookInfo.objects.aggregate(Max('bread'))

        BookInfo.objects.all()

        BookInfo.objects.count()

        BookInfo.objects.filter(btitle__contains='八')

        BookInfo.objects.filter(btitle__startswith='天')

        BookInfo.objects.filter(btitle__endswith='传')

        BookInfo.objects.filter(bread__gt=F('bcomment'))

        BookInfo.objects.filter(id=1,bread=12)

        BookInfo.objects.filter(Q(id=1) | Q(bread=30))

        BookInfo.objects.filter(~Q(id=1))

        BookInfo.objects.exclude(id=1)

        BookInfo.objects.all().order_by('bread')

        BookInfo.objects.filter(bread__gt= F('bcomment'))

        BookInfo.objects.aggregate(Max('bread'))
        # 关联查询一对多
        book = BookInfo.objects.get(id=1)
        book.heroinfo_set.all()

        # 关联查询多对一
        hear = HeroInfo.objects.get(hname='任盈盈')
        hear.hbook

        # 关联过滤查询多对一
        BookInfo.objects.filter(heroinfo__hname__exact='乔峰')

        # 关联过滤查询一对多
        HeroInfo.objects.filter(hbook__btitle__exact='天龙八部')

        # 关联过滤查询一对多
        HeroInfo.objects.filter(hbook__bread__gt=30)


        return HttpResponse('查询结果')
