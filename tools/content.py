"""Everything the home page says. build.py only arranges it.

Copy is Cyan Technology's own, from cyangits.com (fetched 23 Sep 2026),
tightened where the original repeated itself. Anything that is new writing
rather than theirs is listed under "Before this goes live" in the README.
"""

BASE = "https://cyangits.com"
LEGAL = "Cyan Technology for IT Systems Co."
BRAND = "Cyan Technology"
PHONE = "+966531431733"
PHONE_SHOW = "+966 53 143 1733"
EMAIL = "marketing@cyangits.com"      # the address the old contact page publishes
ADDRESS_LINES = ["Prince Nayef Street, 3rd Cross", "Al Khobar Al Shamalia", "Al Khobar 34429, Saudi Arabia"]
MAP_Q = "Prince Nayef Street, Al Khobar Al Shamalia, Al Khobar 34429, Saudi Arabia"

# the old site's counters (data-to-value on the home page)
STATS = [("900", "Active clients"), ("965", "Projects completed"),
         ("15", "Years of experience"), ("150", "Professional team")]

ABOUT_LONG = (
    "Growth with innovation is something we value highly. Over the years we have "
    "grown by delivering innovative products and by building lasting relationships "
    "with clients around the world. We believe great minds create great products."
)
ABOUT_WHO = (
    "Cyan provides IT-enabled services for educational institutions, universities and "
    "business organisations, in the best economic sense and with the least acceptable "
    "risk. From Al Khobar, the company is building a presence in India, Europe and the "
    "Middle East."
)
MISSION = ("To deliver high-quality, technology-driven services that foster long-term "
           "relationships and drive success for our clients worldwide.")
VISION = ("To be a global leader in innovative IT solutions, empowering businesses and "
          "institutions with cutting-edge technology and sustainable growth.")

PROCESS = [
    ("Market research", "Understanding your customers and your competition first, so what we build answers a real need and keeps you competitive."),
    ("A supported team", "Clear guidance, the right resources and steady leadership behind every project team, so goals are met rather than chased."),
    ("First response", "A team that listens to the question, answers it clearly and brings a working solution, so nothing waits in a queue."),
]

ARROW = ('<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" '
         'stroke-width="1.4" aria-hidden="true"><path d="M1 5h8M5.5 1.5 9 5l-3.5 3.5"/></svg>')
ARROW_UP = ('<svg class="go" width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" '
            'stroke-width="1.4" aria-hidden="true"><path d="M2 10 10 2M4 2h6v6"/></svg>')
ICON_PHONE = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
              'aria-hidden="true"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/></svg>')
ICON_MAIL = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
             'aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 7 8.5-7"/></svg>')
ICON_CHAT = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
             'aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 9.5h8M8 12.5h5"/></svg>')

