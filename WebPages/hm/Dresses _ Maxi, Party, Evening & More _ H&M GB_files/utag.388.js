//tealium universal tag - utag.388 ut4.0.201904041153, Copyright 2019 Tealium.com Inc. All Rights Reserved.
function __readRMCookie(e){for(var t=e+"=",a=document.cookie.split(";"),r=0;r<a.length;r++){for(var n=a[r];" "==n.charAt(0);)n=n.substring(1,n.length);if(0==n.indexOf(t))return n.substring(t.length,n.length)}return""}function __readRMCookiev2(e,t){for(var a=__readRMCookie(t=t||"rmStore");a!==decodeURIComponent(a);)a=decodeURIComponent(a);for(var r=a.split("|"),n=0;n<r.length;n++){var o=r[n].split(":")[0],i=r[n].split(":")[1];if(o===e)return i}return""}function __readParam(e,t,a,r){var n=t||"",o=a||"",i=r||{},s=__readRMCookiev2(e||""),d=i[n],m=(s=i.ignoreCookie||!1?0:s)||d||o;return m=("string"!=typeof m||"false"!==m.toLowerCase())&&m}function sRAN(){var e=DataLayer&&DataLayer.Sale&&DataLayer.Sale.Basket?DataLayer.Sale.Basket:{},t=e.affiliateConfig||{},a=__readParam("atm","tagType","pixel",t),r=__readParam("adr","discountType","order",t),n=__readParam("acs","includeStatus","false",t),o=__readParam("arto","removeOrderTax","false",t),i=__readParam("artp","removeTaxFromProducts","false",t),s=__readParam("artd","removeTaxFromDiscount","false",t),d=__readParam("atr","taxRate",0,t),m=(100+(d=Number(d)))/100,u=__readParam("ald","land",!1,{})||(t.land&&!0===t.land?__readRMCookie("ranLandDateTime"):t.land)||!1,l=__readParam("atrv","tr",!1,{})||(t.tr&&!0===t.tr?__readRMCookie("ranSiteID"):t.tr)||!1,c=!1,p=__readParam("amid","ranMID","",t)||e.ranMID;if(!p)return!1;if(!(void 0===t.allowCommission||"false"!==t.allowCommission))return!1;var y=encodeURIComponent(e.orderid||"OrderNumberNotAvailable"),f="",v="",_="",C="",N=e.currency||"";N=encodeURIComponent(N.toUpperCase());var h=e.taxAmount?Math.abs(Math.round(100*Number(e.taxAmount))):0,g=e.discountAmount?Math.abs(Math.round(100*Number(e.discountAmount))):0;s&&d&&(g=Math.round(g/m));var b="pixel"===a?"ep":"mop"===a?"eventnvppixel":"ep",R=e.customerStatus||"",D=document.location.protocol+"//track.linksynergy.com/"+b+"?",I="";null!=R&&""!=R&&(n&&"EXISTING"==R.toUpperCase()||n&&"RETURNING"==R.toUpperCase())&&(I="R_");for(var S=[],w=0,U=0;U<(e.lineitems?e.lineitems.length:0);U++){var x=!1,P=window.JSON?JSON.parse(JSON.stringify(e.lineitems[U])):e.lineitems[U],T=Number(P.unitPriceLessTax||P.unitPrice||0);i&&d&&!P.unitPriceLessTax&&(T/=m);for(var L=0;L<S.length;L++){S[L].SKU===P.SKU&&(x=!0,S[L].quantity=Number(S[L].quantity)+Number(P.quantity),S[L].totalValueLessTax=Number(S[L].totalValueLessTax)+Number(P.quantity)*T,S[L].totalValue=Number(S[L].totalValue)+Number(P.quantity)*Number(P.unitPrice))}x||(P.totalValue=Number(P.quantity)*Number(P.unitPrice),P.totalValueLessTax=Number(P.quantity)*T,S.push(P)),w+=Number(P.quantity)*T*100}var k={};for(U=0;U<S.length;U++){P=S[U];var O=encodeURIComponent(P.SKU),M=P.totalValueLessTax||P.totalValue,A=P.quantity,q=encodeURIComponent(P.productName)||"",E=100*Number(M);"item"===r.toLowerCase()&&g&&(E-=g*E/w);var B=P.optionalData;for(var V in B)B.hasOwnProperty(V)&&(k[V]=k[V]||"",k[V]+=encodeURIComponent(B[V])+"|");f+=I+O+"|",v+=A+"|",_+=Math.round(E)+"|",C+=I+q+"|"}f=f.slice(0,-1),v=v.slice(0,-1),_=_.slice(0,-1),C=C.slice(0,-1),g&&"order"===r.toLowerCase()?(f+="|"+I+"DISCOUNT",C+="|"+I+"DISCOUNT",v+="|0",_+="|-"+g):g&&"item"===r.toLowerCase()&&(c=!0),o&&h&&(f+="|"+I+"ORDERTAX",v+="|0",_+="|-"+h,C+="|"+I+"ORDERTAX"),D+="mid="+p+"&ord="+y+"&skulist="+f+"&qlist="+v+"&amtlist="+_+"&cur="+N+"&namelist="+C+"&img=1&",u&&(D+="land="+u+"&"),l&&(D+="tr="+l+"&"),c&&(D+="discount="+g+"&");B=e.optionalData||{};for(var V in e.discountCode&&(B.coupon=e.discountCode),e.customerStatus&&(B.custstatus=e.customerStatus),e.customerID&&(B.custid=e.customerID),g&&(B.disamt=g),B)B.hasOwnProperty(V)&&(D+=encodeURIComponent(V)+"="+encodeURIComponent(B[V])+"&");for(var V in k)k.hasOwnProperty(V)&&(D+=encodeURIComponent(V)+"list="+k[V].slice(0,-1),g&&"order"===r.toLowerCase()&&(D+="disamt"==V||"margin"==V?"|0":"|DISCOUNT"),h&&o&&(D+="disamt"==V||"margin"==V?"|0":"|ORDERTAX"),D+="&");"&"===D[D.length-1]&&(D=D.slice(0,-1)),2037<D.length&&(D=D.slice(0,2037),D+="&trunc=true");var j,G=document.createElement("img");G.setAttribute("src",D),G.setAttribute("height","1px"),G.setAttribute("width","1px"),(j=document.getElementsByTagName("script")[0]).parentNode.insertBefore(G,j)}function sDisplay(){var e=null,t=e,a=e,r=e,n=e,o=window.DataLayer&&window.DataLayer.Sale&&window.DataLayer.Sale.Basket?window.DataLayer.Sale.Basket:{},i=o.displayConfig||{},s=o.customerStatus||"",d=o.discountAmount?Math.abs(Number(o.discountAmount)):0,m=e,u="",l=__readParam("dmid","rdMID","",i);if(!l)return!1;var c=__readParam("dtm","tagType","js",i),p="if"===(c="js"===c||"if"===c||"img"===c?c:"js")?"iframe":"img"===c?c:"script",y="//"+__readParam("ddn","domain","tags.rd.linksynergy.com",i)+"/"+c+"/"+l,f=__readParam("dis","includeStatus","false",i),v=__readParam("dcomm","allowCommission","notset",i);"true"===v||!0===v||"1"===v||1===v?u="1":"false"!==v&&!1!==v&&"0"!==v&&0!==v||(u="0");var _="";if(null!=s&&""!=s&&(f&&"EXISTING"==s.toUpperCase()||f&&"RETURNING"==s.toUpperCase())&&(_="R_"),!o.orderid||!o.conversionType)return!1;r=0,a=encodeURIComponent(_+o.orderid),t="",n="conv",m=encodeURIComponent(o.currency||"");for(var C=0;C<(o.lineitems?o.lineitems.length:0);C++)r+=Number(o.lineitems[C].unitPriceLessTax)*Number(o.lineitems[C].quantity)||Number(o.lineitems[C].unitPrice)*Number(o.lineitems[C].quantity),t+=encodeURIComponent(o.lineitems[C].SKU)+",";r=Math.round(100*(r-d))/100,t=t.slice(0,-1),n&&(y=-1<y.indexOf("?")?y+"&pt="+n:y+"/?pt="+n),t&&(y=-1<y.indexOf("?")?y+"&prodID="+t:y+"/?prodID="+t),a&&(y=-1<y.indexOf("?")?y+"&orderNumber="+a:y+"/?orderNumber="+a),r&&(y=-1<y.indexOf("?")?y+"&price="+r:y+"/?price="+r),m&&(y=-1<y.indexOf("?")?y+"&cur="+m:y+"/?cur="+m),u&&(y=-1<y.indexOf("?")?y+"&tvalid="+u:y+"/?tvalid="+u);var N=document.createElement(p);N.src=y,"script"===p?N.type="text/javascript":"iframe"===p&&N.setAttribute("style","display: none;"),document.getElementsByTagName("body")[0].appendChild(N)}function sSearch(){var i=window.DataLayer&&window.DataLayer.Sale&&window.DataLayer.Sale.Basket?window.DataLayer.Sale.Basket:{},s=i.searchConfig||{},d=__readParam("smid","rsMID","",s);if(!d)return!1;var e=function(){var e=i.discountAmount?Math.abs(Number(i.discountAmount)):0,t=__readParam("sct","conversionType","conv",s),a=0,r="";if(!i.orderid)return!1;a=0,r=encodeURIComponent(i.orderid);for(var n=0;n<(i.lineitems?i.lineitems.length:0);n++)a+=Number(i.lineitems[n].unitPrice)*Number(i.lineitems[n].quantity);a=Math.round(100*(a-e))/100;window.DataLayer.Sale.Basket;var o=[];o[0]="id="+d,o[1]="type="+t,o[2]="val="+a,o[3]="orderId="+r,o[4]="promoCode="+encodeURIComponent(i.discountCode||""),o[5]="valueCurrency="+encodeURIComponent(i.currency||"USD"),o[6]="GCID=",o[7]="kw=",o[8]="product=",k_trackevent(o,"113")},t=-1<document.location.protocol.indexOf("s")?"https://":"http://";t+="113.xg4ken.com/media/getpx.php?cid="+d;var a=document.createElement("script");a.type="text/javascript",a.src=t,a.onload=e,a.onreadystatechange=function(){"complete"!=this.readyState&&"loaded"!=this.readyState||e()},document.getElementsByTagName("head")[0].appendChild(a)}
try{(function(id,loader){var u={};utag.o[loader].sender[id]=u;if(utag.ut===undefined){utag.ut={};}
if(utag.ut.loader===undefined){u.loader=function(o){var b,c,l,a=document;if(o.type==="iframe"){b=a.createElement("iframe");o.attrs=o.attrs||{"height":"1","width":"1","style":"display:none"};for(l in utag.loader.GV(o.attrs)){b.setAttribute(l,o.attrs[l]);}b.setAttribute("src",o.src);}else if(o.type=="img"){utag.DB("Attach img: "+o.src);b=new Image();b.src=o.src;return;}else{b=a.createElement("script");b.language="javascript";b.type="text/javascript";b.async=1;b.charset="utf-8";for(l in utag.loader.GV(o.attrs)){b[l]=o.attrs[l];}b.src=o.src;}if(o.id){b.id=o.id};if(typeof o.cb=="function"){if(b.addEventListener){b.addEventListener("load",function(){o.cb()},false);}else{b.onreadystatechange=function(){if(this.readyState=='complete'||this.readyState=='loaded'){this.onreadystatechange=null;o.cb()}};}}l=o.loc||"head";c=a.getElementsByTagName(l)[0];if(c){utag.DB("Attach to "+l+": "+o.src);if(l=="script"){c.parentNode.insertBefore(b,c);}else{c.appendChild(b)}}}}else{u.loader=utag.ut.loader;}
if(utag.ut.typeOf===undefined){u.typeOf=function(e){return({}).toString.call(e).match(/\s([a-zA-Z]+)/)[1].toLowerCase();};}else{u.typeOf=utag.ut.typeOf;}
u.ev={"view":1};u.initialized=false;u.map_func=function(arr,obj,item){var i=arr.shift();obj[i]=obj[i]||{};if(arr.length>0){u.map_func(arr,obj[i],item);}else{obj[i]=item;}};u.callBack=function(a,b,c){utag.DB("send:388:CALLBACK");u.initialized=true;if(u.data.order_id){var g={};g.orderid=u.data.order_id;g.currency=u.data.order_currency;g.customerStatus=u.data.customerStatus||"";g.conversionType=u.data.conversionType||"Sale";g.customerID=u.data.customer_id;g.discountCode=u.data.order_coupon_code;g.discountAmount=u.data.discountAmount||0;if(u.data.order_tax&&u.data.order_subtotal){g.taxAmount=(u.data.order_subtotal*(u.data.order_tax/100)).toFixed(2);}
if(u.data.product_id.length>0){g.lineitems=[];}
for(var i=0;i<u.data.product_id.length;i++){u.data.item={};u.data.item.quantity=u.data.product_quantity[i];if(u.data.product_unit_price[i]){u.data.item.unitPrice=u.data.product_unit_price[i];u.data.item.unitPriceLessTax=u.data.product_unit_price[i];}
u.data.item.SKU=u.data.product_id[i];u.data.item.productName=u.data.product_name[i];u.data.item.optionalData={};u.data.item.optionalData.cat=u.data.product_category[i];g.lineitems.push(u.data.item);}
g.affiliateConfig=u.data.affiliateConfig;if(!utag.ut.isEmptyObject(u.data.displayConfig)){g.displayConfig=u.data.displayConfig;}
if(!utag.ut.isEmptyObject(u.data.searchConfig)){g.searchConfig=u.data.searchConfig;}
window.rm_trans=g;if(!window.DataLayer){window.DataLayer={Sale:{Basket:rm_trans}}}else{DataLayer.Sale=DataLayer.Sale||{Basket:rm_trans};DataLayer.Sale.Basket=DataLayer.Sale.Basket||rm_trans}DataLayer.Sale.Basket.Ready=true;sRAN();sDisplay();sSearch();if(!DataLayer.events){DataLayer.events={};}
DataLayer.events.SPIVersion="3.2";}
utag.DB("send:388:CALLBACK:COMPLETE");};u.map={"rakuten_customer_status":"customerStatus","product_quantity":"product_quantity","product_price":"product_unit_price"};u.extend=[function(a,b){try{if(1){try{if(b["cp.rmStore"]&&b["cp.rmStore"].indexOf("amid:4")==0){b.rakuten_ranMID=b["cp.rmStore"].substr(5,5);}
if(b["cp.affiliateCookie_tealium"]){var rakutenCookieObject=JSON.parse(b["cp.affiliateCookie_tealium"]);if(typeof rakutenCookieObject!=='object'){rakutenCookieObject=JSON.parse(rakutenCookieObject);}
var date=new Date(rakutenCookieObject.cookieTime);if(isNaN(date.getTime())){date=new Date();}
var exp=new Date(date.getTime()+(30*24*60*60*1000));var pad=function(number){if(number<10){return'0'+number;}
return''+number;};var timestamp=date.getUTCFullYear()+pad(date.getUTCMonth()+1)+pad(date.getUTCDate())+'_'+pad(date.getUTCHours())+pad(date.getUTCMinutes());var rakutenNewCookie="amid:"+rakutenCookieObject.ranMID+"|atm:pixel|ald:"+timestamp+"|atrv:"+rakutenCookieObject.ranSiteID;document.cookie="rmStore="+rakutenNewCookie+";domain=.hm.com;path=/;expires="+exp;document.cookie="affiliateCookie_tealium=;domain=.hm.com;path=/;expires=Thu, 01 Jan 1970 00:00:00 UTC";}
b.rakuten_product_category=[];if(b._corder!=""&&b._corder!=null){if(b.product_article_id==""||b.product_article_id==null||b.product_article_id==undefined){b._corder=null;}else{if(b.rakuten_ranMID){b._corder=b.selected_market+b._corder;}
b.rakuten_customer_status="New";if(b["cp.utag_main__sn"]>0){b.rakuten_customer_status="Existing";}
b.rakuten_affiliateconfig={"ranMID":b.rakuten_ranMID,"discountType":"item","includeStatus":"false","removeTaxFromDiscount":"true","removeTaxFromProducts":"true","taxRate":0,"allowCommission":"true","tagType":"mop"};b.rakuten_product_category=b.product_category;}}
b.rakuten_site_section="1";for(var i=0;i<b.product_article_id.length;i++){if(b.product_size_code[i]==null){b.product_size_code[i]="";}
b._cprod[i]=b.product_article_id[i].replace('-','')+b.product_size_code[i];}}catch(e){b.exception_reason="9300. [RAKUTEN] Configuration | MSG: "+e.message;}}}catch(e){utag.DB(e)}}];u.send=function(a,b){if(u.ev[a]||u.ev.all!==undefined){var c,d,e,f;u.data={"qsp_delim":"&","kvp_delim":"=","base_url":"//intljs.rmtag.com/{##utag_trackingKey##}.ct.js","trackingKey":"114913","allowCommission":"true","lineitems":[],"item":{},"affiliateConfig":{},"displayConfig":{},"searchConfig":{},"product_id":[],"product_category":[],"product_name":[],"product_quantity":[],"product_unit_price":[],"product_discount":[]};for(c=0;c<u.extend.length;c++){try{d=u.extend[c](a,b);if(d==false)return}catch(e){}};c=[];for(d in utag.loader.GV(u.map)){if(b[d]!==undefined&&b[d]!==""){e=u.map[d].split(",");for(f=0;f<e.length;f++){u.map_func(e[f].split("."),u.data,b[d]);}}}
u.data.order_id=u.data.order_id||b._corder||"";u.data.order_subtotal=u.data.order_subtotal||b._csubtotal||"";u.data.order_tax=u.data.order_tax||b._ctax||"";u.data.order_currency=u.data.order_currency||b._ccurrency||"";u.data.order_coupon_code=u.data.order_coupon_code||b._cpromo||"";u.data.customer_id=u.data.customer_id||b._ccustid||"";if(b.rakuten_affiliateconfig){u.data.affiliateConfig=b.rakuten_affiliateconfig;}else{u.data.affiliateConfig=u.data.affiliateConfig;}
if(u.data.product_id.length===0&&b._cprod!==undefined){u.data.product_id=b._cprod.slice(0);}
if(u.data.product_name.length===0&&b._cprodname!==undefined){u.data.product_name=b._cprodname.slice(0);}
if(u.data.product_category.length===0&&b._ccat!==undefined){u.data.product_category=b.rakuten_product_category.slice(0);}
if(u.data.product_quantity.length===0&&b._cquan!==undefined){u.data.product_quantity=b._cquan.slice(0);}
if(u.data.product_unit_price.length===0&&b._cprice!==undefined){u.data.product_unit_price=b._cprice.slice(0);}
if(u.data.product_discount.length===0&&b._cpdisc!==undefined){u.data.product_discount=b._cpdisc.slice(0);}
if(b["cp.CONSENTMGR"]&&b["cp.CONSENTMGR"].indexOf("consent:true")>-1){window.tealium_consent=1;}
u.data.base_url=u.data.base_url.replace("{##utag_trackingKey##}",u.data.trackingKey);if(!u.initialized){u.loader({"type":"script","src":u.data.base_url,"cb":u.callBack,"loc":"script","id":"utag_388","attrs":{}});}
}};utag.o[loader].loader.LOAD(id);}("388","hm.goe"));}catch(error){utag.DB(error);}
