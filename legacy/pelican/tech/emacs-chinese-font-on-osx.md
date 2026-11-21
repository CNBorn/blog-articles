Date: 2014-10-17
Title: OS X 下调整 Emacs 中文字体
Category: Tech
Tags: Emacs
Lang: zh
Slug: emacs-chinese-font-on-osx


OS X 升级到 Mavericks 之后，Emacs 24 的缺省中文字体意外地成为了[娃娃体](http://zh.wikipedia.org/wiki/%E8%8F%AF%E5%BA%B7%E5%A8%83%E5%A8%83%E9%AB%94)

让 Emacs 的中文字体使用 OS X 的默认华文黑体，在配置文件中加入

    (set-fontset-font "fontset-default" 'han '("STHeiti"))

附:

#### 个人推荐开源的 [Source&trade; Code Pro](http://store1.adobe.com/cfusion/store/html/index.cfm?event=displayFontPackage&code=1960) 字体，适合代码及英文写作工作。

    (set-default-font "Source Code Pro 24”)

后面的24是默认字号，因我的设备 (2010 MacBook Pro 17’) 的屏幕点距关系，我的默认配置字体偏大。

#### 察看系统中安装的所有字体名称 (键入后按 C-j 执行)

     (print (font-family-list))
