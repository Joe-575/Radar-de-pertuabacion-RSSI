# Radar de Perturbación Wi-Fi (RSSI)

Este proyecto es un script en Python diseñado para monitorear y visualizar en tiempo real la intensidad de la señal (RSSI) de una red Wi-Fi específica. El script genera un mapa de calor dinámico que actualiza continuamente la potencia de la señal en dBm, permitiendo detectar posibles perturbaciones o cambios físicos en el entorno cercano al router/dispositivo.

## 🚀 Funcionalidades

- **Escaneo de Redes:** Utiliza tu tarjeta de red Wi-Fi para escanear y localizar una red específica (por nombre o SSID).
- **Monitoreo en Tiempo Real:** Lee constantemente el indicador de fuerza de señal recibida (RSSI) de la red objetivo.
- **Gráfico Dinámico (Mapa de Calor):** Dibuja una representación visual que simula un "radar térmico" a lo largo del tiempo.
- **Escala de Colores:** Muestra intensidades desde -90 dBm (señal débil) hasta -30 dBm (señal excelente).

## 🛠️ Requisitos Previos

Asegúrate de tener instalado **Python 3** en tu sistema. Además, este script depende de algunas librerías externas que debes instalar.

### Dependencias

Puedes instalarlas rápidamente utilizando `pip`:

```bash
pip install pywifi
pip install matplotlib
pip install numpy
```

> **Nota para Windows/Linux:** La librería `pywifi` interactúa con los drivers nativos del sistema operativo, por lo que podría requerir permisos de administrador dependiendo de tu configuración.

## 🔧 Configuración y Uso

1. **Configurar la red objetivo:** 
   Abre el archivo `wifi_radar.py` en un editor de texto o IDE. En la parte inferior del archivo, cambia el valor de la variable `MI_WIFI_SSID` por el nombre (SSID) de tu propia red Wi-Fi:
   
   ```python
   if __name__ == "__main__":
       MI_WIFI_SSID = "TU_NOMBRE_DE_RED_AQUI"
       iniciar_mapa_termico(MI_WIFI_SSID)
   ```

2. **Ejecutar el script:**
   Abre una terminal en la misma carpeta donde se encuentra el archivo y ejecuta:
   ```bash
   python wifi_radar.py
   ```

3. **Interactuar con el Radar:**
   - Se abrirá una ventana gráfica mostrando un mapa de calor que se irá llenando de arriba hacia abajo con lecturas en tiempo real.
   - En la consola, también verás el registro en texto de la intensidad leída (por ejemplo, `Intensidad: -45`).
   - Prueba a moverte, interponer objetos o acercarte/alejarte de tu router para ver cómo varían los valores y los colores del mapa.
   
4. **Detener el programa:**
   Presiona `Ctrl + C` en la terminal para detener la ejecución y cerrar el mapa de calor.

## 📁 Estructura del Proyecto

```text
Proyecto_radar_de_perturbacion_RSSI/
├── wifi_radar.py    # Script principal que contiene la lógica de escaneo y dibujado del gráfico
└── README.md        # Este archivo de documentación
```

## ⚠️ Posibles Errores o Consideraciones

- **Frecuencia de Escaneo:** La función `scan()` en algunos adaptadores de red puede ser un poco lenta o demorar unos segundos en refrescar resultados reales. El script fuerza un ligero retardo con `time.sleep()`.
- **Valores fijos (-100 dBm):** Si la red no es detectada en el escaneo (ya sea porque está muy lejos, apagada, o el nombre está mal escrito), el script reportará `-100`, que corresponde al color más oscuro o de fondo en el gráfico.
