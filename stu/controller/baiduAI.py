'''
百度ia
2020年5月17日23:00:46
西瓜刀
'''
import requests
import json

# 人脸注册
def face_add(img_base64,group_id,user_id,user_info):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
    params = {}
    params["image"] = img_base64
    params["image_type"] = "BASE64"
    params["group_id"] = group_id
    params["user_id"] = user_id
    params["user_info"] = user_info
    params["quality_control"] = "LOW"
    # params["liveness_control"] = "NORMAL"
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        result = response.json()
    return result["result"]


# 人脸更新
def face_update(img_base64,group_id,user_id,user_info):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/update"
    params = {}
    params["image"] = img_base64
    params["image_type"] = "BASE64"
    params["group_id"] = group_id
    params["user_id"] = user_id
    params["user_info"] = user_info
    params["quality_control"] = "LOW"
    # params["liveness_control"] = "NORMAL"
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        result = response.json()
    return result["result"]


# 人脸删除
def face_delete(group_id,user_id,face_token):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/delete"
    params = {}
    params["group_id"] = group_id
    params["user_id"] = user_id
    params["face_token"] = face_token
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        result = response.json()
    return result


# 获取access_token
def get_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    client_id = "rADsnyOHCGscAsCnWXIGWue0"
    client_secret = "ij6Tskx9jmdWBhKTRv7nLxcH6esCl6g6"
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+client_id+'&client_secret='+client_secret
    response = requests.get(host)
    return response.json()["access_token"]


# 人脸基础检测
def face_detect_base(img_base64):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    params = {}
    params["image"] = img_base64
    params["image_type"] = "BASE64"
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    return response.json()["result"]


def face_detect(img_base64):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    params = {}
    params["image"] = img_base64
    params["image_type"] = "BASE64"
    params["face_field"] = "age,beauty,expression,face_shape,gender,glasses,race,quality"
    params["max_face_num"] = 5
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    return response.json()


# 人脸对比
def face_match(img1_base64,img2_base64):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
    params1 = {}
    params1["image"] = img1_base64
    params1["image_type"] = "BASE64"
    # params1["face_type"] = "LIVE"
    # params1["quality_control"] = "LOW"

    params2 = {}
    params2["image"] = img2_base64
    params2["image_type"] = "BASE64"
    # params1["face_type"] = "LIVE"
    # params1["quality_control"] = "LOW"

    params = []
    params.append(params1)
    params.append(params2)

    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    r = requests.post(request_url, data=json.dumps(params), headers=headers)
    return r.json()


# 人脸搜索
def face_search(img_base64,group_id_list):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
    params = {}
    params["image"] = img_base64
    params["image_type"] = "BASE64"
    params["group_id_list"] = group_id_list
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    r = requests.post(request_url, data=params, headers=headers)
    return r.json()
