# Minecraft Mood 🌳🌼

Un paisaje pixelado inspirado en la estética de bloques de Minecraft, creado en Python con Tkinter. El campo se dibuja de a poco y, al terminar, el pastito se mueve suavemente con el viento.

## Características

- Campo con árboles, montañas, nubes y flores de colores.
- Aparición progresiva del paisaje.
- Pasto animado con efecto de brisa.
- Botón **Nuevo paisaje** para generar otra escena.
- Botón **Ver atardecer / Ver día** para cambiar la luz y volver a dibujar la escena.

## Requisitos

- Python 3.8 o posterior.
- Tkinter, incluido normalmente con Python en Windows.
- Un escritorio gráfico para abrir la ventana de la aplicación.

No requiere imágenes, conexión a Internet ni paquetes de `pip` para ejecutarse.

## Cómo ejecutarlo

1. Descargá `minecraftmood.py` o cloná este repositorio.
2. Abrí una terminal en la carpeta donde guardaste el archivo.
3. Ejecutá:

```bash
python minecraftmood.py
```

En algunos sistemas el comando es `python3 minecraftmood.py`.

### En Visual Studio o Visual Studio Code

Abrí el archivo, seleccioná tu intérprete de Python y ejecutalo con el botón de ejecución o con el comando anterior desde la terminal integrada. En Visual Studio necesitás la carga de trabajo de desarrollo de Python; en Visual Studio Code, la extensión de Python.

### Si falta Tkinter

Podés comprobar su instalación con:

```bash
python -m tkinter
```

Debería abrir una pequeña ventana de prueba. Si aparece un error relacionado con `tkinter`, instalá el soporte de Tcl/Tk de tu distribución de Python. En Ubuntu o Debian suele estar disponible como `python3-tk`.

## Personalización

En `minecraftmood.py` podés modificar:

- `WIDTH` y `HEIGHT`: tamaño del lienzo.
- `self.index + 12`, dentro de `draw_next`: cantidad de piezas que aparecen en cada paso. Un número menor hace más lenta la aparición.
- `self.root.after(20, self.draw_next)`: pausa entre pasos del dibujo, en milisegundos.
- `animate_wind`: velocidad y amplitud del movimiento del pasto.
- `flower_colors`, dentro de `render`: colores de las flores.

La escena usa una semilla aleatoria: la misma semilla reproduce el mismo paisaje.

---

Proyecto independiente inspirado en una estética de bloques. No está afiliado a Mojang ni a Microsoft.
