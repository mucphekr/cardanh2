# Hướng Dẫn Sử Dụng - Tạo Thẻ Sinh Viên Ver 2.0

## 🎉 Tính Năng Mới

### ✨ Ver 2.0 - Tự Động Tạo Tên Bằng AI
- 🤖 **Tích hợp Gemini API**: Tự động tạo tên sinh viên Việt Nam bằng AI
- 🔢 **Chọn số lượng**: Chỉ cần nhập số lượng thẻ muốn tạo, không cần chọn từng tên
- 🚫 **Tự động tránh trùng**: Hệ thống tự động lưu và kiểm tra tên đã tạo
- 💾 **Lưu lịch sử**: Tất cả tên đã tạo được lưu vào `out_names/names_log.txt`

---

## 📦 Cài Đặt

### 1. Cài đặt Python (nếu chưa có)
- Tải Python từ: https://www.python.org/downloads/
- Chọn "Add Python to PATH" khi cài đặt

### 2. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

Hoặc cài thủ công:

```bash
pip install Pillow google-generativeai
```

---

## 🚀 Sử Dụng

### Cách 1: Giao Diện Web (Khuyến Nghị)

1. Mở file `index.html` bằng trình duyệt
2. Upload template thẻ sinh viên
3. Chọn chế độ:
   - **Tự động tạo tên (Gemini AI)**: Chỉ cần nhập số lượng
   - **Chọn tên thủ công**: Chọn từng sinh viên từ danh sách
4. Nhấn "Tạo Thẻ Sinh Viên"
5. Download các thẻ đã tạo

**Ưu điểm:**
- ✅ Dễ sử dụng, giao diện thân thiện
- ✅ Xem trước kết quả ngay lập tức
- ✅ Tự động lưu tên đã tạo vào localStorage
- ✅ Không cần API key (dùng tên random offline)

---

### Cách 2: Dòng Lệnh với Gemini API

#### Bước 1: Lấy API Key

1. Truy cập: https://makersuite.google.com/app/apikey
2. Đăng nhập Google
3. Tạo API Key mới
4. Sao chép API Key

#### Bước 2: Sử dụng

**Tạo 10 thẻ với Gemini API:**

```bash
python app.py --num 10 --gemini --gemini-key YOUR_API_KEY
```

**Đặt API key vào biến môi trường:**

```powershell
# Windows PowerShell
$env:GEMINI_API_KEY="YOUR_API_KEY"
python app.py --num 10 --gemini

# Windows CMD
set GEMINI_API_KEY=YOUR_API_KEY
python app.py --num 10 --gemini
```

**Tạo 20 thẻ, padding nếu không đủ:**

```bash
python app.py --num 20 --gemini --gemini-key YOUR_API_KEY --pad-local
```

---

### Cách 3: Dòng Lệnh với File Tên

```bash
# Sử dụng file students_1000.txt
python app.py --num 10 --names-file students_1000.txt

# Padding nếu không đủ tên
python app.py --num 50 --names-file students_1000.txt --pad-local
```

---

### Cách 4: Dòng Lệnh Offline (Không cần API)

```bash
# Tạo 10 thẻ với tên random offline
python app.py --num 10
```

---

## 📝 Tùy Chọn Dòng Lệnh

### Các Tùy Chọn Chính

| Tùy chọn | Mô tả | Ví dụ |
|----------|-------|-------|
| `--num` | Số lượng thẻ muốn tạo | `--num 10` |
| `--gemini` | Sử dụng Gemini API | `--gemini` |
| `--gemini-key` | API key của Gemini | `--gemini-key abc123` |
| `--names-file` | File chứa danh sách tên | `--names-file students.txt` |
| `--template` | Đường dẫn template | `--template my_template.png` |
| `--out` | Thư mục output | `--out output_folder` |
| `--pad-local` | Padding với tên offline nếu thiếu | `--pad-local` |
| `--seed` | Random seed | `--seed 42` |

### Ví Dụ Nâng Cao

```bash
# Tạo 30 thẻ, tùy chỉnh template và output
python app.py --num 30 --gemini --gemini-key YOUR_KEY \
  --template custom_template.png \
  --out my_cards \
  --pad-local

# Sử dụng seed để tạo nhất quán
python app.py --num 10 --seed 42
```

---

## 🎯 So Sánh Các Phương Pháp

| Phương pháp | Ưu điểm | Nhược điểm | Khuyến nghị |
|-------------|---------|------------|-------------|
| **Giao diện Web** | Dễ sử dụng, xem trước ngay | Tên offline đơn giản | ⭐⭐⭐⭐⭐ Tốt nhất cho người mới |
| **Gemini API** | Tên đa dạng, tự nhiên | Cần API key, internet | ⭐⭐⭐⭐ Tốt cho số lượng lớn |
| **File tên** | Kiểm soát hoàn toàn | Cần chuẩn bị file | ⭐⭐⭐ Tốt cho danh sách có sẵn |
| **Offline** | Không cần gì | Tên đơn giản | ⭐⭐ Dùng khi không có internet |

---

## 💾 Hệ Thống Lưu Trữ và Tránh Trùng

### Cách Hoạt Động

