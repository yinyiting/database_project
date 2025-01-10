
import pandas as pd
import random

# 定義常見的英文名字清單
names = ["Tiffany", "John", "Emma", "James", "Sophia", "Michael", "Olivia", "David", "Isabella", "Robert", 
         "Charlotte", "William", "Mia", "Ethan", "Amelia", "Alexander", "Harper", "Daniel", "Evelyn", "Matthew"]

# 隨機生成電話號碼的函式
def generate_phone_number():
    return "09" + ''.join(random.choices("0123456789", k=8))

# 固定前兩筆資料
data = {
    "name": ["Lian", "Tina"] + [random.choice(names) for _ in range(98)],
    "phone": ["900000000", "911111111"] + [generate_phone_number() for _ in range(98)]
}

# 確保剩餘電話號碼不重複
unique_phones = set(data["phone"])
while len(unique_phones) < 100:
    for i in range(2, 100):  # 從第3筆資料開始檢查
        new_phone = generate_phone_number()
        if new_phone not in unique_phones:
            data["phone"][i] = new_phone
            unique_phones.add(new_phone)

# 將資料存入DataFrame
df = pd.DataFrame(data)

# 儲存為CSV檔案
file_path = "Customer_Fixed.csv"
df.to_csv(file_path, index=False)
