# Facebook 粉絲專頁自動發文程式

這是一個可以自動發布貼文到 Facebook 粉絲專頁的 Python 程式。

## 功能特色

✓ **文字貼文** - 發布純文字內容  
✓ **圖片貼文** - 上傳圖片並發布  
✓ **連結分享** - 分享外部連結  
✓ **多專頁支援** - 可指定發布到特定粉絲專頁  
✓ **可重複使用** - 設計為可重複執行的腳本

## 使用方式

### 1. 基本文字貼文

```python
from facebook_auto_post import post_to_facebook

message = "這是一則測試貼文 📢"
result = post_to_facebook(message)
```

### 2. 帶圖片的貼文

```python
message = "分享一張美麗的照片 📷"
image_path = "path/to/your/image.jpg"

result = post_to_facebook(
    message=message,
    image_path=image_path
)
```

### 3. 帶連結的貼文

```python
message = "推薦大家看這篇文章"
link = "https://example.com/article"

result = post_to_facebook(
    message=message,
    link=link
)
```

### 4. 指定特定粉絲專頁

```python
message = "發布到特定專頁"
page_id = "your_page_id"

result = post_to_facebook(
    message=message,
    page_id=page_id
)
```

## 直接執行

你也可以直接執行腳本來測試：

```bash
python facebook_auto_post.py
```

這會顯示使用範例並執行一個測試貼文。

## 透過 Nebula 使用

如果你想要在 Nebula 環境中使用，可以直接告訴我：

- "發布貼文到 Facebook：這是貼文內容"
- "發布圖片到 Facebook 粉絲專頁"
- "分享連結到 Facebook"

## 進階功能

### 整合到定時任務

你可以將這個腳本設定為定時執行，例如：

- 每天早上自動發布「早安」貼文
- 每週發布摘要報告
- 特定事件觸發時自動發文

### 批次發布

```python
posts = [
    {"message": "第一則貼文"},
    {"message": "第二則貼文", "link": "https://example.com"},
    {"message": "第三則貼文", "image_path": "image.jpg"},
]

for post in posts:
    result = post_to_facebook(**post)
    print(f"發布結果: {result}")
```

## 注意事項

1. 確保你有 Facebook 粉絲專頁的管理權限
2. 圖片檔案需要是有效的路徑
3. 連結需要是完整的 URL (包含 http:// 或 https://)
4. Facebook API 有發文頻率限制，避免短時間內大量發文

## 需要協助？

如果需要修改或增加功能，隨時告訴我：

- 增加預約發文功能
- 支援影片上傳
- 新增貼文分析功能
- 批次管理貼文