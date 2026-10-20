
import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("540x760")
root.configure(bg="#244fbd")
root.resizable(False, False)

# Daftar jurusan
daftar_jurusan = [
    "Teknologi Informasi",
    "Teknik Sipil",
    "Teknik Elektro",
    "Teknik Mesin",
    "Rekayasa Otomotif",
    "Rekayasa Elektro Medis"
]

# Fungsi hasil prediksi
def hasil_prediksi():
    label_hasil.config(
        text=f"Hasil Prediksi: {pilihan_jurusan.get()}"
    )

# Frame utama
frame = tk.Frame(
    root,
    bg="#244fbd",
    padx=30,
    pady=25
)
frame.pack(fill="both", expand=True)

# Judul aplikasi
label_judul = tk.Label(
    frame,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 17, "bold"),
    fg="white",
    bg="#244fbd"
)
label_judul.grid(
    row=0, column=0,
    columnspan=2, pady=(0, 20)
)

# Sepuluh input nilai mata pelajaran
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
        row=i + 1, column=0,
        sticky="w", padx=(0, 10), pady=5
    )

    entry = tk.Entry(
        frame,
        width=18,
        font=("Arial", 10),
        justify="center"
    )
    entry.grid(
        row=i + 1, column=1,
        sticky="ew", pady=5
    )
    input_nilai.append(entry)

# Label pilihan jurusan
label_pilihan = tk.Label(
    frame,
    text="Pilihan Jurusan Anda:",
    font=("Arial", 10, "bold"),
    fg="white",
    bg="#244fbd"
)
label_pilihan.grid(
    row=11, column=0,
    columnspan=2, pady=(18, 6)
)

# Dropdown pilihan jurusan
pilihan_jurusan = tk.StringVar(
    value=daftar_jurusan[0]
)

dropdown_jurusan = tk.OptionMenu(
    frame,
    pilihan_jurusan,
    *daftar_jurusan
)
dropdown_jurusan.config(
    font=("Arial", 10),
    width=25,
    bg="white",
    fg="#244fbd"
)
dropdown_jurusan.grid(
    row=12, column=0,
    columnspan=2, pady=5
)

# Tombol hasil prediksi
tombol_prediksi = tk.Button(
    frame,
    text="Hasil Prediksi",
    command=hasil_prediksi,
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#244fbd",
    padx=12,
    pady=6,
    cursor="hand2"
)
tombol_prediksi.grid(
    row=13, column=0,
    columnspan=2, pady=15
)

# Label hasil prediksi
label_hasil = tk.Label(
    frame,
    text="Hasil Prediksi: -",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#244fbd",
    wraplength=450
)
label_hasil.grid(
    row=14, column=0,
    columnspan=2, pady=5
)

# Menjalankan aplikasi
root.mainloop()
