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

### Setup (Only need to do once)

```shell
# clone the repo
git clone https://github.com/marinater/virtual-tab.git
cd virtual-tab
# create a virtual environment for this project
python3 -m venv .venv
# install dependencies within the virtual environment
source .venv/bin/activate
pip install -r requirements.txt
```

### After setup

```shell
# make sure you are in the virtual-tab root directory
# use virtual environment
source .venv/bin/activate
# run the project
python app.py
```



> Important note: This project requires access to your camera and mouse, which some operating systems will flat out deny the first time you run the program. Asking users for these permissions is something that we are interested in implementing, but until then, look at the Troubleshooting section to find out how to grant the necessary access.

### Adding new dependencies to requirements.txt

```shell
# make sure you are in the virtual-tab root directory
python -m pip freeze > requirements.txt
```

## Troubleshooting

Below is a list of problems we ran into while developing the project and anticipate users may as well. This list is not exhaustive by any means, so feel free to open issues on the Github issue tracker or even open a pull request to add more content to this Troubleshooting section!

### Python version

Our project will only work with Python 3. If you are getting strange syntax errors or missing dependencies right off the bat, check that the program is not being run with a Python 2 interpreter.

### Permissions (macOS Big Sur)

If you run the program and it quits immediately (sometimes with an error code, sometimes not), you most likely need to give the Terminal program access to your camera. If, later on, the program is unable to move the mouse the way it should, you most likely need to give the Terminal program access to 'accessibility' features.

##### To grant camera permissions:

- Navigate to System Preferences -> Security & Privacy -> Privacy Tab -> Camera
- Click the lock in the bottom left and enter your password
- Find "Terminal" in the list of apps on the right and ensure that it is checked

##### To grant mouse permissions:

- Navigate to System Preferences -> Security & Privacy -> Privacy Tab -> Accessibility
- Click the lock in the bottom left and enter your password
- Find "Terminal" in the list of apps on the right and ensure that it is checked

> Important note: If "Terminal" does not appear on the list of apps, close the systems preferences menu, rerun the app, and then navigate to the page again. Apps only show up on the list after the first time they request those permissions.

> Important note: You must run the project from an application you grant the above permissions to. If you grant permissions to Terminal, you must run it from the Terminal app. Getting the program to run inside a VS Code shell will be much more difficult and is not something we have done.

### Permissions (Windows)

Need help testing on Windows! Please consider contributing to this section.

### Permissions (Linux)

Need help testing on Linux! Please consider contributing to this section.

## Virtual Tab Community

### Discord (Our quick response discussion forum)

This is the fastest way to get in touch with us! We would love to have more contributors as well as get feedback from real users. At the moment, we have a discord where we have channels dedicated to discussing existing features as well as talk about developing new features.

[Discord link here](https://discord.gg/yxhUZuAShH)

### Github Issues (Official planning and prioritization system)

While the project is under active development, you can count on issues created with the github issue tracker to be seen and at least responded to within a few days. Feel free to ping us on Discord if the issue has been sitting stale for longer than that, since we are less likely to miss it there.

### Github Wiki

The majority of our documentation and status updates will be done through the Github Wiki. Updates, blog posts, etc. can all be found there.
