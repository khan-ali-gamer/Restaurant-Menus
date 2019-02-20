from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Create import Base, Restaurant, Menu

app = Flask(__name__)
engine = create_engine('sqlite:///app.db', connect_args={'check_same_thread': False})
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

# famous=session.query(Restaurant).filter_by(name="Famous").all()
# session.delete(famous[0])
# session.commit()
# @app.route("/delete", methods=['GET', 'POST'])



@app.route("/")
def HelloWorld():
    hi=session.query(Restaurant).all()
    return render_template('home.html', items=hi)

@app.route("/Home", methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        Name=request.form.get('name')
        Address=request.form.get('address')
        Number=request.form.get('phone_no')
        myfirstres = Restaurant(name=Name, address=Address, phone_no=Number)
        session.add(myfirstres)
        session.commit()
    hi=session.query(Restaurant).all()
    return render_template('home.html', items=hi)

@app.route("/Del", methods=['GET', 'POST'])
def del_res():
    if (request.method == 'POST'):
        name = request.form.get('name')
        myfirstres = session.query(Restaurant).filter_by(name=name).one()
        myfirstitem=session.query(Menu).filter_by(restaurant_id=myfirstres.id)
        for i in myfirstitem:
            session.delete(i)
        session.delete(myfirstres)
        session.commit()
    hi = session.query(Restaurant).all()
    return render_template("home.html", items=hi)

@app.route("/restaurants/<int:restaurant_id>/", methods=['GET', 'POST'])
def AddItems(restaurant_id):
    if request.method=='POST':
        myfirstres=session.query(Restaurant).filter_by(id=restaurant_id).one()
        Name=request.form.get('name')
        Price=request.form.get('price')
        myfirstitem = Menu(name=Name, price=Price, restaurant=myfirstres)
        session.add(myfirstitem)
        session.commit()
    item = session.query(Menu).filter_by(restaurant_id=restaurant_id).all()
    return render_template('MenuItem.html', items=item, id=restaurant_id)

@app.route("/del_item<int:restaurant_id>/", methods=['GET', 'POST'])
def del_item(restaurant_id):
    if (request.method == 'POST'):
        name = request.form.get('name')
        myfirstitem = session.query(Menu).filter_by(name=name).one()
        session.delete(myfirstitem)
        session.commit()
    item = session.query(Menu).filter_by(restaurant_id=restaurant_id).all()
    return render_template('MenuItem.html', items=item, id=restaurant_id)

if __name__=='__main__':
    app.run()