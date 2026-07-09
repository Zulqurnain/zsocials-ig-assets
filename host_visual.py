#!/usr/bin/env python3
"""Host a generated visual on the public zsocials-ig-assets repo and emit its URL.

Usage:
    host_visual.py <local_image_path> <brand> [visual_brief_id]

brand: 'nirmal-shah' | 'zj-the-nomad' (slug)
Commits + pushes to the repo and prints the public raw URL.

Requires the repo to be checked out at REPO_DIR and `gh` authed as Zulqurnain.
"""
import os, sys, subprocess

GH_USER = "Zulqurnain"
REPO = "zsocials-ig-assets"
BRANCH = "main"
REPO_DIR = os.path.dirname(os.path.abspath(__file__))

SLUG = {"nirmal-shah": "nirmal-shah", "zj-the-nomad": "zj-the-nomad"}

def main():
    if len(sys.argv) < 3:
        print("usage: host_visual.py <image> <brand-slug> [brief_id]", file=sys.stderr)
        sys.exit(2)
    src, brand = sys.argv[1], sys.argv[2]
    if brand not in SLUG:
        print(f"unknown brand slug {brand!r}", file=sys.stderr); sys.exit(2)
    if not os.path.exists(src):
        print(f"missing {src}", file=sys.stderr); sys.exit(2)
    dest_dir = os.path.join(REPO_DIR, brand)
    os.makedirs(dest_dir, exist_ok=True)
    base = os.path.basename(src)
    dest = os.path.join(dest_dir, base)
    if os.path.abspath(src) != os.path.abspath(dest):
        import shutil; shutil.copy2(src, dest)
    subprocess.run(["git","-C",REPO_DIR,"add","-A"], check=True)
    subprocess.run(["git","-C",REPO_DIR,"commit","-q","-m",f"host {brand}/{base}"], check=True)
    subprocess.run(["git","-C",REPO_DIR,"push","origin",BRANCH], check=True)
    url = f"https://raw.githubusercontent.com/{GH_USER}/{REPO}/{BRANCH}/{brand}/{base}"
    print(url)

if __name__ == "__main__":
    main()
