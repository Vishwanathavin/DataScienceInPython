import pandas as pd
debug = True
#
# inpFile = pd.read_csv('../Data/solarEnergy.csv')
#
# # Get all the columns
# col = inpFile.columns.values
# # if debug: print col
#
# # Get all the rows with condition
# row = inpFile[inpFile['Till March 2016'].values ==0.0].State
#
# # if debug: print row
#
# # Drop rows of selected columns has Nan
# inpFile=inpFile['Till March 2016'and'March-2016 till jan 2017'and'Till Jan 2017'].dropna()



country=pd.read_csv('../Data/inputcountry.csv')
names = pd.read_csv('../Data/inputNames.csv')

# isin
commonNames =names[names.Name.isin(country.Name)]['Name']
uncommonNames =country[~country.Name.isin(names.Name)]['Name']


# Concantenate
names=pd.concat([names.Name,uncommonNames],axis=0)

# merge

# rename

# fill na

# apply ( lambda)

# iloc row