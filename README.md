# Du an 7 - Scrapy Web Scraping Demo

Du an Python minh hoa cach dung [Scrapy](https://github.com/scrapy/scrapy) de thu thap du lieu tu website demo `quotes.toscrape.com`.

## Chuc nang
- Thu thap noi dung trich dan, tac gia va the.
- Tu dong di qua cac trang tiep theo.
- Xuat du lieu ra JSON hoac CSV.
- Cau hinh toc do crawl than thien voi website demo.

## 1. Yeu cau
- Python 3.10 tro len (khuyen nghi Python 3.11-3.13).
- VS Code va Python extension.
- Ket noi Internet.

## 2. Cai dat tren Windows / VS Code

Mo terminal tai thu muc du an:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Neu PowerShell khong cho kich hoat moi truong ao, co the dung truc tiep:
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m scrapy list
```

## 3. Chay spider

Chay tu thu muc co file `scrapy.cfg`:

```powershell
python -m scrapy list
python -m scrapy crawl quotes
```

Luu du lieu:
```powershell
python -m scrapy crawl quotes -O output/quotes.json
python -m scrapy crawl quotes -O output/quotes.csv
```

Tuy chon `-O` ghi de file dau ra neu da ton tai. Thu muc `output` duoc tao tu dong boi spider.

## 4. Cau truc thu muc

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

## 5. Du lieu dau ra
Moi ban ghi gom:
- `text`: noi dung trich dan.
- `author`: ten tac gia.
- `tags`: danh sach the.
- `source_url`: URL trang thu thap.

## 6. Luu y
Chi thu thap du lieu tren website ban co quyen truy cap. Ton trong dieu khoan su dung, robots.txt, gioi han toc do va quyen rieng tu. Du an mac dinh dung website `quotes.toscrape.com` duoc tao cho muc dich hoc tap.

## Tai lieu
- [Scrapy documentation - Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)
- [Scrapy GitHub](https://github.com/scrapy/scrapy)
