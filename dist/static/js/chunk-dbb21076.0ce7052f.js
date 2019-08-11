(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-dbb21076"],{2017:function(t,n,e){"use strict";var s=e("3b76"),a=e.n(s);a.a},"28dd":function(t,n,e){},"3b76":function(t,n,e){},"590b":function(t,n,e){},"9ed6":function(t,n,e){"use strict";e.r(n);var s=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("div",{staticClass:"login-container"},[e("el-form",{ref:"loginForm",staticClass:"login-form",attrs:{model:t.loginForm,rules:t.loginRules,autocomplete:"on","label-position":"left"}},[e("div",{staticClass:"title-container"},[e("h3",{staticClass:"title"},[t._v("\n        "+t._s(t.$t("login.title"))+"\n      ")]),t._v(" "),e("lang-select",{staticClass:"set-language"})],1),t._v(" "),e("el-form-item",{attrs:{prop:"username"}},[e("span",{staticClass:"svg-container"},[e("svg-icon",{attrs:{"icon-class":"user"}})],1),t._v(" "),e("el-input",{ref:"username",attrs:{placeholder:t.$t("login.username"),name:"username",type:"text",tabindex:"1",autocomplete:"on"},model:{value:t.loginForm.username,callback:function(n){t.$set(t.loginForm,"username",n)},expression:"loginForm.username"}})],1),t._v(" "),e("el-tooltip",{attrs:{content:"Caps lock is On",placement:"right",manual:""},model:{value:t.capsTooltip,callback:function(n){t.capsTooltip=n},expression:"capsTooltip"}},[e("el-form-item",{attrs:{prop:"password"}},[e("span",{staticClass:"svg-container"},[e("svg-icon",{attrs:{"icon-class":"password"}})],1),t._v(" "),e("el-input",{key:t.passwordType,ref:"password",attrs:{type:t.passwordType,placeholder:t.$t("login.password"),name:"password",tabindex:"2",autocomplete:"on"},on:{blur:function(n){t.capsTooltip=!1}},nativeOn:{keyup:[function(n){return t.checkCapslock(n)},function(n){return!n.type.indexOf("key")&&t._k(n.keyCode,"enter",13,n.key,"Enter")?null:t.handleLogin(n)}]},model:{value:t.loginForm.password,callback:function(n){t.$set(t.loginForm,"password",n)},expression:"loginForm.password"}}),t._v(" "),e("span",{staticClass:"show-pwd",on:{click:t.showPwd}},[e("svg-icon",{attrs:{"icon-class":"password"===t.passwordType?"eye":"eye-open"}})],1)],1)],1),t._v(" "),e("el-button",{staticStyle:{width:"100%","margin-bottom":"30px"},attrs:{loading:t.loading,type:"primary"},nativeOn:{click:function(n){return n.preventDefault(),t.handleLogin(n)}}},[t._v("\n      "+t._s(t.$t("login.logIn"))+"\n    ")]),t._v(" "),e("div",{staticStyle:{position:"relative"}},[e("div",{staticClass:"tips"},[e("span",[t._v(t._s(t.$t("login.username"))+" : admin")]),t._v(" "),e("span",[t._v(t._s(t.$t("login.password"))+" : "+t._s(t.$t("login.any")))])]),t._v(" "),e("div",{staticClass:"tips"},[e("span",{staticStyle:{"margin-right":"18px"}},[t._v("\n          "+t._s(t.$t("login.username"))+" : editor\n        ")]),t._v(" "),e("span",[t._v(t._s(t.$t("login.password"))+" : "+t._s(t.$t("login.any")))])]),t._v(" "),e("el-button",{staticClass:"thirdparty-button",attrs:{type:"primary"},on:{click:function(n){t.showDialog=!0}}},[t._v("\n        "+t._s(t.$t("login.thirdparty"))+"\n      ")])],1)],1),t._v(" "),e("el-dialog",{attrs:{title:t.$t("login.thirdparty"),visible:t.showDialog},on:{"update:visible":function(n){t.showDialog=n}}},[t._v("\n    "+t._s(t.$t("login.thirdpartyTips"))+"\n    "),e("br"),t._v(" "),e("br"),t._v(" "),e("br"),t._v(" "),e("social-sign")],1)],1)},a=[],o=(e("ac6a"),e("456d"),e("61f7")),i=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("el-dropdown",{staticClass:"international",attrs:{trigger:"click"},on:{command:t.handleSetLanguage}},[e("div",[e("svg-icon",{attrs:{"class-name":"international-icon","icon-class":"language"}})],1),t._v(" "),e("el-dropdown-menu",{attrs:{slot:"dropdown"},slot:"dropdown"},[e("el-dropdown-item",{attrs:{disabled:"zh"===t.language,command:"zh"}},[t._v("\n      中文\n    ")]),t._v(" "),e("el-dropdown-item",{attrs:{disabled:"en"===t.language,command:"en"}},[t._v("\n      English\n    ")]),t._v(" "),e("el-dropdown-item",{attrs:{disabled:"es"===t.language,command:"es"}},[t._v("\n      Español\n    ")]),t._v(" "),e("el-dropdown-item",{attrs:{disabled:"ja"===t.language,command:"ja"}},[t._v("\n      日本語\n    ")])],1)],1)},r=[],l={computed:{language:function(){return this.$store.getters.language}},methods:{handleSetLanguage:function(t){this.$i18n.locale=t,this.$store.dispatch("app/setLanguage",t),this.$message({message:"Switch Language Success",type:"success"})}}},c=l,d=e("2877"),u=Object(d["a"])(c,i,r,!1,null,null,null),p=u.exports,g=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("div",{staticClass:"social-signup-container"},[e("div",{staticClass:"sign-btn",on:{click:function(n){return t.wechatHandleClick("wechat")}}},[e("span",{staticClass:"wx-svg-container"},[e("svg-icon",{staticClass:"icon",attrs:{"icon-class":"wechat"}})],1),t._v("\n    WeChat\n  ")]),t._v(" "),e("div",{staticClass:"sign-btn",on:{click:function(n){return t.tencentHandleClick("tencent")}}},[e("span",{staticClass:"qq-svg-container"},[e("svg-icon",{staticClass:"icon",attrs:{"icon-class":"qq"}})],1),t._v("\n    QQ\n  ")])])},h=[],m={name:"SocialSignin",methods:{wechatHandleClick:function(t){alert("ok")},tencentHandleClick:function(t){alert("ok")}}},v=m,f=(e("d9fb"),Object(d["a"])(v,g,h,!1,null,"7309fbbb",null)),w=f.exports,_={name:"Login",components:{LangSelect:p,SocialSign:w},data:function(){var t=function(t,n,e){Object(o["e"])(n)?e():e(new Error("Please enter the correct user name"))},n=function(t,n,e){n.length<6?e(new Error("The password can not be less than 6 digits")):e()};return{loginForm:{username:"admin",password:"111111"},loginRules:{username:[{required:!0,trigger:"blur",validator:t}],password:[{required:!0,trigger:"blur",validator:n}]},passwordType:"password",capsTooltip:!1,loading:!1,showDialog:!1,redirect:void 0,otherQuery:{}}},watch:{$route:{handler:function(t){var n=t.query;n&&(this.redirect=n.redirect,this.otherQuery=this.getOtherQuery(n))},immediate:!0}},created:function(){},mounted:function(){""===this.loginForm.username?this.$refs.username.focus():""===this.loginForm.password&&this.$refs.password.focus()},destroyed:function(){},methods:{checkCapslock:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},n=t.shiftKey,e=t.key;e&&1===e.length&&(this.capsTooltip=!!(n&&e>="a"&&e<="z"||!n&&e>="A"&&e<="Z")),"CapsLock"===e&&!0===this.capsTooltip&&(this.capsTooltip=!1)},showPwd:function(){var t=this;"password"===this.passwordType?this.passwordType="":this.passwordType="password",this.$nextTick(function(){t.$refs.password.focus()})},handleLogin:function(){var t=this;this.$refs.loginForm.validate(function(n){if(!n)return console.log("error submit!!"),!1;t.loading=!0,t.$store.dispatch("user/login",t.loginForm).then(function(){t.$router.push({path:t.redirect||"/",query:t.otherQuery}),t.loading=!1}).catch(function(){t.loading=!1}),t.$store.dispatch("user/getInfo")})},getOtherQuery:function(t){return Object.keys(t).reduce(function(n,e){return"redirect"!==e&&(n[e]=t[e]),n},{})}}},b=_,y=(e("2017"),e("f8a6"),Object(d["a"])(b,s,a,!1,null,"2a917112",null));n["default"]=y.exports},d9fb:function(t,n,e){"use strict";var s=e("28dd"),a=e.n(s);a.a},f8a6:function(t,n,e){"use strict";var s=e("590b"),a=e.n(s);a.a}}]);