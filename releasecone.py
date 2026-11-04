import argparse
import json
import sys
from pathlib import Path

def analyze(data):
    seen = set()
    stack = list(data['targets'])
    while stack:
        n = stack.pop()
        if n not in seen:
            seen.add(n)
            stack.extend(data['graph'].get(n, []))
    return sorted(seen)

def main():
    parser = argparse.ArgumentParser(description='Birden fazla dağıtım hedefi için gereken bileşen kümesini çıkarır.')
    parser.add_argument('file', nargs='?', help='UTF-8 JSON input file (default: stdin)')
    args = parser.parse_args()
    try:
        raw = Path(args.file).read_text(encoding='utf-8-sig') if args.file else sys.stdin.read()
        result = analyze(json.loads(raw))
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    except (SyntaxError, ValueError, KeyError, TypeError, OSError, IndexError, ArithmeticError) as error:
        parser.exit(2, f'Invalid input: {error}\n')
if __name__ == '__main__':
    main()
