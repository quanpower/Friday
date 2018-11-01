(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[16],{"5WY0":function(e,t,a){e.exports={main:"antd-pro-pages-user-register-main",getCaptcha:"antd-pro-pages-user-register-getCaptcha",submit:"antd-pro-pages-user-register-submit",login:"antd-pro-pages-user-register-login",error:"antd-pro-pages-user-register-error",success:"antd-pro-pages-user-register-success",warning:"antd-pro-pages-user-register-warning","progress-pass":"antd-pro-pages-user-register-progress-pass",progress:"antd-pro-pages-user-register-progress"}},cq3J:function(e,t,a){"use strict";var r=a("TqRt"),s=a("284h");Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0,a("14J3");var l=r(a("BMrR"));a("+L6B");var i=r(a("2/Rp"));a("jCWc");var n=r(a("kPKH"));a("Q9mQ");var o=r(a("diRs"));a("MXD1");var d=r(a("CFYs")),u=r(a("MVZn")),f=r(a("lwsE")),c=r(a("W8MJ")),m=r(a("a1gu")),p=r(a("Nsbk")),g=r(a("7W2i"));a("5NDa");var h=r(a("5rEg"));a("OaEy");var v=r(a("2fM7"));a("y8nQ");var E,w,M,b=r(a("Vl3Y")),y=s(a("q1tI")),k=a("MuoO"),F=a("LLXN"),P=r(a("mOP9")),C=r(a("usdK")),S=r(a("5WY0")),N=b.default.Item,q=v.default.Option,x=h.default.Group,D={ok:y.default.createElement("div",{className:S.default.success},y.default.createElement(F.FormattedMessage,{id:"validation.password.strength.strong"})),pass:y.default.createElement("div",{className:S.default.warning},y.default.createElement(F.FormattedMessage,{id:"validation.password.strength.medium"})),poor:y.default.createElement("div",{className:S.default.error},y.default.createElement(F.FormattedMessage,{id:"validation.password.strength.short"}))},z={ok:"success",pass:"normal",poor:"exception"},W=(E=(0,k.connect)(function(e){var t=e.register,a=e.loading;return{register:t,submitting:a.effects["register/submit"]}}),w=b.default.create(),E(M=w(M=function(e){function t(){var e,a;(0,f.default)(this,t);for(var r=arguments.length,s=new Array(r),l=0;l<r;l++)s[l]=arguments[l];return a=(0,m.default)(this,(e=(0,p.default)(t)).call.apply(e,[this].concat(s))),a.state={count:0,confirmDirty:!1,visible:!1,help:"",prefix:"86"},a.onGetCaptcha=function(){var e=59;a.setState({count:e}),a.interval=setInterval(function(){e-=1,a.setState({count:e}),0===e&&clearInterval(a.interval)},1e3)},a.getPasswordStatus=function(){var e=a.props.form,t=e.getFieldValue("password");return t&&t.length>9?"ok":t&&t.length>5?"pass":"poor"},a.handleSubmit=function(e){e.preventDefault();var t=a.props,r=t.form,s=t.dispatch;r.validateFields({force:!0},function(e,t){if(!e){var r=a.state.prefix;s({type:"register/submit",payload:(0,u.default)({},t,{prefix:r})})}})},a.handleConfirmBlur=function(e){var t=e.target.value,r=a.state.confirmDirty;a.setState({confirmDirty:r||!!t})},a.checkConfirm=function(e,t,r){var s=a.props.form;t&&t!==s.getFieldValue("password")?r((0,F.formatMessage)({id:"validation.password.twice"})):r()},a.checkPassword=function(e,t,r){var s=a.state,l=s.visible,i=s.confirmDirty;if(t)if(a.setState({help:""}),l||a.setState({visible:!!t}),t.length<6)r("error");else{var n=a.props.form;t&&i&&n.validateFields(["confirm"],{force:!0}),r()}else a.setState({help:(0,F.formatMessage)({id:"validation.password.required"}),visible:!!t}),r("error")},a.changePrefix=function(e){a.setState({prefix:e})},a.renderPasswordProgress=function(){var e=a.props.form,t=e.getFieldValue("password"),r=a.getPasswordStatus();return t&&t.length?y.default.createElement("div",{className:S.default["progress-".concat(r)]},y.default.createElement(d.default,{status:z[r],className:S.default.progress,strokeWidth:6,percent:10*t.length>100?100:10*t.length,showInfo:!1})):null},a}return(0,g.default)(t,e),(0,c.default)(t,[{key:"componentDidUpdate",value:function(){var e=this.props,t=e.form,a=e.register,r=t.getFieldValue("mail");"ok"===a.status&&C.default.push({pathname:"/user/register-result",state:{account:r}})}},{key:"componentWillUnmount",value:function(){clearInterval(this.interval)}},{key:"render",value:function(){var e=this.props,t=e.form,a=e.submitting,r=t.getFieldDecorator,s=this.state,d=s.count,u=s.prefix,f=s.help,c=s.visible;return y.default.createElement("div",{className:S.default.main},y.default.createElement("h3",null,y.default.createElement(F.FormattedMessage,{id:"app.register.register"})),y.default.createElement(b.default,{onSubmit:this.handleSubmit},y.default.createElement(N,null,r("mail",{rules:[{required:!0,message:(0,F.formatMessage)({id:"validation.email.required"})},{type:"email",message:(0,F.formatMessage)({id:"validation.email.wrong-format"})}]})(y.default.createElement(h.default,{size:"large",placeholder:(0,F.formatMessage)({id:"form.email.placeholder"})}))),y.default.createElement(N,{help:f},y.default.createElement(o.default,{getPopupContainer:function(e){return e.parentNode},content:y.default.createElement("div",{style:{padding:"4px 0"}},D[this.getPasswordStatus()],this.renderPasswordProgress(),y.default.createElement("div",{style:{marginTop:10}},y.default.createElement(F.FormattedMessage,{id:"validation.password.strength.msg"}))),overlayStyle:{width:240},placement:"right",visible:c},r("password",{rules:[{validator:this.checkPassword}]})(y.default.createElement(h.default,{size:"large",type:"password",placeholder:(0,F.formatMessage)({id:"form.password.placeholder"})})))),y.default.createElement(N,null,r("confirm",{rules:[{required:!0,message:(0,F.formatMessage)({id:"validation.confirm-password.required"})},{validator:this.checkConfirm}]})(y.default.createElement(h.default,{size:"large",type:"password",placeholder:(0,F.formatMessage)({id:"form.confirm-password.placeholder"})}))),y.default.createElement(N,null,y.default.createElement(x,{compact:!0},y.default.createElement(v.default,{size:"large",value:u,onChange:this.changePrefix,style:{width:"20%"}},y.default.createElement(q,{value:"86"},"+86"),y.default.createElement(q,{value:"87"},"+87")),r("mobile",{rules:[{required:!0,message:(0,F.formatMessage)({id:"validation.phone-number.required"})},{pattern:/^\d{11}$/,message:(0,F.formatMessage)({id:"validation.phone-number.wrong-format"})}]})(y.default.createElement(h.default,{size:"large",style:{width:"80%"},placeholder:(0,F.formatMessage)({id:"form.phone-number.placeholder"})})))),y.default.createElement(N,null,y.default.createElement(l.default,{gutter:8},y.default.createElement(n.default,{span:16},r("captcha",{rules:[{required:!0,message:(0,F.formatMessage)({id:"validation.verification-code.required"})}]})(y.default.createElement(h.default,{size:"large",placeholder:(0,F.formatMessage)({id:"form.verification-code.placeholder"})}))),y.default.createElement(n.default,{span:8},y.default.createElement(i.default,{size:"large",disabled:d,className:S.default.getCaptcha,onClick:this.onGetCaptcha},d?"".concat(d," s"):(0,F.formatMessage)({id:"app.register.get-verification-code"}))))),y.default.createElement(N,null,y.default.createElement(i.default,{size:"large",loading:a,className:S.default.submit,type:"primary",htmlType:"submit"},y.default.createElement(F.FormattedMessage,{id:"app.register.register"})),y.default.createElement(P.default,{className:S.default.login,to:"/User/Login"},y.default.createElement(F.FormattedMessage,{id:"app.register.sing-in"})))))}}]),t}(y.Component))||M)||M),I=W;t.default=I}}]);