OpenParty &quot;溪窗听雨&quot;
###############################
:date: 2009-09-01 00:05
:category: Event
:lang: zh

这次的 `OpenParty`_
上自己听到的话题都是期待已久的，所以对于记录这些话题有着精心的准备，随身携带的记录本基本上留住了绝大多数我想要了解的细节。以下的文章包含了我在敏捷项目咨询、X-Moto开源游戏以及wxPython编写的个人财务管理软件三个话题中的如实记录，个别部分是当时演讲话题的细节呈现，整体可能略微缺乏条理，还望大家海涵。如果对于本次OpenParty
"溪窗听雨"活动还不甚了解，欢迎您访问`本次活动的介绍页面`_。
首先听的第一个话题是ThoughtWorks带来的
一次敏捷的咨询经历。整个话题中牵扯到了一个软件项目开发和管理中的太多方面，同时现场还有不少热心的听众参与讨论，毕竟敏捷是一个十分热门的话题。下面我就根据自己记住的内容分要点罗列一下。

对于项目持续集成的改进：

实施多阶段的持续集成方案，从底层组件起逐步集成，这种方式适合于大型项目，上百人的团队。

对于项目测试的改进

自动化测试部分，在该咨询项目中，原本几乎没有什么正规的测试流程，TW的咨询师们首先加入功能测试，选用了Selenium作为解决方案。但是有一个问题是，进行功能测试的部分，应该由谁来撰写？是开发人员？还是测试人员？（在这个咨询案例中，TW认为应该该由开发人员撰写，此问题也引发了在场几位听众的讨论，最终没有一个压倒性的结果，应该说还是根据项目的需要而有所不同）

通常情况下，自动化的测试流程覆盖了软件测试中的大多数功能，那么测试人员的角色究竟是什么呢？TW的一位测试人员说，通常在测试中会把相关的一个行为作为一个可以被识别并评估的Story，逐一进行测试。测试人员所做的，应该说是从一个真正软件用户的角度，来使用并尝试发现问题。因为程序各种功能的测试，可以说只是最核心的功能实现，但是要注意软件最后打交道的是人，一些需要由人在使用中在识别和认知方面引起的偏差和错误，是必须经过实际使用的测试才能够保证相当高的质量。

程序员管理中暴露的问题：

程序员是否一直很忙？在这个测试项目中，TW咨询师发现，在开始在客户处工作之后，提交代码最多的居然是TW的人员！而通过查询版本库显示，发现这个100个人的团队中，经常贡献代码的开发人员仅为20个左右，而这些贡献的人的平均代码量仅为10几行/每周！对程序员团队的管理不当，有可能是整个流程存在的最大的隐患。

最终在这个项目中，应用了如下的解决方案：

-  实践、分阶段的持续集成
-  测试（Ant, Selenuim, Badboy)
-  代码规范检查 StateSVN

ThoughtWorks的工作方式，

-  结对编程，两个头脑并行工作有利于保证工作的高质量。在场很多同仁也纷纷表示，结对编程带来的好处是效率非常高，虽然在形式上看上去是降低了人员利用率，但实际上通过保证高质量所节约的成本是非常显著的。
-  迭代、日报(给项目经理以上的领导汇报使用)、ShowCase
-  站立会议：减少会议时间，绝对不拘泥于形式，注重解决问题。
-  沟通、沟通、再沟通

ThoughtWorks的敏捷原则：

-  不为敏捷而敏捷
-  只有领导支持是不够的
-  敏捷推进必然有组织结构的改变

敏捷的目标，不是实施敏捷。一个问题所需要的解决方案从来不是解决方法本身。在推动一个问题解决的过程中，我们脑海中首先要谨记的是，我们的目标究竟是什么？不为敏捷而敏捷，我们的真正目标是提高效率。而借由这些方法、工具、理念来推动我们工作的过程中，我们原有的一些观点，是要被替换掉的，比如计算程序员的生产力水平的标尺，就不应该再使用代码行数这样的标准了。TW
举了一个例子，在某个咨询项目的过程中，经过两个月的工作，若说代码行数的变动，实际上是负值，因为整个团队在致力于将原来复杂的八个模块重构和精简为四个，大大提高了代码的可维护性，但是这样的工作的成效，就不能简单地用代码行数来衡量的。有一个可以值得考虑的标准是价值点的评估，即完成的这些工作，可以为最终的、客户满意的交付提供多少作用。只要是在朝着面向客户的最终交付这个方向上进行的努力，均可以认为是积极地完成了工作。
可以进行些梳理的是第三条，敏捷作为一个涵盖企业管理的概念，在很多情况下应用起来都会对组织结构的改变提出要求。但是我们应该怎么去作？如何去推动？上来就大刀阔斧地推动是完全不切合实际的，这些改变究竟是不是必须的？我们需要有相应的数据来支持。如果你能够有相应的证据可以表明，现有的一些体制，确实制约了我们在提高效率，和生产力上的努力，那么组织结构上的变化也并不是不可以的。
ThoughtWorks的大牛提到了"响应式设计"这个系统设计理念对于他个人的一个启示，即当所有的需求和限制摆在你面前时，你又尝试去完全考虑他们，那么此题目必是无解的。敏捷问题也是这样，很多时候的很多项目，都存在非常多的问题，但是我们始终要明确目标、以及要做的是什么东西，抓住重点来出发解决。错误是允许的，不允许错误就没有成功，
-----

接下来 Vincent Du 介绍的 X-Moto游戏话题。`X-Moto`_ 这个游戏是 `Elasto Mania`_
类型的游戏（商业游戏的最新对应是在Xbox 360 Arcade Live上的 `Trials HD`_），玩法很有趣。
这是一个需要很多技巧的游戏，完全免费，开源。游戏画面的感觉，是很有趣的"皮影戏"感觉，尤其是按下空格键控制摩托转向的时候，在场大家都在感叹："哇，皮影耶"。游戏画面还有一个更加简洁的Ugly版，适用于低配置的机器。这个版本的画面，完全是用线条来表现的
:)

游戏很细致，我开始一直认为这就是个核心如NES游戏的那种游戏，没想到物理引擎的设计贯穿了整个游戏（虽然物理整个的感觉并不完全要展示显示世界的情况，如在游戏中为了达到很多特殊效果，引力偏小）。规则的设置也很细致，玩家的角色不能碰触任何物体，而摩托车则可以。游戏有着现代竞速和技巧类的游戏都具备的元素，录像功能，Ghost鬼影功能，更有一个成熟的网上社区，玩家可以交流游戏技巧，比拼游戏技术（世界排名），单账户的多点信息同步、更可以交流自制地图。

游戏的地图编辑器技术十分有趣，使用了`InkScape`_ 这款自由的矢量绘图软件，游戏的编辑器功能被设计

.. _OpenParty: http://www.beijing-open-party.org/
.. _本次活动的介绍页面: http://www.beijing-open-party.org/index.php/2009/08/beijing-open-party-2009-08-event-preview.html
.. _X-Moto: http://xmoto.tuxfamily.org/
.. _Elasto Mania: http://en.wikipedia.org/wiki/Elasto_Mania
.. _Trials HD: http://www.gametrailers.com/video/review-trials-hd/54055
.. _InkScape: http://www.inkscape.org/
