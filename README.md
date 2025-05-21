# Centurion Garage Door Integration for Home Assistant

This is a custom Home Assistant integration for **Centurion Smart Garage Door Openers** (e.g. SDO4) that support **local API control** via the MY CGD app.

It allows you to control your garage door (open, close, stop), read its current status, and expose it to platforms like **Apple HomeKit**.

---

## 🔧 Features

- Open/Close/Stop garage door
- Status polling
- Works fully local (no cloud dependency)
- Compatible with HomeKit via Home Assistant
- Configurable via `configuration.yaml`

---

## 📦 Installation

### Step 1: Download & Install

1. Download the latest release (ZIP): [Releases Page](https://github.com/andrew-snape/CGB-HAS/releases)
2. Extract the contents to:
   ```
   <your-home-assistant-config>/custom_components/centurion
   ```

   You should now have:
   ```
   custom_components/
     └── centurion/
         ├── __init__.py
         ├── cover.py
         ├── manifest.json
   ```

3. Restart Home Assistant.

---

## ⚙️ Configuration

Add the following to your `configuration.yaml` file:

```yaml
cover:
  - platform: centurion
    ip_address: 192.168.X.X  # Replace with your device's local IP
    api_key: YOUR_API_KEY     # Replace with your local API key from the MY CGD app
```

- `ip_address`: The **IP address** of your Centurion Smart Controller.
- `api_key`: Your **local API key**, found in the MY CGD app.

> You can test API access by visiting in your browser:
> ```
> http://192.168.X.X/api?key=YOUR_API_KEY&status=json
> ```

---

## 🧪 Testing

After restarting HA, a new entity should appear:
- `cover.centurion_garage_door`

Use this entity in Home Assistant, HomeKit, automations, etc.

---

## 🏠 HomeKit Integration

To expose the garage door to HomeKit:

```yaml
homekit:
  filter:
    include_entities:
      - cover.centurion_garage_door
```

---

## 🛠 Troubleshooting

- Ensure the device has a **static IP address** or DHCP reservation.
- If no status appears, check your network and test the direct URL in a browser.
- Use the IP address instead of the hostname if DNS resolution fails on your network.

---

## 💡 Future Ideas

- Add support for lamp control (`lamp=on/off`)
- Add vacation mode toggle (`vacation=on/off`)
- Add camera stream view (`http://<ip>:88/`)
- Add configuration flow for UI-based setup

---

## 📜 License

MIT

---

## 🙌 Credit

Developed by [Andrew Snape](https://github.com/andrew-snape) based on Centurion's Local API documentation.

This project is not affiliated with Centurion or CGD.
