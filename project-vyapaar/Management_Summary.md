# Project Vyapaar: Management Summary

**Team:** ____________________  
**Data used:** orders (4,000 after cleaning), products (120), reviews (4,000), marketing (18 campaigns), all for Jan-Dec 2025  
**Full workings:** `Vyapaar_Analysis.ipynb` | **Charts:** `charts/` | **Cleaned data and cleaning log:** `data/cleaned/`

---

## Can we trust the data? (Stage 1 in one line)
Yes, mostly. Revenue, cost and profit add up on every order. We fixed 3 duplicate rows, 2 mislabelled products, 1 spelling variant and 1 missing discount (rebuilt from revenue). **The one field we can't trust is the campaign tag on orders**, so we did not use it to judge campaigns. Full Problem → Action → Reason log: `data/cleaned/cleaning_log.csv`.

---

## Finding 1: Electronics sells, but it barely makes money
- **Evidence:** Electronics brings in **14.5% of revenue but only 3.2% of profit**. Its margin is 6.1% against a company average of 27.3%. **237 of its 809 orders lost money.** Its products are priced at only 1.22× cost, so the margin turns negative at a 20% discount. *(Chart 1, Chart 2)*
- **Business implication:** Electronics uses discount budget and management attention for very little return. Beauty is the real profit engine: 30% of revenue but **44.7% of profit**.
- **Recommended action:** cap Electronics discounts at **10%**. Assuming volumes hold, that adds about **₹1.5 lakh profit a year**, roughly doubling the category's profit. Also renegotiate Electronics supplier costs and move promotional focus towards Beauty.

## Finding 2: Deep discounts give away profit without increasing sales
- **Evidence:** customers buy the same number of units whatever the discount: **1.77 units per order at 0% off vs 1.69 at 40% off** (correlation −0.01). Over the same range, profit per order falls from **₹1,915 to −₹33**. Orders at 30-40% off are 18% of orders but only **3.5% of profit**. In total, **₹28 lakh was given away in discounts**, more than half of gross profit. *(Chart 2)*
- **Business implication:** the evidence does **not** support the current discount strategy. Discounts mostly cut the price for people who would have bought anyway.
- **Recommended action:** set a **maximum discount for each category, based on its mark-up**: no 40% discounts anywhere, Electronics capped at 10%, and Home & Kitchen, Office Supplies and Sports capped at 20%. Test any deeper promotion on a small group before rolling it out.

## Finding 3: The East region has a delivery problem that is hurting ratings
- **Evidence:** **38.5% of East orders get a late-delivery complaint, against 12-13%** in the other regions. This happens every month and in every sales channel. East has 19% of orders but **48% of all escalations**, and its average rating is 3.23 against about 3.9 elsewhere. Late delivery is also the worst complaint overall: average rating 2.43 and **48% escalated**. *(Chart 3)*
- **Business implication:** 99% of Vyapaar's customers buy again, so customer experience is the main asset. Escalations cost service time, and low ratings make it harder to win new customers. We could **not** prove that customers are leaving yet. That makes now the time to fix it, before they start leaving.
- **Recommended action:** within 30 days, audit the East delivery partner(s) and the delivery dates we promise there. Set an on-time delivery target for East and review it every month. Give the analytics team `delivery.csv` so they can find the root cause.

---

## 🕵️ OUR HIDDEN MYSTERY: Marketing eats 98% of gross profit, and we can't prove it works
- **Question:** after paying for marketing, how much profit is actually left, and are the campaigns really bringing in the sales?
- **Evidence:**
  - Marketing spend is **₹47.0 lakh**, against **₹48.0 lakh gross profit**. That leaves **under ₹1 lakh** on ₹176 lakh of revenue (0.6%). *(Chart 4)*
  - Only **11%** of campaign-tagged orders were placed while the campaign was running. **48% were placed before the campaign had even started.** *(Chart 5)*
  - Marketing reports **4,309 conversions**, but the company has only **599 customers**. Campaigns launched in H2 spent ₹20.75 lakh, yet only **15 new customers** placed a first order in H2.
- **Business significance:** after product cost, marketing is the biggest cost we can control, and right now nobody can measure whether it works. Since almost all customers are repeat buyers, many of these "conversions" may be people who would have bought anyway.
- **Recommendation:**
  1. Fix campaign tracking: a unique coupon or UTM link per campaign, and the system should reject a tag dated outside the campaign.
  2. Define a conversion as "**first order by a new customer**".
  3. Pause Outdoor in one region for a month and compare sales with similar regions.
  4. Move Outdoor budget (**₹6,587 per conversion, about 10× Affiliate's ₹642**) to Email and Affiliate.

*Not an ROI calculation:* the order data can't tell us which sales each campaign really caused, so we compare cost per conversion with average gross profit per order (₹1,199) and per customer per year (₹8,008) instead.

---

## Other things we checked
- **High-value customers** (our definition: the top 10% by gross profit, at least ₹15,161 each in 2025): these are **60 customers** who average 9.2 orders and bring 23.5% of profit. Profit is spread fairly evenly across customers, so the business does not depend on a handful of them.
- **Seasonality:** revenue is flat at ₹13-17 lakh a month, so timing is not the issue.
- **Suppliers, payment methods and channels:** no big differences in complaints or margin.

## Facts vs assumptions / limitations
- `customers.csv` and `delivery.csv` were not in our data folder. We used `region_at_order` as a stand-in for customer region (every customer orders from only one region) and the "Late delivery" complaint as a stand-in for delivery data.
- Gross profit here is revenue minus product cost only. Shipping, returns, salaries and rent are not in the data, so the profit left after marketing is probably even lower.
- The ₹1.5 lakh Electronics figure assumes customers keep buying the same quantity. The data supports this, but it is still an assumption.

---

## 3-minute boardroom pitch (script)
1. **(20 sec) Hook:** "Vyapaar made ₹176 lakh of revenue last year. After product costs and marketing, less than ₹1 lakh was left. We want to show you where the money goes."
2. **(40 sec) Electronics + discounts:** show Chart 1, then Chart 2. "Electronics is 14.5% of sales but 3% of profit. It loses money at any discount above 15%, and discounts don't make anyone buy more. We gave away ₹28 lakh."
3. **(40 sec) East delivery:** show Chart 3. "In the East, more than 1 in 3 orders gets a late-delivery complaint. East produces half of all escalations. Our customers are loyal (99% buy again), so we need to fix this before they stop coming back."
4. **(50 sec) Hidden mystery:** show Chart 4, then Chart 5. "Marketing costs as much as our entire gross profit, and the tracking can't prove it works. Half the 'campaign' orders came before the campaign started."
5. **(30 sec) Three asks:** "(1) Cap discounts by category, Electronics at 10%. (2) Audit East delivery in 30 days. (3) Fix campaign tracking and move Outdoor budget to Email and Affiliate."
