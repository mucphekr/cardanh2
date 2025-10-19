# 🚀 Quick Start - Bắt Đầu Nhanh

## ⚡ Cách Nhanh Nhất (Không cần cài gì)

### Bước 1: Mở Giao Diện Web
- Mở file `index.html` bằng trình duyệt (Chrome, Edge, Firefox...)

### Bước 2: Upload Template
- Click vào vùng "Upload Template"
- Chọn file `template.png` hoặc template của bạn

### Bước 3: Nhập Số Lượng
- Chế độ mặc định: **Tự động tạo tên (Gemini AI)**
- Nhập số lượng thẻ muốn tạo (ví dụ: 10)

### Bước 4: Tạo Thẻ
- Nhấn nút **"Tạo Thẻ Sinh Viên"**
- Đợi vài giây để xem kết quả

### Bước 5: Download
- Click nút **"Download"** bên dưới mỗi thẻ
- Hoặc download tất cả

**🎉 Xong! Chỉ mất 1 phút!**

---

## 🤖 Nâng Cao: Sử Dụng Gemini API (Tên Đẹp Hơn)

### Bước 1: Lấy API Key (Miễn Phí)
1. Truy cập: https://makersuite.google.com/app/apikey
2. Đăng nhập Google
3. Click "Create API Key"
4. Copy API key

### Bước 2: Cài Đặt
```bash
pip install google-generativeai Pillow
```

### Bước 3: Chạy
```bash
python app.py --num 10 --gemini --gemini-key YOUR_API_KEY
```

### Kết Quả
- 10 thẻ với tên đẹp, đa dạng từ AI
- Tự động lưu vào thư mục `out_names/`
- Tự động tránh trùng tên

**⏱️ Thời gian: ~2 phút**

---

## 📊 So Sánh 2 Phương Pháp

| | Giao Diện Web | Gemini API |
|---|---|---|
| **Cài đặt** | ❌ Không cần | ✅ Cần pip install |
| **API Key** | ❌ Không cần | ✅ Cần (miễn phí) |
| **Tốc độ** | ⚡ Rất nhanh | ⚡ Nhanh |
| **Chất lượng tên** | ⭐⭐⭐ Tốt | ⭐⭐⭐⭐⭐ Xuất sắc |
| **Số lượng** | 1-50 thẻ | 1-100+ thẻ |
| **Khuyến nghị** | Dùng thử, số lượng nhỏ | Sản xuất, số lượng lớn |

---

## 💡 Mẹo

### Mẹo 1: Tránh Trùng Tên
- ✅ Hệ thống tự động lưu tên đã tạo
- ✅ Mỗi lần tạo đều kiểm tra không trùng
- ✅ Xem lịch sử: `out_names/names_log.txt`

### Mẹo 2: Reset Nếu Muốn Tạo Lại
**Giao diện web:**
- Click nút "Reset danh sách"

**Dòng lệnh:**
```bash
del out_names\names_log.txt
```

### Mẹo 3: Tùy Chỉnh Vị Trí Text
**Trong giao diện web:**
- Kéo xuống phần "Cấu Hình Vị Trí Text"
- Điều chỉnh X, Y, Font size
- Xem kết quả ngay lập tức

---

## 🆘 Gặp Vấn Đề?

### Template không hiển thị?
- Kiểm tra file template có tồn tại không
- Thử upload lại

### Text bị lệch?
- Điều chỉnh X, Y trong "Cấu Hình Vị Trí Text"

### Lỗi "google-generativeai not installed"?
```bash
pip install google-generativeai
```

---

## 📚 Tài Liệu Đầy Đủ

- 📖 **Hướng dẫn đầy đủ**: `HUONG_DAN_SU_DUNG.md`
- 🤖 **Hướng dẫn Gemini API**: `README_GEMINI.md`
- 💻 **Mã nguồn**: `app.py` (Python), `index.html` (Web)

---

## 🎯 Bắt Đầu Ngay!

**Cách đơn giản nhất:**
1. Mở `index.html`
2. Upload template
3. Nhập số lượng
4. Nhấn "Tạo Thẻ"

**🎉 Chúc bạn thành công!**

