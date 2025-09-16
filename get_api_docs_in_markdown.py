#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import logging
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

INDEX_URL = "https://developerdocs.instructure.com/services/canvas/resources.md"
BASE_URL = "https://developerdocs.instructure.com/services/canvas/"
OUT_DIR = Path(__file__).parent / "canvas_api_resources"
TIMEOUT = 10


def fetch_text(url: str) -> str:
    resp = requests.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.text


def extract_md_links(md: str, base_url: str) -> dict[str, str]:
    md_links = re.findall(r"\[[^\]]+]\(([^)]+\.md)\)", md)
    soup = BeautifulSoup(md, "html.parser")
    md_links.extend(
        a["href"] for a in soup.find_all("a", href=True) if a["href"].endswith(".md")
    )
    link_map = {}
    for href in set(md_links):
        abs_url = urljoin(base_url, href)
        filename = Path(urlparse(abs_url).path).name
        link_map[filename] = abs_url
    return link_map


def identical(local_file: Path, new_bytes: bytes) -> bool:
    if not local_file.exists():
        return False
    return (
        hashlib.sha256(local_file.read_bytes()).digest()
        == hashlib.sha256(new_bytes).digest()
    )


def download_resources(link_map: dict[str, str], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for fname, url in sorted(link_map.items()):
        dest = out_dir / fname
        logging.info("Downloading %s -> %s", url, dest)
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        if identical(dest, resp.content):
            logging.debug("Unchanged: %s", fname)
            continue
        dest.write_bytes(resp.content)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logging.info("Fetching index: %s", INDEX_URL)
    index_md = fetch_text(INDEX_URL)
    links = extract_md_links(index_md, BASE_URL)
    logging.info("Found %d markdown resources", len(links))
    download_resources(links, OUT_DIR)
    logging.info("Done. Files stored in %s", OUT_DIR.resolve())


if __name__ == "__main__":
    main()
