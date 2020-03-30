import pandas as pd
import plotnine as p9
import matplotlib.pyplot as plt

x = pd.Series(range(21))
y = x ** 2

mygraph = (
    p9.ggplot(pd.DataFrame({'x': x, 'y': y}), p9.aes(x='x', y='y'))
    + p9.geom_path()
    + p9.theme_bw()
)

mygraph.draw()
plt.show()