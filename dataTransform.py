import pandas as pd
#import pandas_usaddress

class dataTransform:
  def __init__(self,df):
    self.df = df


  def myfunc(self):
    # 1st Fill the numerical missing values with the mean of each row
    self.df = self.df.fillna(self.df.mean())
    # Impute the categorical with the most frequent value
    df2 = self.df.apply(lambda x: x.fillna(x.value_counts().index[0]))
    #Standardize date-time field with a given format
    df2['Clean_Date'] = df2.Date.apply(lambda x: pd.to_datetime(x).strftime('%d/%m/%Y %H:%M'))
    #df2.drop(columns=['Name'])
    #Rounding values as configured
    df2.round(3)
    return df2

#Test

df = pd.read_csv("Pokemon.csv")
print(df)
p1 = dataTransform(df)
df = p1.myfunc()
print(df)
df.to_csv('output.csv', header=False, index=False)