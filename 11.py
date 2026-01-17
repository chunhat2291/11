import streamlit as st
from datetime import datetime

# --- BƯỚC 1: TẠO FORM VÀ CÁC THÀNH PHẦN GIAO DIỆN ---
# Gọi thư viện streamlit
with st.form('Order đồ uống'):
    # Thiết lập các danh sách lựa chọn
    drinks = ('Trà sữa truyền thống', 'Trà sữa matcha', 'Trà sữa trái cây')
    sizes = ('S', 'M', 'L')
    sugars = ('Đường trắng', 'Đường nâu', 'Không thêm đường')
    jellys = ('Thạch rau câu', 'Thạch nha đam', 'Không thêm thạch')
    
    # Tạo các thành phần giao diện (Widgets)
    option_drink = st.selectbox('Bạn muốn loại đồ uống gì?', drinks)
    option_size = st.selectbox('Chọn size cho đồ uống:', sizes)
    option_sugar = st.selectbox('Bạn thích thêm loại đường nào cho đồ uống của bạn?', sugars)
    option_jelly = st.selectbox('Bạn thích thêm loại thạch nào cho đồ uống của bạn?', jellys)
    
    # Chọn số lượng bằng slider từ 0 đến 10
    nums = st.slider('Số lượng bạn muốn đặt:', 0, 10, 0)
    
    # Thêm phần ghi chú thêm cho người dùng
    note = st.text_area('Ghi chú thêm cho đơn hàng:')
    
    # Tạo nút submit "Xác nhận" để gửi form
    submitted = st.form_submit_button("Xác nhận")

    # --- BƯỚC 2: LƯU TRỮ VÀ IN KẾT QUẢ ---
    # Lưu các lựa chọn vào 1 dictionary
    bill_data = {
        'Loại đồ uống:': option_drink,
        'Size:': option_size,
        'Loại đường:': option_sugar,
        'Loại thạch:': option_jelly,
        'Số lượng:': nums,
        'Ghi chú:': note
    }

    if submitted:
        st.write('### Bạn đã chọn:')
        for x, y in bill_data.items():
            st.write(f"- **{x}** {y}")

# --- BƯỚC 3: TẠO NÚT DOWNLOAD VÀ TÙY CHỈNH NỘI DUNG BILL ---
# Tạo hộp kiểm "In hoá đơn"
print_bill = st.checkbox('In hoá đơn')

if print_bill:
    # Sáng tạo thêm: Tên shop và ngày giờ
    shop_header = "--- CỬA HÀNG ĐỒ UỐNG PYDC ---"
    current_time = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
    
    # Lưu hoá đơn vào biến ans để có thể tải xuống
    ans = f"{shop_header}\n"
    ans += f"Ngày giờ xuất hóa đơn: {current_time}\n"
    ans += "="*30 + "\n"
    
    for key in bill_data:
        ans += f"{key} {bill_data[key]}\n"
    
    # Tạo nút download_button
    st.download_button(
        label='Tải hoá đơn xuống', 
        data=ans, 
        file_name='hoa_don_order.txt'
    )