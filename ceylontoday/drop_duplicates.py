# Loaded variable 'df' from URI: /Users/whanerendo/Documents/Whaner/Omdena/Omdena_BSC_SriLanka/ceylontoday/news-english-ceylon_today-whaner_endo.csv
import pandas as pd
df = pd.read_csv(r'/Users/whanerendo/Documents/Whaner/Omdena/Omdena_BSC_SriLanka/ceylontoday/news-english-ceylon_today-whaner_endo.csv')

# Drop duplicate rows across all columns
df = df.drop_duplicates()

df.to_csv('news-english-ceylon_today-whaner_endo.csv', index=False, encoding='utf-8')
