# Breton ASR open data

This repository contains open data indended for Natural Language Processing research and applications. The sharing of this data has been authorized by their respective authors, with a preference for permissive licenses whenever possible.

Should you be the owner of any of the data and wish for its removal from this dataset and/or Anaouder's training data, kindly notify me.

If you are interested in contributing to this dataset by providing your own data to improve breton open speech-to-text technologies, feel free to get in touch !

## :microphone: Voices with transcriptions « Mouezhioù »

Each sub-directory contains segmented audio files, and the corresponding segment text is available in the `audio_text/metadata.tsv` file.

The transcription may contain special tokens, such as `<C'HOARZH>`, `<PASAAT>`, `<SONEREZH>`...

### Using with 🤗 HuggingFace

While this dataset isn't available on HuggingFace yet, it follows HuggingFace's audio Dataset structure. After cloning this repository locally, you can easily import the data with :

```python
from datasets import load_dataset

roadennou = load_dataset("audiofolder", data_dir="roadennou/audio_text")

# Rename column names to match MCV's
roadennou = roadennou_ouzhpenn.rename_column("transcript", "sentence")
```

### Data directories

Total audio duration : **5h 34mn 7s**

| Directory | Type | Source | Author(s) | Licence | Duration |
| ---- | ---- | ---- | ---- | ---- | ---- |
| [An_Drouizig](audio_text/An_Drouizig) | Dialog, Presentation | www.youtube.com/watch?v=A-VlNvJ3alI | Pêr Morvan, Gwenn Meynier | [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) | 27mn 26s |
| [Becedia_Komzoù-brezhoneg](audio_text/Becedia_Komzoù-brezhoneg) | Interviews | www.bcd.bzh/becedia/fr/catherine-quiniou-tine-plounevez-du-faou<br>www.bcd.bzh/becedia/fr/suzanne-goarnisson-scrignac | Lors Jouin, Francis Favereau | [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) | 9mn 17s |
| [Brendan-Budok_Durand-Le-Ludec](audio_text/Brendan-Budok_Durand-Le-Ludec) | Chess Youtube channel | www.youtube.com/watch?v=5K0nWjc7XZ4 | Bredan-Budok Durand-Le Ludec, Manon Jouitteau, YF Le Gall, Mélanie Jouitteau | [CC BY](https://creativecommons.org/licenses/by/4.0/) | 5mn 30s |
| [Neus_Ket_Deus_Archoazh](audio_text/Neus_Ket_Deus_Archoazh) | Documentary | www.youtube.com/watch?v=ixAnomWd1YU | Laors Skavenneg, Korin ar Mero | [CC BY](https://creativecommons.org/licenses/by/4.0/) | 26mn 5s |
| [#Brezhoneg](audio_text/Kelaouenn_Brezhoneg) | Read out articles | https://www.youtube.com/channel/UCv8UTrUchQafFAl2QPc2lEA | Skol an Emzav, Dizale | All rights reserved | 4h 25mn 49s |
