# foxitAssetUrl list
# Pearson Physics 11 Western Australia 
    # https://d2f01w1orx96i0.cloudfront.net/resources/products/epubs/generated/b80f43ed-8190-42a2-8c62-9b96f8bb697f/foxit-assets
# Pearson Science 7 2nd Edition
    # https://d2f01w1orx96i0.cloudfront.net/resources/products/epubs/generated/0BF64C74-5379-4819-A22C-590AA451028E/foxit-assets

import requests
from PIL import Image
from io import BytesIO

requests.packages.urllib3.disable_warnings()
print("Instructions:\n\tOpen the book online in the Pearson viewer\n\tOpen dev tools (click F12)\n\tClick the 'console' tab\n\tType in 'foxitAssetUrl' at the bottom\n\tClick enter\n\tCopy the output\n\tPaste the value below\n")
book_url = input("foxitAssetUrl: ")
pages = []
page_no = 0
test_status_code = requests.get(f"{book_url}/pages/page0", verify=False).status_code
if test_status_code != 200:
    print(f"Error finding book ({test_status_code} response)")
    exit()
while True:
    response = requests.get(f"{book_url}/pages/page{page_no}", verify=False)
    if response.status_code == 403 and "AccessDenied" in response.text:
        break
    if page_no == 0:
        image1 = Image.open(BytesIO(response.content))
    else:
        pages.append(Image.open(BytesIO(response.content)))
    page_no += 1
    print(f"{page_no} page(s) downloaded", end="\r")
print("\nConverting to pdf...")
image1.save("output.pdf", save_all=True, append_images=pages)
print("Book saved to ./output.pdf")
