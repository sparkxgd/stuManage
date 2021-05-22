/** layuiAdmin.pro-v1.2.1 LPPL License By http://www.layui.com/admin/ */
 ;layui.define(["table","form","jquery"],function(e){
     var i=(layui.$,layui.admin),t=layui.view,$=layui.jquery,l=layui.table,r=layui.form;

         l.render({
             elem:"#LAY-base-school-manage",
             url:"/school/list/",
             cols:[[
                 {type:"checkbox",fixed:"left"},
                 {field:"id",width:80,title:"ID",sort:!0},
                 {field:"schoolname",title:"学校名称"},
                 {field:"code",title:"代码"},
                 {field:"addr",title:"地址"},
                 {field:"desc",title:"详情"},
                 {field:"updtime",title:"更新时间",sort:!0},{
                 field:"status",title:"审核状态",templet:"#buttonTpl",minWidth:80,align:"center"},
                 {title:"操作",width:150,align:"center",fixed:"right",toolbar:"#table-useradmin-admin"}
                 ]],
                page:!0,
                limit:10,
                limits:[10,15,20,25,30],
             text:"对不起，加载出现异常！"}),
         l.on("tool(LAY-base-school-manage)",function(e){
             "del"===e.event?layer.prompt({formType:1,title:"敏感操作，请验证口令"},function(i,t){layer.close(t),
                     layer.confirm("确定删除此信息？",function(i){
                         $.ajax({
                                type:"post",
                                url:"/school/delete/",
                                data:{"id":e.data.id},
                                dataType:"json",
                                success:function (r) {
                                     layer.alert(r.msg);
                                     layui.table.reload("LAY-base-school-manage");
                                }
                              });
                             layer.close(i)})}):
                 "edit"===e.event&&i.popup({title:"编辑学校信息",area:['530px', '560px'],id:"LAY-popup-school-add",success:function(e,i){t(this.id).render("base/school/add",l).done(function(){r.render(null,"layuiadmin-form-admin"),
                         r.on("submit(LAY-base-school-submit)",function(e){
                            $.ajax({
                                            type:"post",
                                            url:"/school/edit/",
                                            data:e.field,
                                            dataType:"json",
                                            success:function (r) {
                                                layer.alert(r.msg);
                                                layui.table.reload("LAY-base-school-manage");
                                            }
                                         });
                                layer.close(i)})})}})}),


          l.render({
             elem:"#LAY-base-class-manage",
             url:"/class/list/",
             cols:[[
                 {type:"checkbox",fixed:"left"},
                 {field:"id",width:80,title:"ID",sort:!0},
                 {field:"classname",title:"班级名称"},
                 {field:"desc",title:"详情"},
                 {field:"updtime",title:"更新时间",sort:!0},{
                 field:"status",title:"审核状态",templet:"#buttonTpl",minWidth:80,align:"center"},
                 {title:"操作",width:150,align:"center",fixed:"right",toolbar:"#table-useradmin-admin"}
                 ]],
                page:!0,
                limit:10,
                limits:[10,15,20,25,30],
             text:"对不起，加载出现异常！"}),
         l.on("tool(LAY-base-class-manage)",function(e){
             var l=e.data;
             "del"===e.event?layer.prompt({formType:1,title:"敏感操作，请验证口令"},function(i,t){layer.close(t),
                     layer.confirm("确定删除此信息？",function(i){
                         $.ajax({
                                type:"post",
                                url:"/class/delete/",
                                data:{"id":e.data.id},
                                dataType:"json",
                                success:function (r) {
                                     layer.alert(r.msg);
                                     layui.table.reload("LAY-base-class-manage");
                                }
                              });
                             layer.close(i)})}):
                 "edit"===e.event&&i.popup(
                     {
                         title:"编辑班级信息",
                         area:['530px', '560px'],
                         id:"LAY-popup-class-add",success:function(e,i){
                             t(this.id).render("base/class/add",l).done(function(){
                                 r.render(null,"layuiadmin-form-admin"),
                                     r.on("submit(LAY-base-class-submit)",function(e){
                                         $.ajax({
                                            type:"post",
                                            url:"/class/edit/",
                                            data:e.field,
                                            dataType:"json",
                                            success:function (r) {
                                                layer.alert(r.msg);
                                                layui.table.reload("LAY-base-class-manage");
                                            }
                                         });
                                             layer.close(i)})})}})}),
             e("base",{})});
