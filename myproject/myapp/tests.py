# test_views.py
from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):

    def test_home_view(self):
        # 使用 Django 測試 Client 模擬請求
        response = self.client.get(reverse('hello_world'))  # 假設路由名稱是 'home'

        # 檢查 HTTP 狀態碼
        self.assertEqual(response.status_code, 200)

        # 檢查返回的內容
        self.assertContains(response, "Hello, World!")  # 檢查是否包含這個字串
