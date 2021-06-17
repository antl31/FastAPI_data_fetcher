from sqlalchemy.orm import Session


class BaseDAO:
    def __init__(self, db: Session):
        self.db = db
        self.model = None

    def commit(self):
        try:
            self.db.commit()
        except:
            self.db.rollback()
            raise

    def get(self, id: int):
        return self.db.query(self.model).get(id)

    def get_by_id(self, input_id):
        return self.db.query(self.model).filter(self.model.id == input_id)

    def get_by(self, **kwargs):
        q = self.db.query(self.model)
        for key, value in kwargs.items():
            attr = getattr(self.model, key)
            q = q.filter(attr == value)
        return q
