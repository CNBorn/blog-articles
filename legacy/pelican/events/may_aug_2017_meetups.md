Title: 2017年5-8月参加的Meetup记录
Date: 2017-09-10 18:45
Category: Event
Lang: zh
Slug: may-aug-2017-meetups

> 每次参加完Meetup之后我都会记录下当天对这个活动的印象以及了解到的新知识。其诉求是对自己记忆能力的练习以及一种“记录下来的知识就会长久记住”的自我安慰。时间久了之后觉得记录下来的内容没有被分享出来也不算物尽其用。所以开始把参加活动/记录内容/发布出来作为一个正向循环来督促/激励自己。

> 需要说明的是记录下的内容中，技术相关的内容可能是我不甚了解，只是在现场用最大限度的努力消化和记录的内容。在对相关领域了解的人看来可能漏洞濒多甚至错误百出。所以欢迎大家用辩证的方式来阅读，并请在评论中纠正我的错误。感谢。



##### TeamLeadTO - June 13, 2017

全场只有一个话题，讲的是Professtional Service导向的公司（如果这个描述让你感到陌生，那么“外包”这个词你或许熟悉）里面Team Lead的工作内容和方向和产品导向的公司/团队里面的有什么不同。

外包公司同时进行的项目很多（需要大量沟通和细致管理），和团队的关系可能不如长期的产品团队来得密切。另一个经验之谈是人力资源不能全都放在客户项目上（最多75%），要预留一些做替补队员以及研究和学习（因为不知道下一个项目会要求用什么技术，所以研究新技术不只是为了人员技能提升，也是业务必须）。

推崇优秀的概念，并要顶住压力维持自己和公司文化认为正确的实践，比如结对编程，代码Review等（有些客户会有奇怪的对于工作流程的特别要求，比如不允许结对编程。一时的妥协反而会影响公司长期的技术文化发展）

对于招聘和培训，主要的观点是要看重潜力而竭力避免短视的招聘策略（招一个“马上就能用的人”）。有潜力和激情的人才最重要，是公司和团队持续发展的关键。建议部门组成中合同工和全职员工都要有。招聘的时候要考虑其“咨询”能力（我的理解是会主动沟通、具有同理心，能够从客户的角度解决问题）。招聘时兼顾专才和全才（specialist and generalist）。

一个案例：两个合同工同时进驻项目，工作过程中发现处不来，最后从外部调资源协助完成了项目。教训是不要放尚未磨合的新人进同一个的项目，以及面试过程中其实对于候选人有一些疑问，当时应该相信自己的guts不招进来的。

提到团队的组织形式通常分为两种，在做Mentor的时候有一些策略上的不同：依照职能细分团队（比如区分Web和移动，移动再细分平台）和针对项目/客户组建大团队（尽量不细分职能）。一个更大的资源池和团队可以进最大程度避免knowledge silo的发生，同时协调起来也更灵活，有利于资源的合理调动。（缺点可能是到了一定规模就无法快速扩展了）。针对第一种团队，Mentor关注的问题都更具体，而对第二种团队来说，Mentor需要关注宏观决策并做好跨工种之间的反馈。TL自己要避免过于involve项目（的细节工作）中，需要经常和团队Check-in并持续做一对一。

客户提出过的各种“需求”（馊主意）：不要写单元测试；不许用敏捷流程；周末赶工周一上线；原型产品被当作稳定的产品来使用；等等。

如何和客户打交道：不能什么都同意客户的，与客户在一开始就要沟通明确，保障开发团队的想法和利益。现场放了一个视频，是用夸张的手法讲怎么和客户谈项目初始需求（场面一团混乱）。这个视频被用在面试中，希望候选人可以识别这个场景下主要的问题出现在哪里。答案其实很简单：没有人在关注客户奇怪问题背后的目的是什么，而是陷入实现等细节的纠纷中。

提问环节：

- Q：招聘时的否决应聘者的red flag是什么？

- A：是否有自己的主见和对工作的激情，处理冲突的方式，态度是否倾向于humble

- Q：如何有效管理合作方而非本公司的人员？

- A：除了1对1以外没别的办法。

除此之外和现场的另一位朋友交流了下TL的职能，他给出的答案条理清晰：运用经验辅导初级人员，教会他们如何思考及如何入手问题。另外就是需要沟通技巧，明白高层的目标是什么，并可以传达到执行层面。以及做好人员的一对一沟通。



##### Toronto JavaScript Tech Talks - June 26, 2017

话题：Intro to Virtual DOM Components By Jason Miller, the author of Preact.

本以为是来讲使用Preact的知识，结果话题单刀直入地讲React基本概念的实现。本质上把Preact如何实现（的轮廓）细致地讲了一遍。

他提到他着迷于软件设计中的限制，明确限制的设计才会出色。在设计Preact的时候优先考虑的是体积和速度，同时尽最大可能精简不必要的部分。

JSX

