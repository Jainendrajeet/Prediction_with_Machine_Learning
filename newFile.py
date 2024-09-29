import pandas as pd
df = pd.read_csv('survey_results_public.csv',index_col='ResponseId')
schem_df=pd.read_csv('survey_results_schema.csv',index_col='qname')
pd.set_option('display.max_rows',10)
pd.set_option('display.max_columns',10)
print(df)
print(schem_df)
df.sort_values(by='Country',inplace=True)
print(df['Country'].head(200))
print(df['ConvertedCompYearly'].nlargest(10))
print(df.nlargest(10,'ConvertedCompYearly'))
print(df['ConvertedCompYearly'].median())
print(df.median())
print(df.describe())
print(df['ConvertedCompYearly'].value_counts(normalize=True))

# If we want to see the data from a specific country
print(df['Country'].value_counts())
countrygrp=df.groupby(['Country'])
print(countrygrp['TechList'].value_counts().loc['India'])
print(countrygrp['ConvertedCompYearly'].agg(['median','mean']))
print(countrygrp['LanguageHaveWorkedWith'])
print(countrygrp['LanguageHaveWorkedWith'].apply(lambda x : x.str.contains('Python').sum()))
print(countrygrp['LanguageHaveWorkedWith'].apply(lambda x : x.str.contains('Python').sum()*100/x.count()))
print(df.shape)
print(df.head(10))
# print(df.info())
print(schem_df.head(10))#df.tail()
print(df.columns)
print(schem_df.loc['Knowledge_8','question'])# The row , column NN 

print(df.loc[0:2,'Age':'EdLevel'])#Last one is inclusive 

 # Lecture 2

people={
    "first": ["Jai","Ram","Aranu"],
    "second":["Gupta","ji","gupta"],
    "email": ["Jai@gmail.com","Ramji@gmail.com","Ranu@gmail.com"]    
}
df1=pd.DataFrame(people)

print(df1)
print(df1['email'])#df.email but not prefer 
print(df1[['second','email']])
print(df1.columns)
print(df1.iloc[[0,1],[2]])
print(df1.loc[[0,1],['email']])


# #         Lecture    3
df1.set_index('email',inplace=True)
print(df1.index)
print(df1.loc['Jai@gmail.com','second'])# Now the indexing like 0 1 2 3 does not work instead of that 
# in iloc inddexing like 0 1 2 3 still works 


#            Lecture 4

filttt= ((df1['second']=="Gupta") | (df1['second']=="gupta")) # & for AND and | for OR
print(df1.loc[~filttt,'email']) # ~ for the opposite 
countries=["US","India","UK"]


#                                   Lecture 5
#We can chnge the column names by 
df1.columns=["first_name","last_name","Email"]
df1.columns=[x.lower() for x in df1.columns]
df1.columns=df1.columns.str.replace(' ','_')
df1.rename(columns={'first_name':'first','last_name':'last'},inplace=True)
df1.loc[2]=['Ramu','Sharma','Ramu@gmail.com']
df1.loc[2,['last']]=['Gupta']
# If You want to apply a filter and want to change the fvalue of any object ayou can jkust use the .loc
print(df1)
df1['email'].apply(len)
def update_email(email):
    return email.upper()
df1['email']=df1['email'].apply(update_email)
print(df1.apply(pd.Series.max))# lexicographic order 
print(df1.applymap(len))# Apply on the all the DATAS
#While Using map if You dont map any data to other one then the data will be NaN
# So it is bettter to use replace in place of map while dealing with a bigger data nad Uou dont want to change all the values of the data 

#                                  Lecture 6
df1['full_name']=df1['first']+' '+ df1['last']
df1.drop(columns=['first','last'],inplace=True)
df1[['first','last']]=df1['full_name'].str.split(' ',expand=True)
df1.append({'first':'Ranu'},ignore_index=True)
people={
    "first": ["Jain","RamuShyam"],
    "second":["Sharma","JI"],
    "email": ["Jai@gmail.com","Ramji@gmail.com"]    
}
df2=pd.DataFrame(people)
df1=df1.append(df2,ignore_index=True,sort=False)
df1=df1.drop(index=2)
df1=df1.sort_values(by=['last','first'],ascending=[False,False])
print(df1)
