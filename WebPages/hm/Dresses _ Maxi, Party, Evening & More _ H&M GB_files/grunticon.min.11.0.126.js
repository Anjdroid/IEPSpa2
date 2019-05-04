/*! grunt-grunticon Stylesheet Loader - v2.1.2 | https://github.com/filamentgroup/grunticon | (c) 2015 Scott Jehl, Filament Group, Inc. | MIT license. */
(function(b){function a(h,m,j,k){function e(){for(var i,l=0;
f.length>l;
l++){f[l].href&&f[l].href.indexOf(h.replace(/\.\.\//g,""))>-1&&(i=!0)
}i?g.media=j||"all":setTimeout(e)
}var g=b.document.createElement("link"),d=m||b.document.getElementsByTagName("script")[0],f=b.document.styleSheets;
return g.rel="stylesheet",g.href=h,g.media="only x",g.onload=k||null,d.parentNode.insertBefore(g,d),e(),g
}var c=function(h,j){if(h&&2===h.length){var e=b.navigator,g=b.Image,d=!(!document.createElementNS||!document.createElementNS("http://www.w3.org/2000/svg","svg").createSVGRect||!document.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#Image","1.1")||b.opera&&-1===e.userAgent.indexOf("Chrome")||-1!==e.userAgent.indexOf("Series40")),f=new g;
f.onerror=function(){c.method="png",c.href=h[0],a(h[0])
},f.onload=function(){var k=1===f.width&&1===f.height,i=h[k&&d?0:1];
c.method=k&&d?"svg":"datapng",c.href=i,a(i,null,null,j)
},f.src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==",document.documentElement.className+=" grunticon"
}};
c.loadCSS=a,b.grunticon=c
})(this);
(function(h,m){var f=m.document,b="grunticon:",d=function(c){if(f.attachEvent?"complete"===f.readyState:"loading"!==f.readyState){c()
}else{var a=!1;
f.addEventListener("readystatechange",function(){a||(a=!0,c())
},!1)
}},k=function(a){return m.document.querySelector('link[href$="'+a+'"]')
},j=function(v){var z,q,p,x,w,s,y={};
if(z=v.sheet,!z){return y
}q=z.cssRules?z.cssRules:z.rules;
for(var r=0;
q.length>r;
r++){p=q[r].cssText,x=b+q[r].selectorText,w=p.split(");")[0].match(/US\-ASCII\,([^"']+)/),w&&w[1]&&(s=decodeURIComponent(w[1]),y[x]=s)
}return y
},g=function(r){var q,s,n;
s="data-grunticon-embed";
for(var u in r){if(n=u.slice(b.length),q=f.querySelectorAll(n+"["+s+"]"),q.length){for(var p=0;
q.length>p;
p++){q[p].innerHTML=r[u],q[p].style.backgroundImage="none",q[p].removeAttribute(s)
}}}return q
},l=function(a){"svg"===h.method&&d(function(){g(j(k(h.href))),"function"==typeof a&&a()
})
};
h.embedIcons=g,h.getCSS=k,h.getIcons=j,h.ready=d,h.svgLoadedCallback=l,h.embedSVG=l
})(grunticon,this);
grunticon(["/etc.clientlibs/settings/wcm/designs/hm/clientlibs/shared/icons/svg.min"+clientlibsVersion+".css","/etc.clientlibs/settings/wcm/designs/hm/clientlibs/shared/icons/png.min"+clientlibsVersion+".css"]);