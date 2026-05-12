from vieneu import Vieneu
import sounddevice as sd
import numpy as np

tts = Vieneu(mode="turbo")

# ====================== WARM-UP MODEL (RẤT QUAN TRỌNG) ======================
print("Warming up model... (giúp giảm kéo dài phần đầu)")
_ = tts.infer("Xin chào", max_chars=50)   # Chạy 1 lần dummy để khởi động
print("Warm-up xong!")

text = """Bệnh nhân nam 58 tuổi nhập viện vì đau ngực kéo dài 2 giờ, 
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

print("Bắt đầu sinh audio...")

stream = sd.OutputStream(samplerate=24000, channels=1, dtype='float32', blocksize=512, latency='low')
stream.start()

buffer = []
MIN_BUFFER = 2

for i, chunk in enumerate(tts.infer_stream(
    text=text,
    max_chars=30,          # Giảm mạnh
    temperature=0.2,       # Giảm temperature → ít "suy nghĩ" hơn
    top_k=30,              # Giảm top_k
    top_p=0.9,
)):
    if len(chunk) > 0:
        buffer.append(chunk.astype(np.float32))
        print(f"Chunk {i+1} ({len(chunk)} samples)")
        
        if len(buffer) >= MIN_BUFFER:
            audio_block = np.concatenate(buffer)
            stream.write(audio_block.reshape(-1, 1))
            buffer = []

# Phát nốt phần còn lại
if buffer:
    audio_block = np.concatenate(buffer)
    stream.write(audio_block.reshape(-1, 1))

stream.stop()
stream.close()
print("Hoàn tất!")