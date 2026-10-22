"""Builds the Wohletz Roofing & Construction static site into ./public. Run: python3 build.py"""
import json, pathlib

BASE = pathlib.Path(__file__).parent
ROOT = BASE / "public"
SITE = "https://wohletzroofingandconstruction.com"
NAME = "Wohletz Roofing & Construction"
PHONE = "(580) 716-0113"
PHONE_TEL = "+15807160113"
EMAIL = "info@wohletzroofingandconstruction.com"
FORM_TO = "info@wohletzroofingandconstruction.com"   # FormSubmit primary recipient
FORM_CC = "wohletztyler711@gmail.com"                # copy of every quote request
STREET, CITY, REGION, ZIP = "1531 Stangeland Rd", "Ponca City", "OK", "74604"
LICENSE = "80000665"
HOURS = "Mon to Sat, 8am to 5pm"
FACEBOOK = "https://www.facebook.com/WohletzRoofingandConstruction"
GMB = "https://www.google.com/maps/place/?cid=7321191553355990461"
MAP_EMBED = ("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3793.7024561813605!2d-96.984405!3d36.717670999999996!2m3!1f0!2f0!3f0"
             "!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87b0f51e6ca72883%3A0x659a18edae5fc5bd!2sWohletz%20Roofing%20%26%20Construction!5e1!3m2!1sen!2sus!4v1762207207903!5m2!1sen!2sus")
TOWNS = ["Ponca City", "Blackwell", "Tonkawa", "Newkirk", "Kaw City", "McCord", "Fairfax", "Shidler"]
YEAR_FOUNDED = 1994
GA4 = "G-EKZNGQFR8Z"  # Google Analytics 4 property carried over from the GHL site

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">')

ORG = {
    "@context": "https://schema.org",
    "@type": "RoofingContractor",
    "@id": SITE + "/#business",
    "name": NAME,
    "legalName": "Wohletz Roofing & Construction LLC",
    "url": SITE + "/",
    "description": "Locally owned roofing contractor and steel building builder in Ponca City, Oklahoma, serving North Central Oklahoma since 1994. Roof replacement, roof repair, storm damage, metal and commercial roofing, plus custom steel shops, barns, garages and storage buildings.",
    "telephone": PHONE_TEL,
    "email": EMAIL,
    "foundingDate": str(YEAR_FOUNDED),
    "priceRange": "$$",
    "address": {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": CITY, "addressRegion": REGION, "postalCode": ZIP, "addressCountry": "US"},
    "geo": {"@type": "GeoCoordinates", "latitude": 36.717671, "longitude": -96.984405},
    "hasMap": GMB,
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                   "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                                   "opens": "08:00", "closes": "17:00"}],
    "areaServed": [{"@type": "City", "name": t + ", OK"} for t in TOWNS],
    "logo": {"@type": "ImageObject", "url": SITE + "/img/wohletz-roofing-construction-logo.png", "width": 500, "height": 300},
    "image": [SITE + "/img/wohletz-roofing-ponca-city-share.jpg", SITE + "/img/roofer-installing-shingles-ponca-city-ok.webp"],
    "sameAs": [FACEBOOK, GMB],
    "founder": {"@type": "Person", "@id": SITE + "/#justin", "name": "Justin Wohletz", "jobTitle": "Owner", "url": SITE + "/about/"},
    "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "license", "name": "Oklahoma Roofing Contractor License #" + LICENSE},
    "knowsAbout": ["Roof replacement", "Roof repair", "Storm and hail damage repair", "Metal roofing", "Commercial roofing", "Steel building construction"],
}
WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": NAME, "publisher": {"@id": SITE + "/#business"}}

OG_DEFAULT = "/img/wohletz-roofing-ponca-city-share.jpg"

NAV = [("/roofing/", "Roofing"), ("/roof-repair/", "Roof Repair"), ("/steel-buildings/", "Steel Buildings"), ("/about/", "About"), ("/contact-us/", "Contact")]

ICO = {
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
 "roof": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12 12 3l10 9"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/></svg>',
 "storm": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17.5 17H7a5 5 0 1 1 1.1-9.9A6 6 0 0 1 19.6 9 4 4 0 0 1 17.5 17z"/><path d="m12 13-2 4h4l-2 4"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
 "metal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 20V9l9-6 9 6v11"/><path d="M7 20v-9M11 20v-9M15 20v-9M19 20v-9"/></svg>',
 "building": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 21h20"/><path d="M4 21V10l8-5 8 5v11"/><rect x="8" y="13" width="8" height="8"/><path d="M8 16h8M8 19h8"/></svg>',
 "clipboard": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="4" width="14" height="18" rx="2"/><path d="M9 4V2h6v2M9 11h6M9 15h6"/></svg>',
 "flat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="8" width="18" height="12"/><path d="M2 8h20M7 12h3M14 12h3M7 16h3M14 16h3"/></svg>',
 "drop": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.7s6 6.4 6 11a6 6 0 0 1-12 0c0-4.6 6-11 6-11z"/></svg>',
 "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
 "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
 "broom": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m14 4 6-2-2 6"/><path d="M19 3 9 13"/><path d="M5 13h8l-1 9H6z"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
}
FB_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8V6c0-.9.6-1 1-1h2.5V1.1L14 1C10.6 1 10 3.5 10 5.2V8H7.5v4H10v11h4V12h3.1l.4-4z"/></svg>'
G_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.6 12.2c0-.7-.1-1.4-.2-2H12v3.9h5.4a4.6 4.6 0 0 1-2 3v2.5h3.2c1.9-1.7 3-4.3 3-7.4z"/><path d="M12 22c2.7 0 5-.9 6.6-2.4l-3.2-2.5c-.9.6-2 1-3.4 1-2.6 0-4.8-1.8-5.6-4.1H3.1v2.6A10 10 0 0 0 12 22z"/><path d="M6.4 14a6 6 0 0 1 0-3.9V7.5H3.1a10 10 0 0 0 0 9z"/><path d="M12 6c1.5 0 2.8.5 3.8 1.5l2.9-2.9A10 10 0 0 0 3.1 7.5l3.3 2.6C7.2 7.8 9.4 6 12 6z"/></svg>'


def crumbs_schema(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (p, n) in enumerate(trail)]}


def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def service_schema(name, stype, desc, path):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "serviceType": stype, "description": desc,
            "url": SITE + path, "provider": {"@id": SITE + "/#business"},
            "areaServed": [{"@type": "City", "name": t + ", OK"} for t in TOWNS]}


def head(title, desc, path, schema=(), og_image=OG_DEFAULT, og_alt="Wohletz Roofing & Construction, roofing contractor and steel building builder in Ponca City, Oklahoma", noindex=False):
    schemas = [ORG, WEBSITE, *schema]
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, separators=(",", ":"))}</script>' for s in schemas)
    nav = "".join(f'<a href="{p}"{" aria-current=\"page\"" if p == path else ""}>{n}</a>' for p, n in NAV)
    robots = '<meta name="robots" content="noindex, follow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{SITE}{path}">
<meta name="author" content="Justin Wohletz">
<meta property="og:type" content="website"><meta property="og:site_name" content="{NAME}"><meta property="og:locale" content="en_US">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}{og_image}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{og_alt}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{SITE}{og_image}">
<meta name="theme-color" content="#d63a2a">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/favicon-32x32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
{FONTS}
<link rel="stylesheet" href="/styles.css">
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","{GA4}");</script>
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="container">
  <div class="hide-sm"><span>Serving North Central Oklahoma since {YEAR_FOUNDED}</span><span>OK License #{LICENSE}</span></div>
  <div><span class="hide-sm">{HOURS}</span><span><a href="tel:{PHONE_TEL}">Call {PHONE}</a></span></div>
</div></div>
<header class="site-header"><div class="container">
  <a class="logo" href="/" aria-label="{NAME} home"><img src="/img/wohletz-logo-transparent.webp" width="375" height="225" alt="Wohletz Roofing and Construction logo, Ponca City OK, since 1994"></a>
  <button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="nav">{ICO["menu"]}</button>
  <nav class="nav" id="nav" aria-label="Main">
    {nav}
    <a class="btn" href="/contact-us/#quote">Free Estimate</a>
  </nav>
