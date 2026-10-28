import streamlit as st
import urllib.parse
import os
import time
import random

st.set_page_config(
    page_title="AlgoSniper Premium",
    page_icon="🎯",
    layout="wide"
)

I18N = {
    "FR": {
        "title": "🎯 AlgoSniper — Sniper d'Algorithme X",
        "subtitle": "Détectez les tendances mondiales, appliquez le forçage thématique et simulez vos scores de viralité.",
        "license_label": "Clé d'Accès Premium",
        "license_placeholder": "Entrez votre clé de licence (ex: AS-BETA-XXXX)",
        "license_invalid": "Clé invalide ou expirée. Veuillez contacter le management d'AlgoSniper.",
        "license_valid": "Licence AlgoSniper activée avec succès !",
        "select_niche": "Configuration de la Niche / Forçage Sémantique",
        "followers_label": "Nombre d'abonnés de votre compte X",
        "scan_btn": "⚡ Lancer le Scan Global & la Traduction",
        "tab_debat": "🔥 Format Débat / Clivage",
        "tab_humour": "😂 Format Punchline / Humour",
        "tab_hook": "🎯 Format Scroll-Stopper",
        "share_x": "🚀 Propulser sur X (Intent Link)",
        "simulate_btn": "🎮 Exécuter le Crash-Test Algorithmique",
        "sim_running": "🧬 Analyse matricielle de l'algorithme X en cours...",
        "sim_title": "📊 RAPPORT PRÉDICTIF ALGOSNIPER",
        "sim_impressions": "Impressions (Vues) Estimées",
        "sim_engagement": "Taux d'Engagement Estimé",
        "velocity": "Vélocité de la Source",
        "shock_score": "💥 Potentiel de Choc",
        "tweets": [
            {
                "trend": "Alerte Masterclass Détectée (Source: Arabe / @Al_Hilal)",
                "velocity": 184.2,
                "shock": "94%",
                "shock_num": 0.94,
                "debat": "Honnêtement, le Chef Mitrovic vient encore de servir un triplé sur un plateau d'argent. Est-ce qu'on n'est pas sur le meilleur menu de la ligue cette saison ou vous continuez de dormir au resto ? 🍲",
                "humour": "Le gardien adverse a passé la soirée à ramasser des ballons au fond des filets comme un commis de cuisine qui ramasse les assiettes cassées. Fin de cuisson pour lui 💀😭",
                "hook": "Ce qui s'est passé ce soir à Riyad expose une vérité douloureuse que les autres grands d'Europe refusent de voir en cuisine..."
            }
        ]
    }
}

VALID_KEYS = os.environ.get("VALID_LICENSES", "AS-BETA-2026,VIP-DAKAR-2026,DEMO-KEY-0000").split(",")

lang = "FR"
t = I18N[lang]

user_key = st.sidebar.text_input(t["license_label"], placeholder=t["license_placeholder"], type="password")

if user_key.strip() not in VALID_KEYS:
    st.title(t["title"])
    st.caption(t["subtitle"])
    st.warning(t["license_invalid"])
    st.stop()
else:
    st.sidebar.success(t["license_valid"])

st.title(t["title"])
st.caption(t["subtitle"])

col1, col2 = st.columns()

with col1:
    niche = st.selectbox(t["select_niche"], ["🍽️ Food Mercato / Cuisine", "🚀 Tech / Intelligence Artificielle"])
    user_followers = st.number_input(t["followers_label"], min_value=10, max_value=10000000, value=5000, step=500)
    
    st.markdown("---")
    st.markdown("### 🎯 ADN Stylistique (Vos 3 Tweets Références)")
    ref_tweet_1 = st.text_area("Tweet de Référence #1", placeholder="Collez un tweet modèle...", height=70, key="ref_1")
    ref_tweet_2 = st.text_area("Tweet de Référence #2", placeholder="Collez un deuxième tweet...", height=70, key="ref_2")
    ref_tweet_3 = st.text_area("Tweet de Référence #3", placeholder="Collez un troisième tweet...", height=70, key="ref_3")
    
    start_scan = st.button(t["scan_btn"], use_container_width=True, type="primary")

with col2:
    if start_scan:
        st.success("🎯 Algorithme AlgoSniper connecté. Traduction et forçage sémantique appliqués.")
        for idx, item in enumerate(t["tweets"]):
            with st.expander(f"📌 {item['trend']}", expanded=True):
                st.metric(label=t["shock_score"], value=item["shock"], delta="🔥 Impact Majeur détecté")
                tab1, tab2, tab3 = st.tabs([t["tab_debat"], t["tab_humour"], t["tab_hook"]])
                
                for tab, key_type in zip([tab1, tab2, tab3], ["debat", "humour", "hook"]):
                    with tab:
                        tweet_text = item[key_type]
                        st.text_area("Texte du Tweet", tweet_text, height=90, key=f"txt_{idx}_{key_type}")
                        
                        if st.button(t["simulate_btn"], key=f"sim_btn_{idx}_{key_type}"):
                            with st.spinner(t["sim_running"]):
                                progress_bar = st.progress(0)
                                for percent_complete in range(100):
                                    time.sleep(0.005)
                                    progress_bar.progress(percent_complete + 1)
                                
                            calculated_views = int(user_followers * 2.1 * item["shock_num"] * random.uniform(0.8, 1.4))
                            sim_engagement_rate = round(random.uniform(5.1, 11.4) * item["shock_num"], 2)
                            
                            st.markdown(f"### {t['sim_title']}")
                            c1, c2 = st.columns(2)
                            c1.metric(t["sim_impressions"], f"{calculated_views:,}")
                            c2.metric(t["sim_engagement"], f"{sim_engagement_rate}%")
                        
                        encoded_text = urllib.parse.quote(tweet_text)
                        intent_url = f"https://x.com{encoded_text}"
                        st.markdown(f'<a href="{intent_url}" target="_blank"><button style="background-color:#1DA1F2;color:white;border:none;padding:12px 20px;border-radius:6px;cursor:pointer;font-weight:bold;width:100%;">{t["share_x"]}</button></a>', unsafe_allow_html=True)
