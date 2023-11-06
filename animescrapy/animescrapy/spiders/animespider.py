import scrapy
import json
from animescrapy.items import AnimeScrapyItem 

class AnimespiderSpider(scrapy.Spider):
    name = "animespider"
    start_urls = ["https://myanimelist.net/anime/ranking.json?offset=1&type=all"]
    total_data = 25350  # Tentukan jumlah data yang Anda inginkan

    def parse(self, response):
        data = json.loads(response.body)

        for item_data in data:
            item = AnimeScrapyItem()
            item['id'] = item_data['id']
            item['rank'] = item_data['rank']
            item['title'] = item_data['title']
            item['url'] = item_data['url']
            item['image'] = item_data['image']
            item['listStatus'] = item_data['listStatus']
            item['mediaType'] = item_data['mediaType']
            item['numEpisodes'] = item_data['numEpisodes']
            item['score'] = item_data['score']
            item['numListUsers'] = item_data['numListUsers']
            item['status'] = item_data['status']
            yield item

        # Lakukan pengambilan data berikutnya (offset+30) jika masih ada dan belum mencapai total_data
        last_rank = int(data[-1]['rank'])
        next_offset = last_rank + 1  # Gunakan nilai dari field terakhir untuk menentukan offset selanjutnya
        if next_offset <= self.total_data:
            next_url = f'https://myanimelist.net/anime/ranking.json?offset={next_offset}&type=all'
            yield scrapy.Request(url=next_url, callback=self.parse)
