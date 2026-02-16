# Transcribe Uyghur audio samples using Meta MMS (mms-1b-all) model.
# Azat (@azataiot) 2026-02-16

import os
import sys
import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, AutoProcessor

MODEL_ID = "facebook/mms-1b-all"
TARGET_LANG = "uig-script_arabic"
SAMPLE_RATE = 16000

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
SAMPLES_DIR = os.path.join(REPO_ROOT, "samples")
RESULTS_DIR = os.path.join(REPO_ROOT, "results", "meta-mms")

SAMPLES = ["antal-hadi.mp3", "dastan-01.mp3", "dutar-01.mp3", "speedy-01.mp3"]


def load_model():
    print("Loading model: %s (lang: %s)" % (MODEL_ID, TARGET_LANG))
    processor = AutoProcessor.from_pretrained(MODEL_ID, target_lang=TARGET_LANG)
    model = Wav2Vec2ForCTC.from_pretrained(
        MODEL_ID, target_lang=TARGET_LANG, ignore_mismatched_sizes=True
    )
    model.eval()
    return processor, model


def transcribe(processor, model, audio_path):
    audio, sr = torchaudio.load(audio_path)
    if audio.shape[0] > 1:
        audio = audio.mean(dim=0, keepdim=True)
    if sr != SAMPLE_RATE:
        audio = torchaudio.transforms.Resample(sr, SAMPLE_RATE)(audio)
    inputs = processor(
        audio.squeeze().numpy(), sampling_rate=SAMPLE_RATE, return_tensors="pt"
    )
    with torch.no_grad():
        logits = model(**inputs).logits
    ids = torch.argmax(logits, dim=-1)[0]
    return processor.decode(ids)


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    processor, model = load_model()

    for sample in SAMPLES:
        audio_path = os.path.join(SAMPLES_DIR, sample)
        if not os.path.exists(audio_path):
            print("SKIP: %s not found" % audio_path)
            continue

        name = os.path.splitext(sample)[0]
        print("Transcribing: %s" % sample)
        text = transcribe(processor, model, audio_path)

        out_path = os.path.join(RESULTS_DIR, name + ".txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        print("  -> %s" % out_path)
        print("  Preview: %s..." % text[:100])

    print("Done.")


if __name__ == "__main__":
    main()
