import plotly.graph_objects as go
import numpy as np

x = np.linspace(0, 10, 100)
y = x**2

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='y=x^2'))
fig.show()