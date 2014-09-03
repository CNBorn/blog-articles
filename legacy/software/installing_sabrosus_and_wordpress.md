安装Sa.bros.us和Wordpress
######################
Date: 2006-10-27 19:16
Category: Uncategorized
Status: draft

在Ubuntu Server上面装了两个应用级Web服务，WordPress和sa.bros.us，记下几点要注意的
 WordPress就不介绍了吧，著名的blog程序，我接触得晚了些
 下载：`http://wordpress.org/download/`_
 安装说明：`http://codex.wordpress.org/Installing\_WordPress`_
 WordPress的安装确实很方便，有一点我觉得要注意一下：安装目录一定要是blog ，否则install.php不能执行
 我起初安装在http://ommine/wordpress，怎么也不能解析install.php，把目录改名成blog就可以了。
 Sa.bros.us是一个开源的书签程序，类似del.icio.us。
 一直想在本机上面装一个书签程序，所以装来玩玩
 下载：`http://sourceforge.net/project/showfiles.php?group\_id=143603`_
 安装说明：sa.bros.us由于开发者的母语不是英语，所以英语资料比较少。我在这里写个安装说明吧
 安装Sa.bros.us
 将文件解压缩到web的主目录下
 导入mysql数据库
 mysql> CREATE DATABASE bookmark;
 mysql> USE bookmark;
 mysql> source sabrosus.sql
 修改sabrosus/include/config.php 权限为可执行
 sabrosus/include/config.ini 权限为可写
 然后执行 sabrosus/instalar.php (注意说明文档里说的是install.php，但是很显然文件的名字没有改)
 输入数据库的相关数据、已经你想要的设置，就完工了。在我上面的例子里，DatabaseName 就是bookmark
 Technorati Tags: `Wordpress`_ `sabrosus`_ `install`_ `linux`_ `CNBorn`_

.. _`http://wordpress.org/download/`: http://wordpress.org/download/
.. _`http://codex.wordpress.org/Installing\_WordPress`: http://codex.wordpress.org/Installing_WordPress
.. _`http://sourceforge.net/project/showfiles.php?group\_id=143603`: http://sourceforge.net/project/showfiles.php?group_id=143603
.. _Wordpress: http://technorati.com/tag/Wordpress
.. _sabrosus: http://technorati.com/tag/sabrosus
.. _install: http://technorati.com/tag/install
.. _linux: http://technorati.com/tag/linux
.. _CNBorn: http://technorati.com/tag/CNBorn
