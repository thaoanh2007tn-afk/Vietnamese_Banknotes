import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# 1. CẤU HÌNH TRANG (Phải đặt ở dòng đầu tiên của Streamlit)
st.set_page_config(
    page_title="Nhận Diện Tiền Việt Nam", 
    page_icon="🇻🇳", 
    layout="centered"
)

# 2. CSS TÙY CHỈNH - GIAO DIỆN ĐẬM CHẤT VIỆT NAM
st.markdown("""
    <style>
    /* Nền trang màu vàng nhạt (màu giấy dó/hoài cổ) */
    .stApp {
        background-color: #FFFDF0; 
    }
    
    /* Tiêu đề màu đỏ cờ, bóng vàng */
    h1 {
        color: #DA251D; 
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-shadow: 2px 2px 4px #FFCD00;
        padding-bottom: 10px;
    }
    
    /* Khung kết quả */
    .result-box {
        background-color: #FFF;
        border-left: 5px solid #DA251D;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #888;
        font-style: italic;
        margin-top: 50px;
        border-top: 1px solid #ddd;
        padding-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. DANH SÁCH NHÃN (LABELS)
# CHÚ Ý: Bạn BẮT BUỘC phải sắp xếp mảng này theo đúng thứ tự 0, 1, 2... 
# mà lệnh train_generator.class_indices đã in ra trên Colab.
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
    '500.000 Đồng'
]

# 4. HÀM TẢI MÔ HÌNH (Sử dụng cache để không phải load lại mỗi lần đổi ảnh)
@st.cache_resource
def load_my_model():
    # Thay tên file dưới đây bằng tên file mô hình bạn đã lưu (ví dụ: .h5 hoặc .keras)
    return tf.keras.models.load_model('vietnamese_money_v1.h5')

model = load_my_model()

# 5. GIAO DIỆN CHÍNH
st.markdown("<h1>🏮 HỆ THỐNG NHẬN DIỆN TIỀN VIỆT 🇻🇳</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #444;'>🪷 Tự hào vóc dáng cờ hoa - Trí tuệ nhân tạo soi ra đồng tiền 🪷</h4>", unsafe_allow_html=True)
st.write("---")

st.write("**Hướng dẫn:** Hãy tải lên một bức ảnh chụp tờ tiền Việt Nam (Rõ nét, đủ sáng) để AI kiểm tra giúp bạn nhé!")

# Nút Upload ảnh
uploaded_file = st.file_uploader("📂 Chọn ảnh từ máy của bạn...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Hiển thị ảnh vừa tải lên
    image = Image.open(uploaded_file)
    st.image(image, caption='📸 Ảnh bạn vừa tải lên', use_column_width=True)
    
    with st.spinner('AI đang phân tích ...'):
        # 6. TIỀN XỬ LÝ ẢNH
        # Resize ảnh về kích thước mô hình yêu cầu (224x224)
        img = image.resize((224, 224))
        # Chuyển thành mảng numpy và chuẩn hóa (Normalize) về [0, 1]
        img_array = np.array(img) / 255.0
        # Thêm chiều batch (1, 224, 224, 3)
        img_array = np.expand_dims(img_array, axis=0)

        # 7. DỰ ĐOÁN
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions[0])
        confidence = np.max(predictions[0]) * 100

        # Lấy tên mệnh giá dựa trên index
        result_text = LABELS[predicted_class]

        # 8. HIỂN THỊ KẾT QUẢ ĐẸP MẮT
        if confidence > 50:
            st.markdown(f"""
                <div class="result-box">
                    <h3 style="color: #DA251D; margin-top: 0;">✅ Kết Quả: {result_text}</h3>
                    <p style="font-size: 16px; margin-bottom: 0;"><b>Độ tin cậy của AI:</b> {confidence:.2f}%</p>
                </div>
            """, unsafe_allow_html=True)
            st.balloons() 
        else:
            st.warning("⚠️ Trí tuệ nhân tạo đang hơi phân vân. Độ tin cậy khá thấp, bạn thử chụp lại ảnh rõ nét hơn xem sao nhé!")

# Footer
st.markdown("""
    <div class="footer">
        © 2026 - Sản phẩm bài tập môn AI <br>
        Phát triển bởi sinh viên 
    </div>
""", unsafe_allow_html=True)
