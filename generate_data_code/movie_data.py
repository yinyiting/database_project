import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from googletrans import Translator

# 初始化翻譯器
translator = Translator()

# 隨機生成其他欄位內容的函數
def generate_random_data():
    genres = ["Adventure", "Comedy", "Action", "Drama", "Fantasy", "Horror", "Sci-Fi", "Romance"]
    statuses = ["Now Showing", "Coming Soon", "Ended"]
    durations = [f"{random.randint(90, 180)} min" for _ in range(86)]
    descriptions = [
        "A breathtaking tale of courage and discovery.",
        "An unforgettable journey into the unknown.",
        "A story of love, loss, and redemption.",
        "A thrilling adventure that defies all odds.",
        "An epic saga filled with twists and turns."
    ]
    return random.choice(genres), random.choice(statuses), random.choice(durations), random.choice(descriptions)

# 爬取電影中文名稱的函數
def scrape_movie_titles(url, num_titles=86):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 假設電影名稱在 <div class="movie-title"> 中（根據網站調整）
    titles = [title.text.strip() for title in soup.find_all('div', class_='movie-title')]
    return titles[:num_titles]

# 爬取電影名稱
url = "https://example.com/movies"  # 替換為實際目標網站
movie_titles_chinese = scrape_movie_titles(url)

# 翻譯中文名稱到英文
movie_titles_english = [translator.translate(title, src='zh-cn', dest='en').text for title in movie_titles_chinese]

# 構建 DataFrame
movies_data = {
    "Chinese_Title": movie_titles_chinese,
    "English_Title": movie_titles_english,
    "Genre": [],
    "Status": [],
    "Duration": [],
    "Description": []
}

# 填充其他欄位
for _ in range(len(movie_titles_chinese)):
    genre, status, duration, description = generate_random_data()
    movies_data["Genre"].append(genre)
    movies_data["Status"].append(status)
    movies_data["Duration"].append(duration)
    movies_data["Description"].append(description)

# 儲存為 CSV
df = pd.DataFrame(movies_data)
output_path = "movies_scraped_data.csv"
df.to_csv(output_path, index=False, encoding="utf-8-sig")
print(f"CSV file saved to {output_path}")