</div></header>
"""


FOOT = f"""<footer class="site-footer"><div class="container">
  <div class="cols">
    <div>
      <a class="flogo" href="/"><img src="/img/wohletz-roofing-construction-logo.webp" width="500" height="300" alt="Wohletz Roofing and Construction logo" loading="lazy"></a>
      <p style="margin-top:14px;max-width:40ch">Quality and craftsmanship since {YEAR_FOUNDED}. Roofing and steel buildings for homes, farms and businesses across North Central Oklahoma.</p>
      <p style="margin-top:8px">Oklahoma Roofing License #{LICENSE}</p>
      <div class="social"><a href="{FACEBOOK}" aria-label="Wohletz Roofing on Facebook" rel="noopener">{FB_SVG}</a><a href="{GMB}" aria-label="Wohletz Roofing on Google Maps" rel="noopener">{G_SVG}</a></div>
    </div>
    <div><h3>Roofing</h3><ul>
      <li><a href="/roofing/">Roofing Services</a></li>
      <li><a href="/roofing/#replacement">Roof Replacement</a></li>
      <li><a href="/roof-repair/">Roof Repair</a></li>
      <li><a href="/roof-repair/#storm">Storm &amp; Hail Damage</a></li>
      <li><a href="/roofing/#metal">Metal Roofing</a></li>
      <li><a href="/roofing/#commercial">Commercial Roofing</a></li>
    </ul></div>
    <div><h3>Steel Buildings</h3><ul>
      <li><a href="/steel-buildings/">Steel Buildings</a></li>
      <li><a href="/steel-buildings/#shops">Metal Shop Buildings</a></li>
      <li><a href="/steel-buildings/#equipment">Equipment Barns</a></li>
      <li><a href="/steel-buildings/#garages">Steel Garages</a></li>
      <li><a href="/steel-buildings/#storage">Storage Buildings</a></li>
      <li><a href="/steel-buildings/#two-lakes">Two Lakes Storage Project</a></li>
    </ul></div>
    <div><h3>Contact</h3><ul>
      <li><a href="tel:{PHONE_TEL}"><b>{PHONE}</b></a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a href="{GMB}" rel="noopener">{STREET}<br>{CITY}, {REGION} {ZIP}</a></li>
      <li>{HOURS}<br>Sunday closed</li>
      <li><a href="/about/">About Us</a> &middot; <a href="/service-area/">Service Area</a></li>
    </ul></div>
  </div>
  <div class="bottom">
    <span>&copy; 2026 {NAME}. All rights reserved. &middot; <a href="/privacy-policy/">Privacy Policy</a> &middot; <a href="/terms/">Terms</a></span>
    <span>Website by <a href="https://toddhayes.com" rel="noopener">Hayes Digital Marketing</a></span>
  </div>
</div></footer>
<div class="callbar"><a href="tel:{PHONE_TEL}">{ICO["phone"]} Call Now</a><a href="/contact-us/#quote">Free Estimate</a></div>
<script>
(function(){{var b=document.querySelector(".menu-btn"),n=document.getElementById("nav");if(b)b.addEventListener("click",function(){{var o=n.classList.toggle("open");b.setAttribute("aria-expanded",o)}});
document.querySelectorAll(".next-url").forEach(function(i){{i.value=location.origin+"/thank-you/"}});
document.querySelectorAll(".page-url").forEach(function(i){{i.value=location.href}});
if(location.pathname==="/thank-you/"&&window.gtag)gtag("event","generate_lead");}})();
</script>
</body>
</html>
"""


SERVICES = ["Roof repair", "Roof replacement", "Storm or hail damage inspection", "Metal roofing", "Commercial or flat roofing", "Steel building quote", "Something else"]


def form(heading="Get Your Free Estimate", sub="Tell us a little about the job. We'll get back to you quickly, usually the same business day.", preselect=None, fid="q"):
    opts = "".join(f'<option{" selected" if s == preselect else ""}>{s}</option>' for s in SERVICES)
    return f"""<div class="form-card" id="quote">
  <h2>{heading}</h2>
  <p class="sub">{sub}</p>
  <form action="https://formsubmit.co/{FORM_TO}" method="POST">
    <input type="hidden" name="_subject" value="New quote request from wohletzroofingandconstruction.com">
    <input type="hidden" name="_cc" value="{FORM_CC}">
    <input type="hidden" name="_next" value="{SITE}/thank-you/" class="next-url">
    <input type="hidden" name="_template" value="table">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="Page" value="" class="page-url">
    <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
    <div class="row">
      <div><label for="{fid}-name">Name</label><input id="{fid}-name" name="Name" required autocomplete="name"></div>
      <div><label for="{fid}-phone">Phone</label><input id="{fid}-phone" name="Phone" type="tel" required autocomplete="tel"></div>
    </div>
    <div class="row">
      <div><label for="{fid}-email">Email</label><input id="{fid}-email" name="email" type="email" required autocomplete="email"></div>
      <div><label for="{fid}-town">Town or address</label><input id="{fid}-town" name="Location" autocomplete="street-address" placeholder="Ponca City"></div>
    </div>
    <div class="row">
      <div><label for="{fid}-svc">What do you need?</label><select id="{fid}-svc" name="Service">{opts}</select></div>
      <div><label for="{fid}-type">Property type</label><select id="{fid}-type" name="Property type"><option>Residential</option><option>Commercial</option><option>Farm or ranch</option></select></div>
    </div>
    <label for="{fid}-msg">Anything we should know? (optional)</label>
    <textarea id="{fid}-msg" name="Message" placeholder="Leak over the kitchen, hail last week, 40x60 shop with two overhead doors..."></textarea>
    <button class="btn" type="submit">Request My Free Estimate</button>
    <p class="or">Rather talk to a person? Call <a href="tel:{PHONE_TEL}">{PHONE}</a></p>
  </form>
</div>"""


def trust_strip():
    return f"""<div class="trust"><div class="container">
  <div>{ICO["calendar"]}<p><b>Since {YEAR_FOUNDED}</b><span>Over 30 years of local work</span></p></div>
  <div>{ICO["shield"]}<p><b>Licensed</b><span>Oklahoma License #{LICENSE}</span></p></div>
  <div>{ICO["user"]}<p><b>Owner-Led</b><span>Justin oversees every project</span></p></div>
  <div>{ICO["clipboard"]}<p><b>Free Estimates</b><span>Honest pricing, no pressure</span></p></div>
</div></div>"""


def hero(h1, small, lead, bullets, img, img_alt, form_html, eyebrow, crumbs=None, page=False):
    cr = ""
    if crumbs:
        cr = '<p class="crumbs">' + " / ".join(f'<a href="{p}">{n}</a>' for p, n in crumbs[:-1]) + f" / {crumbs[-1][1]}</p>"
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f"""<section class="hero{' page-hero' if page else ''}">
  <img class="bg" src="/img/{img}.webp" alt="{img_alt}" width="1350" height="675" fetchpriority="high">
  <div class="container hero-grid">
    <div>
      {cr}
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}<small>{small}</small></h1>
      <p class="lead">{lead}</p>
      <ul class="checks">{lis}</ul>
      <div class="hero-ctas"><a class="btn" href="tel:{PHONE_TEL}">{ICO["phone"]} Call {PHONE}</a></div>
    </div>
    {form_html}
  </div>
</section>"""


def faq_block(items, eyebrow="Questions", heading="Frequently asked questions", lead=""):
    det = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)
    lp = f'<p class="lead">{lead}</p>' if lead else ""
    return f"""<section class="alt"><div class="container grid-2" style="align-items:start">
  <div><span class="eyebrow">{eyebrow}</span><h2>{heading}</h2>{lp}
    <p style="margin-top:20px">Still have a question? Give us a call at <a href="tel:{PHONE_TEL}"><b>{PHONE}</b></a>. You'll talk to a real person here in Ponca City.</p></div>
  <div class="faq">{det}</div>
