# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import sqlite3
import os
from datetime import datetime
from lucy_data import MEMBERS, ALBUMS, CONCERT_GROWTH, ALBUM_SALES_GROWTH, MOOD_RECOMMENDATIONS

# Page Configuration
st.set_page_config(
    page_title="LUCY SPACE - 왈왈이들의 아지트",
    page_icon="🎻",
    layout="wide",
    initial_sidebar_state="collapsed" # Collapse sidebar by default for homepage view
)

# Load Custom Styles (HTML containing CSS <style>)
def load_styles(file_name):
    if os.path.exists(file_name):
        with open(file_name, encoding="utf-8") as f:
            st.markdown(f.read(), unsafe_allow_html=True)

load_styles("style.html")

# SQLite Database Setup for Guestbook
DB_FILE = "guestbook.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS cheers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            avatar TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_cheer(name, avatar, message):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO cheers (name, avatar, message, timestamp) VALUES (?, ?, ?, ?)",
              (name, avatar, message, now))
    conn.commit()
    conn.close()

def get_cheers():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT name, avatar, message, timestamp FROM cheers ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows

# Initialize DB
init_db()

# Session State Initialization
if "selected_album_idx" not in st.session_state:
    st.session_state.selected_album_idx = 0
if "selected_member" not in st.session_state:
    st.session_state.selected_member = None

# Helper to check and render image or placeholder (Light Theme optimized)
def render_image(image_path, label, filename):
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        placeholder_html = f"""
        <div class="img-placeholder">
            <div style="font-size: 36px; margin-bottom: 8px;">📷</div>
            <div style="font-weight: bold; margin-bottom: 4px; color: #0891b2;">{label}</div>
            <div style="font-size: 11px; opacity: 0.8; color: #475569;">
                assets/{filename} 경로에 이미지를 넣어주세요.
            </div>
        </div>
        """
        st.markdown(placeholder_html, unsafe_allow_html=True)

# Main Header (Homepage style)
st.markdown("<h1 class='gradient-title' style='font-size: 3.5rem; margin-top: 10px; margin-bottom: 5px;'>🎻 LUCY SPACE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #475569; font-weight: 500; margin-bottom: 25px;'>청춘을 노래하는 청량 밴드 루시(LUCY)의 공식 아지트</p>", unsafe_allow_html=True)

# Top Horizontal Menu (Segmented Tabs Layout)
tab_home, tab_members, tab_timeline, tab_growth, tab_recommend, tab_guestbook = st.tabs([
    "🏠 루시 소개 (Home)",
    "🎸 멤버 프로필 (Members)",
    "💿 앨범 타임라인 (Timeline)",
    "📈 성장 스토리 (Growth)",
    "💌 오늘의 감정 추천곡 (Recommendations)",
    "💬 왈왈이 응원보드 (Guestbook)"
])

