const fs = require("fs");
const path = require("path");
const { pathToFileURL } = require("url");
const { chromium } = require("playwright");

const projectRoot = path.resolve(__dirname, "..");
const outputPath = path.join(projectRoot, "renders", "pursuit-problem-courseware-with-narration.webm");
const chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";

async function main() {
  const browser = await chromium.launch({
    headless: true,
    executablePath: chromePath,
    args: ["--autoplay-policy=no-user-gesture-required", "--allow-file-access-from-files"],
  });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  page.on("pageerror", (error) => console.error(error.message));

  await page.goto(pathToFileURL(path.join(projectRoot, "scripts", "mux-video-audio.html")).href, {
    waitUntil: "load",
  });
  await page.waitForFunction(() => typeof window.renderMux === "function");
  const base64 = await page.evaluate(() => window.renderMux());
  fs.writeFileSync(outputPath, Buffer.from(base64, "base64"));
  await browser.close();
  console.log(outputPath);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
