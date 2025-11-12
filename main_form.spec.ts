import { test, expect, Locator, Page } from '@playwright/test';

test('Main form end-to-end flow', async ({ page }: { page: Page }) => {
  // === LOGIN + NAVIGATION ===
  await page.goto('https://your-app-url.com/login');
  await page.fill('#username', ''); // optional if auto-login
  await page.click('#loginButton');
  await page.waitForURL('**/home');

  await page.click('button:has-text("Go To Form")');
  await expect(page).toHaveURL('**/form');

  // === FORM FIELD CHECKS ===
  const formSelectors: string[] = [
    '#companyName',
    '#firstName',
    '#lastName',
    '#ssn',
    '#startupName',
    '#jobTitle',
    '#uploadResume',
    '#uploadOtherDocs',
    '#submitButton'
  ];

  for (const selector of formSelectors) {
    const elem: Locator = page.locator(selector);
    await expect(elem, `Element not visible: ${selector}`).toBeVisible();
  }

  const factCheckBtn: Locator = page.locator('#factCheckBtn');
  await expect(factCheckBtn).toBeDisabled();

  // === FIELD ENTRY + VALIDATION ===
  type Entry = { selector: string; value: string; expected?: string };
  const entries: Entry[] = [
    { selector: '#companyName', value: 'Company Name' },
    { selector: '#firstName', value: 'John' },
    { selector: '#lastName', value: 'Smithereens' },
    { selector: '#ssn', value: '123456789', expected: '***-**-6789' },
    { selector: '#startupName', value: 'Startup Name' },
    { selector: '#jobTitle', value: 'CFO' }
  ];

  for (const { selector, value, expected } of entries) {
    await page.fill(selector, value);
    const actual = await page.inputValue(selector);
    expect(actual).toBe(expected ?? value);
  }

  // === FILE UPLOADS ===
  await page.setInputFiles('#uploadResume', 'John Smithereens Resume.pdf');
  const resumeTitle = await page.getAttribute('#resumeFile', 'title');
  expect(resumeTitle).toContain('John Smithereens Resume.pdf');

  await page.setInputFiles('#uploadOtherDocs', 'Demo Pitch Deck.pdf');
  const docsTitle = await page.getAttribute('#otherDocsFile', 'title');
  expect(docsTitle).toContain('Demo Pitch Deck.pdf');

  // === REMOVE / RE-UPLOAD ===
  await page.click('#removeResume');
  await expect(page.locator('#uploadResume')).toHaveText('+ Upload Docs');

  await page.click('#removeOtherDocs');
  await expect(page.locator('#uploadOtherDocs')).toHaveText('+ Upload Docs');

  await page.setInputFiles('#uploadResume', 'John Smithereens Resume.pdf');
  await page.setInputFiles('#uploadOtherDocs', 'Demo Pitch Deck.pdf');

  // === SUBMIT ===
  await page.click('#submitButton');
  await expect(page.locator('#loadingScreen')).toBeVisible();
  await page.waitForSelector('#reportPage');

  // === EDUCATION PAGE VALIDATION ===
  const eduSelectors: string[] = [
    '#companyNameHeader',
    '#startupSidebar',
    '#nameHeader',
    '#eduButtonSidebar',
    '#expButtonSidebar',
    '#licenseButtonSidebar',
    '#backgroundCheckSidebar',
    '#verificationScore',
    '#suitabilityScore',
    '#seeMoreVerification',
    '#seeMoreSuitability',
    '#universityName1',
    '#degreeTitle1',
    '#major1',
    '#minor1',
    '#universityName2',
    '#degreeTitle2',
    '#major2',
    '#minor2'
  ];

  for (const sel of eduSelectors) {
    const elem: Locator = page.locator(sel);
    await expect(elem, `Failed on ${sel}`).toBeVisible();
  }

  // === EXPERIENCE PAGE ===
  await page.click('#experienceButton');
  const expButton: Locator = page.locator('#experienceButton');
  const expClass = await expButton.getAttribute('class');
  expect(expClass).toContain('bg-[#8aecb3]');

  const experienceBlocks: Locator = page.locator('.experience-block');
  await expect(experienceBlocks).toHaveCountGreaterThan(0);

  const count = await experienceBlocks.count();
  for (let i = 0; i < count; i++) {
    const fields: Locator = experienceBlocks.nth(i).locator('.exp-field');
    const fieldCount = await fields.count();
    for (let j = 0; j < fieldCount; j++) {
      const text = await fields.nth(j).textContent();
      expect(text?.trim()).not.toBe('');
    }
  }
});
