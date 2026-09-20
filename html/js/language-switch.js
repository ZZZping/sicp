// Links are already present in XHTML. Enhance navigation without requiring
// JavaScript for the language selector itself to appear or work.
(function () {
  "use strict";
  function enhanceReader() {
    var toolbar = document.querySelector(".reader-toolbar");
    if (!toolbar || toolbar.hasAttribute("data-enhanced")) return;
    toolbar.setAttribute("data-enhanced", "true");

    var chinese = document.documentElement.lang === "zh";
    var links = document.querySelectorAll(".reader-toolbar a[hreflang]");
    function updateTargets() {
      Array.prototype.forEach.call(links, function (link) {
        var target = new URL(link.getAttribute("href"), window.location.href);
        target.hash = window.location.hash;
        target.search = window.location.search;
        link.href = target.href;
        if (link.hreflang === (chinese ? "zh" : "en")) link.setAttribute("aria-current", "page");
      });
    }
    updateTargets();
    window.addEventListener("hashchange", updateTargets);
    Array.prototype.forEach.call(links, function (link) {
      link.addEventListener("click", updateTargets);
    });

    Array.prototype.forEach.call(document.querySelectorAll("nav.header"), function (nav) {
      var seen = {};
      var labels = chinese
        ? {n: "下一节", p: "上一节", u: "上一级", c: "目录"}
        : {n: "Next", p: "Previous", u: "Up", c: "Contents"};
      Array.prototype.forEach.call(nav.querySelectorAll("a[href]"), function (link) {
        var href = link.getAttribute("href");
        // Info's directory link points outside the served book directory.
        if (href === "../index.xhtml" || seen[href]) {
          link.hidden = true;
          return;
        }
        seen[href] = true;
        var text = link.textContent.trim();
        if (text === "UTF") text = chinese ? "非官方 Texinfo 格式" : "Unofficial Texinfo Format";
        var key = link.getAttribute("accesskey");
        link.textContent = key === "c" ? labels.c : (labels[key] || "") + " · " + text;
      });
      Array.prototype.forEach.call(nav.querySelectorAll("p"), function (p) {
        Array.prototype.slice.call(p.childNodes).forEach(function (node) {
          if (node.nodeType === 3) p.removeChild(node);
        });
      });
      nav.classList.add("reader-navigation");
      nav.setAttribute("aria-label", chinese ? "章节导航" : "Chapter navigation");
    });
  }
  // Some XHTML parsers execute deferred scripts before body nodes are ready.
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", enhanceReader);
  } else {
    enhanceReader();
  }
}());
