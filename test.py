from vieneu import Vieneu

# Initialize
tts = Vieneu()

# 1. Simple synthesis
text = """Chào bạn, mình đang tìm hiểu máy sấy aqua, bạn tư vấn ngắn gọn giúp mình máy này có gì nổi bật với bảo hành bao lâu được không?

Ừm, phần đó nghe cũng hợp nhu cầu đó. Bạn nói ngắn gọn vậy là được. Mình hỏi tiếp nhé: nếu mình cần quần áo đỡ nhăn với bớt mùi thì máy này có hỗ trợ gì không?

Ừm, vậy là mình hiểu ý chính rồi: có hỗ trợ đỡ nhăn và có chế độ giúp giảm mùi, làm mới quần áo. Nghe cũng đúng cái mình đang quan tâm. Cho mình hỏi tiếp luôn: bảo hành cụ thể bao lâu, và tính từ ngày mua hay ngày sản xuất?

Ok, phần bảo hành bạn nói vậy là rõ rồi. Mình hỏi thêm ý cuối giúp mình nhé: nếu mình chồng máy sấy lên máy giặt nhà mình đang dùng hãng khác thì có bị ảnh hưởng bảo hành không?

Ừm, vậy thì yên tâm hơn rồi, vì nhà mình đang dùng máy giặt hãng khác nên mình lo 
khoản đó nhất. Với nhà mình ban công cũng hơi nhỏ nên mình đang nghiêng về phương án xếp 
chồng. Bạn tư vấn tiếp giúp mình ngắn gọn thôi nhé: nếu mình đang xem mẫu V901K thì thời 
điểm này bảo hành của mẫu đó có gì khác không? Nếu có, nói rõ giúp mình luôn để mình còn cân nhắc đi xem mẫu hoặc hỏi nơi mua."""
audio = tts.infer(text=text)

tts.save(audio, "output_xuan_vinh.wav")
print("Saved to output_xuan_vinh.wav")


# 2. List voices
voices = tts.list_preset_voices()

if not voices:
    raise ValueError("No preset voices found")

for desc, voice_id in voices:
    print(f"Voice: {desc} (ID: {voice_id})")

# Chọn voice an toàn (tránh index lỗi)
my_voice_id = voices[2][1] if len(voices) > 1 else voices[0][1]

voice_data = tts.get_preset_voice(my_voice_id)


# 3. Text (không dùng raw string để tránh lỗi xuống dòng)
text_medical = """Alo, cho tôi hỏi đây có phải bộ phận hỗ trợ aqua không? Máy sấy nhà tôi cứ kêu tít tít rồi không chạy, nhờ kiểm tra giúp tôi với.

Vâng, chị đang cần gấp lắm. Máy nhà tôi vẫn lên đèn, bấm thì nó cứ tít tít mấy tiếng thôi chứ không chạy, lồng không quay luôn. Hôm qua còn dùng bình thường.

Tôi đóng rồi mà. Sáng giờ bấm mấy lần vẫn vậy đó.

Tôi có bấm thử mấy chương trình khác nhau rồi, chương trình nào nó cũng tít tít chứ không chạy. Giờ cụ thể tôi cần kiểm tra cái gì trước?
"""

audio_custom = tts.infer(
    text=text_medical,
    voice=voice_data
)

tts.save(audio_custom, "output_pham_tuyen.wav")
print("Saved to output_pham_tuyen.wav")

my_voice_id = voices[2][1] if len(voices) > 1 else voices[0][1]

voice_data = tts.get_preset_voice(my_voice_id)


