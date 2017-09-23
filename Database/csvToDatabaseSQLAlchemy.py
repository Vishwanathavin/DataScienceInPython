import ast
import sys

sys.path.insert(0,'../Utils/')
from convertCSVTOJSON import convertCSVtoJSON

def csvToDatabase():
    CSVdata = open(sys.argv[1],'r')
    JSONdata = convertCSVtoJSON(CSVdata)
    JSONdata = JSONdata.replace("Till March 2016","till_mar_2016").replace("March-2016 till jan 2017","mar_2016_to_jan_2017").replace("Till Jan 2017","till_jan_2017").replace('Sr.NO','SNO')

    JSONdata = ast.literal_eval(JSONdata)
    print JSONdata

    keys = ['till_jan_2017', 'State', 'SNO', 'mar_2016_to_jan_2017', 'till_mar_2016']

    try:
        import pymysql
        pymysql.install_as_MySQLdb()
    except ImportError:
        print "Error Importing python"
        pass

    import traceback
    from sqlalchemy import create_engine
    # Connect to server
    engine = create_engine("mysql://root:******@localhost:3306", encoding='utf-8')

    # engine.execute("CREATE DATABASE Tutorial")
    engine.execute("use Tutorial")

    # Delete existsing table to start afresh
    engine.execute("drop table if exists solarEnergy")
    # Create the query to create the table
    query = "create table solarEnergy (idx int not null auto_increment"

    q0 = "Insert into solarEnergy ("  # Get the list of keys and create the table
    for key in keys:
        query = query + ', %s VARCHAR(1000)' % (key)
        if keys.index(key) == 0:
            q0 = q0 + ' %s' % (key)
        else:
            q0 = q0 + ', %s' % (key)

    query = query + ', PRIMARY KEY(idx))'
    q0 = q0 + ') values '

    # Execute the query
    engine.execute(query)

    for i in range(len(JSONdata)):
        temp_list = []
        for key in keys:
            k = JSONdata[i][key]
            temp_list.append((", ".join([str(j) for j in k])) if type(k) is list else k)

        q1 = str(tuple(temp_list))
        try:
            engine.execute(q0 + q1)
        except UnicodeEncodeError:
            engine.execute(q0 + q1)
            pass


if __name__=='__main__':
    csvToDatabase()