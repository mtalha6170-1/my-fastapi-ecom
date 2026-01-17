from sqlalchemy.orm import session 
from .import models, schemas


def get_products(db: Session):
    return db.query(models.Product).all()

def create_product(db:Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product