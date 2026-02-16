[English](README.md)

# ئۇيغۇرچە ئاۋاز-تېكىستكە ئايلاندۇرۇش سىنىقى

ئۇيغۇر تىلىنى قوللايدىغان ئاۋازنى تېكىستكە ئايلاندۇرۇش (STT) يۇمشاق دېتاللىرىنى سىناش ۋە سېلىشتۇرۇش.

## مەقسەت

بۇ ئامبار ھەر خىل STT مەھسۇلاتلىرىنىڭ ئۇيغۇرچە ئاۋاز تونۇش سۈپىتىنى باھالايدۇ. ھەر بىر مەھسۇلات ئوخشاش ئاۋاز نۇسخىلىرى بىلەن سىنالغاندىن كېيىن، نەتىجىلەر بىر-بىرلەپ سېلىشتۇرۇلىدۇ.

## قۇرۇلما

ئامبارنىڭ ئاساسىي مۇندەرىجىسىدىكى ھەر بىر ھۆججەتقىسقۇچ بىر STT مەھسۇلاتىنى كۆرسىتىدۇ:

```
uyghur-stt-bench/
├── README.md
├── samples/                       # ئورتاق سىناق ئاۋاز ھۆججەتلىرى
├── providers/
│   ├── bilingual-asr/             # BilingualASR خاتىرىلىرى
│   ├── gheyret-asr/               # Gheyret ASR ئەسلى كودى (تارماق مودۇل)
│   ├── konch/                     # Konch خاتىرىلىرى
│   ├── qwen3-asr/                 # Qwen3-ASR خاتىرىلىرى
│   ├── sonix/                     # Sonix خاتىرىلىرى
│   ├── speechmatics/              # Speechmatics ئەسلى كودى (تارماق مودۇل)
│   └── speechyou/                 # SpeechYou خاتىرىلىرى
├── results/
│   ├── bilingual-asr/             # BilingualASR نەتىجىلىرى
│   ├── gheyret-asr/               # Gheyret ASR نەتىجىلىرى
│   ├── konch/                     # Konch نەتىجىلىرى
│   ├── qwen3-asr/                 # Qwen3-ASR نەتىجىلىرى
│   ├── sonix/                     # Sonix نەتىجىلىرى
│   ├── speechmatics/              # Speechmatics نەتىجىلىرى
│   └── speechyou/                 # SpeechYou نەتىجىلىرى
└── ...
```

## سىنالغان مەھسۇلاتلار

| مەھسۇلات | تىپى | يېزىق | ئەسلى كود | نەتىجىلەر | ئىزاھات |
|-----------|------|-------|------------|------------|---------|
| [BilingualASR](https://github.com/GSQZ/BilingualASR) | ئوچۇق كودلۇق (ئۇيغۇرچە+خەنزۇچە) | — | [providers/bilingual-asr/](providers/bilingual-asr/) | [results/bilingual-asr/](results/bilingual-asr/) | توسالغان — مودېل چۈشۈرۈش ئۇلانمىلىرى بۇزۇلغان |
| [Gheyret ASR](https://github.com/gheyret/uyghur-asr-transformer) | ئوچۇق كودلۇق transformer | لاتىن (ULY) | [providers/gheyret-asr/](providers/gheyret-asr/) (تارماق مودۇل) | [results/gheyret-asr/](results/gheyret-asr/) | |
| [Konch](https://app.konch.ai/) | تىجارەت SaaS | ئەرەب | [providers/konch/](providers/konch/) | [results/konch/](results/konch/) | تور كۆرۈنمىسى |
| [Qwen3-ASR](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | ئوچۇق كودلۇق LLM | — | [providers/qwen3-asr/](providers/qwen3-asr/) | [results/qwen3-asr/](results/qwen3-asr/) | پىلانلانغان — رەسمىي ئۇيغۇرچە قوللىمايدۇ، NVIDIA GPU كېرەك، [ئىشلەيدىغانلىقى خەۋەر قىلىندى](https://blog.csdn.net/weixin_42599908/article/details/158059889) |
| [Sonix](https://sonix.ai/) | تىجارەت SaaS | ئەرەب | [providers/sonix/](providers/sonix/) | [results/sonix/](results/sonix/) | |
| [Speechmatics](https://www.speechmatics.com/) | تىجارەت API | ئەرەب | [providers/speechmatics/](providers/speechmatics/) (تارماق مودۇل) | [results/speechmatics/](results/speechmatics/) | |
| [SpeechYou](https://app.speechyou.com/) | تىجارەت SaaS | ئەرەب | [providers/speechyou/](providers/speechyou/) | [results/speechyou/](results/speechyou/) | تور كۆرۈنمىسى |

## سىناق نۇسخىلىرى

بارلىق نۇسخىلار [`samples/`](samples/) ھۆججەتقىسقۇچتا.

| نۇسخا | قىيىنلىق دەرىجىسى | ۋاقتى | چۈشەندۈرۈش |
|--------|---------------------|-------|-------------|
| `antal-hadi.mp3` | قىيىن | 4:03 | شىۋە ئۆزگەرتىلمىسى — ئېغىر شىۋىلىك سۆزلىگەن ئۇيغۇرچە |
| `dastan-01.mp3` | ئوتتۇرا | 2:26 | ياخشى ئاۋاز سۈپىتى، رېئال سىنارىيە، تۆۋەن تەگلىك مۇزىكا |
| `dutar-01.mp3` | قىيىن | 2:44 | تەگلىك مۇزىكا، بالا يىغلىشى، شاۋقۇنلۇق مۇھىت |
| `speedy-01.mp3` | ئوتتۇرا | 0:36 | نورمالدىن تېز سۆزلەش تېزلىكى |

## ئەسكەرتىش

يۇقىرىدىكى مەھسۇلاتلار ئۆزلىرىنىڭ رەسمىي تور بېتى ياكى ھۆججەتلىرىدە ئۇيغۇر تىلىنى قوللايدىغانلىقىنى بىلدۈرگەنلىكى ئۈچۈن تاللانغان. تاللاشتا ھېچقانداق مايىللىق ياكى تەرەپدارلىق يوق.

## ئاگاھلاندۇرۇش

بۇ ئامباردىكى ئاۋاز نۇسخىلىرى توردىن توپلانغان بولۇپ، پەقەت **تەتقىقات ۋە مائارىپ مەقسىتى** ئۈچۈن ئىشلىتىلىدۇ. ئەگەر سىز مەزكۇر نۇسخىلارنىڭ نەشر ھوقۇقى ئىگىسى بولسىڭىز ۋە ئۇنى ئۆچۈرۈۋېتىشنى خالىسىڭىز، مەسىلە (issue) ئېچىڭ.

## ئىجازەتنامە

بۇ خىزمەت [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) ئىجازەتنامىسى بىلەن تارقىتىلىدۇ.
