from tasks.database import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<Task {self.id} - {self.title} / {self.status}>'
    