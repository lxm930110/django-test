from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render

# Create your views here.


def object_response(request):
         # 方法
    # return HttpResponse(
    #     content='响应内容',
    #     content_type='text/html; charset=utf8',
    #     status=200
    # )
    # return HttpResponse(
    #     content="{'name':'zilong'}",
    #     content_type='application/json; charset=utf8',
    #     status=200
    # )
        # 属性
    response = HttpResponse()
    response.content = '操作属性方式'
    # response['itcast'] = 'python'
    response.content_type = ''
    response.status_code = 200
    return response


def json_response(request):
    # 字典格式
    result = {'name': 'laowang',
              'age': 20
            }
    return JsonResponse(result)

    # 列表格式
    # result = [{'name': ' laowang',
    #           'age': 20
    #           }]
    #
    # return JsonResponse(result, safe=False)

