

from wordcloud import WordCloud
from bs4 import BeautifulSoup
import requests
from os import path


def get_lyrics(wiki_url, tag, tag_name):
    """ Takes a url for a lyrics page of lyrics.wikia.com, a tag and a tag name searches for that tag
    in the urls HTML that has the tag_name passed in. Returns the song lyrics found.
    :param wiki_url: string lyrics.wikia lyrics url e.g. http://lyrics.wikia.com/wiki/The_Beatles:Girl.
    :param tag: string HTML tag to look for lyrics in e.g. "div"
    :param tag_name: string name of HTML tag to look for lyrics in e.g. lyricbox
    :return: string song lyrics
    """
    response = requests.get(wiki_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if soup.find_all(tag, tag_name):
        return soup[0].text


def create_wordcloud(wiki_url, file_name, tag, tag_name):
    """ Takes a url for a lyrics page of lyrics.wikia.com and creates a wordcloud from the lyrics.
    :param wiki_url: string lyrics.wikia lyrics url e.g. http://lyrics.wikia.com/wiki/The_Beatles:Girl.
    """
    lyrics = get_lyrics(wiki_url, tag, tag_name)
    wordcloud = WordCloud().generate(lyrics)
    image = wordcloud.to_image()
    image.show()
    image.save(path.dirname(__file__) + '/wordcloud.jpg')


# create_wordcloud('http://lyrics.wikia.com/wiki/The_Beatles:Lucy_In_The_Sky_With_Diamonds', 'word_cloud.jpg', 'div',
#                  'lyricbox')

