import scrapy
import urllib
from harriscounty.items import HarriscountyItem


class QuotesSpider(scrapy.Spider):
    name = "asites"
    start_urls = [
        'http://hcps.harriscountytx.gov/',
    ]
    allowed_domains = ['harriscountytx.gov']

    def parse(self, response):

        doc = HarriscountyItem()
        # if not HTMl, parse the URL as text
        if response.headers.get("content-type", "").lower() != b'text/html; charset=utf-8':
            doc['url'] = response.url
            doc['text'] = urllib.parse.unquote(response.url)
            yield doc
        else:
            a = '. '.join([x.rstrip() for x in response.xpath("//body//text()[not(ancestor::script)]").extract() if len(x.rstrip()) > 0 ][3:-10]).replace('\r','').replace('\n','').replace('\t','').replace('  ','')
            doc['url'] = response.url
            doc['text'] = a
            yield doc

            a_selectors = response.xpath("//a")
            for selector in a_selectors:
                # Extract the link href
                link = selector.xpath("@href").extract_first()
                if link:
                    # print('--'*25)
                    if bool(urllib.parse.urlsplit(link).netloc):
                        yield scrapy.Request(link, callback=self.parse)
                    else:
                        link = response.urljoin(link)
                        yield scrapy.Request(link, callback=self.parse, dont_filter=False)
