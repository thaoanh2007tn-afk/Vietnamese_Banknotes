import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

st.set_page_config(
    page_title="Nhận Diện Tiền Việt Nam",
    page_icon="🇻🇳",
    layout="wide"
)

st.markdown("""
<style>
/* ─── Google Fonts ─────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Be+Vietnam+Pro:wght@300;400;600&display=swap');

/* ─── Biến màu ──────────────────────────────────────────────── */
:root {
    --do:       #C8102E;
    --do-dam:   #8B0000;
    --vang:     #F5C518;
    --vang-nhat:#FFF9E6;
    --kem:      #FBF5E6;
    --nau:      #5C3A1E;
    --xanh:     #1B4D3E;
    --trang:    #FFFFFF;
    --bong:     0 8px 32px rgba(200,16,46,0.15);
}

/* ─── Nền tổng thể ──────────────────────────────────────────── */
.stApp {
    background-color: var(--kem);
    background-image:
        radial-gradient(circle at 10% 20%,  rgba(245,197,24,0.08)  0%, transparent 50%),
        radial-gradient(circle at 90% 80%,  rgba(200,16,46,0.06)   0%, transparent 50%),
        url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23C8102E' fill-opacity='0.03'%3E%3Cpath d='M30 0 L35 10 L45 10 L37 16 L40 27 L30 21 L20 27 L23 16 L15 10 L25 10 Z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    font-family: 'Be Vietnam Pro', sans-serif;
}

/* ─── Ẩn toolbar mặc định ────────────────────────────────── */
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 1rem; padding-bottom: 2rem; max-width: 1100px;}

/* ─── BANNER ─────────────────────────────────────────────────── */
.banner {
    background: linear-gradient(135deg, var(--do-dam) 0%, var(--do) 60%, #E8391A 100%);
    border-radius: 20px;
    padding: 2.5rem 2rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: var(--bong), inset 0 1px 0 rgba(255,255,255,0.15);
    margin-bottom: 2rem;
    border: 2px solid rgba(245,197,24,0.4);
}
.banner::before {
    content: '';
    position: absolute;
    inset: 0;
    background: repeating-linear-gradient(
        45deg,
        transparent,
        transparent 20px,
        rgba(245,197,24,0.04) 20px,
        rgba(245,197,24,0.04) 21px
    );
}
.banner-star {
    font-size: 2.8rem;
    animation: pulse-star 2s ease-in-out infinite;
    display: block;
    margin-bottom: 0.4rem;
}
@keyframes pulse-star {
    0%, 100% { transform: scale(1);   filter: drop-shadow(0 0 6px #F5C518); }
    50%       { transform: scale(1.1); filter: drop-shadow(0 0 18px #F5C518); }
}
.banner h1 {
    font-family: 'Playfair Display', serif;
    color: var(--vang);
    font-size: 2.4rem;
    margin: 0 0 0.3rem;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.4);
    letter-spacing: 1px;
}
.banner .sub {
    color: rgba(255,255,255,0.85);
    font-size: 1rem;
    font-style: italic;
    font-family: 'Playfair Display', serif;
    letter-spacing: 0.5px;
}
.banner-deco {
    position: absolute;
    font-size: 5rem;
    opacity: 0.07;
}
.banner-deco.left  { left: -10px;  top: -10px; transform: rotate(-20deg); }
.banner-deco.right { right: -10px; bottom: -10px; transform: rotate(20deg); }

/* ─── ĐƯỜNG KẺ HOA VĂN ───────────────────────────────────────── */
.divider {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 1.5rem 0;
}
.divider-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--vang), transparent);
}
.divider-icon { color: var(--do); font-size: 1.1rem; }

/* ─── KHUNG UPLOAD ───────────────────────────────────────────── */
.upload-area {
    background: white;
    border: 2px dashed var(--do);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 2px 16px rgba(200,16,46,0.07);
}
.upload-area:hover { border-color: var(--vang); box-shadow: 0 4px 24px rgba(245,197,24,0.2); }

.upload-icon { font-size: 3rem; margin-bottom: 0.5rem; }
.upload-text { color: var(--nau); font-size: 0.95rem; }

/* ─── THẺ KẾT QUẢ ───────────────────────────────────────────── */
.result-card {
    background: white;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: var(--bong);
    border: 1px solid rgba(200,16,46,0.12);
    animation: slide-up 0.5s ease;
}
@keyframes slide-up {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}
.result-header {
    background: linear-gradient(135deg, var(--do) 0%, var(--do-dam) 100%);
    padding: 1.2rem 1.5rem;
    display: flex;
    align-items: center;
    gap: 12px;
}
.result-header-icon { font-size: 2rem; }
.result-header-label {
    color: rgba(255,255,255,0.7);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 2px;
}
.result-header-value {
    color: var(--vang);
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 700;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.3);
}
.result-body { padding: 1.2rem 1.5rem; }

/* ─── THANH CONFIDENCE ──────────────────────────────────────── */
.conf-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.82rem;
    color: #666;
    margin-bottom: 6px;
    font-weight: 600;
}
.conf-bar-bg {
    background: #F0ECE4;
    border-radius: 999px;
    height: 14px;
    overflow: hidden;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
}
.conf-bar-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, var(--do), var(--vang));
    transition: width 1s ease;
    box-shadow: 0 2px 6px rgba(200,16,46,0.4);
}
.conf-bar-fill.low  { background: linear-gradient(90deg, #e67e22, #f39c12); }
.conf-bar-fill.very-low { background: linear-gradient(90deg, #95a5a6, #bdc3c7); }

/* ─── THÔNG TIN THÊM ─────────────────────────────────────────── */
.info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 12px;
}
.info-chip {
    background: var(--vang-nhat);
    border: 1px solid rgba(245,197,24,0.4);
    border-radius: 10px;
    padding: 10px 14px;
    text-align: center;
}
.info-chip-label { font-size: 0.7rem; color: #888; text-transform: uppercase; letter-spacing: 1px; }
.info-chip-value { font-size: 1rem; font-weight: 700; color: var(--nau); margin-top: 2px; }

/* ─── THẺ HƯỚNG DẪN ─────────────────────────────────────────── */
.guide-card {
    background: linear-gradient(135deg, #F0FFF4 0%, #E8F5E9 100%);
    border: 1px solid #A8D5B5;
    border-radius: 14px;
    padding: 1rem 1.2rem;
    margin-bottom: 1rem;
}
.guide-title {
    color: var(--xanh);
    font-weight: 700;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 6px;
}
.guide-list { list-style: none; padding: 0; margin: 0; }
.guide-list li {
    color: #2D6A4F;
    font-size: 0.82rem;
    padding: 2px 0;
    display: flex;
    align-items: flex-start;
    gap: 6px;
}

/* ─── CẢNH BÁO ──────────────────────────────────────────────── */
.warning-card {
    background: #FFF8E1;
    border: 1px solid #FFCC02;
    border-left: 5px solid #F5C518;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    animation: slide-up 0.5s ease;
}
.warning-card p { margin: 0; color: #7B5800; font-size: 0.9rem; }

/* ─── NHÃN LOẠI TIỀN ──────────────────────────────────────── */
.badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.5px;
}
.badge-polymer  { background: #E8F5E9; color: #2D6A4F; border: 1px solid #A8D5B5; }
.badge-cotton   { background: #FFF3E0; color: #7B4F00; border: 1px solid #FFCC80; }
.badge-invalid  { background: #FCECEA; color: #8B0000; border: 1px solid #FFAAA0; }

/* ─── FOOTER ────────────────────────────────────────────────── */
.footer {
    text-align: center;
    color: #aaa;
    font-size: 0.78rem;
    margin-top: 3rem;
    padding-top: 1.2rem;
    border-top: 1px solid rgba(200,16,46,0.15);
}
.footer span { color: var(--do); }

/* ─── Streamlit overrides ──────────────────────────────────── */
.stFileUploader > label { display: none; }
.stFileUploader section {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}
[data-testid="stFileUploaderDropzone"] {
    background: white !important;
    border: 2px dashed var(--do) !important;
    border-radius: 16px !important;
    padding: 2rem !important;
    transition: all 0.3s !important;
}
[data-testid="stFileUploaderDropzone"]:hover {
    border-color: var(--vang) !important;
}
[data-testid="stImage"] img {
    border-radius: 14px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.12);
}
</style>
""", unsafe_allow_html=True)


