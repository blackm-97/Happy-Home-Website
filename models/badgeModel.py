class BadgeInfo(db.Model):
    __tablename__ = 'BadgeInfo'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    imagePath = db.Column(db.Text, nullable=False, default='static/images/Cheese.png')
    difficulty = db.Column(db.Text)
    shadow = db.Column(db.Integer, nullable=False, default=0)
    gearName = db.Column(db.Text, nullable=False, default='None')
    noncanon = db.Column(db.Integer, nullable=False, default=0)
    artifact = db.Column(db.Integer, nullable=False, default=0)
    date_uploaded = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f"<BadgeInfo id={self.id} name='{self.name}'>"