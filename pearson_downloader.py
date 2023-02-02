import requests
from PIL import Image
from io import BytesIO

print("Instructions:\n\tOpen the book online in the Pearson viewer\n\tOpen dev tools (click F12)\n\tClick the 'console' tab\n\tType in 'foxitAssetUrl' at the bottom\n\tClick enter\n\tCopy the output\n\tPaste the value below\n")
book_url = input("foxitAssetUrl: ")
pages = []
page_no = 0
test_status_code = requests.get(f"{book_url}/pages/page0").status_code
if test_status_code != 200:
    print(f"Error finding book ({test_status_code} response)")
    exit()
while True:
    response = requests.get(f"{book_url}/pages/page{page_no}")
    if response.status_code == 403 and "AccessDenied" in response.text:
        break
    if page_no == 0:
        image1 = Image.open(BytesIO(response.content))
    else:
        pages.append(Image.open(BytesIO(response.content)))
    page_no += 1
    print(f"{page_no} page(s) downloaded", end="\r")
print("\nFinished downloading all page(s)")
image1.save("output.pdf", save_all=True, append_images=pages)
print("Book saved to ./output.pdf")
