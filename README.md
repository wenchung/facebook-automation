# Facebook 粉絲專頁自動發文工具

使用 **Facebook Graph API** 自動發布貼文到粉絲專頁的 Python 工具。

## 功能特色

✅ **真正的 API 呼叫** - 直接使用 Facebook Graph API v18.0  
✅ **文字貼文** - 發布純文字內容  
✅ **圖片貼文** - 上傳圖片並發布  
✅ **連結分享** - 分享外部連結  
✅ **專頁管理** - 取得專頁資訊、最近貼文  
✅ **錯誤處理** - 完整的錯誤處理和提示訊息

## 環境需求

```bash
pip install requests
```

## 設定方式

### 1. 取得 Facebook Page Access Token

前往 [Facebook Developers](https://developers.facebook.com/):

1. 建立應用程式（或使用現有的）
2. 啟用 **Facebook Login** 和 **Pages API**
3. 在 Graph API Explorer 中：
   - 選擇你的應用程式
   - 選擇「取得頁面存取權束」
   - 授權必要權限：`pages_manage_posts`, `pages_read_engagement`
   - 複製 Page Access Token

### 2. 取得粉絲專頁 ID

- 方法 1：進入專頁設定 → 關於 → 頁面 ID
- 方法 2：使用 Graph API Explorer 查詢 `/me/accounts`

### 3. 設定環境變數

```bash
export FACEBOOK_PAGE_ACCESS_TOKEN="你的_Page_Access_Token"
export FACEBOOK_PAGE_ID="你的粉絲專頁ID"
```

## 使用方式

### 方式 1：直接執行腳本

```bash
python facebook_auto_post.py
```

這會執行示範程式，包含：
- 取得專頁資訊（名稱、粉絲數）
- 發布測試貼文
- 取得最近 5 則貼文

### 方式 2：在程式中使用

```python
from facebook_auto_post import FacebookPagesPoster

# 初始化
poster = FacebookPagesPoster(
    access_token="你的_Page_Access_Token",
    page_id="你的粉絲專頁ID"
)

# 發布文字貼文
result = poster.post_text("🎉 這是一則測試貼文！")
print(f"貼文 ID: {result['id']}")

# 發布圖片貼文
result = poster.post_photo(
    message="分享一張美麗的照片",
    photo_url="https://example.com/image.jpg"
)

# 發布連結貼文
result = poster.post_link(
    message="推薦閱讀這篇文章",
    link="https://example.com/article"
)

# 取得專頁資訊
page_info = poster.get_page_info()
print(f"專頁名稱: {page_info['name']}")
print(f"粉絲數: {page_info['fan_count']}")

# 取得最近的貼文
recent_posts = poster.get_recent_posts(limit=10)
for post in recent_posts['data']:
    print(post['message'])
```

## API 方法說明

### `post_text(message: str)`
發布純文字貼文

### `post_photo(message: str, photo_url: str)`
發布圖片貼文（需提供圖片網址）

### `post_link(message: str, link: str)`
發布連結貼文

### `get_page_info()`
取得粉絲專頁資訊（名稱、粉絲數、追蹤者）

### `get_recent_posts(limit: int = 10)`
取得最近的貼文列表

## 範例：定時發文

結合排程工具（如 cron）實現定時發文：

```bash
# 每天早上 9:00 發布貼文
0 9 * * * /usr/bin/python3 /path/to/facebook_auto_post.py
```

或在 Python 中使用 `schedule` 套件：

```python
import schedule
import time

def daily_post():
    poster = FacebookPagesPoster(access_token, page_id)
    message = f"早安！今天是 {datetime.now().strftime('%Y-%m-%d')}"
    poster.post_text(message)

schedule.every().day.at("09:00").do(daily_post)

while True:
    schedule.run_pending()
    time.sleep(60)
```

## 常見問題

### Q: 為什麼發文失敗？
A: 檢查以下項目：
1. Access Token 是否有效（是否為 Page Access Token）
2. 是否有 `pages_manage_posts` 權限
3. Page ID 是否正確
4. 網路連線是否正常

### Q: 如何上傳本地圖片？
A: Facebook Graph API 需要圖片網址。你可以：
1. 先上傳到圖床（如 Imgur）
2. 使用 `files` 參數上傳本地檔案（需修改程式碼）

### Q: 有發文頻率限制嗎？
A: 是的，Facebook 有 Rate Limiting。建議：
- 避免短時間內大量發文
- 每則貼文間隔至少 30 秒
- 一天不超過 200 則貼文

## 進階應用

### 整合 AI 生成內容

```python
def generate_ai_content():
    # 使用 AI 生成貼文內容
    return "AI 生成的有趣內容"

content = generate_ai_content()
poster.post_text(content)
```

### 批次發布多則貼文

```python
posts = [
    {"type": "text", "message": "第一則貼文"},
    {"type": "link", "message": "分享連結", "link": "https://example.com"},
    {"type": "photo", "message": "分享圖片", "photo_url": "https://example.com/image.jpg"},
]

for post_data in posts:
    if post_data["type"] == "text":
        poster.post_text(post_data["message"])
    elif post_data["type"] == "link":
        poster.post_link(post_data["message"], post_data["link"])
    elif post_data["type"] == "photo":
        poster.post_photo(post_data["message"], post_data["photo_url"])
    
    time.sleep(30)  # 避免觸發頻率限制
```

## 授權與免責聲明

本工具僅供學習和合法用途使用。使用時請遵守 Facebook 平台政策和使用條款。

## 需要協助？

如果遇到問題或需要新增功能，歡迎回報：
- 預約發文功能
- 影片上傳支援
- 貼文分析統計
- 多專頁批次管理
