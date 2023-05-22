

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YouTube API')
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

    def __str__(self):
        return f'{self.title}({self.url})'

    def __add__(self, other):
        return int(self.subs) + int(other.subs)

    def __sub__(self, other):
        return int(self.subs) - int(other.subs)

    def __gt__(self, other):
        return int(self.subs) > int(other.subs)

    def __ge__(self, other):
        return int(self.subs) >= int(other.subs)

    def __lt__(self, other):
        return int(self.subs) < int(other.subs)

    def __le__(self, other):
        return int(self.subs) <= int(other.subs)

 def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        # print(json.dumps(channel, indent=2, ensure_ascii=False))
        return channel
