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

## Figures

### Figure 1. 
Hate Segment Length and Proportion Distributions

![Hate Segment Length and Proportion Distributions](Images/HateSegment_clear.png)

> The distributions of hate segment lengths (in seconds) and proportions (%) in videos for each platform and hate type (explicit, implicit), with x- and y-axes in log scale and mean values marked by vertical dashed lines.

---

### Figure 2. Normalized Starting Time Distribution of Hate Segments

![Normalized Starting Time Distribution of Hate Segments](Images/HateStartingTime_clear.png)

> The density-normalized starting times of hate segments by platform and video length, comparing explicit and implicit types.

---

### Figure 3. Modality Composition of Explicit and Implicit Hate

![Modality Composition of Explicit and Implicit Hate](Images/HateModality_clear.png)

> The modality composition for explicit and implicit hate in the dataset.

---

### Figure 4. Proportion of Hateful Videos by Target Group

![Proportion of Hateful Videos by Target Group](Images/HateTargetGroup_clear.png)

> The proportion of hateful videos by targeted group, separated into explicit and implicit hate.

---

### Figure 5. Audio Zero Crossing Rate and Emotion

#### (a) Zero Crossing Rate (ZCR) for Explicit, Implicit, and Non-Hate Content

![Zero Crossing Rate for Explicit Hate](Images/cross_rate_explicit.jpg)
![Zero Crossing Rate for Implicit Hate](Images/cross_rate_implicit.jpg)
![Zero Crossing Rate for Non-Hate](Images/cross_rate_non-hate.jpg)

> The Zero Crossing Rate (ZCR) of the audio signal over time for explicit hate, implicit hate, and non-hate content, respectively.

---

#### (b) Audio Emotion Heatmap

![Audio Emotion Heatmap](Images/emotion_audio_heatmap.jpg)

> The distribution of detected emotions in the audio across different content types, with columns representing emotions and rows representing explicit, implicit, and non-hate categories.

---

### Figure 7. Object Detection and Word Cloud for Explicit and Implicit Hate Content

![Object Detection and Word Cloud](Images/HateObjectDetection_clear.jpg)

> The detected object categories (word clouds) and example video frames with object detection results for explicit hate (left) and implicit hate (right) content.

---

### Figure 6. Sentiment Scores and Top Keywords in Textual Content

![Sentiment Scores and Top Keywords](Images/sentiment_box_and_table.jpg)

> The sentiment scores of textual content across explicit hate, implicit hate, and non-hate categories for BitChute and TikTok (left). The top 10 keywords for each category: explicit, implicit, non-Hate (right).

---

## File List

- `DeHate.xlsx` — Main data file with video-level and segment-level annotations.

---

## Citation

If you use this dataset, please cite:

```bibtex
@inproceedings{DeHATE2025,
  author    = {Yuchen Zhang and Tailin Chen and Jiangbei Yue and Yueming Sun and Rahul Singh and Jianbo Jiao and Zeyu Fu},
  title     = {DeHATE: A Holistic Hateful Video Dataset for Explicit and Implicit Hate Detection and Localization},
  year      = {2025}
}
