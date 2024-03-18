'''' This file takes the server input and plot it the ecg'''
from dash_extensions import WebSocket
import plotly.express as px
from dash_extensions.enrich import html, dcc, Output, Input, DashProxy
import pandas as pd

app = DashProxy(prevent_initial_callbacks=True)


## COMMENT: This block of code should not be in the repo as it does nothing

# update_graph = """ function(msg){
# if (!msg){return {};}
# # const data = JSON.parse(msg.split(','));
# const data = msg.split(',');
# print(msg)
# # # x = data[0];
# # # y = data[2];

# return {data: [{x: data[0], y: data[2], type: "line"}]}};
# }
# """

# COMMENT: You have a lot of trailing white-space, make sure to install a package that highlights this
app.layout = html.Div([
    WebSocket(id='ws', url="ws://assemblix:8282"),
    dcc.Graph(id="graph")
])
# # Output("graph", "figure")


@app.callback(Output("graph", "figure"), [Input("ws", "message")])
def update_graph(message):
    global delta_time, raw_signal,filtered_ecg
    delta_time = []
    raw_signal = []
    filtered_ecg = []
    data = message['data'].split(',')
    # COMMENT: Perhaps you can make a parameter that controlls this behaviour?
    # print(data[0])
    # print(data[2])

    # COMMENTS: In stead of three checks, this code could be replaced by one
    # Example: If not header: then do what you do
    if data[0] != "" :
        delta_time.append(pd.to_timedelta(data[0]).total_seconds())
    if data[1] != 'ECG':
        raw_signal.append(float(data[1]))
    if data[2] != "ECG I filtered":
        filtered_ecg.append(float(data[2]))

    df = pd.DataFrame({
        'delta_time': delta_time,
        'raw_signal': raw_signal,
        'ecg_filtered': filtered_ecg,
    })

    fig = px.line(data_frame=df, x="delta_time", y=['raw_signal', 'ecg_filtered'])
    return fig


if __name__ == '__main__':
    app.run(debug=True)