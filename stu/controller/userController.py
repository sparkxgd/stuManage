'''
用户信息管理
2020年5月5日10:15:35
西瓜刀
'''
from stu.models import User as Mo
from django.http.response import JsonResponse
from datetime import datetime
import json
from stu.controller import baiduAI


#   获取信息列表
def getlist(request):
    #   获取页面提交的数据
    page = int(request.GET.get("page"))
    limit = int(request.GET.get("limit"))
    username = request.GET.get("username")
    if username:
        #   到数据库去查找数据
        values = Mo.objects.filter(username__contains=username)[(page-1)*limit:limit*page].values()
        datas = list(values)
        total = Mo.objects.filter(username__contains=username).count()
    else:
        #   到数据库去查找数据
        values = Mo.objects.all()[(page-1)*limit:limit*page].values()
        datas = list(values)
        total = Mo.objects.all().count()
    result = {"code": 0, "msg": "查询成功", "count": total, "data": datas}
    return JsonResponse(result)


#   添加
def add(request):
    result = {"code": 0, "msg": "保存成功！","info":{"code": 0, "msg": "保存成功！"}}
    #   获取前端的数据
    username = request.POST.get("username")
    password = request.POST.get("password")
    nickname = request.POST.get("nickname")
    pho = request.POST.get("pho")
    num = Mo.objects.filter(username=username).count()
    if num > 0:
        result["info"]["code"] = -1
        result["info"]["msg"] =username+ "用户名已经存在！！"
    else:
        group_id = "student"
        img_base64 = pho.split(",")[1]
        # replace("data:image/jpeg;base64,", "")
        # 将人类注册到百度人脸库
        r = baiduAI.face_add(img_base64, group_id, username, nickname)
        if r:
            face_token = r["face_token"]
            #   赋值
            m = Mo()
            m.username = username
            m.password = password
            m.nickname = nickname
            m.pho = pho
            m.group_id = group_id
            m.face_token = face_token
            m.updtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #   保存
            m.save()
        else:
            result["info"]["code"] = -1
            result["info"]["msg"] = "百度注册人脸失败！"
    return JsonResponse(result)


#   修改、编辑
def edit(request):
    result = {"code": 0, "msg": "修改成功！","info":{"code": 0, "msg": "更新成功！"}}
    #   获取前端的数据
    id = request.POST.get("id")
    username = request.POST.get("username")
    password = request.POST.get("password")
    nickname = request.POST.get("nickname")
    pho = request.POST.get("pho")
    updtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    group_id = "student"
    img_base64 = pho.split(",")[1]
    r = baiduAI.face_update(img_base64, group_id, username, nickname)
    if r:
        face_token = r["face_token"]
        #   更新数据库
        Mo.objects.filter(id=id).update(group_id=group_id,password=password,nickname=nickname,pho=pho,face_token=face_token,updtime=updtime)
    else:
        result["info"]["code"] = -1
        result["info"]["msg"] = "百度更新人脸失败！"
    return JsonResponse(result)


#   删除
def delete(request):
    result = {"code": 0, "msg": "删除失败！","info": {"code": -1, "msg": "删除失败！"}}
    #   获取前端的数据
    id = request.POST.get("id")
    # 到数据库去把数据拿过来
    values = Mo.objects.filter(id=id).values()
    data = list(values)[0]
    group_id = data["group_id"]
    user_id = data["username"]
    face_token = data["face_token"]
    r = baiduAI.face_delete(group_id, user_id, face_token)
    error_code = r["error_code"]
    if error_code == 0:
        Mo.objects.filter(id=id).delete()
        result["info"]["code"] = 0
        result["info"]["msg"] = "删除人脸成功！"
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

