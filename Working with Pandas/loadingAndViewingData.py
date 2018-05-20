'''
Loading and Viewing data with Pandas

'''
import pandas as pd #pd referring panda dataframe

#csv_path='https://ibm.box.com/shared/static/keo2qz0bvh4iu6gf5qjq4vdrkt67bvvb.csv'
csv_path='resource/data/top_selling_albums.csv'
df = pd.read_csv(csv_path) #use read_excel to read excel file

df.head() #To examine first five rows of dataframe

#We can access the column "Length" and assign it to new dataframe
x=df[['Length']]

#Assign value to a series, think series as a 1-D dataframe in pandas, use one bracket
x=df['length']

#For multiple columns
x=df[['Artist','Length','Genre']]

#Access cell data
df.iloc[0,0] #First first row and first column

df.iloc[1,0] #second row first column

#Access cell data using column name
df.loc[0,'Artist']

df.loc[0,'Released']

#Perform slicing using both index and name of the column
df.iloc[0:2, 0:3]

df.loc[0:2, 'Artist':'Released']
