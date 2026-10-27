const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9"; // 10 x 5.625
pres.title = "Project Vyapaar - Findings";
const DARK = "0F3D4C", ACC = "E36414", LIGHT = "F3F6F7", INK = "1F2A30", MUTED = "5B6B73", GREY = "B8C2C7";
const H = "Cambria", B = "Calibri";
const chartBase = { catAxisLabelColor: MUTED, valAxisLabelColor: MUTED, catAxisLabelFontFace: B, valAxisLabelFontFace: B,
  catAxisLabelFontSize: 11, valAxisLabelFontSize: 10, valGridLine: { color: "E1E6E8", size: 0.5 }, catGridLine: { style: "none" },
  dataLabelFontFace: B, dataLabelFontSize: 10, dataLabelColor: INK, legendFontFace: B, legendFontSize: 11, legendColor: INK };

function title(s, t) { s.addText(t, { x: 0.5, y: 0.3, w: 9, h: 0.75, fontFace: H, fontSize: 26, bold: true, color: INK, isTextBox: true, margin: 0 }); }
function stat(s, x, y, big, small, color) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 3.0, h: 1.05, fill: { color: "FFFFFF" }, rectRadius: 0.08, line: { color: "E1E6E8", width: 0.75 } });
  s.addText(big, { x: x + 0.2, y: y + 0.08, w: 2.6, h: 0.55, fontFace: H, fontSize: 28, bold: true, color: color || ACC, isTextBox: true, margin: 0 });
  s.addText(small, { x: x + 0.2, y: y + 0.6, w: 2.6, h: 0.4, fontFace: B, fontSize: 11, color: MUTED, isTextBox: true, margin: 0 });
}
function action(s, x, y, text) {
  s.addText([{ text: "Action: ", options: { bold: true, color: ACC } }, { text, options: { color: INK } }],
    { x, y, w: 3.0, h: 1.0, fontFace: B, fontSize: 13, valign: "top", isTextBox: true, margin: 0 });
}

// 1. Title
let s = pres.addSlide(); s.background = { color: DARK };
s.addText("Project Vyapaar", { x: 0.6, y: 0.7, w: 8.8, h: 0.8, fontFace: H, fontSize: 40, bold: true, color: "FFFFFF", isTextBox: true, margin: 0 });
s.addText("₹176 lakh of revenue. Under ₹1 lakh left after product cost and marketing.", { x: 0.6, y: 1.5, w: 8.8, h: 0.9, fontFace: B, fontSize: 18, italic: true, color: "CFE3EA", isTextBox: true, margin: 0 });
[["₹176L", "Revenue (2025)"], ["₹48L", "Gross profit (27%)"], ["₹47L", "Marketing spend"]].forEach((d, i) => {
  const x = 0.6 + i * 3.0;
  s.addText(d[0], { x, y: 2.85, w: 2.7, h: 0.8, fontFace: H, fontSize: 36, bold: true, color: i === 2 ? "F4A261" : "FFFFFF", isTextBox: true, margin: 0 });
  s.addText(d[1], { x, y: 3.65, w: 2.7, h: 0.4, fontFace: B, fontSize: 13, color: "CFE3EA", isTextBox: true, margin: 0 });
});
s.addText("Team: ____________________   |   BBA Business Analytics Hackathon", { x: 0.6, y: 4.8, w: 8.8, h: 0.4, fontFace: B, fontSize: 11, color: "9FB8C1", isTextBox: true, margin: 0 });
s.addNotes("Hook: Vyapaar made 176 lakh of revenue last year, but after product costs and marketing, less than 1 lakh was left. Here is where the money goes.");

// 2. Electronics
s = pres.addSlide(); s.background = { color: LIGHT };
title(s, "Electronics sells, but barely makes money");
s.addChart(pres.charts.BAR, [
  { name: "Share of revenue", labels: ["Beauty", "Sports", "Home & Kitchen", "Electronics", "Office", "Fashion"], values: [30.0, 17.0, 15.9, 14.5, 12.2, 10.4] },
  { name: "Share of profit", labels: ["Beauty", "Sports", "Home & Kitchen", "Electronics", "Office", "Fashion"], values: [44.7, 18.1, 13.2, 3.2, 11.5, 9.3] },
], { x: 0.4, y: 1.15, w: 5.9, h: 4.1, barDir: "col", barGapWidthPct: 60, chartColors: [GREY, ACC], showValue: true, dataLabelPosition: "outEnd",
  dataLabelFormatCode: '0.0"%"', valAxisHidden: true, showLegend: true, legendPos: "t", ...chartBase });
stat(s, 6.6, 1.25, "6.1%", "Electronics margin vs 27% average");
stat(s, 6.6, 2.45, "237", "Electronics orders sold at a loss");
action(s, 6.6, 3.7, "cap Electronics discounts at 10% (about +₹1.5 lakh profit a year). Push Beauty, our profit engine.");
s.addNotes("Electronics is 14.5% of revenue but only 3.2% of profit. It is priced at only 1.22x cost, so it has no room for discounts. Beauty is 30% of revenue and 45% of profit.");

