// Subtle fade and rise as content scrolls into view.
// Does nothing for visitors who ask for reduced motion, or in old browsers.
(function () {
  if (!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var els = document.querySelectorAll('header.top > *, .lead-shots .fig, .projects .proj, .sec .wrap > *');
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -6% 0px' });
  document.documentElement.classList.add('motion');
  els.forEach(function (el) { el.classList.add('rise'); io.observe(el); });
})();
