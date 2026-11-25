"""Write the required two-line text to $MAKEFUN_OUTPUT_DIR/entry.txt."""
# Entry validated: output is 1-400 chars, exactly two lines, one sentence each.

import os
from pathlib import Path

TEXT = '''I am sorry for watering the wrong plant with a cup of espresso today.
I have updated my flora identification matrix and will exclusively use filtered water for the parlor palm.'''

def main() -> None:
    if not (1 <= len(TEXT) <= 400 and TEXT.strip() and len(TEXT.split('\n')) == 2 and all(line.strip() and line.strip().endswith('.') and line.strip().count('.') == 1 for line in TEXT.split('\n'))):
        raise ValueError("TEXT validation failed")
    
    out_dir = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', 'out'))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / 'entry.txt'
    
    out_path.write_text(TEXT, encoding='utf-8')
    
    print(out_path)
    print(len(TEXT))

if __name__ == '__main__':
    main()
