import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
from module.downlaod_video import download_video
import threading

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=24)
        self.set_child(self.box1)
        self.save_path = "~/Videos"
        self.label = Gtk.Label(label="Youtube to DaVinci")
        self.label.set_hexpand(True)
        self.label.set_halign(Gtk.Align.CENTER)
        self.label.add_css_class("title-2")
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Paste url on YouTube")
        self.entry.set_hexpand(True)
        self.buttons_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        self.buttons_box.set_halign(Gtk.Align.CENTER)
        self.format_type= None
        self.video = Gtk.ToggleButton(label="Video")
        self.audio = Gtk.ToggleButton(label="Only Audio")
        self.with_out_audio = Gtk.ToggleButton(label="With out Audio")
        self.audio.set_group(self.video)
        self.with_out_audio.set_group(self.video)
        self.label1 = Gtk.Label(label="Choose Codec (only for video)")
        self.items = ["ProRes (Easy)", "DNxHR (Quality/Hard)", "Native (MKV + PCM Audio)"]
        self.items1 = ["1080", "1440", "2160"]
        self.dropdown = Gtk.DropDown.new_from_strings(self.items)
        self.dropdown1 = Gtk.DropDown.new_from_strings(self.items1)
        self.label2 = Gtk.Label(label=f"Save in {self.save_path}")
        self.button = Gtk.Button(label="Change Directory")
        self.button1 = Gtk.Button(label="Start")
        self.video.connect("toggled", self.video1)
        self.audio.connect("toggled", self.audio1)
        self.with_out_audio.connect("toggled", self.with_out_aduio1)
        self.button.connect("clicked", self.on_change_directory)
        self.button1.connect("clicked", self.start)
        self.box1.append(self.label)
        self.box1.append(self.entry)
        self.buttons_box.append(self.video)
        self.buttons_box.append(self.audio)
        self.buttons_box.append(self.with_out_audio)
        self.box1.append(self.buttons_box)
        self.box1.append(self.label1)
        self.box1.append(self.dropdown)
        self.box1.append(self.dropdown1)
        self.box1.append(self.label2)
        self.box1.append(self.button)
        self.box1.append(self.button1)

        
    def on_change_directory(self, button):
        dialog = Gtk.FileDialog()
        dialog.select_folder(
            parent=self,
            cancellable=None,
            callback=self.on_directory_selected
        )

        
    def on_directory_selected(self, dialog, result):
        try:
            directory = dialog.select_folder_finish(result)
            if directory:
                path = directory.get_path()
                self.label2.set_label(f"Save in {path}")
                self.save_path = path
        except Exception as e:
            pass
    
    def start(self, button):
        ts = threading.Thread(target=download_video, args=(self.save_path, self.entry.get_text(), self.format_type, self.dropdown1.get_selected_item().get_string(), self.dropdown.get_selected()), daemon=True)
        ts.start()

    def video1(self, widget):
        self.format_type = "Video"
    
    def audio1(self, widget):
        self.format_type = "Only Audio"
    
    def with_out_aduio1(self, widget):
        self.format_type = None

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