# 3. Text (không dùng raw string để tránh lỗi xuống dòng)
text_medical = """Vâng, mình bắt đầu nhé. Câu 1: Thời gian bảo hành 
của sản phẩm aqua được tính theo nguyên tắc nào? Khi nào tính theo ngày mua, 
khi nào tính theo ngày sản xuất?

Đúng ý chính rồi em nhé. Em nhớ thêm một lưu ý nhỏ: biên nhận hay đơn bán 
lẻ không dùng để tính thời hạn bảo hành. Mình sang câu 2: Điều kiện để một sản phẩm được bảo hành miễn phí là gì?

Tốt, câu 2 em trả lời đúng rồi: còn trong thời hạn bảo hành và lỗi kỹ thuật 
từ nhà sản xuất. Mình tiếp câu 3 nhé: Nêu ít nhất 4 trường hợp phổ biến bị từ chối bảo hành.

Ổn rồi, em đã nêu được hơn 4 ý đúng. Có thể nhớ thêm các nhóm hay gặp như 
côn trùng/vật lạ gây hỏng, sai hoặc chỉnh sửa số máy, và vệ sinh bảo trì định kỳ không thuộc bảo hành. Câu 4: Khách hàng có thể gửi yêu cầu bảo hành cho aqua qua những kênh nào? Nêu thêm thời gian làm việc của tổng đài.

Em nhớ đúng được kênh và khung giờ, nhưng thông tin số tổng đài với email 
đang chưa chính xác nhé. Em thử trả lời lại 1 lần, nhớ giúp cô:

zalo aqua Việt Nam
website yêu cầu bảo hành
email
tổng đài và giờ làm việc

Mời em trả lời lại câu 4.

Chưa đúng em nhé, cô chốt lại để em nhớ:

Zalo aqua Việt Nam
Website yêu cầu bảo hành
Email: cskh@aquavietnam.vn
Tổng đài: 1800 58 58 32
Thời gian làm việc tổng đài: 7:00 đến 19:00, tất cả các ngày

Mình sang câu 5 luôn nhé: Cho cô 3 ví dụ về thời hạn bảo hành của các nhóm 
sản phẩm aqua mà em nhớ chắc, kèm lưu ý nếu đó là bảo hành sản phẩm hay bảo hành linh kiện chính.

Tốt em nhé, 3 ví dụ đó đều đúng ở mức mốc cơ bản. Nếu đầy đủ hơn thì em có 
thể nói thêm đây là bảo hành sản phẩm; còn một số nhóm có bảo hành linh kiện chính riêng như máy nén. Vì em trả lời khá ổn, cô hỏi thêm 1 câu ngắn nhé: Biên nhận hoặc đơn bán lẻ có được dùng để tính thời hạn bảo hành không?

Đúng rồi em, ý đúng là biên nhận hoặc đơn bán lẻ không được dùng để tính thời 
hạn bảo hành. Hôm nay mình dừng tại đây nhé. Em nắm được phần nguyên tắc tính hạn, 
điều kiện miễn phí, các trường hợp từ chối và kênh tiếp nhận rồi; chỉ cần rà lại 
chính xác số tổng đài và email là tốt hơn. Cảm ơn em, chúc em học tốt nhé.
"""

audio_custom = tts.infer(
    text=text_medical,
    voice=voice_data
)

tts.save(audio_custom, "output_thucdoan.wav")
print("Saved to output_thucdoan.wav")

my_voice_id = voices[0][1] if len(voices) > 1 else voices[0][1]

voice_data = tts.get_preset_voice(my_voice_id)


# 3. Text (không dùng raw string để tránh lỗi xuống dòng)
text_medical = """Máy sấy aqua nhà tôi cứ kêu tít tít mà không chạy, bên em bán kiểu gì vậy? Tôi cần xử lý ngay bây giờ.

Rồi , nói nhanh giúp tôi đi . Tôi bấm đi bấm lại mấy lần rồi , cứ tít tít xong đứng im. Đừng bắt tôi tự mò thêm nữa.

Em hỏi gì vậy? nói rõ đi. máy nó có điện, bấm lên thì kêu tít tít, nhưng lồng không quay, quần áo vẫn ướt. Tôi đang cần sấy gấp cho con đi học sáng mai, đừng hỏi vòng vo nữa.

Đúng, bấm Start là nó tít tít rồi đứng im luôn. Có điện, màn hình vẫn lên. Tôi nói từ nãy rồi, cần xử lý ngay chứ không phải nhắc lại mãi.

Ừ, cái này thì nói ngay từ đầu có phải nhanh hơn không. Lúc nãy tôi nhét hơi nhiều đồ, cửa có thể chưa khép thật chặt. Giờ tôi ấn mạnh lại thì thấy nó kín hơn. Tiếp theo làm gì nói luôn đi.

Tôi đang chọn chế độ gió, kiểu thổi hơi ấy. Tôi nghĩ chọn cái đó thì khô nhanh hơn, xong bấm Start thì nó tít tít mà không chạy như mong đợi. Nói ngắn gọn giúp tôi, giờ tôi cần máy chạy được.

Được, cái này còn nghe hợp lý. Máy nhà tôi đang cắm chung ổ nối với máy giặt với cả bàn ủi, mà cái ổ đó dạo này cũng chập chờn. Tôi rút ra cắm lại trực tiếp thì thử được, nhưng nói rõ luôn nhé: nếu vẫn không chạy thì bên em phải cho người qua kiểm tra tại nhà cho tôi, đừng để tôi gọi đi gọi lại.
"""

audio_custom = tts.infer(
    text=text_medical,
    voice=voice_data
)

tts.save(audio_custom, "output_bichngoc.wav")
print("Saved to output_bichngoc.wav")