</div></section>"""


def cta_band(h="Ready to get started?", p="Whether it's a leak that can't wait or a shop you've been dreaming about for years, we'd love to take a look. Estimates are always free."):
    return f"""<section class="cta-band"><div class="container">
  <h2>{h}</h2>
  <p>{p}</p>
  <div class="btns"><a class="btn" href="tel:{PHONE_TEL}">{ICO["phone"]} Call {PHONE}</a><a class="btn ghost" href="/contact-us/#quote">Request a Free Estimate</a></div>
</div></section>"""


def map_section():
    towns = "".join(f"<li>{t}</li>" for t in TOWNS)
    return f"""<section class="dark"><div class="container grid-2">
  <div>
    <span class="eyebrow">Where we work</span>
    <h2>Proudly serving North Central Oklahoma</h2>
    <p class="lead">We're based right here in Ponca City, so we're never far away. We also work in the towns and rural areas around us.</p>
    <ul class="towns">{towns}</ul>
    <p style="margin-top:20px">Don't see your town? Call us anyway. If it's a good fit, we'll make the drive. <a href="/service-area/" style="color:#fff;font-weight:700">See our service area</a></p>
  </div>
  <div class="map"><iframe src="{MAP_EMBED}" title="Map to {NAME}, {STREET}, {CITY}, {REGION}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</div></section>"""


QUOTES = [
    ("Justin Wohletz did a tricky one for us 30 years ago on our old farmhouse.", "Local homeowner"),
    ("Price was good, workers did great cleanup. I know his family personally.", "Ponca City customer"),
]


def testimonials():
    q = "".join(f'<div class="quote"><p>{t}</p><cite>{c}</cite></div>' for t, c in QUOTES)
    return f"""<section><div class="container">
  <div class="section-head center"><span class="eyebrow">What neighbors say</span><h2>Trusted for generations of roofs</h2>
  <p class="lead">Some of our customers have known us for decades. That's the kind of reputation you only get by doing the job right the first time.</p></div>
  <div class="grid-2" style="align-items:stretch">{q}</div>
  <p style="text-align:center;margin-top:26px"><a class="btn dark" href="{GMB}" rel="noopener">Read our Google reviews</a></p>
</div></section>"""


def img(name, alt, w, h, cls="", lazy=True):
    return f'<img src="/img/{name}.webp" alt="{alt}" width="{w}" height="{h}"{" loading=\"lazy\"" if lazy else ""}{f" class={cls!r}" if cls else ""}>'


def write(path, html):
    assert "—" not in html, f"em dash found in {path}"
    out = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    if path.endswith(".html"):
        out = ROOT / path.strip("/")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


# ======================= HOME =======================
HOME_FAQ = [
    ("Do you offer free estimates?", "Yes. Roof inspections and estimates are free, and so are steel building quotes. We'll come look, tell you what we see, and give you an honest price. No pressure."),
    ("Can you help with my insurance claim after a hail storm?", "Yes. We inspect the roof, document the damage with photos, and work with your adjuster so nothing gets missed. If your roof doesn't need replacing, we'll tell you that too."),
    ("Are you licensed?", f"Yes. Wohletz Roofing &amp; Construction is a licensed Oklahoma roofing contractor, license #{LICENSE}."),
    ("What kinds of roofs do you install?", "Asphalt and composite shingles, metal roofing, and flat or low-slope commercial systems like membrane roofs. We handle homes, shops, barns, and commercial buildings."),
    ("What size steel buildings do you build?", "Just about anything. Single-car garages, big multi-bay shops, equipment barns, covered RV and boat storage, and full self-storage facilities. If you can dream it, we can build it."),
    ("What areas do you serve?", "Ponca City and the surrounding North Central Oklahoma area, including Blackwell, Tonkawa, Newkirk, Kaw City, McCord, Fairfax and Shidler."),
]

home = head("Roofing Contractor in Ponca City, OK | Wohletz Roofing &amp; Construction",
            "Roofing contractor in Ponca City, OK since 1994. Roof replacement, roof repair, hail and storm damage, metal roofing and custom steel buildings. Free estimates: (580) 716-0113.",
            "/", [faq_schema(HOME_FAQ)]) + f"""
<main id="main">
{hero("Roofing Contractor in Ponca City, OK", "Roofs &amp; steel buildings, built right since 1994",
      "When there's water coming through the ceiling, or a hail storm just rolled through, you want someone local who picks up the phone and shows up. That's us.",
      ["Roof repair, replacement and storm damage", "Custom steel shops, barns, garages and storage", "Owner Justin Wohletz oversees every job", "Free estimates and honest answers"],
      "roofer-installing-shingles-ponca-city-ok", "Wohletz roofing crew installing new asphalt shingles on a home in Ponca City, Oklahoma",
      form(fid="home"), "Locally owned &middot; Ponca City, Oklahoma")}
{trust_strip()}

<section><div class="container">
  <div class="section-head center"><span class="eyebrow">What we do</span><h2>Two trades. One local crew you can trust.</h2>
  <p class="lead">Most companies do one or the other. We've spent over 30 years doing both, so we know roofs, steel and Oklahoma weather inside and out.</p></div>
  <div class="grid-2" style="align-items:stretch">
    <a class="division" href="/roofing/">{img("new-construction-roof-install-ponca-city-ok", "New roof installed on a home under construction in Ponca City", 1400, 1050)}
      <div class="txt"><h3>Roofing</h3><p>Repairs, full replacements, storm and hail damage, metal roofs and commercial flat roofs for homes and businesses.</p><span class="more">Roofing services</span></div></a>
    <a class="division" href="/steel-buildings/">{img("metal-shop-building-overhead-doors", "Steel shop building with tall overhead doors built by Wohletz Construction", 1024, 768)}
      <div class="txt"><h3>Steel Buildings</h3><p>Shops, equipment barns, garages, covered storage and self-storage facilities, designed and built start to finish.</p><span class="more">Steel buildings</span></div></a>
  </div>
</div></section>

<section class="alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Roofing services</span><h2>Everything your roof needs, under one roof</h2>
  <p class="lead">From a few missing shingles to a whole new roof, we'll tell you straight what it needs... and what it doesn't.</p></div>
  <div class="grid-3">
    <div class="card"><div class="ico">{ICO["roof"]}</div><h3>Roof Replacement</h3><p>Complete tear-offs and new roofs that add curb appeal and real protection for decades.</p><a class="more" href="/roofing/#replacement">Learn more</a></div>
    <div class="card"><div class="ico">{ICO["drop"]}</div><h3>Roof Repair</h3><p>Leaks, flashing, missing shingles and damaged decking fixed fast, before small problems get expensive.</p><a class="more" href="/roof-repair/">Learn more</a></div>
    <div class="card"><div class="ico">{ICO["storm"]}</div><h3>Storm &amp; Hail Damage</h3><p>Free inspections after the storm, photo documentation, and help working with your insurance adjuster.</p><a class="more" href="/roof-repair/#storm">Learn more</a></div>
    <div class="card"><div class="ico">{ICO["metal"]}</div><h3>Metal Roofing</h3><p>Tough, weather-resistant metal roofs for homes, shops and barns. Built for long-term protection.</p><a class="more" href="/roofing/#metal">Learn more</a></div>
    <div class="card"><div class="ico">{ICO["flat"]}</div><h3>Commercial Roofing</h3><p>Flat, low-slope and membrane roofs for businesses, warehouses and industrial buildings.</p><a class="more" href="/roofing/#commercial">Learn more</a></div>
    <div class="card"><div class="ico">{ICO["clipboard"]}</div><h3>Inspections</h3><p>Not sure what's going on up there? We'll climb up, take photos, and walk you through what we find.</p><a class="more" href="/contact-us/#quote">Book an inspection</a></div>
  </div>
</div></section>

<section><div class="container grid-2">
  <div class="photo-stack"><div class="photo">{img("new-asphalt-shingle-roof-ponca-city-ok", "Finished asphalt shingle roof with blue trim on a Ponca City home", 600, 399)}</div>
    <div class="badge"><b>30+</b>Years in Ponca City</div></div>
  <div>
    <span class="eyebrow">Why Wohletz</span>
    <h2>The kind of contractor you'd recommend to your mom</h2>
    <p>Let's be honest... roofing has a reputation. Storm chasers roll into town, knock on doors, and they're gone before the first leak shows up. We've been here since {YEAR_FOUNDED}, and we're not going anywhere.</p>
    <ul class="why">
      <li>{ICO["user"]}<div><b>Owner on the job</b>Justin Wohletz personally oversees every project. You'll always know who to call.</div></li>
      <li>{ICO["clipboard"]}<div><b>Honest estimates</b>Clear pricing up front, and we'll never sell you a roof you don't need.</div></li>
      <li>{ICO["broom"]}<div><b>Clean job sites</b>Customers notice how we leave the place. Nails, scraps and debris get picked up.</div></li>
      <li>{ICO["shield"]}<div><b>Licensed and local</b>Oklahoma license #{LICENSE}, with an office right here on Stangeland Road.</div></li>
    </ul>
  </div>
</div></section>

<section class="alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Steel buildings</span><h2>Steel buildings built for Oklahoma</h2>
  <p class="lead">Red iron framing, steel-clad walls, and doors sized for the way you actually work. Here's what we build most.</p></div>
  <div class="grid-3">
    <div class="img-card">{img("steel-equipment-storage-building-oklahoma", "Steel equipment storage building with green tractors parked inside", 770, 564)}<div class="body"><h3>Equipment Barns</h3><p>Keep tractors, combines and implements out of the weather and protect a big investment.</p></div></div>
    <div class="img-card">{img("metal-shop-building-overhead-doors", "Gray metal shop building with five tall overhead doors", 1024, 768)}<div class="body"><h3>Metal Shops</h3><p>Door sizes, height and layout designed around your work. A shop worth bragging about.</p></div></div>
    <div class="img-card">{img("steel-garage-building-multi-bay", "Three-bay steel garage with a classic red pickup inside", 1024, 724)}<div class="body"><h3>Steel Garages</h3><p>From a single door to rows of auto bays, built to fit your trucks, toys and tools.</p></div></div>
  </div>
  <p style="margin-top:28px"><a class="btn" href="/steel-buildings/">See all steel buildings</a></p>
</div></section>

<section><div class="container">
  <div class="feature">
    {img("two-lakes-storage-boat-rv-storage-ponca-city-ok", "Two Lakes Storage boat and RV storage building near Kaw Lake, built by Wohletz Construction", 800, 600)}
    <div class="body">
      <span class="eyebrow">Recent project</span>
      <h2>Two Lakes Storage</h2>
      <p>We recently finished Two Lakes Storage, a brand new 50 unit boat and RV storage facility at 5430 Lake Road, between Ponca City and Kaw Lake.</p>
      <p>Projects like this are where steel really shines. Low maintenance, long life, and a strong return on investment for the owner.</p>
      <p style="margin-top:20px"><a class="btn dark" href="/steel-buildings/#two-lakes">More about this project</a></p>
    </div>
  </div>
</div></section>

{testimonials()}

<section class="alt"><div class="container">
  <div class="section-head center"><span class="eyebrow">How it works</span><h2>Simple from first call to final cleanup</h2></div>
  <ol class="steps">
    <li><h3>Call or send a request</h3><p>Tell us what's going on. We'll set a time to come out that works for you.</p></li>
    <li><h3>Free inspection &amp; estimate</h3><p>We look everything over, take photos, and give you an honest, clear price.</p></li>
    <li><h3>We build it right</h3><p>Our crew does the work, Justin checks it, and we clean up before we leave.</p></li>
  </ol>
</div></section>

{map_section()}
{faq_block(HOME_FAQ)}
{cta_band()}
</main>
""" + FOOT
write("/", home)


