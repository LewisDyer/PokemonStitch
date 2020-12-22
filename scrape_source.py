import os, requests

def get_url(number_or_url):
    # Get URL to scrape
    # if argument is a number, get the "normal" URL, else just return the provided URL
    # only provide a URL for limited edition designs!

    if type(number_or_url) == int:
        return f"https://pokemon.originalstitch.com/en/img/pattern_all/{number_or_url}.jpg"
    else:
        return number_or_url

def scrape_image(url, i):

    response = requests.get(url)

    with open(f"source/{i}.jpg", "wb") as image:
        image.write(response.content)



if __name__ == '__main__':
    os.makedirs("source", exist_ok=True)

    images_to_scrape = list(range(1, 252)) # Kanto + Johto Pokémon
    images_to_scrape.extend([252, 255, 258]) # Preview Hoenn Pokémon
    images_to_scrape.extend([f"https://pokemon.originalstitch.com/en/img/20201016/kito{i}.jpg" for i in range(1, 6)]) # Inori Kito designs
    images_to_scrape.extend([f"https://pokemon.originalstitch.com/en/img/20201120/coco{i}.jpg" for i in range(1, 5)]) # Coco designs

    images_to_scrape = map(get_url, images_to_scrape)

    for i, url in enumerate(images_to_scrape):
        scrape_image(url, i)
        if i % 50 == 0:
            print(i)
    