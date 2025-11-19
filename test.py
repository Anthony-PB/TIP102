import requests
from bs4 import BeautifulSoup
import re # Used for advanced attribute matching

try:
    response = requests.get('https://tns4lpgmziiypnxxzel5ss5nyu0nftol.lambda-url.us-east-1.on.aws/challenge')
    response.raise_for_status() # Check for bad status code
    html_doc = response.text
except Exception as e:
    print(f"Error fetching URL: {e}")
    # Using placeholder HTML for demonstration if fetching fails
    html_doc = """
    <html><body>
    <section data-id="123">...</section>
    <section data-id="92A">
        <article data-class="X45">
            <div data-tag="B78C">
                <b class="ref" value="h"></b>
            </div>
        </article>
    </section>
    <div data-tag="78">...</div>
    <section data-id="92B">
        <article data-class="Y45">
            <div data-tag="A78B">
                <b class="ref" value="t"></b>
            </div>
        </article>
    </section>
    </body></html>
    """

# Initialize Beautiful Soup
soup = BeautifulSoup(html_doc, 'html.parser')

# Build the final URL string
hidden_url_chars = []

# --- CSS Selector Logic ---

# We need to find the <b> tag nested inside the exact pattern:
# <section data-id="92*">
#   <article data-class="*45">
#     <div data-tag="*78*">
#       <b class="ref" value="VALID_CHARACTER"></b>
#     </div>
#   </article>
# </section>

# CSS Selectors for complex attribute matching:
# 1. `section[data-id^="92"]`  -> <section> where 'data-id' starts with "92"
# 2. `article[data-class$="45"]` -> <article> where 'data-class' ends with "45"
# 3. `div[data-tag*="78"]`   -> <div> where 'data-tag' contains "78"
# 4. `b.ref`                  -> <b> with class="ref"

# The descendant selector (space) links these nested elements
css_selector = 'section[data-id^="92"] article[data-class$="45"] div[data-tag*="78"] b.ref'

# 2. Execute the single, powerful selector query
# This finds ALL <b> elements that match the nested pattern in order
valid_b_tags = soup.select(css_selector)

# 3. Extract the 'value' attribute from each matching tag
for b_tag in valid_b_tags:
    # Get the value of the 'value' attribute
    char = b_tag.get('value')
    if char:
        hidden_url_chars.append(char)

# 4. Join the characters to form the final URL
final_url = "".join(hidden_url_chars)

## Results
print(f"Found {len(hidden_url_chars)} characters.")
print(f"The hidden URL is: **{final_url}**")