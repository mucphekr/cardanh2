#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate random Vietnamese student names and write them onto the template image
right after the "Họ và tên:" label (beneath "Vừa làm vừa học").
- Works offline (built-in name lists) to avoid duplicates.
- You can control how many images to create with NUM_IMAGES.
- Coordinates are ratio-based so it scales with different image sizes.
- If the text is a bit off, tweak the four R_* ratios below.
- NEW: Support Gemini API for automatic name generation
"""
import random
import argparse
import json
from typing import Iterable
import re
import os
try:
    import requests  # optional, used for API fetch
except Exception:
    requests = None  # fallback to urllib if needed
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    genai = None

# ============ USER SETTINGS ============
TEMPLATE_PATH = r"C:\Users\Muc Phe\Desktop\Card Viet\template.png"
   # put your base image path here
OUTPUT_DIR = str((Path(__file__).parent / "out_names").resolve())
NAMES_LOG = str((Path(__file__).parent / "out_names" / "names_log.txt").resolve())
API_SOURCES_FILE = str((Path(__file__).parent / "api_sources.txt").resolve())
# Default to English names file inside the project folder
DEFAULT_NAMES_FILE = str((Path(__file__).parent / "students_english.txt").resolve())
NUM_IMAGES = 1                 # default number of images when no --num is given
SEED = 42                        # set None for fully random

# Position to place the student's name
# These are ratios of the image size; they should work well with the sample provided.
# If needed, nudge them a little.

# Vị trí tên sinh viên đầy đủ
FULL_NAME_X = 0.56      # left X ratio of the full name area
FULL_NAME_Y = 0.455     # top Y ratio of the full name area
FULL_NAME_W = 0.52      # width ratio of the full name area
FULL_NAME_H = 0.055     # height ratio of the full name area

# Vị trí họ sinh viên sau "Dear:"
LAST_NAME_X = 0.25      # left X ratio of the last name area (after Dear:)
LAST_NAME_Y = 0.15      # top Y ratio of the last name area
LAST_NAME_W = 0.3       # width ratio of the last name area
LAST_NAME_H = 0.04      # height ratio of the last name area

# Font config (choose a font that supports Vietnamese accents).
# On most systems, DejaVuSans or Arial Unicode MS works. Change to a local .ttf if needed.
FONT_CANDIDATES = [
    "DejaVuSans.ttf",            # Linux / Colab
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "Arial Unicode.ttf",         # Windows (if installed)
    "Arial.ttf",                 # Windows
    r"C:\\Windows\\Fonts\\arial.ttf",
    r"C:\\Windows\\Fonts\\arialuni.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",  # macOS
]

# Preferred initial font size (the script auto-shrinks to fit the box if needed)
BASE_FONT_SIZE = 54

# ============ NAME DATA ============
# Common English family names
FAMILY_NAMES = [
    "Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis",
    "Rodriguez","Martinez","Hernandez","Lopez","Gonzalez","Wilson","Anderson",
    "Thomas","Taylor","Moore","Jackson","Martin","Lee","Perez","Thompson",
    "White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson","Walker",
    "Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores",
    "Green","Adams","Nelson","Baker","Hall","Rivera","Campbell","Mitchell",
    "Carter","Roberts","Gomez","Phillips","Evans","Turner","Diaz","Parker",
    "Cruz","Edwards","Collins","Reyes","Stewart","Morris","Morales","Murphy",
    "Cook","Rogers","Gutierrez","Ortiz","Morgan","Cooper","Peterson","Bailey",
    "Reed","Kelly","Howard","Ramos","Kim","Cox","Ward","Richardson","Watson",
    "Brooks","Chavez","Wood","James","Bennett","Gray","Mendoza","Ruiz",
    "Hughes","Price","Alvarez","Castillo","Sanders","Patel","Myers","Long",
    "Ross","Foster","Jimenez","Powell","Jenkins","Perry","Russell","Sullivan",
    "Bell","Coleman","Butler","Henderson","Barnes","Gonzales","Fisher","Vasquez",
    "Simmons","Romero","Jordan","Patterson","Alexander","Hamilton","Graham",
    "Porter","Owens","Palmer","Washington","Tucker","Marshall","Woods","Cole",
    "West","Jordan","Reed","Hayes","Bryant","Dunn","Hughes","Woods","Washington"
]

# Common English middle names
MIDDLE_NAMES = [
    "James","Mary","John","Patricia","Robert","Jennifer","Michael","Linda",
    "William","Elizabeth","David","Barbara","Richard","Susan","Joseph","Jessica",
    "Thomas","Sarah","Christopher","Karen","Charles","Nancy","Daniel","Lisa",
    "Matthew","Betty","Anthony","Helen","Mark","Sandra","Donald","Donna",
    "Steven","Carol","Paul","Ruth","Andrew","Sharon","Joshua","Michelle",
    "Kenneth","Laura","Kevin","Sarah","Brian","Kimberly","George","Deborah",
    "Timothy","Dorothy","Ronald","Amy","Jason","Angela","Edward","Ashley",
    "Jeffrey","Brenda","Ryan","Emma","Jacob","Olivia","Gary","Cynthia",
    "Nicholas","Marie","Eric","Janet","Jonathan","Catherine","Stephen","Frances",
    "Larry","Christine","Justin","Samantha","Scott","Debra","Brandon","Rachel",
    "Benjamin","Carolyn","Samuel","Janet","Gregory","Virginia","Frank","Maria",
    "Raymond","Heather","Alexander","Diane","Patrick","Julie","Jack","Joyce",
    "Dennis","Victoria","Jerry","Kelly","Tyler","Christina","Aaron","Joan",
    "Jose","Evelyn","Henry","Judith","Adam","Megan","Douglas","Cheryl",
    "Nathan","Andrea","Peter","Hannah","Zachary","Jacqueline","Kyle","Martha",
    "Noah","Gloria","Alan","Teresa","Wayne","Sara","Roy","Janice",
    "Ralph","Julia","Eugene","Marie","Louis","Madison","Philip","Grace",
    "Bobby","Judy","Johnny","Theresa","Earl","Beverly","Jimmy","Denise"
]

# Common English given names
GIVEN_NAMES = [
    "Alexander","Benjamin","Christopher","Daniel","Ethan","Gabriel","Henry",
    "Isaac","Jacob","Kevin","Liam","Michael","Nathan","Oliver","Patrick",
    "Quinn","Ryan","Samuel","Thomas","Victor","William","Zachary","Aaron",
    "Brandon","Caleb","David","Elijah","Felix","George","Hunter","Ian",
    "Jack","Kyle","Luke","Matthew","Nicholas","Owen","Paul","Robert",
    "Sebastian","Tyler","Vincent","Wyatt","Adam","Blake","Carter","Dylan",
    "Evan","Finn","Grayson","Hayden","Isaac","Jaxon","Kai","Lucas",
    "Mason","Noah","Oscar","Parker","Quentin","Riley","Sawyer","Tristan",
    "Uriel","Vaughn","Wesley","Xavier","Yusuf","Zane","Amelia","Bella",
    "Charlotte","Delilah","Emma","Faith","Grace","Hannah","Isabella","Julia",
    "Katherine","Lily","Madison","Natalie","Olivia","Penelope","Quinn","Ruby",
    "Sophia","Taylor","Uma","Victoria","Willow","Ximena","Yara","Zoe",
    "Abigail","Brooklyn","Chloe","Diana","Elena","Fiona","Gabriella","Harper",
    "Iris","Jasmine","Kinsley","Luna","Maya","Nora","Ophelia","Piper",
    "Quinn","Rose","Stella","Tessa","Una","Violet","Wren","Xara",
    "Yolanda","Zara","Aria","Brielle","Cora","Daisy","Eva","Freya",
    "Gianna","Hazel","Ivy","Jade","Kira","Layla","Mia","Nova",
    "Oakley","Paisley","Quinn","Raya","Sage","Talia","Uma","Vera",
    "Willa","Xara","Yara","Zara"
]

def pick_font(size: int) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        try:
            return ImageFont.truetype(path, size=size)
        except Exception:
            continue
    # Fallback to PIL default (limited Vietnamese support)
    return ImageFont.load_default()

def load_previous_names(log_path: str) -> set[str]:
    path = Path(log_path)
    if not path.exists():
        return set()
    try:
        return set(x.strip() for x in path.read_text(encoding="utf-8").splitlines() if x.strip())
    except Exception:
        return set()

def append_names_to_log(log_path: str, names: Iterable[str]) -> None:
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        for name in names:
            f.write(f"{name}\n")

def make_unique_names(n: int) -> list[str]:
    """Create up to n unique full names."""
    seen = set()
    names = []
    attempts = 0
    while len(names) < n and attempts < n * 20:
        # English name format: First Name + Last Name
        full = f"{random.choice(GIVEN_NAMES)} {random.choice(FAMILY_NAMES)}"
        if full not in seen:
            seen.add(full)
            names.append(full)
        attempts += 1
    return names

def try_extract_full_names_from_json(payload) -> list[str]:
    # Accept formats: ["Nguyễn Văn A", ...] or [{"name": ...}] or {"data": [...]}
    candidates = []
    data = payload
    if isinstance(payload, dict):
        # common keys
        for key in ("data", "results", "items", "names"):
            if key in payload:
                data = payload[key]
                break
    if isinstance(data, list):
        for item in data:
            if isinstance(item, str):
                candidates.append(item)
            elif isinstance(item, dict):
                for key in ("full_name", "name", "fullname"):
                    if key in item and isinstance(item[key], str):
                        candidates.append(item[key])
                        break
    elif isinstance(data, dict):
        for key in ("full_name", "name", "fullname"):
            if key in data and isinstance(data[key], str):
                candidates.append(data[key])
                break
    return candidates

def fetch_names_from_api(api_url: str, count: int) -> list[str]:
    if not api_url:
        return []
    try:
        if requests is not None:
            resp = requests.get(api_url, timeout=10)
            resp.raise_for_status()
            payload = resp.json()
        else:
            req = Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
            with urlopen(req, timeout=10) as r:
                content = r.read().decode("utf-8", errors="ignore")
            try:
                payload = json.loads(content)
            except Exception:
                payload = content
        # Try JSON extraction first
        names = try_extract_full_names_from_json(payload)
        # If string content, try HTML/text extraction heuristics
        if not names and isinstance(payload, str):
            text = payload
            # Remove HTML tags quickly
            text_no_tags = re.sub(r"<[^>]+>", " ", text)
            # Vietnamese-looking full names: 2-4 capitalized tokens possibly with accents
            # Basic pattern: Capitalized word (with Vietnamese letters) separated by spaces
            word = r"[A-ZÀÁÂÃÄÅĂẠẢẤẦẨẪẬẮẰẲẴẶÈÉÊËẸẺẼẾỀỂỄỆÌÍÎÏỊỈĨÒÓÔÕÖƠỌỎỐỒỔỖỘỚỜỞỠỢÙÚÛÜƯỤỦỨỪỬỮỰỲÝỶỸỴĐ][a-zàáâãäåăạảấầẩẫậắằẳẵặèéêëẹẻẽếềểễệìíîïịỉĩòóôõöơọỏốồổỗộớờởỡợùúûüưụủứừửữựỳýỷỹỵđ]+"
            pattern = rf"\b{word}(\s+{word}){{1,3}}\b"
            candidates = re.findall(pattern, text_no_tags)
            # re.findall with groups returns only the last group unless we use finditer
            names_found = []
            for m in re.finditer(pattern, text_no_tags):
                names_found.append(m.group(0).strip())
            # Fallback: newline-based
            if not names_found:
                names_found = [x.strip() for x in text_no_tags.splitlines() if x.strip()]
            names = names_found
        # Trim and dedupe order-preserving
        seen = set()
        result = []
        for nm in names:
            nm = nm.strip()
            if nm and nm not in seen:
                seen.add(nm)
                result.append(nm)
        return result[:count]
    except (HTTPError, URLError, Exception):
        return []

def generate_names_api_only(num_needed: int, api_url: str, avoid: set[str]) -> list[str]:
    collected: list[str] = []
    api_names = fetch_names_from_api(api_url, num_needed * 5)
    for nm in api_names:
        if len(collected) >= num_needed:
            break
        if nm not in avoid and nm not in collected:
            collected.append(nm)
    return collected

def load_candidate_api_urls(sources_file: str) -> list[str]:
    urls: list[str] = []
    # Read from local file if present
    p = Path(sources_file)
    if p.exists():
        try:
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#"):
                    urls.append(line)
        except Exception:
            pass
    # Hard-coded candidates can be extended here if you have known endpoints
    # Keep this list minimal to avoid hitting unknown services unintentionally
    return urls

def try_auto_api(num_needed: int, avoid: set[str], sources_file: str) -> list[str]:
    urls = load_candidate_api_urls(sources_file)
    if not urls:
        return []
    param_variants = [
        "count", "limit", "size", "n"
    ]
    collected: list[str] = []
    for base in urls:
        candidates = [base]
        # try with common count params
        for key in param_variants:
            sep = "&" if "?" in base else "?"
            candidates.append(f"{base}{sep}{key}={num_needed*5}")
        for url in candidates:
            names = fetch_names_from_api(url, num_needed * 5)
            for nm in names:
                if len(collected) >= num_needed:
                    break
                if nm not in avoid and nm not in collected:
                    collected.append(nm)
            if len(collected) >= num_needed:
                return collected
    return collected

def fetch_names_namefake(num_needed: int, timeout_s: float = 5.0, max_attempts: int = 10) -> list[str]:
    """Fetch ~num_needed Vietnamese names from namefake API, de-duplicated."""
    url = "https://api.namefake.com/vietnamese-vietnam/random"
    got: set[str] = set()
    attempts = 0
    def fetch_once() -> str:
        if requests is not None:
            r = requests.get(url, timeout=timeout_s)
            if r.ok:
                try:
                    data = r.json()
                except Exception:
                    return ""
                return str(data.get("name", "")).strip()
            return ""
        # urllib fallback
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urlopen(req, timeout=timeout_s) as resp:
                content = resp.read().decode("utf-8", errors="ignore")
            data = json.loads(content)
            return str(data.get("name", "")).strip()
        except Exception:
            return ""

    while len(got) < num_needed and attempts < max_attempts * max(1, num_needed):
        name = fetch_once()
        if name:
            got.add(name)
        else:
            try:
                import time as _t
                _t.sleep(0.3)
            except Exception:
                pass
        attempts += 1
    return list(got)

def make_unique_names_offline(n: int, avoid: set[str]) -> list[str]:
    seen = set()
    names: list[str] = []
    attempts = 0
    while len(names) < n and attempts < n * 30:
        # English name format: First Name + Last Name
        full = f"{random.choice(GIVEN_NAMES)} {random.choice(FAMILY_NAMES)}"
        if full not in seen and full not in avoid and full not in names:
            seen.add(full)
            names.append(full)
        attempts += 1
    return names

def generate_names_with_gemini(num_needed: int, avoid: set[str], api_key: str) -> list[str]:
    """Generate English student names using Gemini API."""
    if not GEMINI_AVAILABLE:
        print("⚠️ google-generativeai not installed. Install with: pip install google-generativeai")
        return []
    
    if not api_key:
        print("⚠️ No Gemini API key provided. Use --gemini-key YOUR_KEY or set GEMINI_API_KEY env variable.")
        return []
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        
        collected_names = []
        attempts = 0
        max_attempts = num_needed * 3
        
        while len(collected_names) < num_needed and attempts < max_attempts:
            # Request more names than needed to account for duplicates
            batch_size = min(20, num_needed - len(collected_names) + 5)
            
            prompt = f"""Generate {batch_size} random English student names, diverse.
