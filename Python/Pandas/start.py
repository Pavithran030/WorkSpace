import pandas as pd 
import re
re=pd.read_csv('Excel Files\\pokemon_data.csv')

# to read a data from the top
    #print(re.head(3))


# to read a data from the bottm
    #print(re.tail(1))


# to print the columns headings
    #print(re.columns)


#to print the specific columns
    #print(re['Speed'])


#to print the each rows 
    #print(re.iloc[0:3])


#to read the specific rows and column
    #print(re.iloc[0,4]) 


#to print each row in a step by step
    # for i,ro in re.iterrows():
    #     if i<=10:
    #         print(ro['Type 1'])


#to print the specific row based on the specific condition

    #print(re.loc[re['Generation']==1])


#to print the sort values

    # print(re.sort_values('Type 1',ascending=False))

    # print(re.sort_values(['Type 1','Generation'],ascending=[0,0]))


#to remove the specific column
    # re=re.drop(columns=['Type 1','Speed','Generation'])
    # re=re.head(5)
    # print(re.sort_values('Type 2',ascending=True))


#to sum a specific range of values

    # re['SUM']=re.iloc[0:5,4:7].sum(axis=1)
    # print(re.head(3))


#to reorder the column of the file 
    # col=list(re.columns)
    # print(col)
    # re=re[col[1:4] +col[4:10]]
    # re=re.head(5)


#to save the file 
    # re.to_csv('Excel Files\\New.csv')
    #re.to_csv('Excel Files\\New-1.txt',index=False,sep='\t')


#to remove the index
    #print(re.reset_index(drop=True))

#use of regular expression

k=re.loc[re['Type 1'].str.contains('Fire|Grass',regex=True)]
print(k.head(5))
