# Minecraft Mood 🌳🌼

[English](#english) · [Español](#español) · [Русский](#русский)

## English

A pixel landscape inspired by Minecraft’s block aesthetic, built with Python and Tkinter. The scene appears gradually, then the grass sways gently in the wind.

### Features

- A field with trees, mountains, clouds, and colorful flowers.
- Progressive drawing of the landscape.
- Animated grass with a gentle breeze effect.
- **Nuevo paisaje** (New landscape) button to generate another scene.
- **Ver atardecer / Ver día** (View sunset / View day) button to change the lighting and redraw the scene.

### Requirements

- Python 3.8 or later.
- Tkinter, normally included with Python on Windows.
- A graphical desktop to open the application window.

No images, Internet connection, or `pip` packages are required to run it. The application’s interface is in Spanish.

### How to run

1. Download `minecraftmood.py` or clone this repository.
2. Open a terminal in the folder containing the file.
3. Run:

```bash
python minecraftmood.py
```

On some systems, use `python3 minecraftmood.py`.

#### Visual Studio or Visual Studio Code

Open the file, select your Python interpreter, and run it using the Run button or the command above in the integrated terminal. Visual Studio requires the Python development workload; Visual Studio Code requires the Python extension.

#### If Tkinter is missing

Check your installation with:

```bash
python -m tkinter
```

A small test window should open. If you get a `tkinter` error, install Tcl/Tk support for your Python distribution. On Ubuntu or Debian, it is usually available as `python3-tk`.

### Customization

In `minecraftmood.py`, you can change:

- `WIDTH` and `HEIGHT`: canvas dimensions.
- `self.index + 12`, inside `draw_next`: number of pieces drawn per step. A smaller number makes the scene appear more slowly.
- `self.root.after(20, self.draw_next)`: delay between drawing steps, in milliseconds.
- `animate_wind`: speed and amplitude of the grass movement.
- `flower_colors`, inside `render`: flower colors.

The scene uses a random seed: the same seed reproduces the same landscape.

Independent project inspired by a block aesthetic. Not affiliated with Mojang or Microsoft.

---

## Español

Un paisaje pixelado inspirado en la estética de bloques de Minecraft, creado en Python con Tkinter. El campo se dibuja de a poco y, al terminar, el pastito se mueve suavemente con el viento.

### Características

- Campo con árboles, montañas, nubes y flores de colores.
- Aparición progresiva del paisaje.
- Pasto animado con efecto de brisa.
- Botón **Nuevo paisaje** para generar otra escena.
- Botón **Ver atardecer / Ver día** para cambiar la luz y volver a dibujar la escena.

### Requisitos

- Python 3.8 o posterior.
- Tkinter, incluido normalmente con Python en Windows.
- Un escritorio gráfico para abrir la ventana de la aplicación.

No requiere imágenes, conexión a Internet ni paquetes de `pip` para ejecutarse. La interfaz de la aplicación está en español.

### Cómo ejecutarlo

1. Descargá `minecraftmood.py` o cloná este repositorio.
2. Abrí una terminal en la carpeta donde guardaste el archivo.
3. Ejecutá:

```bash
python minecraftmood.py
```

En algunos sistemas el comando es `python3 minecraftmood.py`.

#### En Visual Studio o Visual Studio Code

Abrí el archivo, seleccioná tu intérprete de Python y ejecutalo con el botón de ejecución o con el comando anterior desde la terminal integrada. En Visual Studio necesitás la carga de trabajo de desarrollo de Python; en Visual Studio Code, la extensión de Python.

#### Si falta Tkinter

Podés comprobar su instalación con:

```bash
python -m tkinter
```

Debería abrir una pequeña ventana de prueba. Si aparece un error relacionado con `tkinter`, instalá el soporte de Tcl/Tk de tu distribución de Python. En Ubuntu o Debian suele estar disponible como `python3-tk`.

### Personalización

En `minecraftmood.py` podés modificar:

- `WIDTH` y `HEIGHT`: tamaño del lienzo.
- `self.index + 12`, dentro de `draw_next`: cantidad de piezas que aparecen en cada paso. Un número menor hace más lenta la aparición.
- `self.root.after(20, self.draw_next)`: pausa entre pasos del dibujo, en milisegundos.
- `animate_wind`: velocidad y amplitud del movimiento del pasto.
- `flower_colors`, dentro de `render`: colores de las flores.

La escena usa una semilla aleatoria: la misma semilla reproduce el mismo paisaje.


Proyecto independiente inspirado en una estética de bloques. No está afiliado a Mojang ni a Microsoft.

---

## Русский

Пиксельный пейзаж в блочной эстетике Minecraft, созданный на Python с помощью Tkinter. Пейзаж появляется постепенно, а затем трава плавно колышется на ветру.

### Возможности

- Поле с деревьями, горами, облаками и разноцветными цветами.
- Постепенная отрисовка пейзажа.
- Анимация травы с эффектом лёгкого ветерка.
- Кнопка **Nuevo paisaje** («Новый пейзаж») для создания новой сцены.
- Кнопка **Ver atardecer / Ver día** («Показать закат / Показать день») для смены освещения и повторной отрисовки сцены.

### Требования

- Python 3.8 или новее.
- Tkinter, который обычно входит в состав Python для Windows.
- Графическая среда для открытия окна приложения.

Для запуска не нужны изображения, подключение к Интернету или пакеты из `pip`. Интерфейс приложения — на испанском языке.

### Как запустить

1. Скачайте `minecraftmood.py` или клонируйте этот репозиторий.
2. Откройте терминал в папке с файлом.
3. Выполните:

```bash
python minecraftmood.py
```

В некоторых системах используется команда `python3 minecraftmood.py`.

#### Visual Studio или Visual Studio Code

Откройте файл, выберите интерпретатор Python и запустите программу кнопкой запуска или указанной выше командой во встроенном терминале. Для Visual Studio необходима рабочая нагрузка «Разработка на Python», а для Visual Studio Code — расширение Python.

#### Если Tkinter отсутствует

Проверьте установку командой:

```bash
python -m tkinter
```

Должно открыться небольшое тестовое окно. Если возникает ошибка, связанная с `tkinter`, установите поддержку Tcl/Tk для вашего дистрибутива Python. В Ubuntu и Debian она обычно доступна в пакете `python3-tk`.

### Настройка

В файле `minecraftmood.py` можно изменить:

- `WIDTH` и `HEIGHT`: размеры холста.
- `self.index + 12` внутри `draw_next`: количество элементов, отрисовываемых за один шаг. Меньшее число замедляет появление пейзажа.
- `self.root.after(20, self.draw_next)`: задержку между шагами отрисовки в миллисекундах.
- `animate_wind`: скорость и амплитуду движения травы.
- `flower_colors` внутри `render`: цвета цветов.

Сцена использует начальное значение генератора случайных чисел: одинаковое значение воспроизводит одинаковый пейзаж.

Независимый проект, вдохновлённый блочной эстетикой. Не связан с Mojang или Microsoft.
