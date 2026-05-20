from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(
        channel="chrome",
        headless=False
    )

    page = browser.new_page()

    page.goto("https://www.baidu.com")

    # 输入“你好”
    page.fill("#kw", "你好")

    # 回车搜索
    page.keyboard.press("Enter")

    input("按回车关闭")

    browser.close()