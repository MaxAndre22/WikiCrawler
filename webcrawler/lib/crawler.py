import hashlib
import requests
from time import sleep
from bs4 import BeautifulSoup
from lib.hermes import Hermes

class Crawler:
    def __init__(self, delay: int ,firstUrl: str, maxDepth: int, urlRules: list, messanger: Hermes) -> None:
        self.__visited = []
        self.__dataProcessor = messanger

        # Config
        self.__delay    = delay
        self.__firstUrl = firstUrl
        self.__maxDepth = maxDepth
        self.__urlRules = urlRules
    
    def __find_index(self, element: str) -> int:
        top = len(self.__visited)
        bottom = 0
        while bottom != top:
            middle = (top - bottom) // 2
            if element > self.__visited[bottom+middle]:
                bottom = bottom + middle + 1
            elif element < self.__visited[bottom+middle]:
                top = bottom + middle
            else:
                return bottom + middle
        return top

    def __insert_visited(self, url: str) -> bool:
        hash = hashlib.md5(url.encode()).hexdigest()
        index = self.__find_index(hash)
        if len(self.__visited) <= index or self.__visited[index] != hash:
            self.__visited.insert(index, hash)
            return True
        return False

    def __check_rules(self, url: str) -> bool:
        # Check rules for the url
        for rule in self.__urlRules:
            if not rule(url):
                return False
        return True
    
    def __get_root_url(self, url: str) -> str:
        segments = url.split('/')
        return f'{segments[0]}//{segments[2]}'
    
    def __process_data(self, url: str, soup: BeautifulSoup) -> None:
        self.__dataProcessor.put_message('dataProcessor', {'url': url, 'soup': soup})

    def crawl(self) -> None:
        depth = 0
        url_buffer = [[self.__firstUrl]]
        while depth < self.__maxDepth:
            url_buffer.append([])
            for url in url_buffer[depth]:
                if self.__insert_visited(url):
                    # Make the request for each url
                    response = requests.get(url)
                    html_soup = BeautifulSoup(response.content, "html.parser")
                    # Iterate over all the links on the page
                    for link in html_soup.find_all('a'):
                         if link.has_attr('href'):
                            linkUrl = link['href']
                            if linkUrl.startswith('/'):
                                linkUrl = self.__get_root_url(url) + linkUrl
                            # Check rules for each valid http link
                            if linkUrl.startswith('http') and self.__check_rules(linkUrl):
                                url_buffer[depth+1].append(linkUrl)
                    self.__process_data(url, html_soup)
                    sleep(self.__delay)
            depth += 1                  