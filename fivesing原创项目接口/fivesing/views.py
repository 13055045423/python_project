from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from fivesing import models
from django.http import HttpResponse,JsonResponse
from rest_framework.throttling import SimpleRateThrottle
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,FormParser

class MySimpleRateThrottle(SimpleRateThrottle):
    scope = 'rate'
    def get_cache_key(self, request, view):
        return self.get_ident(request)

class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'pagesize'
    max_page_size = 15

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 15
class MyCursorPagination(CursorPagination):
    cursor_query_param = 'cursor'
    page_size = 15
    ordering = 'sign'
    page_size_query_param = 'pagesize'
    max_page_size = 15

class Banzoufenleiserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banzoufenlei
        fields = "__all__"

class Gedancontentinfoserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gedancontentinfo
        fields = "__all__"

class Gedaninfoserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gedaninfo
        fields = "__all__"

class Yuanchuangcontentserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Yuanchuangcontent
        fields = "__all__"

class Yunachuangfenleiserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Yunachuangfenlei
        fields = "__all__"

class Banzoufenleilistserializer(serializers.ModelSerializer):
    detailUrl =serializers.HyperlinkedIdentityField(view_name='banzoufenleiDetail')
    class Meta:
        model = models.Banzoufenlei
        fields = ['detailUrl','id','zhonglei']

class Gedancontentinfolistserializer(serializers.ModelSerializer):
    detailUrl =serializers.HyperlinkedIdentityField(view_name='gedancontentinfoDetail')
    class Meta:
        model = models.Gedancontentinfo
        fields = ['detailUrl','id','gequzuozhe','chuangjianren']

class Gedaninfolistserializer(serializers.ModelSerializer):
    detailUrl =serializers.HyperlinkedIdentityField(view_name='gedaninfoetail')
    class Meta:
        model = models.Gedaninfo
        fields = ['detailUrl','id','zuozhe','gedanname']

class Yuanchuanglistcontentserializer(serializers.ModelSerializer):
    detailUrl =serializers.HyperlinkedIdentityField(view_name='yuanchuangcontentDetail')
    class Meta:
        model = models.Yuanchuangcontent
        fields = ['detailUrl','id','qufeng']

class Yunachuanglistfenleiserializer(serializers.ModelSerializer):
    detailUrl =serializers.HyperlinkedIdentityField(view_name='yunachuangfenleiDetail')
    class Meta:
        model = models.Yunachuangfenlei
        fields = ['detailUrl','id','mokuai']

class BanzoufenleiView(APIView):
    # throttle_classes = [MySimpleRateThrottle,]
    # parser_classes = [JSONParser,FormParser]
    def get(self,request,*args,**kwargs):
        id =kwargs.get('pk')
        if id:
            obj=models.Banzoufenlei.objects.filter(id=id).first()
            ser=Banzoufenleiserializer(instance=obj,many=False)
        else:
            pgination =MyLimitOffsetPagination()
            obj =models.Banzoufenlei.objects.all()
            obj= pgination.paginate_queryset(obj,request,view=self)
            ser = Banzoufenleilistserializer(instance=obj,context={'request':request},many=True)
            return pgination.get_paginated_response(ser.data)
        return Response({'code':1,'msg':'susee','data':ser.data})

    def post(self,request,*args,**kwargs):
        data=request.data
        print(data)
        ser = Banzoufenleiserializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({'code':1,'msg':'save sucessed','data':ser.validated_data})
        else:
            print(ser.errors)
            Response({'code':0,'msg':'Failed'})
        return Response({'code':1})

    def delete(self,request,*args,**kwargs):
        #......com/?sign='123'
        id=request.query_params.get('id')
        if id:
            try:
                obj=models.Banzoufenlei.objects.get(id=id)
                obj.delete()
                return Response({'code':1,'msg':'delete sucessed'})
            except models.Banzoufenlei.DoesNotExist as err:
                print(err)
                return Response({'code':0,'msg':'该数值不存在'})
        return Response({'code':0,'msg':'缺少必要参数'})

    def put(self,request,*args,**kwargs):
        data = request.data
        id = data['id']
        try:
            obj = models.Banzoufenlei.objects.get(id=id)
            ser = Banzoufenleiserializer(obj,data=data)
            if ser.is_valid():
                ser.save()
                return Response({'code':1,'msg':'put sucesssed'})
            else:
                print('更新失败')
                return Response({'code':1,'msg':'put failed'})
        except models.Banzoufenlei.DoesNotExist as err:
            print(err)
            return Response({'code':0,'msg':'put faild data not exists'})
    def patch(self,request,*args,**kwargs):
        data = request.data
        id = data['id']
        try:
            obj = models.Banzoufenlei.objects.get(id=id)
            ser = Banzoufenleiserializer(obj, data=data,partial=True)
            if ser.is_valid():
                ser.save()
                return Response({'code': 1, 'msg': 'patch sucesssed'})
            else:
                print('更新失败')
                return Response({'code': 1, 'msg': 'patch failed'})
        except models.Banzoufenlei.DoesNotExist as err:
            print(err)
            return Response({'code': 0, 'msg': 'patch faild data not exists'})

