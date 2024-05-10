import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write


class Generator:
    def __init__(self, pretrained="facebook/musicgen-melody"):
        self.model = pretrained
        self.output = None
        self.melody_wavs = None
        self.melody_sample_rate = None

    def create_model(self, pretrained="facebook/musicgen-melody"):
        self.model = MusicGen.get_pretrained(pretrained)

    def config_model(self, duration=6, top_k=250, temperature=1, cfg_coef=10):
        self.model.set_generation_params(duration, top_k, temperature, cfg_coef)

    def load_melody(self, filename):
        self.melody_wavs, self.melody_sample_rate = torchaudio.load(filename)
        self.melody_wavs = self.melody_wavs.unsqueeze(0).repeat(1,1,1)
    
    def generate_audio(self, description, progress=True, return_tokens=True):
        self.output = self.model.generate_with_chroma(
            descriptions=[description],
            melody_wavs=self.melody_wavs,
            melody_sample_rate=self.melody_sample_rate,
            progress=progress, return_tokens=return_tokens
        )

    def generate_audios(self, descriptions, progress=True, return_tokens=True):
        self.output = self.model.generate_with_chroma(
            descriptions=descriptions,
            melody_wavs=self.melody_wavs,
            melody_sample_rate=self.melody_sample_rate,
            progress=progress, return_tokens=return_tokens
        )

    def save_output(self, output_filename, single_file=True):
        if single_file:
            audio_write(output_filename, self.output[0][0], self.model.sample_rate)



