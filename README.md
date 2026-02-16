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
├── speechmatics/              # Speechmatics source (submodule)
├── results/
│   └── speechmatics/          # Benchmark results
└── ...
```

## Products Tested

| Product | Source | Results |
|---------|--------|---------|
| [Speechmatics](https://www.speechmatics.com/) | [speechmatics/](speechmatics/) (submodule) | [results/speechmatics/](results/speechmatics/) |

## Test Samples

| Sample | Difficulty | Duration | Description |
|--------|------------|----------|-------------|
All samples are in the [`samples/`](samples/) folder.

| Sample | Difficulty | Duration | Description |
|--------|------------|----------|-------------|
| `antal-hadi.mp3` | Hard | 4:03 | Dialect variant — spoken Uyghur with heavy dialect |
| `dastan-01.mp3` | Medium | 2:26 | Good audio quality, realistic scenario, low background music |
| `dutar-01.mp3` | Hard | 2:44 | Background music, child crying, noisy environment |
| `speedy-01.mp3` | Medium | 0:36 | Faster-than-normal speech tempo |
