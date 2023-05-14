import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px


df_comisiones = pd.read_csv('/drive/MyDrive/Notebooks/data/cnsf/Comisiones.csv', encoding='cp1252', sep=',', on_bad_lines='warn')
df_emision = pd.read_csv('/drive/MyDrive/Notebooks/data/cnsf/Emision.csv', encoding='cp1252', sep=',', on_bad_lines='warn')
df_siniestros = pd.read_csv('/drive/MyDrive/Notebooks/data/cnsf/Siniestros.csv', encoding='cp1252', sep=',', on_bad_lines='warn')


app = dash.Dash(__name__)


app.layout = html.Div(
    children=[
        html.H1("Visualización de datos de comisiones"),
        dcc.Graph(id="comisiones-graph"),
    ]
)


@app.callback(
    Output("comisiones-graph", "figure"),
    Input("input-component", "value")  
)
def update_graph(input_value):
   

    fig = px.scatter(df_comisiones, x="columna_x", y="columna_y")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
