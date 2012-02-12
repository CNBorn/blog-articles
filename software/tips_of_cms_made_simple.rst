CMS Made Simple的几点技巧
####################
:date: 2007-06-02 11:14
:category: Software

`CMS Made Simple`_是一个简洁好用的CMS，`tarsusa的新网站`_就是由它驱动的。具体的介绍大家可以参阅以下两篇文章：
 `优秀的轻量级内容管理系统: CMS Made Simple`_
 `简单的cms:cmsmadesimple`_
 以下是我在使用 CMS Made Simple架设站点时，在`CMS Made
Simple论坛`_上看到的一些我认为很实用的小技巧，做一下简单介绍。每一条后面都有相关的链接，供大家参考。
 1、 CMS Made Simple Google Sitemaps Generator
 为CMS Made Simple站点提供Google 网站管理员工具需要的Sitemaps
 只需要把下载的gsitemaps.php复制到CMSMS安装的目录，然后在Google里提交指向gsitemaps.php的url即可
 链接：`CMSMS Forge - Google Sitemaps Generator`_
 2、根据显示内容的不同定制模板显示
 我们可以使用添加标志进行判断的方法，让模板可以根据不同的内容进行变化，以避免在模板库中出现一大堆只是有微小不同的模板
用途：比如网页的大版块和文章显示可以使用同一个模板，但在文章显示的页面上出现"收藏到"以及层次路径指示 （breadcrumbs）
 论坛原贴中举出的应用实例更多，欢迎参考
步骤：编辑需要模板有所变化的页面（这里的例子是显示具体文章的页面），在编辑页面的"选项"选项卡的"可变数据"（即metadata）里面，加入
{assign var='showbreadcrumbs' value='1'}
即定义一个名为showbreadcrumbs，值为1的变量
然后将"可缓存"前面的钩去掉
接着修改模板，加入相应的判断
{if isset($showbreadcrumbs)}
 {breadcrumbs}
<br />
{/if}
这样，所有显示文章的页面上，都有了breadcrumbs，而其它的页面不会受到影响。
这个技巧更多、更复杂的应用，请参考原帖
 原文链接：`Customizing your template based on the current page`_
3、一键保存到在线书签
国外的新闻网站常见的，文章底下有一排在线书签的小图标，点击即保存到相应的网站中
步骤：首先创建一个用户自定义标签，粘贴进相应代码（代码很长就不贴了，请参见原贴第一个代码框）
 然后修改需要显示这个的模板，加入这个用户自定义标签（例如如果你定义的是saveto\_tools，就写上{saveto\_tools}）
 修改样式表，将原贴第二个代码框的内容粘贴为一个新的样式表并且绑定到你需要使用的模板上
 将原贴中的那些图标下载下来并且复制到你的网站上（注意要和上面一步样式表中的路径一致，可以自己修改）
这样就可以了。（这个目前还都是外国流行的那些服务，如果针对中文网站使用的话，把中文的那些常用服务修改下加进去比较好）
原贴链接：`News Article Tools (digg, delicious, stumbleupon...) User Defined
Tag`_**
**4、提升站点速度之更改样式表
查看网站的源代码，找到类似
<link rel="stylesheet" type="text/css"
href="http://www.yourdomain.com/stylesheet.php?templateid=23" />
<link
 rel="stylesheet" type="text/css" media="print"

href="http://www.yourdomain.com/stylesheet.php?templateid=23&amp;mediatype=print"
 />
这样的行，然后把&amp;这个去掉，在浏览器中把这两个文件打开，并且另存为像yoursite-screen.css及yoursite-print.css这样的文件，上传到服务器
然后修改模板，把{stylesheet}字段修改为
<link rel="stylesheet" type="text/css"
href="/uploads/yoursite-screen.css" />
<link rel="stylesheet" type="text/css" media="print"
href="/uploads/yoursite-print.css" />
注意路径要一致，并且css文件中的图片路径也要一致（我改得很辛苦......）
这样，即把需要stylesheet.php调用的CSS替换成了静态文件，速度大大加快。一般来说，推荐给所有CSS设计已经定型，不需要改动了的网站。
原贴： `Speed up your site.. lose {stylesheet}`_
另外，目前版本的CMS Made
Simple还不支持多语言站点功能，虽然程序不支持，可是用户们还是实验出了很多的解决方案。比如出现了修改的多语言版 `CMS Made
Simple Multilingual`_
这篇帖子 `My trick for multilingual pages with regular CMS v1.0.6`_
提供了一个使用原版程序实现多语言网站的参考，我还没有实验（和上面的第2条技巧实现方法类似），有这个需要的朋友可以试试。
把论坛上的一些小东西简单翻译了一下，感觉CMS Made Simple的中文资料少得可怜（程序的中文化却相当好），贴上这些东西补充一下吧。
这些技巧都不复杂，也都经过我的实验，CMS Made Simple的玩家们可以试试。

.. _CMS Made Simple: http://www.cmsmadesimple.org/main/home.shtml
.. _tarsusa的新网站: http://tarsusa.yiblog.com/cmsms/
.. _`优秀的轻量级内容管理系统: CMS Made
Simple`: http://blog.daviesliu.net/article/entry20061223-171405
.. _`简单的cms:cmsmadesimple`: http://blog.devep.net/virushuo/2007/03/01/cms-made-simple-install.html
.. _CMS Made Simple论坛: http://forum.cmsmadesimple.org/index.php
.. _CMSMS Forge - Google Sitemaps
Generator: http://dev.cmsmadesimple.org/projects/gsgenerator/
.. _Customizing your template based on the current
page: http://forum.cmsmadesimple.org/index.php/topic,11689.0.html
.. _News Article Tools (digg, delicious, stumbleupon...) User Defined
Tag: http://forum.cmsmadesimple.org/index.php?topic=12250.0
.. _Speed up your site.. lose
{stylesheet}: http://forum.cmsmadesimple.org/index.php?topic=10630.0
.. _CMS Made Simple
Multilingual: http://dev.cmsmadesimple.org/projects/multilang/
.. _My trick for multilingual pages with regular CMS
v1.0.6: http://forum.cmsmadesimple.org/index.php?topic=11756.0
