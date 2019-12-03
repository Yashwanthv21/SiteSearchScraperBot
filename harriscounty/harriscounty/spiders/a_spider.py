import scrapy


class QuotesSpider(scrapy.Spider):
    name = "asites"
    start_urls = [
        'http://hcps.harriscountytx.gov/',
    ]
    # domain = 'hcps.harriscountytx.gov'

    def parse(self, response):
        # print(response.get(), "this is response")
        # print(''.join(response.xpath("//body//text()").extract()).strip())

        print(response.url)
        a = ' '.join([x.rstrip() for x in response.xpath("//body//text()[not(ancestor::script)]").extract()]).replace('\n','').replace('\t','').replace('  ','')
        print(len(a))
        print(response.xpath("//body//text()[not(ancestor::script)]").extract())
        with open('test.txt','w') as f:
            f.write(a)
        # Get all the <a> tags
        a_selectors = response.xpath("//a")
        print('*'*20, a_selectors, '*'*20)
        # Loop on each tag
        for selector in a_selectors:
            # Extract the link text
            text = ''.join(selector.xpath(".//text()").extract()).strip()

            # Extract the link href
            link = selector.xpath("@href").extract_first()
            # Create a new Request object
            print(text, link,'\n')

            # request = response.follow(link, callback=self.parse)
            # Return it thanks to a generator
            # yield request
            # print(text, link, request)

        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').get(),
        #         'author': quote.css('small.author::text').get(),
        #         'tags': quote.css('div.tags a.tag::text').getall(),
        #     }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)