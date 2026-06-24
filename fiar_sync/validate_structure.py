import os
import sys
import json

with open(os.path.join(os.path.dirname(__file__), "fiar_structure.json")) as f:
    CONFIG = json.load(f)

BASE_DIR = "artefatos_projeto"


def check_required_files():
    missing = {}

    for key, value in CONFIG.items():
        if key in ["legacy", "version"]:
            continue

        if isinstance(value, dict) and "required_files" in value:
            base_path = os.path.join(BASE_DIR, value["path"])

            for file in value["required_files"]:
                path = os.path.join(base_path, file)
                if not os.path.exists(path):
                    missing.setdefault(base_path, []).append(file)

    return missing


def check_operational():
    missing_dirs = []

    ops = CONFIG["operational_artifacts"]
    base = os.path.join(BASE_DIR, ops["path"])

    if not os.path.exists(base):
        missing_dirs.append(base)
    else:
        for d in ops["subdirs"]:
            path = os.path.join(base, d)
            if not os.path.exists(path):
                missing_dirs.append(path)

    return missing_dirs


def main():
    print("🔎 FIAR VALIDATION START\n")

    missing = check_required_files()
    legacy = check_operational()

    if missing:
        print("❌ Missing files:")
        for folder, files in missing.items():
            for f in files:
                print(f"  - {folder}/{f}")

    if legacy:
        print("\n❌ Missing operational structure:")
        for d in legacy:
            print(f"  - {d}")

    if missing or legacy:
        print("\n🚨 FIAR VALIDATION FAILED")
        sys.exit(1)

    print("\n✅ FIAR VALIDATION PASSED")
    sys.exit(0)


if __name__ == "__main__":
    main()