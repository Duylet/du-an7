# Dự án 7 — Scrapy Web Scraping Demo

Dự án Python minh họa cách sử dụng [Scrapy](https://github.com/scrapy/scrapy) để thu thập dữ liệu từ website luyện tập `quotes.toscrape.com`.

## Chức năng
- Thu thập nội dung trích dẫn, tên tác giả và thẻ.
- Tự động chuyển sang các trang tiếp theo.
- Xuất dữ liệu ra JSON hoặc CSV.
- Cấu hình tốc độ thu thập thận trọng, phù hợp cho việc học.

## 1. Yêu cầu
- Python 3.10 trở lên (khuyến nghị Python 3.11–3.13).
- VS Code và Python extension.
- Kết nối Internet.

## 2. Cài đặt trên Windows / VS Code

Mở terminal tại thư mục dự án:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Nếu PowerShell không cho kích hoạt môi trường ảo, có thể gọi Python trong môi trường ảo trực tiếp:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m scrapy list
```

## 3. Chạy spider

Chạy lệnh từ thư mục có file `scrapy.cfg`:

```powershell
python -m scrapy list
python -m scrapy crawl quotes
```

Lưu dữ liệu vào JSON hoặc CSV:

```powershell
python -m scrapy crawl quotes -O output/quotes.json
python -m scrapy crawl quotes -O output/quotes.csv
```

Tùy chọn `-O` ghi đè file đầu ra nếu file đã tồn tại. Thư mục `output` sẽ được tạo khi Scrapy ghi dữ liệu.

## 4. Cấu trúc thư mục

```text
du-an7/
├── scrapy.cfg
├── requirements.txt
├── README.md
├── .gitignore
└── scrapy_demo/
    ├── __init__.py
    ├── items.py
    ├── settings.py
    ├── pipelines.py
    ├── middlewares.py
    └── spiders/
        ├── __init__.py
        └── quotes_spider.py
```

## 5. Dữ liệu đầu ra

Mỗi bản ghi gồm:
- `text`: nội dung trích dẫn.
- `author`: tên tác giả.
- `tags`: danh sách thẻ.
- `source_url`: URL trang chứa trích dẫn.

## 6. Lưu ý sử dụng có trách nhiệm

Chỉ thu thập dữ liệu từ website mà bạn được phép truy cập. Tôn trọng điều khoản sử dụng, `robots.txt`, giới hạn tốc độ và quyền riêng tư. Dự án mặc định dùng website `quotes.toscrape.com` phục vụ mục đích học tập.

## Tài liệu
- [Scrapy documentation — Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)
- [Mã nguồn Scrapy trên GitHub](https://github.com/scrapy/scrapy)
