import matplotlib.pyplot as plt
import pandas as pd

dataset = load_wine()
data = pd.DataFrame(dataset.data, columns=dataset.feature_names)
x = data.alcohol
y = data.flavanoids

print()