# ======================= ROOFING =======================
ROOF_FAQ = [
    ("How do I know if I need a new roof or just a repair?", "It depends on the age of the roof, how widespread the damage is, and whether the decking underneath is still solid. We'll inspect it, show you photos, and give you an honest recommendation. If a repair will do the job, that's what we'll tell you."),
    ("What roofing materials do you work with?", "Asphalt and composite shingles, metal roofing, and flat or low-slope systems including membrane roofs for commercial buildings."),
    ("Do you handle insurance claims?", "Yes. After hail or wind damage we document everything and work with your insurance adjuster to make sure the claim covers what it should."),
    ("Do you work on commercial buildings?", "Yes. We roof businesses, shops, warehouses and industrial buildings, and we pay close attention to safety and building codes."),
    ("Do you clean up after the job?", "Always. Old shingles, nails and debris get hauled off, and we go over the yard before we leave."),
]
roof_svc = service_schema("Roofing Services in Ponca City, OK", "Roofing contractor",
                          "Residential and commercial roofing in Ponca City, OK: roof replacement, roof repair, storm and hail damage, metal roofing, flat and membrane roofs.", "/roofing/")
roofing = head("Roofing Company in Ponca City, OK | Roof Replacement &amp; Repair | Wohletz",
               "Roofing company in Ponca City, OK. Roof replacement, roof repair, metal roofing and commercial flat roofs from a local, licensed roofer since 1994. Free estimates.",
               "/roofing/", [roof_svc, crumbs_schema([("/", "Home"), ("/roofing/", "Roofing")]), faq_schema(ROOF_FAQ)]) + f"""
<main id="main">
{hero("Roofing Company in Ponca City, OK", "Residential &amp; commercial roofing since 1994",
      "Your roof is the one thing standing between your family and an Oklahoma storm. It deserves a local crew that does it right the first time.",
      ["Roof replacement and complete tear-offs", "Leak repair, flashing and decking", "Asphalt, metal and flat roofs", "Free inspections and insurance claim help"],
      "roofer-installing-shingles-ponca-city-ok", "Roofer using a nail gun to install shingles on a Ponca City roof",
      form("Get a Free Roofing Estimate", fid="roof", preselect="Roof replacement"), "Roofing services", [("/", "Home"), ("/roofing/", "Roofing")], page=True)}
{trust_strip()}

<section><div class="container grid-2">
  <div>
    <span class="eyebrow">Roofing you can rely on</span>
    <h2>We understand Oklahoma weather</h2>
    <p>Hail in the spring. Straight-line winds in the summer. Ice in the winter. Around here, a roof has to handle all of it, year after year.</p>
    <p>For over 30 years we've been building and fixing roofs across Ponca City and North Central Oklahoma. Whether you need a small repair or a full replacement, we have the tools and the experience to get it done right. And we'll explain everything in plain English, so you know exactly what you're paying for.</p>
    <ul class="list">
      <li>Roof replacement and tear-offs</li><li>Leak repair and storm damage</li><li>Asphalt and composite shingle roofs</li><li>Metal roofs for homes, shops and barns</li><li>Flat, low-slope and membrane roofs</li><li>Roof decking repair</li><li>Inspections and maintenance</li><li>Insurance claim help</li>
    </ul>
  </div>
  <div class="photo">{img("new-construction-roof-install-ponca-city-ok", "Newly shingled roof on a home addition in Ponca City, Oklahoma", 1400, 1050)}</div>
</div></section>

<section class="alt" id="replacement"><div class="container grid-2">
  <div class="photo">{img("new-asphalt-shingle-roof-ponca-city-ok", "New gray architectural shingle roof replacement on a home", 600, 399)}</div>
  <div>
    <span class="eyebrow">Roof replacement</span>
    <h2>A new roof, done once and done right</h2>
    <p>When a roof is past its prime, patching it over and over just throws good money after bad. A full replacement fixes the problem for good, and it's one of the best ways to boost curb appeal.</p>
    <p>We tear off the old roof down to the decking, replace any soft or rotted boards, then install new underlayment, flashing, vents and shingles. When we're done, we clean up like we were never there... except for the great-looking new roof.</p>
  </div>
</div></section>

<section><div class="container">
  <div class="section-head"><span class="eyebrow">Roof types</span><h2>The right roof for your building</h2></div>
  <div class="grid-3">
    <div class="card"><div class="ico">{ICO["roof"]}</div><h3>Asphalt Shingle Roofs</h3><p>Cost-effective, good looking and durable. The most popular choice for homes in Ponca City, with plenty of colors and styles to choose from.</p></div>
    <div class="card" id="metal"><div class="ico">{ICO["metal"]}</div><h3>Metal Roofing</h3><p>Durable and weather-resistant, with long-term protection and energy efficiency. A great fit for homes, shops, barns and outbuildings.</p></div>
    <div class="card" id="commercial"><div class="ico">{ICO["flat"]}</div><h3>Commercial &amp; Flat Roofs</h3><p>Membrane and low-slope systems that keep water out of businesses, warehouses and industrial buildings, built with safety and code in mind.</p></div>
  </div>
  <div class="table-wrap" style="margin-top:30px"><table class="compare">
    <thead><tr><th>Roof type</th><th>Best for</th><th>Why people choose it</th></tr></thead>
    <tbody>
      <tr><td><b>Asphalt shingles</b></td><td>Most homes</td><td>Lower upfront cost, classic look, lots of color options</td></tr>
      <tr><td><b>Metal</b></td><td>Homes, shops, barns</td><td>Long life, stands up to wind and weather, low maintenance</td></tr>
      <tr><td><b>Membrane / flat</b></td><td>Commercial and industrial</td><td>Watertight on low-slope roofs, handles large spans</td></tr>
    </tbody>
  </table></div>
</div></section>

<section class="alt"><div class="container grid-2">
  <div>
    <span class="eyebrow">Repairs &amp; storm damage</span>
    <h2>Got a leak? Hail damage? Call us first.</h2>
    <p>A small leak today can mean rotted decking, ruined drywall and mold a few months from now. We fix leaks, flashing, missing shingles and storm damage quickly, and we'll help you through the insurance process if a storm caused it.</p>
    <p style="margin-top:20px"><a class="btn" href="/roof-repair/">Roof repair &amp; storm damage</a></p>
  </div>
  <div class="card"><div class="ico">{ICO["storm"]}</div><h3>Signs your roof needs attention</h3>
    <ul class="list"><li>Water stains on ceilings or walls</li><li>Missing, curled or cracked shingles</li><li>Granules piling up in the gutters</li><li>Dents or bruises after a hail storm</li><li>Sagging spots or a soft feel underfoot</li><li>Daylight showing through the attic boards</li></ul>
  </div>
</div></section>

{testimonials()}
{faq_block(ROOF_FAQ, "Roofing questions", "Roofing questions we hear a lot")}
{cta_band("Schedule your free roof inspection", "We'll climb up, take photos, and give you an honest answer about what your roof needs. No pressure, no storm-chaser games.")}
</main>
""" + FOOT
write("/roofing/", roofing)


