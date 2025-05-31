# DeHATE: A Holistic Hateful Video Dataset

**DeHATE** is a large-scale multimodal dataset for the detection and localization of explicit and implicit hate in short-form videos. The dataset comprises over 6,000 annotated videos collected from TikTok and BitChute, spanning six social groups, with fine-grained segment-level labels.

This repository contains:
- The cleaned annotation data in `.csv` format
- Documentation and statistics on label distributions, segment, modality, and group breakdowns

---

## Dataset Summary

DeHATE includes:
- Videos from two platforms: TikTok (highly regulated) and BitChute (loosely moderated)
- Annotation of both explicit and implicit hate
- Segment-level localization (timestamps for hateful content)
- Modality labels (text, audio, visual)
- Six target groups: Race, Gender, Religion, Sexual Orientation, Disability, Immigration

---

## Data Statistics

### Label Distribution

**Table 2: Label distribution of DeHATE.**

| Platform  | Hate (Explicit) | Hate (Implicit) | Non-Hate |
|-----------|:--------------:|:---------------:|:--------:|
| BitChute  | 1055           | 835             | 3162     |
| TikTok    | 115            | 115             | 1407     |
| **Total** | 1170           | 950             | 4569     |

---

### Figures

#### Figure 1: Dataset statistics and temporal analysis of hate speech segments in DeHATE

> The left histograms show the distributions of hate segment lengths (sec) and proportions (%) in videos for each platform and hate type (explicit, implicit), with x- and y-axes in log scale and mean values marked by vertical dashed lines. The middle histograms illustrate density-normalized starting times of hate segments by platform and video length, comparing explicit and implicit types. The right donut charts summarize the modality composition for explicit and implicit hate, and the bar chart shows the proportion of hateful videos by targeted group.

#### Figure 2: Audio Zero Crossing Rate and Emotion

> This figure visualizes the Zero Crossing Rate (ZCR) and the detected emotions from the audio input in the dataset.

#### Figure 3: Keywords and sentiment analysis for textual content

> This figure presents sentiment scores and the top 10 keywords for explicit hate, implicit hate, and non-hate content across platforms.

#### Figure 4: Object detection and word cloud for explicit and implicit hate content

> This figure displays the results of object detection (using YOLOv11) and word clouds for explicit and implicit hate content in the dataset.

---

## File List

- `Data_Final_clean_with_duration.csv` — Main data file with video-level and segment-level annotations.

---

## Citation

If you use this dataset, please cite:

```bibtex
@inproceedings{DeHATE2025,
  author    = {Yuchen Zhang and Tailin Chen and Jiangbei Yue and Yueming Sun and Rahul Singh and Jianbo Jiao and Zeyu Fu},
  title     = {DeHATE: A Holistic Hateful Video Dataset for Explicit and Implicit Hate Detection and Localization},
  year      = {2025}
}