# ------------------------------------------------------------------
# Services. Order is the order on the page and in the footer. The slug
# is the old WordPress slug, kept as the enquiry form's option key.
# ------------------------------------------------------------------
SERVICES = [
    dict(
        slug="erp-solution", name="ERP & Software Development",
        card="The whole product life cycle, from the first idea through deployment to user acceptance.",
        meta=["Engineering", "Integration", "Support"],
    ),
    dict(
        slug="mobile-application", name="Mobile Applications",
        card="Native iOS and Android, or one cross-platform build that reaches every device.",
        meta=["iOS", "Android", "Cross-platform"],
    ),
    dict(
        slug="web-design-development", name="Web Design & Development",
        card="Custom websites and web applications, WooCommerce shops, WordPress and Drupal, and the SEO behind them.",
        meta=["Web", "E-commerce", "SEO"],
    ),
    dict(
        slug="whatsapp-api-services", name="WhatsApp API Services",
        card="The WhatsApp Business API, wired into your CRM, your shop and your payment gateway.",
        meta=["WhatsApp", "CRM", "Payments"],
    ),
    dict(
        slug="server-hosting-cloud-management", name="Server Hosting & Cloud",
        card="Secure, high-uptime hosting, and management of private, public or hybrid cloud.",
        meta=["Hosting", "Cloud", "24/7 support"],
    ),
    dict(
        slug="g-suite-microsoft-365", name="Google Workspace & Microsoft 365",
        card="Setup, email and data migration, security configuration and ongoing support for both suites.",
        meta=["Setup", "Migration", "Support"],
    ),
    dict(
        slug="integration-migration", name="Integration & Migration",
        card="Off on-premise servers or another cloud, without losing an email, a contact or a calendar.",
        meta=["Email", "Data", "Hybrid cloud"],
    ),
    dict(
        slug="bulk-email-service", name="Bulk Email",
        card="Personalised campaigns to thousands at once, built to land in the inbox rather than spam.",
        meta=["Campaigns", "Automation"],
    ),
    dict(
        slug="bulk-sms-service", name="Bulk SMS",
        card="Campaigns, OTPs and alerts through our own SMS gateway, across India and the Middle East.",
        meta=["India", "Middle East", "API"],
    ),
    dict(
        slug="social-media-services", name="Social Media",
        card="Strategy, content, paid campaigns and reporting, on every platform your customers use.",
        meta=["Strategy", "Content", "Ads"],
    ),
    dict(
        slug="graphic-designing", name="Graphic Design",
        card="Logos, brand identity, print and marketing design, drawn to say what the brand stands for.",
        meta=["Logo", "Identity", "Print"],
    ),
]

# ------------------------------------------------------------------
# Products: names come from the product logos. The one-line
# descriptions marked * are inferred from the artwork, not stated
# anywhere on the old site (see README).
# ------------------------------------------------------------------
PRODUCTS = [
    ("Cyan Real World", "Software for apartments &amp; real estate", "p-realworld.webp"),
    ("Cyan HR &amp; Payroll", "HR and payroll software", "p-hr.webp"),
    ("EduCyan", "Education software", "p-edu.webp"),                 # *
    ("CyanSoft", "Logistics cloud application", "p-logistics.webp"),
    ("Cyan Smartshop", "Retail solutions", "p-smartshop.webp"),
    ("Cyan Traco", "Trading &amp; construction software", "p-traco.webp"),
    ("Cyan Glitz", "Jewellery management system", "p-glitz.webp"),
    ("MediCyan", "Healthcare software", "p-medi.webp"),              # *
    ("Cyan Smart Wheels", "Automotive software", "p-wheels.webp"),   # *
    ("Cyan Auto Smart", "Automotive software", "p-auto.webp"),       # *
    ("Cyan Media", "Media and design", "p-media.webp"),              # *
]

