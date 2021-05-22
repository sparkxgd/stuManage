'''
图片上传
2020年5月17日23:36:26
西瓜刀
'''
import base64
from stu.controller import baiduAI
from django.http.response import JsonResponse


def upload_face_detect(request):
    # 获取上传图片(二进制文件)
    img = request.FILES['file']
    img_base64 = base64.b64encode(img.read()).decode()
    r = baiduAI.face_detect_base(img_base64)
    n = r["face_num"]
    if n > 0:
        result = {"code": 0, "msg": "成功", "result": {"code": 0, "msg": "成功检测到人脸"}}
    else:
        result = {"code": 0, "msg": "成功", "result": {"code": -1, "msg": "检测不到人脸"}}
    return JsonResponse(result)


# 检测人脸的基本信息(图片信息是json)
def face_detect_base_json(request):
    # 获取上传图片
    img = request.POST.get("img")
    img_base64 = img.replace("data:image/jpeg;base64,", "")
    r = baiduAI.face_detect_base(img_base64)
    result = {"code": 0, "msg": "成功", "result": {"code": -1, "msg": "检测不到人脸", "face": r}}
    if r:
        n = r["face_num"]
        if n > 0:
            result = {"code": 0, "msg": "成功", "result": {"code": 0, "msg": "成功检测到人脸", "face": r}}
    return JsonResponse(result)


# 识别人脸所有信息
def face_detect(request):
    # 获取上传图片
    img = request.FILES['file']
    img_base64 = base64.b64encode(img.read()).decode()
    # 到百度ai去检测
    r = baiduAI.face_detect(img_base64)
    # 分析检测的结果
    ai_result = r["result"]
    result = {"code": 0, "msg": "", "ai": ai_result}
    return JsonResponse(result)


# 人脸对比
def face_match(request):
    # 获取上传图片
    img1 = request.POST.get("img1")
    img2 = request.POST.get("img2")
    img1_base64 = img1.replace("data:image/jpeg;base64,", "")
    img2_base64 = img2.replace("data:image/jpeg;base64,", "")
    # 到百度ai去检测
    r = baiduAI.face_match(img1_base64, img2_base64)
    # 分析检测的结果
    ai_result = r["result"]
    result = {"code": 0, "msg": "", "ai": ai_result}
    return JsonResponse(result)