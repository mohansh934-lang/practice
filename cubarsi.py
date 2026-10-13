from faker import Faker
import pandas as pd
fake = Faker()

pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)

columns = [
    "name",
    "email",
    "city",
    "country",
    "ipv4",
    "url",
    "domain_name",
    "company",
    "job",
    "year"
]

details = []
for i in range(10):
    row =[fake.name(),
       fake.email(),
       fake.city(),
       fake.country(),
       fake.ipv4(),
       fake.url(),
       fake.domain_name(),
       fake.company(),
       fake.job(),
       fake.year()]

    details.append(row)

df = pd.DataFrame(details, columns=columns)

print(df)
