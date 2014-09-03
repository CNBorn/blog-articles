OpenParty &quot;聚萤&quot;
###########################
:date: 2010-01-31 23:51
:category: Event
:status: draft

2010年开场的OP活动依然精彩，此次活动吸引了近百名朋友前来参加。此篇文章仍像以往一样，简要描述下在本次活动中，自己聆听的几个话题。

首先是ThoughtWorks咨询师钱钱带来的"敏捷需求分析"话题。此话题分量很足，在此简要呈现下我的零星记录，作为个人对整个话题思路(不完整)的简单梳理。
**敏捷软件需求**

软件需求遇到的最大问题是什么？基本上都是**沟通和交流**的相关问题

需求从哪里来：客户（市场）、用户

我们需要确定的是：**谁是用户？当前业务流程情况？业务目标是什么？**

项目需求确定中遇到的最大问题是什么？需求文档驱动的过程不堪重负

ThoughtWorks如何进行需求分析

项目启动：QuickStart

概要的需求分析，初步估算规模

不是不需要文档和需求分析：但是也不期望一次弄清楚所有需求。在项目启动阶段，先实行粗粒度的计划，暂时不考虑远期偏向细节的东西。

粒度最好可以控制到，单一发布中，每两周一个迭代。

这期间最重要的，是\**了解\**业务、\**分解\**业务。这在各个领域、各个公司、各种情况下都不同，没有规则可以遵循。

项目启动阶段（概要分析阶段）

产出：

1 愿景和动机、驱动力，业务价值

2 需求列表

3 可视化项目原型

同时评估项目风险、成本，提供可视的、便于评估的文档。

通过需求分析师、客户面对面的信息交流，把需求、目标具体化，最终创建大家一致、认可的目标和分析。可以通过一些具体的东西来实现，比如财务流程图，业务流程图，功能分解图。

在文档不堪重负的情况下，如何表述需求？使用 User Story (用户故事)卡片

（卡片范例）

来自： `http://www.agilemodeling.com/artifacts/userStory.htm`_

为什么用卡片：单一的需求文档只是信息的聚合，而分解为可以量化和检索的知识，更加便于我们评估和分析。

每个 User Story的基本定义为：一小块对客户有价值的功能。
这个原则是如何产生的呢，通过角色流程（ Role-Process）的方法，绘制出流程图， User Story是该图上基本的元素

Story的3C原则：

-  Card 需求存在
-  Conversation 一段对话和交流
-  Confirmation 用户需求的确定性

如何分辨 User Story的质量呢？好的User Story遵循INVEST原则

-  Independent 可以独立开发
-  Negotiable 可以协商
-  Valuable 有价值
-  Estimate 大小可评估
-  Sized appropriately 合适的粒度 （1~3天为最合适的粒度）
-  Testable 可测试性

需求可以分解为：产品、模块、特性、用户故事、开发任务五种不同的的类型，逐步细化。
举例：
产品：电子商务系统

模块：电子商务模块
特性：购物车、在线支付

用户故事：添加到购物车，查看购物车

开发任务：更改数目、计算总额

任务分解后，先排出优先级，对技术可行性作出验证。

UserStory的生命周期：使用Mingle管理，建立 StoryWall

可视化管理：

-  墙上贴卡片
-  直观
-  增强了管理透明度

总的来说，敏捷＝开发实践＋项目管理实践

简单谈两句我个人对于敏捷的非常粗浅的理解：

这其实更是一种管理技巧与方法，而不是具体的技术问题。如果仅从一个(懒惰的)程序员自身的角度出发，那么整套东西基本是很多看起来奇怪、有些还打破了日常工作习惯的行为准则的堆砌。但如果你有幸能够参与多个角色（如同时作为产品的销售、开发、决策人员其中的数职），来从一个更高的高度来审视并经历过一个或数个软件项目的时候，就会发现这些行为准则完全都是为了一个清晰的目标：为了按时、高质量地完成软件项目。同时竭力避免软件项目各个过程中各种由于人员、交流以及其它问题所造成的不利影响。

结尾的时候钱钱推荐了一本书： `User Stories Applied`_ ---- TW敏捷需求分析师必读，欢迎感兴趣的朋友参阅。

----

Mozilla在会场展示了火狐中文版本的一个功能，"火狐魔镜"。简单的说，就是可以把任何网站页面上单独的一部分取出作为Widget放在桌面的功能。整个演示很眩。

我个人认为整个话题最好的地方在于异常良好的互动性。整个话题是一次互动的交流、这个产品的走向、发展以及未来开源的情况，在场观众都得到了即时的了解。同时通过和在场观众的互动，Mozilla方面也更好的获得了开发需求的反馈，用户也可以窥见未来产品的方向。我认为这种形式非常值得借鉴，是参与开源社区产品的公司，与开源产品的用户一种非常好的交互模式。

----

接下来就是 `超群`_ 带来的MongoDB介绍。通过超群抛砖引玉的介绍，让听众对于MongoDB的特性有了比较好的了解。

具体的信息可以参考当时演讲的slides: `MongoDB in Action`_ 很适合入门，同时MongoDB 项目的
`Tutorial`_ 也值得推荐。

我再次简要描述一下大家普遍关注的几个方面：

性能Benchmark

可以参考这个页面，`http://www.mongodb.org/display/DOCS/Benchmarks`_

比较值得记录的如下：

-  不支持JOIN
-  不支持事务
-  支持其它大多数常用SQL功能

提供了三种Replication的方式

-  主从
-  pair形式
-  有限的主－主

便捷、自动Sharding (这点很Cool!)

GridFS 内建的文件系统

两个应用：

-  nginx模块，可以直接读取GridFS
-  fuse模块 让\*nix操作系统可直接挂载 GridFS

提问时间，我根据自

.. _|image1|: http://docs.google.com/File?id=ajgc2xkd4rgc_153gjg42fg4_b
.. _`http://www.agilemodeling.com/artifacts/userStory.htm`: http://www.agilemodeling.com/artifacts/userStory.htm
.. _User Stories Applied: http://www.douban.com/subject/1610317/
.. _超群: http://www.fuchaoqun.com/
.. _MongoDB in Action: http://www.fuchaoqun.com/2010/01/mongodb-in-action/
.. _Tutorial: http://www.mongodb.org/display/DOCS/Tutorial
.. _`http://www.mongodb.org/display/DOCS/Benchmarks`: http://www.mongodb.org/display/DOCS/Benchmarks

.. |image0| image:: http://docs.google.com/File?id=ajgc2xkd4rgc_153gjg42fg4_b
.. |image1| image:: http://docs.google.com/File?id=ajgc2xkd4rgc_153gjg42fg4_b
