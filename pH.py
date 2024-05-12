import streamlit as st

def show_splash_screen():
    st.title('Penentuan Nilai pH')
    st.markdown("---")
    st.write("Aplikasi ini akan membantu Anda menentukan sifat asam basa berdasarkan nilai pH yang dimasukkan.")

def main():
    show_splash_screen()

    # Dictionary to store pH categories, colors, and examples
    ph_categories = {
        "BASA KUAT": (11, 14, "#8A2BE2", "Amonia dan Larutan Alkali", "Basa kuat adalah larutan dengan pH tinggi, yang berarti konsentrasi ion OH- dalam larutan tinggi. Contohnya adalah larutan amonia dan larutan alkali."),
        "BASA LEMAH": (9, 10, "#800080", "Soda Kue dan Sabun", "Basa lemah adalah larutan dengan pH sedang, yang berarti konsentrasi ion OH- dalam larutan sedang. Contohnya adalah soda kue dan sabun."),
        "BASA SANGAT LEMAH": (8, 8, "#0000FF", "Sabun", "Basa sangat lemah adalah larutan dengan pH rendah, yang berarti konsentrasi ion OH- dalam larutan rendah. Contohnya adalah sabun."),
        "NETRAL": (7, 7, "#008000", "Air", "Netral adalah larutan dengan pH netral, yang berarti konsentrasi ion H+ dan OH- dalam larutan seimbang. Contohnya adalah air."),
        "ASAM SANGAT LEMAH": (6, 6, "#FFFF00", "Susu", "Asam sangat lemah adalah larutan dengan pH rendah, yang berarti konsentrasi ion H+ dalam larutan sedang. Contohnya adalah susu."),
        "ASAM LEMAH": (4, 5, "#FFA500", "Kopi Hitam, Tomat", "Asam lemah adalah larutan dengan pH rendah, yang berarti konsentrasi ion H+ dalam larutan sedang. Contohnya adalah kopi hitam dan tomat."),
        "ASAM KUAT": (1, 3, "#FF0000", "Gastric acid, Jeruk, Apel", "Asam kuat adalah larutan dengan pH sangat rendah, yang berarti konsentrasi ion H+ dalam larutan tinggi. Contohnya adalah asam lambung, jeruk, dan apel.")
    }

    nilai = st.number_input('Masukkan nilai pH:', min_value=0.0, max_value=14.0, value=7.0, step=0.1)

    ph_category, color, example, definition = get_ph_category(nilai, ph_categories)
    
    st.markdown(f"<p style='color:{color}; font-size: 24px;'>Sifat Asam Basa = <strong>{ph_category}</strong></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:{color}; font-size: 18px;'>Contoh = <em>{example}</em></p>", unsafe_allow_html=True)
    st.write(f"Pengertian: {definition}")

def get_ph_category(nilai, categories):
    for category, (min_val, max_val, color, example, definition) in categories.items():
        if min_val <= nilai <= max_val:
            return category, color, example, definition
    return 'Nilai pH di luar rentang yang valid.', '', '', ''

if __name__ == "__main__":
    main()
