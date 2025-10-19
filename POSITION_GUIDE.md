# 🎯 Hướng Dẫn Cấu Hình Vị Trí Text

## 📍 Tổng Quan
Hệ thống hiện tại hỗ trợ **2 vị trí text riêng biệt**:
1. **Tên sinh viên đầy đủ** (First Name + Last Name) - vị trí chính
2. **Chỉ tên** (First Name) xuất hiện sau "Dear:" - vị trí phụ

## 🖥️ Cấu Hình Trên Giao Diện Web (index.html)

### 1. Vị Trí Tên Sinh Viên Đầy Đủ
- **Tỷ lệ ngang (X)**: `0.55` (55% từ trái sang phải)
- **Tỷ lệ dọc (Y)**: `0.475` (47.5% từ trên xuống)
- **Kích thước font**: `46px`
- **Màu sắc**: `#000000` (đen)

### 2. Vị Trí Tên (First Name) Sau "Dear:"
- **Tỷ lệ ngang (X)**: `0.25` (25% từ trái sang phải)
- **Tỷ lệ dọc (Y)**: `0.15` (15% từ trên xuống)
- **Kích thước font**: `32px`
- **Màu sắc**: `#000000` (đen)

## ⚙️ Cấu Hình Trong Code (app.py)

### Vị Trí Tên Đầy Đủ
```python
FULL_NAME_X = 0.56      # left X ratio of the full name area
FULL_NAME_Y = 0.455     # top Y ratio of the full name area
FULL_NAME_W = 0.52      # width ratio of the full name area
FULL_NAME_H = 0.055     # height ratio of the full name area
```

### Vị Trí Tên (First Name) Sau "Dear:"
```python
LAST_NAME_X = 0.25      # left X ratio of the first name area (after Dear:)
LAST_NAME_Y = 0.15      # top Y ratio of the first name area
LAST_NAME_W = 0.3       # width ratio of the first name area
LAST_NAME_H = 0.04      # height ratio of the first name area
```

## 🎨 Cách Chỉnh Sửa Vị Trí

### Trên Giao Diện Web:
1. Mở file `index.html` trong trình duyệt
2. Tìm phần "Cấu Hình Vị Trí Text"
3. Điều chỉnh các giá trị trong form:
   - **Tỷ lệ ngang (X)**: 0.0 = bên trái, 1.0 = bên phải
   - **Tỷ lệ dọc (Y)**: 0.0 = trên cùng, 1.0 = dưới cùng
   - **Kích thước font**: Số pixel
   - **Màu sắc**: Chọn màu từ color picker

### Trong Code Python:
1. Mở file `app.py`
2. Tìm các hằng số `FULL_NAME_*` và `LAST_NAME_*`
3. Thay đổi giá trị theo ý muốn:
   - Giá trị từ 0.0 đến 1.0
   - 0.0 = bên trái/trên cùng
   - 1.0 = bên phải/dưới cùng

## 📝 Ví Dụ Cấu Hình

### Để di chuyển tên sang phải:
- Tăng giá trị X (ví dụ: từ 0.55 → 0.65)

### Để di chuyển tên xuống dưới:
- Tăng giá trị Y (ví dụ: từ 0.475 → 0.525)

### Để tăng kích thước font:
- Tăng giá trị font size (ví dụ: từ 46 → 56)

### Để thay đổi màu sắc:
- Thay đổi mã màu (ví dụ: #000000 → #FF0000 cho màu đỏ)

## 🔧 Test Cấu Hình

### Sử dụng Web Interface:
1. Upload template
2. Điều chỉnh vị trí trong form
3. Click "Tạo Thẻ Sinh Viên"
4. Kiểm tra kết quả

### Sử dụng Command Line:
```bash
python app.py --num 1 --template "DOC ANH (3).png"
```

## 📊 Giá Trị Mặc Định

| Vị Trí | X | Y | Font Size | Màu |
|--------|---|---|-----------|-----|
| Tên đầy đủ (vị trí chính) | 0.55 | 0.475 | 46px | #000000 |
| Tên (First Name) sau "Dear:" | 0.25 | 0.15 | 32px | #000000 |

## 💡 Mẹo Chỉnh Sửa

1. **Bắt đầu với giá trị nhỏ**: Thay đổi từng giá trị một cách nhỏ (0.01-0.05)
2. **Test thường xuyên**: Chạy test sau mỗi lần thay đổi
3. **Lưu backup**: Sao lưu cấu hình cũ trước khi thay đổi
4. **Sử dụng tỷ lệ**: Tỷ lệ 0.5 = giữa màn hình, 0.25 = 1/4 màn hình

## 🚨 Lưu Ý Quan Trọng

- **Giá trị X, Y**: Phải từ 0.0 đến 1.0
- **Font size**: Phải là số nguyên dương
- **Màu sắc**: Phải là mã hex hợp lệ (#RRGGBB)
- **Template**: Phải upload template trước khi test
