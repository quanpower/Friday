(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-06c951f4"],{"236a":function(t,e,a){},"2a58":function(t,e,a){"use strict";a.r(e);var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"mixin-components-container"},[a("el-row",[a("el-card",{staticClass:"box-card"},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("span",[t._v("Buttons")])]),t._v(" "),a("div",{staticStyle:{"margin-bottom":"50px"}},[a("el-col",{staticClass:"text-center",attrs:{span:4}},[a("router-link",{staticClass:"pan-btn blue-btn",attrs:{to:"/documentation/index"}},[t._v("Documentation")])],1),t._v(" "),a("el-col",{staticClass:"text-center",attrs:{span:4}},[a("router-link",{staticClass:"pan-btn light-blue-btn",attrs:{to:"/icon/index"}},[t._v("Icons")])],1),t._v(" "),a("el-col",{staticClass:"text-center",attrs:{span:4}},[a("router-link",{staticClass:"pan-btn pink-btn",attrs:{to:"/excel/export-excel"}},[t._v("Excel")])],1),t._v(" "),a("el-col",{staticClass:"text-center",attrs:{span:4}},[a("router-link",{staticClass:"pan-btn green-btn",attrs:{to:"/table/complex-table"}},[t._v("Table")])],1),t._v(" "),a("el-col",{staticClass:"text-center",attrs:{span:4}},[a("router-link",{staticClass:"pan-btn tiffany-btn",attrs:{to:"/example/create"}},[t._v("Form")])],1),t._v(" "),a("el-col",{staticClass:"text-center",attrs:{span:4}},[a("router-link",{staticClass:"pan-btn yellow-btn",attrs:{to:"/theme/index"}},[t._v("Theme")])],1)],1)])],1),t._v(" "),a("el-row",{staticStyle:{"margin-top":"50px"},attrs:{gutter:20}},[a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"box-card"},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("span",[t._v("Material Design 的input")])]),t._v(" "),a("div",{staticStyle:{height:"100px"}},[a("el-form",{attrs:{model:t.demo,rules:t.demoRules}},[a("el-form-item",{attrs:{prop:"title"}},[a("md-input",{attrs:{icon:"search",name:"title",placeholder:"输入标题"},model:{value:t.demo.title,callback:function(e){t.$set(t.demo,"title",e)},expression:"demo.title"}},[t._v("标题")])],1)],1)],1)])],1),t._v(" "),a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"box-card"},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("span",[t._v("图片hover效果")])]),t._v(" "),a("div",{staticClass:"component-item"},[a("pan-thumb",{attrs:{width:"100px",height:"100px",image:"https://wpimg.wallstcn.com/577965b9-bb9e-4e02-9f0c-095b41417191"}},[t._v("\n            vue-element-admin\n          ")])],1)])],1),t._v(" "),a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"box-card"},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("span",[t._v("水波纹 waves v-directive")])]),t._v(" "),a("div",{staticClass:"component-item"},[a("el-button",{directives:[{name:"waves",rawName:"v-waves"}],attrs:{type:"primary"}},[t._v("水波纹效果")])],1)])],1),t._v(" "),a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"box-card"},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("span",[t._v("hover text")])]),t._v(" "),a("div",{staticClass:"component-item"},[a("mallki",{attrs:{"class-name":"mallki-text",text:"vue-element-admin"}})],1)])],1)],1),t._v(" "),a("el-row",{staticStyle:{"margin-top":"50px"},attrs:{gutter:20}},[a("el-col",{attrs:{span:8}},[a("el-card",{staticClass:"box-card"},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("span",[t._v("Share")])]),t._v(" "),a("div",{staticClass:"component-item",staticStyle:{height:"420px"}},[a("dropdown-menu",{staticStyle:{margin:"0 auto"},attrs:{items:t.articleList,title:"系列文章"}})],1)])],1)],1)],1)},l=[],i=a("3cbc"),n=a("1aba"),r=a("137c"),c=a("7c70"),o=a("6724"),d={name:"ComponentMixinDemo",components:{PanThumb:i["a"],MdInput:n["a"],Mallki:r["a"],DropdownMenu:c["a"]},directives:{waves:o["a"]},data:function(){var t=function(t,e,a){6!==e.length?a(new Error("请输入六个字符")):a()};return{demo:{title:""},demoRules:{title:[{required:!0,trigger:"change",validator:t}]},articleList:[{title:"基础篇",href:"https://juejin.im/post/59097cd7a22b9d0065fb61d2"},{title:"登录权限篇",href:"https://juejin.im/post/591aa14f570c35006961acac"},{title:"实战篇",href:"https://juejin.im/post/593121aa0ce4630057f70d35"},{title:"vue-admin-template 篇",href:"https://juejin.im/post/595b4d776fb9a06bbe7dba56"},{title:"优雅的使用 icon",href:"https://juejin.im/post/59bb864b5188257e7a427c09"}]}}},p=d,v=(a("4b4d"),a("2877")),m=Object(v["a"])(p,s,l,!1,null,"aa7ce150",null);e["default"]=m.exports},"4b4d":function(t,e,a){"use strict";var s=a("236a"),l=a.n(s);l.a},6724:function(t,e,a){"use strict";a("8d41");var s="@@wavesContext";function l(t,e){function a(a){var s=Object.assign({},e.value),l=Object.assign({ele:t,type:"hit",color:"rgba(0, 0, 0, 0.15)"},s),i=l.ele;if(i){i.style.position="relative",i.style.overflow="hidden";var n=i.getBoundingClientRect(),r=i.querySelector(".waves-ripple");switch(r?r.className="waves-ripple":(r=document.createElement("span"),r.className="waves-ripple",r.style.height=r.style.width=Math.max(n.width,n.height)+"px",i.appendChild(r)),l.type){case"center":r.style.top=n.height/2-r.offsetHeight/2+"px",r.style.left=n.width/2-r.offsetWidth/2+"px";break;default:r.style.top=(a.pageY-n.top-r.offsetHeight/2-document.documentElement.scrollTop||document.body.scrollTop)+"px",r.style.left=(a.pageX-n.left-r.offsetWidth/2-document.documentElement.scrollLeft||document.body.scrollLeft)+"px"}return r.style.backgroundColor=l.color,r.className="waves-ripple z-active",!1}}return t[s]?t[s].removeHandle=a:t[s]={removeHandle:a},a}var i={bind:function(t,e){t.addEventListener("click",l(t,e),!1)},update:function(t,e){t.removeEventListener("click",t[s].removeHandle,!1),t.addEventListener("click",l(t,e),!1)},unbind:function(t){t.removeEventListener("click",t[s].removeHandle,!1),t[s]=null,delete t[s]}},n=function(t){t.directive("waves",i)};window.Vue&&(window.waves=i,Vue.use(n)),i.install=n;e["a"]=i},"8d41":function(t,e,a){}}]);