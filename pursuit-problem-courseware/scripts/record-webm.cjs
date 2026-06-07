const fs = require("fs");
const path = require("path");
const { pathToFileURL } = require("url");
const { chromium } = require("playwright");

const projectRoot = path.resolve(__dirname, "..");
const renderDir = path.join(projectRoot, "renders");
const outputPath = path.join(renderDir, "pursuit-problem-courseware.webm");
const chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";

async function main() {
  fs.mkdirSync(renderDir, { recursive: true });
  if (fs.existsSync(outputPath)) {
    fs.unlinkSync(outputPath);
  }

  const browser = await chromium.launch({
    headless: true,
    executablePath: chromePath,
    args: ["--autoplay-policy=no-user-gesture-required"],
  });

  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    recordVideo: {
      dir: renderDir,
      size: { width: 1920, height: 1080 },
    },
  });

  const page = await context.newPage();
  page.on("console", (message) => {
    console.log(`console.${message.type()}: ${message.text()}`);
  });
  page.on("pageerror", (error) => {
    console.error(`pageerror: ${error.message}`);
  });
  const sourceUrl = `${pathToFileURL(path.join(projectRoot, "index.html")).href}?autoplay=1`;
  await page.goto(sourceUrl, { waitUntil: "networkidle" });
  await page.waitForFunction(() => Boolean(window.__timelines && window.__timelines.main), null, {
    timeout: 10000,
  });
  await page.waitForTimeout(73000);

  const video = page.video();
  await context.close();
  await browser.close();

  const recordedPath = await video.path();
  fs.renameSync(recordedPath, outputPath);
  console.log(outputPath);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
