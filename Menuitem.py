from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Create import Base, Restaurant, Menu

app = Flask(__name__)
engine = create_engine('sqlite:///app.db', connect_args={'check_same_thread': False})
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()


@app.route("/")
def HelloWorld():
    hi=session.query(Restaurant).first()
    item=session.query(Menu).filter_by(restaurant_id=hi.id)
    out=''
    for i in item:
        out+=str(i.id)
        out+="<br>"
        out+=i.name
        out+="<br>"
        out+=str(i.price)
        out+="<br>"
        out+=str(i.restaurant_id)
    return out

if __name__=='__main__':
    app.run()