# ======================= ROOF REPAIR =======================
REP_FAQ = [
    ("How fast can you come look at my roof?", f"Call us at {PHONE} and we'll get you on the schedule as quickly as we can. After a big storm things get busy, so it helps to call early."),
    ("Will my insurance cover hail damage?", "Often it does, but every policy is different. We'll inspect the roof, document the damage with photos, and work with your adjuster. Your insurance company makes the final call on coverage."),
    ("Should I tarp my roof after a storm?", "If water is actively coming in, a temporary tarp can prevent a lot of interior damage. Please don't climb on a wet or damaged roof yourself. Call us and we'll help."),
    ("Can you repair just part of a roof?", "Yes. If the damage is limited and the rest of the roof is in good shape, a repair is usually the smart move. We'll tell you honestly which makes more sense."),
    ("Do you repair commercial roofs too?", "Yes. We repair flat, low-slope, membrane and metal roofs on commercial and industrial buildings."),
]
rep_svc = service_schema("Roof Repair and Storm Damage Repair in Ponca City, OK", "Roof repair",
                         "Roof leak repair, hail and wind damage repair, flashing and decking repair, and insurance claim help in Ponca City, OK.", "/roof-repair/")
repair = head("Roof Repair in Ponca City, OK | Hail &amp; Storm Damage | Wohletz Roofing",
              "Roof repair in Ponca City, OK. Leaks, hail and wind damage, flashing and decking fixed by a local licensed roofer. Free storm damage inspections and insurance help.",
              "/roof-repair/", [rep_svc, crumbs_schema([("/", "Home"), ("/roofing/", "Roofing"), ("/roof-repair/", "Roof Repair")]), faq_schema(REP_FAQ)]) + f"""
<main id="main">
{hero("Roof Repair in Ponca City, OK", "Leaks, hail &amp; storm damage fixed fast",
      "That drip in the ceiling has a way of ruining your whole week. Let's find where it's coming from and stop it, before it turns into a bigger bill.",
      ["Leak, flashing and shingle repair", "Free hail and wind damage inspections", "Photo documentation for your insurance", "Local crew, not out-of-town storm chasers"],
      "roofer-installing-shingles-ponca-city-ok", "Roofer repairing shingles on a storm damaged roof in Ponca City",
      form("Request a Roof Repair", "Tell us what you're seeing. We'll call you back to set up a time to take a look.", "Roof repair", "rep"),
      "Roof repair &amp; storm damage", [("/", "Home"), ("/roofing/", "Roofing"), ("/roof-repair/", "Roof Repair")], page=True)}
{trust_strip()}

<section><div class="container">
  <div class="section-head"><span class="eyebrow">Repair services</span><h2>Swift repairs that restore your roof's protection</h2>
  <p class="lead">Most roof problems start small. Catching them early is the cheapest roof work you'll ever pay for.</p></div>
  <div class="grid-3">
    <div class="card"><div class="ico">{ICO["drop"]}</div><h3>Leak Repair</h3><p>We track down where water is really getting in (it's not always right above the stain) and fix the source.</p></div>
    <div class="card"><div class="ico">{ICO["roof"]}</div><h3>Shingle Repair</h3><p>Missing, cracked or curled shingles replaced and matched as closely as possible to your existing roof.</p></div>
    <div class="card"><div class="ico">{ICO["shield"]}</div><h3>Flashing &amp; Vents</h3><p>Chimneys, pipe boots, skylights and valleys are the most common leak spots. We reseal and replace them right.</p></div>
    <div class="card"><div class="ico">{ICO["building"]}</div><h3>Decking Repair</h3><p>Soft, rotted or water-damaged roof boards replaced so your new shingles have a solid base.</p></div>
    <div class="card"><div class="ico">{ICO["flat"]}</div><h3>Commercial Roof Repair</h3><p>Flat, membrane and metal roof repairs for businesses, keeping water away from inventory and equipment.</p></div>
    <div class="card"><div class="ico">{ICO["clipboard"]}</div><h3>Roof Inspections</h3><p>Buying a home, or just not sure? We'll inspect the roof and give you an honest report with photos.</p></div>
  </div>
</div></section>

<section class="alt" id="storm"><div class="container grid-2">
  <div>
    <span class="eyebrow">Storm &amp; hail damage</span>
    <h2>After the storm, here's what to do</h2>
    <p>Oklahoma hail doesn't always leave obvious damage from the ground. Bruised shingles and cracked mats can turn into leaks months later, long after the claim window gets tight. A free inspection now gives you peace of mind.</p>
    <ol class="steps" style="grid-template-columns:1fr;margin-top:20px">
      <li><h3>Stay safe and stay off the roof</h3><p>If water is coming in, move valuables and catch the drip. Leave the climbing to us.</p></li>
      <li><h3>Call for a free inspection</h3><p>We check the shingles, vents, flashing, gutters and decking, and photograph everything we find.</p></li>
      <li><h3>We work with your adjuster</h3><p>We'll meet your insurance adjuster and make sure all the damage gets seen. Then we make the repair or replacement.</p></li>
    </ol>
  </div>
  <div class="photo">{img("new-construction-roof-install-ponca-city-ok", "Roof with new shingles installed after storm damage in North Central Oklahoma", 1400, 1050)}</div>
</div></section>

<section><div class="container grid-2">
  <div class="card"><div class="ico">{ICO["user"]}</div><h3>Watch out for storm chasers</h3>
    <p>After every big hail storm, out-of-state crews show up with a truck, a clipboard and a great deal. Some do fine work. Many are gone by the time a problem shows up.</p>
    <ul class="list"><li>Ask for a local address and phone number</li><li>Check for an Oklahoma roofing license</li><li>Never sign over your insurance check before work is done</li><li>Get a written estimate</li></ul>
  </div>
  <div>
    <span class="eyebrow">Local since {YEAR_FOUNDED}</span>
    <h2>We'll still be here next year</h2>
    <p>Our office is on Stangeland Road in Ponca City, and we've been answering the phone here for over 30 years. If something isn't right with our work, you know exactly where to find us.</p>
    <p>That's a promise a storm chaser can't make.</p>
  </div>
</div></section>

{faq_block(REP_FAQ, "Repair questions", "Roof repair questions")}
{cta_band("Don't let a small leak get bigger", "Call now or request a repair online. We'll get out to take a look as soon as we can.")}
</main>
""" + FOOT
write("/roof-repair/", repair)


