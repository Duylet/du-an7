class ScrapyDemoPipeline:
    """Optional pipeline hook for validating scraped items."""

    def process_item(self, item, spider):
        # Keep only items with both quote text and author.
        if not item.get("text") or not item.get("author"):
            spider.logger.warning("Skipping incomplete quote item")
            from scrapy.exceptions import DropItem
            raise DropItem("Missing quote text or author")
        return item
