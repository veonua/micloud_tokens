import micloud
import streamlit as st

server = st.selectbox("Select server", ["cn", "de", "i2", "ru", "sg", "us"])
username = st.text_input("Enter your name")
password = st.text_input("Enter your password", type="password")

products = {
    577: "Mi Robot Vacuum",
    51: "Yeelight",
    109: "Mi Control Hub",
    245: "AC Partner",
    65567: "Infrared Remote",
    206: "Toothbrush",
    152: "Plant Monitor",
}

login = None
if username and password:
    cloud = micloud.MiCloud(username, password)
    cloud.default_server = server
    login = cloud.login()

    if login:
        devices = cloud.get_devices()

        short_devices = [
            {'name':dev.get("name"),
             'localip':dev.get("localip"),
             'token':dev.get("token"),
             'pd_id': dev.get("pd_id"),  # product id see products
             'model':dev.get("model"),
             'ssid':dev.get("ssid"),
             } for dev in devices if dev.get("token")]

        my_dict = {}
        for v in short_devices:
            k = v.pop('ssid')
            my_dict.setdefault(k, []).append(v)

        st.write(my_dict)
    else:
        st.write("Login failed")

