BOT_NAME = "scrapy_demo"

SPIDER_MODULES = ["scrapy_demo.spiders"]
NEWSPIDER_MODULE = "scrapy_demo.spiders"

# Identify the crawler clearly and crawl politely.
USER_AGENT = "du-an7-scrapy-learning-project (+https://github.com/Duylet/du-an7)"
ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 8
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1.0
DOWNLOAD_TIMEOUT = 20

ITEM_PIPELINES = {
    "scrapy_demo.pipelines.ScrapyDemoPipeline": 300,
}

FEED_EXPORT_ENCODING = "utf-8"
LOG_LEVEL = "INFO"

# Keep output files outside source code.
FEEDS = {
    "output/quotes-%(time)s.json": {
        "format": "json",
        "encoding": "utf8",
        "overwrite": False,
    },
}
