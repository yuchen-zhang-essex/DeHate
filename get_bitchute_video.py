#!/usr/bin/env python3
"""
BitChute Video Downloader
-------------------------

Downloads videos from BitChute using their video IDs.

Usage:
    python bitchute_downloader.py --video_id abc123
    python bitchute_downloader.py --video_id abc123 --output_dir videos/
"""

import argparse
import re
import pathlib
import urllib.request
from lxml import html
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def get_tree(url):
    """Fetch and parse HTML tree from a BitChute video page."""
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        )
    }
    req = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(req).read()
    return html.document_fromstring(page)


def extract_video_info(video_id):
    """Extract video source URL and metadata from a BitChute video ID."""
    url = f"https://www.bitchute.com/video/{video_id}/"
    logging.info(f"Fetching metadata from: {url}")
    tree = get_tree(url)

    # Get video URL
    source_elem = tree.xpath('//*[@id="player"]/source')
    if not source_elem:
        raise ValueError("Could not find video source on the page.")
    video_url = source_elem[0].get('src')

    # Get title
    title_elem = tree.xpath('//*[@id="video-title"]')
    title = title_elem[0].text_content().strip() if title_elem else f"video_{video_id}"
    title_clean = re.sub(r"[^\w\-_. ]", "", title).replace(" ", "_")

    # Get publisher
    publisher_elem = tree.xpath(
        '//*[@id="video-watch"]/div/div[1]/div[3]/div/div[2]/div[3]/p[1]/a'
    )
    publisher = publisher_elem[0].text_content().strip() if publisher_elem else "unknown"

    # Get date
    date_elem = tree.xpath('//*[@id="video-watch"]/div/div[1]/div[3]/div/div[1]')
    if date_elem:
        date_text = date_elem[0].text_content()
        date_stripped = date_text[20:-10] + date_text[-8:-2]
        date = datetime.strptime(date_stripped, "%H:%M %Z on %B %d, %Y").strftime("%Y%m%d")
    else:
        date = "unknown_date"

    # Get file extension
    ext = pathlib.Path(video_url).suffix or ".mp4"

    # Construct filename
    filename = f"{publisher}_{date}_{title_clean}{ext}"
    return video_url, filename


def download_video(video_url, filename, output_dir="bitchute"):
    """Download the video to the specified directory."""
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
    filepath = pathlib.Path(output_dir) / filename

    if filepath.exists():
        logging.warning(f"File already exists: {filepath}")
        return str(filepath)

    logging.info(f"Downloading to: {filepath}")
    urllib.request.urlretrieve(video_url, filepath)
    logging.info("Download complete.")
    return str(filepath)


def main(video_id, output_dir):
    try:
        video_url, filename = extract_video_info(video_id)
        path = download_video(video_url, filename, output_dir)
        logging.info(f"Saved: {path}")
    except Exception as e:
        logging.error(f"Failed to download video {video_id}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download BitChute video by ID.")
    parser.add_argument("--video_id", type=str, required=True, help="BitChute video ID")
    parser.add_argument("--output_dir", type=str, default="bitchute", help="Output directory")

    args = parser.parse_args()
    main(args.video_id, args.output_dir)
