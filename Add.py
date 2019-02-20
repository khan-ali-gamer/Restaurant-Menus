from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Create import Base, Restaurant, Menu


engine = create_engine('sqlite:///app.db', connect_args={'check_same_thread': False})
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

myfirstres = session.query(Restaurant).filter_by(name='APJ Mess').one()
# session.add(myfirstres)
# session.commit()

myfirstitem = session.query(Menu).filter_by(restaurant_id=myfirstres.id).all()
# session.delete(myfirstitem[1])
# session.commit()

