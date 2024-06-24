import { test, expect } from "@playwright/test";

test("reproduce un video en una página de anime", async ({ page }) => {
  // Navega a la página web del anime
  await page.goto("https://animenix.com/ver/spyxfamily-1x1/");

  // Espera a que el botón de reproducción esté presente
  const playButton = await page.waitForSelector(".jw-svg-icon-play");
  expect(playButton).not.toBeNull();

  // Haz clic en el botón de reproducción
  await playButton.click();

  // Espera un momento para asegurar que el video se está reproduciendo
  await page.waitForTimeout(5000); // Espera 5 segundos, ajusta según sea necesario
});
