# Import library yang dibutuhkan
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')

dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))

fig, ax = plt.subplots()

dataset[dataset['order_month']=='2019-12'].groupby(['province'])['customer_id'].nunique().plot(kind='barh', color=colors, zorder=2, width=0.85)

for i, (p,pr) in enumerate(zip(dataset.index, dataset[dataset['order_month']=='2019-12'].groupby(['province'])['customer_id'].nunique())):
    plt.text(s=str(pr), x=pr-5, y=i, color="w", verticalalignment="center", horizontalalignment="right", size=10)
ax.invert_yaxis() 
ax.set_xlabel('Number of Customers')
ax.set_ylabel('Province')
ax.set_title('Number of Customers for December 2019 by Province', loc='center', pad=30, fontsize=16)
ax.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")
vals = ax.get_xticks()
for tick in vals:
      ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)
ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))
plt.show()