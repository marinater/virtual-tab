# virtual-tab

Camera based replacement for physical drawing tablets

## Overview

Our goal is to make a desktop application that can act as a stand in replacement for drawing tablets. Drawing tablets, for those unaware, are devices roughly the size and shape of an iPad that you can connect to your computer. They come equipped with a special stylus that you can use with the tablet to move your mouse and create digital art more easily. However, they come with a few downsides:

- Expensive. Can cost anywhere between \$100 to \$800
- Takes up a lot of physical space, even when not in use
- Could be a big investment for a more casual user that may only need it once or twice

Our project focuses on helping those who want a drawing tablet for more casual use. It would be very hard to come close to the level of precision that real drawing tablets offer, but there is no doubt we can achieve a reasonable degree of accuracy for someone using this for something less fine grained. For example, players of the game Osu typically buy trackpads to play the game more comfortably. However, they don't need something as precise as a real drawing tablet, so a webcam based solution could be a feasible alternative.

## Goals

By the end of the Spring 2021 semester, we would like to have

- An application that can map a stylus in the the real world to screen coordinates
- A GUI interface to modify settings and see the stylus being tracked in real time
- Global keybinds to turn tracking on and off
- The ability to move the mouse pointer
- Proper documentation
- Repository organization in line with established Open Source projects

The scope of this project may change based on how many members join and how much each member is able to contribute.

## Getting Started

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Developers

```
python -m pip freeze > requirements.txt
```

