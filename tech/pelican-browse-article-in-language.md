Title: Pelican - Browse articles by language
Date: 2014-08-28 22:37
Category: Tech
Lang: en
Tags: Pelican
Slug: pelican-browse-articles-by-language

Recently I wrote a pelican plugin called [pelican-langcategory](https://github.com/CNBorn/pelican-langcategory) to let visitors can browse articles by language. As an result, you can view all [english articles on my blog](http://cnborn.net/blog/lang/en/) as well as [the chinese ones](http://cnborn.net/blog/lang/cn/). 

> In case you don't know what pelican is, it is a popular static blog generator which powered by Python, You can learn more at [Pelican Homepage](http://blog.getpelican.com/).

I came up the idea to let visitor browse articles by language, but found current version of pelican is not capable of doing this. There are [other people calling for this feature](https://github.com/getpelican/pelican/issues/1393), I'm glad to see a comrade here so I want to do this. The plugin itself is easy to implement once you've looked into basic [Pelican-internal](http://docs.getpelican.com/en/3.4.0/internals.html). I started hacking into pelican first, but soon found a plugin will be feasible and neat solution.

The default pelican language principle: A blog has a default language and usually an article other than default language will be a translation post which co-exists with original article, is kind of ignored by this plugin, which please bloggers who write articles in more than one language and usually don't do translations on their blog. If this is what you are looking for, [peican-langcategory](https://github.com/CNBorn/pelican-langcategory) is made for you.

Hope you will like it, I'm looking forward for your reply and feedback! For more information on Installtion/Usage/Feedback, please go to [pelican-langcategory on Github](https://github.com/CNBorn/pelican-langcategory).