Requirements:
- Each name should be in format: First Name + Last Name (e.g., John Smith)
- Use common English first names like: John, Michael, David, Sarah, Jessica, Emily, etc.
- Use common English last names like: Smith, Johnson, Williams, Brown, Jones, etc.
- Each name on one line
- No numbering, no explanations, just list the names

Example format:
John Smith
Sarah Johnson
Michael Brown
Emily Davis"""

            response = model.generate_content(prompt)
            
            if response and response.text:
                # Parse names from response
                lines = response.text.strip().split('\n')
                for line in lines:
                    # Clean up the line
                    name = line.strip()
                    # Remove numbering if present (1. Name, 1) Name, etc.)
                    name = re.sub(r'^\d+[\.\)]\s*', '', name)
                    # Remove bullet points
                    name = re.sub(r'^[-*•]\s*', '', name)
                    name = name.strip()
                    
                    # Validate name format (should have 2 words)
                    if name and len(name.split()) == 2:
                        if name not in avoid and name not in collected_names:
                            collected_names.append(name)
                            if len(collected_names) >= num_needed:
                                break
            
            attempts += 1
        
        print(f"✅ Gemini API generated {len(collected_names)}/{num_needed} unique names")
        return collected_names[:num_needed]
        
    except Exception as e:
        print(f"❌ Error with Gemini API: {e}")
        return []

def load_names_from_file(path: str) -> list[str]:
    try:
        content = Path(path).read_text(encoding="utf-8")
    except Exception:
        return []
    lines = [ln.strip() for ln in content.splitlines() if ln.strip()]
    # normalize whitespace
    names = [re.sub(r"\s+", " ", ln) for ln in lines]
    # preserve order while deduping
    seen = set()
    out: list[str] = []
    for nm in names:
        if nm not in seen:
            seen.add(nm)
            out.append(nm)
    return out

def sanitize_filename(name: str) -> str:
    # Replace characters not safe for Windows filenames
    safe = "".join(c for c in name if c not in "\\/:*?\"<>|\n\r\t")
    safe = safe.strip()
    # Fallback if empty after sanitization
    return safe or "student"

def autowrap_and_fit(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, box_w: int, box_h: int):
    """Shrink font until text height fits; no multi-line needed for short names."""
    size = font.size
    while size > 12:
        f = pick_font(size)
        bbox = draw.textbbox((0, 0), text, font=f)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        if tw <= box_w and th <= box_h:
            return f
        size -= 2
    return pick_font(12)

def place_name_on_image(template_path: str, out_path: str, name_text: str):
    im = Image.open(template_path).convert("RGBA")
    W, H = im.size

    # Draw
    draw = ImageDraw.Draw(im)

    # Tách tên và họ
    name_parts = name_text.strip().split(' ')
    last_name = name_parts[-1] if name_parts else name_text
    first_name = ' '.join(name_parts[:-1]) if len(name_parts) > 1 else name_text  # Tất cả từ trước từ cuối cùng
    full_name = name_text

    # Vẽ tên đầy đủ
    full_name_box_x = int(W * FULL_NAME_X)
    full_name_box_y = int(H * FULL_NAME_Y)
    full_name_box_w = int(W * FULL_NAME_W)
    full_name_box_h = int(H * FULL_NAME_H)

    # Prepare font that fits for full name
    full_name_font = autowrap_and_fit(draw, full_name, pick_font(BASE_FONT_SIZE), full_name_box_w, full_name_box_h)

    # Left align, vertically centered within the box for full name
    full_name_bbox = draw.textbbox((0,0), full_name, font=full_name_font)
    full_name_h = full_name_bbox[3] - full_name_bbox[1]
    full_name_y = full_name_box_y + (full_name_box_h - full_name_h)//2
    full_name_x = full_name_box_x + 10  # small left padding

    # Draw full name with white stroke
    draw.text((full_name_x, full_name_y), full_name, font=full_name_font, fill=(0,0,0), stroke_width=2, stroke_fill=(255,255,255))

    # Vẽ chỉ tên (First Name) sau "Dear:"
    dear_name_box_x = int(W * LAST_NAME_X)
    dear_name_box_y = int(H * LAST_NAME_Y)
    dear_name_box_w = int(W * LAST_NAME_W)
    dear_name_box_h = int(H * LAST_NAME_H)

    # Prepare font that fits for dear name (smaller font)
    dear_name_font_size = max(12, BASE_FONT_SIZE - 10)
    dear_name_font = autowrap_and_fit(draw, first_name, pick_font(dear_name_font_size), dear_name_box_w, dear_name_box_h)

    # Left align, vertically centered within the box for dear name
    dear_name_bbox = draw.textbbox((0,0), first_name, font=dear_name_font)
    dear_name_h = dear_name_bbox[3] - dear_name_bbox[1]
    dear_name_y = dear_name_box_y + (dear_name_box_h - dear_name_h)//2
    dear_name_x = dear_name_box_x + 10  # small left padding

    # Draw first name after "Dear:" with white stroke
    draw.text((dear_name_x, dear_name_y), first_name, font=dear_name_font, fill=(0,0,0), stroke_width=2, stroke_fill=(255,255,255))

    im.save(out_path)

def main():
    parser = argparse.ArgumentParser(description="Generate Vietnamese student ID photos with names")
    parser.add_argument("--num", type=int, default=None, help="Number of images to generate")
    parser.add_argument("--api-url", type=str, default="", help="API endpoint that returns Vietnamese names (required unless --auto-api or --namefake)")
    parser.add_argument("--auto-api", action="store_true", help="Automatically try candidate API endpoints from api_sources.txt")
    parser.add_argument("--namefake", action="store_true", help="Use namefake.com Vietnamese API as the online source")
    parser.add_argument("--gemini", action="store_true", help="Use Gemini API to generate names automatically")
    parser.add_argument("--gemini-key", type=str, default="", help="Gemini API key (or set GEMINI_API_KEY env variable)")
    parser.add_argument("--pad-local", action="store_true", help="If online source returns insufficient names, pad with offline names to reach --num")
    parser.add_argument("--template", type=str, default=TEMPLATE_PATH, help="Path to template image")
    parser.add_argument("--out", type=str, default=OUTPUT_DIR, help="Output directory for generated images")
    parser.add_argument("--seed", type=int, default=SEED if SEED is not None else None, help="Random seed")
    parser.add_argument("--names-file", type=str, default="", help="Path to a local file with one full name per line (preferred over API)")
    args = parser.parse_args()

    num_images = args.num if args.num is not None else NUM_IMAGES
    template_path = args.template
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.seed is not None:
        random.seed(args.seed)

    previous = load_previous_names(NAMES_LOG)
    names: list[str]
    
    # Priority 1: Use Gemini API if specified
    if args.gemini:
        gemini_key = args.gemini_key or os.environ.get('GEMINI_API_KEY', '')
        print(f"🤖 Using Gemini API to generate {num_images} Vietnamese student names...")
        names = generate_names_with_gemini(num_images, previous, gemini_key)
        if len(names) < num_images:
            if args.pad_local:
                need = num_images - len(names)
                print(f"📝 Padding with {need} offline-generated names...")
                names += make_unique_names_offline(need, set(previous).union(names))
            else:
                raise SystemExit(f"Gemini API did not return enough unique names ({len(names)}/{num_images}). Use --pad-local to fill remaining.")
    # Priority 2: Use names file if exists
    elif args.names_file or Path(DEFAULT_NAMES_FILE).exists():
        chosen_path = args.names_file or DEFAULT_NAMES_FILE
        file_names = load_names_from_file(chosen_path)
        # filter against previous
        filtered = [nm for nm in file_names if nm not in previous]
        # randomize to diversify picks
        random.shuffle(filtered)
        names = filtered[:num_images]
        if len(names) < num_images:
            # pad from remaining in file (including previously used if necessary?)
            # keep strict: do not reuse previous across runs
            pass
        if len(names) < num_images:
            if args.pad_local:
                need = num_images - len(names)
                names += make_unique_names_offline(need, set(previous).union(names))
            else:
                raise SystemExit(f"Names file did not provide enough unique names ({len(names)}/{num_images}).")
    elif args.api_url:
        names = generate_names_api_only(num_images, args.api_url, previous)
        if len(names) < num_images:
            if args.pad_local:
                need = num_images - len(names)
                names += make_unique_names_offline(need, set(previous).union(names))
            else:
                raise SystemExit(f"API did not return enough unique names ({len(names)}/{num_images}).")
    elif args.auto_api:
        names = try_auto_api(num_images, previous, API_SOURCES_FILE)
        if len(names) < num_images:
            if args.pad_local:
                need = num_images - len(names)
                names += make_unique_names_offline(need, set(previous).union(names))
            else:
                raise SystemExit(f"Auto-API did not return enough unique names ({len(names)}/{num_images}).")
    elif args.namefake:
        names = [nm for nm in fetch_names_namefake(num_images * 2) if nm not in previous]
        names = names[:num_images]
        if len(names) < num_images:
            if args.pad_local:
                need = num_images - len(names)
                names += make_unique_names_offline(need, set(previous).union(names))
            else:
                raise SystemExit(f"Namefake did not return enough unique names ({len(names)}/{num_images}).")
    # Default: Use offline generation
    else:
        print(f"📝 Using offline name generation (no API or file specified)...")
        names = make_unique_names_offline(num_images, previous)

    used_filenames = set()
    for i, full_name in enumerate(names, start=1):
        base = sanitize_filename(full_name)
        candidate = base
        suffix = 1
        while candidate.lower() in used_filenames or (out_dir / f"{candidate}.png").exists():
            suffix += 1
            candidate = f"{base}_{suffix}"
        used_filenames.add(candidate.lower())
        out_file = out_dir / f"{candidate}.png"
        place_name_on_image(template_path, str(out_file), full_name)
        print(f"[OK] {out_file} -> {full_name}")

    append_names_to_log(NAMES_LOG, names)

if __name__ == "__main__":
    main()
