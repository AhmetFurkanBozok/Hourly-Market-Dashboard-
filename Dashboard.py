import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

# --- 1. SAYFA AYARLARI ---
st.set_page_config(page_title="Piyasa Analiz Paneli", layout="wide")

# --- ŞİRKET SÖZLÜĞÜ (Havacılık ve Otomotiv Odaklı) ---
# Ticker sembollerini şirketlerin gerçek isimleriyle eşleştiriyoruz
sirketler = {
    "AIR.PA": "Airbus SE",
    "BA": "The Boeing Company",
    "F": "Ford Motor Company",
    "TSLA": "Tesla, Inc.",
    "THYAO.IS": "Türk Hava Yolları"
}

# --- YAN MENÜ (SIDEBAR) ---
st.sidebar.header("🛠️ Kontrol Paneli")

# Kullanıcıya şirketin ismini gösterip, arka planda ticker sembolünü alıyoruz (Extra UI Feature)
secilen_ticker = st.sidebar.selectbox(
    "Analiz Edilecek Şirketi Seçin", 
    options=list(sirketler.keys()), 
    format_func=lambda x: sirketler[x] # Kullanıcı ekranda sadece şirket adını görecek
)

goster_sma = st.sidebar.checkbox("Hareketli Ortalamayı (SMA) Göster", value=True)

# Seçilen şirketin adını başlığa dinamik olarak yazdırıyoruz
st.title(f"📊 {sirketler[secilen_ticker]} 1 Aylık Saatlik Analiz Paneli")
st.markdown("---")

# --- 2. VERİ ÇEKME VE SAKLAMA ---
@st.cache_data 
def load_data(ticker):
    stock = yf.Ticker(ticker)
    df = stock.history(period="1mo", interval="1h")
    
    df.reset_index(inplace=True) 
    
    if 'Date' in df.columns:
        df.rename(columns={'Date': 'Datetime'}, inplace=True)
    elif 'index' in df.columns:
        df.rename(columns={'index': 'Datetime'}, inplace=True)
        
    df.to_csv("hourly_data.csv", index=False)
    
    return df

# Kullanıcının yan menüden seçtiği hisseyi yüklüyoruz
df = load_data(secilen_ticker) 

# --- 3. EKSTRA İNDİKATÖR (Extra Effort) ---
df['SMA_20'] = df['Close'].rolling(window=20).mean() 

# --- 4. ARAYÜZ VE GRAFİKLER ---
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"{sirketler[secilen_ticker]} Fiyat Trendi")
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=df['Datetime'], y=df['Close'], mode='lines', name='Kapanış', line=dict(color='#1f77b4')))
    
    if goster_sma:
        fig_line.add_trace(go.Scatter(x=df['Datetime'], y=df['SMA_20'], mode='lines', name='SMA 20', line=dict(color='#ff7f0e')))
        
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader("Saatlik İşlem Hacmi")
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(x=df['Datetime'], y=df['Volume'], marker_color='#2ca02c'))
    st.plotly_chart(fig_bar, use_container_width=True)

st.subheader("Veri Tablosu")
st.dataframe(df)