# ======================= STEEL BUILDINGS =======================
STEEL_FAQ = [
    ("Do you handle the whole project?", "Yes. We provide complete design and build services: site prep, concrete foundations, red iron framing, steel-clad walls and roof, and doors. One crew, one point of contact."),
    ("Can I choose the size and door layout?", "Absolutely. Every building is built around how you'll use it, from building height and door sizes to walk-in doors, windows and auto bays."),
    ("Why choose steel over a wood pole barn?", "Steel won't rot, warp or attract termites, it stands up to Oklahoma wind and weather, and it needs very little maintenance. For long-term value it's hard to beat."),
    ("Do you build commercial storage facilities?", "Yes. We recently built Two Lakes Storage, a 50 unit boat and RV storage facility near Kaw Lake, and we build self-storage buildings of all sizes."),
    ("Can you add on to or retrofit an existing building?", "Yes. We do expansions and retrofits on existing metal buildings."),
]
steel_svc = service_schema("Steel Building Construction in Ponca City, OK", "Steel building construction",
                           "Design and build steel buildings in Ponca City, OK: metal shops, equipment barns, steel garages, covered RV and boat storage, self-storage facilities and custom metal buildings.", "/steel-buildings/")
two_lakes = {"@context": "https://schema.org", "@type": "CreativeWork", "name": "Two Lakes Storage, 50 unit boat and RV storage facility",
             "about": "Steel building construction project at 5430 Lake Road between Ponca City, OK and Kaw Lake",
             "creator": {"@id": SITE + "/#business"}, "image": SITE + "/img/two-lakes-storage-boat-rv-storage-ponca-city-ok.webp"}
STEEL_TYPES = [
    ("equipment", "steel-equipment-storage-building-oklahoma", "Steel equipment storage building with tractors inside, North Central Oklahoma", 770, 564,
     "Equipment Storage Buildings", "Your tractors, combines and other farm equipment are a massive investment. Protect them with a durable steel building with doors designed to handle your biggest machines."),
    ("shops", "metal-shop-building-overhead-doors", "Metal shop building with five open overhead doors", 1024, 768,
     "Metal Shop Buildings", "Durable, weather-resistant shops designed for your work. We'll plan the doors, height and amenities to make your shop something to brag about."),
    ("garages", "steel-garage-building-multi-bay", "Multi-bay steel garage building with overhead doors", 1024, 724,
     "Steel Garage Buildings", "From a single door to rows of big garage doors and auto bays, we can custom build your dream garage to fit your needs."),
    ("storage", "steel-self-storage-building", "Row of steel self-storage units with roll-up doors", 800, 600,
     "Metal Storage Buildings", "From backyard and business storage to large self-storage facilities. For low maintenance, long life and return on investment, nothing beats all-steel storage."),
    ("covered", "steel-covered-rv-boat-storage", "Steel covered storage building sheltering an RV, a boat and a tractor", 1024, 768,
     "Steel Covered Storage", "Covered storage for your RV, boat and toys, or for equipment and hay. Think of it as a giant carport for whatever you need to protect."),
    ("custom", "metal-garage-building-ponca-city-ok", "Custom metal building with a walk-in door and three overhead doors", 1024, 768,
     "Custom Metal Buildings", "If you can dream it, we can build it. Built with durable red iron beams and a steel-clad exterior for long-term strength."),
]
cards = "".join(f'<div class="img-card" id="{a}">{img(f, alt, w, h)}<div class="body"><h3>{t}</h3><p>{d}</p></div></div>' for a, f, alt, w, h, t, d in STEEL_TYPES)
steel = head("Steel Buildings in Ponca City, OK | Metal Shops, Barns &amp; Garages | Wohletz",
             "Steel buildings in Ponca City, OK. Custom metal shops, equipment barns, steel garages, covered RV storage and self-storage facilities. Design and build since 1994.",
             "/steel-buildings/", [steel_svc, two_lakes, crumbs_schema([("/", "Home"), ("/steel-buildings/", "Steel Buildings")]), faq_schema(STEEL_FAQ)]) + f"""
<main id="main">
{hero("Steel Buildings in Ponca City, OK", "Built tough. Built local. Built for you.",
      "You've been picturing that shop or barn for a while now. Let's build it the right way, with steel that'll still be standing strong for your grandkids.",
      ["Shops, barns, garages and storage buildings", "Complete design and build, start to finish", "Concrete foundations and site prep", "Red iron framing and steel-clad exteriors"],
      "steel-building-ponca-city-ok", "Two-tone steel building with overhead doors built by Wohletz in Ponca City, Oklahoma",
      form("Get a Free Steel Building Quote", "Tell us roughly what you have in mind: size, doors and how you'll use it.", "Steel building quote", "steel"),
      "Steel building construction", [("/", "Home"), ("/steel-buildings/", "Steel Buildings")], page=True)}
{trust_strip()}

<section><div class="container">
  <div class="section-head"><span class="eyebrow">What we build</span><h2>Steel buildings for every purpose</h2>
  <p class="lead">From garages to large commercial storage facilities, we provide complete design and build services. Every structure is planned around what you need it to do.</p></div>
  <div class="grid-3">{cards}</div>
</div></section>

<section class="alt"><div class="container grid-2">
  <div>
    <span class="eyebrow">Why steel?</span>
    <h2>The smart choice for strength and value</h2>
    <p>Wood rots. Termites eat it. Oklahoma wind loves to peel it apart. Steel just keeps going.</p>
    <ul class="why">
      <li>{ICO["shield"]}<div><b>Built to last</b>Red iron frames and steel panels stand up to wind, hail and time.</div></li>
      <li>{ICO["check"]}<div><b>Low maintenance</b>No rot, no warping, no termites. Less upkeep year after year.</div></li>
      <li>{ICO["building"]}<div><b>Flexible design</b>Wide clear spans and doors sized for whatever you're parking or working on.</div></li>
      <li>{ICO["clipboard"]}<div><b>Strong return</b>For storage facilities and businesses, steel delivers long-term value.</div></li>
    </ul>
  </div>
  <div class="card"><div class="ico">{ICO["building"]}</div><h3>Our steel building services</h3>
    <ul class="list"><li>Metal building design and construction</li><li>Garages, equipment barns and workshops</li><li>Commercial storage buildings and outbuildings</li><li>Farm and ranch steel structures</li><li>Covered RV, boat and hay storage</li><li>Concrete foundations and site preparation</li><li>Building retrofits and expansions</li></ul>
  </div>
</div></section>

<section id="two-lakes"><div class="container">
  <div class="feature">
    {img("two-lakes-storage-boat-rv-storage-ponca-city-ok", "Red and tan steel storage building at Two Lakes Storage near Kaw Lake, Oklahoma", 800, 600)}
    <div class="body">
      <span class="eyebrow">Featured project</span>
      <h2>Two Lakes Storage</h2>
      <p>We recently completed Two Lakes Storage, a new 50 unit boat and RV storage facility at 5430 Lake Road, between Ponca City and Kaw Lake.</p>
      <p>With Kaw Lake just up the road, folks needed a secure, covered place to keep their boats and campers. Steel was the obvious choice: tall doors, long life and very little upkeep for the owner.</p>
      <p style="margin-top:20px"><a class="btn" href="/contact-us/#quote">Plan your storage project</a></p>
    </div>
  </div>
</div></section>

<section class="alt"><div class="container">
  <div class="section-head center"><span class="eyebrow">How it works</span><h2>From idea to finished building</h2></div>
  <ol class="steps">
    <li><h3>Talk it through</h3><p>Tell us how you'll use the building. We'll help you nail down size, doors and features.</p></li>
    <li><h3>Get your quote</h3><p>We'll put together a clear, honest price for the building, foundation and site work.</p></li>
    <li><h3>We build it</h3><p>Site prep, concrete, framing, panels and doors, all handled by our crew with Justin overseeing.</p></li>
  </ol>
</div></section>

{faq_block(STEEL_FAQ, "Steel building questions", "Steel building questions")}
{cta_band("Let's build your steel building", "Shop, barn, garage or a whole storage facility. Call us or request a free quote, and let's talk about what you have in mind.")}
</main>
""" + FOOT
write("/steel-buildings/", steel)


