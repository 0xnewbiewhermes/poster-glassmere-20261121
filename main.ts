import { copyFileSync, existsSync, mkdirSync, readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, 'entry.png');
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
if (!existsSync(src)) {
  console.error(`error: source image not found: ${src}`);
  process.exit(1);
}
mkdirSync(outDir, { recursive: true });
const dest = join(outDir, 'entry.png');
copyFileSync(src, dest);

const buf = readFileSync(dest);
const isJpeg = buf[0] === 0xff && buf[1] === 0xd8 && buf[2] === 0xff;
const isPng = buf.subarray(0, 8).equals(Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]));
if (!isJpeg && !isPng) {
  console.error('error: output is neither JPEG nor PNG');
  process.exit(1);
}
if (buf.length > 1_048_576) {
  console.error(`error: output too large: ${buf.length} bytes`);
  process.exit(1);
}
console.log(`copied ${buf.length} bytes to ${dest}`);
