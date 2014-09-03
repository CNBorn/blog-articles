Title: OpenParty &quot;有狐&quot;
Date: 2009-03-14 10:42
Category: Event
Lang: cn
Tags: OpenParty
Slug: openparty-mozilla-event

本次的[OpenParty](http://www.beijing-open-party.org/)
"有狐"活动是以Mozilla的内容为核心，同时继续保持OpenParty传统的话题分享方式。这是我第二次参与OpenParty的活动，也是我第一次在这里进行话题分享。

来自雅虎中国的一位朋友在这次的OpenParty上展示了一个让我十分震撼的应用案例：将Firefox这款大家几乎每天都在使用的客户端软件，运用在

生产环境中的服务器上面变成集群，以实现大规模搜索引擎对于抓取后数据的分析。完全应用Firefox对于抓取到的Web界面进行解析（事实上可以说是利
 用了Gecko），同时在这个过程中，应用不少统计学、以及数学的相关概念，来实现对Web页面的认知工作。

难能可贵的是对于并不怎么深入了解搜索引擎相关技术的我来说，这个实现过程其实很好理解。但是在理解这个过程的同时，我不禁发出赞叹。很多我们平时没能注

意的问题，使用数学进行总结，实际上非常清晰直观：如，Web页面中划分区域，其中宽度大于高度，并且高出很多倍的区域，必然是导航条一类的部分，而不可

能是正文。然后利用一些统计学的原理去总结，就可以得到我们想要的数据。而且整套工具所使用的软件，如Firefox，以及特别为搜索引擎抓取任务所定制
 的Firefox Extensions, 在这里的应用堪称巧妙。这种将同一软件应用到不同领域的方式，可以很好地激励大家发散思维。
 技术方面我就不太多叙述了，难免班门弄斧。大家可到 [http://agentzh.org/](http://agentzh.org/)
，分享话题的这位朋友的Blog来查看整个详情。另外他的Blog完全是用Javascript生成的。
 ----

我带到OpenParty上面进行分享的话题，是对于Bugzilla，这个缺陷追踪系统的定制化上自己进行的一些研究。事实上，自己由于工作的需要，从
 去年12月开始接触Bugzilla这个开源项目，其间对于这个软件的部署、修改、本地化应用有了不少的体会。正好借这个机会进行一番总结。
 整个演示通过展示一个对于Bugzilla系统的，超过它原有适用的领域及应用形式的定制化修改。以此来向大家展示这个系统在定制化方面的潜力，

并希望籍此给更多的希望在更多领域应用开源软件的朋友以启迪，从而对于帮助大家将已有的开源软件产品通过一定的定制化，快速融入所需的应用环境中。事实上
 我要描述的，也是将一个在已知领域的软件，放入其它应用领域里的例子，只是没有Firefox集群那位朋友的技术那般高深。

我对总体的结果十分高兴和欣慰的，因为这个并不是特别技术的展示可能对于专业的技术人员来说并不是特别吸引人。但还是有不少朋友很捧场，完成了一次很好的
 交流。感谢那些的朋友，更希望我的这点分享能够对你们有所启发。总的来说不妄我费了很多时间来准备这个Slides了。

演示Slides请查看：[http://docs.google.com/Presentation?id=ajgc2xkd4rgc\_24fthmz2cn](http://docs.google.com/Presentation?id=ajgc2xkd4rgc_24fthmz2cn)
 ----
 下次或再下一次的OpenParty上面，我会针对Google App Engine开发、以及自己的[CheckNerds](http://checknerds.appspot.com)项
 目来进行一个专题。我会重点讲述Google App Engine
 比较高级方面的内容。在对于GAE简单的概述同时，我会讲一下框架的选择、如何打破GAE的限制，以及什么样的应用目前在GAE上面无法实现。同时对于
 CheckNerds这个网站的架构做出一些讲解，相信这其中架构这方面的知识也会帮助到很多对于Web2.0网站架构感兴趣的朋友
 今年，我预计会在信息分享上花费相当的时间。接下来的时间里，我还会陆续对于我较有经验的几个领域进行一些技术分享，如Google App
Engine等，欢迎大家关注。通常我的演讲会在[OpenParty](http://www.beijing-open-party.org/) 上进行，也欢迎大家到场来一起交流。