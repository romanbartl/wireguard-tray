#!/usr/bin/env python3
import gi
import sys
import json
import subprocess
import os

# --- fallback pro různé Ubuntu verze ---
try:
    gi.require_version('AyatanaAppIndicator3', '0.1')
    from gi.repository import AyatanaAppIndicator3 as AppIndicator3
except (ImportError, ValueError):
    gi.require_version('AppIndicator3', '0.1')
    from gi.repository import AppIndicator3

from gi.repository import Gtk

# --- Kontrola argumentu ---
if len(sys.argv) != 2:
    print(f"Použití: {sys.argv[0]} /cesta/k/config.json")
    sys.exit(1)

config_path = sys.argv[1]
if not os.path.exists(config_path):
    print(f"Chyba: {config_path} neexistuje")
    sys.exit(1)

# --- Načtení konfigurace ---
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

# Očekáváme strukturu JSON:
# {
#   "tray_icon": "/absolutní/cesta/k/ikona.png",
#   "menu": [
#       {"label": "Spustit zálohu", "command": "~/scripts/backup.sh"},
#       {"label": "Restart služby", "command": "systemctl restart myservice"},
#       {"label": "Konec", "command": "quit"}
#   ]
# }

tray_icon = config.get("tray_icon", "")
menu_items = config.get("menu", [])

# --- Funkce pro spouštění příkazů ---
def run_command(cmd):
    subprocess.Popen(cmd, shell=True)

# --- Funkce pro vytvoření menu položky ---
def create_menu_item(label, command):
    item = Gtk.MenuItem(label=label)
    item.connect("activate", lambda _: run_command(command))
    return item

# --- Sestavení menu ---
def build_menu():
    menu = Gtk.Menu()
    for entry in menu_items:
        label = entry.get("label", "???")
        command = entry.get("command", "")
        menu.append(create_menu_item(label, command))
    menu.show_all()
    return menu

# --- Inicializace indikátoru ---
indicator = AppIndicator3.Indicator.new(
    "custom-tray",
    tray_icon if tray_icon else "utilities-terminal",
    AppIndicator3.IndicatorCategory.APPLICATION_STATUS
)
indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
indicator.set_menu(build_menu())

Gtk.main()
