Movable Type 4.3 分页改进
#########################
:date: 2009-12-13 14:25
:category: Software
:status: draft

Movable Type 4.3
版本开始，官方提供了一种分页方法。解决了MT静态化爱好者们实现像各种动态Blog程序，如Wordpress那样，可以一页一页地翻到最后的心愿。
从Movable Type
4.3开始加入的分页方法，其原理是将网站首页进行静态化生成，此后翻页的第2页开始，内容使用MT-Search脚本动态生成。此功能可以在文章索引以及按日期索引上使用。
对于原教旨主义静态化控的朋友们来说，此方案难免差强人意；但是作为普通的用户，这个方案已经是一个近似于完美的方案了。(纯静态化的分页方案，网上也有相关的插件等解决方案。不过这些方案的性能热点在于发布生成这些页面的时间会非常长。相比之下此种方法通过动态访问的性能还是可以接受的，毕竟系统其它页面都是静态页面，资源的耗费在通常情况下可以接受。）据我观察一些大型网站如apple4us所使用的，猜测也是类似的解决方案（如果有误请指正）
官方的Pagination解决方案，请点击：`http://www.movabletype.org/documentation/designer/pagination-static.html#pagination-in-movable-type-43`_
但是在我架设Blog的过程中，发现官方的分页解决方案有如下两个问题：

-  上一页/下一页的链接，在首页是/pages/n.html这种格式，但是在从第二页开始的动态生成页面中，程序就对此链接直接生成了mt-search.cgi?xxxx=xxxx这样的链接，而不是期待中的pages/2.html。不美观同时也不利于SEO
-  同样在从第二页开始的动态生成页面中，页码显示也不正确，只显示出了当前页的页码，而没有所有页面的页码，无法快速翻页。

 于是自己针对原始版本，进行了一些小修改，解决了如上问题。
首先需要确认已经应用官方的分页方式，根据官方的文档，对模板中的 Main Index 模板做出相应修改。
然后确保已经加入Rewrite Rule。我使用的Rewrite Rule如下：(.htaccess放置于网站根目录)

    RewriteEngine on
    #Pagination
    RewriteRule page/([0-9]+).html/?$
    /cgi-bin/mt4/mt-search.cgi?IncludeBlogs=1&template\_id=46&limit=3&archive\_type=Index&page=$1
    [L,QSA]

Pagination分页的url设置为 /page/1.html
这种格式。需要注意的是，用户需要把/cgi-bin/mt4/这个路径，需要修改为和自己blog一致的cgi路径。同时template\_id也要和自己的网站设置一致。
然后我们就动手针对遇到的问题进行修改。要解决这些问题，只要修改Main Index这个模板就可以了。
MT的模板文件中，使用很多MT标签来执行一些简单的程序逻辑，首先让我们看看该问题的根源。
从这里可以发现"上一页"链接的指向。

    <mt:IfPreviousResults>
     <a href="<$mt:PreviousLink$>" rel="prev" onclick="return
    swapContent(-1);">&lt; Previous</a>&nbsp;
     </mt:IfPreviousResults>

可以发现上一页/下一页的链接是由<mt:PreviousLink>以及<mt:NextLink>两个模板标签来控制的。经过测试发现这两个标签会直接输出诸如mt-search.cgi?xxxx=xxx这样的链接。
那么就要把这两个标志用指向页面的链接替换，以达到我们使用直观页面URL的效果。

通过分析下方控制第一页链接的部分，我们可以看到，链接是通过一个记录当前页链接的变量，再组合url来生成的。

    <a href="<$mt:Var name="search\_link"|image0|gt;<$mt:Var
    name="pbpage"|image1|gt;.html"><$mt:Var
    name="\_\_value\_\_"|image2|gt;</a>

这样具体解决这个问题的思路就清晰了：首先找到当前页面的页码，然后生成一个url显示出来，就可以达到我们想要的美观的分页url。
所以我们就需要在<mt:PagerBlock>里面，设置一个记录当前页码的变量。（<mt:PagerBlock是循环体，相当于程序设计语言里的for，遍历程序的所有页面）
我们只需要判断一个循环中的页面是否是当前页，然后设置一个变量即可。但是需要注意的是，我经过很多次实验，发现<mt:IfCurrentPge>这个判断条件判断的，恰恰不是CurrentPage,
<mt:Else>分支下，反而是当前页面的判断，这十分奇怪。（这情况也导致出现这许多问题）
最终修改好的PreviousLink部分代码为：(该部分设置了一个变量currpage，记录当前页面号码）

    <mt:Ignore><!-- Navigation for dynamic pages (same as navigation
    found in the Search Results system template). --></mt:Ignore>
     <mt:IfPreviousResults>
     <mt:PagerBlock>
     <mt:IfCurrentPage>
     <mt:Else>
     <$mt:Var name="currpage" value="$\_\_value\_\_"$>
     </mt:IfCurrentPage>
     </mt:PagerBlock>
     <$mt:SetVar name="currpage" op="--"$>
     <a href="<$mt:Var name="search\_link"$><$mt:Var
    name="currpage"$>.html" rel="prev" onclick="return
    swapContent(-1);">&lt; 上一页</a>&nbsp;
     <$mt:SetVar name="currpage" op="++"$>
     <mt:Else>
     <$mt:Var name="currpage" value=1$>
     </mt:IfPreviousResults>

随后处理并修改页码显示的部分，修改后可以正确显示当前页面以及所有页面。

    <mt:PagerBlock>
     <mt:SetVarBlock name="pbpage"><$mt:Var
    name="\_\_value\_\_"$></mt:SetVarBlock>
     <mt:If name="pbpage" ne="$currpage"><a href="<$mt:Var
    name="search\_link"$><$mt:Var name="pbpage"$>.html"><$mt:Var
    name="\_\_value\_\_"$></a></mt:If>
     <mt:IfCurrentPage><mt:Else>
     <$mt:Var name="\_\_value\_\_"$><$mt:Var name="currpage"
    value="$\_\_value\_\_"$>
     </mt:IfCurrentPage>
     </mt:PagerBlock>

最后是处理下一页的链接部分：

    <mt:IfMoreResults>
     <$mt:SetVar name="currpage" op="++"$>
     &nbsp;<a href="<$mt:Var name="search\_link"$><$mt:Var
    name="currpage"$>.html" rel="next" onclick="return
    swapContent();">下一页 &gt;</a>
     </mt:IfMoreResults>

进行完这些修改后，从第二页开始的动态生成的分页页面中的链接，以及所有的页码链接，都可以显示正确了。
倘若没有耐心读完前面逐步修改与分析的结果，也可把如下完整的修改后的分页模板代码粘贴到Main Index模板中，覆盖 从 <mt:Ignore>
Create pagination 开始，直到 <a href="<$mt:Link
template="archive\_index"$>">Archive Index</a> 这部分代码即可。
修改后的分页效果可查看我的Blog`第二页`_的显示效果

    <mt:Ignore><!-- Create pagination navigation. Condition based upon
    if page is statically or dynamically rendered using the
    search\_results variable. --></mt:Ignore>
    <mt:Ignore><!-- pagination url mod by CNBorn, cnborn.net
    --></mt:Ignore>
    <mt:SetVarBlock name="pagination\_navigation">
     <mt:If name="search\_results">
     <mt:Ignore><!-- Navigation for dynamic pages (same as navigation
    found in the Search Results system template). --></mt:Ignore>
     <mt:IfPreviousResults>
     <mt:PagerBlock>
     <mt:IfCurrentPage>
     <mt:Else>
     &n
     bsp; <$mt:Var name="currpage" value="$\_\_value\_\_"$>
     </mt:IfCurrentPage>
     </mt:PagerBlock>
     <$mt:SetVar name="currpage" op="--"$>
     <a href="<$mt:Var name="search\_link"$><$mt:Var
    name="currpage"$>.html" rel="prev" onclick="return
    swapContent(-1);">&lt; 上一页</a>&nbsp;
     <$mt:SetVar name="currpage" op="++"$>
     <mt:Else>
     <$mt:Var name="currpage" value=1$>
     </mt:IfPreviousResults>
     <mt:PagerBlock>
     <mt:SetVarBlock name="pbpage"><$mt:Var
    name="\_\_value\_\_"$></mt:SetVarBlock>
     <mt:If name="pbpage" ne="$currpage"><a href="<$mt:Var
    name="search\_link"$><$mt:Var name="pbpage"$>.html"><$mt:Var
    name="\_\_value\_\_"$></a></mt:If>
     <mt:IfCurrentPage><mt:Else>
     <$mt:Var name="\_\_value\_\_"$><$mt:Var name="currpage"
    value="$\_\_value\_\_"$>
     </mt:IfCurrentPage>
     </mt:PagerBlock>
     <mt:IfMoreResults>
     <$mt:SetVar name="currpage" op="++"$>
     &nbsp;<a href="<$mt:Var name="search\_link"$><$mt:Var
    name="currpage"$>.html" rel="next" onclick="return
    swapContent();">下一页 &gt;</a>
     </mt:IfMoreResults>
     <mt:Else>
     <mt:Ignore><!-- Navigation for statically published page.
    --></mt:Ignore>
     <mt:If name="archive\_template">
     <$mt:ArchiveCount setvar="total\_entries"$>
     <mt:Else>
     <$mt:BlogEntryCount setvar="total\_entries"$>
     </mt:If>
     <mt:Ignore><!-- If blog contains more entries than the number of
    entries to display per page. --></mt:Ignore>
     <mt:If name="total\_entries" gt="$entries\_per\_page">
     <mt:Ignore><!-- Set the total number of entries to iterate through
    the pages. --></mt:Ignore>
     <mt:Ignore><!-- IF total entries divided by entries per page is a
    whole number. --></mt:Ignore>
     <mt:If name="total\_entries" op="%" value="$entries\_per\_page"
    eq="0">
     <mt:Ignore><!-- Set total pages to total entries divided by entries
    per page. --></mt:Ignore>
     <$mt:Var name="total\_entries" op="/" value="$entries\_per\_page"
    setvar="total\_pages"$>
     <mt:Else>
     <mt:Ignore><!-- Get the remainder when dividing total entries by
    entries per page. --></mt:Ignore>
     <$mt:Var name="total\_entries" op="%" value="$entries\_per\_page"
    setvar="remainder"$>
     <mt:Ignore><!-- Subtract remainder from total entries.
    --></mt:Ignore>
     <$mt:Var name="total\_entries" op="-" value="$remainder"
    setvar="total\_entries"$>
     <mt:Ignore><!-- Determine total pages by dividing total entries
    (minus remainder) by entries per page. --></mt:Ignore>
     <$mt:Var name="total\_entries" op="/" value="$entries\_per\_page"
    setvar="total\_pages"$>
     <mt:Ignore><!-- Add one page to handle the remainder of entries.
    --></mt:Ignore>
     <$mt:SetVar name="total\_pages" op="++"$>
     </mt:If>
     <mt:Ignore><!-- Loop through total pages, creating links to all but
    the first page (which is the current page). --></mt:Ignore>
     <mt:For from="1" to="$total\_pages" step="1">
     <mt:If name="\_\_first\_\_">
     <$mt:Var name="\_\_index\_\_"$>
     <mt:Else>
     <a href="<$mt:Var name="search\_link"$><$mt:Var
    name="\_\_index\_\_"$>.html"><$mt:Var name="\_\_index\_\_"$></a>
     </mt:If>
     </mt:For>
     <mt:Ignore><!-- Hard-coded link to the next page (page 2).
    --></mt:Ignore>
     &nbsp;<a href="<$mt:Var name="search\_link"$>2.html" rel="next">下一页
    &raquo;</a>
     </mt:If>
     </mt:If>
    </mt:SetVarBlock>
    <mt:Ignore><!-- Strip space and trim navigation code.
    --></mt:Ignore>
    <$mt:Var name="pagination\_navigation" strip=" " trim="1"
    setvar="pagination\_navigation"$>
    <div class="content-nav">
    <mt:Ignore><!-- Output variable if exists. --></mt:Ignore>
    <$mt:Var name="pagination\_navigation" strip=" " trim="1"
    setvar="pagination\_navigation"$>
    <mt:If name="pagination\_navigation">
     <div class="pagination-navigation">
     <$mt:Var name="pagination\_navigation"$>
    &nbs
     p; </div>
    </mt:If>
     <a href="<$mt:Link template="archive\_index"$>">历史归档</a>
    </div>

.. _`http://www.movabletype.org/documentation/designer/pagination-static.html#pagination-in-movable-type-43`: http://www.movabletype.org/documentation/designer/pagination-static.html#pagination-in-movable-type-43
.. _第二页: http://cnborn.net/blog/page/2.html

.. |image0| image:: http://docs.google.com/goog_1260681303154
.. |image1| image:: http://docs.google.com/goog_1260681303154
.. |image2| image:: http://docs.google.com/goog_1260681303154