# --- 1. HOME TAB ---
with tab_home:
    st.markdown("<h2 class='gradient-text-blue' style='font-size: 1.8rem; margin-bottom: 15px;'>🏠 루시의 세계로</h2>", unsafe_allow_html=True)
    
    # Hero Banner Section
    st.markdown(
        """
        <div class="glass-card" style="text-align: center; padding: 40px 20px; background: rgba(255, 255, 255, 0.9) !important; border: 1px solid rgba(6, 182, 212, 0.15) !important;">
            <h3 style="color: #0891b2; font-size: 2rem; margin-bottom: 15px; font-weight: 800;">청춘(靑春)과 청량(淸凉)을 노래하는 밴드, <b>LUCY</b></h3>
            <p style="font-size: 1.15rem; color: #334155; max-width: 850px; margin: 0 auto 20px auto; line-height: 1.8; font-weight: 400;">
                2019년 JTBC 오디션 프로그램 '슈퍼밴드' 준우승 결성 이후, 푸른 하늘과 흩날리는 바람, 
                숨차게 달리는 청춘의 순간들을 음악에 담아 대중에게 커다란 선물과 위로를 선사하는 4인조 하이브리드 팝락 밴드입니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Features Section
    st.markdown("### 🌟 루시(LUCY)만의 특별함과 매력 포인트")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div class="glass-card" style="height: 100%; background: white !important;">
                <h3 style="color: #0891b2; display: flex; align-items: center; margin-top:0;"><span style="font-size: 24px; margin-right: 8px;">🎻</span> 바이올린 리드 사운드</h3>
                <p style="font-size: 14px; color: #475569; line-height: 1.7;">
                    일반적인 밴드의 일렉트릭 기타 솔로나 키보드 대신, <b>리더 신예찬의 정열적인 바이올린 연주</b>가 리드 악기로 활약합니다. 
                    클래식한 우아함과 폭발적인 락 에너지가 만나 루시만의 독보적인 <b>'하이브리드 팝락(Hybrid Pop-Rock)'</b> 사운드를 완성합니다.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col2:
        st.markdown(
            """
            <div class="glass-card" style="height: 100%; background: white !important;">
                <h3 style="color: #059669; display: flex; align-items: center; margin-top:0;"><span style="font-size: 24px; margin-right: 8px;">🍃</span> 청춘(靑春)과 청량(淸凉)의 대명사</h3>
                <p style="font-size: 14px; color: #475569; line-height: 1.7;">
                    봄바람이 불어오는 기분 좋은 아침, 신나게 뛰는 오후의 러닝, 아련한 노을길의 밤하늘까지. 
                    듣는 것만으로도 눈앞에 푸른 풍경이 파노라마처럼 펼쳐지는 <b>맑고 청량한 밴드 에너지</b>로 온 세상을 가득 채웁니다.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col3:
        st.markdown(
            """
            <div class="glass-card" style="height: 100%; background: white !important;">
                <h3 style="color: #4f46e5; display: flex; align-items: center; margin-top:0;"><span style="font-size: 24px; margin-right: 8px;">🎧</span> 일상과 동화 속 엠비언스 & 가사</h3>
                <p style="font-size: 14px; color: #475569; line-height: 1.7;">
                    바람소리, 물소리, 지하철 안내음, 발걸음 소리 등 조원상 프로듀서가 직접 채집한 <b>일상 속 공간음(Ambience Sound)</b>을 
                    곡 곳곳에 녹여내어 생생함을 더합니다. 여기에 한 편의 문학 작품이나 동화 같은 시적이고 따뜻한 가사가 위로를 건넵니다.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    st.write("")
    
    # SuperBand Formation Story
    st.markdown("### 🏆 결성 스토리 : JTBC 슈퍼밴드가 낳은 최고의 선물")
    st.markdown(
        """
        <div class="glass-card" style="padding: 30px; background: white !important;">
            <div style="font-size: 15px; color: #334155; line-height: 1.8;">
                천재적인 베이시스트이자 프로듀서 <b>조원상</b>, 폭발적인 에너지를 가진 버스커 바이올리니스트 <b>신예찬</b>, 
                페루 유학 경력과 청아한 미성을 보유한 드러머/보컬 <b>신광일</b>이 오디션 프로그램 '슈퍼밴드'를 통해 뜻을 함께 모았습니다. 
                이후 보컬의 깊이를 더해줄 감성 보컬리스트 <b>최상엽</b>이 정식 합류하며 현재의 무적 4인조 <b>LUCY</b>가 탄생했습니다.<br><br>
                결성 초기부터 '지구상의 유일무이한 바이올린 록 밴드'라는 찬사를 받으며 매 무대 신선한 충격을 주었던 이들은, 
                현재 K-밴드 트렌드의 최전선에서 청량함과 예술성을 동시에 잡은 대표 아이콘으로 굳건히 자리매김하고 있습니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- 2. MEMBERS TAB ---
with tab_members:
    st.markdown("<h2 class='gradient-text-blue' style='font-size: 1.8rem; margin-bottom: 15px;'>🎸 멤버 소개 (4인 4색)</h2>", unsafe_allow_html=True)
    
    # Create 4 columns for 4 members
    cols = st.columns(4)
    
    for i, member in enumerate(MEMBERS):
        with cols[i]:
            st.markdown(f"<div class='member-card'>", unsafe_allow_html=True)
            
            # Display photo or placeholder
            render_image(member["image_path"], f"{member['name'].split()[0]} 프로필", f"{member['id']}.png")
            
            # Text Info (MBTI 제외 및 밝은 색상 반영)
            st.markdown(
                f"""
                <div style='margin-top: 15px;'>
                    <h3 style='margin-bottom: 5px; color: {member["color"]}; font-weight:800; font-size:1.3rem;'>{member["name"]}</h3>
                    <p style='margin: 4px 0; font-size: 13px; color: #64748b;'>🎂 {member["birth"]}</p>
                    <p style='margin: 4px 0; font-size: 14px; font-weight: bold; color: #1e293b;'>🎵 {member["role"]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Active Member Detail Toggle
            if st.button(f"상세 정보 확인", key=f"btn_{member['id']}", use_container_width=True):
                st.session_state.selected_member = member["id"]
                
            # Namuwiki Link
            st.markdown(
                f"""
                <a href='{member["namu_url"]}' target='_blank' style='text-decoration: none;'>
                    <button style='width: 100%; border: 1px solid rgba(0,0,0,0.1); background: #f8fafc; color: #475569; padding: 7px; border-radius: 8px; margin-top: 6px; cursor: pointer; font-size: 12px; font-weight:500;'>
                        나무위키 프로필 보기 ↗
                    </button>
                </a>
                """,
                unsafe_allow_html=True
            )
            st.markdown("</div>", unsafe_allow_html=True)
            
    # Render detail window below if selected
    if st.session_state.selected_member:
        selected_mem = next((m for m in MEMBERS if m["id"] == st.session_state.selected_member), None)
        if selected_mem:
            st.write("---")
            st.markdown(
                f"""
                <div class="glass-card" style="border-left: 5px solid {selected_mem['color']} !important; background: white !important; color: #1e293b;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h3 style="color: {selected_mem['color']}; margin: 0; font-weight:800;">✨ {selected_mem['name']} 상세 설명</h3>
                    </div>
                    <p style="font-size: 15px; line-height: 1.8; color: #334155; margin-top: 15px; font-weight: 400;">
                        {selected_mem['description']}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

# --- 3. TIMELINE TAB ---
with tab_timeline:
    import streamlit as st
    # 상단 타이틀 및 안내 문구
    st.markdown("<h2 class='gradient-text-blue' style='font-size: 1.8rem; margin-bottom: 15px;'>💿 앨범 타임라인 및 음반</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px; color: #475569; text-align: center; margin-bottom:15px;'>앨범을 클릭하여 수록곡 정보와 뮤직비디오를 확인해 보세요!</p>", unsafe_allow_html=True)

    # 2. 레이아웃 분할: 왼쪽(앨범 목록) 1 : 오른쪽(상세 정보) 2 비율
    col_menu, col_content = st.columns([1, 2])

    # 앨범 버튼용 옵션 텍스트 리스트 생성
    album_options = [f"[{album['type']}] {album['title']}  ({album['date']})" for album in ALBUMS]

    # 3. [왼쪽 영역] 세로 버튼 타임라인 목록
    with col_menu:
        st.markdown("<h4 style='color:#1e293b; font-weight:700; margin-bottom:10px;'>📅 앨범 목록</h4>", unsafe_allow_html=True)
    
    for idx, label in enumerate(album_options):
        # 현재 선택된 앨범 버튼은 primary(색상 강조), 나머지는 secondary 스타일 적용
        is_selected = (st.session_state.selected_album_idx == idx)
        btn_type = "primary" if is_selected else "secondary"
        
        # 버튼 생성 및 클릭 이벤트 처리 (드롭다운 대체)
        if st.button(label, key=f"album_btn_{idx}", type=btn_type, use_container_width=True):
            st.session_state.selected_album_idx = idx
            st.rerun()

    # 4. [오른쪽 영역] 선택된 앨범의 상세 정보 출력
    with col_content:
        # 현재 선택된 앨범 데이터 가져오기
        active_album = ALBUMS[st.session_state.selected_album_idx]
        
        # 오른쪽 영역 내부에서 다시 이미지(1)와 정보(2) 비율로 분할
        col_img, col_info = st.columns([1, 2])
    
    # 4-1. 오른쪽 내부의 왼쪽: 앨범 이미지 및 발매 정보 카드
    with col_img:
        # 기존 Album Cover render 함수 호출
        render_image(f"assets/{active_album['id']}.png", f"{active_album['title']} 앨범 커버", f"{active_album['id']}.png")
        st.write("")
        
        # 기존 발매일 및 앨범 구분 HTML 카드
        st.markdown(
            f"""
            <div style='background: white; padding: 15px; border-radius: 12px; border: 1px solid rgba(0,0,0,0.06); text-align: center;'>
                <span style='font-size: 13px; color: #64748b;'>발매일</span><br>
                <b style='font-size: 16px; color: #1e293b;'>{active_album['date']}</b><br><br>
                <span style='font-size: 13px; color: #64748b;'>앨범 구분</span><br>
                <b style='font-size: 16px; color: #1e293b;'>{active_album['type']}</b>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    # 4-2. 오른쪽 내부의 오른쪽: 제목, 소개글, 수록곡, 뮤직비디오
    with col_info:
        # 타이틀 및 타이틀곡 정보
        st.markdown(f"<h2 style='color: #0891b2; margin-bottom: 5px; font-weight:800; line-height:1.2;'>{active_album['title']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 16px; font-weight: bold; color: #059669;'>타이틀곡: {active_album['title_song']}</p>", unsafe_allow_html=True)
        st.write("---")
        
        # 앨범 정보 및 소개글
        st.markdown("<h5 style='color:#1e293b; font-weight:700;'>📖 앨범 정보 및 소개</h5>", unsafe_allow_html=True)
        st.write(active_album["info"])
        st.write("")
        
        # 수록곡 리스트 (TITLE 강조 포함)
        st.markdown("<h5 style='color:#1e293b; font-weight:700;'>🎵 수록곡 리스트</h5>", unsafe_allow_html=True)
        tracks_formatted = "\n".join([f"- **{track}**" if "[TITLE]" in track else f"- {track}" for track in active_album["tracks"]])
        st.markdown(tracks_formatted)
        st.write("")
        
        # 유튜브 뮤직비디오
        st.markdown(f"<h5 style='color:#1e293b; font-weight:700;'>🎬 '{active_album['title_song']}' 공식 뮤직비디오 감상</h5>", unsafe_allow_html=True)
        st.video(active_album["youtube_url"])


# --- 4. GROWTH STORY TAB ---
with tab_growth:
    st.markdown("<h2 class='gradient-text-blue' style='font-size: 1.8rem; margin-bottom: 15px;'>📈 루시의 성장 스토리</h2>", unsafe_allow_html=True)
    
    # Summary of growth
    st.markdown(
        """
        <div class="glass-card" style="padding: 25px; border-left: 5px solid #059669 !important; background: white !important;">
            <h4 style="color: #059669; margin-top:0; font-weight:800;">지속적인 커리어 하이 경신!</h4>
            <p style="font-size: 14.5px; line-height: 1.7; color: #334155; margin: 0;">
                루시는 공연 관객 수와 첫 주 앨범 판매량(초동) 모두에서 <b>가파른 우상향 그래프</b>를 그리는 
                대표적인 '계단식 성장형' 밴드입니다. 2021년 첫 단독 콘서트 이후 약 5년 만에 공연 관객 동원력은 
                <b>8.8배 이상</b>, 앨범 판매량은 첫 피지컬 대비 무려 <b>121배 이상</b> 비약적으로 상승하며 K-밴드씬의 대세 주자로 확고히 자리 잡았습니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Tabs for the two growth metrics
    tab_concert, tab_sales = st.tabs(["🎪 단독 콘서트 관객 수", "💿 앨범 초동 판매량"])
    
    with tab_concert:
        st.markdown("### 🎪 연도별 단독 콘서트 관객 동원력 추이")
        st.write("루시는 라이브 무대에서 진가를 발휘하며 매 활동마다 대형 콘서트 홀로 진출하고 있습니다.")
        
        chart_data_concert = CONCERT_GROWTH.copy()
        chart_data_concert = chart_data_concert.set_index("시기")
        
        col_chart, col_summ = st.columns([2, 1])
        with col_chart:
            st.bar_chart(chart_data_concert["관객수"], color="#06B6D4")
            
        with col_summ:
            st.markdown(
                """
                <div style='background: white; padding: 20px; border-radius: 12px; border: 1px solid rgba(0,0,0,0.06);'>
                    <h4 style='color: #0891b2; margin-top: 0; font-weight:700;'>주요 이정표</h4>
                    <ul style='font-size: 13px; color: #334155; padding-left: 20px; line-height:1.7;'>
                        <li><b>2021.06</b>: 첫 단독 콘서트 1,700명 규모 매진</li>
                        <li><b>2022.03</b>: 첫 정규 앨범 기념 3,000명 동원</li>
                        <li><b>2023.08</b>: 장충체육관 5회 단독 7,600명 돌파 (4.4배 성장)</li>
                        <li><b>2026.05</b>: 대망의 <b>체조경기장(KSPO DOME)</b> 입성! 양일간 15,000명 이상의 관객을 동원하며 탑티어 밴드로 우뚝 섰습니다.</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    with tab_sales:
        st.markdown("### 💿 앨범 첫 주 판매량 (초동) 성장 추이")
        st.write("루시를 향한 팬덤(왈왈이)의 뜨거운 성원과 대중성의 확장을 보여주는 지표입니다.")
        
        chart_data_sales = ALBUM_SALES_GROWTH.copy()
        chart_data_sales = chart_data_sales.set_index("시기")
        
        col_chart2, col_summ2 = st.columns([2, 1])
        with col_chart2:
            st.bar_chart(chart_data_sales["판매량"], color="#10B981")
            
        with col_summ2:
            st.markdown(
                """
                <div style='background: white; padding: 20px; border-radius: 12px; border: 1px solid rgba(0,0,0,0.06);'>
                    <h4 style='color: #059669; margin-top: 0; font-weight:700;'>성장률 요약</h4>
                    <ul style='font-size: 13px; color: #334155; padding-left: 20px; line-height:1.7;'>
                        <li><b>PANORAMA</b>: 초동 약 850장으로 출발</li>
                        <li><b>Childhood</b>: 데뷔 후 첫 정규 음반 초동 24,000장</li>
                        <li><b>열 (10)</b>: 탄탄한 성장 가도를 달리며 초동 64,000장 돌파</li>
                        <li><b>Childish</b>: 정규 2집 발매 첫 주 만에 <b>103,562장</b> 돌파로 첫 <b>초동 10만 장 돌파(커리어하이)</b> 달성! 데뷔 앨범 대비 <b>121배 성장</b></li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )

# --- 5. RECOMMENDATIONS TAB ---
with tab_recommend:
    st.markdown("<h2 class='gradient-text-blue' style='font-size: 1.8rem; margin-bottom: 15px;'>💌 오늘의 감정 추천곡</h2>", unsafe_allow_html=True)
    
    # Selection options instead of text input
    st.markdown("### 🤔 지금 당신의 기분이나 상황은 어떤가요?")
    
    options = [rec["option_text"] for rec in MOOD_RECOMMENDATIONS]
    selected_option = st.radio("아래 선택지 중 가장 공감되는 상태를 선택해 주세요:", options)
    
    matched_rec = next((rec for rec in MOOD_RECOMMENDATIONS if rec["option_text"] == selected_option), None)
    
    if matched_rec:
        st.write("---")
        
        col_rec_info, col_rec_vid = st.columns([1, 1])
        
        with col_rec_info:
            st.markdown(
                f"""
                <div class="glass-card" style="border-left: 5px solid #06b6d4 !important; background: white !important; color: #1e293b; height: 100%;">
                    <span style="font-size: 12px; background: rgba(6,182,212,0.1); color: #0891b2; padding: 4px 10px; border-radius: 20px; font-weight: bold;">
                        RECOMMENDED SONG
                    </span>
                    <h2 style="color: #0f172a; margin-top: 15px; margin-bottom: 2px; font-weight:800;">{matched_rec['song']}</h2>
                    <p style="color: #64748b; font-size: 14px;">앨범: {matched_rec['album']}</p>
                    
                    <div style="background: #f8fafc; border-left: 3px solid #10b981; padding: 12px; margin: 20px 0; border-radius: 0 8px 8px 0;">
                        <span style="font-size: 12px; color: #059669; font-weight: bold; display: block; margin-bottom: 5px;">✍️ 왈왈이 감성 킬링 가사</span>
                        <i style="color: #1e293b; font-size: 14.5px; font-weight:500;">{matched_rec['lyric']}</i>
                    </div>
                    
                    <p style="font-size: 14px; line-height: 1.7; color: #475569; margin-bottom: 0;">
                        {matched_rec['description']}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        with col_rec_vid:
            st.markdown(f"##### 🎬 '{matched_rec['song']}' 공식 뮤직비디오 바로 감상하기")
            st.video(matched_rec["youtube_url"])

# --- 6. GUESTBOOK TAB ---
with tab_guestbook:
    st.markdown("<h2 class='gradient-text-blue' style='font-size: 1.8rem; margin-bottom: 15px;'>💬 왈왈이 응원보드 (방명록)</h2>", unsafe_allow_html=True)
    
    col_form, col_board = st.columns([1, 2])
    
    with col_form:
        st.markdown("### 💌 응원 남기기")
        
        with st.form("cheer_form", clear_on_submit=True):
            name = st.text_input("닉네임", max_chars=15, placeholder="왈왈이 닉네임 입력")
            
            # Emoji Avatar Selector
            avatars = ["🐶", "🎻", "🍀", "🎸", "🥁", "🦊", "🐱", "🦁", "🐰", "🦄", "🌈", "🔥"]
            avatar = st.selectbox("대표 아바타 선택", avatars)
            
            message = st.text_area("응원의 한마디", max_chars=200, placeholder="루시에게 힘이 되는 메시지를 작성해주세요. (최대 200자)")
            
            submit_btn = st.form_submit_button("방명록 남기기", use_container_width=True)
            
            if submit_btn:
                if not name.strip():
                    st.error("닉네임을 입력해 주세요!")
                elif not message.strip():
                    st.error("응원의 메시지를 입력해 주세요!")
                else:
                    save_cheer(name.strip(), avatar, message.strip())
                    st.success("응원 메시지가 소중하게 등록되었습니다! 🎉")
                    st.rerun()
                    
    with col_board:
        st.markdown("### 💬 왈왈이들의 한마디 실시간 현황")
        
        cheers = get_cheers()
        
        if not cheers:
            st.info("아직 등록된 응원이 없습니다. 첫 번째 왈왈이가 되어 메시지를 남겨보세요!")
        else:
            for cheer_name, cheer_avatar, cheer_msg, cheer_time in cheers:
                st.markdown(
                    f"""
                    <div class="cheer-card">
                        <div class="cheer-header">
                            <span class="cheer-avatar">{cheer_avatar}</span>
                            <span class="cheer-name">{cheer_name}</span>
                            <span class="cheer-date">{cheer_time}</span>
                        </div>
                        <div class="cheer-msg">{cheer_msg}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
