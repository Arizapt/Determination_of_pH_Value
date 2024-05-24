import streamlit as st

def show_splash_screen():
    st.title('Penentuan Nilai pH')
    st.markdown("---")
    st.write("Aplikasi ini akan membantu Anda menentukan sifat asam basa berdasarkan nama sampel yang dimasukkan.")

def main():
    # Apply custom CSS for background image
    add_background()

    show_splash_screen()

    # Dictionary to store pH categories, colors, and definitions
    ph_categories = {
        "BASA KUAT": (11, 14, "#8A2BE2", 
                      "Basa kuat adalah larutan dengan pH tinggi, yang berarti konsentrasi ion OH- dalam larutan tinggi. "
                      "Kegunaan Basa Kuat termasuk dalam produk pembersih rumah tangga, "
                      "pembuatan kertas, sabun, minuman ringan, pengawet makanan, dan obat-obatan."),
        "BASA LEMAH": (9, 10, "#800080", 
                       "Basa lemah adalah larutan dengan pH sedang, yang berarti konsentrasi ion OH- dalam larutan sedang. "
                       "Kegunaan Basa Lemah termasuk menyesuaikan atau menetralkan pH, pembuatan pupuk, "
                       "pemisahan senyawa organik, produksi kertas, dan menyesuaikan pH tanah."),
        "BASA SANGAT LEMAH": (8, 8, "#0000FF", 
                              "Basa sangat lemah adalah larutan dengan pH rendah, yang berarti konsentrasi ion OH- dalam larutan rendah. "
                              "Kegunaan Basa Sangat Lemah termasuk menyesuaikan atau menetralkan pH, pembuatan pupuk, "
                              "dan produksi kertas."),
        "NETRAL": (7, 7, "#008000", 
                   "Netral adalah larutan dengan pH netral, yang berarti konsentrasi ion H+ dan OH- dalam larutan seimbang. "
                   "Kegunaan pH netral sebagai air mineral yang diminum sehari-hari oleh manusia."), 
        "ASAM SANGAT LEMAH": (6, 6, "#FFFF00", 
                              "Asam sangat lemah adalah larutan dengan pH rendah, yang berarti konsentrasi ion H+ dalam larutan sedang. "
                              "Kegunaan Asam Sangat Lemah termasuk sebagai etchant gigi, aditif makanan, pendispersi, "
                              "fluks, inhibitor karat, elektrolit, bahan baku pupuk, dan produk pembersih rumah."),
        "ASAM LEMAH": (4, 5, "#FFA500", 
                       "Asam lemah adalah larutan dengan pH rendah, yang berarti konsentrasi ion H+ dalam larutan sedang. "
                       "Kegunaan Asam Lemah termasuk sebagai etchant gigi, aditif makanan, pendispersi, "
                       "fluks, inhibitor karat, elektrolit, bahan baku pupuk, dan produk pembersih rumah."),
        "ASAM KUAT": (1, 3, "#FF0000", 
                      "Asam kuat adalah larutan dengan pH sangat rendah, yang berarti konsentrasi ion H+ dalam larutan tinggi. "
                      "Kegunaan Asam Kuat termasuk cairan pengisi aki motor, bahan pupuk kimia, "
                      "dan pembersih logam dari korosi.")
    }

    # Dictionary to map sample names to pH categories
    sample_to_ph = {
        "Asam lambung": "ASAM KUAT",
        "Jeruk": "ASAM KUAT",
        "Apel": "ASAM KUAT",
        "Kopi hitam": "ASAM LEMAH",
        "Tomat": "ASAM LEMAH",
        "Susu": "ASAM SANGAT LEMAH",
        "Air": "NETRAL",
        "Sabun": "BASA SANGAT LEMAH",
        "Soda kue": "BASA LEMAH",
        "Natrium Hidroksida": "BASA KUAT",
        "Amonia": "BASA KUAT",
        "HCL": "ASAM KUAT",
        "NaOH": "BASA KUAT", 
        "NH3": "BASA KUAT",
        "Jus lemon": "ASAM KUAT",
        "Asam lemak": "ASAM KUAT",
        "Cuka": "ASAM KUAT",
        "Yogurt": "ASAM LEMAH",
        "Air hujan": "ASAM SANGAT LEMAH",
        "Telur": "ASAM SANGAT LEMAH",
        "Bayam": "ASAM SANGAT LEMAH",
        "Larutan soda": "BASA SANGAT LEMAH",
        "Buffer fosfat": "BASA SANGAT LEMAH",
        "Pemutih": "BASA LEMAH",
        "Soda api": "BASA LEMAH",
        "Larutan kapur": "BASA LEMAH",
        "Larutan limbah": "BASA KUAT",
        "Pembasmi lumpur": "BASA KUAT",
        "Beton basa": "BASA KUAT",
        "Air kapur jenuh": "BASA KUAT",
        "Sabun cuci": "BASA KUAT"
    }

    sample_name = st.text_input('Masukkan nama sampel:')

    if sample_name in sample_to_ph:
        ph_category = sample_to_ph[sample_name]
        min_val, max_val, color, definition = ph_categories[ph_category]
        st.markdown(f"<p style='color:{color}; font-size: 24px;'>Nama Sampel: <strong>{sample_name}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{color}; font-size: 24px;'>Sifat Asam Basa: <strong>{ph_category}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{color}; font-size: 18px;'>Nilai pH: <strong>{min_val} - {max_val}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:black; font-size: 18px;'>Pengertian: {definition}</p>", unsafe_allow_html=True)
    elif sample_name:
        st.write("Nama sampel tidak dikenali. Silakan coba lagi.")

def add_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: url("https://themeliorist.ca/wp-content/uploads/2020/12/%E2%80%94Pngtree%E2%80%94vector-design-background-of-scientist_1160371.png");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
