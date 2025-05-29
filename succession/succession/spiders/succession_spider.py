from pathlib import Path

import scrapy
from traitlets import default


class SuccessorsSpider(scrapy.Spider):
    name = "successors"

    async def start(self):
        urls = [
            # "https://www.catholic-hierarchy.org/bishop/bzimon.html"
            "https://www.catholic-hierarchy.org/bishop/brebi.html"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={"consecrator": "", "level": 0})

    def parse(self, response):
        
        #consecrator = response.xpath("//*[text() = 'Principal Consecrator:']//a[1]/@href").get(default="").split(".")[0]
        consecrator = response.meta.get("consecrator")
        
        level = response.meta.get("level")
        
        b_id = response.url.split("/")[-1].split(".")[0]
        
        yield {
            "id": b_id,
            "name": "".join(response.xpath("//h1[1]//text()").getall()),
            "death": response.xpath("""//*[@itemprop="deathDate"]/text()""").get(default=""),
            #"mdata": response.xpath("""//section[@id="mdata"]""").get(default=""),
            "consecrator": consecrator,
            "level": level,
        }
        for succ in response.xpath("//*[text() = 'Principal Consecrator of:']//a[1]/@href").getall():
            yield response.follow(succ, self.parse, meta={"consecrator": b_id, "level": level+1})