- Compile XML like syntax to javascript function call
- 本质上和 [Hyperscript](https://github.com/hyperhype/hyperscript) 做的事情是一样的。如果要描述JSX如何工作的话，那么本质上回到了h()这个方法调用。

Virtual Dom

- Objects represent a DOM tree

The essential of this framework: Write JSX, compiles to h() function call then create virtual DOM objects. We need to have a renderer that can render to DOM objects.

DOM慢其实是一个主观观点，DOM提供的诸多便利功能以及其重要性("everything talks to DOM")不应该被忽视。在直接操作DOM的时候，有一些技巧可以避免复杂低效的DOM行为。（本质上是更细致地了解DOM的工作原理和数据/对象结构）。我的理解是这里也是Preact在做diff比较时针对DOM的优化技巧

- Textnode: Don't recreate text object, change the text instead
- Avoid getters
- Avoid live node-lists

Always profiling - 提到了两个工具

- [IRHydra](https://github.com/mraleph/irhydra)

  Chrome built in tool to tell you whether your code is going to be run in optimized mode. Needs chrome to be built with flags

- [ESBench.com](ESbench.com)

  If you tell JS engine more about your application, it will optimize it better.



##### React Native Meetup - July 18, 2017

第一个话题讲的是React Native Storybook。这个话题讲了一下在WealthSimple移动应用中RN的逐步替换，大体是这篇文章的内容<http://code.wealthsimple.com/integrating-react-native-into-existing-native-apps/>。

随后根据经验讲述了在使用RN中的一些优势（漏记了一个）：

- 使用storybook之后设计师也可以测试component并给予反馈了（因为边际状态也很好测试）

- Jest can take snapshots for component （这个自动生成UI测试还是蛮厉害的）

- 有些Component单独拿出来没有上下文可能很难理解及调整，通过decorator稍微增加一些上下文有助于解决此问题。

在使用中需要注意的两点：

- Move all stories together in a single directory
- Mock redux layer

唯一的缺点：RN Storybook needs a simulator

第二个话题来自一位Rango.io的工程师讲React Native的Navigation库选择。

他做的第一个项目：在一个拥有长列表的应用中，针对同样的数据集有不同的view使得情况非常复杂，最终使用了定制的navigation方案。后来再做其它项目的时候首选开源库但发现选择过多，排除了不靠谱的选项后最后定位到如下四个各有利弊的实现：

- react-native-nagivation

  社区活跃，原生方案，每个scene都是独自的rootview且支持Redux；缺点是还在重构中，难以追踪stack以及Scene需被定义为class component.

- react-navigation

  设置方便，支持Deep Linking， 有Redux和Web的集成；非原生方案，在高负荷下JS引擎和UI Thread的通信不能保证动画的流畅；Deep-linking between stack navigations with redux can be tricky

- react-router

  优点没记下来，缺点是不支持动画，非原生方案，设置麻烦

- native-navigation

  完全原生方案，每个scene都是独自的rootview，与react-native类似的api；缺点是还在beta中，且文档尚未完善。

最终推荐: react-native-navigation

原则是尽量使用原生方案。另外一个因素是最好其navigation的抽象独立于实现以外（怎么也记不起这句的上下文了，现在回溯起来不太理解）。

最后一个话题讲Airbnb出品的Sketch插件。简单描述为 React Component 可以被导入导出，从此之后也是一种可以同时被设计师使用其专业工具（Sketch) 和程序员使用代码同时修改的东西了。用例讲的是Airbnb的Styleguide实现。



##### React Meetup - August 22, 2017

第一次参加在500px办公室举办的活动。500px外面的小楼看起来光鲜但办公室比较拥挤。活动首先宣布名称从原先的React Native Meetup改成React Meetup，因为组织者发现React的用户不多的话本地的RN社区也不会壮大。

第一个话题是500px的一位TL讲React/Redux是如何与Rails App结合起来的。他负责的业务我理解像是豆瓣的一拍一摄影服务。话题先讲了他们为什么开始引入React，原因居然只是简单的“因为大家觉得好”，我期待的是针对每个技术选型都能有理有据地说明。(即使我并不反对这个决策，但更想了解背后细致的、基于自身状况的技术选型详述。因为我从实际工作中发现，越来越多的思考和决策发生在“思考清楚是否有必要跟进新工具和技术”上，这尤其适用于前端领域）。接下来讲的是三种在原有前端应用上逐步添加React的方式，但前两个用例都和Rails高度结合：用react的gem、升级rails 5和切换到browserify。然后展开谈了一个应用场景：如何把一个小的弹出窗口替换为react/redux的实现。整个话题不能说没价值，但应用场景过于单一和具体，对于非Rails的团队可能帮助不大。随后听众的问题果然都集中在“为什么要和Rails紧密相关”，答曰因为部署是通过Rails，以及还有其它历史原因需要极力简化其方案（所以没有重写），且团队只有三个人。

第二个话题是mobx简介，演讲者的风格相当生动，在现场用一个简单的实例来给大家演示如何在一个简单的React Todolist项目中使用mobx。不过听众的问题都和mobx不相关，比如“如何持久化store”。有个老先生确认了下babel是否要调整设置才能用decorator，答曰是。我在很久之前使用过Mobx做选型尝试，提问题问了下observable的结构是不是仍非标准JS Object，是否需要经常toJS()。答曰如果用React的binding其实不需要经常toJS，Angular的binding应该也是这样。我想可能我之前的使用方法可能有问题。

第三个话题是同做web开发的双胞胎两兄弟来讲react native如何处理/实现offline。我觉得是当天最好的话题。他们明确地把asyncstorage等几个概念描述清楚，在演示代码的时候对于顺带出现的概念也有简略、清晰的介绍，比如redux的middleware、compose函数需要调用的参数等。其主要介绍了两个库：存储store的react-persist和用来管理离线逻辑的redux-optimistic。另外又顺便提及了对这俩库的包装redux-offline。听众提问则集中在所讲技术的主要应用场景PWA (Progressive Web App)上，他俩索性顺着这个线索又讲了下service worker的前世今生。最后和两兄弟之一聊了一下，他居然接触redux才不久。于是我们一起吐槽了下已经过于蓬勃发展的redux生态圈。
