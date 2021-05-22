'''
班级信息管理
2020年5月3日10:59:00
西瓜刀
'''
from stu.models import Classinfo as Mo
from django.http.response import JsonResponse
from datetime import datetime
import json


#   获取信息列表
def getlist(request):
    #   获取页面提交的数据
    page = int(request.GET.get("page"))
    limit = int(request.GET.get("limit"))
    classname = request.GET.get("classname")
    if classname:
        #   到数据库去查找数据
        values = Mo.objects.filter(classname__contains=classname)[(page-1)*limit:limit*page].values()
        datas = list(values)
        total = Mo.objects.filter(classname__contains=classname).count()
    else:
        #   到数据库去查找数据
        values = Mo.objects.all()[(page-1)*limit:limit*page].values()
        datas = list(values)
        total = Mo.objects.all().count()
    result = {"code": 0, "msg": "查询成功", "count": total, "data": datas}
    return JsonResponse(result)


#   添加
def add(request):
    result = {"code": 0, "msg": "保存成功！"}
    #   获取前端的数据
    classname = request.POST.get("classname")
    desc = request.POST.get("desc")
    #   赋值
    m = Mo()
    m.classname = classname
    m.desc = desc
    m.updtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #   保存
    m.save()
    return JsonResponse(result)


#   修改、编辑
def edit(request):
    result = {"code": 0, "msg": "修改成功！"}
    #   获取前端的数据
    id = request.POST.get("id")
    classname = request.POST.get("classname")
    desc = request.POST.get("desc")
    updtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #   更新
    Mo.objects.filter(id=id).update(classname=classname,desc=desc,updtime=updtime)
    return JsonResponse(result)


#   删除
def delete(request):
    result = {"code": 0, "msg": "删除成功！"}
    #   获取前端的数据
    id = request.POST.get("id")
    Mo.objects.filter(id=id).delete()
    return JsonResponse(result)


#   批量删除
def batchdel(request):
    result = {"code": 0, "msg": "删除成功！"}
    #   获取前端的数据
    ids = request.POST.get("ids")
    #   转化成json数据
    ids_json = json.loads(ids)
    #   转换成列表
    ids_list = []
    for m in ids_json:
        ids_list.append(m["id"])
    Mo.objects.filter(id__in=ids_list).delete()
    return JsonResponse(result)

