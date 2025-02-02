import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    # Encode the image data to base64 for embedding in HTML
    graph = base64.b64encode(image_png).decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Monthly Expense Tracker')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('items')
    plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    return graph