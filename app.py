import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Muestra la versión de Python junto con detalles adicionales
st.write("Versión de Python:", platform.python_version())

values = 0.0
act1="OFF"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="broker.mqttdashboard.com"
port=1883
client1= paho.Client("MajoCliente")
client1.on_message = on_message



st.title("MQTT Control")

if st.button('ON'):
    act1="ON"
    client1= paho.Client("MajoCliente")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_majoo", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('OFF'):
    act1="OFF"
    client1= paho.Client("MajoClienteGIT-HUB")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =jsoimport time
import json
import platform
import paho.mqtt.client as paho
import streamlit as st

# 1. Configuración de la Página
st.set_page_config(
    page_title="Panel de Control MQTT IoT",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estilos CSS Personalizados
st.markdown("""
    <style>
    /* Banner principal tipo dashboard */
    .dashboard-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #3b82f6 100%);
        padding: 30px;
        border-radius: 20px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.25);
    }
    .dashboard-header h1 {
        margin: 0;
        font-size: 2.3rem;
        font-weight: 800;
        color: white !important;
    }
    .dashboard-header p {
        margin-top: 8px;
        font-size: 1.05rem;
        color: #93c5fd !important;
    }

    /* Contenedor de Tarjeta de Control */
    .control-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(128, 128, 128, 0.25);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 15px;
    }
    
    /* Personalización de botones */
    .stButton > button {
        border-radius: 10px !important;
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Funciones Callback MQTT
def on_publish(client, userdata, result):
    print("El dato ha sido publicado correctamente.\n")

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

# Configuración del Broker
broker = "broker.mqttdashboard.com"
port = 1883

# 4. Barra Lateral - Estado del Sistema y Red
with st.sidebar:
    st.title("🌐 Red & Sistema")
    st.caption("Panel de Conectividad MQTT")
    
    st.markdown("---")
    st.markdown(f"**Broker:** `{broker}`")
    st.markdown(f"**Puerto:** `{port}`")
    st.markdown(f"**Tópico Digital:** `cmqtt_majoo`")
    st.markdown(f"**Tópico Analógico:** `cmqtt_m`")
    
    st.markdown("---")
    st.caption(f"🐍 **Python Version:** `{platform.python_version()}`")

# 5. Banner de Encabezado Principal
st.markdown("""
    <div class="dashboard-header">
        <h1>⚡ Panel de Control Ciberfísico MQTT</h1>
        <p>Envío de comandos digitales (ON/OFF) y señales analógicas en tiempo real a dispositivos IoT.</p>
    </div>
""", unsafe_allow_html=True)

# 6. Sección Principal - 2 Columnas de Control
col_digital, col_analog = st.columns([1, 1], gap="large")

# --- COLUMNA 1: CONTROL DIGITAL (ON / OFF) ---
with col_digital:
    st.subheader("🔴🟢 Control Digital (Actuador)")
    st.write("Envía un pulso de encendido o apagado al sistema ciberfísico.")
    
    col_on, col_off = st.columns(2)
    
    with col_on:
        if st.button('🟢 Encender (ON)', use_container_width=True, type="primary"):
            act1 = "ON"
            client1 = paho.Client("MajoCliente")
            client1.on_publish = on_publish
            client1.connect(broker, port)
            message = json.dumps({"Act1": act1})
            ret = client1.publish("cmqtt_majoo", message)
            st.success("Comando ON enviado con éxito a `cmqtt_majoo`", icon="✅")

    with col_off:
        if st.button('🔴 Apagar (OFF)', use_container_width=True):
            act1 = "OFF"
            client1 = paho.Client("MajoClienteGIT-HUB")
            client1.on_publish = on_publish
            client1.connect(broker, port)
            message = json.dumps({"Act1": act1})
            ret = client1.publish("cmqtt_majoo", message)
            st.error("Comando OFF enviado a `cmqtt_majoo`", icon="🛑")

# --- COLUMNA 2: CONTROL ANALÓGICO ---
with col_analog:
    st.subheader("🎚️ Control Analógico")
    st.write("Ajusta y transmite un valor continuo en el rango de 0.0 a 100.0.")
    
    values = st.slider('Selecciona el valor analógico:', 0.0, 100.0, 25.0)
    
    st.metric(label="Valor Seleccionado", value=f"{values:.1f}")
    
    if st.button('🚀 Enviar Valor Analógico', use_container_width=True):
        client1 = paho.Client("MajoClienteB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Analog": float(values)})
        ret = client1.publish("cmqtt_m", message)
        st.info(f"Valor `{values}` transmitido con éxito al tópico `cmqtt_m`", icon="📡")n.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_majoo", message)
  
    
else:
    st.write('')

values = st.slider('Selecciona el rango de valores',0.0, 100.0)
st.write('Values:', values)

if st.button('Enviar valor analógico'):
    client1= paho.Client("MajoClienteB")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)   
    message =json.dumps({"Analog": float(values)})
    ret= client1.publish("cmqtt_m", message)
    
 
else:
    st.write('')




