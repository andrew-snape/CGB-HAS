# Centurion Garage Door Integration for Home Assistant

This is a custom integration for **Centurion Smart Garage Door Openers** that support local API access through the MY CGD App. It allows full control and monitoring of the garage door, internal lamp, vacation mode, and camera feed.

---

## ✅ Features

- 🚪 Open, close, and stop garage door
- 💡 Control garage lamp (on/off)
- 🏖 Enable or disable vacation mode
- 📷 View garage camera stream (`http://<ip>:88/`)
- ⚙️ Setup directly via Home Assistant UI (no YAML required)
- 🏠 HomeKit compatible through standard cover/switch/camera entities

---

## 📦 Installation

### Option 1: Manual

1. Download the [latest release](https://github.com/andrew-snape/CGB-HAS/releases)
2. Extract to your Home Assistant config:
   ```
   /config/custom_components/centurion/
   ```

3. Restart Home Assistant.

### Option 2: HACS (once published)

Coming soon!

---

## ⚙️ Configuration

1. Go to **Settings → Devices & Services**
2. Click **+ Add Integration**
3. Search for **Centurion**
4. Enter the **IP address** and **API key** from your MY CGD app

No YAML configuration required.

---

## 🧪 Entities Created

| Entity Type | Name                            | Example Entity ID                |
|-------------|----------------------------------|----------------------------------|
| Cover       | Centurion Garage Door           | `cover.centurion_garage_door`   |
| Switch      | Centurion Garage Lamp           | `switch.centurion_garage_lamp`  |
| Switch      | Centurion Vacation Mode         | `switch.centurion_vacation_mode`|
| Camera      | Centurion Garage Camera         | `camera.centurion_garage_camera`|

---

## 🛠 Troubleshooting

- Ensure your Centurion device has a **static IP** or DHCP reservation
- API key must be from the **MY CGD** app under “Local API”
- If camera doesn't load, try opening `http://<ip>:88/` directly

---

## 🧱 Roadmap

- Config validation on setup
- Lamp and vacation status polling
- HACS submission and automatic updates

---

## 📜 License

MIT License

---

## 🙌 Credits

Developed by [Andrew Snape](https://github.com/andrew-snape)  
This project is not affiliated with Centurion or CGD.
