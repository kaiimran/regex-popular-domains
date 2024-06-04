import re

# Use this function to remove some characters from a URL for standization first before checking the pattern
def clean_url(url):
    # Convert to lowercase for case-insensitive matching
    url = url.lower()
    # Remove 5 patterns: https://, http://, www., https://www., http://www.
    patterns_to_remove = ["https?://www\\.", "https?://", "www\\."] # the order is important
    for pattern in patterns_to_remove:
        url = re.sub(pattern, "", url)
    # Remove query parameters (?) and trailing slash (last "/" at the end of URL)
    url = re.sub("\\?.*$", "", url)
    url = re.sub("/$", "", url)
    return url

# Regex pattern to check if a URL is from the platforms listed below
facebook_pattern = r'^(?:(?:lm|m|l|adsmanager|free|business|web|mobile|mtouch|touch)\.)?facebook\.com|fb\.(com|watch|me|gg)'
twitter_pattern = r'^t\.co|(?:mobile\.|m\.)?(?:twitter|x)\.com'
google_pattern = r'^(?:google\.com|partner\.googleadservices\.com|.*\.safeframe\.googlesyndication\.com)'
bing_pattern = r'^bing\.com'
youtube_pattern = r'^(?:m\.youtube\.com|youtube\.com|youtu\.be)'
telegram_pattern = r'^(?:t\.me|web\.telegram\.org)'
whatsapp_pattern = r'^(?:wa\.me|web\.whatsapp\.com)'
instagram_pattern = r'^(?:l\.|m\.)?instagram\.com'
tiktok_pattern = r'^(?:vt|vm\.)?tiktok\.com'
pinterest_pattern = r'^pin\.it|(?:(?:br|id|in|nl|sk)\.)?pinterest\.(?:com|ca|co\.kr|co\.uk|com\.au|fr|it|ph|se)'
threads_pattern = r'^(?:l|m\.)?threads\.net'
blogspot_pattern = r'^[a-zA-Z0-9-]+\.blogspot\.com'
tumblr_pattern = r'^[a-zA-Z0-9-]+\.tumblr\.com'
wordpress_pattern = r'^[a-zA-Z0-9-]+\.wordpress\.com'
linkedin_pattern = r'^(?:linkedin\.com|lnkd\.in)'
reddit_pattern = r'^(?:old|new)\.reddit\.com|reddit\.com|redd\.it'
quora_pattern = r'^quora\.com|qr\.ae'
medium_pattern = r'^(?:medium\.com|link\.medium\.com)'

# Top 10 most popular link in bio platforms: linktr.ee, beacons.ai, msha.ke, bio.link, linkpop.com, linknbio.com, linkin.bio, lnk.bio, campsite.to, carrd.co
link_in_bio_pattern = r'^(?:linktr\.ee|beacons\.ai|msha\.ke|bio\.link|linkpop\.com|linknbio\.com|linkin\.bio|lnk\.bio|campsite\.to|(?:[^/]+\.)?carrd\.co)'
goviral_pattern = r'^goviral\.growthtools\.com'
link_shortener_pattern = r'^(?:bit\.ly|tinyurl\.com|tiny\.cc|ow\.ly|is\.gd)'

# Malaysians' popular platforms
lowyat_pattern = r'^(?:forum\.)?lowyat\.net'
cari_pattern = r'^(?:cari\.com\.my|b\.cari\.com\.my|c\.cari\.com\.my)'
mudah_pattern = r'^mudah\.my'
# KIV: shopee, lazada, carousel because need to consider the country code (e.g., shopee.com.my, shopee.com.sg), language and the short link shp.ee

#################### TESTING ####################
# The pattern below is a bit different from the above patterns because it is used to find the URL in a text article or sentence
cari_pattern = r"(^|\s)([a-zA-Z0-9-]+\.)*cari\.com\.my(\s|$)"

test_strings = [
    "Visit cari.com.my for more information.",
    "cari.com.my",
    "Check out the new topics at b.cari.com.my!",
    "Invalid link: caricom.my", # False
]

#### 1. Function to test the pattern by matching it with the test strings
def match_pattern(pattern, test_strings):
    for test_string in test_strings:
        if re.search(pattern, test_string):
            print(f"Contain: {test_string}")
        else:
            print(f"Did not contain: {test_string}")

# Run the test for cari_pattern
match_pattern(cari_pattern, test_strings)

#### 2. Function to test if a URL is from a specific platform
def url_match_pattern(pattern, url):
    cleaned_url = clean_url(url)
    return re.match(pattern, cleaned_url, re.IGNORECASE) is not None

test_urls = [
    "https://bit.ly/abc",
    "http://tinyurl.com/xyz",
    "https://www.bit.ly/abc",
    "http://www.ow.ly/abc123",
    "is.gd/",
    "https://wrong.com/path", # False
    "tiny.cc/123",
    "www.bit.ly/abc"
]

# The pattern below is a bit different from the previous patterns because it is used to match https://www assuming clean_url() is not called inside the url_match_pattern() function
link_shortener_pattern = r'^(?:https?://)?(?:www\.)?(bit\.ly|tinyurl\.com|tiny\.cc|ow\.ly|is\.gd)'

# Run the test for link_shortener_pattern
for url in test_urls:
    if url_match_pattern(link_shortener_pattern, url):
        print(f"{url}: This refers to a link shortener service.")
    else:
        print(f"{url}: This DOES NOT refer to a link shortener service.")
