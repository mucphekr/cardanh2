# 🎓 Tạo Thẻ Sinh Viên Ver 2.0

**Tự động tạo thẻ sinh viên với tên do AI sinh ra hoặc chọn tên thủ công**

[![Version](https://img.shields.io/badge/version-2.0-blue.svg)](https://github.com)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)

---

## ✨ Tính Năng Mới Ver 2.0

### 🤖 Tự Động Tạo Tên Bằng AI
- ✅ Tích hợp **Gemini API** để tạo tên sinh viên Việt Nam tự động
- ✅ Tên đa dạng, tự nhiên, có dấu chính xác
- ✅ Không cần chuẩn bị danh sách tên trước

### 🔢 Chọn Số Lượng Thay Vì Chọn Tên
- ✅ Chỉ cần nhập số lượng thẻ muốn tạo
- ✅ Script tự động tạo tên và thẻ
- ✅ Tiết kiệm thời gian cho số lượng lớn

### 🚫 Tự Động Tránh Trùng Lặp
- ✅ Lưu tất cả tên đã tạo vào `out_names/names_log.txt`
- ✅ Tự động kiểm tra và tránh tạo tên trùng
- ✅ Hoạt động cả với giao diện web và dòng lệnh

### 🎨 Giao Diện Web Hiện Đại
- ✅ 2 chế độ: **Tự động** và **Thủ công**
- ✅ Xem trước và điều chỉnh vị trí text
- ✅ Lưu lịch sử vào localStorage

---

## 🚀 Bắt Đầu Nhanh

### Cách 1: Giao Diện Web (Khuyến Nghị)

```bash
# Mở file index.html bằng trình duyệt
# Không cần cài đặt gì!
```

1. Mở `index.html`
2. Upload template thẻ
3. Nhập số lượng (hoặc chọn tên thủ công)
4. Nhấn "Tạo Thẻ Sinh Viên"
5. Download kết quả

⏱️ **Thời gian: 1 phút**

---

### Cách 2: Dòng Lệnh với Gemini API

```bash
# Bước 1: Cài đặt
pip install -r requirements.txt

# Bước 2: Lấy API key từ https://makersuite.google.com/app/apikey

# Bước 3: Tạo thẻ
python app.py --num 10 --gemini --gemini-key YOUR_API_KEY
```

⏱️ **Thời gian: 2 phút**

---

## 📦 Cài Đặt

### Yêu Cầu
- Python 3.8+
- Pillow
- google-generativeai (chỉ khi dùng Gemini API)

### Cài Đặt Thư Viện

```bash
pip install -r requirements.txt
```

Hoặc:

```bash
pip install Pillow google-generativeai
```

---

## 📖 Hướng Dẫn Sử Dụng

### Giao Diện Web

#### Chế độ Tự Động (AI)
```
1. Mở index.html
2. Upload template
3. Chọn "Tự động tạo tên (Gemini AI)"
4. Nhập số lượng: 10
5. Nhấn "Tạo Thẻ"
```

#### Chế độ Thủ Công
```
1. Mở index.html
2. Upload template
3. Chọn "Chọn tên thủ công"
4. Chọn sinh viên từ danh sách
5. Nhấn "Tạo Thẻ"
```

---

### Dòng Lệnh

#### Gemini API (Khuyến nghị)
```bash
# Tạo 10 thẻ với tên AI
python app.py --num 10 --gemini --gemini-key YOUR_KEY

# Tạo 50 thẻ, padding nếu không đủ
python app.py --num 50 --gemini --gemini-key YOUR_KEY --pad-local

# Đặt API key vào biến môi trường
$env:GEMINI_API_KEY="YOUR_KEY"
python app.py --num 10 --gemini
```

#### File Tên
```bash
# Sử dụng file students_1000.txt
python app.py --num 10 --names-file students_1000.txt
```

#### Offline (Không cần API)
```bash
# Tạo tên random offline
python app.py --num 10
```

---

## 🎯 Các Tùy Chọn

| Tùy chọn | Mô tả |
|----------|-------|
| `--num` | Số lượng thẻ |
| `--gemini` | Dùng Gemini API |
| `--gemini-key` | API key |
| `--names-file` | File chứa tên |
| `--template` | Template thẻ |
| `--out` | Thư mục output |
| `--pad-local` | Padding offline |
| `--seed` | Random seed |

---

## 📂 Cấu Trúc Thư Mục

```
Card Viet/
├── app.py                      # Script Python chính
├── index.html                  # Giao diện web
├── template.png                # Template thẻ
├── requirements.txt            # Thư viện cần thiết
├── students_1000.txt           # Danh sách 1000 tên
├── students_1000.js            # Tên cho web
├── out_names/                  # Thư mục output
│   ├── *.png                   # Các thẻ đã tạo
│   └── names_log.txt           # Log tên đã tạo
├── README.md                   # File này
├── QUICK_START.md              # Hướng dẫn nhanh
├── HUONG_DAN_SU_DUNG.md       # Hướng dẫn đầy đủ
└── README_GEMINI.md            # Hướng dẫn Gemini API
```

---

## 💡 Tính Năng Nổi Bật

### ✅ Đa Phương Pháp
- 🌐 Giao diện web (không cần cài)
- 🤖 Gemini API (tên AI)
- 📁 File tên có sẵn
- 💻 Tên offline

### ✅ Tự Động Tránh Trùng
- Lưu vào `names_log.txt`
- Kiểm tra tự động
- Hoạt động với mọi phương pháp

### ✅ Tùy Chỉnh Dễ Dàng
- Điều chỉnh vị trí text
- Tùy chỉnh font size
- Xem trước ngay lập tức

---

## 🔧 Tùy Chỉnh

### Vị Trí Text trong app.py

```python
R_X = 0.56      # Vị trí ngang (0-1)
R_Y = 0.455     # Vị trí dọc (0-1)
R_W = 0.52      # Chiều rộng vùng text
R_H = 0.055     # Chiều cao vùng text
BASE_FONT_SIZE = 54  # Kích thước font
```

### Vị Trí Text trong Web
- Kéo xuống "Cấu Hình Vị Trí Text"
- Điều chỉnh X, Y, Font size
- Xem kết quả ngay

---

## 📊 Ví Dụ

### Ví Dụ 1: Tạo 20 Thẻ Nhanh (Web)
```
1. Mở index.html
2. Upload template
3. Nhập: 20
4. Tạo thẻ
5. Download
```
⏱️ **1 phút**

### Ví Dụ 2: Tạo 100 Thẻ với AI
```bash
python app.py --num 100 --gemini --gemini-key YOUR_KEY --pad-local
```
⏱️ **3 phút** • 🎯 **~90 tên AI + ~10 offline**

### Ví Dụ 3: Tạo Từ Danh Sách
```bash
python app.py --num 50 --names-file students_1000.txt
```
⏱️ **2 phút**

---

## 🆘 Khắc Phục Sự Cố

### Lỗi: "google-generativeai not installed"
```bash
pip install google-generativeai
```

### Lỗi: "No API key"
- Lấy key: https://makersuite.google.com/app/apikey
- Dùng: `--gemini-key YOUR_KEY`

### Text bị lệch
- Điều chỉnh R_X, R_Y trong app.py
- Hoặc dùng "Cấu Hình Vị Trí Text" trong web

### Xem log chi tiết
```bash
python app.py --num 10 --gemini --gemini-key YOUR_KEY 2>&1 | tee log.txt
```

---

## 📚 Tài Liệu

- 📖 [Hướng Dẫn Đầy Đủ](HUONG_DAN_SU_DUNG.md)
- 🚀 [Quick Start](QUICK_START.md)
- 🤖 [Gemini API Guide](README_GEMINI.md)

---

## 🎓 Workflow Đề Xuất

### Cho Người Mới
1. Dùng giao diện web
2. Tạo 5-10 thẻ thử
3. Xem kết quả
4. Tăng dần số lượng

### Cho Người Có Kinh Nghiệm
1. Cài Gemini API
2. Tạo hàng loạt với `--gemini`
3. Tùy chỉnh template
4. Tự động hóa workflow

---

## 🌟 So Sánh Ver 1.0 vs 2.0

| Tính năng | Ver 1.0 | Ver 2.0 |
|-----------|---------|---------|
| Chọn tên | ✅ Thủ công | ✅ Tự động + Thủ công |
| AI tạo tên | ❌ | ✅ Gemini API |
| Tránh trùng | ⚠️ Cơ bản | ✅ Tự động |
| Giao diện | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Tốc độ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 🎉 Kết Luận

**Ver 2.0 mang đến:**
- 🤖 Tự động hóa với AI
- 🔢 Chọn số lượng dễ dàng
- 🚫 Tránh trùng tự động
- 🎨 Giao diện đẹp hơn

**Bắt đầu ngay:**
1. Mở `index.html`
2. Upload template
3. Nhập số lượng
4. Nhấn "Tạo Thẻ"

**🎊 Chúc bạn thành công!**

---

## 📞 Hỗ Trợ

- 📖 Đọc hướng dẫn: `HUONG_DAN_SU_DUNG.md`
- 🚀 Quick start: `QUICK_START.md`
- 🤖 Gemini API: `README_GEMINI.md`

---

## 📄 License

MIT License - Tự do sử dụng, chỉnh sửa và phân phối.

---

**Made with ❤️ for Vietnamese students**

