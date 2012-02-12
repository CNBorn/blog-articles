shootGFW: 一个使用PyGame开发的小游戏
##########################
:date: 2009-07-11 12:22
:category: Projects
:status: draft

|image0|
shootGFW: 一个使用PyGame开发的小游戏。源码已经依据GPL协议公开，Google Code 项目主页:
`http://code.google.com/p/shootgfw/`_

这个游戏的灵感来源于HelloTee的breakGFWTee(`图片`_)， 自从一看到这个图案就想要实现这个好玩的创意。

起先打算自己使用PyGame从底层开始来写，后来决定采用更加快捷的方法。上网搜寻了几个类似的游戏源码，直接在上面实现这个创意。

原版的创意是打砖块，后来觉得用Space Invader（俗称小蜜蜂）的游戏方式可能会更加过瘾。

本游戏的源码改自

    Python Space Invader
    2004/08/16
    Jim E. Brooks
    `http://www.jimbrooks.org/python/pyspaceinvaders/`_

这个源码采用GPL授权，如果对原版有兴趣请到上述网站下载。

写shootGFW的过程中，发现PyGame是一个可以快速实现心中构想的游戏开发框架。整个程序开始修改到现在公开的版本大致用了4个多小时，大约是两个晚上下班回家后的时间完成的。当然我做的修改只是非常小的一部分，可即使是原版部分原作者也谈到是在非常短的时间里完成的。在工作之余可以快速完成一个轻松的小东西，很惬意。

**具体的操作方法是：**

Z，X，左右箭头控制移动

左右Ctrl键开火

Space: 特技1

C: 特技2

**安装方法：**

**Ubuntu 及其他 \*nix 系统**

**首先需要安装 PyGame (Python在大多数系统上已默认安装，就不再做特殊说明)
开启终端执行 sudo apt-get install python-pygame
到 `http://code.google.com/p/shootgfw/downloads/list`_ 下载程序（或者通过mercurial
从 Google Code 里面 clone 最新的代码)
使用 python 执行 pyspaceinvaders.py 这个脚本 : python pyspaceinvaders.py
即可开始游戏！**

**Windows**

首先需要到python.org 上面下载python 的Windows 安装包 (Windows 下推荐安装 Python 2.5,
`安装包链接`_)
然后到pygame.org ，下载对应Python相应版本的PyGame安装包 （Python 2.5安装包`链接`_)
到 `http://code.google.com/p/shootgfw/downloads/list`_ 下载程序（或者通过mercurial
从 Google Code 里面 clone 最新的代码)
使用 python 执行 pyspaceinvaders.py 这个脚本 : 即打开解压好的程序文件夹，双击
pyspaceinvaders.py 即可开始游戏！（如不能执行可能需要重启电脑）

本来考虑为了方便Windows的用户也可以方便地爽到这款游戏，我想要通过py2exe编译一个Windows版本。谁知屡次尝试均告失败。目前只好麻烦一些了

此游戏源码遵照GPL协议开源。对此程序有兴趣，希望自己亲自做些修改的朋友，请到Google Code
的项目上，参与这个项目（此项目使用Mercurial版本管理系统）

不过想对这个游戏的提一些指导意见，希望各位未来的贡献者们能够认同:

-  此游戏主旨在于娱乐以及PyGame学习交流，请不要在游戏中夹杂各种与政治、时事等相关观点
-  游戏中不出现任何中文文字
-  尊重各位贡献者的署名权

最后祝大家玩得开心，Have Fun!

.. _`http://code.google.com/p/shootgfw/`: http://code.google.com/p/shootgfw/
.. _图片: http://hellotee.com/wp-content/uploads/2009/07/21.jpg
.. _`http://www.jimbrooks.org/python/pyspaceinvaders/`: http://www.jimbrooks.org/python/pyspaceinvaders/
.. _`http://code.google.com/p/shootgfw/downloads/list`: http://code.google.com/p/shootgfw/downloads/list
.. _安装包链接: http://www.python.org/ftp/python/2.5.4/python-2.5.4.msi
.. _链接: http://pygame.org/ftp/pygame-1.8.1release.win32-py2.5.msi

.. |image0| image:: http://cnborn.net/blog/images/shootGFW_blog.png
