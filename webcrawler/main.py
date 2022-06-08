import json
import time
from threading import Thread
from lib.crawler import Crawler
from lib.hermes import Hermes
from lib.data_processor import DataProcessor


def url_limiter(url):
    return url.startswith('https://en.wikipedia.org/wiki')

if __name__ == '__main__':
    # Load configuration
    config_file = open('config.json', 'r')
    config = json.load(config_file)
    config_file.close()

    # Hermes setup
    hermes = Hermes()

    # DataProcessor setup
    dataProcessor = DataProcessor()
    hermes.register_service('dataProcessor', dataProcessor.process_page)

    # Crawler setup
    firstUrl = 'https://en.wikipedia.org/wiki/Costa_Rica'
    rules = [url_limiter]
    crawler = Crawler(config['crawler']['delay'], firstUrl, config['crawler']['maxDepth'], rules, hermes)

    # Threads
    crawler_thread = Thread(target=crawler.crawl)
    crawler_thread.daemon = True

    hermes_thread = Thread(target=hermes.start_work)
    hermes_thread.daemon = True
    # Start Threads
    crawler_thread.start()
    hermes_thread.start()
    
    # Keep the main thread alive
    try:
        while True: time.sleep(1)
    finally:
        dataProcessor.close_file()
        



    