"""Write the one-page site into site/index.html.

    python tools/build.py

The copy lives in content.py; this file only arranges it. The page is
generated rather than hand-written because the eleven service cards, the
eleven products, forty drifting client logos and the enquiry form's options
are all lists, and a list typed out by hand drifts out of step with itself.
"""
import html
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from content import *  # noqa: E402,F401,F403

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
FONTS = ("https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,200..600;"
         "1,6..72,200..600&family=Outfit:wght@300;400;500&display=swap")
ORG_ID = BASE + "/#org"
TEL = "tel:" + PHONE
MAILTO = "mailto:" + EMAIL

NAV = [("#about", "About"), ("#services", "Services"), ("#products", "Products"),
       ("#clients", "Clients"), ("#process", "How we work"), ("#contact", "Contact")]


def esc(s):
    return html.escape(s, quote=True)


def plain(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def service_card(i, s):
    meta = "".join(f"<span>{m}</span>" for m in s["meta"])
    return f"""        <article class="card rise">
          <p class="no">{i:02d}</p>
          <h3>{s['name']}</h3>
          <span class="rule" aria-hidden="true"></span>
          <p>{s['card']}</p>
          <p class="meta">{meta}</p>
        </article>"""


def product_card(p):
    name, sub, img = p
    return f"""        <article class="product rise">
          <span class="shot"><img src="assets/img/{img}" width="640" height="640" loading="lazy" alt="{name} logo"></span>
          <h3>{name}</h3>
          <p class="sub">{sub}</p>
        </article>"""


def logo_tile(stem):
    name = CLIENTS.get(stem)
    alt = esc(name) if name else "Client logo"
    return (f'<span class="logo-tile"><img src="assets/clients/{stem}.webp" width="194" height="124" '
            f'loading="lazy" alt="{alt}"></span>')


def steps(items):
    return "\n".join(f"""        <article class="step rise">
          <p class="no">{i + 1:02d}</p>
          <h3>{t}</h3>
          <p>{d}</p>
        </article>""" for i, (t, d) in enumerate(items))


def graph():
    return [
        {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": BRAND,
         "inLanguage": "en", "publisher": {"@id": ORG_ID}},
        {"@type": ["Organization", "LocalBusiness"], "@id": ORG_ID, "name": LEGAL,
         "alternateName": ["Cyan Technology", "CyanGits"], "url": BASE + "/",
         "logo": BASE + "/assets/logo.svg", "image": BASE + "/assets/img/hero.webp",
         "telephone": PHONE, "email": EMAIL,
         "address": {"@type": "PostalAddress", "streetAddress": "Prince Nayef Street, 3rd Cross",
                     "addressLocality": "Al Khobar", "addressRegion": "Eastern Province",
                     "postalCode": "34429", "addressCountry": "SA"},
         "areaServed": [{"@type": "Country", "name": "Saudi Arabia"}, {"@type": "Country", "name": "India"}],
         "description": "IT services for businesses and institutions: software and ERP, mobile and web development, "
                        "hosting and cloud, WhatsApp API, bulk SMS and email, social media and graphic design.",
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "IT services", "itemListElement": [
             {"@type": "Offer", "itemOffered": {"@type": "Service", "name": plain(s["name"]),
                                                "description": plain(s["card"])}} for s in SERVICES]}},
    ]


def build():
    title = "Cyan Technology | IT Solutions & Software Development in Al Khobar, Saudi Arabia"
    desc = ("Software and ERP, mobile and web development, hosting and cloud, WhatsApp API, bulk SMS and email "
            "for businesses and institutions. Al Khobar, Saudi Arabia. 900+ active clients.")
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph()}, indent=2, ensure_ascii=False)

    nav = "\n".join(f'      <a href="{h}">{t}</a>' for h, t in NAV)
    cards = "\n".join(service_card(i + 1, s) for i, s in enumerate(SERVICES))
    stats = "\n".join(f'          <div class="stat"><b>{n}<sup>+</sup></b><span>{t}</span></div>' for n, t in STATS)
    prods = "\n".join(product_card(p) for p in PRODUCTS)
    row_a = "\n".join("          " + logo_tile(s) for s in ROW_A)
    row_b = "\n".join("          " + logo_tile(s) for s in ROW_B)
    options = "\n".join(f'              <option data-slug="{s["slug"]}">{s["name"]}</option>' for s in SERVICES)
    foot_svc = "\n".join(f'          <li><a href="#services">{s["name"]}</a></li>' for s in SERVICES)
    addr = "<br>\n            ".join(ADDRESS_LINES)
    map_src = ("https://maps.google.com/maps?q=" + MAP_Q.replace(" ", "%20").replace(",", "%2C")
               + "&amp;z=15&amp;output=embed")
    map_link = ("https://www.google.com/maps/search/?api=1&amp;query="
                + MAP_Q.replace(",", "%2C").replace(" ", "+"))

    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{BASE}/">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#F6F9F9">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:locale" content="en_SA">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{BASE}/">
