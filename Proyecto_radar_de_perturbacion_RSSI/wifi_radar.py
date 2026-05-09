import time
import pywifi
import matplotlib.pyplot as plt
import numpy as np


def obtner_rssi(iface, nombre_red_objeto):

    iface.scan()
    time.sleep(0.00003)
    scan_results = iface.scan_results()

    for result in scan_results:
        if result.ssid == nombre_red_objeto:
            return result.signal # devuelve el valor en dBm
    return -100


def iniciar_mapa_termico(mi_red):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0] # para tomar la tarjeta de red
    
    print(f" Iniciando rastero de: {mi_red}")
    print(" Presion Crtl+C en la terminal para detener")

    history_size = 50
    width = 10

    data_matrix = np.full((history_size, width), -100)

    plt.ion()
    fig, ax = plt.subplots(figsize=(4,6))

    #mapa de calor
    im = ax.imshow(data_matrix, cmap='viridis', aspect='auto',
                   vmin=-90, vmax=-30, interpolation='bilinear')
    
    #oculta los ejes 
    ax.axis('off')
    plt.title(f" Monitos de presencia: {mi_red}")
    char = fig.colorbar(im, ax=ax, orientation='vertical')
    char.set_label('Potencia de señal dBm ')

    try:
        while True:
            rssi = obtner_rssi(iface, mi_red)

            print(f" Intensidad: {rssi}")
            data_matrix = np.roll(data_matrix, 1, axis=0)

            data_matrix[0, :] =rssi
            im.set_data(data_matrix)
            fig.canvas.draw()
            fig.canvas.flush_events()

    except KeyboardInterrupt:
        print(" \n Radar detenido")


if __name__ == "__main__":
    MI_WIFI_SSID = "FIBRAMAX_L_5G"
    iniciar_mapa_termico(MI_WIFI_SSID)
        