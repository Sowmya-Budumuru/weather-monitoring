# database.py
from sqlalchemy import create_engine, Column, String, Float, Date, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_URI
import datetime

#from your_database_setup import WeatherSummary
#from your_database_setup import engine

Base = declarative_base()
engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)
session = Session()

class WeatherSummary(Base):
    __tablename__ = 'weather_summary'
    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    avg_temp = Column(Float, nullable=False)
    max_temp = Column(Float, nullable=False)
    min_temp = Column(Float, nullable=False)
    dominant_condition = Column(String, nullable=False)

def create_database():
    Base.metadata.create_all(engine)

def save_to_database(daily_summary):
    # Create a database engine
    engine = create_engine('sqlite:///weather_data.db')  # Update the connection string as needed
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Iterate over the DataFrame rows and save to the database
        for _, row in daily_summary.iterrows():
            weather_entry = WeatherSummary(
                city=row['city'],
                date=row['date'],  # Make sure this is a date object
                avg_temp=row['avg_temp'],
                max_temp=row['max_temp'],
                min_temp=row['min_temp'],
                dominant_condition=row['dominant_condition']
            )
            session.add(weather_entry)
        
        session.commit()  # Commit the transaction
    except Exception as e:
        session.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
    finally:
        session.close()  