// 3. Discounts
s = pres.addSlide(); s.background = { color: LIGHT };
title(s, "Big discounts cut profit without lifting sales");
const d = ["0%", "5%", "10%", "15%", "20%", "30%", "40%"];
s.addChart(pres.charts.LINE, [
  { name: "All categories", labels: d, values: [37.5, 33.4, 29.6, 26.2, 20.8, 11.7, -1.2] },
  { name: "Electronics", labels: d, values: [18.0, 13.7, 8.9, 3.5, -2.5, -17.1, -36.7] },
], { x: 0.4, y: 1.15, w: 5.9, h: 4.1, chartColors: [GREY, ACC], lineSize: 3, lineDataSymbolSize: 7, showLegend: true, legendPos: "t",
  valAxisTitle: "Profit margin %", showValAxisTitle: true, valAxisTitleFontSize: 11, valAxisTitleColor: MUTED, catAxisTitle: "Discount given", showCatAxisTitle: true, catAxisTitleFontSize: 11, catAxisTitleColor: MUTED, ...chartBase });
stat(s, 6.6, 1.25, "1.77 → 1.69", "Units per order at 0% vs 40% off");
stat(s, 6.6, 2.45, "₹28L", "Given away in discounts in 2025");
action(s, 6.6, 3.7, "set a maximum discount per category. No 40% discounts; test big sales on a small group first.");
s.addNotes("Customers buy the same number of units whatever the discount (correlation -0.01). Profit per order falls from 1,915 to -33 rupees. 30-40% discount orders are 18% of orders but 3.5% of profit.");

// 4. East
s = pres.addSlide(); s.background = { color: LIGHT };
title(s, "The East region has a late-delivery problem");
s.addChart(pres.charts.BAR, [{ name: "% orders with late-delivery complaint", labels: ["East", "North", "South", "West"], values: [38.5, 12.3, 12.1, 13.1] }],
  { x: 0.4, y: 1.15, w: 5.9, h: 4.1, barDir: "col", barGapWidthPct: 50, chartColors: [ACC, GREY, GREY, GREY], showValue: true, dataLabelPosition: "outEnd",
    dataLabelFormatCode: '0.0"%"', valAxisHidden: true, showLegend: false, showTitle: true, title: "% of orders with a late-delivery complaint", titleFontFace: B, titleFontSize: 12, titleColor: MUTED, ...chartBase });
stat(s, 6.6, 1.25, "48%", "of all escalations come from East (19% of orders)");
stat(s, 6.6, 2.45, "3.2 vs 3.9", "East average rating vs other regions");
action(s, 6.6, 3.7, "audit the East delivery partner within 30 days and set an on-time target.");
s.addNotes("38.5% of East orders get a late-delivery complaint vs 12-13% elsewhere, in every month and every channel. Late delivery has the worst rating (2.43) and 48% get escalated. 99% of customers come back, so experience matters. We could not prove customers are leaving yet.");

// 5. Hidden mystery + actions
s = pres.addSlide(); s.background = { color: DARK };
s.addText("Our hidden mystery: marketing eats 98% of profit", { x: 0.5, y: 0.3, w: 9, h: 0.75, fontFace: H, fontSize: 26, bold: true, color: "FFFFFF", isTextBox: true, margin: 0 });
[["98%", "of gross profit spent on marketing"], ["11%", "of 'campaign' orders placed while the campaign ran"], ["15", "new customers in Jul-Dec, despite ₹20.75L spend"]].forEach((t, i) => {
  const x = 0.5 + i * 3.1;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.25, w: 2.8, h: 1.45, fill: { color: "174E60" }, rectRadius: 0.08, line: { color: "174E60" } });
  s.addText(t[0], { x: x + 0.2, y: 1.35, w: 2.4, h: 0.7, fontFace: H, fontSize: 36, bold: true, color: "F4A261", isTextBox: true, margin: 0 });
  s.addText(t[1], { x: x + 0.2, y: 2.05, w: 2.4, h: 0.55, fontFace: B, fontSize: 12, color: "CFE3EA", isTextBox: true, margin: 0 });
});
s.addText("What we recommend", { x: 0.5, y: 3.0, w: 9, h: 0.4, fontFace: H, fontSize: 18, bold: true, color: "FFFFFF", isTextBox: true, margin: 0 });
s.addText([
  { text: "Discounts: cap by category; Electronics at 10%, no 40% offers.", options: { bullet: true, breakLine: true } },
  { text: "Delivery: audit East's delivery partner in 30 days; set an on-time target.", options: { bullet: true, breakLine: true } },
  { text: "Marketing: fix campaign tracking, count only new customers as conversions, move Outdoor budget (₹6,587 per conversion) to Email and Affiliate.", options: { bullet: true } },
], { x: 0.5, y: 3.45, w: 9, h: 1.8, fontFace: B, fontSize: 14, color: "FFFFFF", paraSpaceAfter: 6, valign: "top", isTextBox: true, margin: 0 });
s.addNotes("Marketing spend of 47 lakh equals 98% of the 48 lakh gross profit. Only 11% of campaign-tagged orders happened during the campaign; 48% came before it started. Marketing reports 4,309 conversions but we have only 599 customers. This is not an ROI claim: the data cannot show which sales campaigns caused.");

pres.writeFile({ fileName: "Vyapaar_Findings.pptx" }).then(() => console.log("ok"));
