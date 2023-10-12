import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a fictional DataFrame
np.random.seed(42)
data = {
    'total_bill': np.random.uniform(10, 60, 200),
    'tip': np.random.uniform(1, 12, 200),
    'time': np.random.choice(['Lunch', 'Dinner'], 200),
    'sex': np.random.choice(['Male', 'Female'], 200)
}
df = pd.DataFrame(data)

# Use FacetGrid with the custom dataframe 'df'
g = sns.FacetGrid(df, col="time", row="sex")
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.set_axis_labels("Total bill ($)", "Tip ($)")
g.set_titles(col_template="{col_name} patrons", row_template="{row_name}")
g.set(xlim=(0, 60), ylim=(0, 12), xticks=[10, 30, 50], yticks=[2, 6, 10])
g.tight_layout()
plt.show()
