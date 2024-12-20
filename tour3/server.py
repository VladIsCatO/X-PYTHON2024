"""Server side, where code is encoding all the line in one symbol
the principle of this code is to encode all the line in one symbol, and then send it to the client
that will add it to database, example:
'Hello WoRlD' : �

and like this for every file.
also it will check if there's already phrases like that in database, if yes, 
it will not add it, but give the symbol from database.

if "OverflowError: Python int too large to convert to C int" error:
it will add another byte of info (it will look like: 'Hello WoRlD' : ��)
"""

import socket
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column
from multiprocessing import Process

engine = create_engine("sqlite:///tour3/default.db", echo=False)

Session = sessionmaker(bind=engine)

SERVER_IP = (
    "localhost"  # after, IF it will be in big productions will be changed to ip.
)
MAX = 55295  # Max number for chr() or unicode characters
NW = [
    " ",
    "",
    "\n",
    """
""",
]  # Means NOT WORKING


class Base(DeclarativeBase):
    """Base functions for db"""

    def createdb(self):
        """Create database"""
        Base.metadata.create_all(engine)

    def dropdb(self):
        """dropping database"""
        Base.metadata.drop_all(engine)

    def new_phrase(self, string, symbol):
        """adding new record to Database"""
        with Session() as session:
            new_phrase = Database(string=string, symbol=symbol)
            session.add(new_phrase)
            session.commit()

    def remove_from_lib(self, phrase):  # Only for me, will not be used in app
        """Only development function to delete a record from Database"""
        with Session() as session:
            item = session.query(Database).filter_by(string=phrase).first()
            session.delete(item)
            session.commit()

    def select_by_phrase(self, phrase):
        """getting a record by line"""
        with Session() as session:
            return session.query(Database).filter_by(string=phrase).first()

    def select_by_symbol(self, symbol):
        """getting a record by symbol"""
        with Session() as session:
            return session.query(Database).filter_by(symbol=symbol).first()

    def get_symbol(self):
        """gets the id for chr() function. (just last id from database)"""
        with Session() as session:
            return session.query(Database).order_by(Database.id.desc()).first()


class Database(Base):
    """Database table"""

    __tablename__ = "database"
    id: Mapped[int] = mapped_column(primary_key=True)
    string: Mapped[str] = mapped_column(
        String(999999999999999999999999999999999999 ^ 2)
    )
    symbol: Mapped[str] = mapped_column(String(1))


class Server:
    """Server Class"""

    def __init__(self):
        self.db = Base()
        self.db.createdb()

    def main(self):
        """Main function: connecting with user and giving information from functions to him."""
        sock = socket.socket()
        sock.bind(("", 9090))
        while True:
            sock.listen(1)
            conn, addr = sock.accept()
            print("connected:", addr)
            all_ = conn.recv(1024).decode().split("|")
            mode = all_.pop(0)
            data = str()
            for i in all_:
                data += i
            if mode == "encode":
                conn.send(self.encode(data))
            elif mode == "decode":
                conn.send(self.decode(data))
            conn.close()

    def encode(self, data: str) -> bytes:
        """function made for encoding user's data and giving it back, but encoded."""
        before = (
            str()
        )  # if there's more than one symbol to put, it will be added to this var
        final = str()
        symbol_id = self.db.get_symbol()
        data = data.split("\n")
        if symbol_id is None:
            symbol_id = 1
            count = 0
        else:
            symbol_id = symbol_id.id + 1
            count = int(symbol_id / MAX)
            symbol_id = symbol_id % MAX

        for i in data:
            if (
                chr(symbol_id) in NW or symbol_id == 13
            ):  # without this there will be error while decoding
                symbol_id = self.encoding_checker(symbol_id + 1)
            if self.db.select_by_phrase(i) is not None:
                final += self.db.select_by_phrase(i).symbol + "\n"
                continue
            try:
                if count != 0:
                    before = chr(count)
                    final += before
                encoding = chr(symbol_id)
            except UnicodeError:
                count += 1
            self.db.new_phrase(i, encoding)
            symbol_id += 1
            final += encoding + "\n"
        return final.encode()

    def encoding_checker(self, symbol_id: int) -> int:
        """function that checks if symbol is something kinda empty..? idk how to explain.
        in any case, without it decoding will not work because of impossibleness
        of getting phrase from db"""
        if chr(symbol_id) in NW:
            return self.encoding_checker(symbol_id + 1)
        return symbol_id

    def decode(self, data: str) -> bytes:
        """function made for decoding info and returning it back to the user."""
        finish = str()
        for i in data:
            try:
                finish += self.db.select_by_symbol(i).string + "\n"
            except AttributeError:
                pass
        return finish.encode()


if __name__ == "__main__":
    server = Server()
    server.main()
