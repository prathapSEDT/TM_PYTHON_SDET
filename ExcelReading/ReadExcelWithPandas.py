import pandas
filepath=r"C:\Users\hanshik\Downloads\challenge.xlsx"

df1=pandas.read_excel(filepath,sheet_name='Data')
newDataFrame=pandas.DataFrame(columns=['First Name','Phone Number'])
#
# print(df1)

for ind in df1.index:

    newDataFrame.loc[len(newDataFrame)]=[df1['First Name'][ind]]+[df1['Phone Number'][ind]]


print(newDataFrame)

#write the data into an excel

newDataFrame.to_excel(r"D:\PDF Data\abc.xlsx")




