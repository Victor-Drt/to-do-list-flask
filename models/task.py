class Task:
    def __init__(self, title, status):
        self.title = title
        self.status = status
        
    def __str__(self):
        return f'{self.title} - {self.status}'