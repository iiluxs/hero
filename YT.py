from requests import Session
from re import search
from json import loads

class YT:
    def __init__(self, cache) -> None:
        self.cache = cache
        self.session = Session()
        self.regex = r'^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#\&\?]*).*'
        self.ajax_url = 'https://www.y2mate.com/mates/analyzeV2/ajax'
        self.index_url = 'https://www.y2mate.com/mates/convertV2/index'
        self.error_index = 'mess'
        self.url_pointer = 'dlink'  
        
    def get_data(self, url:str):
        if (id := self.get_id(url)):
            if id in self.cache: return self.cache[id]
            if (d:=loads(self.session.post(self.ajax_url, {'k_query': f'https://www.youtube.com/watch?v={id}', 'k_page': 'home', 'hl': 'en', 'q_auto': 1}).text)) and not d.get('mess'): self.cache[id] = d
            return d
        else: return {"status":"ok", "c_status":"FAILED", "mess":"Sorry! An error has occurred."} 
        
    def get_link(self, video_id:str, file_url:str):
        s = loads(self.session.post(self.index_url, {'vid': video_id, 'k': file_url}).text)
        if s.get(self.error_index, 'YES'): return None
        return s.get(self.url_pointer)

    def get_id(self, url):
        if (s := search(self.regex, url)): return s.group(7)
        else: return ''

