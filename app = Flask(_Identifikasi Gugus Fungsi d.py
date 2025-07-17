app = Flask("Identifikasi Gugus Fungsi dan Tata Nama Senyawa Organik")

# Kamus sederhana untuk mengenali gugus fungsi berdasarkan pola string
gugus_fungsi_kamus = {
    'COOH': 'Asam Karboksilat',
    'CHO': 'Aldehid',
    'CO': 'Keton',
    'OH': 'Alkohol',
    'NH2': 'Amina',
    'COO': 'Ester',
    'C=C': 'Alkena',
    'C≡C': 'Alkuna'
}

# Fungsi sederhana untuk mengenali gugus fungsi
def identifikasi_gugus_fungsi(rumus):
    hasil = []
    for gugus, nama in gugus_fungsi_kamus.items():
        if gugus in rumus:
            hasil.append(nama)
    return hasil if hasil else ['Tidak teridentifikasi']

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil_gugus = []
    nama_senyawa = ''
    rumus = ''

    if request.method == 'POST':
        rumus = request.form['rumus']
        hasil_gugus = identifikasi_gugus_fungsi(rumus)

        # Tata nama sangat sederhana berdasarkan prioritas gugus
        if 'Asam Karboksilat' in hasil_gugus:
            nama_senyawa = f"Asam {rumus.lower()}"
        elif 'Aldehid' in hasil_gugus:
            nama_senyawa = f"{rumus.lower()} - al"
        elif 'Keton' in hasil_gugus:
            nama_senyawa = f"{rumus.lower()} - on"
        elif 'Alkohol' in hasil_gugus:
            nama_senyawa = f"{rumus.lower()} - ol"
        elif 'Amina' in hasil_gugus:
            nama_senyawa = f"{rumus.lower()} - amina"
        else:
            nama_senyawa = f"Tidak diketahui"

    return render_template('index.html', hasil_gugus=hasil_gugus, nama_senyawa=nama_senyawa, rumus=rumus)

if _name_ == '_main_':
    app.run(debug=True)