from uuid import uuid4
import pandas as pd
from ifscfinder.models import Bank
df = pd.read_csv("bank_branches.csv")

for i in range(len(df)-1):
    print(i)
    Bank.objects.create(id=uuid4(),bank_name=df['bank_name'][i],
        ifsc=df['ifsc'][i],branch=df['branch'][i],
        address=df['address'][i],district=df['district'][i],
        state=['state'][i])
