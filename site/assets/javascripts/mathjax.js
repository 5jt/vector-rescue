// MathJax for the mathematics marked by arithmatex (#285): only those
// elements are typeset, so APL, J and K text elsewhere is left alone.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// Typeset again after each instant-navigation page load.
if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    if (!window.MathJax.typesetPromise) return;
    MathJax.startup.output.clearCache();
    MathJax.typesetClear();
    MathJax.texReset();
    MathJax.typesetPromise();
  });
}
