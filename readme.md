## Giới thiệu
`Morphology functions` là một chương trình có giao diện đơn giản để thử nghiệm một số phép biến đổi morphology cho ảnh nhị phân và ảnh mức xám. 
## Cấu trúc thư mục
- `src:`
  - `data/`:  chứa các ảnh để kiểm thử cho chương trình của chúng tôi
  - `function/`
    - `binary/`:
        - `lib/`:  Chứa các hàm morphology cho ảnh nhị phân có sẵn trong các thư viện opencv, skimage, ...
        - `non_lib/`: Chứa các hàm morphology cho ảnh nhị phân tự cài đặt, chỉ sử dụng thư viện numpy để hỗ trợ các phép tính trên ma trận. 
    - `grayscale`: 
        - `lib/`:  Chứa các hàm morphology cho ảnh mức xám có sẵn trong các thư viện 
        - `non_lib/`: Chứa các hàm morphology cho ảnh mức xám tự cài đặt, chỉ sử dụng thư viện numpy để hỗ trợ các phép tính trên ma trận. 
    - `UI.py`: Giao diện cho chương trình của chúng tôi 


## Cài đặt
Đảm bảo bạn đã cài đặt các thư viện cần thiết:
  ```bash
      pip install -r requirements.txt
  ```
## Hướng dẫn sử dụng
1. ** chạy chương trình**
   -  Mở terminal và di chuyển đến thư mục `src/`
   - Chạy file UI.py để khởi động giao diện:
     ```bash
     python function/UI.py
     ```
2. **Sử dụng giao diện**
   - Chọn loại ảnh (nhị phân hoặc mức xám)
   - Chọn các phép biến đổi morphology từ danh sách có sẵn
   - Xem kết quả trực tiếp trên giao diện và lưu lại nếu cần

