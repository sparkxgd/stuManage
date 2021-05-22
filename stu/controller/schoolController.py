'''
学校信息管理
2020年5月2日09:30:49
西瓜刀
'''
from stu.models import School
from django.http.response import JsonResponse
from datetime import datetime
import json


#   获取信息列表
def getlist(request):
    #   获取页面提交的数据
    page = int(request.GET.get("page"))
    limit = int(request.GET.get("limit"))
    schoolname = request.GET.get("schoolname")
    if schoolname:
        #   到数据库去查找数据
        values = School.objects.filter(schoolname__contains=schoolname)[(page-1)*limit:limit*page].values()
        datas = list(values)
        total = School.objects.filter(schoolname__contains=schoolname).count()
    else:
        #   到数据库去查找数据
        values = School.objects.all()[(page-1)*limit:limit*page].values()
        datas = list(values)
        total = School.objects.all().count()
    result = {"code": 0, "msg": "查询成功", "count": total, "data": datas}
    return JsonResponse(result)


#   添加
def add(request):
    result = {"code": 0, "msg": "保存成功！"}
    #   获取前端的数据
    schoolname = request.POST.get("schoolname")
    code = request.POST.get("code")
    addr = request.POST.get("addr")
    desc = request.POST.get("desc")
    #   赋值
    m = School()
    m.schoolname = schoolname
    m.code = code
    m.addr = addr
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
    schoolname = request.POST.get("schoolname")
    code = request.POST.get("code")
    addr = request.POST.get("addr")
    desc = request.POST.get("desc")
    updtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #   更新
    School.objects.filter(id=id).update(schoolname=schoolname,code=code,addr=addr,desc=desc,updtime=updtime)
    return JsonResponse(result)


#   删除
def delete(request):
    result = {"code": 0, "msg": "删除成功！"}
    #   获取前端的数据
    id = request.POST.get("id")
    School.objects.filter(id=id).delete()
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
    School.objects.filter(id__in=ids_list).delete()
    return JsonResponse(result)

