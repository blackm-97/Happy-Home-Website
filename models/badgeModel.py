
from datetime import datetime

def badgeInfoMaker(db):

    class BadgeInfo(db.Model):
        __tablename__ = 'BadgeInfo'

        id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
        displayName = db.Column(db.Text, nullable=False)
        description = db.Column(db.Text, nullable=False)
        imagePath = db.Column(db.Text, nullable=False, default='static/images/Cheese.webp')
        difficultyVal = db.Column(db.Text, default=0)
        shadow = db.Column(db.Integer, nullable=False, default=0)
        gearName = db.Column(db.Text, nullable=False, default='None')
        noncanon = db.Column(db.Integer, nullable=False, default=0)
        artifact = db.Column(db.Integer, nullable=False, default=0)
        date_uploaded = db.Column(db.DateTime, nullable=False, default=datetime.now)
        order = db.Column(db.Integer)
        collected = False
        awardedDate = "N/A"


        def __repr__(self):
            return {f"<BadgeInfo id={self.id} displayName='{self.name}'>"}
        
        def to_dict(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        
    return BadgeInfo