from sqlalchemy import create_engine,types
import pandas as pd
import sys

def csvToDatabase():
    csvfile = open(sys.argv[1], 'r')


    engine = create_engine('mysql+mysqlconnector://root:******@localhost:3306/Tutorial', echo=False)

    data = pd.read_csv(csvfile)
    data.to_sql(name='solarEnergy', con=engine, if_exists='replace', index=False)

    return

if __name__=='__main__':
    csvToDatabase()