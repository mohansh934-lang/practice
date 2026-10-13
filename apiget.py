import pandas as pd

# df = pd.read_csv("employee_details.csv", encoding="utf-8").head(5) #nrows=5: for 5 uper ki rows lene ke liye, #sample(5) random 5 rows lene ke liye 

# print(df)

# # head(10) starting ki 5 rows by deafault 5
# # tail(10) last ki 10 rows or by default 5 rows

# --- display the infoe ---

df =pd.read_csv("movies_dataset_final.csv", encoding="utf-8")

# print(df.info())  #this shows the info of the dataset

print(df.describe())