1. **Lưu tên đã tạo**: Mỗi lần tạo thẻ, tên được lưu vào `out_names/names_log.txt`
2. **Kiểm tra trùng**: Trước khi tạo, script kiểm tra xem tên đã tồn tại chưa
3. **Tránh trùng lặp**: Chỉ tạo tên chưa có trong log

### Xem Lịch Sử

```bash
# Xem tất cả tên đã tạo
type out_names\names_log.txt

# Đếm số tên đã tạo
find /c /v "" out_names\names_log.txt
```

### Reset Lịch Sử

```bash
# Xóa file log để bắt đầu lại
del out_names\names_log.txt

# Hoặc dùng giao diện web: nhấn nút "Reset danh sách"
```

---

## 🎨 Tùy Chỉnh Vị Trí Text

### Trong Giao Diện Web

1. Mở `index.html`
2. Kéo xuống phần "Cấu Hình Vị Trí Text"
3. Điều chỉnh:
   - **Tỷ lệ ngang (X)**: 0-1 (0 = trái, 1 = phải)
   - **Tỷ lệ dọc (Y)**: 0-1 (0 = trên, 1 = dưới)
   - **Kích thước font**: pixels

### Trong File app.py

Tìm và sửa các biến:

```python
R_X = 0.56      # Vị trí ngang (0-1)
R_Y = 0.455     # Vị trí dọc (0-1)
R_W = 0.52      # Chiều rộng vùng text (0-1)
R_H = 0.055     # Chiều cao vùng text (0-1)
BASE_FONT_SIZE = 54  # Kích thước font
```

---

## 🔧 Khắc Phục Sự Cố

### Lỗi: "google-generativeai not installed"

**Giải pháp:**
```bash
pip install google-generativeai
```

### Lỗi: "No Gemini API key provided"

**Giải pháp:**
- Cung cấp API key: `--gemini-key YOUR_KEY`
- Hoặc đặt biến môi trường: `$env:GEMINI_API_KEY="YOUR_KEY"`

### Lỗi: "Template not found"

**Giải pháp:**
- Kiểm tra đường dẫn template trong `app.py`:
  ```python
  TEMPLATE_PATH = r"C:\path\to\template.png"
  ```
- Hoặc dùng: `--template path/to/template.png`

### Text bị lệch vị trí

**Giải pháp:**
- Điều chỉnh `R_X` và `R_Y` trong app.py
- Hoặc dùng giao diện web để xem trước và điều chỉnh

### Không đủ tên không trùng

**Giải pháp:**
- Thêm `--pad-local` để padding với tên offline
- Hoặc giảm số lượng thẻ
- Hoặc reset lịch sử: `del out_names\names_log.txt`

---

## 📊 Giới Hạn

- **Gemini API**: 
  - Free tier: 60 requests/minute
  - Có thể tạo ~100-200 tên/batch
- **Tên offline**: 
  - Có thể tạo hàng nghìn tên không trùng
  - Kết hợp từ họ, tên đệm, tên chính
- **Giao diện web**:
  - localStorage giới hạn ~5-10MB
  - Đủ cho hàng nghìn tên

---

## 🎓 Ví Dụ Workflow

### Workflow 1: Tạo Thẻ Nhanh (Giao Diện Web)

1. Mở `index.html`
2. Upload template
3. Chọn "Tự động tạo tên"
4. Nhập số lượng: 20
5. Nhấn "Tạo Thẻ"
6. Download tất cả

⏱️ **Thời gian**: ~1 phút

---

### Workflow 2: Tạo Nhiều Thẻ (Gemini API)

```bash
# Tạo 100 thẻ với tên AI
python app.py --num 100 --gemini --gemini-key YOUR_KEY --pad-local

# Kết quả:
# ✅ Gemini tạo ~80-90 tên unique
# ✅ Offline padding ~10-20 tên còn lại
# ✅ Tất cả được lưu vào out_names/
```

⏱️ **Thời gian**: ~2-3 phút

---

### Workflow 3: Tạo Từ Danh Sách Có Sẵn

```bash
# Bước 1: Chuẩn bị file students.txt
# Mỗi dòng 1 tên

# Bước 2: Tạo thẻ
python app.py --num 50 --names-file students.txt

# Bước 3: Kiểm tra output
dir out_names\*.png
```

⏱️ **Thời gian**: ~1-2 phút

---

## 📚 Tài Liệu Tham Khảo

- **Gemini API**: https://ai.google.dev/docs
- **PIL/Pillow**: https://pillow.readthedocs.io/
- **Python Argparse**: https://docs.python.org/3/library/argparse.html

---

## 🆘 Hỗ Trợ

Nếu gặp vấn đề:
1. Kiểm tra phần "Khắc Phục Sự Cố" ở trên
2. Xem file `README_GEMINI.md` để biết thêm chi tiết về Gemini API
3. Kiểm tra log trong terminal/console

---

## 📝 Ghi Chú

- ✅ Tên đã tạo được lưu tự động, không lo trùng lặp
- ✅ Có thể dùng cả giao diện web và dòng lệnh
- ✅ Gemini API miễn phí (có giới hạn quota)
- ✅ Hoạt động offline nếu không dùng Gemini

**Chúc bạn tạo thẻ thành công! 🎉**

