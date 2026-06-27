import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="Enterprise Data Pipeline", layout="wide")
st.title("📡 Enterprise Network Transaction Pipeline")
st.subheader("Automated Data Processing & Financial Analytics Engine")
st.markdown("---")

@st.cache_data
def generate_telecom_data():
    np.random.seed(42)
    num_records = 5000
    start_date = datetime.now() - timedelta(days=30)
    date_list = [start_date + timedelta(minutes=int(i)) for i in np.random.randint(0, 43200, num_records)]
    services = ['Mobile Data Bundle', 'Voice Call Minute', 'Mobile Money Transfer', 'SMS Value Pack']
    status_options = ['SUCCESS', 'SUCCESS', 'SUCCESS', 'FAILED']
    regions = ['Greater Accra', 'Ashanti', 'Western', 'Eastern', 'Northern']
    
    data = {
        'Timestamp': date_list,
        'Transaction_ID': [f"TXN-{100000 + i}" for i in range(num_records)],
        'Service_Type': np.random.choice(services, num_records),
        'Region': np.random.choice(regions, num_records),
        'Data_Volume_MB': np.where(np.random.choice(services, num_records) == 'Mobile Data Bundle', np.random.randint(50, 5000, num_records), 0),
        'Revenue_GHS': np.round(np.random.uniform(1.00, 150.00, num_records), 2),
        'Status': np.random.choice(status_options, num_records)
    }
    return pd.DataFrame(data).sort_values(by='Timestamp')

df = generate_telecom_data()
successful_txns = df[df['Status'] == 'SUCCESS']
total_revenue = successful_txns['Revenue_GHS'].sum()
total_data_traffic = df['Data_Volume_MB'].sum() / 1024
failed_count = len(df[df['Status'] == 'FAILED'])

col1, col2, col3 = st.columns(3)
with col1: st.metric(label="Processed Gross Revenue", value=f"GH₵ {total_revenue:,.2f}")
with col2: st.metric(label="Total Network Traffic Volume", value=f"{total_data_traffic:,.2f} GB")
with col3: st.metric(label="System Failure Logs Flagged", value=f"{failed_count:,} Errors", delta=f"{failed_count:,} Errors", delta_color="inverse")

st.markdown("### 🔍 Real-Time Stream Ingestion Ledger")
selected_service = st.selectbox("Select Service Vector:", ['All Services'] + list(df['Service_Type'].unique()))
filtered_df = df if selected_service == 'All Services' else df[df['Service_Type'] == selected_service]
st.dataframe(filtered_df, use_container_width=True)
st.caption("🔒 Architecture managed via Git Source Control. Compliant with telecom logging standards.")
