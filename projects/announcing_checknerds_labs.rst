CheckNerds Labs 开源项目正式上线
########################
:date: 2009-08-11 23:24
:category: Projects

2008年7月19日，`CheckNerds`_ 写下了最初的代码。而在接下来的这一年里，CheckNerds
从一个还仅存在于我头脑概念中的网站，到有千余注册用户的小型站点，算是迈出了第一步。

而如何将这样一个带有强烈个人色彩的项目，成为自己期望中的"更好的工具"，是我在这么长的时间以来，始终在思考的一件事情。

在这期间，我进行了无数的尝试与改进。其中，包括那些被大家所熟知的如针对移动设备(`手机`_、`iPhone/iPod`_)的`版本`_。但同时有着更多不为人知的改进，他们大多数止步于萌芽阶段，而止步的原因或是由于实际的理念于CheckNerds
当前的发展并不完全相符，或者完全是由于Google App Engine
所造成的技术限制等。甚至还有若干已经动手实施，并最终止步于半途的项目。固然惋惜，但却也在无数的尝试和思考中，对于自己要做一个什么样的产品，前所未有地清晰、明确起来。

CheckNerds 正在进行的方向，仍如同我最初设想的那样简单，以至于用如下几点就可以概括：

-  下一步目标，技术结构上，不是做到最大，而是再尽力做"小"；
-  如何让更多的人在上面花费更"少"的时间；
-  这种工具没有最"好"，如何再度巩固和突出特色，并且做得更好，"一个更好的工具"

2009年6月在`Google 开发者日大会上的介绍`_进行完以后，根据当时自己总结的方向和计划，我立即开始着手于 CheckNerds
开放API 的工作上面。

第一步开放的 API 已经于 6 月 25 日正式上线。前期公开的可调用功能还比较简单，这些会逐步进行完善。欢迎持续关注
`http://www.checknerds.com/docs/api/function`_。

API 将是CheckNerds 作为 "一个更好的工具" 中非常重要的一环。在建设 API 的工作以外，如何更好的让开发者和用户使用API
，同样是非常重要的工作。于是 `CheckNerds Labs 项目`_作为我在这个方面的尝试，正式启动。

`CheckNerds Labs`_ 为 基于 CheckNerds API 构建的一些辅助工具，旨在帮助用户更好、更便捷地访问和使用
CheckNerds。这些工具的源代码完全开放，您可以从 Google Code
的开发站点下载。同时欢迎广大用户参与改进！关于如何申请应用程序API权限、或想把自己写的基于CheckNerds
API的小程序加入到项目中这样的相关问题，欢迎各位感兴趣的开发者直接和我联系，期待你们的反馈。

目前 Labs 中包含的工具有：

amboy.py 导出用户所有 CheckNerds 事项的 Python 命令行脚本，用户资料导出，让用户完全掌握自己的信息。

未来计划会包含的其它内容：

CheckNerds Python Binding Library

CheckNerds GUI - Based on wxPython
 CheckNerds 完整版 API 调用文档
 等等其它，可以实现的应用有太多，唯一的限制是大家的想象力
目前这个项目需要完善的文档工作还有很多，欢迎大家关注 Google
Code上面的项目主页，所需文档和使用方式我会随时进行更新。代码在近期会放出snapshot下载，同时也欢迎大家使用`mercurial`_直接从Google
Code 项目站点下载最新的开发版本。（命令 hg clone
https://checknerds-labs.googlecode.com/hg/ checknerds-labs ）
总的来说，这部分的开放为 CheckNerds
实现Web以外的其它目标提供了更多的方式和可能，用户从此可以不仅是使用者，也可以是参与者。作为项目发起者，心里都会淡淡地希望可以瞬间有不少开发者能够关注这些代码，显然这非常不容易；而自己目前的想法实际上只是更加单纯：不管未来是一个人还是十个人维护这些代码，这个项目的开始意味着自己认真进行的一个项目从此可以更及时和透明地展现给整个世界，还有什么比这个更重要的呢？

.. _CheckNerds: http://www.checknerds.com/
.. _手机: http://cnborn.net/blog/2008/12/checknerds-mobile.html
.. _iPhone/iPod: http://cnborn.net/blog/2009/04/checknerds-iphone-ipodtouch-version-announced.html
.. _版本: http://www.checknerds.com/m
.. _Google
开发者日大会上的介绍: http://cnborn.net/blog/2009/06/google-developer-day-2009-beijing65.html
.. _`http://www.checknerds.com/docs/api/function`: http://www.checknerds.com/docs/api/function
.. _CheckNerds Labs 项目: http://code.google.com/p/checknerds-labs/
.. _CheckNerds Labs: http://code.google.com/p/checknerds-labs/
.. _mercurial: http://www.selenic.com/mercurial/
