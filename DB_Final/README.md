# 建立虛擬環境 / 進入虛擬環境
python -m venv DB_venv
.\DB_venv\Scripts\activate

# 安裝 Django 與其他相關套件
pip install django PyMySQL

# 安裝並設定 MySQL
- 到 MySQL 官網下載安裝檔並安裝 (參考 lab2)
- 下載 MySQL Workbench
- 將 .csv檔匯入 MySQL Workbench

# 建立 Django 新專案
django-admin startproject DB_project
- 輸入此指令會產生一個 Django project 資料夾

# 測試是否成功連進 Django
cd DB_project
python manage.py runserver
http://127.0.0.1:8000/

# 建立 Django app : https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/django/project_and_app.html
python manage.py startapp myapp

1. 先到 myapp/views.py 新增 hello_world
    from django.http import HttpResponse
    def home(request):
        return HttpResponse("Hello World!")

2. 再到 DB_project/urls.py 中，引入剛剛再views中定義的 hello_world 
    from myapp.views import home
    path('home/', home),
 
3. 執行並檢查是否成功
    python manage.py runserver
    http://127.0.0.1:8000/home/

# 建立 Django Template

1. 在 DB_project/settings.py 搜尋 TEMPLATES，在 DIRS 中加入：
    os.path.join(BASE_DIR, 'templates').replace('\\', '/')

2. 在 manage.py 同級處新增一個 templates 資料夾，並在其中新增 home.html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>hello_world</title>
    </head>
    <body>
        <h1>hello_world!</h1>
    </body>
    </html>

3. 進入 myapp/views.py 中，修改 home
    from django.shortcuts import render
    def home(request):  
        return render(request, 'home.html') #修改

4. 執行並檢查是否成功
    python manage.py runserver
    http://127.0.0.1:8000/home/

5. 補充資料
    https://ithelp.ithome.com.tw/articles/10297327

# 資料庫遷移 (MySQL 連線到 Django)
0. DB_project 的 __init__ 新增:
    import pymysql
    pymysql.install_as_MySQLdb()

1. 修改 settings.py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',   # 使用 MySQL
            'NAME': 'movie_db',                     # 資料庫名稱
            'USER': 'root',                         # 資料庫用戶
            'PASSWORD': '1234',                     # 密碼
            'HOST': 'localhost',                    # 主機地址（本機用 localhost）
            'PORT': '3306',                         # MySQL 預設端口
        }
    }

2. 連結已有的資料庫與Django app (根據現有資料庫自動生成 Django 模型。如果是新的資料庫或手動建立的模型，可以跳過這一步。)
    python manage.py inspectdb > myapp/models.py

3. 剪下所有 models.py 內容，vscode 轉成 utf-8 把內容貼上

4. 建立migrations資料表
    python manage.py makemigrations

5. migrate同步資料表
    python manage.py migrate

# Django app 接後端
1. myapp.view
2. 接到前端 .html



python manage.py runserver
http://localhost:8000/main/home/

# update log

## 1230 1651 update
將home.html的js css分出來
將重複的html改為迴圈 (上映中電影、所有電影)

## 1230 2042 update
將home改為index

## 1230 2113 update
新增base模板

## 1230 2208 update
修正沒有更改分店 場次時 無法選座位的問題

## 1230 2219 update
修正 按send後 訂位成功的頁面 無法顯示問題

## 1230 2235 update
新增按send(button2)後 將data insert入database

## 1230 2318
簡單修改查詢訂單頁面

## 1230 2324
新增查詢訂票後 刪除按鈕

# todo