<meta property="og:image" content="{BASE}/assets/img/hero.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/site.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<a class="sr-only" href="#main">Skip to content</a>

<header class="nav">
  <div class="shell nav-in">
    <a href="#top" aria-label="{BRAND}, back to top">
      <img class="logo" src="assets/logo.svg" width="685" height="128" alt="{LEGAL}">
    </a>
    <nav class="nav-links" id="nav-links" aria-label="Main">
{nav}
      <a class="btn btn-cyan" href="#contact">Get a quote</a>
    </nav>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-links" aria-label="Menu">
      <span class="bars" aria-hidden="true"></span>
    </button>
    <div class="nav-end">
      <a class="nav-tel" href="{TEL}">{PHONE_SHOW}</a>
      <a class="btn btn-cyan" href="#contact">Get a quote</a>
    </div>
  </div>
</header>

<main id="main">
  <!-- ══════════ 1 · HERO ══════════ -->
  <section class="hero" id="top">
    <img class="hero-img on" src="assets/img/hero.webp" width="2400" height="1500" fetchpriority="high"
         alt="A glowing teal wireframe polyhedron hovering above a reflective black floor.">
    <div class="shell">
      <h1 class="rise">Your partner in innovation, from the first line of code to the <em>server it runs on</em>.</h1>
      <p class="lede rise">
        Software and ERP, mobile and web development, hosting and cloud, and business messaging,
        for companies, schools and universities across the Kingdom and beyond.
      </p>
      <div class="cta rise">
        <a class="btn btn-cyan" href="#contact">Talk to us</a>
        <a class="btn btn-ghost" href="#services">Explore services</a>
      </div>
      <div class="hero-facts rise">
        <div><b>900+</b><span>Active clients</span></div>
        <div><b>965+</b><span>Projects completed</span></div>
        <div><b>150+</b><span>Professional team</span></div>
      </div>
    </div>
  </section>

  <!-- ══════════ 2 · ABOUT ══════════ -->
  <section class="band on-white" id="about">
    <div class="shell">
      <div class="sec-head center narrow">
        <p class="eyebrow mid rise">About the company</p>
        <h2 class="rise">Great minds create great products.</h2>
      </div>

      <div class="about-body">
        <figure class="picture rise">
          <img src="assets/img/team.webp" width="1280" height="720" loading="lazy"
               alt="Three colleagues leaning over a desk together, working through a plan on paper.">
          <figcaption><b>{LEGAL}</b><span>Al Khobar, Kingdom of Saudi Arabia</span></figcaption>
        </figure>

        <div class="about-text">
          <div class="prose rise">
            <p>{ABOUT_LONG}</p>
            <p>{ABOUT_WHO}</p>
            <p class="reach"><span>Middle East</span><span>India</span><span>Europe</span></p>
          </div>
          <div class="prose rise">
            <dl class="mv">
              <div><dt>Our mission</dt><dd>{MISSION}</dd></div>
              <div><dt>Our vision</dt><dd>{VISION}</dd></div>
            </dl>
          </div>
        </div>

        <div class="stats rise">
{stats}
        </div>
      </div>
    </div>
  </section>

  <!-- ══════════ 3 · SERVICES ══════════ -->
  <section class="band on-paper wide" id="services">
    <div class="shell">
      <div class="sec-head">
        <p class="eyebrow rise">Our services</p>
        <h2 class="rise">Eleven services, one team that answers for all of them.</h2>
      </div>

      <div class="cards">
{cards}
        <a class="card card-ask rise" href="#contact">
          {ARROW_UP}
          <p class="no">Ask</p>
          <h3>Not sure which you need?</h3>
          <span class="rule" aria-hidden="true"></span>
          <p>Tell us what the business runs on today and where it is stuck, and we will suggest where to start.</p>
          <p class="meta"><span>Free first conversation</span></p>
        </a>
      </div>
    </div>
  </section>

  <!-- ══════════ 4 · THE SPINE ══════════ -->
  <section class="band on-ice" id="why">
    <div class="shell">
      <div class="sec-head center narrow">
        <p class="eyebrow mid rise">Why Cyan</p>
        <h2 class="rise">Building it is half the job. Keeping it running is the other half.</h2>
        <p class="lede rise">Three things we hold to while it is being built, and three once it is live.</p>
      </div>

      <div class="strands">
        <div class="strand-heads rise">
          <p class="strand-label">While we build</p>
          <p class="strand-label">Once it is live</p>
        </div>
        <div class="col col-l">
          <article class="strand rise">
            <span class="side">While we build</span>
            <h3>Research before code</h3>
            <p>We start with your customers and your market, so the product answers a real need and keeps you competitive.</p>
          </article>
          <article class="strand rise">
            <span class="side">While we build</span>
            <h3>Smarter solutions</h3>
            <p>Software shaped around how the business actually runs, with new technology used where it earns its place.</p>
          </article>
          <article class="strand rise">
            <span class="side">While we build</span>
            <h3>Faster to market</h3>
            <p>New products built, or existing ones modernised, in a timely and cost-effective way, so you adapt as quickly as the market does.</p>
          </article>
        </div>
        <div class="col col-r">
          <article class="strand rise">
            <span class="side">Once it is live</span>
            <h3>Data protection</h3>
            <p>Sensitive information secured, unauthorised access prevented, and privacy and security regulations complied with.</p>
          </article>
          <article class="strand rise">
            <span class="side">Once it is live</span>
            <h3>Systems kept optimised</h3>
            <p>Performance, security and reliability tuned continuously, so operations stay streamlined as the business grows.</p>
          </article>
          <article class="strand rise">
            <span class="side">Once it is live</span>
            <h3>One point of contact</h3>
            <p>A first-response team that listens, answers clearly and resolves quickly, under a single contract for every system.</p>
          </article>
        </div>
        <div class="strands-foot rise">
          <img src="assets/mark.svg" width="98" height="112" alt="" aria-hidden="true">
          <p>&ldquo;Innovation is not just a goal; it is the principle that drives our growth.&rdquo;</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ══════════ 5 · PRODUCTS ══════════ -->
  <section class="band on-paper2 wide" id="products">
    <div class="shell">
      <div class="sec-head">
        <p class="eyebrow rise">Our products</p>
        <h2 class="rise">Software we have built, ready to run yours.</h2>
      </div>
      <div class="products">
{prods}
        <a class="product product-ask rise" href="#contact" data-service="other">
          <span class="shot"><span>Ask for<br>a demo</span></span>
          <h3>See one working</h3>
          <p class="sub">Any product, on a call or at our office</p>
        </a>
      </div>
    </div>
  </section>

  <!-- ══════════ 6 · CLIENTS ══════════ -->
  <section class="band on-paper" id="clients">
    <div class="shell">
      <div class="sec-head center narrow">
        <p class="eyebrow mid rise">Our clients</p>
        <h2 class="rise">Trusted by hotels, hospitals, schools and traders across the Kingdom.</h2>
        <div class="listings rise">
          <span class="listing"><b>900+</b><span>Active clients</span></span>
          <span class="listing"><b>965+</b><span>Projects completed</span></span>
        </div>
      </div>
    </div>

    <!-- two rows drifting in opposite directions; the script repeats each set
         until it covers the screen, then mirrors it so -50% loops seamlessly -->
    <div class="rail rise">
      <div class="marquee">
        <div class="track" data-loop>
{row_a}
        </div>
      </div>
      <div class="marquee">
        <div class="track back" data-loop>
{row_b}
        </div>
      </div>
    </div>
  </section>

  <!-- ══════════ 6b · THE SMS PLATFORM ══════════ -->
  <section class="band on-ice" id="platform">
    <div class="shell">
      <div class="split2">
        <div class="split2-text">
          <p class="eyebrow rise">Our platform &middot; Bulk SMS</p>
          <h2 class="rise">Every customer&rsquo;s phone, in one click.</h2>
          <p class="lede rise">Campaigns, OTPs and alerts from our own web-based gateway, <b class="plat">digital.connectify.mobi</b>.</p>
          <dl class="facts rise">
            <div><dt>Where</dt><dd>India and the Middle East, targeted by region, city or country</dd></div>
            <div><dt>Sender</dt><dd>Your own brand name as the sender ID</dd></div>
            <div><dt>Connect</dt><dd>An API into your applications or CRM</dd></div>
            <div><dt>Track</dt><dd>Delivery and campaign analytics in real time, with 24/7 support</dd></div>
          </dl>
          <div class="split2-cta rise">
            <a class="btn btn-cyan" href="#contact" data-service="bulk-sms-service">Start sending</a>
          </div>
        </div>
        <figure class="split2-shot rise">
          <img src="assets/img/s-sms.webp" width="990" height="619" loading="lazy"
               alt="A man in a suit framing an envelope icon between his hands, contact icons around it.">
        </figure>
      </div>
    </div>
  </section>

  <!-- ══════════ 7 · PROCESS ══════════ -->
  <section class="band on-paper2" id="process">
    <div class="shell">
      <div class="sec-head">
        <p class="eyebrow rise">How we work</p>
        <h2 class="rise">Every engagement runs the same way.</h2>
      </div>
      <div class="steps">
{steps(PROCESS)}
      </div>
    </div>
  </section>

  <!-- ══════════ CONTACT ══════════ -->
  <section class="band on-paper" id="contact">
    <div class="shell">
      <div class="sec-head center narrow">
        <p class="eyebrow mid rise">Get in touch</p>
        <h2 class="rise">Tell us what you are building. We will tell you how.</h2>
        <p class="lede rise">We are here to listen and to help. Call, write, or send the form and a member of the team will reply.</p>
      </div>

      <div class="contact-grid">
        <form class="form rise" id="enquiry" data-to="{EMAIL}" novalidate>
          <div class="field-row">
            <div class="field">
              <label for="q-name">Your name</label>
              <input id="q-name" name="name" type="text" autocomplete="name" placeholder="Faisal Al-Harbi" required>
            </div>
            <div class="field">
              <label for="q-company">Company or institution</label>
              <input id="q-company" name="company" type="text" autocomplete="organization" placeholder="Optional">
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label for="q-email">Email</label>
              <input id="q-email" name="email" type="email" autocomplete="email" placeholder="you@company.sa">
            </div>
            <div class="field">
              <label for="q-phone">Phone</label>
              <input id="q-phone" name="phone" type="tel" autocomplete="tel" placeholder="+966">
            </div>
          </div>
          <div class="field">
            <label for="q-service">What you need help with</label>
            <select id="q-service" name="service">
{options}
              <option data-slug="other" selected>Not sure yet</option>
            </select>
          </div>
          <div class="field">
            <label for="q-msg">Your question or brief</label>
            <textarea id="q-msg" name="message" rows="3" placeholder="What the business runs on today, and what you would like it to do"></textarea>
          </div>
          <div class="form-actions">
            <button class="btn btn-cyan" type="submit">Send enquiry</button>
            <a class="btn btn-line" href="{TEL}">Call us</a>
          </div>
          <p class="form-note" id="enquiry-note" aria-live="polite">
            Sending opens your email app with the enquiry written out, addressed to {EMAIL}.
            Nothing is stored on this page.
          </p>
        </form>

        <div class="where rise">
          <div class="map">
            <iframe src="{map_src}"
              title="Map showing {LEGAL} on Prince Nayef Street, Al Khobar"
              loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
          </div>
          <address>
            <b>{LEGAL}</b>
            {addr}
          </address>
          <div class="reach-lines">
            <a href="{TEL}">{ICON_PHONE} {PHONE_SHOW}</a>
            <a href="{MAILTO}">{ICON_MAIL} {EMAIL}</a>
          </div>
          <a class="link" href="{map_link}" target="_blank" rel="noopener">Open in Google Maps {ARROW}</a>
        </div>
      </div>
    </div>
  </section>
