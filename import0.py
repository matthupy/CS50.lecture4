import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

try:
    engine = create_engine(os.getenv("DATABASE_URL"))
except:
    engine = create_engine("postgres://postgres:admin@localhost:5432/lecture3")
    
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
            {"origin": origin, "destination": destination, "duration": duration})
        print(f"Added flight from {origin} to {destination} lasting {duration}.")
    db.commit()

if __name__ == "__main__":
    main()