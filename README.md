# Cyan Technology: home page redesign

A one-page redesign of cyangits.com (Cyan Technology for IT Systems Co.,
Al Khobar). The copy, counters, products, client logos and photography are
Cyan's own, taken from the live WordPress site on 23 Sep 2026.

The layout follows the Avadhuta site in `../avadhutayoga` as a design
reference. Avadhuta itself was only read, never changed. What carries over:
a fixed light bar, a full-height photograph as the hero's ground, small
tracked eyebrows over light serif headings, ruled white cards, a spine
section, drifting logo rows, an underlined form beside a map, and a deep
footer. The palette, type and content are Cyan's.

## Run it

    python serve.py              http://127.0.0.1:8106   (launch config: cyangits)

## Mobile

Checked at 320, 375, 768 and 1440 px with no horizontal overflow. On phones
the hero scrim becomes a full wash, because the shape stands directly behind
the copy there. The hero counters become a row of three, products sit two
across, and the footer puts the brand block full width above the two lists.

## Hosting

Vercel, connected to github.com/EJ1307/cyangits-redesign. Every push to
`main` deploys. There is no build step on Vercel: `vercel.json` points it
straight at `site/`, which is the finished page. So rebuild locally first,
then commit `site/` with the change:

    python tools/build.py
    git add -A && git commit -m "..." && git push origin main

`raw/` (about 30 MB of original downloads) is git-ignored, so
`prepare_assets.py` only runs on this machine.

## Rebuild

    python tools/prepare_assets.py   raw/ -> site/assets (images, logos)
    python tools/build.py            content.py -> site/index.html

`site/index.html` is generated, so edit `tools/content.py` (the words) or
`tools/build.py` (the markup), not the HTML. `site/` is the deployable folder.

## Section flow

    1  Hero            one still photograph, the line, three counters
    2  About           the team photo, the company, mission and vision, four counters
    3  Services        eleven numbered cards plus an "ask" card, three rows of four
    4  Why Cyan        the spine: three promises while building, three once live
    5  Products        eleven product logos plus an "ask for a demo" tile
    6  Clients         two rows of twenty logos, drifting in opposite directions
    6b SMS platform    digital.connectify.mobi, four facts, one picture
    7  How we work     the three-step process
       Contact         enquiry form, map, address, phone, email
       Footer

## Colour and type

Cyan `#3AC2D4` is sampled from the logo. It is 2.1:1 on white, so it only
ever fills buttons and markers, and sits under dark ink (`#06222A`, 7.75:1).
Anything small that has to be read in an accent colour uses teal `#0A6E7E`
(5.6:1 on the paper ground). The grounds are a cool paper, `#F6F9F9`, and
an ice band `#DCF1F4` at the middle of the page. All tokens and their
contrast ratios are at the top of `site/assets/site.css`.

The page is single-theme on purpose. It does not follow the OS dark mode.

Newsreader (light, variable) carries the headings. Outfit carries everything
else.

## Images

- The old service banners had the service name burned into the left half.
  Only the SMS one is used, cropped to its right half.
- The product logo JPEGs sat on off-white grounds that showed as grey boxes
  inside white cards. `prepare_assets.py` whitens anything lighter than 236.
- Every client logo came with a 2 px grey frame baked in, which is trimmed.
  `raw/clients/` holds all 101. Only the 40 named in `ROW_A` / `ROW_B` in
  `content.py` are exported.
- The hero is a glowing teal polyhedron by Rostislav Uzunov
  (unsplash.com/photos/B6AOQPcd7fQ), free for commercial use under the
  Unsplash License. Credit is given in the footer anyway. The right 26% of
  the frame is cropped off so the shape sits clear of the headline. It
  replaced a Riyadh skyline (Saif Al-Dhaher), which replaced the old site's
  three slides (a phone with chat bubbles, an API graphic, and an
  AI-generated hooded figure at a bank of monitors).

## The contact form

There is no backend. **Send enquiry** writes the enquiry into an email to
marketing@cyangits.com and opens it in the visitor's mail app. Nothing is
stored. Buttons with `data-service` (Start sending, Ask for a demo) preselect
the matching service in the dropdown. For inbox delivery without a mail app,
point the submit handler in `site.js` at Formspree or a small endpoint. The
fields already have `name` attributes.

The map uses the keyless `maps.google.com/maps?q=…&output=embed` form. It
works, but that endpoint is undocumented. For production, move to the Maps
Embed API with a key.

## Before this goes live

- **Counters.** 900+ clients, 965+ projects, 15+ years and 150+ team are
  the old site's own numbers. Confirm them.
- **Product one-liners.** Six of them are stated on the product artwork
  (Real World, HR & Payroll, CyanSoft, Smartshop, Traco, Glitz). The others
  were inferred from the logo alone (EduCyan "Education", MediCyan
  "Healthcare", Smart Wheels and Auto Smart "Automotive", Cyan Media "Media
  and design"). Smart Wheels and Auto Smart currently say the same thing.
- **The "Why Cyan" spine** rephrases the old site's scattered claims (work
  process, data protection, IT optimisation, third-party maintenance) into
  six promises. The wording is new and needs sign-off.
- **Client names in alt text** were read off the logos. Twelve emblem-only
  logos have a generic alt. Check the names.
- **"G Suite" is now Google Workspace.** The card says Google Workspace &
  Microsoft 365.
- **Social links were left out.** The old site's links went to bare
  facebook.com, instagram.com and so on. Add the real profiles to the footer.
- **Arabic.** The old site had an `/ar/` version. This redesign is English
  only.
- **Two email addresses.** The old site listed info@ in its top bar and
  marketing@ everywhere else. The form uses marketing@.
- **Sub-pages were not rebuilt.** Only the home page was asked for. The old
  service, about, products, clients, careers and contact URLs are not in
  `site/`. If this replaces WordPress, redirect those URLs to the matching
  `#section`, or keep them live.
