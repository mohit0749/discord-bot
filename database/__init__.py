from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

host = "postgres://vhxxdvqxcecghl:4ec712700a41971800f10477af330f2ac9a7d0de3bbaa70b8250f1d502eb486d@ec2-52-203-165-126.compute-1.amazonaws.com:5432/d2phr5236osibr"
engine = create_engine(host, echo=True)
Session = scoped_session(sessionmaker(bind=engine))