# ------------------------------------------------------------------
# Clients: file stem -> name as read off the logo. None where the logo
# is an emblem with no legible name; those get a generic alt.
# ------------------------------------------------------------------
CLIENTS = {
    "1264642": "InterContinental Al Khobar", "18350227": "Zara Continental Hotel, Al Khobar",
    "18986624": "Specialized Dentists Clinics", "25455618": "Saudi Arabian Hydroponic Co.",
    "32184717": "First Choice Building Materials", "3star": "Three Star Engineering Services",
    "4-season": "Four Season Stores", "4476565": "Grand Hyper",
    "52922116": "Dream Foundation's Group", "62655526": "Zaina International Co.",
    "6487159": "Obagi Medi Spa", "65283312": "Abdallah Opticals",
    "6783123": "Modern Waseet Logistics", "7689816": "Sheraton Hotels & Resorts",
    "82283222": "Middle East Group", "84799511": "Nesto",
    "8662125": "Training Marks", "87102929": "Ziryab Restaurant",
    "87847514": "Badr Al-Rabie Medical Group", "9566143": "Malabar Gold & Diamonds",
    "98621613": "Al-Ghadeer Pharmacy", "abeercold": "Al-Abeer Cold Stores",
    "ahazco-1": "Ahazco Group", "al-abeer": "Al-Abeer Coldstore Trading Company",
    "al-muneer": "Al Muneer", "ala11": "Al-Ammari", "alm1": "Al-Madar International Est.",
    "alotasihn": "Abdulrahman Al-Otaishan Group", "at-your": "At Your Service",
    "auto": "Auto Heaven", "bloom-arabia": "Bloom Al-Arabia Service & Trading Est.",
    "bm-cargo": "BM Cargo", "c1": "Al Majd International School, Dammam",
    "c10": "Sona Gold & Diamonds", "c11": "Malak Gold & Diamonds",
    "c12": "Gulf Asian Medical Center", "c13": "ELC World SA", "c14": None,
    "c15": "Nexus Middle East Industrial Services", "c16": "LuLu Hypermarket",
    "c17": "Speed Track", "c18": None, "c19": "Dammam Laundry",
    "c2": "Al Muna International School", "c20": "Suncity Polyclinic", "c21": None,
    "c22": "Gulfwest Company Limited", "c23": "Lustro", "c24": "Joyalukkas",
    "c25": "GBCo.", "c4": "Al Hussaini Co.", "c5": "Dunes International School",
    "c6": None, "c7acc": "Arabian Company for Construction Engineering", "c8": None,
    "c9": "Al-Fakhri Co.", "calex": "Calex Marine & Industrial Services",
    "care-hut": "Care Hut Health Care", "cliadtc": "AD Stationery",
    "cliajaz": "Al Jazira Clinic", "clialfalah": "Halawiyat Al Falah", "clialmo": None,
    "clialsharq": None, "cliammar": "Ammar Bin Ali Al-Shaib Gen. Cont. Est.",
    "cliastic": "Advance System Company", "clicaltech": "Caltech Arabia",
    "clidar": "Dar wa Emaar", "clieamas": "Amas Arabia Contracting Est.",
    "cliegc": "Eastern Gulf Gen. Cont. Est.", "cliershid": "Ershid", "clifa": None,
    "climace": "Mace", "climadeena": "Al Madeena Cold Store",
    "climeshan": "Ahmed Meshan Al-Shammari & Co.", "climom": "Momenco",
    "clinvss": "Narrative Vision Industrial Support Services",
    "clios": "Online Systems & Communications Est.", "cliquadi": "Quadisiyya English Medium School",
    "clitawasol": "Tawasol", "clitrinity": None, "clitst": "TST Technical Information Solutions & Training",
    "clivhgss": None, "clivictory": "Victory International Schools", "east1": "Eastern Group",
    "emaar": None, "era1": "Era Advanced", "ft-creative": "Future Creative Craft Industrial Services",
    "gann1": "Gannas Al-Khobar", "glo1": "Global Tide International Trading Est.",
    "gouna-site": "Gouna Company Limited", "khonaini": "Khonaini Catering & Camps Services",
    "kmad": None, "mac": "Mani Arabian Company", "malaaz": "Maran Restaurant",
    "ms-alwahami": None, "nafitha": "Nafitha Services Est.", "new-metro": "New Metro Trading Company",
    "plus-two": None, "rag1": "Ragce", "tasneem": "Tasneem", "zomorrud": "Zomorrud Hotel",
}

# the two drifting rows on the home page: the best-known names first
ROW_A = ["1264642", "c16", "7689816", "c24", "9566143", "84799511", "4476565", "18350227",
         "87847514", "98621613", "c12", "6487159", "clicaltech", "zomorrud", "6783123",
         "bm-cargo", "calex", "east1", "c10", "82283222"]
ROW_B = ["c5", "clivictory", "c2", "cliquadi", "alotasihn", "cliammar", "c7acc", "climace",
         "care-hut", "cliajaz", "65283312", "32184717", "3star", "ft-creative", "khonaini",
         "gouna-site", "mac", "clitst", "climadeena", "c11"]
