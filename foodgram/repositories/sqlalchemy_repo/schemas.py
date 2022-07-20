from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.schema import Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class IngredientTable(Base):
    __tablename__ = 'ingredients'

    pk = Column(Integer, primary_key=True)
    name = Column(String(200))
    measurement_unit = Column(String(200))


class TagTable(Base):
    __tablename__ = 'tags'

    pk = Column(Integer, primary_key=True)
    name = Column(String(200))
    color = Column(String(200))


recipe_tag_association_table = Table(
    'recipe_tags',
    Base.metadata,
    Column('recipe_pk', Integer, ForeignKey('recipes.pk'), primary_key=True),
    Column('tag_pk', Integer, ForeignKey('tags.pk'), primary_key=True)
)


class RecipeTable(Base):
    __tablename__ = 'recipes'

    pk = Column(Integer, primary_key=True)
    # author
    tags = relationship(
        'TagTable',
        secondary=recipe_tag_association_table
    )
    # ingredients
    name = Column(String(200))
    cooking_time = Column(Integer)
    text = Column(Text)
    pub_date = Column(DateTime)
    # path to image on server from static folder, max 200 symmbols
    image_path = Column(String(200))


# class Author
# class User roles
# class relations
# class token
