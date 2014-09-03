Bugzilla中针对不同产品的权限设定
####################
:date: 2009-04-28 17:58
:category: Software
:status: draft

`Bugzilla`_是一个经典的软件缺陷追踪工具，最初版本由Netscape开发，1998年遵循Mozilla Public
License协议公开源代码。Bugzilla作为功能强大的Bug Tracking系统，在无数的商业/非商业组织和项目中得到广泛的应用。
Bugzilla

系统中默认的设计是可将所有的信息对任何人开放，但是针对用户应用需求的不同，可以针对不同产品设置不同的权限设定。可以适用于如：在一个大公司的多个软
 件项目组，通过一个全公司的Bugzilla系统来追踪各个项目的Bug，各个组之间的人员并不能查看或编辑其它组的内容等类似情况。
事实上Bugzilla

网站上的手册里针对此部分有很详细的说明，但是我在使用中发现，互联网上还没有对此进行介绍的较为详细的文章，同时如果没有通过实际的例子来将设置方法加

以展示的话，整个设置和对照英文文档的过程还是让人感觉晦涩及难以理解。所以本篇文章将以Bugzilla系统应用中的实例来讲解下如何对不同产品的权限
 进行设定。
（本篇文章的内容在Bugzilla 3.2,3.2.3中测试完成，Bugzilla后续版本可能会对此部分功能进行变更，请在使用及部署中注意）
**本文目的与要求：**
通过实例讲述在Bugzilla系统中如何针对用户应用需求的不同，针对不同产品设置不同的权限。
您需要对Bugzilla有简单的了解和部署经验，并且已经在开始使用Bugzilla。本文中不会针对个别选项、设置进行事无巨细的探讨，也不保证所讲述
 的内容涉及到权限设置部分的各个方面。仅以一些实例，为各位Bugzilla用户在各自的应用中起到一些抛砖引玉的作用。
**设置不同组权限设置的前提要求：**

首先需要完成Bugzilla里的分组设置。如可根据用户的不同分为"质量"、"前端"、"测试"等不同的用户组。用户可以同属为多个组。组的分类可以和

要提交问题的产品相关，如针对"质量"的问题，会有一个对应的"质量"人员组；也可以和问题不相关，如通常为了管理方便，我会创建一个"部门主管"组（可
 查看所有记录）、以及"所有用户"组（通过通配符 .\*
 匹配所有用户，在使用中可简化一些设置）。以下的几个实例的解决方法，会遵循我在这里的用户组设计。
 如需设置组分类和产品分类相对应，可启用Bugzilla->管理->参数设置->组安全设置
中的makeproductgroups选项。启用此选项后，每创建一个新产品，系统均会自动在用户组中创建一个与此产品对应的用户组。
**产品分组权限设置页面：**
 无特殊说明，均在Bugzilla->管理->产品管理->产品页面->编辑组访问控制页面中

**权限设计需求实例:
**

#. 每个用户都可以提交不同产品的Bug
#. 所有用户均可编辑问题/只有相应组的用户才能编辑相应的问题
#. 所有用户在提交问题时，均可选择此问题是否针对其它各个部门的人员可见
#. 产品严格分组，不同的产品组只能查看相应组的产品Bug信息 - 此范例来自 Bugzilla官方手册
#. 创建一个只读产品（此产品的相关信息只能查看，不能提交和修改）- 此范例来自 Bugzilla官方手册

问题1解决：
 选中"所有用户"组的Entry选项
问题1解决说明：
 Entry
选项决定了一个组的用户是否有权限可以针对一个产品提交问题。同时如果有至少一个组选择了Entry这个选项的话，那么其它没有选择的组均无法针对此产品提出问题
问题2解决：
 所有用户均可编辑问题：选中"所有用户"组的editbugs选项
 只有相应组的用户才能编辑相应的问题：依次编辑各个产品，选中相应组的Editbug选项
问题2解决说明：

Editbug 以及 editbugs 两个选项的差别：

-  当有任何一个组选择了Editbug选项后，其它未选择的组均无法编辑此产品
-  如果有一个组选择了editbugs以后，该组即可编辑此产品的所有问题

