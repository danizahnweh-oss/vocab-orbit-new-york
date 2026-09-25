"""Build the self-contained, offline-capable game without dependencies."""
import json
from pathlib import Path
root = Path(__file__).resolve().parent
words = [dict(zip(('topic', 'en', 'de', 'sentence'), row.split('\t')))
         for row in (root / 'vocabulary.tsv').read_text().splitlines()]
assert len(words) == 86
assert len({word['en'] for word in words}) == len(words)
assert all(word['sentence'].count('___') == 1 for word in words)
(root / 'index.html').write_text((root / 'index.template.html').read_text().replace(
    '__VOCAB__', json.dumps(words, ensure_ascii=False)))
