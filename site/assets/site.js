/* assets/site.js  -  shared behaviour for every page.
   Every block guards on the element existing, so the one file is safe to
   load on pages with no hero, no marquee and no form. */
(function () {
  document.documentElement.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- hero slideshow, if more than one .hero-img is ever added back.
         Under prefers-reduced-motion the first slide simply stays put. --- */
  var slides = document.querySelectorAll('.hero-img');
  if (slides.length > 1 && !reduce) {
    var shown = 0;
    setInterval(function () {
      slides[shown].classList.remove('on');
      shown = (shown + 1) % slides.length;
      slides[shown].classList.add('on');
    }, 6500);
  }

  /* --- the logo rows loop by translating the track -50%, so the second
         half has to be an exact copy of the first. If one pass is narrower
         than the screen the set is repeated first, so no blank gap ever
         drags through the row. Clones are hidden from assistive tech. --- */
  document.querySelectorAll('.track[data-loop]').forEach(function (track) {
    var originals = Array.prototype.slice.call(track.children);
    var clone = function (node) {
      var c = node.cloneNode(true);
      c.setAttribute('aria-hidden', 'true');
      track.appendChild(c);
    };
    for (var guard = 0; track.scrollWidth < innerWidth + 240 && guard < 8; guard++) {
      originals.forEach(clone);
    }
    Array.prototype.slice.call(track.children).forEach(clone);
    /* pace by distance, not by a fixed duration: 34px a second throughout */
    var travel = track.scrollWidth / 2;
    if (travel > 0) track.style.animationDuration = Math.round(travel / 34) + 's';
  });

  /* --- reveal on scroll ---
     A sweep rather than IntersectionObserver, so landing mid-page on an
     anchor, or one fast flick, never strands a block at opacity 0. */
  var pending = Array.prototype.slice.call(document.querySelectorAll('.rise'));
  if (reduce) {
    pending.forEach(function (el) { el.classList.add('in'); });
  } else {
    var queued = false;
    var sweep = function () {
      queued = false;
      var line = innerHeight * 0.92;
      pending = pending.filter(function (el) {
        if (el.getBoundingClientRect().top > line) return true;
        var sibs = Array.prototype.slice.call(el.parentNode.children).filter(function (n) {
          return n.classList && n.classList.contains('rise');
        });
        el.style.transitionDelay = Math.min(sibs.indexOf(el), 6) * 60 + 'ms';
        el.classList.add('in');
        return false;
      });
      if (!pending.length) removeEventListener('scroll', onSweep);
    };
    var onSweep = function () {
      if (!queued) { queued = true; requestAnimationFrame(sweep); }
    };
    sweep();
    addEventListener('scroll', onSweep, { passive: true });
    addEventListener('resize', onSweep);
  }

  /* --- mobile menu --- */
  var mb = document.querySelector('.menu-btn');
  var panel = document.getElementById('nav-links');
  if (mb && panel) {
    var setOpen = function (open) {
      mb.setAttribute('aria-expanded', open ? 'true' : 'false');
      panel.setAttribute('data-open', open ? 'true' : 'false');
    };
    mb.addEventListener('click', function () {
      setOpen(mb.getAttribute('aria-expanded') !== 'true');
    });
    panel.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
    addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mb.getAttribute('aria-expanded') === 'true') { setOpen(false); mb.focus(); }
    });
  }

  /* --- the enquiry form composes an email. There is no backend: nothing
         is stored, and nothing is sent until the visitor sends it from their
         own mail app. A link carrying data-service="<slug>" preselects the
         matching option on its way down to the form. --- */
  var form = document.getElementById('enquiry');
  if (form) {
    var sel = document.getElementById('q-service');
    document.querySelectorAll('a[data-service]').forEach(function (a) {
      a.addEventListener('click', function () {
        var pick = a.getAttribute('data-service');
        Array.prototype.forEach.call(sel.options, function (o) {
          if (o.getAttribute('data-slug') === pick) sel.value = o.value;
        });
      });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var val = function (id) { var el = document.getElementById(id); return el ? (el.value || '').trim() : ''; };
      var name = val('q-name'), mail = val('q-email'), phone = val('q-phone'),
          company = val('q-company'), service = val('q-service'), msg = val('q-msg');
      var note = document.getElementById('enquiry-note');
      if (!name || (!mail && !phone)) {
        note.textContent = 'Please add your name, and an email address or a phone number so we can reply.';
        document.getElementById(name ? 'q-email' : 'q-name').focus();
        return;
      }
      var lines = ['Hello Cyan Technology,', '', msg || 'I would like to talk about ' + service.toLowerCase() + '.', '',
                   'Name: ' + name];
      if (company) lines.push('Company: ' + company);
      if (mail) lines.push('Email: ' + mail);
      if (phone) lines.push('Phone: ' + phone);
      lines.push('Interested in: ' + service);
      var to = form.getAttribute('data-to');
      location.href = 'mailto:' + to +
        '?subject=' + encodeURIComponent('Enquiry: ' + service + (company ? ' / ' + company : '')) +
        '&body=' + encodeURIComponent(lines.join('\n'));
      note.textContent = 'Opening your email app with the enquiry written out, ready to send.';
    });
  }

  /* --- on the home page, mark the section being read --- */
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav-links a')).filter(function (a) {
    return (a.getAttribute('href') || '').charAt(0) === '#';
  });
  var targets = links.map(function (a) { return document.querySelector(a.getAttribute('href')); });
  if (links.length && 'IntersectionObserver' in window) {
    var visible = [];
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var i = targets.indexOf(e.target);
        if (i < 0) return;
        var at = visible.indexOf(i);
        if (e.isIntersecting && at < 0) visible.push(i);
        if (!e.isIntersecting && at >= 0) visible.splice(at, 1);
      });
      links.forEach(function (a) { a.removeAttribute('aria-current'); });
      if (!visible.length) return;
      var best = visible.slice().sort(function (a, b) {
        return targets[a].getBoundingClientRect().top - targets[b].getBoundingClientRect().top;
      })[0];
      links[best].setAttribute('aria-current', 'page');
    }, { rootMargin: '-45% 0px -50% 0px' });
    targets.forEach(function (t) { if (t) io.observe(t); });
  }
})();
