from requests import Session
from re import search
from json import loads

class YT:
    def __init__(self) -> None:
        self.session = Session()
        self.regex = r"(?<=v=)[a-zA-Z0-9_-]+"
        self.ajax_url = 'https://www.y2mate.com/mates/analyzeV2/ajax'
        self.index_url = 'https://www.y2mate.com/mates/convertV2/index'
        self.error_index = 'mess'
        self.url_pointer = 'dlink'  
        
    def get_data(self, url:str):
        if (s := search(self.regex, url)): return loads(self.session.post(self.ajax_url, {'k_query': f'https://www.youtube.com/watch?v={s.group(0)}', 'k_page': 'home', 'hl': 'en', 'q_auto': 1}).text)
        return {"status":"ok", "c_status":"FAILED", "mess":"Sorry! An error has occurred."} 
        
    def get_link(self, video_id:str, file_url:str):
        s = loads(self.session.post(self.index_url, {'vid': video_id, 'k': file_url}).text)
        if s.get(self.error_index, 'YES'): return None
        return s.get(self.url_pointer)




