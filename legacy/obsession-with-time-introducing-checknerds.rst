对时间的痴迷
######
:date: 2008-10-23 20:16
:category: Uncategorized
:status: draft

`|image0|`_
 我

有若干个记满了事情的本子。在度过的一个又一个24小时里，我会把我完成的较为有意义的事情以及想法都记录在上面。看着它们，我可以自豪地说我在近三四年
 来所度过的每一天都是连续而有意义的。这样在我日后想要回顾某些东西的时候，我可以清晰地看到那个轨迹，看到我所珍惜的时间没有轻易地被浪费。

大学四年里，我用了很长的几段时间来坚持一些简单的事情。我在寻求简单的实践辅以毅力，最终可以达到怎么样的效果？于是，跑步、背单词、听写训练、甚至是

看电影、读书这样的项目，都曾出现在我"每日必做"的列表上，而每次将它们完成，在我心目中的意义，俨然就是对近24小时逝去时光的一种肯定，所以每一条

这样的记录出现在本子上都会让我感到十分踏实。我承认这是一种十分Nerd的想法，从我意识到时间的宝贵开始，我就始终抱着对这种概念类似有些极端的痴迷。
06年，当我的世界观被开源软件和Python洗礼了之后，我就开始尝试使用Python来构建基于我的这种观念、可帮助我进行记录的工具。而这最终的成果就是当年发布的`tarsusa`_。
 tarsusa的定位现在想来十分怪异：为了开始尝试我感兴趣的Web软件开发，我选用了不出名的Web开发框架和数据库

(Karrigell+buzhug)，搭建出了一款localhost的Web软件产品。而将这些笨拙的代码开源则是向从很多意义上感召了我的自由软件
 行动致敬。
 在我的笔记本上一直运行着的原始tarsusa
build记录了我太多的在那段时间里的印迹。每个"完美日"（tarsusa里对于完成所有任务的一天的称呼）对我而言，都是一个小小的里程碑。
 原始版本的功能少得可怜，但因为可以满足自己的需要就没有进行太多的改进。在发布的一年多以后，07年10月，我才把长久以来的一些更新打包成一个

build，作为新版本继续发布。尽管是开源软件，但这个软件略有些奇怪的localhost形式，以及融入了我个人很多特色的风格，让它不太可能变成一

个可在更大程度上被广为使用的软件。我只是希望在我自己使用它的同时，能有一些想要学习和使用Python的入门爱好者，能够从我那些并不漂亮的代码中看
 到一些可帮助他们快速入门的东西就好了。

但这个小软件还是做到了一些我之前没有想到的东西。我的一个好朋友告诉我，他从tarsusa中受到了一些启发，对他的开发和工作有些帮助；有用户就一些问题和我发信交流；Ubuntu论坛里的一位前辈题出了许多修改意见，并期待下一个版本......
每一个这样的信息回馈都让我十分惊喜。（仿佛又回到了16岁时开始那个MP3搜索软件时的自己）而又让我有些内疚的是，我没有能及时更新tarsusa这个软件。
 08年年中我购置了新的LCD Display，日常用的主力机器也因此由Joybook换成了庞大的台式机Omnine。那个tarsusa
build也就闲置了一段时间没有使用。当我有一天再看到它时，我意识到是时候该用什么东西来更新它了。
 继续为原来的包写新的Release?

我已经不想在原来不完美的架构上越走越远。全新的重建？我还没有过上线的、代码完全属于自己的Web项目，全新的tarsusa（肯定也不会再延续这个名
 字）相信是个好选择。平台？Python的选用毫无疑问；而基于零成本的考虑，App
 Engine在经过很多人的试水之后，无疑被认定是一个很好的选择。我对于App
 Engine的发现和了解很晚，不过带来的好处是在我开始研究时，已经有很多的文档可供学习。于是在七月中旬，项目正式开始。

进行开发的时间，是利用我每天下班之后的那几个小时和周末。进度时快时慢，GAE的限制也比想象中还要多。在10月份，终于完成了一个基本可以开始使用的版本。
 `CheckNerds`_，

继承了我在tarsusa里面就融入的一些观念。作为一个在线的日程、计划管理网站，目前阶段的功能，可看作是一个tarsusa的多人、可交互版本。不
 必对概念进行过多的的担心，您大可简单地把日常要做的一个个项目打上"√
 "。但如果您在某些事情上像我一样，有坚持完成它们并坚持记录下来的nerdness的话，恭喜您，您来对了地方！

这是我第一次接触MVC，Django，GAE，Ajax，成果还远不完善，但过程我却很享受。我真心地希望这个作品能像tarsusa一样，在服务我的
 同时也为别人做出些贡献。而日后这个项目的变化，我有着一些想法，而其中的一些需要时间去实现。我也很期待实现它们的过程和最终结果。
 而关于这个项目开源的情况，我会在以后陆续发布，希望您能够继续关注！
 CheckNerds: `http://checknerds.appspot.com`_
 tarsusa website: `http://tarsusa.yiblog.com/cmsms/`_
 tarsusa on Google Code: `http://code.google.com/p/tarsusa/`_
 关于tarsusa的相关文章请`点击这里`_查看。
 P.S. 能够在有一个生日来临前，Release一个阶段性成果，十分令人欣喜。
 P.S. Oct 19th 在甘家口KFC 用笔手写完这一整篇文章实在有些辛苦！

.. _|image1|: http://picasaweb.google.com/lh/photo/5Hn-RErBK9cNmEDn0-0rwQ
.. _tarsusa: http://tarsusa.yiblog.com/cmsms/
.. _CheckNerds: http://checknerds.appspot.com/
.. _`http://checknerds.appspot.com`: http://checknerds.appspot.com/
.. _`http://tarsusa.yiblog.com/cmsms/`: http://tarsusa.yiblog.com/cmsms/
.. _`http://code.google.com/p/tarsusa/`: http://code.google.com/p/tarsusa/
.. _点击这里: http://www.google.cn/custom?domains=http://blog.donews.com/cnborn/&sa=Search&sitesearch=http://blog.donews.com/cnborn/&ie=UTF-8&oe=UTF-8&hl=zh-CN&q=tarsusa

.. |image0| image:: http://lh6.ggpht.com/CNBorn/SP86A06XfoI/AAAAAAAAAbA/X9xoJMzNhsA/s400/checknerds.jpg
.. |image1| image:: http://lh6.ggpht.com/CNBorn/SP86A06XfoI/AAAAAAAAAbA/X9xoJMzNhsA/s400/checknerds.jpg
