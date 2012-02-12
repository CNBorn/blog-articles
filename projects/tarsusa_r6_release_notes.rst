tarsusa r6 发布说明
###############
:date: 2007-12-19 13:06
:category: Projects
:status: draft

tarsusa是一个非常简单的时间管理程序。使用它，您可以方便地管理所有您要完成的事情。无论是将杂乱的事项分门别类地整理，还是提醒您优先处理即将
 到期的任务，tarsusa都游刃有余。tarsusa可以提示您每天都必须完成的工作，并且记录每日您完成这些工作的情况。
这个程序是使用Python开发的localhost端Web应用程序。Web框架选择了Karrigell，一个纯Python的Web
Framework，使用的数据库系统是Karrigell内部自带的buzhug数据库。
发布札记：

在我笔记本中运行的tarsusa的记录里，r6版本来是定于2006年12月发布的。原本设想中的版本比现在发布的这个有更复杂的功能，但以"够用就好
 "这种准则的指导下，tarsusa的开发始终就处于极小的改进这种规模。这部分代码在我的硬盘上，基本上用电脑的日子都会使用，觉得缺少那个
 Feature实在是很麻烦的时候就加上。就这样过了一年，添加的代码不多，功能更像样些，经过我长时间试用的这些代码就摆在您面前。
关于更多更详尽的信息，您可以查阅 `http://blog.donews.com/CNBorn`_ 中 `关于tarsusa的文章`_ 以及
`tarsusa网站`_ 以及 `tarsusa的Google Code页面`_
下载：

-  `tarsusa\_r6.tar.bz2`_

 截图：

-  `tarsusa截图展示`_

 如何安装与试用：

-  参阅 `tarsusa - HowTo`_ 以及软件自带的帮助页面

r6 功能更新：

-  首页显示昨天完成每日任务的数量
-  首页不再显示所有未完成的任务，而显示所有未完成的任务分类，点击相应分类查看相应的任务 - 避免首页显示过长
-  在任务的详细页面中可以完成该项任务了
-  在任务的详细页面中可以看到于此任务相关的其它任务的信息
-  显示每个类别项目的数量在整个数据库中的百分比

已知问题：

-  添加项目时尽量不要加入半角引号，会导致js脚本无法正常处理删除提示信息而无法删除项目

以往的发布：
 tarsusa r5 - `第一次发布`_

.. _`http://blog.donews.com/CNBorn`: http://blog.donews.com/CNBorn
.. _关于tarsusa的文章: http://www.google.com/search?hl=zh-CN&q=tarsusa+site:blog.donews.com/CNBorn&btnG=Google+搜索&lr=
.. _tarsusa网站: http://tarsusa.yiblog.com/cmsms/
.. _tarsusa的Google Code页面: http://tarsusa.googlecode.com/
.. _tarsusa\_r6.tar.bz2: http://tarsusa.googlecode.com/files/tarsusa_r6.tar.bz2
.. _tarsusa截图展示: http://tarsusa.yiblog.com/cmsms/screenshots.htm
.. _tarsusa - HowTo: http://tarsusa.yiblog.com/cmsms/howto.htm
.. _第一次发布: http://blog.donews.com/cnborn/archive/2006/08/30/1023608.aspx