class GedancontentinfoView(APIView):
    # throttle_classes = [MySimpleRateThrottle,]
    # parser_classes = [JSONParser,FormParser]
    def get(self,request,*args,**kwargs):
        id =kwargs.get('pk')
        if id:
            obj=models.Gedancontentinfo.objects.filter(id=id).first()
            ser=Gedancontentinfoserializer(instance=obj,many=False)
        else:
            pgination =MyLimitOffsetPagination()
            obj =models.Gedancontentinfo.objects.all()
            obj= pgination.paginate_queryset(obj,request,view=self)
            ser = Gedancontentinfolistserializer(instance=obj,context={'request':request},many=True)
            return pgination.get_paginated_response(ser.data)
        return Response({'code':1,'msg':'susee','data':ser.data})

    def post(self,request,*args,**kwargs):
        data=request.data
        print(data)
        ser = Gedancontentinfoserializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({'code':1,'msg':'save sucessed','data':ser.validated_data})
        else:
            print(ser.errors)
            Response({'code':0,'msg':'Failed'})

        return Response({'code':1})

    def delete(self,request,*args,**kwargs):
        #......com/?sign='123'
        id=request.query_params.get('id')
        if id:
            try:
                obj=models.Gedancontentinfo.objects.get(id=id)
                obj.delete()
                return Response({'code':1,'msg':'delete sucessed'})
            except models.Gedancontentinfo.DoesNotExist as err:
                print(err)
                return Response({'code':0,'msg':'该数值不存在'})
        return Response({'code':0,'msg':'缺少必要参数'})

    def put(self,request,*args,**kwargs):
        data = request.data
        id = data['id']
        try:
            obj = models.Gedancontentinfo.objects.get(id=id)
            ser = Gedancontentinfoserializer(obj,data=data)
            if ser.is_valid():
                ser.save()
                return Response({'code':1,'msg':'put sucesssed'})
            else:
                print('更新失败')
                return Response({'code':1,'msg':'put failed'})
        except models.Gedancontentinfo.DoesNotExist as err:
            print(err)
            return Response({'code':0,'msg':'put faild data not exists'})
    def patch(self,request,*args,**kwargs):
        data = request.data
        id = data['id']
        try:
            obj = models.Gedancontentinfo.objects.get(id=id)
            ser = Gedancontentinfoserializer(obj, data=data,partial=True)
            if ser.is_valid():
                ser.save()
                return Response({'code': 1, 'msg': 'patch sucesssed'})
            else:
                print('更新失败')
                return Response({'code': 1, 'msg': 'patch failed'})
        except models.Gedancontentinfo.DoesNotExist as err:
            print(err)
            return Response({'code': 0, 'msg': 'patch faild data not exists'})

class GedaninfoView(APIView):
    # throttle_classes = [MySimpleRateThrottle,]
    # parser_classes = [JSONParser,FormParser]
    def get(self,request,*args,**kwargs):
        id = kwargs.get('pk')
        print(id)
        if id:
            obj=models.Gedaninfo.objects.filter(id=id).first()
            ser=Gedaninfoserializer(instance=obj,many=False)
        else:
            pgination =MyLimitOffsetPagination()
            obj =models.Gedaninfo.objects.all()
            obj= pgination.paginate_queryset(obj,request,view=self)
            ser = Gedaninfolistserializer(instance=obj,context={'request':request},many=True)

            return pgination.get_paginated_response(ser.data)
        return Response({'code':1,'msg':'susee','data':ser.data})

    def post(self,request,*args,**kwargs):

        data=request.data
        print(data)
        ser = Gedaninfoserializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({'code':1,'msg':'save sucessed','data':ser.validated_data})
        else:
            print(ser.errors)
            Response({'code':0,'msg':'Failed'})

        return Response({'code':1})

    def delete(self,request,*args,**kwargs):
        #......com/?sign='123'
        id=request.query_params.get('id')
        if id:
            try:
                obj=models.Gedaninfo.objects.get(id=id)
                obj.delete()
                return Response({'code':1,'msg':'delete sucessed'})
            except models.Gedaninfo.DoesNotExist as err:
                print(err)
                return Response({'code':0,'msg':'该数值不存在'})
        return Response({'code':0,'msg':'缺少必要参数'})

    def put(self,request,*args,**kwargs):
        data = request.data
        id = data['id']
        try:
            obj = models.Gedaninfo.objects.get(id=id)
            ser = Gedaninfoserializer(obj,data=data)
            if ser.is_valid():
                ser.save()
                return Response({'code':1,'msg':'put sucesssed'})
            else:
                print('更新失败')
                return Response({'code':1,'msg':'put failed'})
        except models.Gedaninfo.DoesNotExist as err:
            print(err)
            return Response({'code':0,'msg':'put faild data not exists'})
    def patch(self,request,*args,**kwargs):
        data = request.data
        id = data['id']
        try:
            obj = models.Gedaninfo.objects.get(id=id)
            ser = Gedaninfoserializer(obj, data=data,partial=True)
            if ser.is_valid():
                ser.save()
                return Response({'code': 1, 'msg': 'patch sucesssed'})
            else:
                print('更新失败')
                return Response({'code': 1, 'msg': 'patch failed'})
        except models.Gedaninfo.DoesNotExist as err:
            print(err)
            return Response({'code': 0, 'msg': 'patch faild data not exists'})


