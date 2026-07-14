#!/usr/bin/env python3
"""Replace heavy Lottie/SVG assets for disabled SimpleTG features with minimal stubs."""
import os
import shutil

ROOT = os.path.join(os.path.dirname(__file__), "..", "TMessagesProj", "src", "main", "res", "raw")
STUB_LOTTIE = os.path.join(ROOT, "import_check.json")  # ~1.7 KB valid RLottie
STUB_SVG = os.path.join(os.path.dirname(__file__), "minimal.svg")

JSON_PREFIXES = (
    "star_reaction_effect", "star_reaction", "stars_", "emoji_stars", "star_fill", "star_loader",
    "star_premium", "phone_stars", "phone_dots",
    "premium_gift", "premium_",  # json only; svg handled separately
    "gift", "giveaway", "wallet_", "boosts", "boost",
    "stories_intro", "msg_story", "msg_stories", "story_bomb", "story_",
    "utyan_", "biz_", "custom_emoji_reaction",
    "fire_on", "fire_off", "fire_once",
    "channel_create", "utyan_streaming",
)

JSON_EXACT = {
    "write_contacts_fab_icon",  # unreferenced; replace then delete from build via shrink
}

SVG_PREFIXES = (
    "premium_object_", "filled_crown", "filled_messages_paid", "filled_premium",
)

SVG_EXACT = {
    "default_pattern",  # 495 KB wallpaper pattern; e-ink uses solid white
}

MINIMAL_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"/>\n'


def should_slim_json(name: str) -> bool:
    if name in JSON_EXACT:
        return True
    return any(name.startswith(p) for p in JSON_PREFIXES)


def should_slim_svg(name: str) -> bool:
    if name in SVG_EXACT:
        return True
    return any(name.startswith(p) for p in SVG_PREFIXES)


def main():
    if not os.path.isfile(STUB_LOTTIE):
        raise SystemExit(f"Missing stub lottie: {STUB_LOTTIE}")

    os.makedirs(os.path.dirname(STUB_SVG), exist_ok=True)
    with open(STUB_SVG, "w", encoding="utf-8") as f:
        f.write(MINIMAL_SVG)

    saved = 0
    count = 0
    for fname in os.listdir(ROOT):
        path = os.path.join(ROOT, fname)
        if not os.path.isfile(path):
            continue
        base, ext = os.path.splitext(fname)
        old_size = os.path.getsize(path)
        if ext == ".json" and should_slim_json(base):
            shutil.copy2(STUB_LOTTIE, path)
            saved += old_size - os.path.getsize(path)
            count += 1
        elif ext == ".svg" and should_slim_svg(base):
            with open(path, "w", encoding="utf-8") as f:
                f.write(MINIMAL_SVG)
            saved += old_size - os.path.getsize(path)
            count += 1

    print(f"Slimmed {count} assets, saved {saved / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    main()
