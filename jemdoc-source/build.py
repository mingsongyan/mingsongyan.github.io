#!/usr/bin/env python3
"""Optional: regenerate docs/*.html with a separately downloaded jemdoc program.

Back up direct HTML edits first. No generator is downloaded or run implicitly.
"""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generator', required=True, type=Path,
                        help='Path to the jemdoc file from wsshin/jemdoc_mathjax')
    parser.add_argument('--overwrite', action='store_true',
                        help='Confirm replacement of the prebuilt HTML pages')
    args = parser.parse_args()
    generator = args.generator.expanduser().resolve()
    here = Path(__file__).resolve().parent
    destination = here.parent / 'docs'
    if not generator.is_file():
        parser.error('The generator path must point to the downloaded jemdoc file.')
    if not args.overwrite:
        parser.error('Back up HTML edits, then add --overwrite to confirm regeneration.')
    pages = sorted(here.glob('*.jemdoc'))
    if not pages:
        parser.error('No .jemdoc source files were found beside this script.')
    try:
        with tempfile.TemporaryDirectory(prefix='jemdoc-build-') as staging:
            staging = Path(staging)
            for page in pages:
                subprocess.run([sys.executable, str(generator), '-c', 'site.conf',
                                '-o', str(staging / (page.stem + '.html')), page.name],
                               cwd=here, check=True)
            destination.mkdir(parents=True, exist_ok=True)
            for output in staging.glob('*.html'):
                shutil.copy2(output, destination / output.name)
            (destination / '.nojekyll').touch()
    except (OSError, subprocess.CalledProcessError) as exc:
        print('Build failed; existing pages were not replaced: ' + str(exc), file=sys.stderr)
        return 1
    print('Rebuilt pages in ' + str(destination))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