LABELS = [
    '0 Đồng (Không phải tiền)',
    '200 Đồng',
    '500 Đồng',
    '1.000 Đồng',
    '2.000 Đồng',
    '5.000 Đồng',
    '10.000 Đồng',
    '20.000 Đồng',
    '50.000 Đồng',
    '100.000 Đồng',
    '200.000 Đồng',
    '500.000 Đồng',
]
BANKNOTE_INFO = {
    '0 Đồng (Không phải tiền)':  ('❌', 'invalid',  '—',         '—'),
    '200 Đồng':                  ('🟤', 'cotton',   'Nâu xanh',  'Hồ Chí Minh / Chùa Một Cột'),
    '500 Đồng':                  ('🔵', 'cotton',   'Xanh lam',  'Hồ Chí Minh / Kho xăng dầu'),
    '1.000 Đồng':                ('🟣', 'cotton',   'Tím nâu',   'Hồ Chí Minh / Mỏ than Quảng Ninh'),
    '2.000 Đồng':                ('🟢', 'cotton',   'Xanh lá',   'Hồ Chí Minh / Nhà máy Thủy điện'),
    '5.000 Đồng':                ('🔷', 'cotton',   'Xanh ngọc', 'Hồ Chí Minh / Thủy điện Trị An'),
    '10.000 Đồng':               ('🟡', 'polymer',  'Tím xanh',  'Hồ Chí Minh / Khai thác dầu khí'),
    '20.000 Đồng':               ('🔵', 'polymer',  'Xanh lam',  'Hồ Chí Minh / Chùa Cầu Hội An'),
    '50.000 Đồng':               ('🟣', 'polymer',  'Tím đỏ',    'Hồ Chí Minh / Cảnh Huế – Văn Miếu'),
    '100.000 Đồng':              ('🟢', 'polymer',  'Xanh lá',   'Hồ Chí Minh / Văn Miếu Quốc Tử Giám'),
    '200.000 Đồng':              ('🔴', 'polymer',  'Đỏ nâu',    'Hồ Chí Minh / Vịnh Hạ Long'),
    '500.000 Đồng':              ('💛', 'polymer',  'Xanh lam',  'Hồ Chí Minh / Hội trường Thống Nhất'),
}

