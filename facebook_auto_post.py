#!/usr/bin/env python3
"""
Facebook Pages 自動發文工具
使用 Facebook Graph API 發布貼文到粉絲專頁
"""

import os
import sys
import requests
from datetime import datetime
from typing import Optional, Dict, Any


class FacebookPagesPoster:
    """Facebook 粉絲專頁發文管理器"""
    
    def __init__(self, access_token: str, page_id: str):
        """
        初始化 Facebook API 客戶端
        
        Args:
            access_token: Facebook Page Access Token
            page_id: Facebook 粉絲專頁 ID
        """
        self.access_token = access_token
        self.page_id = page_id
        self.base_url = "https://graph.facebook.com/v18.0"
    
    def post_text(self, message: str) -> Dict[str, Any]:
        """
        發布純文字貼文
        
        Args:
            message: 貼文內容
            
        Returns:
            API 回應結果
        """
        endpoint = f"{self.base_url}/{self.page_id}/feed"
        
        payload = {
            "message": message,
            "access_token": self.access_token
        }
        
        response = requests.post(endpoint, data=payload)
        return self._handle_response(response)
    
    def post_photo(self, message: str, photo_url: str) -> Dict[str, Any]:
        """
        發布圖片貼文
        
        Args:
            message: 貼文內容
            photo_url: 圖片網址
            
        Returns:
            API 回應結果
        """
        endpoint = f"{self.base_url}/{self.page_id}/photos"
        
        payload = {
            "message": message,
            "url": photo_url,
            "access_token": self.access_token
        }
        
        response = requests.post(endpoint, data=payload)
        return self._handle_response(response)
    
    def post_link(self, message: str, link: str) -> Dict[str, Any]:
        """
        發布連結貼文
        
        Args:
            message: 貼文內容
            link: 連結網址
            
        Returns:
            API 回應結果
        """
        endpoint = f"{self.base_url}/{self.page_id}/feed"
        
        payload = {
            "message": message,
            "link": link,
            "access_token": self.access_token
        }
        
        response = requests.post(endpoint, data=payload)
        return self._handle_response(response)
    
    def get_page_info(self) -> Dict[str, Any]:
        """
        取得粉絲專頁資訊
        
        Returns:
            專頁資訊
        """
        endpoint = f"{self.base_url}/{self.page_id}"
        
        params = {
            "fields": "id,name,username,fan_count,followers_count",
            "access_token": self.access_token
        }
        
        response = requests.get(endpoint, params=params)
        return self._handle_response(response)
    
    def get_recent_posts(self, limit: int = 10) -> Dict[str, Any]:
        """
        取得最近的貼文
        
        Args:
            limit: 取得數量
            
        Returns:
            貼文列表
        """
        endpoint = f"{self.base_url}/{self.page_id}/feed"
        
        params = {
            "fields": "id,message,created_time,permalink_url",
            "limit": limit,
            "access_token": self.access_token
        }
        
        response = requests.get(endpoint, params=params)
        return self._handle_response(response)
    
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """
        處理 API 回應
        
        Args:
            response: requests 回應物件
            
        Returns:
            解析後的 JSON 資料
            
        Raises:
            Exception: API 呼叫失敗時
        """
        if response.status_code == 200:
            return response.json()
        else:
            error_data = response.json()
            error_msg = error_data.get("error", {}).get("message", "Unknown error")
            raise Exception(f"Facebook API Error: {error_msg} (Status: {response.status_code})")


def main():
    """主程式：示範如何使用 FacebookPagesPoster"""
    
    # 從環境變數讀取設定
    access_token = os.getenv("FACEBOOK_PAGE_ACCESS_TOKEN")
    page_id = os.getenv("FACEBOOK_PAGE_ID")
    
    if not access_token or not page_id:
        print("❌ 錯誤：請設定環境變數")
        print("   export FACEBOOK_PAGE_ACCESS_TOKEN='你的 Page Access Token'")
        print("   export FACEBOOK_PAGE_ID='你的粉絲專頁 ID'")
        sys.exit(1)
    
    # 初始化發文工具
    poster = FacebookPagesPoster(access_token, page_id)
    
    try:
        # 1. 取得專頁資訊
        print("📊 取得專頁資訊...")
        page_info = poster.get_page_info()
        print(f"   專頁名稱: {page_info.get('name')}")
        print(f"   粉絲數: {page_info.get('fan_count', 0):,}")
        print(f"   追蹤者: {page_info.get('followers_count', 0):,}")
        print()
        
        # 2. 發布測試貼文
        print("✍️  發布測試貼文...")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        test_message = f"🤖 AI 機器人測試貼文\n\n發布時間: {timestamp}"
        
        result = poster.post_text(test_message)
        post_id = result.get("id")
        print(f"   ✅ 發布成功！貼文 ID: {post_id}")
        print()
        
        # 3. 取得最近的貼文
        print("📝 取得最近 5 則貼文...")
        recent_posts = poster.get_recent_posts(limit=5)
        
        for idx, post in enumerate(recent_posts.get("data", []), 1):
            message = post.get("message", "(無內容)")[:50]
            created_time = post.get("created_time", "")
            print(f"   {idx}. {message}...")
            print(f"      發布時間: {created_time}")
        
        print("\n✅ 所有操作完成！")
        
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
