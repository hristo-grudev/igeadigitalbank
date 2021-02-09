BOT_NAME = 'igeadigitalbank'

SPIDER_MODULES = ['igeadigitalbank.spiders']
NEWSPIDER_MODULE = 'igeadigitalbank.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'igeadigitalbank.pipelines.IgeadigitalbankPipeline': 100,

}