class GedancontentinfoView(APIView):
    # throttle_classes = [MySimpleRateThrottle,]
    # parser_classes = [JSONParser,FormParser]
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        if id:
            obj = models.Gedancontentinfo.objects.filter(id=id).first()
            ser = Gedancontentinfoserializer(instance=obj, many=False)
        else:
            pgination = MyLimitOffsetPagination()
            obj = models.Gedancontentinfo.objects.all()
            obj = pgination.paginate_queryset(obj, request, view=self)
            ser = Gedancontentinfolistserializer(instance=obj, context={'request': request}, many=True)

            return pgination.get_paginated_response(ser.data)
        return Response({'code': 1, 'msg': 'susee', 'data': ser.data})

    def post(self, request, *args, **kwargs):

        data = request.data
        print(data)
        ser = Gedancontentinfoserializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({'code': 1, 'msg': 'save sucessed', 'data': ser.validated_data})
        else:
            print(ser.errors)
            Response({'code': 0, 'msg': 'Failed'})

        return Response({'code': 1})

    def delete(self, request, *args, **kwargs):
        # ......com/?sign='123'
        id = request.query_params.get('id')
        if id:
            try:
                obj = models.Gedancontentinfo.objects.get(id=id)
                obj.delete()
                return Response({'code': 1, 'msg': 'delete sucessed'})
            except models.Gedancontentinfo.DoesNotExist as err:
                print(err)
                return Response({'code': 0, 'msg': '该数值不存在'})
        return Response({'code': 0, 'msg': '缺少必要参数'})

    def put(self, request, *args, **kwargs):
        data = request.data
        id = data['id']
        try:
            obj = models.Gedancontentinfo.objects.get(id=id)
            ser = Gedancontentinfoserializer(obj, data=data)
            if ser.is_valid():
                ser.save()
                return Response({'code': 1, 'msg': 'put sucesssed'})
            else:
                print('更新失败')
                return Response({'code': 1, 'msg': 'put failed'})
        except models.Gedancontentinfo.DoesNotExist as err:
            print(err)
            return Response({'code': 0, 'msg': 'put faild data not exists'})

    def patch(self, request, *args, **kwargs):
        data = request.data
        id = data['id']
        try:
            obj = models.Gedancontentinfo.objects.get(id=id)
            ser = Gedancontentinfoserializer(obj, data=data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response({'code': 1, 'msg': 'patch sucesssed'})
            else:
                print('更新失败')
                return Response({'code': 1, 'msg': 'patch failed'})
        except models.Gedancontentinfo.DoesNotExist as err:
            print(err)
            return Response({'code': 0, 'msg': 'patch faild data not exists'})


class YuanchuangcontentView(APIView):
    # throttle_classes = [MySimpleRateThrottle,]
    # parser_classes = [JSONParser,FormParser]
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        if id:
            obj = models.Yuanchuangcontent.objects.filter(id=id).first()
            ser =Yuanchuangcontentserializer(instance=obj, many=False)
        else:
            pgination = MyLimitOffsetPagination()
            obj = models.Yuanchuangcontent.objects.all()
            obj = pgination.paginate_queryset(obj, request, view=self)
            ser = Yuanchuanglistcontentserializer(instance=obj, context={'request': request}, many=True)

            return pgination.get_paginated_response(ser.data)
        return Response({'code': 1, 'msg': 'susee', 'data': ser.data})

    def post(self, request, *args, **kwargs):

        data = request.data
        print(data)
        ser = Yuanchuangcontentserializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({'code': 1, 'msg': 'save sucessed', 'data': ser.validated_data})
        else:
            print(ser.errors)
            Response({'code': 0, 'msg': 'Failed'})

        return Response({'code': 1})

    def delete(self, request, *args, **kwargs):
        # ......com/?sign='123'
        id = request.query_params.get('id')
        if id:
            try:
                obj = models.Yuanchuangcontent.objects.get(id=id)
                obj.delete()
                return Response({'code': 1, 'msg': 'delete sucessed'})
            except models.Yuanchuangcontent.DoesNotExist as err:
                print(err)
                return Response({'code': 0, 'msg': '该数值不存在'})
        return Response({'code': 0, 'msg': '缺少必要参数'})

    def put(self, request, *args, **kwargs):
        data = request.data
        id = data['id']
        try:
            obj = models.Yuanchuangcontent.objects.get(id=id)
            ser = Yuanchuangcontentserializer(obj, data=data)
            if ser.is_valid():
                ser.save()
                return Response({'code': 1, 'msg': 'put sucesssed'})
            else:
                print('更新失败')
                return Response({'code': 1, 'msg': 'put failed'})
        except models.Yuanchuangcontent.DoesNotExist as err:
            print(err)
            return Response({'code': 0, 'msg': 'put faild data not exists'})

    def patch(self, request, *args, **kwargs):
        data = request.data
        id = data['id']
        try:
            obj = models.Yuanchuangcontent.objects.get(id=id)
            ser = Yuanchuangcontentserializer(obj, data=data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response({'code': 1, 'msg': 'patch sucesssed'})
            else:
                print('更新失败')
                return Response({'code': 1, 'msg': 'patch failed'})
        except models.Yuanchuangcontent.DoesNotExist as err:
            print(err)
            return Response({'code': 0, 'msg': 'patch faild data not exists'})

class YunachuangfenleiView(APIView):
    # throttle_classes = [MySimpleRateThrottle,]
    # parser_classes = [JSONParser,FormParser]
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        if id:
            obj = models.Yunachuangfenlei.objects.filter(id=id).first()
            ser =Yunachuangfenleiserializer(instance=obj, many=False)
        else:
            pgination = MyLimitOffsetPagination()
            obj = models.Yunachuangfenlei.objects.all()
            obj = pgination.paginate_queryset(obj, request, view=self)
            ser = Yunachuanglistfenleiserializer(instance=obj, context={'request': request}, many=True)

            return pgination.get_paginated_response(ser.data)
        return Response({'code': 1, 'msg': 'susee', 'data': ser.data})

    def post(self, request, *args, **kwargs):

        data = request.data
        print(data)
        ser = Yunachuangfenleiserializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({'code': 1, 'msg': 'save sucessed', 'data': ser.validated_data})
        else:
            print(ser.errors)
            Response({'code': 0, 'msg': 'Failed'})

        return Response({'code': 1})

    def delete(self, request, *args, **kwargs):
        # ......com/?sign='123'
        id = request.query_params('id')
        if id:
            try:
                obj = models.Yunachuangfenlei.objects.get(id=id)
                obj.delete()
                return Response({'code': 1, 'msg': 'delete sucessed'})
            except models.Yunachuangfenlei.DoesNotExist as err:
                print(err)
                return Response({'code': 0, 'msg': '该数值不存在'})
        return Response({'code': 0, 'msg': '缺少必要参数'})

    def put(self, request, *args, **kwargs):
        data = request.data
        id = data['id']
        try:
            obj = models.Yunachuangfenlei.objects.get(id=id)
            ser = Yunachuangfenleiserializer(obj, data=data)
            if ser.is_valid():
                ser.save()
                return Response({'code': 1, 'msg': 'put sucesssed'})
            else:
                print('更新失败')
                return Response({'code': 1, 'msg': 'put failed'})
        except models.Yunachuangfenlei.DoesNotExist as err:
            print(err)
            return Response({'code': 0, 'msg': 'put faild data not exists'})

    def patch(self, request, *args, **kwargs):
        data = request.data
        id = data['id']
        try:
            obj = models.Yunachuangfenlei.objects.get(id=id)
            ser = Yunachuangfenleiserializer(obj, data=data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response({'code': 1, 'msg': 'patch sucesssed'})
            else:
                print('更新失败')
                return Response({'code': 1, 'msg': 'patch failed'})
        except models.Yunachuangfenlei.DoesNotExist as err:
            print(err)
            return Response({'code': 0, 'msg': 'patch faild data not exists'})