def get_badge_html(loai):
    if loai == 'polymer':
        return '<span class="badge badge-polymer">Polymer</span>'
    elif loai == 'cotton':
        return '<span class="badge badge-cotton">Cotton</span>'
    return '<span class="badge badge-invalid">Không hợp lệ</span>'

@st.cache_resource
def load_my_model():
    return tf.keras.models.load_model('vietnamese_money_v1.h5')

model = load_my_model()

st.markdown("""
<div class="banner">
    <span class="banner-deco left">🏮</span>
    <span class="banner-deco right">🌸</span>
    <span class="banner-star">⭐</span>
    <h1>Nhận Diện Tiền Việt Nam</h1>
    <p class="sub">🪷 Tự hào vóc dáng cờ hoa - Trí tuệ nhân tạo soi ra đồng tiền 🪷</p>
</div>
""", unsafe_allow_html=True)

col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown("""
    <div class="guide-card">
        <div class="guide-title">📋 Hướng dẫn sử dụng</div>
        <ul class="guide-list">
            <li>📸 Tải ảnh chụp rõ nét, đủ sáng</li>
            <li>🔲 Tờ tiền nằm trọn trong khung</li>
            <li>🚫 Tránh ánh sáng phản chiếu</li>
            <li>✅ Hỗ trợ JPG, JPEG, PNG</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Tải ảnh lên",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="📸 Ảnh vừa tải lên", use_column_width=True)

with col_right:
    st.markdown("""
    <div class="divider">
        <div class="divider-line"></div>
        <div class="divider-icon">🪷</div>
        <div style="color:#C8102E;font-weight:700;font-size:0.9rem;letter-spacing:1px">KẾT QUẢ PHÂN TÍCH</div>
        <div class="divider-icon">🪷</div>
        <div class="divider-line"></div>
    </div>
    """, unsafe_allow_html=True)

    if uploaded_file is None:
        st.markdown("""
        <div style="text-align:center; color:#bbb; padding: 4rem 1rem;">
            <div style="font-size:4rem; margin-bottom:1rem; opacity:0.5">🏦</div>
            <div style="font-size:1rem; font-style:italic;">
                Hãy tải ảnh tờ tiền lên để AI nhận diện
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        with st.spinner('🔍 AI đang phân tích...'):
            img_rgb   = image.convert('RGB')
            img_res   = img_rgb.resize((224, 224))
            img_array = np.array(img_res) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            predictions    = model.predict(img_array)
            predicted_idx  = int(np.argmax(predictions[0]))
            confidence     = float(np.max(predictions[0])) * 100
            result_text    = LABELS[predicted_idx]

            icon, loai, mau, hinh = BANKNOTE_INFO.get(
                result_text, ('💵', 'polymer', '—', '—')
            )

        if confidence > 50:
            bar_class = "conf-bar-fill" if confidence >= 70 else "conf-bar-fill low"

            top3_idx = np.argsort(predictions[0])[::-1][:3]

            st.markdown(f"""
            <div class="result-card">
                <div class="result-header">
                    <div class="result-header-icon">{icon}</div>
                    <div>
                        <div class="result-header-label">Mệnh giá nhận diện được</div>
                        <div class="result-header-value">{result_text}</div>
                    </div>
                </div>
                <div class="result-body">
                    <div class="conf-label">
                        <span>Độ tin cậy</span>
                        <span>{confidence:.1f}%</span>
                    </div>
                    <div class="conf-bar-bg">
                        <div class="{bar_class}" style="width:{min(confidence,100):.1f}%"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.balloons()

            # Top-3 dự đoán
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
            <div class="divider">
                <div class="divider-line"></div>
                <div style="color:#888;font-size:0.78rem;letter-spacing:1px;white-space:nowrap">TOP 3 KHẢ NĂNG</div>
                <div class="divider-line"></div>
            </div>
            """, unsafe_allow_html=True)

            for rank, idx in enumerate(top3_idx):
                lbl  = LABELS[idx]
                pct  = float(predictions[0][idx]) * 100
                is_top = rank == 0
                border = "2px solid #C8102E" if is_top else "1px solid #eee"
                bg     = "#FFF9E6"           if is_top else "#F8F8F8"
                fw     = "700"               if is_top else "400"
                st.markdown(f"""
                <div style="display:flex;align-items:center;gap:10px;
                            background:{bg};border:{border};border-radius:10px;
                            padding:8px 12px;margin-bottom:6px">
                    <span style="font-size:1rem">{"🥇" if rank==0 else ("🥈" if rank==1 else "🥉")}</span>
                    <span style="flex:1;font-size:0.88rem;font-weight:{fw};color:#333">{lbl}</span>
                    <span style="font-size:0.88rem;font-weight:{fw};color:#C8102E">{pct:.1f}%</span>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.markdown(f"""
            <div class="warning-card">
                <p>⚠️ <b>AI chưa chắc chắn</b> — độ tin cậy chỉ đạt <b>{confidence:.1f}%</b>.<br><br>
                Vui lòng thử lại với ảnh:<br>
                &nbsp;&nbsp;• Rõ nét hơn, đủ sáng hơn<br>
                &nbsp;&nbsp;• Tờ tiền nằm phẳng, không bị nhăn<br>
                &nbsp;&nbsp;• Không bị che khuất bởi tay hoặc vật khác</p>
            </div>
            """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    🇻🇳 <span>Nhận Diện Tiền Việt Nam</span> &nbsp;·&nbsp;
    Bài tập môn Trí Tuệ Nhân Tạo &nbsp;·&nbsp;
    Mô hình: <span>CNN – TensorFlow/Keras</span><br>
    <span style="color:#bbb;font-size:0.72rem">
    </span>
</div>
""", unsafe_allow_html=True)
