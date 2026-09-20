// English and Chinese editions share filenames (apart from _zh) and anchor IDs.
(function () {
  "use strict";

  function addLanguageSwitch() {
    if (document.getElementById("language-switch")) return;

    var target = new URL(window.location.href);
    // Also support servers configured to serve index.xhtml for directory URLs.
    var path = target.pathname.replace(/\/$/, "/index.xhtml");
    if (!/\.xhtml$/.test(path)) return;

    var isChinese = /_zh\.xhtml$/.test(path);
    target.pathname = isChinese
      ? path.replace(/_zh\.xhtml$/, ".xhtml")
      : path.replace(/\.xhtml$/, "_zh.xhtml");

    // XHTML served as application/xhtml+xml requires namespaced elements.
    var link = document.createElementNS("http://www.w3.org/1999/xhtml", "a");
    link.id = "language-switch";
    link.className = "language-switch";
    link.textContent = isChinese ? "English" : "中文";
    link.hreflang = isChinese ? "en" : "zh";
    link.lang = link.hreflang;
    link.title = isChinese ? "切换到本页英文版" : "Read this page in Chinese";
    link.setAttribute("aria-label", link.title);

    function updateTarget() {
      target.hash = window.location.hash;
      target.search = window.location.search;
      link.href = target.href;
    }

    updateTarget();
    window.addEventListener("hashchange", updateTarget);
    link.addEventListener("click", updateTarget);
    document.body.appendChild(link);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", addLanguageSwitch);
  } else {
    addLanguageSwitch();
  }
}());
