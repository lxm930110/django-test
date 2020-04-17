
# 自定义一个中间件
def middleware_one(get_response):

    def middleware(request):

        print('处理请求对象之前，middleware_one')

        response = get_response(request)

        print('处理请求对象之后，middleware_one')

        return response

    return middleware


# 自定义一个中间件
def middleware_two(get_response):

    def middleware(request):

        print('中间件开始工作了，middleware_two')

        response = get_response(request)

        print('中间件结束工作了，middleware_two')

        return response

    return middleware