</main>

<footer class="site-foot">
  <div class="shell">
    <div class="foot-grid">
      <div class="foot-brand">
        <a href="#top" aria-label="{BRAND}, back to top">
          <img class="logo" src="assets/logo-light.svg" width="685" height="128" alt="{LEGAL}">
        </a>
        <p>Innovation is not just a goal at Cyan; it is the principle that drives our growth.</p>
        <address>
          {LEGAL}<br>
          {"<br>".join(ADDRESS_LINES)}
        </address>
        <div class="foot-reach">
          <a href="{TEL}">{PHONE_SHOW}</a>
          <a href="{MAILTO}">{EMAIL}</a>
        </div>
      </div>
      <div>
        <h2>Services</h2>
        <ul>
{foot_svc}
        </ul>
      </div>
      <div>
        <h2>Company</h2>
        <ul>
          <li><a href="#about">About us</a></li>
          <li><a href="#products">Products</a></li>
          <li><a href="#clients">Our clients</a></li>
          <li><a href="#platform">SMS platform</a></li>
          <li><a href="#process">How we work</a></li>
          <li><a href="#contact">Contact us</a></li>
        </ul>
      </div>
    </div>

    <div class="foot-rule">
      <span>&copy; 2026 {LEGAL} All rights reserved.</span>
      <span>Hero image: Rostislav Uzunov on <a href="https://unsplash.com/photos/a-blue-and-green-light-shines-in-the-dark-B6AOQPcd7fQ" target="_blank" rel="noopener">Unsplash</a></span>
    </div>
  </div>
</footer>

<a class="float" href="#contact" aria-label="Get a quote">
  {ICON_CHAT}
  <span>Get a quote</span>
</a>

<script src="assets/site.js" defer></script>
</body>
</html>
"""
    (SITE / "index.html").write_text(doc, encoding="utf-8")
    (SITE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <url><loc>{BASE}/</loc></url>\n</urlset>\n", encoding="utf-8")
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
    print("site/index.html", len(doc) // 1024, "KB")


if __name__ == "__main__":
    build()
