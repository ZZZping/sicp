SICP
====

<img src="https://sicpebook.files.wordpress.com/2013/09/smile0.png"
 alt="微笑的 Par" align="right" />

这是 Abelson、Sussman 和 Sussman 所著《计算机程序的构造和解释》的新版 HTML5 和 EPUB3 版本。它源自[非官方 Texinfo 格式](http://www.neilvandyke.org/sicp-texi)，该格式由麻省理工学院出版社提供的原始 [HTML 版本](https://mitpress.mit.edu/sicp)转换而来。

<b>EPUB3 格式：[sicp.epub](https://github.com/sarabander/sicp-epub/blob/master/sicp.epub?raw=true)</b>

<b>在线阅读：[HTML 版电子书](https://sarabander.github.io/sicp)</b>

本项目采用了可缩放矢量图形、基于 MathML 和 MathJax 的数学标记、嵌入式网页字体以及语法高亮等现代技术。响应式设计的基础框架已搭建完成，可使页面适应便携设备和平板电脑上的阅读。还需要在小屏幕上进行更多测试，以调整字体大小和排版，因此欢迎智能手机和平板电脑用户提供反馈。

源文件
------

根目录中的 `sicp-pocket.texi` 是 Texinfo 源文件。要重新生成 HTML 文件并构建 EPUB，请输入：

```bash
$ make
```

`html` 目录中的所有文件都会被覆盖，但其子目录中的文件不会，因此应优先在 `sicp-pocket.texi` 中进行修改。EPUB 文件将在项目目录树之外的父目录中生成。

编译本书需要 [Texinfo 5.1](https://ftp.gnu.org/gnu/texinfo)、Perl 5.12 或更高版本、Ruby 1.9.3 或更高版本、[Nokogiri](http://nokogiri.org) gem 包、[PhantomJS](http://phantomjs.org)，以及互联网连接。

致谢
----------------

* Lytha Ayth
* Neil Van Dyke
* Gavrie Philipson
* Li Xuanji
* J. E. Johnson
* Matt Iversen
* Eugene Sharygin

许可证
-------

源文件 `sicp-pocket.texi`、本书的 HTML 内容以及 `html/fig` 目录中的图表，采用 Creative Commons 署名—相同方式共享 4.0 国际许可协议（[CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0)）授权。

大多数脚本采用 GNU 通用公共许可证第 3 版授权（详情参见 LICENSE.src）。

字体采用 SIL 开放字体许可证第 1.1 版授权。其他文件（例如 JavaScript 库）各自适用其相应的许可证。

姊妹项目
--------------

与此 HTML 版本配套的还有一个从 LaTeX 源文件构建的 [PDF 版本](https://github.com/sarabander/sicp-pdf)。
