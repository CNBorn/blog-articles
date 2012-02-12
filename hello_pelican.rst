Hello, Pelican
#########################

:tags: Pelican
:date: 2012-01-09 02:01
:category: Tech
:author: CNBorn

在原先的
`Blog
<http://cnborn.net/blog>`_
被墙许久以后，我始终为自己接下来在哪里写字发愁。后来还专门申请了一个Blogspot打算用于写游记（请参见
`cnborn.info
<http://cnborn.info>`_
）,当时的感觉是无论感觉无论用什么，最后也终究会被墙掉的。鉴于我始终对Wordpress怀有莫名其妙的成见，同时MovableType的安装过程仍然无比繁杂，我也渐渐失去了再费力架设一个Blog的兴致，以及更重要的，写Blog的时间。

直到2011年末，自己才又冒出些念头想要写些什么，尽管自己游记的大坑还没有填完。此时各种静态化Blog的方案已经相当成熟了。静态化是我这种一直使用MovableType的用户始终推崇的，不过Octopress引领的新静态化浪潮才真的让人耳目一新，可以不再考虑性能、资源和墙的问题。不过想了解下有没有Python制作的相应替代品，很荣幸找到了Pelican。最早的一些关于Pelican的信息是在
`微風夕語
<http://bone.twbbs.org.tw/blog/>`_
这个Blog看到的，很感兴趣，同时在西安OpenParty的邮件列表里面向大家推荐。真正使用是在2012年的1月，这天下班路上读书有感觉，精神抖擞地做了笔记，迫切得想和大家分享。心里觉得新的Blog是非弄不可了，一定要把Pelican弄起来。

再次上网搜寻，结果发现前同事DuoDuo已经
`切换到了Pelican
<http://blog.xduo.me/2011/12/17/pelican-static-blog/>`_
，在这篇博文的帮助下顺利更新了之前在硬盘上的测试版本，并放上了新鲜出炉的文章。并同时把自己原来Blog的样式也搬了过来（把原来Fork别人的样式，再次Fork了一遍)，放在了Github上。就是您现在看到这篇文章的模版。如果您喜欢，可以在
`这里
<https://github.com/CNBorn/pelican-themes/tree/master/cnborn>`_
下载安装。

* 安装模版

::

  pelican-themes -i /download_dir/pelican-themes/cnborn/

* 使用模版(在生成Blog时使用-t参数)

::

  pelican /your-blog-source -o /your-blog-output -s /your-pelican.conf.py -t cnborn 