# ======================= ABOUT =======================
about_page = {"@context": "https://schema.org", "@type": "AboutPage", "url": SITE + "/about/", "about": {"@id": SITE + "/#business"},
              "mainEntity": {"@type": "Person", "@id": SITE + "/#justin", "name": "Justin Wohletz", "jobTitle": "Owner",
                             "worksFor": {"@id": SITE + "/#business"}, "homeLocation": {"@type": "Place", "name": "Ponca City, OK"}}}
about = head("About Wohletz Roofing &amp; Construction | Ponca City Roofer Since 1994",
             "Meet Justin Wohletz and the team at Wohletz Roofing & Construction. Locally owned in Ponca City, OK since 1994, building roofs and steel buildings the right way.",
             "/about/", [about_page, crumbs_schema([("/", "Home"), ("/about/", "About")])]) + f"""
<main id="main">
<section class="hero page-hero">
  <img class="bg" src="/img/new-construction-roof-install-ponca-city-ok.webp" alt="Roof installed by Wohletz Roofing on a Ponca City home" width="1400" height="1050" fetchpriority="high">
  <div class="container">
    <p class="crumbs"><a href="/">Home</a> / About</p>
    <span class="eyebrow">About us</span>
    <h1>About Wohletz Roofing &amp; Construction<small>Family owned. Locally trusted. Quality driven.</small></h1>
    <p class="lead">We're more than a roofing company. We're your neighbors, and we take protecting your biggest investments personally.</p>
  </div>
</section>
{trust_strip()}

<section><div class="container grid-2">
  <div>
    <span class="eyebrow">Our story</span>
    <h2>A legacy of local craftsmanship</h2>
    <p>Wohletz Roofing &amp; Construction started in {YEAR_FOUNDED} with a simple goal: bring reliable, high-quality roofing and construction to Ponca City.</p>
    <p>More than 30 years later, that hasn't changed. Our reputation was built one roof and one building at a time, on honesty, hard work, and a job done right the first time. Some of our customers called us decades ago, and they still call us today.</p>
    <p>Today we specialize in two things: roofing for homes and businesses, and custom steel buildings for farms, shops and storage. Both are built for Oklahoma weather, and both get the same attention to detail.</p>
  </div>
  <div class="photo">{img("roofer-installing-shingles-ponca-city-ok", "Wohletz crew installing roof shingles in Ponca City", 1350, 675)}</div>
</div></section>

<section class="alt"><div class="container grid-2">
  <div class="card"><div class="ico">{ICO["user"]}</div><h3>Meet Justin Wohletz, Owner</h3>
    <p>Justin grew up in Ponca City and takes real pride in serving the community he calls home. He personally oversees every project, so every roof and every steel building meets his standards before we call it done.</p>
    <p>When you call Wohletz, you're not getting passed around a call center. You're working with the guy whose name is on the sign.</p>
  </div>
  <div>
    <span class="eyebrow">Our values</span>
    <h2>What sets us apart</h2>
    <ul class="why">
      <li>{ICO["calendar"]}<div><b>Experience</b>Over 30 years of roofing and construction in North Central Oklahoma.</div></li>
      <li>{ICO["clipboard"]}<div><b>Integrity</b>Honest communication, clear estimates, and follow-through.</div></li>
      <li>{ICO["shield"]}<div><b>Craftsmanship</b>Built to last, because we'll see your roof every time we drive by.</div></li>
      <li>{ICO["pin"]}<div><b>Community</b>Locally owned and proud to serve Ponca City and the towns around it.</div></li>
    </ul>
  </div>
</div></section>

{testimonials()}
{map_section()}
{cta_band("Let's talk about your project", "Roof, repair or steel building, we'd be glad to come take a look. Estimates are always free.")}
</main>
""" + FOOT
write("/about/", about)


# ======================= SERVICE AREA =======================
TOWN_NOTES = {
    "Ponca City": "Our home base. Our office is on Stangeland Road, so most Ponca City jobs are just minutes away.",
    "Blackwell": "Roof repairs, replacements and steel buildings for homes, farms and businesses in Blackwell and the surrounding Kay County area.",
    "Tonkawa": "Roofing and steel buildings for Tonkawa homeowners, farmers and businesses.",
    "Newkirk": "Serving Newkirk and the rural areas around it with roofing and steel building construction.",
    "Kaw City": "Roofing, covered storage and steel buildings near Kaw Lake, including boat and RV storage like our Two Lakes Storage project.",
    "McCord": "Roofing and steel buildings in McCord and the nearby Osage County area, right next door to Ponca City.",
    "Fairfax": "Roof repair, roof replacement and steel buildings for Fairfax and Osage County properties.",
    "Shidler": "Serving Shidler and rural Osage County with roofing and farm and ranch steel buildings.",
}
area_cards = "".join(f'<div class="card"><div class="ico">{ICO["pin"]}</div><h3>{t}, OK</h3><p>{TOWN_NOTES[t]}</p></div>' for t in TOWNS)
area = head("Roofing &amp; Steel Buildings Service Area | Ponca City, Blackwell, Tonkawa &amp; More",
            "Wohletz Roofing & Construction serves Ponca City, Blackwell, Tonkawa, Newkirk, Kaw City, McCord, Fairfax and Shidler, OK with roofing and steel buildings.",
            "/service-area/", [crumbs_schema([("/", "Home"), ("/service-area/", "Service Area")])]) + f"""
<main id="main">
<section class="hero page-hero">
  <img class="bg" src="/img/steel-equipment-storage-building-oklahoma.webp" alt="Steel equipment barn on an Oklahoma farm" width="770" height="564" fetchpriority="high">
  <div class="container">
    <p class="crumbs"><a href="/">Home</a> / Service Area</p>
    <span class="eyebrow">Service area</span>
    <h1>Roofing &amp; Steel Buildings Across North Central Oklahoma<small>Based in Ponca City since 1994</small></h1>
    <p class="lead">From town homes to farms out on the county roads, we're glad to make the drive.</p>
    <div class="hero-ctas"><a class="btn" href="tel:{PHONE_TEL}">{ICO["phone"]} Call {PHONE}</a><a class="btn ghost" href="/contact-us/#quote">Free Estimate</a></div>
  </div>
</section>
<section><div class="container">
  <div class="section-head"><span class="eyebrow">Towns we serve</span><h2>Where we work</h2>
  <p class="lead">Roof repair, roof replacement, storm damage and steel building construction in these communities and the rural areas in between.</p></div>
  <div class="grid-4">{area_cards}</div>
</div></section>
{map_section()}
{cta_band()}
</main>
""" + FOOT
write("/service-area/", area)


