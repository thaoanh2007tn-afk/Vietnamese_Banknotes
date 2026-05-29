# 🇻🇳 Nhận Diện Tiền Việt Nam – Vietnamese Banknote Recognition

<div align="center">
  
> 🏮 **Ứng dụng nhận diện mệnh giá tiền Việt Nam bằng mô hình học sâu (CNN), triển khai qua giao diện web Streamlit.**  
> Bài tập môn **Trí Tuệ Nhân Tạo** – Phát triển bởi sinh viên.

</div>

---

## 📌 Giới thiệu

Dự án xây dựng một hệ thống nhận diện **12 loại mệnh giá tiền Việt Nam** (từ 200đ đến 500.000đ) từ ảnh chụp tờ tiền, sử dụng mô hình **Convolutional Neural Network (CNN)** được huấn luyện bằng TensorFlow/Keras và triển khai dưới dạng web app với **Streamlit**.

Giao diện mang đậm **văn hóa Việt Nam**: màu đỏ – vàng quốc kỳ, họa tiết truyền thống, thể hiện sự tự hào dân tộc trong từng chi tiết thiết kế.

---

## ✨ Tính năng

- 📸 **Upload ảnh** tờ tiền (JPG, JPEG, PNG) và nhận kết quả tức thì
- 🤖 **Nhận diện 12 mệnh giá** tiền Việt Nam với CNN
- 📊 **Thanh độ tin cậy** trực quan, thể hiện mức chắc chắn của AI
- 🥇 **Top 3 dự đoán** – hiển thị các khả năng cao nhất
- 🎨 **Giao diện đẹp** mang cảm hứng văn hoá Việt Nam

---

## 🗂️ Cấu trúc dự án

```
Vietnamese_Banknotes/
│
├── app.py                    # Ứng dụng Streamlit chính
├── vietnamese_money_v1.h5    # Mô hình CNN đã huấn luyện
├── requirements.txt          # Thư viện cần thiết
└── README.md                 # Tài liệu dự án
```

---

## 🏷️ Các mệnh giá được nhận diện

| # | Mệnh giá |
|---|----------|
| 0 | ❌ Không phải tiền |
| 1 | 200 Đồng |
| 2 | 500 Đồng | 
| 3 | 1.000 Đồng |
| 4 | 2.000 Đồng | 
| 5 | 5.000 Đồng | 
| 6 | 10.000 Đồng |
| 7 | 20.000 Đồng |
| 8 | 50.000 Đồng |
| 9 | 100.000 Đồng | 
| 10 | 200.000 Đồng | 
| 11 | 500.000 Đồng | 

---

## 🧠 Kiến trúc mô hình

- **Kiến trúc:** Convolutional Neural Network (CNN)
- **Framework:** TensorFlow / Keras
- **Input:** Ảnh RGB kích thước `224 × 224` pixel
- **Output:** Phân loại 12 lớp (softmax)
- **File mô hình:** `vietnamese_money_v1.h5`
- **Tiền xử lý:** Resize → Normalize `[0, 1]` → Expand dims (batch)

---

## 🚀 Cài đặt & Chạy

### 1. Clone repository

```bash
git clone https://github.com/thaoanh2007tn-afk/Vietnamese_Banknotes.git
cd Vietnamese_Banknotes
```

### 2. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

> Nội dung `requirements.txt`:
> ```
> streamlit
> tensorflow
> numpy
> Pillow
> ```

### 3. Chạy ứng dụng

```bash
streamlit run app.py
```
---

## 🖼️ Hướng dẫn sử dụng

1. Truy cập ứng dụng qua trình duyệt
2. Nhấn **"Browse files"** hoặc kéo thả ảnh tờ tiền vào khung upload
3. AI tự động phân tích và hiển thị kết quả ngay bên cạnh
4. Xem thêm thông tin chi tiết và top 3 dự đoán phía dưới

> **Mẹo để kết quả chính xác nhất:**
> - Ảnh rõ nét, đủ sáng, tờ tiền nằm phẳng
> - Tờ tiền chiếm phần lớn khung hình
> - Không bị che khuất, không phản chiếu ánh sáng

---

## 📦 Công nghệ sử dụng

| Công nghệ | Mục đích |
|-----------|----------|
| Python | Ngôn ngữ lập trình chính |
| TensorFlow| Huấn luyện & chạy mô hình CNN |
| Keras | API xây dựng mô hình |
| Streamlit | Giao diện web |
| NumPy | Xử lý mảng số |
| Pillow | Xử lý ảnh |

---

## 👨‍💻 Tác giả
Trần Ngọc Thảo Anh - 
Lê Thái Bảo - 
Lê Thị Như Quỳnh

---

<div align="center">
  <i>🇻🇳 Tự hào sản phẩm Việt – Bài tập môn Trí Tuệ Nhân Tạo 🇻🇳</i>
</div>
