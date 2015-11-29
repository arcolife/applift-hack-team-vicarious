df = pd.read_csv('dataset_1mb.csv')

v = df[['Latitude','Longitude']]

loc_arr = []

for i in v.values:
    loc_arr.append(geohash.encode(i[0],i[1]))
    
df.drop(['Longitude','Latitude'], axis=1, inplace=True)