问题3解决
 修改相应其他组的MemberControl、OtherControl权限
 这两个权限各有三个选项
 简单说明，
 一个组的MemberControl指操作中用户属于这个组时，
 Default指可以在界面上选择此组用户是否可查看此产品问题，并且默认此选项选中
 Mandatory指在界面上无法选择此组用户是否可查看此产品问题，但此问题设置为强制与此组用户相关
 Show指可以在界面上选择此组用户是否可查看此产品问题，并且默认此选项不选中
 N/A指与此组完全没有关系，无法访问
 一个组的MemberControl指操作中的用户不属于这个组时的情况，三个选项和上面的相同。
 举个例子
 倘若有一个"主管"用户组，可查看/编辑所有提交的信息（并且此设置不可能由其它用户或相关的Bug提交者所改变），权限可设置为
 主管 Mandatogy Mandatory editbugs

倘若有一个问题，可能需要"质量"、"前端"组用户查看，但需要提交此问题的用户（所有用户，可以不是这两个组的成员）在提交时进行设置。同时还不需要让"程序"组的用户查看，那么权限可设置为
 质量 Shown Shown
 前端 Shown Shown
 程序 N/A N/A
 所有用户 Entry (或设置为 除"程序"组以外的其他组均可以Entry)
 针对问题三的情况，应该设置成为：
 对其他可能会与此问题相关的用户组，权限设置成为 Shown Shown
 这样在提交问题时，选项里就会出现"是否让一下组查看问题"的选项了。
问题4解决：(此问题可视作问题3里设置权限的例子的一个延续)

产品A里面采用如下设定：
 A组: ENTRY, MANDATORY/MANDATORY
产品B:
 B组: ENTRY, MANDATORY/MANDATORY

问题5解决：(此问题可视作问题3里设置权限的例子的一个延续)
 创建一个用户组，名为"只读"。将需要设置权限的产品设置为

::

            只读 Entry, N/A N/A, CanEdit        简单说明                Entry及CanEdit均为排他设置，只要确保"只读"组没有用户，即可实现无用户可提交和编辑此产品的Bug信息。

Mozilla官方手册中还有不少权限设置的实例，相信在读完以上部分以后，理解`Mozilla的说明`_会更加方便一些。
本文的大多数内容均经过我的实验，但是仅供参考之用，我不能确定文章中的所有设置均正确并适应您的需求，总的来说，Bugzilla的设置，还需要在实践中加以揣摩。
在日后时间宽裕时可能会对此文章进行进一步补充。如对此文章由什么意见或纠正，欢迎留言或直接给我写信，我的邮箱是 我的英文ID@gmail.com
最后需要明确的是"产品"这个概念。我在工作中搭建的Bugzilla系统均不是应用于软件开发领域，而是对流程中的问题进行追踪。"产品"这个在

Bugzilla中的概念，可能在Bugzilla系统根据用户需求进行定制的过程中被其它文字替换。关于针对Bugzilla系统进行定制的更多信息，
 欢迎查看这篇文章：`OpenParty
"有狐"`_，在此次活动中，我进行了一个"Bugzilla系统部署、定制"的演讲，具体的介绍幻灯片可以查看这里`《Bugzilla @
Customization》`_。
作者：`CNBorn`_，`bugzilla-cn`_ (Bugzilla中文本地化)项目组成员
**主要参考文档
**本文中Bugzilla的中文翻译均来自 `bugzilla-cn`_ (Bugzilla中文本地化项目)
Bugzilla官方文档中对于产品组权限部分的说明(Bugzilla 3.2)
`http://www.bugzilla.org/docs/3.2/en/html/products.html#product-group-controls`_
Bugzilla权限管理讨论，这个是我在中文互联网上发现的少见的关于此问题的帖子，只有2句话，总结得不错
`http://topic.csdn.net/t/20061226/23/5258177.html`_

.. _Bugzilla: http://bugzilla.org/
.. _Mozilla的说明: http://www.bugzilla.org/docs/3.2/en/html/products.html#product-group-controls
.. _OpenParty
"有狐": http://cnborn.net/blog/2009/03/openparty-mozilla-event.html
.. _《Bugzilla @
Customization》: http://docs.google.com/Presentation?id=ajgc2xkd4rgc_24fthmz2cn
.. _CNBorn: http://cnborn.net/
.. _bugzilla-cn: http://code.google.com/p/bugzilla-cn/
.. _`http://www.bugzilla.org/docs/3.2/en/html/products.html#product-group-controls`: http://www.bugzilla.org/docs/3.2/en/html/products.html#product-group-controls
.. _`http://topic.csdn.net/t/20061226/23/5258177.html`: http://topic.csdn.net/t/20061226/23/5258177.html
