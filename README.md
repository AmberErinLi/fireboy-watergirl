# Fireboy and Watergirl

A clone of the Fireboy and Watergirl puzzle-platformer, built with [pygame-ce](https://pyga.me/).

## Goal

Each level has two characters, Fireboy and Watergirl, who must each reach their own door to complete the level. Fire is harmless to Fireboy but deadly to Watergirl, and water is harmless to Watergirl but deadly to Fireboy, so getting both characters to their doors means navigating shared platforms while keeping each one off the hazard that kills them.

## Status

Early in development. Currently implemented:

- Fireboy sprite with sub-pixel movement, gravity, and jumping
- Block collision (solid ground/walls)
- Fire and water hazard tiles: stepping on the matching element is safe and acts as ground, stepping on the mismatched element resets the player to the start
- Levels defined as JSON (`levels/level1.json`) and loaded at runtime

Planned:

- Watergirl, controllable alongside Fireboy
- Door objects for each character, and level-complete detection when both reach their doors
- Additional levels

## Requirements

- Python 3
- [pygame-ce](https://pyga.me/)

Install dependencies:

```
pip install -r requirements.txt
```

## Running

```
python main.py
```

## Controls

| Key | Action |
|---|---|
| Left / Right Arrow | Move Fireboy |
| Up Arrow | Jump (when on the ground) |

Watergirl's controls (planned: WASD or similar) will be added once she's playable.

## Level format

Levels live in `levels/*.json` and describe block and hazard placement in a grid of `[x, y]` pixel coordinates:

```json
{
    "width": 800,
    "height": 600,
    "players": {
        "fireboy": [50, 500],
        "watergirl": [700, 500]
    },
    "blocks": [[0, 580], [20, 580]],
    "hazards": {
        "water": [[460, 580]],
        "fire": [[300, 580]]
    }
}
```

Door positions for each character will be added to this format once doors are implemented.

## Project structure

```
main.py       # game loop, input, physics, collision
player.py     # Player class (position, velocity, image)
block.py      # Block class (static solid geometry)
hazard.py     # Hazard class (fire/water tiles)
level.py      # Loads blocks/hazards from a level JSON file
levels/       # Level definitions
assets/       # Sprites
```
