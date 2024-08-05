from pydub import AudioSegment
from pydub.generators import Sine

# Gerar sons
normal_sound = Sine(440).to_audio_segment(duration=1000)  # 440 Hz, 1 segundo
despair_sound = Sine(220).to_audio_segment(duration=1000)  # 220 Hz, 1 segundo
hope_sound = Sine(880).to_audio_segment(duration=1000)  # 880 Hz, 1 segundo

# Salvar sons como arquivos WAV
normal_sound.export("normal.wav", format="wav")
despair_sound.export("despair.wav", format="wav")
hope_sound.export("hope.wav", format="wav")
