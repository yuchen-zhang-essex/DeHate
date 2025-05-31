# DeHATE: A Holistic Hateful Video Dataset

## Ethics Statement

The videos and data provided for annotation in this project have been sourced from publicly accessible social media platforms in compliance with all applicable laws and regulations. The content within these videos does not reflect the opinions, beliefs, or viewpoints of the research group or its members.

This dataset is intended solely for research purposes and must be treated with strict confidentiality. Annotators are prohibited from downloading, saving, or disseminating any part of the data in any form. Any breach of this policy will be considered a violation of project terms and may result in legal consequences. No personally identifiable information is included, and all procedures align with relevant legal and ethical standards.

---

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

**Table 1: Label distribution of DeHATE.**

| Platform  | Hate (Explicit) | Hate (Implicit) | Non-Hate |
|-----------|:--------------:|:---------------:|:--------:|
| BitChute  | 1055           | 835             | 3162     |
| TikTok    | 115            | 115             | 1407     |
| **Total** | 1170           | 950             | 4569     |

---

### Modality Distribution

**Table 2: Distribution of contributing modalities (Top 3 in bold).**

| Modality                   | BitChute | TikTok |
|----------------------------|:--------:|:------:|
| **Text only**              | 951      | 23     |
| Visual only                | 9        | 15     |
| Audio only                 | 207      | 66     |
| Visual + Audio             | 257      | 92     |
| Visual + Text              | 26       | 2      |
| Text + Audio               | 82       | 3      |
| **Visual + Audio + Text**  | 358      | 29     |

---

### Target Group Distribution

**Table 3: Distribution of hateful videos by single and multiple target groups (Top 3 single targets in bold).**

| Target Group(s)                | BitChute | TikTok |
|--------------------------------|:--------:|:------:|
| **Single Target Group**        |          |        |
| **Race**                       | 573      | 71     |
| **Gender**                     | 289      | 16     |
| Religion                       | 71       | 28     |
| Sexual Orientation             | 203      | 19     |
| Disability                     | 23       | 31     |
| Immigration                    | 318      | 33     |
| **Top 5 Multiple Target Groups**|         |        |
| Race + Immigration             | 134      | 14     |
| Race + Religion                | 61       | 6      |
| Race + Gender                  | 59       | 2      |
| Gender + Sexual Orientation    | 46       | 4      |
| Race + Sexual Orientation      | 38       | –      |
| Race + Religion + Immigration  | –        | 2      |

---

## Figures

### Figure 1. Hate Segment Length and Proportion Distributions

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

### Figure 6. Sentiment Scores and Top Keywords in Textual Content

![Sentiment Scores and Top Keywords](Images/sentiment_box_and_table.jpg)

> The sentiment scores of textual content across explicit hate, implicit hate, and non-hate categories for BitChute and TikTok (left). The top 10 keywords for each category: explicit, implicit, non-Hate (right).

---

### Figure 7. Object Detection and Word Cloud for Explicit and Implicit Hate Content

![Object Detection and Word Cloud](Images/HateObjectDetection_clear.jpg)

> The detected object categories (word clouds) and example video frames with object detection results for explicit hate (left) and implicit hate (right) content.

---

## File List

- `DeHate.xlsx` — Main data file with video-level and segment-level annotations.

---

## Accessing Videos

For the public version of the DeHATE dataset, we provide only the video IDs, which can be used to identify and retrieve the videos from TikTok and BitChute. You may use a script such as `video_download.py` to download the videos using these IDs, subject to platform availability and access permissions. Please note that some high-risk or policy-violating videos may have been removed from the platforms since collection. Due to copyright and platform restrictions, we are unable to release the raw video files directly. If you encounter video IDs that are no longer downloadable or require assistance with access, please contact [yuchen.zhang@essex.ac.uk](mailto:yuchen.zhang@essex.ac.uk) for support.









