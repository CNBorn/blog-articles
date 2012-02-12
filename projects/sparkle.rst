Sparkle
#######
:date: 2007-08-10 17:02
:category: Projects

终于基本实现了我一直以来十分需要的，一个可以帮助自己记忆单词的软件。
Sparkle
web端服务使用`Karrigell`_，数据库使用Karrigell内置的`buzhug`_数据库
`|screenshot of sparkle|`_
我需要这个工具的原因，是因为我一直以来是一个忠实的`《词汇大爆炸》`_用户（该软件已经停止开发），自从2004年以来已经累计使用它背了几百个小时的单词，从中获益菲浅。可以说《词汇大爆炸》是使用ubuntu之后，要使用Windows的唯一理由。
我曾经的计划是做一个《词汇大爆炸》的clone，发现自己水平可能比较难做到。在这种类别的开源软件里面，我还没有找到比较像《词汇大爆炸》这样的（惭愧，还没有用过黑客背单词）。后来觉得只要有一个可以基本帮助自己背不熟悉的单词的东西也就可以满足了。于是在开发`tarsusa`_的同时，这个东西其实已经在着手准备，只是自己一直都没有下定决心一口气做出来。
前

一阵想把台式机上面许久不用的Windows重新安装一下，没想到安装过程中CPU过热会导致频繁关机，并且由于安装程序重写了主引导区，我还需要费时恢
 复GRUB......

这促成了我和Windows说拜拜并且写完sparkle的原因。具体到架构如何实现、使用什么界面形式这些问题在我脑海中已经构想了许久，所以大约两个
 晚上就写了出来。
sparkle总体的结构：一个单词数据库记录平时遇到的不认识的单词（我已经积攒了一段时间了），然后像词汇大爆炸那

样，依据用户对单词的熟悉程度，随机抽取单词和解释，由用户进行选择形式的做答，用户较熟悉的单词会较少出现，不熟悉的单词会经常出现，以此达到学习的目
 的。
当然这个程序还远没有《词汇大爆炸》那种规模，没有应用艾宾浩斯记忆曲线原理，也没有针对用户行为的、更细致的词义混淆等等，还只是

一个简单的小程序。目前通过web界面来实现，但事实上并不局限于web界面，实际上任何连入网络能够执行Python程序的平台都有可能实现。比如可以
 执行`Xbox Media Center`_的破解版Xbox,甚至是Symbian S60
Smartphone。我希望能够有时间、有精力、有技术来实现以上那些功能。
去年的这个时候，也是使用同样的工具完成了自己需要的日程管理软件tarsusa，若问我用最好的语言Python完成这些简单的工具是什么感觉，那只有简单的一个字，爽。
参考阅读：
 `《tarsusa Release RC》`_

.. _Karrigell: http://karrigell.sourceforge.net/
.. _buzhug: http://buzhug.sourceforge.net/
.. _|image1|: http://tarsusa.yiblog.com/cmsms/uploads/images/sparkle/sparkle_by_CNBorn.png
.. _《词汇大爆炸》: http://www.netful.net/
.. _tarsusa: http://tarsusa.yiblog.com/cmsms/
.. _Xbox Media Center: http://www.xboxmediacenter.com/
.. _《tarsusa Release
RC》: http://blog.donews.com/CNBorn/archive/2006/08/30/1023608.aspx

.. |screenshot of
sparkle| image:: http://tarsusa.yiblog.com/cmsms/uploads/images/sparkle/thumb_sparkle_by_CNBorn.png
.. |image1| image:: http://tarsusa.yiblog.com/cmsms/uploads/images/sparkle/thumb_sparkle_by_CNBorn.png
