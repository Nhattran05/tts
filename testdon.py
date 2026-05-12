from vieneu import Vieneu

# Initialize TTS
tts = Vieneu()

# List voices
voices = tts.list_preset_voices()

if not voices:
    raise ValueError("No preset voices found")

# Chọn voice
my_voice_id = voices[3][1]
voice_data = tts.get_preset_voice(my_voice_id)

# Text
text_medical = """
máy sấy aqua nhà tôi cứ kêu tít tít mà không chạy, bên em bán kiểu gì vậy? tôi cần xử lý ngay bây giờ. tôi bấm đi bấm lại mấy lần rồi, cứ tít tít xong đứng im. đừng bắt tôi tự mò thêm nữa.

em hỏi gì vậy? nói rõ đi. máy nó có điện, bấm lên thì kêu tít tít, nhưng lồng không quay, quần áo vẫn ướt. tôi đang cần sấy gấp cho con đi học sáng mai, đừng hỏi vòng vo nữa.

đúng, bấm start là nó tít tít rồi đứng im luôn. có điện, màn hình vẫn lên. tôi nói từ nãy rồi, cần xử lý ngay chứ không phải nhắc lại mãi.

ừ, cái này thì nói ngay từ đầu có phải nhanh hơn không. lúc nãy tôi nhét hơi nhiều đồ, cửa có thể chưa khép thật chặt. giờ tôi ấn mạnh lại thì thấy nó kín hơn. tiếp theo làm gì nói luôn đi.

tôi đang chọn chế độ gió , kiểu thổi hơi ấy. tôi nghĩ chọn cái đó thì khô nhanh hơn , xong bấm start thì nó tít tít mà không chạy như mong đợi. nói ngắn gọn giúp tôi , giờ tôi cần máy chạy được.

được, cái này còn nghe hợp lý. máy nhà tôi đang cắm chung ổ nối với máy giặt với cả bàn ủi , mà cái ổ đó dạo này cũng chập chờn. tôi rút ra cắm lại trực tiếp thì thử được. nhưng nói rõ luôn nhé , nếu vẫn không chạy thì bên em phải cho người qua kiểm tra tại nhà cho tôi. đừng để tôi gọi đi gọi lại.
"""

# Generate audio
audio_custom = tts.infer(
    text=text_medical,
    voice=voice_data
)

# Save audio
output_file = "output_bichngoc.wav"
tts.save(audio_custom, output_file)

print(f"saved to {output_file}")