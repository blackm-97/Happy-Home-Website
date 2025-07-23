def fanartInfoMaker(db):

    class Fanart(db.Model):
        __tablename__ = 'fanartInfo'

        id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
        author = db.Column(db.Text, nullable = True)
        name = db.Column(db.Text, nullable = True)
        imagePath = db.Column(db.Text, nullable = True)


        def __repr__(self):
            return {f"<FanartInfo displayName='{self.name}'>"}
        
    return Fanart