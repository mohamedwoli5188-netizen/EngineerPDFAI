import streamlit as st

from pages.Dashboard import show as dashboard_show
from pages.Upload_Project import show as upload_show
from pages.BOQ_Analyzer import show as boq_show
from pages.BOQ_Coefficient_AI import show as coeff_show
from pages.PPA_Calculator import show as ppa_show
from pages.Price_Adjustment import show as adjustment_show
from pages.Forecasting import show as forecast_show
from pages.Project_Run import show as project_show
from pages.Reports import show as reports_show
from pages.Database import show as database_show
from pages.Settings import show as settings_show
from pages.About import show as about_show

st.set_page_config(page_title="EngineerPDFAI", layout="wide")

pages = {
    "Dashboard": dashboard_show,
    "Upload Project": upload_show,
    "BOQ Analyzer": boq_show,
    "BOQ Coefficient AI": coeff_show,
    "PPA Calculator": ppa_show,
    "Price Adjustment": adjustment_show,
    "Forecasting": forecast_show,
    "Project Run": project_show,
    "Reports": reports_show,
    "Database": database_show,
    "Settings": settings_show,
    "About": about_show,
}

choice = st.sidebar.radio("📑 Navigation", list(pages.keys()))

pages[choice]()
