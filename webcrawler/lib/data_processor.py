from bs4 import BeautifulSoup

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

import json

def pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:         
        return None


class DataProcessor:
    def __init__(self) -> None:
        self.lemmatizer = WordNetLemmatizer()
        self.saved_pages = 0
        self.file = open('crowler_output.json', 'w')
        self.file.write('[')

    def __get_images(self, soup: BeautifulSoup) -> None:
        images = []
        for image in soup.find_all('img'):
            image_data = {
                'src': image['src'] if image.has_attr('src') else '',
                'alt': image['alt'] if image.has_attr('alt') else ''
            }
            if image_data['alt'] != '':
                image_data['lemmatized-alt'] = self.__lemmatize_text(image_data['alt'])
            images.append(image_data)
        return images
    
    def __get_title(self, soup: BeautifulSoup) -> None:
        title = soup.find('h1', {"id": 'firstHeading'})
        return title
    
    # TODO: Process the data to get only the text
    def __get_titles(self, soup: BeautifulSoup) -> None:
        titles = []
        titles.append(soup.find('h1', {"id": 'firstHeading'}).getText())
        for h2 in soup.find_all('h2'):
            for title in soup.find_all("span", {"class": "mw-headline"}):
                titles.append({
                    'title': title.getText(),
                    'lemmatized-title': self.__lemmatize_text(title.getText())
                })
        return titles
    
    # TODO: Process the data to get only the text
    def __get_sub_titles(self, soup: BeautifulSoup) -> None:
        subtitles = []
        for h3 in soup.find_all('h3'):
            for subtitle in soup.find_all("span", {"class": "mw-headline"}):
                subtitles.append({
                    'sub-title': subtitle.getText(),
                    'lemmatized-sub-title': self.__lemmatize_text(subtitle.getText())
                })
        for h4 in soup.find_all('h4'):
            for subtitle in soup.find_all("span", {"class": "mw-headline"}):
                subtitles.append({
                    'sub-title': subtitle.getText(),
                    'lemmatized-sub-title': self.__lemmatize_text(subtitle.getText())
                })
        return subtitles
    
    # TODO: Todo
    def __get_page_text(self, soup: BeautifulSoup) -> str:
        text = { 'text': '' }
        for text_block in soup.find_all(['p', 'blockquote']):
            text['text'] += text_block.getText()
        text['lemmatized-text'] = self.__lemmatize_text(text['text'])
        return text
    
    def __get_page_text_by_tag(self, soup: BeautifulSoup) -> list:
        viable = ['h1', 'cite', 'h3', 'h2', 'li', 'a', 'p', 'h4', 'span']
        tags = set(tag.name for tag in soup.find_all())
        text = {}
        for tag in tags:
            if tag in viable:
                text[tag] = { 'text': '' }
                for text_block in soup.find_all(tag):
                    text[tag]['text'] += ' ' + text_block.getText()
                text[tag]['lemmatized-text'] = self.__lemmatize_text(text[tag]['text'])
        return text

    def __get_references(self, soup: BeautifulSoup) -> None:
        ref_list = soup.find("div", {"class": "reflist"})
        references = []
        if ref_list == None:
            return references
        for reference in ref_list.find_all('li'):
            cite = reference.find('cite')
            if cite:
                a = cite.find('a')
                if a:
                    references.append({
                        'text': a.getText(),
                        'lemmatized-text': self.__lemmatize_text(a.getText()),
                        'href': a['href'] if not a['href'].startswith('/') else 'https://en.wikipedia.org'+a['href']
                    })
        return references

    def __save_on_file(self, data: dict) -> None:
        json_str = json.dumps(data, indent = 4)
        if self.saved_pages != 0:
            json_str = ','+json_str
        self.file.write(json_str)
        self.saved_pages += 1
    
    def close_file(self) -> None:
        self.file.write(']')
        self.file.close()

    def __lemmatize_text(self, text: str) -> str:
        pos_tagged = nltk.pos_tag(nltk.word_tokenize(text))
        pos_tagged = [(word.lower(), pos_tagger(tag)) for word, tag in pos_tagged]
        lemmatized_text = []
        for word, tag in pos_tagged:
            if tag is None:
                lemmatized_text.append(word)
            else:
                lemmatized_text.append(self.lemmatizer.lemmatize(word, tag))
        lemmatized_text = " ".join(lemmatized_text)
        return lemmatized_text

    def process_page(self, data) -> None:
        soup = data['soup'].find('div', {"id": 'content'})
        data = {
            'url': data['url'],
            'images': self.__get_images(soup),
            'titles': self.__get_titles(soup),
            'subtitles': self.__get_sub_titles(soup),
            'page_text': self.__get_page_text(soup),
            'page_text_by_tag': self.__get_page_text_by_tag(soup),
            'references': self.__get_references(soup)
        }
        self.__save_on_file(data)
        

#
#lemmatizer.lemmatize("rocks")