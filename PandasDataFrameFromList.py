import pandas as pd
lst = [['Geek', 25], ['is', 30],
       ['for', 26], ['GeeksforGeeks', 22]]
df = pd.DataFrame(lst, columns=['Tag', 'number'])
print(df)