# ======================= CONTACT =======================
contact_page = {"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + "/contact-us/", "about": {"@id": SITE + "/#business"}}
contact = head("Contact Wohletz Roofing &amp; Construction | Free Estimate Ponca City OK",
               "Call (580) 716-0113 or request a free estimate for roof repair, roof replacement, storm damage or a new steel building in Ponca City, OK.",
               "/contact-us/", [contact_page, crumbs_schema([("/", "Home"), ("/contact-us/", "Contact")])]) + f"""
<main id="main">
<section class="hero page-hero">
  <img class="bg" src="/img/roofer-installing-shingles-ponca-city-ok.webp" alt="Roofer installing shingles in Ponca City" width="1350" height="675" fetchpriority="high">
  <div class="container hero-grid">
    <div>
      <p class="crumbs"><a href="/">Home</a> / Contact</p>
      <span class="eyebrow">Contact us</span>
      <h1>Let's Get Your Project Started<small>Free estimates in Ponca City &amp; North Central Oklahoma</small></h1>
      <p class="lead">Roofing question? Need a price on a new steel building? We're here to help. Call, email or fill out the form, and we'll get back to you as soon as possible.</p>
      <ul class="checks">
        <li>Phone: <a href="tel:{PHONE_TEL}" style="color:#fff;font-weight:700">{PHONE}</a></li>
        <li>Email: <a href="mailto:{EMAIL}" style="color:#fff">{EMAIL}</a></li>
        <li>Office: {STREET}, {CITY}, {REGION} {ZIP}</li>
        <li>Hours: {HOURS}. Sunday closed.</li>
      </ul>
    </div>
    {form(fid="contact")}
  </div>
</section>
{map_section()}
</main>
""" + FOOT
write("/contact-us/", contact)


# ======================= THANK YOU =======================
thanks = head("Thank You | Wohletz Roofing &amp; Construction", "Thanks for contacting Wohletz Roofing & Construction. We'll be in touch soon.", "/thank-you/", noindex=True) + f"""
<main id="main">
<section><div class="container center-card">
  <span class="eyebrow">Request received</span>
  <h1>Thanks! We've got your request.</h1>
  <p class="lead" style="margin-top:12px">We'll reach out soon, usually the same business day during our hours ({HOURS}). If it's urgent, like water coming in right now, please give us a call.</p>
  <p style="margin-top:22px"><a class="btn" href="tel:{PHONE_TEL}">{ICO["phone"]} Call {PHONE}</a></p>
  <div class="grid-3 next-steps" style="margin-top:44px">
    <div class="card"><div class="ico">{ICO["phone"]}</div><h3>1. We call you</h3><p>We'll ask a few quick questions and set a time to come out.</p></div>
    <div class="card"><div class="ico">{ICO["clipboard"]}</div><h3>2. Free estimate</h3><p>We inspect, take photos, and give you a clear, honest price.</p></div>
    <div class="card"><div class="ico">{ICO["check"]}</div><h3>3. Job done right</h3><p>Our crew does the work and cleans up before we leave.</p></div>
  </div>
  <div style="margin-top:44px">
    <h2 style="font-size:1.8rem">While you wait</h2>
    <p>See what our customers say on <a href="{GMB}" rel="noopener">Google</a>, follow us on <a href="{FACEBOOK}" rel="noopener">Facebook</a>, or look at the <a href="/steel-buildings/">steel buildings we build</a>.</p>
  </div>
</div></section>
{testimonials()}
</main>
""" + FOOT
write("/thank-you/", thanks)


# ======================= PRIVACY / TERMS =======================
def legal(path, title, h1, body, crumb):
    return head(f"{title} | {NAME}", f"{title} for wohletzroofingandconstruction.com.", path, [crumbs_schema([("/", "Home"), (path, crumb)])]) + f"""
<main id="main"><section><div class="container prose">
<p class="crumbs" style="color:var(--muted)"><a href="/">Home</a> / {crumb}</p>
<h1 style="font-size:2.6rem">{h1}</h1>
<p><i>Last updated October 2026</i></p>
{body}
</div></section></main>
""" + FOOT

privacy = legal("/privacy-policy/", "Privacy Policy", "Privacy Policy", f"""
<p>{NAME} LLC ("we," "us") respects your privacy. This policy explains what information we collect on wohletzroofingandconstruction.com and how we use it.</p>
<h2>Information you give us</h2>
<p>When you fill out our estimate form, we collect what you enter: your name, phone number, email, location, the service you're interested in, and any message. We use it only to respond to your request, schedule estimates and provide our services.</p>
<h2>How form submissions are delivered</h2>
<p>Our contact form is processed by FormSubmit, a third-party form service that delivers your submission to our email. Their handling of data is covered by their own privacy policy.</p>
<h2>Information collected automatically</h2>
<p>Like most websites, our hosting provider may log basic technical information such as IP address, browser type and pages visited, for security and performance. If we use analytics tools such as Google Analytics, they may use cookies to understand how visitors use the site. You can opt out of Google Analytics with Google's browser add-on.</p>
<h2>Sharing</h2>
<p>We don't sell, rent or trade your personal information. We only share it with service providers who help us run this website and our business, or when required by law.</p>
<h2>Text messages and email</h2>
<p>If you give us your phone number or email, we may contact you about your request. Message and data rates may apply. You can ask us to stop at any time.</p>
<h2>Your choices</h2>
<p>You can ask us to update or delete the information you've sent us by emailing <a href="mailto:{EMAIL}">{EMAIL}</a> or calling <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>
<h2>Contact</h2>
<p>{NAME}, {STREET}, {CITY}, {REGION} {ZIP}. Phone {PHONE}.</p>
""", "Privacy Policy")
write("/privacy-policy/", privacy)

terms = legal("/terms/", "Terms and Conditions", "Terms &amp; Conditions", f"""
<p>By using wohletzroofingandconstruction.com you agree to these terms.</p>
<h2>Website content</h2>
<p>The information on this website is for general information about our services. It isn't a quote, contract or warranty. Pricing, scope and warranties for any project are set out in a written estimate or agreement.</p>
<h2>Estimates</h2>
<p>Estimates are free and based on an inspection of your property. Final pricing may change if hidden damage, such as rotted decking, is found once work begins. We'll always talk with you before doing additional work.</p>
<h2>Photos</h2>
<p>Photos on this site show our work and representative examples of buildings and roofs we offer. Your project will be built to your own specifications.</p>
<h2>Links</h2>
<p>We may link to other websites, such as Google or Facebook. We aren't responsible for their content or privacy practices.</p>
<h2>Limitation of liability</h2>
<p>We work to keep this site accurate and available, but we don't guarantee it will be error free or uninterrupted, and we aren't liable for damages from your use of the site.</p>
<h2>Contact</h2>
<p>Questions? Call <a href="tel:{PHONE_TEL}">{PHONE}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
""", "Terms")
write("/terms/", terms)


# ======================= 404 =======================
nf = head("Page Not Found | Wohletz Roofing &amp; Construction", "Sorry, that page couldn't be found.", "/404/", noindex=True) + f"""
<main id="main"><section><div class="container center-card">
  {img("page-not-found-robot", "Cartoon construction robot holding a 404 page not found sign", 600, 516, lazy=False)}
  <h1>This page blew off in the wind</h1>
  <p class="lead" style="margin-top:12px">The page you're looking for isn't here. Let's get you back on solid ground.</p>
  <p style="margin-top:22px;display:flex;gap:12px;justify-content:center;flex-wrap:wrap"><a class="btn" href="/">Home</a><a class="btn dark" href="/roofing/">Roofing</a><a class="btn dark" href="/steel-buildings/">Steel Buildings</a></p>
</div></section></main>
""" + FOOT
write("404.html", nf)


# ======================= SUPPORT FILES =======================
PAGES = ["/", "/roofing/", "/roof-repair/", "/steel-buildings/", "/about/", "/service-area/", "/contact-us/", "/privacy-policy/", "/terms/"]
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{SITE}{p}</loc><lastmod>2026-10-18</lastmod></url>\n" for p in PAGES) + "</urlset>\n")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /thank-you/\n\nSitemap: {SITE}/sitemap.xml\n")
(ROOT / "site.webmanifest").write_text(json.dumps({"name": NAME, "short_name": "Wohletz", "icons": [
    {"src": "/android-chrome-192x192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "/android-chrome-512x512.png", "sizes": "512x512", "type": "image/png"}],
    "theme_color": "#d63a2a", "background_color": "#ffffff", "display": "standalone"}, indent=1))
# Old GoHighLevel URLs -> new pages
(ROOT / "_redirects").write_text("/home / 301\n/home/ / 301\n/contact /contact-us/ 301\n/roofing-services /roofing/ 301\n/steel-building /steel-buildings/ 301\n")
print("built", len(PAGES) + 2, "pages")

# IndexNow key file (Bing, Yandex and other IndexNow engines)
INDEXNOW_KEY = "30a53187beae0ab2168d3487d8b216fc"
(ROOT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY)
