(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-fced8294"],{"2a2d":function(e,t,a){},"2b1b":function(e,t,a){"use strict";a.d(t,"c",function(){return n}),a.d(t,"b",function(){return l}),a.d(t,"d",function(){return s}),a.d(t,"a",function(){return o});var i=a("b775");function n(e){return Object(i["a"])({url:"booking/bookings/",method:"get",params:e})}function l(e){return Object(i["a"])({url:"booking/bookings/".concat(e,"/"),method:"get"})}function s(e,t){return Object(i["a"])({url:"booking/bookings/".concat(e,"/"),method:"put",data:t})}function o(e){return Object(i["a"])({url:"booking/bookings/",method:"post",data:e})}},"3daa":function(e,t,a){"use strict";var i=a("4563"),n=a.n(i);n.a},"3dad":function(e,t,a){"use strict";var i=a("d366"),n=a.n(i);n.a},4563:function(e,t,a){},"67ac":function(e,t,a){"use strict";var i=a("75f9"),n=a.n(i);n.a},"75f9":function(e,t,a){},"8d41":function(e,t,a){},9406:function(e,t,a){"use strict";a.r(t);var i=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"dashboard-container"},[a("el-row",{attrs:{gutter:8}},[a("el-col",{staticStyle:{"margin-bottom":"30px","padding-top":"10px"},attrs:{xs:{span:24},sm:{span:12},md:{span:10},lg:{span:4},xl:{span:4}}},[a("company-panel")],1),e._v(" "),a("el-col",{staticStyle:{"margin-bottom":"30px"},attrs:{xs:{span:24},sm:{span:12},md:{span:14},lg:{span:20},xl:{span:20}}},[a("tab-view")],1)],1)],1)},n=[],l=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("el-card",{staticClass:"box-card-component"},[a("div",{staticClass:"box-card-header",attrs:{slot:"header"},slot:"header"},[a("img",{attrs:{src:"http://www.luxos.com/cn/media/k2/items/cache/5d9bd784bfd234610bf8ba15e7ad6a4e_XL.jpg"}})]),e._v(" "),a("div",{staticStyle:{position:"relative"}},[a("div",{staticClass:"progress-item",staticStyle:{"padding-top":"5px"}},[a("span",{staticStyle:{"font-size":"18px"}},[e._v(e._s(e.company.name))])]),e._v(" "),a("div",{staticClass:"progress-item",staticStyle:{"padding-top":"15px"}},[a("span",[e._v("Phone:")]),e._v(" "),a("span",[e._v(e._s(e.company.phone))])]),e._v(" "),a("div",{staticClass:"progress-item",staticStyle:{"padding-top":"15px"}},[a("span",[e._v("Tel:")]),e._v(" "),a("span",[e._v(e._s(e.company.tel))])]),e._v(" "),a("div",{staticClass:"progress-item",staticStyle:{"padding-top":"15px"}},[a("span",[e._v("Email:")]),e._v(" "),a("span",[e._v(e._s(e.company.email))])]),e._v(" "),a("div",{staticClass:"progress-item",staticStyle:{"padding-top":"15px"}},[a("span",[e._v("Address:")]),e._v(" "),a("span",[e._v(e._s(e.company.address))])]),e._v(" "),a("div",{staticClass:"progress-item",staticStyle:{"padding-top":"15px"}},[a("span",[e._v("Discount:")]),e._v(" "),e.company.discount?a("span",[e._v(e._s(e.discount))]):a("span",[e._v("None")])])])])},s=[],o={filters:{statusFilter:function(e){var t={success:"success",pending:"danger"};return t[e]}},computed:{discount:{get:function(){if(this.company&&this.company.discount)return this.company.discount>0?100*this.company.discount+"% for free":"no discount"}}},data:function(){return{company:this.$store.getters.user.company}}},r=o,c=(a("3dad"),a("67ac"),a("2877")),u=Object(c["a"])(r,l,s,!1,null,"6733d10d",null),d=u.exports,p=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("el-tabs",{model:{value:e.activeTabName,callback:function(t){e.activeTabName=t},expression:"activeTabName"}},[a("el-tab-pane",{attrs:{label:"All Booking",name:"all",lazy:""}}),e._v(" "),a("el-tab-pane",{attrs:{label:"My Booking",name:"my",lazy:""}}),e._v(" "),a("el-tab-pane",{attrs:{label:"Vehicle",name:"vehicle",lazy:""}}),e._v(" "),a("el-tab-pane",{attrs:{label:"Guide",name:"guide",lazy:""}}),e._v(" "),a("el-tab-pane",{attrs:{label:"Users",name:"user",lazy:""}})],1),e._v(" "),a(e.activeTabName,{tag:"component",attrs:{tabName:e.activeTabName,query:e.get_queryset()}})],1)},m=[],f=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",{staticClass:"filter-container"},[a("el-input",{staticClass:"filter-item",staticStyle:{width:"240px"},attrs:{placeholder:""},nativeOn:{keyup:function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.handleFilter(t)}},model:{value:e.listQuery.search,callback:function(t){e.$set(e.listQuery,"search",t)},expression:"listQuery.search"}}),e._v(" "),a("el-date-picker",{staticClass:"filter-item",attrs:{type:"datetime",format:"yyyy-MM-dd HH:mm",placeholder:"Start Time:"},model:{value:e.listQuery.start_time,callback:function(t){e.$set(e.listQuery,"start_time",t)},expression:"listQuery.start_time"}}),e._v(" "),a("el-date-picker",{staticClass:"filter-item",attrs:{type:"datetime",format:"yyyy-MM-dd HH:mm",placeholder:"End Time:"},model:{value:e.listQuery.end_time,callback:function(t){e.$set(e.listQuery,"end_time",t)},expression:"listQuery.end_time"}}),e._v(" "),a("el-select",{staticClass:"filter-item",attrs:{placeholder:"Status",clearable:""},on:{change:e.handleFilter},model:{value:e.listQuery.status,callback:function(t){e.$set(e.listQuery,"status",t)},expression:"listQuery.status"}},e._l(e.options,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}),1),e._v(" "),a("el-button",{staticClass:"filter-item",attrs:{type:"primary",icon:"el-icon-search"},on:{click:e.handleFilter}},[e._v("\n      Search\n    ")]),e._v(" "),a("el-button",{staticClass:"filter-item",attrs:{type:"primary",icon:"el-icon-edit"},on:{click:e.handleCreate}},[e._v("\n      Add\n    ")])],1),e._v(" "),a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.listLoading,expression:"listLoading"}],key:e.tableKey,staticStyle:{width:"100%"},attrs:{data:e.list,border:"",stripe:"",fit:"","highlight-current-row":"","row-key":"id"}},[a("el-table-column",{attrs:{prop:"bookingId",label:"BookingId",width:"220px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("router-link",{staticClass:"link-type",attrs:{to:"/booking/edit/"+i.id}},[a("span",[e._v(e._s(i.bookingId))])])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Start Time",width:"160px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("router-link",{staticClass:"link-type",attrs:{to:"/booking/edit/"+i.id}},[a("span",[e._v(e._s(e._f("moment")(i.start_time,"YYYY-MM-DD HH:mm")))])])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"End Time",width:"160px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("router-link",{staticClass:"link-type",attrs:{to:"/booking/edit/"+i.id}},[a("span",[e._v(e._s(e._f("moment")(i.end_time,"YYYY-MM-DD HH:mm")))])])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Creator","min-width":"120px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("router-link",{staticClass:"link-type",attrs:{to:"/booking/edit/"+i.id}},[i.create_by?a("span",[e._v(e._s(i.create_by.name||i.create_by.username))]):e._e()])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Vehicle","min-width":"120px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("router-link",{staticClass:"link-type",attrs:{to:"/booking/edit/"+i.id}},[i.vehicle?a("span",[e._v(e._s(i.vehicle.traffic_plate_no))]):e._e()])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Guide","min-width":"120px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("router-link",{staticClass:"link-type",attrs:{to:"/booking/edit/"+i.id}},[i.guide?a("span",[e._v(e._s(i.guide.name||i.guide.username))]):e._e()])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Status",width:"100px","class-name":"status-col",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("el-tag",{attrs:{type:e._f("typeStatus")(i.status)}},[e._v("\n          "+e._s(i.status)+"\n        ")])]}}])})],1),e._v(" "),a("pagination",{directives:[{name:"show",rawName:"v-show",value:e.total>0,expression:"total>0"}],attrs:{total:e.total,page:e.listQuery.page,limit:e.listQuery.limit},on:{"update:page":function(t){return e.$set(e.listQuery,"page",t)},"update:limit":function(t){return e.$set(e.listQuery,"limit",t)},pagination:e.getList}})],1)},v=[],h=a("2b1b"),g=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"pagination-container",class:{hidden:e.hidden}},[a("el-pagination",e._b({attrs:{background:e.background,"current-page":e.currentPage,"page-size":e.pageSize,layout:e.layout,"page-sizes":e.pageSizes,total:e.total},on:{"update:currentPage":function(t){e.currentPage=t},"update:current-page":function(t){e.currentPage=t},"update:pageSize":function(t){e.pageSize=t},"update:page-size":function(t){e.pageSize=t},"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}},"el-pagination",e.$attrs,!1))],1)},y=[];a("c5f6");Math.easeInOutQuad=function(e,t,a,i){return e/=i/2,e<1?a/2*e*e+t:(e--,-a/2*(e*(e-2)-1)+t)};var b=function(){return window.requestAnimationFrame||window.webkitRequestAnimationFrame||window.mozRequestAnimationFrame||function(e){window.setTimeout(e,1e3/60)}}();function _(e){document.documentElement.scrollTop=e,document.body.parentNode.scrollTop=e,document.body.scrollTop=e}function k(){return document.documentElement.scrollTop||document.body.parentNode.scrollTop||document.body.scrollTop}function w(e,t,a){var i=k(),n=e-i,l=20,s=0;t="undefined"===typeof t?500:t;var o=function e(){s+=l;var o=Math.easeInOutQuad(s,i,n,t);_(o),s<t?b(e):a&&"function"===typeof a&&a()};o()}var x={name:"Pagination",props:{total:{required:!0,type:Number},page:{type:Number,default:1},limit:{type:Number,default:20},pageSizes:{type:Array,default:function(){return[10,20,30,50,100]}},layout:{type:String,default:"total, sizes, prev, pager, next, jumper"},background:{type:Boolean,default:!0},autoScroll:{type:Boolean,default:!0},hidden:{type:Boolean,default:!1}},computed:{currentPage:{get:function(){return this.page},set:function(e){this.$emit("update:page",e)}},pageSize:{get:function(){return this.limit},set:function(e){this.$emit("update:limit",e)}}},methods:{handleSizeChange:function(e){this.$emit("pagination",{page:this.currentPage,limit:e}),this.autoScroll&&w(0,800)},handleCurrentChange:function(e){this.$emit("pagination",{page:e,limit:this.pageSize}),this.autoScroll&&w(0,800)}}},S=x,C=(a("3daa"),Object(c["a"])(S,g,y,!1,null,"48241e4c",null)),$=C.exports,L=[{value:"Created",label:"Created"},{value:"Process",label:"Process"},{value:"Complete",label:"Complete"},{value:"Cancel",label:"Cancel"},{value:"Delete",label:"Delete"}],O={components:{Pagination:$},props:{query:{type:Object,default:{page:1,limit:20,search:void 0,start_time:void 0,end_time:void 0,status:void 0,create_by:void 0}}},filters:{typeStatus:function(e){var t={Created:"success",Cancel:"danger",Process:"warning",Complete:"primary"};return t[e]}},data:function(){return{tableKey:0,total:0,list:null,listLoading:!0,options:L,listQuery:Object.assign({},this.query)}},created:function(){this.getList()},methods:{getList:function(){var e=this;this.listLoading=!0,Object(h["c"])(this.listQuery).then(function(t){e.list=t.data.items,e.total=t.data.total,e.listLoading=!1}).catch(function(){e.listLoading=!1})},handleFilter:function(){this.listQuery.page=1,this.listQuery.list=null,this.getList()},handleCreate:function(){this.$router.push({path:"/booking/create/"})},mounted:function(){}}},j=O,N=Object(c["a"])(j,f,v,!1,null,null,null),F=N.exports,T=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.listLoading,expression:"listLoading"}],key:e.tableKey,attrs:{data:e.list,border:"",stripe:"",fit:"","highlight-current-row":""}},[a("el-table-column",{attrs:{label:"UserName",align:"center",width:"180px"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",[e._v(e._s(i.username))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Name",align:"center",width:"120px"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",[e._v(e._s(i.name))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Phone",width:"120px",align:"center","class-name":"small-padding fixed-width"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",[e._v(e._s(i.phone))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Email",width:"180px",align:"center","class-name":"small-padding fixed-width"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",[e._v(e._s(i.email))])]}}])})],1),e._v(" "),a("pagination",{directives:[{name:"show",rawName:"v-show",value:e.total>0,expression:"total>0"}],attrs:{total:e.total,page:e.listQuery.page,limit:e.listQuery.limit},on:{"update:page":function(t){return e.$set(e.listQuery,"page",t)},"update:limit":function(t){return e.$set(e.listQuery,"limit",t)},pagination:e.getList}}),e._v(" "),a("el-dialog",{attrs:{title:e.textMap[e.dialogStatus],visible:e.dialogFormVisible},on:{"update:visible":function(t){e.dialogFormVisible=t}}},[a("el-form",{ref:"dataForm",staticStyle:{width:"400px","margin-left":"20px"},attrs:{rules:e.rules,model:e.temp,"label-position":"left","label-width":"100px"}},[a("el-form-item",{attrs:{label:"UserName:",prop:"username"}},[a("el-input",{attrs:{disabled:""},model:{value:e.temp.username,callback:function(t){e.$set(e.temp,"username",t)},expression:"temp.username"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"Name:",prop:"name"}},[a("el-input",{model:{value:e.temp.name,callback:function(t){e.$set(e.temp,"name",t)},expression:"temp.name"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"Phone:",prop:"phone"}},[a("el-input",{model:{value:e.temp.phone,callback:function(t){e.$set(e.temp,"phone",t)},expression:"temp.phone"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"Email:",prop:"email"}},[a("el-input",{model:{value:e.temp.email,callback:function(t){e.$set(e.temp,"email",t)},expression:"temp.email"}})],1)],1),e._v(" "),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.dialogFormVisible=!1}}},[e._v("\n        Cancel\n      ")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:function(t){"create"===e.dialogStatus?e.createData():e.updateData()}}},[e._v("\n        Confirm\n      ")])],1)],1)],1)},E=[],Q=(a("ac4d"),a("8a81"),a("ac6a"),a("7f7f"),a("c24f")),q=(a("8d41"),"@@wavesContext");function z(e,t){function a(a){var i=Object.assign({},t.value),n=Object.assign({ele:e,type:"hit",color:"rgba(0, 0, 0, 0.15)"},i),l=n.ele;if(l){l.style.position="relative",l.style.overflow="hidden";var s=l.getBoundingClientRect(),o=l.querySelector(".waves-ripple");switch(o?o.className="waves-ripple":(o=document.createElement("span"),o.className="waves-ripple",o.style.height=o.style.width=Math.max(s.width,s.height)+"px",l.appendChild(o)),n.type){case"center":o.style.top=s.height/2-o.offsetHeight/2+"px",o.style.left=s.width/2-o.offsetWidth/2+"px";break;default:o.style.top=(a.pageY-s.top-o.offsetHeight/2-document.documentElement.scrollTop||document.body.scrollTop)+"px",o.style.left=(a.pageX-s.left-o.offsetWidth/2-document.documentElement.scrollLeft||document.body.scrollLeft)+"px"}return o.style.backgroundColor=n.color,o.className="waves-ripple z-active",!1}}return e[q]?e[q].removeHandle=a:e[q]={removeHandle:a},a}var P={bind:function(e,t){e.addEventListener("click",z(e,t),!1)},update:function(e,t){e.removeEventListener("click",e[q].removeHandle,!1),e.addEventListener("click",z(e,t),!1)},unbind:function(e){e.removeEventListener("click",e[q].removeHandle,!1),e[q]=null,delete e[q]}},H=function(e){e.directive("waves",P)};window.Vue&&(window.waves=P,Vue.use(H)),P.install=H;var V=P,M=(a("ed08"),a("b775"));function A(e){return Object(M["a"])({url:"role/roles/",method:"get",params:e})}function D(e,t){return Object(M["a"])({url:"role/roles/".concat(e,"/"),method:"put",data:t})}function G(e){return Object(M["a"])({url:"role/roles/",method:"post",data:e})}var U={components:{Pagination:$},directives:{waves:V},props:{query:{type:Object,default:{page:1,limit:20,search:void 0,company:void 0}}},data:function(){return{tableKey:0,list:null,total:0,listLoading:!0,listQuery:Object.assign({},this.query),temp:{id:void 0,name:void 0,phone:void 0,email:void 0,role_id:void 0,company_id:this.$store.getters.user.company.id},textMap:{update:"Edit",create:"Create"},dialogFormVisible:!1,dialogStatus:"",rules:{},role:{data:[],loading:!1,role_id:[]}}},created:function(){this.getList()},methods:{userRole:function(e){return e.role.map(function(e){return e.name}).join(",")},getList:function(){var e=this;this.listLoading=!0,Object(Q["b"])(this.listQuery).then(function(t){e.list=t.data.items,e.total=t.data.total,e.listLoading=!1}).catch(function(){e.listLoading=!1})},handleFilter:function(){this.listQuery.page=1,this.getList()},handleChangeStatus:function(e,t){var a=this;this.listLoading=!0;var i={id:e.id,username:e.username};i[t]=e[t],Object(Q["e"])(e.id,i).then(function(e){a.listLoading=!1,a.$notify({title:"Success",message:"Change Successfully",type:"success",duration:2e3})}).catch(function(){e[t]=!e[t],a.listLoading=!1})},handleCreate:function(){var e=this;this.temp={id:void 0,name:void 0,phone:void 0,email:void 0,role_id:void 0,company_id:this.$store.getters.user.company.id},0==this.role.data.length&&(this.role.loading=!0,A({company:this.$store.getters.user.company.id}).then(function(t){e.role.data=t.data,e.role.loading=!1}).catch(function(t){e.role.loading=!1})),this.dialogStatus="create",this.dialogFormVisible=!0,this.$nextTick(function(){e.$refs["dataForm"].clearValidate()})},handleUpdate:function(e){var t=this;this.temp=Object.assign({},{id:e.id,username:e.username,name:e.name,email:e.email,phone:e.phone,role_id:e.role.map(function(e){return e.id}),company_id:this.$store.getters.user.company.id}),0==this.role.data.length&&(this.role.loading=!0,A({company:this.$store.getters.user.company.id}).then(function(e){t.role.data=e.data,t.role.loading=!1}).catch(function(e){t.role.loading=!1})),this.dialogStatus="update",this.dialogFormVisible=!0,this.$nextTick(function(){t.$refs["dataForm"].clearValidate()})},updateData:function(){var e=this;this.$refs["dataForm"].validate(function(t){t&&Object(Q["e"])(e.temp.id,e.temp).then(function(t){var a=t.data,i=!0,n=!1,l=void 0;try{for(var s,o=e.list[Symbol.iterator]();!(i=(s=o.next()).done);i=!0){var r=s.value;if(r.id===a.id){var c=e.list.indexOf(r);e.list.splice(c,1,a);break}}}catch(u){n=!0,l=u}finally{try{i||null==o.return||o.return()}finally{if(n)throw l}}e.dialogFormVisible=!1,e.$notify({title:"Success",message:"Update Successfully",type:"success",duration:2e3})})})}}},Y=U,B=Object(c["a"])(Y,T,E,!1,null,null,null),K=B.exports,I=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",{staticClass:"filter-container"},[a("el-button",{staticClass:"filter-item",staticStyle:{"margin-left":"10px"},attrs:{type:"primary",icon:"el-icon-edit"},on:{click:e.handleCreate}},[e._v("\n      Add\n    ")])],1),e._v(" "),a("div",[a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.list.loading,expression:"list.loading"}],attrs:{data:e.list.data,border:"",stripe:""}},[a("el-table-column",{attrs:{label:"Name",align:"center",width:"180px"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",{staticClass:"link-type",on:{click:function(t){return e.handleUpdate(i)}}},[e._v(e._s(i.name))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Name",align:"center",width:"180px"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",{staticClass:"link-type",on:{click:function(t){return e.handleUpdate(i)}}},[e._v(e._s(e.rolePermission(i)))])]}}])})],1)],1),e._v(" "),a("div",[a("el-dialog",{directives:[{name:"loading",rawName:"v-loading",value:e.dialog.loading,expression:"dialog.loading"}],attrs:{title:e.dialog.title,visible:e.dialog.visible,width:"55%"},on:{"update:visible":function(t){return e.$set(e.dialog,"visible",t)}}},[a("el-form",{ref:"roleForm",staticStyle:{width:"600px","margin-left":"20px"},attrs:{model:e.temp,rules:e.dialog.rules,"label-width":"80px","label-position":"left"}},[a("el-form-item",{attrs:{label:"Name:",prop:"name"}},[a("el-input",{model:{value:e.temp.name,callback:function(t){e.$set(e.temp,"name",t)},expression:"temp.name"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"Permission:",prop:"permission"}},[a("el-transfer",{attrs:{data:e.permission,titles:["Source","Target"]},on:{change:e.handlePermissionChange},model:{value:e.temp.permission_id,callback:function(t){e.$set(e.temp,"permission_id",t)},expression:"temp.permission_id"}})],1)],1),e._v(" "),a("span",{attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.dialog.visible=!1}}},[e._v("Cancel")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:function(t){"Edit"===e.dialog.title?e.updateForm():e.createForm()}}},[e._v("Confirm")])],1)],1)],1)])},R=[];function J(){return Object(M["a"])({url:"permission/permissions/",method:"get"})}var W={created:function(){this.getList()},data:function(){return{list:{loading:!1,data:[]},permission:[],listFilter:{company:this.$store.getters.user.company.id},dialog:{title:"Edit",visible:!1,data:void 0,loading:!1,rules:{name:[{required:!0,message:"This fields is required",trigger:"change"}]}},temp:{id:void 0,name:"",permission_id:[],company_id:this.$store.getters.user.company.id}}},methods:{rolePermission:function(e){return e.permission.map(function(e){return e.label}).join(",")},getList:function(){var e=this;this.list.loading=!0,A(this.listFilter).then(function(t){e.list.loading=!1,e.list.data=t.data}).catch(function(t){e.list.loading=!1})},handleUpdate:function(e){var t=this;this.dialog.visible=!0,this.dialog.title="Edit",this.temp=Object.assign({},{id:e.id,name:e.name,permission_id:e.permission.map(function(e){return e.key}),company_id:this.$store.getters.user.company.id}),0==this.permission.length&&(this.dialog.loading=!0,J().then(function(e){t.dialog.loading=!1,t.permission=e.data}).catch(function(e){t.dialog.loading=!1})),this.$nextTick(function(){t.$refs["roleForm"].clearValidate()})},updateForm:function(){var e=this;this.$refs["roleForm"].validate(function(t){t&&D(e.temp.id,e.temp).then(function(t){var a=t.data;e.dialog.visible=!1;var i=!0,n=!1,l=void 0;try{for(var s,o=e.list.data[Symbol.iterator]();!(i=(s=o.next()).done);i=!0){var r=s.value;if(r.id===a.id){var c=e.list.data.indexOf(r);e.list.data.splice(c,1,a);break}}}catch(u){n=!0,l=u}finally{try{i||null==o.return||o.return()}finally{if(n)throw l}}e.$notify({title:"Success",message:"Update Successfully",type:"success",duration:2e3})}).catch(function(t){e.dialog.visible=!1})})},handleCreate:function(){var e=this;this.temp={id:void 0,name:"",permission_id:[],company_id:this.$store.getters.user.company.id},this.dialog.visible=!0,this.dialog.title="Create",0==this.permission.length&&(this.dialog.loading=!0,J().then(function(t){e.dialog.loading=!1,e.permission=t.data}).catch(function(t){e.dialog.loading=!1})),this.$nextTick(function(){e.$refs["roleForm"].clearValidate()})},createForm:function(){var e=this;this.$refs["roleForm"].validate(function(t){t&&(console.log(e.temp),G(e.temp).then(function(t){e.dialog.visible=!1}).catch(function(t){e.dialog.visible=!1}))})}}},X=W,Z=Object(c["a"])(X,I,R,!1,null,null,null),ee=(Z.exports,function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",{staticClass:"filter-container"},[a("el-input",{staticClass:"filter-item",staticStyle:{width:"240px"},attrs:{placeholder:""},nativeOn:{keyup:function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.handleFilter(t)}},model:{value:e.query.search,callback:function(t){e.$set(e.query,"search",t)},expression:"query.search"}}),e._v(" "),a("el-button",{staticClass:"filter-item",attrs:{type:"primary"},on:{click:e.loadVehicles}},[e._v("Search")])],1),e._v(" "),a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.vehicleLoading,expression:"vehicleLoading"}],key:e.tableKey,staticStyle:{width:"100%"},attrs:{data:e.vehicleList,border:"",stripe:"",fit:"","highlight-current-row":""}},[a("el-table-column",{attrs:{label:"Traffic Number",align:"center","min-width":"120px"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",[e._v(e._s(i.traffic_plate_no))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Brand",align:"center",width:"120px"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",[e._v(e._s(i.model.brand.name))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Model",align:"center","min-width":"120px"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",[e._v(e._s(i.model.name))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Year",align:"center",width:"120px"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",[e._v(e._s(i.model.year))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Type",align:"center",width:"120px"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",[e._v(e._s(i.model.type))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Category",align:"center","min-width":"120px"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",[e._v(e._s(i.model.category))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Passengers",align:"center",width:"120px"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",[e._v(e._s(i.model.passengers))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Average Score",width:"130px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",[e._v(e._s(i.avg_score))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Total Score",width:"130px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",[e._v(e._s(i.total_score))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Active",width:"130px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("el-checkbox",{attrs:{disabled:""},model:{value:i.is_actived,callback:function(t){e.$set(i,"is_actived",t)},expression:"row.is_actived"}})]}}])})],1),e._v(" "),a("pagination",{directives:[{name:"show",rawName:"v-show",value:e.total>0,expression:"total>0"}],attrs:{total:e.total,page:e.query.page,limit:e.query.limit},on:{"update:page":function(t){return e.$set(e.query,"page",t)},"update:limit":function(t){return e.$set(e.query,"limit",t)},pagination:e.loadVehicles}})],1)}),te=[],ae=a("fbb2"),ie={components:{Pagination:$},data:function(){return{tableKey:0,total:0,query:{model:void 0,limit:20,page:1,search:void 0},vehicleList:[],modelLoading:!1,vehicleLoading:!1}},created:function(){this.loadVehicles()},methods:{loadVehicles:function(){var e=this;this.vehicleLoading=!0,this.vehicleList=[],Object(ae["b"])(this.query).then(function(t){e.vehicleList=t.data.items,e.total=t.data.total,e.vehicleLoading=!1}).catch(function(t){e.vehicleLoading=!1})},handleFilter:function(){this.query.page=1,this.vehicleList=[],this.loadVehicles()}}},ne=ie,le=Object(c["a"])(ne,ee,te,!1,null,null,null),se=le.exports,oe=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.loading,expression:"loading"}],key:e.tableKey,staticStyle:{width:"100%"},attrs:{data:e.list,border:"",stripe:"",fit:"","highlight-current-row":""}},[a("el-table-column",{attrs:{label:"UserName",align:"center",width:"180px"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",{staticClass:"link-type",on:{click:function(t){return e.selectGuideHandle(i)}}},[e._v(e._s(i.username))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Name",align:"center",width:"120px"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",{staticClass:"link-type",on:{click:function(t){return e.selectGuideHandle(i)}}},[e._v(e._s(i.name))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Phone",width:"120px",align:"center","class-name":"small-padding fixed-width"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",{staticClass:"link-type",on:{click:function(t){return e.selectGuideHandle(i)}}},[e._v(e._s(i.phone))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Company",width:"200px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[i.company?a("span",{staticClass:"link-type",on:{click:function(t){return e.selectGuideHandle(i)}}},[e._v(e._s(i.company.name))]):e._e()]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Average Score",width:"130px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",{staticClass:"link-type",on:{click:function(t){return e.selectGuideHandle(i)}}},[e._v(e._s(i.avg_score))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Total Score",width:"130px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",{staticClass:"link-type",on:{click:function(t){return e.selectGuideHandle(i)}}},[e._v(e._s(i.total_score))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Introduction","min-width":"150px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.row;return[a("span",{staticClass:"link-type",on:{click:function(t){return e.selectGuideHandle(i)}}},[e._v(e._s(i.introduction))])]}}])})],1)],1)},re=[],ce={data:function(){return{query:{is_actived:!0,is_tourguide:!0},list:[],loading:!1}},created:function(){this.loadGuides()},methods:{loadGuides:function(){var e=this;this.loading=!0,this.list=[],Object(Q["b"])(this.query).then(function(t){e.list=t.data,e.loading=!1}).catch(function(t){e.loading=!1})}}},ue=ce,de=Object(c["a"])(ue,oe,re,!1,null,null,null),pe=de.exports,me={components:{all:F,my:F,user:K,vehicle:se,guide:pe},data:function(){return{activeTabName:"all",all:"all",month:"month",my:"my",user:"user",role:"role",vehicle:"vehicle",guide:"guide",monthTitle:this.$moment().format("MMM")+" Booking"}},methods:{get_queryset:function(){switch(this.activeTabName){case"all":return{page:1,limit:20,search:void 0,start_time:void 0,end_time:void 0,status:void 0,create_by:void 0};case"month":return{page:1,limit:20,search:void 0,status:void 0,create_by:void 0,start_time:this.$moment().startOf("month").format(),end_time:this.$moment().endOf("month").format()};case"my":return{page:1,limit:20,search:void 0,start_time:void 0,end_time:void 0,status:void 0,create_by:this.$store.getters.user.id};case"user":return{page:1,limit:20,search:void 0,company:this.$store.getters.user.company.id}}}}},fe=me,ve=Object(c["a"])(fe,p,m,!1,null,null,null),he=ve.exports,ge={name:"Dashboard",components:{CompanyPanel:d,TabView:he}},ye=ge,be=(a("af54"),Object(c["a"])(ye,i,n,!1,null,null,null));t["default"]=be.exports},af54:function(e,t,a){"use strict";var i=a("2a2d"),n=a.n(i);n.a},d366:function(e,t,a){},fbb2:function(e,t,a){"use strict";a.d(t,"b",function(){return n}),a.d(t,"a",function(){return l});var i=a("b775");function n(e){return Object(i["a"])({url:"vehicle/vehicles/",method:"get",params:e})}function l(e){return Object(i["a"])({url:"vehicle/models/",method:"get",params:e})}}}]);