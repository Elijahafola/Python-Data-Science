import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#Load Finance_data.csv
df=pd.read_csv("Finance_data.csv")
#print(df.head())

#Basic info and missing values
df.info()
df.isnull().sum()

#Insights and visualizations
plt.figure(figsize=(10,6))
sns.histplot(df['Salary'], bins=50, kde=True)
plt.title('Salary Distribution')
plt.show()
plt.savefig('Goku.jpg')

#City-Wise Salary comaprisons
plt.figure(figsize=(12,6))
sns.boxplot(data=df,x='City',y='Salary')
plt.xticks(rotation=45)
plt.title('City vs Salary')
plt.show()
plt.savefig('Gohan.jpg')

#Finance behaviour vs salary
correlation = df[['Salary','Airtime','Electricity','Insurance','Overtime']].corr()
sns.heatmap(correlation, annot=True, cmap= 'coolwarm')
plt.title('Correlation Matrix')
plt.show()
plt.savefig('Broly.jpg')

#Salary trends over time
df['Date']=pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
average_salary_per_year = df.groupby('Year')['Salary'].mean()
plt.title('Average Salary Over Years')
plt.ylabel('Salary')
plt.grid()
plt.show()
plt.savefig('Trend.jpg')

#Job title vs average salary
top_jobs = df.groupby('Job Description')['Salary'].mean().sort_values(ascending=True)
print(top_jobs.head(10))

