import customtkinter as ctk
import serial
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Arduino Serial Monitor")
app.geometry("600x500")  # Uygulamayı biraz daha genişletiyoruz

ser = None
reading = False
previous_min_set = None
previous_max_set = None

# Arduino'ya veri göndermek için fonksiyon
def send_data_to_arduino():
    global previous_min_set, previous_max_set
    if ser and ser.is_open:
        min_val = min_set_entry.get()
        max_val = max_set_entry.get()
        try:
            min_val = int(min_val)
            max_val = int(max_val)
            # Arduino'ya min ve max değeri gönder
            ser.write(f"{min_val},{max_val}\n".encode('utf-8'))
            # Önceki min ve max değerlerini güncelle
            previous_min_set = min_val
            previous_max_set = max_val
            # Değerleri güncelle
            previous_min_set_label.configure(text=f"Önceki Min Set: {previous_min_set}")
            previous_max_set_label.configure(text=f"Önceki Max Set: {previous_max_set}")
            status_label.configure(text="Veri Gönderildi ✅")
        except ValueError:
            status_label.configure(text="Hatalı Veri! ❌")

def read_serial():
    global reading
    while reading:
        if ser.in_waiting:
            line = ser.readline().decode('utf-8').strip()
            textbox.insert("end", line + "\n")
            textbox.see("end")

def connect_serial():
    global ser, reading
    try:
        ser = serial.Serial(port_entry.get(), int(baud_entry.get()))
        reading = True
        threading.Thread(target=read_serial, daemon=True).start()
        status_label.configure(text="Bağlandı ✅")
    except:
        status_label.configure(text="Bağlantı Hatası ❌")

def disconnect_serial():
    global ser, reading
    if ser and ser.is_open:
        reading = False
        ser.close()
        status_label.configure(text="Bağlantı Kesildi 🔌")

# GUI elemanları
port_entry = ctk.CTkEntry(app, placeholder_text="Port (örn: COM3)")
port_entry.pack(pady=10)

baud_entry = ctk.CTkEntry(app, placeholder_text="Baud Rate (örn: 9600)")
baud_entry.pack(pady=10)

connect_btn = ctk.CTkButton(app, text="Bağlan", command=connect_serial)
connect_btn.pack(pady=5)

disconnect_btn = ctk.CTkButton(app, text="Bağlantıyı Kes", command=disconnect_serial)
disconnect_btn.pack(pady=5)

min_set_entry = ctk.CTkEntry(app, placeholder_text="Min Set (örn: 20)")
min_set_entry.pack(pady=10)

max_set_entry = ctk.CTkEntry(app, placeholder_text="Max Set (örn: 30)")
max_set_entry.pack(pady=10)

send_btn = ctk.CTkButton(app, text="Veri Gönder", command=send_data_to_arduino)
send_btn.pack(pady=5)

# Önceki min ve max set gösterimi
previous_min_set_label = ctk.CTkLabel(app, text="Önceki Min Set: -")
previous_min_set_label.pack(pady=5)

previous_max_set_label = ctk.CTkLabel(app, text="Önceki Max Set: -")
previous_max_set_label.pack(pady=5)

textbox = ctk.CTkTextbox(app, width=480, height=200)
textbox.pack(pady=10)

status_label = ctk.CTkLabel(app, text="Bağlantı Durumu: ⚪")
status_label.pack()

app.mainloop()
