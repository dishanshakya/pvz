# pvz-portable-setup

One-command Arch Linux setup for [PvZ-Portable](https://github.com/wszqkzqk/PvZ-Portable) using `yay`, with ALSA audio fix (`SDL_AUDIO_DRIVER=alsa`), `rofi`/`dmenu` launcher integration, and an optional save unlocker.

> **Note:** Copyrighted game assets (`main.pak` and `properties/`) are not included in this repository. Provide your own legally owned copy of *Plants vs. Zombies: Game of the Year Edition*.

## Usage

```bash
git clone https://github.com/dishanshakya/pvz.git
cd pvz
./install-pvz /path/to/PlantsVsZombies-GOTY.zip --unlock
```

- You can pass either a `.zip` archive or an extracted folder containing `main.pak` and `properties/`.
- If omitted, `install-pvz` checks `~/Downloads` and standard Steam directories automatically.
- Omit `--unlock` if you want to start Adventure mode fresh.
- You can also run `./unlock-all.py [ProfileName]` anytime later to unlock all modes, plants, and shop items.

## Launching

- Terminal / `dmenu` / `rofi -show run`: `pvz`
- App launcher (`rofi -show drun`): **PvZ Portable**
