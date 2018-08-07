from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article( name , topic , rating):
	adding_to_db =Knowledge(
		name=name,
		topic = topic,
		rating=rating)
	session.add(adding_to_db)
	session.commit()

#add_article( "wadi", "name", 5 )		
def query_all_articles():
	knowledge = session.query(
		Knowledge).all()
	return knowledge
print (query_all_articles())		


def query_article_by_topic(topic):
	knowledge = session.query(
		Knowledge).filter_by(topic = topic).all()

	return knowledge
add_article("william", "wiwi", 10)
print("!!!")
print (query_article_by_topic("wiwi"))



def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
