import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="E-Waste Management Platform", page_icon="🌱", layout="wide")

# Custom CSS for Sleek Top-Tab Portal Design
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stMetric { background-color: #ffffff; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); border-top: 4px solid #10b981; }
    .insight-box { background-color: #f0fdf4; padding: 16px; border-radius: 10px; border-left: 4px solid #22c55e; margin-top: 12px; color: #166534; font-size: 14px; }
    .card-box { background-color: #ffffff; padding: 24px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom: 20px; }
    h1 { font-size: 30px !important; color: #0f172a !important; font-weight: 800 !important; }
    </style>
""", unsafe_allow_html=True)

try:
    df_txn = pd.read_csv('data/ewaste_transactions.csv')
    df_recycle = pd.read_csv('data/recycling_yield.csv')
except:
    df_txn = pd.read_csv('../data/ewaste_transactions.csv')
    df_recycle = pd.read_csv('../data/recycling_yield.csv')

# Top Header Banner
st.title("🌱 แพลตฟอร์มจัดการซากผลิตภัณฑ์เครื่องใช้ไฟฟ้าและอิเล็กทรอนิกส์เพื่อสิ่งแวดล้อม")
st.markdown("**Business Idea Creation Dashboard** | ระบบรายงานสรุปภาพรวมธุรกิจและการขับเคลื่อนเศรษฐกิจหมุนเวียนอย่างยั่งยืน")
st.markdown("---")

# Modern Top Tabs (Clean Portal Style)
tab1, tab2, tab3, tab4 = st.tabs([
    "🏠 ภาพรวมโครงการ (Overview)", 
    "📊 วิเคราะห์ตลาดและ AI (Market & AI)", 
    "💰 รายได้และ ESG (Revenue & ESG)", 
    "📋 ข้อมูลธุรกรรม (Transactions)"
])

with tab1:
    st.markdown("### 📊 ตัวชี้วัดผลการดำเนินงานหลัก (Key Performance Indicators)")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("จำนวนอุปกรณ์ทั้งหมด", f"{len(df_txn)} เครื่อง", "+15% จากเดือนก่อน")
    col2.metric("ความปลอดภัยข้อมูล", "100%", "ผ่านมาตรฐานสากล")
    col3.metric("รายได้จากการรีไซเคิล", f"{df_recycle['recycling_revenue_thb'].sum():,.0f} บาท", "+22% จากเป้า")
    col4.metric("ลดคาร์บอน (Carbon Offset)", "1,240 กก.", "เทียบเท่าปลูกต้นไม้ 130 ต้น")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.subheader("🎯 วิสัยทัศน์และพันธกิจโครงการ")
        st.markdown("""
        * **Problem:** ขยะอิเล็กทรอนิกส์ล้นเมือง ผู้บริโภคกังวลเรื่องข้อมูลรั่วไหล (Data Leak)[cite: 2]
        * **Solution:** แพลตฟอร์มประเมินราคาด้วย AI พร้อมระบบลบข้อมูล (Data Wiping) ปลอดภัย 100%[cite: 2]
        * **Target:** ขยายผลในพื้นที่ EEC และเครือข่ายร้านค้าพาร์ทเนอร์ทั่วประเทศ[cite: 2]
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.subheader("🌍 ผลกระทบด้านสิ่งแวดล้อมหลัก")
        e1, e2 = st.columns(2)
        e1.metric("⚡ พลังงานประหยัด", "3,450 kWh", "เทียบไฟบ้าน 4 เดือน")
        e2.metric("💧 น้ำที่รักษาไว้", "12,800 ลิตร", "ลดมลพิษลงสู่ดิน")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.subheader("📊 วิเคราะห์ตลาดและประสิทธิภาพระบบ AI")
    st.markdown("แสดงสัดส่วนประเภทอุปกรณ์ที่ผู้ใช้งานนิยมนำมาเทิร์นผ่านระบบ AI[cite: 2]")
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.subheader("📱 สัดส่วนประเภทอุปกรณ์")
        fig_pie = px.pie(df_txn, names='device_type', hole=0.5, color_discrete_sequence=px.colors.qualitative.Safe)
        fig_pie.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=320)
        st.plotly_chart(fig_pie, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.subheader("💡 การวิเคราะห์พฤติกรรมลูกค้า (AI Insights)")
        st.markdown("""
        * **Smartphones & Laptops:** ครองสัดส่วนสูงสุดเนื่องจากมีข้อมูลส่วนบุคคลจัดเก็บอยู่มาก
        * **AI Pricing:** ประเมินราคาแม่นยำ รวดเร็ว ไม่ต้องเดินทางไปหน้าร้าน[cite: 2]
        * **Trust Factor:** ฟีเจอร์ Data Wiping สร้างความมั่นใจให้ผู้ใช้งาน 100%[cite: 2]
        """)
        st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.subheader("💰 โครงสร้างรายได้และผลตอบแทน (Revenue Streams)")
    st.markdown("การวิเคราะห์ผลกำไรจากการสกัดโลหะมีค่า (ทองคำ, ทองแดง) และบริการ B2B[cite: 2]")
    st.markdown("---")
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    fig_bar = px.bar(df_recycle, x='batch_id', y='recycling_revenue_thb', color='device_type',
                     text='recycling_revenue_thb', labels={'batch_id': 'รอบการรีไซเคิล', 'recycling_revenue_thb': 'รายได้รวม (บาท)'},
                     color_discrete_sequence=px.colors.qualitative.Bold)
    fig_bar.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=350)
    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown('<div class="insight-box">💡 <b>Financial Insight:</b> ล็อตการรีไซเคิลแล็ปท็อป (Laptop) สร้างรายได้สูงสุดต่อรอบ เนื่องจากมีสัดส่วนแผงวงจรที่มีทองคำและทองแดงบริสุทธิ์สูงตามโมเดล BMC[cite: 2]</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.subheader("📋 ฐานข้อมูลและรายงานธุรกรรม (Transactions Log)")
    st.markdown("บันทึกข้อมูลการรับซื้อ ตรวจสอบสภาพ และสถานะการจัดการซากอิเล็กทรอนิกส์แบบเรียลไทม์")
    st.markdown("---")
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.dataframe(df_txn, use_container_width=True)
    st.success("✅ ข้อมูลเชื่อมต่อกับระบบฐานข้อมูลเรียบร้อย พร้อมสำหรับการพรีเซนต์")
    st.markdown('</div>', unsafe_allow_html=True)
