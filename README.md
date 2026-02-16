[ئۇيغۇرچە](README.ug.md)

# Uyghur Speech-to-Text Benchmark

Benchmarking and comparing Speech-to-Text (STT) software that supports the Uyghur language.

## Purpose

This repository evaluates the accuracy and quality of various STT products for Uyghur language transcription. Each product is tested against the same audio samples, and results are compared side by side.

## Structure

```
uyghur-stt-bench/
├── README.md
├── samples/                       # Shared test audio files
├── providers/
│   ├── bilingual-asr/             # BilingualASR notes
│   ├── gheyret-asr/               # Gheyret ASR source (submodule)
│   ├── konch/                     # Konch notes
│   ├── openl/                     # OpenL notes
│   ├── qwen3-asr/                 # Qwen3-ASR notes
│   ├── sonix/                     # Sonix notes
│   ├── speechmatics/              # Speechmatics source (submodule)
│   └── speechyou/                 # SpeechYou notes
├── results/
│   ├── bilingual-asr/             # BilingualASR results
│   ├── gheyret-asr/               # Gheyret ASR results
│   ├── konch/                     # Konch results
│   ├── openl/                     # OpenL results
│   ├── qwen3-asr/                 # Qwen3-ASR results
│   ├── sonix/                     # Sonix results
│   ├── speechmatics/              # Speechmatics results
│   └── speechyou/                 # SpeechYou results
└── ...
```

## Products Tested

| Product | Type | Output Script | Source | Results | Notes |
|---------|------|---------------|--------|---------|-------|
| [BilingualASR](https://github.com/GSQZ/BilingualASR) | Open-source (Uyghur+Chinese) | — | [providers/bilingual-asr/](providers/bilingual-asr/) | [results/bilingual-asr/](results/bilingual-asr/) | Blocked — pretrained model download links are broken |
| [Clipto](https://www.clipto.com/) | Commercial SaaS | — | — | — | Claims Uyghur support but does not actually provide it |
| [GoTranscript](https://gotranscript.com/our-languages) | Commercial SaaS | — | — | — | Requires requesting a quote and multi-step setup, no easy trial — skipped for now |
| [Gheyret ASR](https://github.com/gheyret/uyghur-asr-transformer) | Open-source transformer | Latin (ULY) | [providers/gheyret-asr/](providers/gheyret-asr/) (submodule) | [results/gheyret-asr/](results/gheyret-asr/) | |
| [Konch](https://app.konch.ai/) | Commercial SaaS | Arabic | [providers/konch/](providers/konch/) | [results/konch/](results/konch/) | Web interface |
| [Lingvanex](https://lingvanex.com/services/uyghur-speech-to-text/) | Commercial SaaS | — | — | — | Claims Uyghur support but does not actually provide it |
| [OpenL](https://openl.io/translate/speech/uyghur) | Commercial SaaS | Arabic | [providers/openl/](providers/openl/) | [results/openl/](results/openl/) | Web interface |
| [Qwen3-ASR](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | Open-source LLM | — | [providers/qwen3-asr/](providers/qwen3-asr/) | [results/qwen3-asr/](results/qwen3-asr/) | Planned — no official Uyghur support, requires NVIDIA GPU, [reportedly works](https://blog.csdn.net/weixin_42599908/article/details/158059889) |
| [Sonix](https://sonix.ai/) | Commercial SaaS | Arabic | [providers/sonix/](providers/sonix/) | [results/sonix/](results/sonix/) | |
| [Transkriptor](https://transkriptor.com/) | Commercial SaaS | — | — | — | Claims Uyghur support but does not actually provide it |
| [TransPerfect](https://www.transperfect.com/) | Commercial SaaS | — | — | — | Listed as top Uyghur STT provider but supported languages do not include Uyghur |
| [TurboScribe](https://turboscribe.ai/) | Commercial SaaS | — | — | — | Claims Uyghur support but transcribes to Turkish instead |
| [Speechmatics](https://www.speechmatics.com/) | Commercial API | Arabic | [providers/speechmatics/](providers/speechmatics/) (submodule) | [results/speechmatics/](results/speechmatics/) | |
| [SpeechYou](https://app.speechyou.com/) | Commercial SaaS | Arabic | [providers/speechyou/](providers/speechyou/) | [results/speechyou/](results/speechyou/) | Web interface |

## Test Samples

All samples are in the [`samples/`](samples/) folder.

| Sample | Difficulty | Duration | Description |
|--------|------------|----------|-------------|
| `antal-hadi.mp3` | Hard | 4:03 | Dialect variant — spoken Uyghur with heavy dialect |
| `dastan-01.mp3` | Medium | 2:26 | Good audio quality, realistic scenario, low background music |
| `dutar-01.mp3` | Hard | 2:44 | Background music, child crying, noisy environment |
| `speedy-01.mp3` | Medium | 0:36 | Faster-than-normal speech tempo |

## Provider Selection

The products listed above were found by searching Google and Bing for Uyghur speech-to-text services across the first 10 pages of results. Every service that appeared in those results was evaluated. Many websites and apps claim to support Uyghur, but do not actually offer it — for example, some have no Uyghur option in their language selector on the web interface, or no Uyghur option in their SDK/API when attempting to submit audio for transcription. Only products that genuinely provide Uyghur STT functionality (or have an open-source model targeting Uyghur) are included in the benchmark. The selection is not based on any bias or preference.

## Disclaimer

The audio samples in this repository were collected from the internet and are intended for **research and educational purposes only**. If you are the copyright holder of any sample and wish to have it removed, please open an issue.

## License

This work is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
