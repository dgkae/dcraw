# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.TextItem'

ITEM_PIPELINES = {'dirbot.pipelines.SaveTextPipeline':1}
