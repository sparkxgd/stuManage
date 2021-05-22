{
    "code"
:
    0
        , "msg"
:
    ""
        , "data"
:
    [{
        "title": "主页"
        , "icon": "layui-icon-home"
        , "name": "homepage1"
        , "jump": "home/homepage1"
    },
        {
            "name": "base"
            , "title": "基础数据管理"
            , "icon": "layui-icon-template"
            , "list": [{
                "name": "school"
                , "title": "学校信息管理"
            }, {
                "name": "class"
                , "title": "班级信息管理"
            }, {
                "name": "student"
                , "title": "学生信息管理"
            }]
        },
        {
            "name": "user"
            , "title": "用户"
            , "icon": "layui-icon-user"
            , "list": [{
                "name": "user"
                , "title": "用户管理"
            }, {
                "name": "administrators-rule"
                , "title": "角色管理"
                , "jump": "user/administrators/role"
            }]
        },
        {
            "name": "baiduAI"
            , "title": "百度AI"
            , "icon": "layui-icon-face-smile-b"
            , "list": [
                {
                    "name": "detect"
                    , "title": "人脸检测"
                }, {
                    "name": "match"
                    , "title": "人脸比对"
                }
            ]
        },
        {
            "name": "set"
            , "title": "设置"
            , "icon": "layui-icon-set"
            , "list": [{
                "name": "user"
                , "title": "我的设置"
                , "spread": true
                , "list": [{
                    "name": "info"
                    , "title": "基本资料"
                }, {
                    "name": "password"
                    , "title": "修改密码"
                }]
            }]
        }]
}