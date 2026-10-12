// MathJax for the mathematics marked by arithmatex (#285): only those
// elements are typeset, so APL, J and K text elsewhere is left alone.
// SVG output: glyphs are drawn as paths, needing no web fonts or styles.
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
  },
  svg: { fontCache: "global" }
};

// Typeset again when instant navigation brings in a new page; MathJax
// typesets the first page itself.
if (typeof document$ !== "undefined") {
  let first = true;
  document$.subscribe(() => {
    if (first) { first = false; return; }
    if (!window.MathJax || !MathJax.typesetPromise) return;
    MathJax.typesetClear();
    MathJax.texReset();
    MathJax.typesetPromise();
  });
}
