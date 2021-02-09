import scrapy

from scrapy.loader import ItemLoader
from ..items import IgeadigitalbankItem
from itemloaders.processors import TakeFirst


class IgeadigitalbankSpider(scrapy.Spider):
	name = 'igeadigitalbank'
	start_urls = ['https://www.igeadigitalbank.it/news']

	def parse(self, response):
		post_links = response.xpath('//div[@class="grid__content form-group"]')
		for post_link in post_links:
			date = post_link.xpath('.//div[@class="views-field views-field-created"]/span/text()').get()
			link = post_link.xpath('.//a[@hreflang="it"]/@href').get()
			yield response.follow(link, self.parse_post, cb_kwargs=dict(date=date))

	def parse_post(self, response, date):
		title = response.xpath('//ol[@class="breadcrumb"]/li[2]/text()').get()
		description = response.xpath('//article//text()[normalize-space() and not(ancestor::div[@class="field field--name-field-categoria field--type-entity-reference field--label-hidden field--item"])]').getall()

		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=IgeadigitalbankItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
