import tkinter as tk
import tkinter as tk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")

def hasil_prediksi():
    label_hasil.config(text="Hasil Prediksi: Teknologi Informasi")

    root = tk.Tk()
   root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="#244fbd")
root.resizable(False, False)

frame = tk.Frame(root, bg="#244fbd", padx=30, pady=25)
frame.pack(fill="both", expand=True)

label_judul = tk.Label(
     frame,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 17, "bold"),
    fg="white",
    bg="#244fbd"
)
label_judul.grid(row=0, column=0, columnspan=2, pady=(0, 25))

input_nilai = []

for i in range(10):
    label_mapel = tk.Label(
        frame,
        text=f"Nilai Mata Pelajaran {i + 1}:",
        font=("Arial", 10),
        fg="white",
        bg="#244fbd",
        anchor="w"
    )
    label_mapel.grid(
        row=i + 1, column=0, sticky="w",
        padx=(0, 12), pady=5
    )
