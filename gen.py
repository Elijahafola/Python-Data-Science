import csv
import random
from faker import Faker # Faker library to generate data that will look realistic for analysis and data science
from datetime import datetime, timedelta

#Initialize Faker
fake= Faker()

#Parameters
num_entries = 1000000
start_year=2005
end_year= 2024
file_name='Finance_data.csv'

#Cities and job title samples
cities=['Mombasa','Kisumu','Eldoret','Thika','Kakamega','Lodwar','Nakuru','Nanyuki','Nairobi','Naivasha','Homabay','Nyahururu']
job_titles= ['Accountant','Data analyst','Software Engineer','HR Manager','Finance Clerk','Managing Executive','Customer Service Agent','Payroll Associate','Java Engineer','Python developer','Risk analyst']

#Function to generate date entries between 2005 and 2024
def random_date():
    start_date= datetime(start_year,1,1)
    end_date = datetime(end_year,12,31)
    delta= end_date - start_date
    random_days = random.randint(0,delta.days)
    return start_date + timedelta(days=random_days)

#Generate data
with open(file_name,mode='w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Date','Salary','Job Description','City','Email','Contact','Airtime','Electricity','Insurance','Overtime'])

    for _ in range(num_entries):
        writer.writerow([
        random_date().strftime('%Y-%m-%d'),
        round(random.uniform(30000,20000),2),
        random.choice(job_titles),
        random.choice(cities),
        fake.email(),
        fake.phone_number(),
        round(random.uniform(500,5000),2),
        round(random.uniform(1000,10000),2),
        round(random.uniform(2000,15000),2),
        round(random.uniform(0,50),2)])

print(f"{num_entries:,} rows of Finance data writen to {file_name}.")

