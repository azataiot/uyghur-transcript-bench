[ئۇيغۇرچە](README.ug.md)

# Uyghur Speech-to-Text Benchmark

Benchmarking and comparing Speech-to-Text (STT) software that supports the Uyghur language.

## Purpose

This repository evaluates the accuracy and quality of various STT products for Uyghur language transcription. Each product is tested against the same audio samples, and results are compared side by side.

## Structure

Each folder in the repository root represents a different STT product/service:

```
uyghur-transcript-bench/
├── README.md
├── samples/                   # Shared test audio files
├── gheyret-asr/               # Gheyret ASR source (submodule)
├── qwen3-asr/                 # Qwen3-ASR notes
├── sonix/                     # Sonix notes
├── speechmatics/              # Speechmatics source (submodule)
├── results/
│   ├── gheyret-asr/           # Gheyret ASR results
│   ├── qwen3-asr/             # Qwen3-ASR results
│   ├── sonix/                 # Sonix results
│   └── speechmatics/          # Speechmatics results
└── ...
```

## Products Tested

| Product | Type | Output Script | Source | Results | Notes |
|---------|------|---------------|--------|---------|-------|
| [Gheyret ASR](https://github.com/gheyret/uyghur-asr-transformer) | Open-source transformer | Latin (ULY) | [gheyret-asr/](gheyret-asr/) (submodule) | [results/gheyret-asr/](results/gheyret-asr/) | |
| [Qwen3-ASR](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | Open-source LLM | — | [qwen3-asr/](qwen3-asr/) | [results/qwen3-asr/](results/qwen3-asr/) | Planned — no official Uyghur support, requires NVIDIA GPU, [reportedly works](https://blog.csdn.net/weixin_42599908/article/details/158059889) |
| [Sonix](https://sonix.ai/) | Commercial SaaS | Arabic | [sonix/](sonix/) | [results/sonix/](results/sonix/) | |
| [Speechmatics](https://www.speechmatics.com/) | Commercial API | Arabic | [speechmatics/](speechmatics/) (submodule) | [results/speechmatics/](results/speechmatics/) | |

## Test Samples

All samples are in the [`samples/`](samples/) folder.

| Sample | Difficulty | Duration | Description |
|--------|------------|----------|-------------|
| `antal-hadi.mp3` | Hard | 4:03 | Dialect variant — spoken Uyghur with heavy dialect |
| `dastan-01.mp3` | Medium | 2:26 | Good audio quality, realistic scenario, low background music |
| `dutar-01.mp3` | Hard | 2:44 | Background music, child crying, noisy environment |
| `speedy-01.mp3` | Medium | 0:36 | Faster-than-normal speech tempo |

## Disclaimer

The audio samples in this repository were collected from the internet and are intended for **research and educational purposes only**. If you are the copyright holder of any sample and wish to have it removed, please open an issue.

## License

This work is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
