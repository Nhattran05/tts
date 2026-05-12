from vieneu import Vieneu

# Initialize
tts = Vieneu()

# 1. Simple synthesis
text = """Hệ thống điện hiện đại chủ yếu sử dụng alternating current (AC) because it is 
more efficient trong việc truyền tải năng lượng trên khoảng cách xa. Khi dùng AC, 
voltage can be easily stepped up or stepped down thông qua transformers, giúp giảm tổn 
thất năng lượng trong dây dẫn. This is a key advantage compared to direct current (DC), 
vốn gặp khó khăn hơn trong việc biến đổi điện áp một cách linh hoạt. Trong thực tế, power 
plants generate electricity and then transmit it across long distances using high-voltage 
AC, sau đó được hạ áp xuống mức an toàn để sử dụng trong households and industrial 
systems. Ngoài ra, AC systems are simpler in terms of infrastructure và có chi phí vận 
hành thấp hơn trong nhiều trường hợp. Tuy nhiên, DC vẫn có vai trò nhất định trong một 
số ứng dụng như battery storage, electronic devices, và high-voltage DC transmission 
(HVDC) trong các hệ thống đặc biệt. Việc lựa chọn giữa AC và DC depends on the specific 
use case, nhưng nhìn chung AC remains the dominant standard trong hệ thống điện toàn 
cầu. This combination of efficiency, flexibility, and cost-effectiveness makes alternating 
current the preferred choice trong hầu hết các quốc gia hiện nay, especially in large-scale 
power distribution networks."""
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
text_medical = """Chào anh, dựa trên kết quả nội soi vừa rồi, tôi thấy niêm mạc dạ dày của anh đang bị viêm khá nặng.

Triệu chứng ợ chua và đau rát vùng thượng vị mà anh mô tả chính là biểu hiện điển hình của tình trạng trào ngược dạ dày thực quản. Nguyên nhân chủ yếu có thể do chế độ ăn uống không điều độ và áp lực căng thẳng kéo dài khiến dạ dày tăng tiết axit quá mức.

Để điều trị dứt điểm, tôi sẽ kê cho anh một đợt thuốc ức chế bơm proton để giúp giảm bớt dịch vị. Anh cần đặc biệt lưu ý việc thay đổi lối sống, hạn chế tối đa đồ ăn cay nóng và rượu bia.

Đặc biệt, anh tuyệt đối không nên nằm ngay sau khi ăn để tránh tình trạng trào ngược trở nên tồi tệ hơn. Nếu anh tuân thủ đúng phác đồ điều trị này, các vết loét trong dạ dày sẽ sớm hồi phục thôi.

Bây giờ anh có thắc mắc gì về các tác dụng phụ của thuốc hay cần tôi tư vấn thêm về thực đơn ăn uống hằng ngày không?
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
text_medical = """Bệnh nhân nam 58 tuổi nhập viện vì đau ngực kéo dài 2 giờ, 
lan lên vai trái, kèm khó thở nhẹ và vã mồ hôi. Tiền sử có tăng huyết áp, 
đái tháo đường type 2 và rối loạn lipid máu. Trước nhập viện, bệnh nhân dùng 
Amlodipine 5 mg/ngày, Metformin 1000 mg/ngày, và Atorvastatin 20 mg/ngày nhưng 
uân thủ không đều. Tại khoa cấp cứu, bệnh nhân được cho dùng Aspirin 300 mg nhai, 
Clopidogrel 300 mg, Heparin truyền tĩnh mạch và Nitroglycerin ngậm dưới lưỡi. 
Điện tâm đồ gợi ý hội chứng vành cấp, sau đó bệnh nhân được chỉ định dùng thêm 
Metoprolol để kiểm soát nhịp tim và Morphine giảm đau. Sau can thiệp, phác đồ duy 
trì gồm Enalapril, Rosuvastatin, cùng Insulin điều chỉnh đường huyết. Bệnh nhân 
được theo dõi sát dấu hiệu sinh tồn, xét nghiệm men tim và tư vấn thay đổi lối sống.
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
text_medical = """Bệnh nhân nam 58 tuổi nhập viện vì đau ngực kéo dài 2 giờ, 
lan lên vai trái, kèm khó thở nhẹ và vã mồ hôi. Tiền sử có tăng huyết áp, 
đái tháo đường type 2 và rối loạn lipid máu. Trước nhập viện, bệnh nhân dùng 
Amlodipine 5 mg/ngày, Metformin 1000 mg/ngày, và Atorvastatin 20 mg/ngày nhưng 
uân thủ không đều. Tại khoa cấp cứu, bệnh nhân được cho dùng Aspirin 300 mg nhai, 
Clopidogrel 300 mg, Heparin truyền tĩnh mạch và Nitroglycerin ngậm dưới lưỡi. 
Điện tâm đồ gợi ý hội chứng vành cấp, sau đó bệnh nhân được chỉ định dùng thêm 
Metoprolol để kiểm soát nhịp tim và Morphine giảm đau. Sau can thiệp, phác đồ duy 
trì gồm Enalapril, Rosuvastatin, cùng Insulin điều chỉnh đường huyết. Bệnh nhân 
được theo dõi sát dấu hiệu sinh tồn, xét nghiệm men tim và tư vấn thay đổi lối sống.
"""

audio_custom = tts.infer(
    text=text_medical,
    voice=voice_data
)

tts.save(audio_custom, "output_bichngoc.wav")
print("Saved to output_bichngoc.wav")
