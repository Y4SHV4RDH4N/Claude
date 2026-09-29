# ---------------- COVER ----------------
A('''<div style="padding:10px 0 20px"><span class="tag">Midterm</span><span class="tag">Service Operations</span>
<h1>Midterm Study Guide</h1>
<p class="sub">Prof. Sirsha Pattanayak &middot; Session 1 &middot; Waiting &amp; Queuing &middot; Revenue &amp; Yield Management &middot; Service Facility Layout (slide 47 onwards)</p></div>''')
A('''<div class="box"><b>How to use this in the last days before the exam</b>
<ol><li>Read <b>Part 0</b> (formula sheet map + traps) once. It is the highest-value page.</li>
<li>For each part: skim the formula boxes, then <b>cover the solution and redo every solved example</b> on paper. Numbers here were all re-computed and checked.</li>
<li>In the exam, always follow the same loop: <b>identify the model &rarr; list givens with units &rarr; pick formulas &rarr; compute &rarr; interpret / decide</b>.</li></ol></div>''')
A('''<div class="box"><b>Contents</b><ol class="toc">
<li><a href="#p0">Part 0 &mdash; Formula sheet: what is on it, what is not, and the traps</a></li>
<li><a href="#p1">Part 1 &mdash; Session 1: Nature of services (theory)</a></li>
<li><a href="#p2">Part 2 &mdash; Waiting lines &amp; queuing (formulas + 10 solved examples)</a></li>
<li><a href="#p3">Part 3 &mdash; Revenue &amp; yield management (formulas + 7 solved examples)</a></li>
<li><a href="#p4">Part 4 &mdash; Service facility layout (formulas + 4 solved examples)</a></li>
<li><a href="#p5">Part 5 &mdash; 2-hour exam plan, unit checks, last-minute checklist</a></li></ol></div>''')
A(T(["Topic", "Emphasis (my estimate from your note)", "Type"], [
 ["Waiting lines (M/M/1, M/M/1/N, M/M/c, M/D/1, cost trade-offs)", "Largest", "Numerical"],
 ["Revenue mgmt (Littlewood, overbooking, multi-segment pricing)", "Large", "Numerical + short concept"],
 ["Facility layout (line balancing, utilization, bottleneck, cost)", "Medium", "Numerical"],
 ["Session 1 + game theory in RM + servicescape/layout concepts", "Small", "Short answers"]]))

# ---------------- PART 0 ----------------
A('<section class="part" id="p0"><span class="tag">Part 0</span><h2>The Formula Sheet: how to use it</h2><p class="sub">The sheet has 3 pages. Know exactly what is on it and what is missing.</p>')
A(T(["Formula-sheet block", "Use for", "Watch out"], [
 ["<b>M/M/1/&infin;/&infin;</b> (11 items)", "Single server, unlimited queue and population. Needs &lambda; &lt; &mu;.", "Items 6&amp;7 are Little&rsquo;s law. Item 5: L<sub>S</sub> = L<sub>Q</sub> + &rho;. Item 11 has a typo (&ldquo;==&rdquo;) &mdash; it is W<sub>Q</sub> = &lambda;/[&mu;(&mu;&minus;&lambda;)]."],
 ["<b>M/M/1/N/&infin;</b>", "Single server, max N customers in the <i>system</i> (waiting room + server). Blocked customers are lost.", "Use &lambda;<sub>eff</sub> (not &lambda;) in W<sub>S</sub>, W<sub>Q</sub>. Formula for L<sub>S</sub> fails when &rho;=1 (not expected)."],
 ["<b>M/M/c/&infin;/&infin;</b>", "c identical servers, one queue.", "<b>&rho; = &lambda;/(c&mu;)</b> in P<sub>0</sub>, but in the L<sub>Q</sub> formula the symbol &rho; means <b>r = &lambda;/&mu;</b> (offered load). See trap below."],
 ["<b>M/D/1/&infin;/&infin;</b>", "Constant (fixed) service time: automatic machines, car wash, compactor.", "L<sub>Q</sub> and W<sub>Q</sub> are exactly <b>half</b> of the M/M/1 values (extra 2 in denominator)."],
 ["<b>Page 3 (bottom): capacity &amp; cost lines</b>", "Layout (line balancing) and the critical ratio for Littlewood/overbooking.", "C<sub>u</sub> = p&minus;c and C<sub>o</sub> = c&minus;v are the <i>generic newsvendor</i> definitions. For RM, redefine them (see Part 3)."]]))
A(W("Trap 1 &mdash; &rho; in M/M/c", "On the sheet, &rho; = &lambda;/(c&mu;) is <i>utilisation</i>. Inside L<sub>Q</sub> = &rho;<sup>c+1</sup>P<sub>0</sub> / [(c&minus;&rho;)<sup>2</sup>(c&minus;1)!] the &rho; is really <b>&lambda;/&mu;</b>. Check with c=1: it must collapse to &lambda;<sup>2</sup>/[&mu;(&mu;&minus;&lambda;)]. Only that reading passes. Also in P<sub>0</sub>, (c&rho;)<sup>n</sup> = (&lambda;/&mu;)<sup>n</sup>, so it is consistent."))
A(W("Trap 2 &mdash; Units", "Convert everything to <b>per hour</b> first. &ldquo;Customers arrive every 3 minutes&rdquo; &rArr; &lambda; = 60/3 = 20 per hour. Formulas return hours; multiply by 60 for minutes."))
A(W("Trap 3 &mdash; Not on the sheet (memorise!)", "P(n &gt; k in system) = &rho;<sup>k+1</sup> (M/M/1) &bull; Probability an arrival waits in M/M/c &bull; Littlewood: P(D<sub>H</sub> &gt; Q) = F<sub>L</sub>/F<sub>H</sub> &bull; optimal price p = A/(2B) + c/2 &bull; capacitated pricing with Lagrange multiplier &bull; utilisation of bottlenecked lines with cost per customer &bull; normal <b>z-values</b> (table below)."))
A(F("Which line of the sheet answers which question", 
 "<i>&ldquo;% of time server idle&rdquo;</i> &rarr; P<sub>0</sub> ;; <i>&ldquo;% of time no queue&rdquo;</i> &rarr; P<sub>0</sub>+P<sub>1</sub> (server has at most 1 customer)",
 "<i>&ldquo;Average number waiting&rdquo;</i> &rarr; L<sub>Q</sub> ;; <i>&ldquo;in the system&rdquo;</i> &rarr; L<sub>S</sub>",
 "<i>&ldquo;Average time waiting to be served&rdquo;</i> &rarr; W<sub>Q</sub> ;; <i>&ldquo;total time incl. service&rdquo;</i> &rarr; W<sub>S</sub>",
 "<i>&ldquo;Server utilisation / busy&rdquo;</i> &rarr; &rho; (or 1&minus;P<sub>0</sub>) ;; <i>&ldquo;lost customers&rdquo;</i> &rarr; &lambda;&middot;P<sub>N</sub>",
 "<i>&ldquo;How many seats to protect / how many to overbook&rdquo;</i> &rarr; CR and Q* = &mu;+z&sigma;",
 "<i>&ldquo;Capacity / cycle time / utilisation of a line&rdquo;</i> &rarr; page-3 capacity lines"))
A('<h3>Normal z-table shortcuts (for CR &rarr; z)</h3>')
A(T(["CR = P(X&le;Q)", "0.10", "0.20", "0.2857", "0.29", "0.30", "0.40", "0.50", "0.60", "0.70", "0.75", "0.80", "0.90", "0.95", "0.975", "0.99"],
    [["z", "&minus;1.28", "&minus;0.84", "&minus;0.57", "&minus;0.55", "&minus;0.52", "&minus;0.25", "0", "0.25", "0.52", "0.67", "0.84", "1.28", "1.64", "1.96", "2.33"]], num=range(1, 16)))
A('<p class="small">Symmetry: z(1&minus;p) = &minus;z(p). If the exam gives its own z-table, use that; small differences in the 2nd decimal are fine.</p></section>')

# ---------------- PART 1 ----------------
A('<section class="part" id="p1"><span class="tag">Part 1</span><h2>Session 1: Nature of Services</h2><p class="sub">Mostly theory &mdash; expect short answers / 1-2 marks. Learn the lists and the examples.</p>')
A('<h3>Core ideas</h3>')
A(UL("<b>Definition by exclusion:</b> services are defined by what they are <i>not</i> &mdash; economic reports call anything not &ldquo;goods-producing&rdquo; or &ldquo;extraction-based&rdquo; a service (retail, wholesale, transport, finance, lodging, education, government, entertainment&hellip;).",
 "<b>Evolution:</b> Pre-industrial (domestic servants, sailors; relationships; little tech) &rarr; Industrial (assembly line, human as a &ldquo;cog&rdquo;, output focus, blue- vs white-collar) &rarr; Post-industrial (health, education, recreation; information rather than muscle; far higher share of service activity).",
 "<b>Service&ndash;product continuum:</b> product-dominant (passenger cars, machine tools) &harr; mixed (restaurants, fitness centres, hospitals) &harr; service-dominant (consulting, legal, logistics, tourism, facilities maintenance).",))
A('<h3>Services vs manufacturing (the 5 differences)</h3>')
A(T(["Feature", "Manufacturing", "Services"], [
 ["Customer role", "Not part of the process", "<b>Customer is an input</b>; participates (facility design, decor, layout, noise matter; open kitchens build confidence)."],
 ["System type", "Closed system", "<b>Permeable</b> system"],
 ["Simultaneity", "Produce, store, then sell", "Created and consumed at the same time"],
 ["Inventory", "Inventory control", "<b>Cannot be inventoried</b> &rarr; queuing / capacity management instead"],
 ["Perishability", "Stockable", "Perishable (empty seat / room / hour is lost forever) &rarr; revenue management"],
 ["Tangibility", "Customer can see, touch, test", "Intangible; performance judged after/while consumed"]]))
A('<h3>Classifications of services</h3>')
A(T(["Type", "Distinctive", "Example", "Main managerial issue"], [
 ["B2B", "Customer is an organisation; buyer may not be end user", "Consultancy, maintenance", "Demonstrate value, reliability, customisation"],
 ["B2C", "Individual is buyer/user", "Hotel, bank, retail", "Consistency across heterogeneous customers"],
 ["Internal", "Customer is another unit in same firm", "HR, IT, Finance", "Show value vs outsourcing"],
 ["Public (G2C/G2B)", "Little choice; tax-funded", "Govt hospital, school, prisons", "Access, fairness, acceptable quality, capacity"],
 ["Not-for-profit", "Beneficiary may not be payer", "Faith orgs, aid agencies", "Mission effectiveness"]]))
A('<h4>Customer-contact classification</h4>')
A(UL("<b>High contact = pure services</b> (hospitals, restaurants, banking) &rarr; <b>mixed</b> &rarr; <b>Low contact = quasi-manufacturing</b> (distribution centres, warehouses)."))
A('<h4>Service process matrix (labour intensity vs interaction &amp; customisation)</h4>')
A(T(["", "Low interaction &amp; customisation", "High interaction &amp; customisation"], [
 ["<b>Low labour intensity</b>", "<b>Service factory</b> &mdash; airlines", "<b>Service shop</b> &mdash; hospital"],
 ["<b>High labour intensity</b>", "<b>Mass service</b> &mdash; retailing", "<b>Professional service</b> &mdash; consultancy"]]))
A('<p><b>Challenges by cell:</b> low-labour/low-customisation (service factory) &rarr; capital decisions, technology, demand peaks, scheduling. High-labour/high-customisation (professional) &rarr; hiring &amp; training, SOPs, workforce scheduling, control of far-flung locations, making service &ldquo;warm&rdquo;, quality vs cost, customers intervening in the process.</p>')
A('<h3>Other slide points</h3>')
A(UL("<b>Low-cost vs full-service airline:</b> high volume/low cost, short hauls, secondary airports, no frills vs global network, long haul with partner connections, primary airports, economy-to-first cabins.",
 "<b>Service blueprint:</b> strategic elements (service concept, service design) vs tactical/operational elements (facility, revenue management, queuing theory).",
 "<b>Sharing economy:</b> classical inventory asks <i>how much / when to order</i> (controlled supply). On platforms supply and demand stimulate each other and are not controlled by the platform &rarr; the decision becomes <b>matching</b> a unit of supply to a unit of demand.",
 "<b>Internet service design elements:</b> product, process, touch point, outcome; product/technology/task; customer/employee; performance.",
 "<b>New services (examples):</b> AIaaS, carbon-footprint auditing, elder companionship, pet tech, digital detox (fast growth); circular economy, urban farming, skill barter, therapy bots (scalable); metaverse, space tourism, memory preservation (transformational)."))
A('</section>')

# ---------------- PART 2 ----------------
A('<section class="part" id="p2"><span class="tag">Part 2</span><h2>Waiting Lines &amp; Queuing</h2><p class="sub">The biggest numerical block. Master M/M/1, M/M/1/N, M/M/c, M/D/1 and the cost trade-off.</p>')
A('<h3>2.1 Concepts (1-2 mark theory)</h3>')
A(UL("<b>Why lines form:</b> (a) workload &gt; capacity, or (b) <b>variability</b> in arrivals and/or service times &mdash; even when average workload &lt; capacity. Class demo: single teller, workload 50 min vs 60 min available &rarr; total wait <b>52 min</b>; two tellers (120 min available) &rarr; <b>7 min</b>. So <b>waiting is not linear in capacity</b>.",
 "<b>Balking</b> = arrival sees long queue and does not join. <b>Reneging</b> = leaves the queue before service. <b>Jockeying</b> = switches queues. (Single queue &rarr; no jockeying; multiple queues &rarr; jockeying.)",
 "<b>Channel</b> = number of servers; <b>phase</b> = number of sequential steps. Single-channel/single-phase (one cashier); single-channel/multi-phase (car wash: wash &rarr; dry); multi-channel/single-phase (bank counters); multi-channel/multi-phase (hospital: registration &rarr; doctor &rarr; tests).",
 "<b>Kendall notation M/M/c/N/pop:</b> arrivals Poisson (M), service Exponential (M) or Deterministic (D), c servers, N = max in system, population size.",
 "<b>Economics:</b> cost of capacity rises with servers, cost of waiting falls; <b>total cost is U-shaped</b>; minimum = optimal capacity. Waiting costs = opportunity cost of time, psychological cost, abandonment.",
 "<b>Stability:</b> for infinite queue models need &rho; &lt; 1."))
A('<h4>Psychology of waiting (tactics)</h4>')
A(T(["Law of service", "Tactic", "Example"], [
 ["Unoccupied time feels longer", "Distract / entertain", "Mirrors in Boston hotel elevator lobby instead of more elevators"],
 ["Pre-process waits feel longer than in-process", "Get customers &ldquo;in process&rdquo; quickly", "Menus, welcome drinks; fill a form while waiting"],
 ["Uncertain waits feel longer than known waits", "Communicate expected wait upfront and update", "Call-centre &ldquo;expected wait 6 minutes&rdquo;"],
 ["Fairness", "Tokens, FCFS, one common queue, transparent priority", "Car dealership: appointment customers have priority, walk-ins get token"],
 ["Meaningful wait", "Let customers do something useful", "Fill forms, choose from menu"],
 ["Social comparison", "Show queue position and progress", "&ldquo;You are #3&rdquo;, A21&rarr;A22&rarr;A23"]]))
A('<h4>Managing demand</h4>')
A(UL("Challenges: cyclical demand (daily/weekly), random vs planned arrivals (emergency vs appointments), heterogeneous demand sources (business vs leisure).",
 "Strategies: use off-peak capacity creatively (hotel conferences); complementary services (kids zone in cinema); <b>price incentives</b> (night data packs, mid-week discounts); <b>reservations</b> (benefits: customer &mdash; no wait, guaranteed service; firm &mdash; steadier demand, caps demand). Risk: reserved demand that does not show up = lost revenue &rarr; leads to overbooking (Part 3)."))

A('<h3>2.2 Formula boxes (all from the sheet)</h3>')
A(F("M/M/1/&infin;/&infin;  (&lambda; &lt; &mu;)",
 "&rho; = &lambda;/&mu; ;; P<sub>0</sub> = 1 &minus; &rho; ;; P<sub>n</sub> = &rho;<sup>n</sup>P<sub>0</sub>",
 "L<sub>S</sub> = {{&rho;|1&minus;&rho;}} = {{&lambda;|&mu;&minus;&lambda;}} ;; L<sub>Q</sub> = {{&lambda;<sup>2</sup>|&mu;(&mu;&minus;&lambda;)}} ;; L<sub>S</sub> = L<sub>Q</sub> + &rho;",
 "W<sub>S</sub> = {{1|&mu;&minus;&lambda;}} ;; W<sub>Q</sub> = {{&lambda;|&mu;(&mu;&minus;&lambda;)}} ;; W<sub>S</sub> = W<sub>Q</sub> + 1/&mu;",
 "Little: L<sub>S</sub> = &lambda;W<sub>S</sub> ;; L<sub>Q</sub> = &lambda;W<sub>Q</sub>"))
A(F("Extras derived from P<sub>n</sub> (not on sheet)",
 "P(n &ge; k) = &rho;<sup>k</sup> ;; P(n &gt; k) = &rho;<sup>k+1</sup> ;; P(server busy) = &rho;",
 "% time <i>no queue</i> = P<sub>0</sub> + P<sub>1</sub> = (1&minus;&rho;)(1+&rho;) ;; P(wait &gt; 0) = &rho;"))
A(F("M/M/1/N/&infin;  (max N in system; blocked customers lost)",
 "&rho; = &lambda;/&mu; ;; P<sub>0</sub> = {{1&minus;&rho;|1&minus;&rho;<sup>N+1</sup>}} ;; P<sub>n</sub> = &rho;<sup>n</sup>P<sub>0</sub> ;; P<sub>N</sub> = &rho;<sup>N</sup>P<sub>0</sub> (blocking probability)",
 "&lambda;<sub>eff</sub> = &lambda;(1 &minus; P<sub>N</sub>)  ;; lost = &lambda;P<sub>N</sub>",
 "L<sub>S</sub> = {{&rho;{1 + N&rho;<sup>N+1</sup> &minus; (N+1)&rho;<sup>N</sup>}|(1&minus;&rho;)(1&minus;&rho;<sup>N+1</sup>)}}",
 "L<sub>Q</sub> = L<sub>S</sub> &minus; &lambda;<sub>eff</sub>/&mu; ;; W<sub>S</sub> = L<sub>S</sub>/&lambda;<sub>eff</sub> ;; W<sub>Q</sub> = L<sub>Q</sub>/&lambda;<sub>eff</sub>"))
A(F("M/M/c/&infin;/&infin;  (c servers, one queue)",
 "&rho; = {{&lambda;|c&mu;}}  (utilisation) ;; r = &lambda;/&mu; = c&rho; (offered load)",
 "P<sub>0</sub> = {{1|&sum;<sub>n=0</sub><sup>c&minus;1</sup> (c&rho;)<sup>n</sup>/n! + (c&rho;)<sup>c</sup>/[c!(1&minus;&rho;)]}}",
 "P<sub>n</sub> = {{&lambda;<sup>n</sup>P<sub>0</sub>|&mu;<sup>n</sup> n!}} for n &lt; c ;; P<sub>n</sub> = {{&lambda;<sup>n</sup>P<sub>0</sub>|c! &mu;<sup>n</sup> c<sup>n&minus;c</sup>}} for n &ge; c",
 "L<sub>Q</sub> = {{r<sup>c+1</sup>P<sub>0</sub>|(c&minus;r)<sup>2</sup>(c&minus;1)!}}   [sheet writes r as &rho;] ;; W<sub>Q</sub> = L<sub>Q</sub>/&lambda;",
 "W<sub>S</sub> = W<sub>Q</sub> + 1/&mu; ;; L<sub>S</sub> = &lambda;W<sub>Q</sub> + &lambda;/&mu;",
 "P(arrival must wait) = {{r<sup>c</sup>P<sub>0</sub>|c!(1&minus;&rho;)}}  (= P(n &ge; c), derived)"))
A(F("M/D/1/&infin;/&infin;  (constant service time)",
 "&rho; = &lambda;/&mu; ;; P<sub>0</sub> = 1 &minus; &rho;",
 "L<sub>Q</sub> = {{&lambda;<sup>2</sup>|2&mu;(&mu;&minus;&lambda;)}} ;; W<sub>Q</sub> = {{&lambda;|2&mu;(&mu;&minus;&lambda;)}}",
 "L<sub>S</sub> = L<sub>Q</sub> + &lambda;/&mu; ;; W<sub>S</sub> = W<sub>Q</sub> + 1/&mu;"))
A(F("Queue cost (economics of waiting)",
 "Total cost/hr = (server cost/hr &times; no. of servers) + (waiting cost/hr per customer &times; L<sub>Q</sub> or L<sub>S</sub>)",
 "Per customer: waiting cost = c<sub>w</sub> &times; W<sub>Q</sub> (or W<sub>S</sub> if the problem charges time in system)",
 "Read the wording: &ldquo;waiting <i>in queue</i>&rdquo; &rArr; use L<sub>Q</sub>/W<sub>Q</sub>. &ldquo;Time in system&rdquo; &rArr; L<sub>S</sub>/W<sub>S</sub>. Multiply hours by hours of operation for daily cost."))
A(W("Method", "1) Identify model (Poisson/exp? fixed service? limit N? c servers?). 2) Write &lambda;, &mu;, c per hour. 3) Check &rho;&lt;1. 4) Compute &rho;, then L<sub>S</sub>/L<sub>Q</sub>, then W via Little. 5) If costs given, build total cost for each option and compare. 6) State the decision in one sentence."))

A('<h3>2.3 Solved examples</h3>')
A(EX("Example 2.1 &mdash; M/M/1 basics (class: railway counter)", "Easy", 
 "Customers arrive every 3 minutes at a railway ticket counter; the teller serves 25 customers/hour. Infinite queue and population. (a) % of time teller idle, (b) % of time there is no queue. Also find L<sub>Q</sub> and W<sub>Q</sub>.",
 "&lambda; = 60/3 = <b>20/hr</b>, &mu; = 25/hr &rArr; &rho; = 20/25 = <b>0.8</b>.",
 "(a) P<sub>0</sub> = 1 &minus; &rho; = <b>0.20 &rarr; 20%</b>.",
 "(b) No queue &hArr; 0 or 1 in system: P<sub>0</sub> + P<sub>1</sub> = 0.20 + 0.8(0.20) = 0.20 + 0.16 = <b>0.36 &rarr; 36%</b>.",
 "L<sub>Q</sub> = &lambda;<sup>2</sup>/[&mu;(&mu;&minus;&lambda;)] = 400/(25&times;5) = <b>3.2</b> customers. W<sub>Q</sub> = 20/(25&times;5) = 0.16 hr = <b>9.6 min</b>. L<sub>S</sub> = 3.2+0.8 = 4.0; W<sub>S</sub> = 1/5 hr = 12 min.",
 ans="(a) 20%  (b) 36%  L<sub>Q</sub> = 3.2, W<sub>Q</sub> = 9.6 min"))
A(EX("Example 2.2 &mdash; M/M/1 probabilities (pharmacy counter)", "Easy-Moderate",
 "Arrivals every 5 min; average service 4 min; one pharmacist. Find L<sub>S</sub>, L<sub>Q</sub>, W<sub>S</sub>, W<sub>Q</sub>, the probability that 3 or more people are in the system, and that more than 4 are.",
 "&lambda; = 12/hr, &mu; = 60/4 = 15/hr, &rho; = 0.8.",
 "L<sub>S</sub> = &rho;/(1&minus;&rho;) = 0.8/0.2 = <b>4</b>. L<sub>Q</sub> = 144/(15&times;3) = <b>3.2</b> (check: 4 &minus; 0.8 = 3.2 &#10003;).",
 "W<sub>S</sub> = 1/(15&minus;12) = 1/3 hr = <b>20 min</b>. W<sub>Q</sub> = 12/(15&times;3) = 0.2667 hr = <b>16 min</b> (check: L<sub>Q</sub>/&lambda; = 3.2/12 &#10003;).",
 "P(n &ge; 3) = &rho;<sup>3</sup> = 0.8<sup>3</sup> = <b>0.512</b>. P(n &gt; 4) = &rho;<sup>5</sup> = 0.8<sup>5</sup> = <b>0.328</b>.",
 ans="L<sub>S</sub>=4, L<sub>Q</sub>=3.2, W<sub>S</sub>=20 min, W<sub>Q</sub>=16 min, P(&ge;3)=0.512, P(&gt;4)=0.328"))
A(EX("Example 2.3 &mdash; Finite queue M/M/1/N (class, then extended)", "Moderate",
 "Same railway teller (&lambda;=20, &mu;=25) but at most N = 10 customers in the system. (a) % idle, (b) % no queue. Then interpret vs the infinite case.",
 "&rho; = 0.8. P<sub>0</sub> = (1&minus;&rho;)/(1&minus;&rho;<sup>11</sup>) = 0.2/(1 &minus; 0.0859) = <b>0.2188 &rarr; 21.9%</b>.",
 "P<sub>1</sub> = &rho;P<sub>0</sub> = 0.175; no queue = P<sub>0</sub>+P<sub>1</sub> = <b>0.394 &rarr; 39.4%</b>.",
 "<b>Interpretation:</b> idle time is <i>higher</i> with a finite queue (21.9% vs 20%; no-queue 39.4% vs 36%) because arrivals are turned away when full. Customer view: less congestion for admitted customers but risk of being blocked. Provider view: controls congestion and needs less waiting space, but lost customers and revenue.",
 ans="21.9% and 39.4% (vs 20% and 36% for infinite queue)"))
A(EX("Example 2.4 &mdash; M/M/1/N with lost revenue", "Difficult",
 "A car-wash bay has room for at most N = 4 cars in total (one being washed). Cars arrive at &lambda; = 6/hr; the wash rate is &mu; = 5/hr. Each car brings Rs 200 contribution. Find P<sub>0</sub>, P<sub>N</sub>, &lambda;<sub>eff</sub>, L<sub>S</sub>, L<sub>Q</sub>, W<sub>S</sub>, W<sub>Q</sub>, and lost contribution per 10-hour day.",
 "&rho; = 6/5 = 1.2 (&gt;1 is allowed because the system is finite).",
 "P<sub>0</sub> = (1&minus;1.2)/(1&minus;1.2<sup>5</sup>) = (&minus;0.2)/(1&minus;2.48832) = 0.2/1.48832 = <b>0.1344</b>.",
 "P<sub>N</sub> = P<sub>4</sub> = 1.2<sup>4</sup>&times;0.1344 = 2.0736&times;0.1344 = <b>0.2786</b> (27.9% of arrivals are blocked).",
 "&lambda;<sub>eff</sub> = 6(1&minus;0.2786) = <b>4.328/hr</b>. Lost = 6&times;0.2786 = 1.672/hr.",
 "L<sub>S</sub> = &rho;{1 + N&rho;<sup>N+1</sup> &minus; (N+1)&rho;<sup>N</sup>} / [(1&minus;&rho;)(1&minus;&rho;<sup>N+1</sup>)] = 1.2{1 + 4(2.48832) &minus; 5(2.0736)} / [(&minus;0.2)(&minus;1.48832)] = 1.2(1 + 9.9533 &minus; 10.368)/0.29766 = 1.2(0.5853)/0.29766 = <b>2.359</b>.",
 "L<sub>Q</sub> = L<sub>S</sub> &minus; &lambda;<sub>eff</sub>/&mu; = 2.359 &minus; 4.328/5 = 2.359 &minus; 0.866 = <b>1.494</b>.",
 "W<sub>S</sub> = 2.359/4.328 = 0.545 hr = <b>32.7 min</b>. W<sub>Q</sub> = 1.494/4.328 = 0.345 hr = <b>20.7 min</b>.",
 "Lost contribution/day = 1.672 &times; 10 &times; 200 = <b>Rs 3,344</b>. Two decimals of &rho;<sup>N+1</sup> matter &mdash; keep 4 decimals.",
 ans="P<sub>N</sub>=0.279, &lambda;<sub>eff</sub>=4.33/hr, L<sub>S</sub>=2.36, L<sub>Q</sub>=1.49, W<sub>S</sub>=32.7 min, W<sub>Q</sub>=20.7 min, loss &asymp; Rs 3,344/day"))
A(EX("Example 2.5 &mdash; Fire one mechanic, hire another? (class: Star Garage)", "Moderate",
 "Raju installs 3 mufflers/hr; customers arrive at 1/hr; shop open 8 hr/day. Waiting cost = Rs 500 per hour of customer time in queue. Raju is paid Rs 150/hr. Shyam does 4/hr but is paid 50% more. Should Apte replace Raju by Shyam?",
 "&lambda; = 1. <b>Raju:</b> &mu; = 3 &rArr; L<sub>Q</sub> = 1/[3(3&minus;1)] = 1/6 = 0.1667. Waiting cost/hr = 500 &times; 0.1667 = 83.33. Wage 150. Total/hr = 233.33 &rArr; <b>Rs 1,866.67/day</b>.",
 "<b>Shyam:</b> &mu; = 4 &rArr; L<sub>Q</sub> = 1/[4(3)] = 1/12 = 0.0833. Waiting cost/hr = 41.67. Wage = 1.5&times;150 = 225. Total/hr = 266.67 &rArr; <b>Rs 2,133.33/day</b>.",
 "(Same answer using W<sub>Q</sub>: Raju W<sub>Q</sub> = 1/6 hr; cost/hr = 500&times;&lambda;&times;W<sub>Q</sub> = 83.33 &mdash; identical because L<sub>Q</sub> = &lambda;W<sub>Q</sub> and &lambda; = 1.)",
 ans="Keep Raju: Rs 1,867 vs Rs 2,133 per day. Faster server does not pay for its wage premium."))
A(EX("Example 2.6 &mdash; Multi-server M/M/c and pooling", "Difficult",
 "A bank branch has &lambda; = 8 customers/hr and each teller serves &mu; = 5/hr. Compare (i) two tellers sharing <b>one</b> queue (M/M/2) with (ii) two tellers each with their own queue receiving 4/hr (two M/M/1). Then find M/M/3 as well.",
 "<b>(i) M/M/2:</b> &rho; = 8/(2&times;5) = 0.8; r = &lambda;/&mu; = 1.6.",
 "P<sub>0</sub> = 1/[ (r<sup>0</sup>/0!) + (r<sup>1</sup>/1!) + r<sup>2</sup>/(2!(1&minus;0.8)) ] = 1/[1 + 1.6 + 2.56/(2&times;0.2)] = 1/[1 + 1.6 + 6.4] = 1/9 = <b>0.1111</b>.",
 "L<sub>Q</sub> = r<sup>3</sup>P<sub>0</sub>/[(2&minus;1.6)<sup>2</sup>(1!)] = 4.096&times;0.1111/0.16 = <b>2.844</b>.",
 "W<sub>Q</sub> = L<sub>Q</sub>/&lambda; = 2.844/8 = 0.3556 hr = <b>21.3 min</b>. W<sub>S</sub> = W<sub>Q</sub> + 1/&mu; = 0.3556 + 0.2 = 0.5556 hr = <b>33.3 min</b>. L<sub>S</sub> = &lambda;W<sub>Q</sub> + &lambda;/&mu; = 2.844 + 1.6 = <b>4.444</b>.",
 "P(customer has to wait) = r<sup>2</sup>P<sub>0</sub>/[2!(1&minus;&rho;)] = 2.56&times;0.1111/0.4 = <b>0.711</b>.",
 "<b>(ii) Two M/M/1 with &lambda; = 4:</b> W<sub>Q</sub> = 4/[5(1)] = 0.8 hr = <b>48 min</b>; L<sub>Q</sub> per line = 3.2. Pooling cuts the wait from 48 min to 21.3 min with the same 2 tellers.",
 "<b>(iii) M/M/3:</b> &rho; = 8/15 = 0.5333, r = 1.6. P<sub>0</sub> = 1/[1 + 1.6 + 1.28 + 1.6<sup>3</sup>/(6(1&minus;0.5333))] = 1/[3.88 + 4.096/2.8] = 1/(3.88+1.4629) = <b>0.1872</b>. L<sub>Q</sub> = 1.6<sup>4</sup>&times;0.1872/[(3&minus;1.6)<sup>2</sup>&times;2!] = 6.5536&times;0.1872/3.92 = <b>0.3129</b>. W<sub>Q</sub> = 0.3129/8 = 0.0391 hr = <b>2.35 min</b>.",
 ans="M/M/2: L<sub>Q</sub>=2.84, W<sub>Q</sub>=21.3 min &nbsp;|&nbsp; 2&times;M/M/1: W<sub>Q</sub>=48 min &nbsp;|&nbsp; M/M/3: L<sub>Q</sub>=0.31, W<sub>Q</sub>=2.35 min"))
A(EX("Example 2.7 &mdash; Constant service time M/D/1 (class: recycling firm)", "Moderate",
 "Trucks currently wait 15 min (per trip). Waiting cost = Rs 6,000/hr. A new compactor serves at a constant 12 trucks/hr; arrivals are Poisson, 8/hr. Amortised cost of the compactor = Rs 300 per truck unloaded. Buy?",
 "Current waiting cost/truck = 6000 &times; (15/60) = <b>Rs 1,500</b>.",
 "M/D/1: &lambda; = 8, &mu; = 12. W<sub>Q</sub> = &lambda;/[2&mu;(&mu;&minus;&lambda;)] = 8/[2&times;12&times;4] = 8/96 = 1/12 hr = <b>5 min</b>.",
 "New waiting cost/truck = 6000 &times; (1/12) = Rs 500. Add amortised cost Rs 300 &rArr; <b>Rs 800/truck</b>.",
 "Saving = 1500 &minus; 800 = Rs 700 per truck.",
 "<i>Check:</i> the M/M/1 W<sub>Q</sub> at the same rates = 8/[12&times;4] = 10 min, exactly twice the M/D/1 value.",
 ans="Buy the compactor: Rs 800 vs Rs 1,500 per truck (saves Rs 700)."))
A(EX("Example 2.8 &mdash; Economics of waiting: how many tellers? (class: cooperative bank)", "Moderate",
 "Total waiting time accumulated per hour = 54/t<sup>2</sup> minutes where t = number of tellers. Waiting costs Rs 10/min; a teller costs Rs 40/hr. (1) Optimal tellers? (2) Show the trade-off from t&minus;2 to t+2. (3) Over- or under-capacitate?",
 "Total cost(t) = 40t + 10 &times; 54/t<sup>2</sup> = 40t + 540/t<sup>2</sup>.",
 T(["t", "Teller cost", "Waiting cost", "Total"], [["1", "40", "540", "580"], ["2", "80", "135", "215"], ["<b>3</b>", "120", "60", "<b>180</b>"], ["4", "160", "33.75", "193.75"], ["5", "200", "21.60", "221.60"]], num=(1,2,3)),
 "Check with calculus: d/dt = 40 &minus; 1080/t<sup>3</sup> = 0 &rArr; t<sup>3</sup> = 27 &rArr; <b>t = 3</b>.",
 "Trade-off: as t rises capacity cost climbs linearly while waiting cost falls steeply then flattens &rArr; U-shaped total cost &#10003;. Being <b>2 below</b> the optimum costs +35 (215); <b>2 above</b> costs +41.6 (221.6) &mdash; but <b>1 above</b> costs only +13.75 vs <b>1 below</b> +35.",
 ans="3 tellers (Rs 180/hr). Prefer slightly <b>over</b>-capacity: the cost curve is steeper on the under-capacity side."))
A(EX("Example 2.9 &mdash; Two-phase queue: hire a second registration clerk? (class scenario)", "Difficult",
 "Patients arrive at 10/hr. Phase 1 registration: one clerk, &mu;<sub>1</sub> = 12/hr. Phase 2 doctor: &mu;<sub>2</sub> = 15/hr. Patient waiting cost = Rs 150/hr; clerk Rs 300/hr; doctor Rs 1,200/hr. Clinic works 8 hr/day. Is a second registration clerk worthwhile (two clerks working as M/M/2 each at 12/hr)?",
 "Doctor phase is unchanged in both options, so compare only Phase 1. (Departures from an M/M/1 queue are again Poisson at &lambda; = 10, so the phases can be analysed separately.)",
 "<b>Option A &mdash; one clerk (M/M/1):</b> L<sub>S</sub> = 10/(12&minus;10) = 5 patients; L<sub>Q</sub> = 100/(12&times;2) = 4.167; W<sub>S</sub> = 30 min. Cost/hr = 150&times;5 + 300 = <b>Rs 1,050</b>.",
 "<b>Option B &mdash; two clerks (M/M/2):</b> &rho; = 10/24 = 0.4167; r = 0.8333. P<sub>0</sub> = 1/[1 + 0.8333 + 0.8333<sup>2</sup>/(2&times;0.5833)] = 1/[1.8333 + 0.5952] = 0.4118. L<sub>Q</sub> = 0.8333<sup>3</sup>&times;0.4118/[(2&minus;0.8333)<sup>2</sup>&times;1] = 0.5787&times;0.4118/1.3611 = 0.1751. W<sub>Q</sub> = 1.05 min. L<sub>S</sub> = 0.1751 + 0.8333 = 1.0084; W<sub>S</sub> = 6.05 min. Cost/hr = 150&times;1.0084 + 600 = <b>Rs 751.3</b>.",
 "Saving = 1,050 &minus; 751.3 = <b>Rs 298.7/hr &asymp; Rs 2,390/day</b>. (Using L<sub>Q</sub> instead of L<sub>S</sub> gives the same saving, because L<sub>S</sub>&minus;L<sub>Q</sub> = &lambda;/&mu; is identical for both.)",
 ans="Yes, hire the second clerk: saves &asymp; Rs 299/hr (&asymp; Rs 2,390/day); patient time in registration drops from 30 min to 6 min."))
A('<h4>Simulation-style question: compute waiting times from an arrival table (class practice)</h4>')
A(EX("Example 2.10 &mdash; Waiting from a table (class practice A&ndash;I)", "Moderate",
 "Arrivals (clock minutes after 08:00) and service times: A 08:01 (2), B 08:07 (10), C 08:09 (4), D 08:20 (13), E 08:31 (9), F 08:39 (2), G 08:40 (7), H 08:52 (5), I 08:54 (3). Find each customer&rsquo;s wait and the total for (a) one teller, (b) two tellers.",
 "Rule: <b>start = max(arrival, time server becomes free)</b>; wait = start &minus; arrival; free-time = start + service. With two tellers send the customer to whichever is free first.",
 T(["Cust", "Arrive", "Serv", "Start (1 teller)", "Wait", "Leaves", "Start (2 tellers)", "Wait"], [
  ["A","08:01","2","08:01","0","08:03","08:01","0"],["B","08:07","10","08:07","0","08:17","08:07","0"],
  ["C","08:09","4","08:17","8","08:21","08:09","0"],["D","08:20","13","08:21","1","08:34","08:20","0"],
  ["E","08:31","9","08:34","3","08:43","08:31","0"],["F","08:39","2","08:43","4","08:45","08:39","0"],
  ["G","08:40","7","08:45","5","08:52","08:40","0"],["H","08:52","5","08:52","0","08:57","08:52","0"],
  ["I","08:54","3","08:57","3","09:00","08:54","0"]], num=(2,4)),
 "Total workload = 2+10+4+13+9+2+7+5+3 = <b>55 min</b>; capacity 60 min (1 teller) or 120 min (2 tellers).",
 ans="One teller: total wait = <b>24 min</b> (8+1+3+4+5+0+3). Two tellers: total wait = <b>0</b>."))
A('<p class="small">Try yourself: redo Example 2.6 with &lambda; = 12/hr, &mu; = 5/hr for c = 3 and c = 4 and find the cheapest c if a teller costs Rs 200/hr and waiting costs Rs 300 per customer-hour in the queue.</p>')
A('</section>')

# ---------------- PART 3 ----------------
A('<section class="part" id="p3"><span class="tag">Part 3</span><h2>Revenue &amp; Yield Management</h2><p class="sub">Selling the right product to the right customer at the right time, through the right channel, at the right price.</p>')
A('<h3>3.1 Concepts</h3>')
A(UL("<b>Definition:</b> using pricing to increase the profit generated from limited (perishable) assets.",
 "<b>Works best when:</b> value differs across segments (business vs vacationers); the product is perishable (seats, rooms); demand has seasonality/peaks; services are sold in advance. Core dilemma: <i>accept an early discounted booking or hold the unit for a late high-paying customer?</i>",
 "<b>Traditional pricing</b> (Total revenue = P&times;Q on one demand curve) ignores segments with inelastic demand (business traveller booking last minute).",
 "<b>Fare classes (airlines):</b> Corporate (buy any time, fully refundable/changeable), Vacationers (&ge; 2 weeks advance, non-refundable), Internet special (when flight not expected full, non-refundable).",
 "<b>Two questions RM answers:</b> how to differentiate segments so one pays more, and how to stop the low-fare segment consuming all capacity (&rarr; <b>capacity protection</b>).",
 "<b>Overbooking</b> applies when capacity is fixed &amp; perishable and customers cancel/no-show. Denied service &rarr; airlines compensate/re-accommodate; hotels re-accommodate at other hotels; air cargo re-books; clinics use overtime."))
A('<h3>3.2 Formula boxes</h3>')
A(F("Critical ratio (newsvendor logic)", "C<sub>u</sub> = cost of <i>under</i>-protecting/under-booking ;; C<sub>o</sub> = cost of <i>over</i>-protecting/over-booking", "CR = {{C<sub>u</sub>|C<sub>u</sub> + C<sub>o</sub>}} ;; Q* = &mu; + z&sigma;  where  P(X &le; Q*) = CR   (z from normal table)"))
A(F("Littlewood&rsquo;s rule (capacity protection for the high fare)",
 "Protect the next seat for the high fare while F<sub>H</sub> &times; P(D<sub>H</sub> &gt; Q) &gt; F<sub>L</sub>",
 "At the optimum: P(D<sub>H</sub> &gt; Q*) = {{F<sub>L</sub>|F<sub>H</sub>}}  &hArr;  P(D<sub>H</sub> &le; Q*) = {{F<sub>H</sub> &minus; F<sub>L</sub>|F<sub>H</sub>}} = CR",
 "C<sub>u</sub> = F<sub>H</sub> &minus; F<sub>L</sub> (protected too few &rarr; sold a seat cheap that could earn F<sub>H</sub>) ;; C<sub>o</sub> = F<sub>L</sub> (protected too many &rarr; seat empty, could have earned F<sub>L</sub>)",
 "Q* = &mu;<sub>H</sub> + z&sigma;<sub>H</sub> = seats to <b>protect</b> for high fare &nbsp;&rArr;&nbsp; max low-fare seats to sell = Capacity &minus; Q*",
 "&sigma; = &radic;variance. &ldquo;CR probability = 1 &minus; Littlewood probability&rdquo;: Littlewood probability = P(D<sub>H</sub> &gt; Q) = F<sub>L</sub>/F<sub>H</sub>."))
A(F("Overbooking",
 "Let X = number of no-shows (or no-show %). Overbook by q where P(X &le; q) &ge; CR",
 "C<sub>u</sub> = cost when a booked customer <b>doesn&rsquo;t show</b> and the room/seat goes empty (lost contribution) ;; C<sub>o</sub> = cost when someone <b>shows and is denied</b> (compensation + goodwill)",
 "CR = {{C<sub>u</sub>|C<sub>u</sub> + C<sub>o</sub>}} ;; q* = &mu;<sub>no-show</sub> + z&sigma;<sub>no-show</sub> (normal)  or  smallest q with cumulative P(X&le;q) &ge; CR (discrete table)"))
A(F("Multi-segment pricing &mdash; uncapacitated",
 "Demand of segment i: d<sub>i</sub> = A<sub>i</sub> &minus; B<sub>i</sub>p<sub>i</sub> ;; unit cost c",
 "Profit = &sum;(p<sub>i</sub> &minus; c)(A<sub>i</sub> &minus; B<sub>i</sub>p<sub>i</sub>)",
 "Optimal price: p<sub>i</sub>* = {{A<sub>i</sub>|2B<sub>i</sub>}} + {{c|2}}   (set d(profit)/dp = 0)"))
A(F("Multi-segment pricing &mdash; capacitated (total capacity Q)",
 "Max &sum;(p<sub>i</sub> &minus; c)(A<sub>i</sub> &minus; B<sub>i</sub>p<sub>i</sub>) &nbsp; s.t. &nbsp; &sum;(A<sub>i</sub> &minus; B<sub>i</sub>p<sub>i</sub>) &le; Q, &nbsp; A<sub>i</sub> &minus; B<sub>i</sub>p<sub>i</sub> &ge; 0",
 "<b>Step 1:</b> compute uncapacitated demand. If &sum;d<sub>i</sub> &le; Q &rarr; constraint slack, use the uncapacitated prices.",
 "<b>Step 2 (binding):</b> replace c by s = c + &lambda; (shadow price): p<sub>i</sub> = {{A<sub>i</sub>|2B<sub>i</sub>}} + {{s|2}}. Demand d<sub>i</sub> = {{A<sub>i</sub>|2}} &minus; {{B<sub>i</sub>s|2}}",
 "Solve &sum;d<sub>i</sub> = Q: &nbsp; s = {{&sum;A<sub>i</sub>/2 &minus; Q|&sum;B<sub>i</sub>/2}} &nbsp; &rArr; &nbsp; shadow price &lambda; = s &minus; c",
 "Profit computed with the <i>true</i> cost c (not s)."))
A('<p class="small">Same-price (single segment) benchmark: add demand curves d = &sum;A &minus; (&sum;B)p and apply p = A/(2B) + c/2 to the aggregate.</p>')
A('<h3>3.3 Solved examples</h3>')
A(EX("Example 3.1 &mdash; Littlewood (class: budget airline)", "Moderate",
 "Full-fare and internet-special return tickets cost Rs 6,900 and Rs 4,900. Aircraft has 95 seats; ample demand for the internet special. Full-fare demand ~ Normal(mean 60, variance 225). How many internet-special tickets should be sold at most?",
 "F<sub>H</sub> = 6900, F<sub>L</sub> = 4900. C<sub>u</sub> = 2000, C<sub>o</sub> = 4900. CR = 2000/6900 = <b>0.2899</b>.",
 "&sigma; = &radic;225 = 15. Find z with P(Z &le; z) = 0.2899 &rArr; z &asymp; <b>&minus;0.55</b> (z-table: 0.2912 at &minus;0.55; exact &minus;0.554).",
 "Q* = 60 + (&minus;0.554)(15) = 60 &minus; 8.3 = <b>51.7 &rarr; protect 52 seats</b> for full fare.",
 "Max internet specials = 95 &minus; 52 = <b>43</b>.",
 "<i>Sanity check:</i> F<sub>L</sub>/F<sub>H</sub> = 0.71 &rArr; we protect only until there is a 71% chance of selling the marginal seat at full fare, so Q* is below the mean (51.7 &lt; 60).",
 ans="Protect &asymp; 52 seats for full fare; sell at most 43 internet-special tickets."))
A(EX("Example 3.2 &mdash; Hotel protection level (class)", "Moderate",
 "Hotel has 120 rooms. Corporate Flex Rate Rs 10,000; Advance Saver Rs 2,000 (sells out). Flex demand ~ Normal(70, variance 225). How many rooms to protect for Flex and what is the max number of Advance Saver bookings?",
 "CR = (10000&minus;2000)/10000 = <b>0.80</b> &rArr; z = <b>+0.84</b>. &sigma; = 15.",
 "Q* = 70 + 0.84(15) = 70 + 12.6 = <b>82.6 &rarr; protect 83 rooms</b>.",
 "Advance Saver limit = 120 &minus; 83 = <b>37 rooms</b>.",
 "Note the direction: high fare is ~5&times; the low fare, so the hotel protects <i>more</i> than the mean (z &gt; 0). Always check the sign of z against F<sub>L</sub>/F<sub>H</sub>: if F<sub>L</sub>/F<sub>H</sub> &lt; 0.5 then Q* &gt; &mu;.",
 ans="Protect 83 rooms for Flex; accept at most 37 Advance Saver bookings."))
A(EX("Example 3.3 &mdash; Overbooking with normal no-shows (class hotel)", "Moderate",
 "Historically 30% no-shows, variance 9 (%<sup>2</sup>, so &sigma; = 3%). Cost of an empty room from a no-show = Rs 3,200; cost when a booked guest shows and there is no room = Rs 8,000. Extent of overbooking?",
 "C<sub>u</sub> = 3200 (no-show &rarr; empty room), C<sub>o</sub> = 8000 (denied guest). CR = 3200/11200 = <b>0.2857</b> &rArr; z = <b>&minus;0.57</b>.",
 "q* = 30% + (&minus;0.57)(3%) = 30% &minus; 1.7% = <b>&asymp; 28.3%</b>.",
 "Interpretation: plan overbooking around a 28.3% no-show level (class treatment: overbooking extent q* = 28.3%). Being cautious (below the 30% mean) is right because a denied guest costs 2.5&times; an empty room. If the exam gives a room count, state your reading: e.g. covering 28.3% expected no-shows on N booked rooms means accepting N bookings for N(1&minus;0.283) rooms of capacity.",
 "<i>Be ready for the exam wording:</i> if variance were given as 0.09 for a proportion, &sigma; = 0.3 &mdash; state your interpretation.",
 ans="Overbook to about 28.3% no-shows (z &asymp; &minus;0.57): a conservative level because C<sub>o</sub> &gt; C<sub>u</sub>."))
A(EX("Example 3.4 &mdash; Overbooking from a discrete table (class)", "Moderate",
 "No-show distribution P(d): 0 &rarr; .07, 1 &rarr; .19, 2 &rarr; .22, 3 &rarr; .16, 4 &rarr; .12, 5 &rarr; .10, 6 &rarr; .07, 7 &rarr; .04, 8 &rarr; .02, 9 &rarr; .01. C<sub>u</sub> = $40 (room contribution lost when a reservation is not honoured, i.e., no-shows underestimated). C<sub>o</sub> = $100 (cost of not having a room for an overbooked guest). How many reservations to overbook?",
 "CR = 40/(40+100) = <b>0.2857</b>.",
 T(["q", "0", "1", "2", "3", "4", "5", "6"], [["P(d)", ".07", ".19", ".22", ".16", ".12", ".10", ".07"], ["Cumulative P(d &le; q)", ".07", ".26", "<b>.48</b>", ".64", ".76", ".86", ".93"]]),
 "Smallest q with cumulative &ge; 0.2857 is q = <b>2</b> (0.26 &lt; 0.2857 &le; 0.48).",
 "<i>Cross-check by marginal analysis:</i> the 2nd overbooked booking is worth it if 40&times;P(no-shows &ge; 2) &gt; 100&times;P(no-shows &lt; 2): 40(0.74) = 29.6 &gt; 100(0.26) = 26 &#10003;. The 3rd: 40(0.52) = 20.8 &lt; 100(0.48) = 48 &#10007;.",
 ans="Overbook by 2 reservations."))
A(EX("Example 3.5 &mdash; Two-segment pricing (class)", "Moderate",
 "d<sub>1</sub> = 5000 &minus; 20p<sub>1</sub>; d<sub>2</sub> = 5000 &minus; 40p<sub>2</sub>; c = Rs 10. (a) Optimal prices and total profit. (b) What if one single price is forced? (c) Capacity Q = 4,000.",
 "(a) p<sub>1</sub> = 5000/(2&times;20) + 10/2 = 125 + 5 = <b>Rs 130</b>; p<sub>2</sub> = 5000/80 + 5 = 62.5 + 5 = <b>Rs 67.5</b>.",
 "d<sub>1</sub> = 5000 &minus; 2600 = 2,400; d<sub>2</sub> = 5000 &minus; 2700 = 2,300 (total 4,700). Profit = (130&minus;10)(2400) + (67.5&minus;10)(2300) = 288,000 + 132,250 = <b>Rs 420,250</b>.",
 "(b) Aggregate demand d = 10000 &minus; 60p &rArr; p = 10000/120 + 5 = <b>Rs 88.33</b>; d = 4,700; profit = (78.33)(4700) = <b>Rs 368,167</b>. Price discrimination gains 420,250 &minus; 368,167 = <b>Rs 52,083</b> (+14.1%).",
 "(c) Uncapacitated demand 4,700 &gt; 4,000 &rArr; constraint <b>binds</b>. s = (&sum;A/2 &minus; Q)/(&sum;B/2) = (5000 &minus; 4000)/30 = <b>33.33</b> (so &lambda; = s &minus; c = 23.33 per unit).",
 "p<sub>1</sub> = 125 + 16.67 = <b>Rs 141.67</b>; p<sub>2</sub> = 62.5 + 16.67 = <b>Rs 79.17</b>. d<sub>1</sub> = 5000 &minus; 20(141.67) = 2,166.7; d<sub>2</sub> = 5000 &minus; 40(79.17) = 1,833.3; total = 4,000 &#10003;.",
 "Profit = (141.67&minus;10)(2166.7) + (79.17&minus;10)(1833.3) = 285,278 + 126,806 = <b>Rs 412,083</b>. Both prices rise; the capacity limit costs Rs 8,167 relative to unlimited capacity.",
 ans="(a) Rs 130 / Rs 67.5, profit Rs 420,250  (b) single price Rs 88.33, profit Rs 368,167  (c) Rs 141.67 / Rs 79.17, profit Rs 412,083"))
A(EX("Example 3.6 &mdash; Three-segment capacitated pricing", "Difficult",
 "A conference venue sells to three segments: d<sub>1</sub> = 3000 &minus; 10p<sub>1</sub>, d<sub>2</sub> = 2000 &minus; 10p<sub>2</sub>, d<sub>3</sub> = 1500 &minus; 5p<sub>3</sub>. Cost per unit c = 20. Capacity = 2,500 units. Find prices, allocation, profit, and the value of one extra unit of capacity.",
 "<b>Uncapacitated:</b> p<sub>1</sub> = 3000/20 + 10 = 160; p<sub>2</sub> = 2000/20 + 10 = 110; p<sub>3</sub> = 1500/10 + 10 = 160. Demands 1,400 + 900 + 700 = <b>3,000 &gt; 2,500 &rarr; binds</b>.",
 "&sum;A/2 = (3000+2000+1500)/2 = 3250; &sum;B/2 = (10+10+5)/2 = 12.5. s = (3250 &minus; 2500)/12.5 = <b>60</b> &rArr; &lambda; = 60 &minus; 20 = <b>40</b>.",
 "Prices: p<sub>1</sub> = 150 + 30 = <b>180</b>; p<sub>2</sub> = 100 + 30 = <b>130</b>; p<sub>3</sub> = 150 + 30 = <b>180</b>.",
 "Demands: d<sub>1</sub> = 3000 &minus; 1800 = 1,200; d<sub>2</sub> = 2000 &minus; 1300 = 700; d<sub>3</sub> = 1500 &minus; 900 = 600. Total = 2,500 &#10003;.",
 "Profit = (180&minus;20)(1200) + (130&minus;20)(700) + (180&minus;20)(600) = 192,000 + 77,000 + 96,000 = <b>365,000</b> (vs 375,000 if capacity were unlimited).",
 "The shadow price &lambda; = 40 says one extra unit of capacity is worth about 40 of extra profit.",
 ans="p = 180 / 130 / 180; allocation 1,200 / 700 / 600; profit 365,000; capacity worth &asymp; 40 per unit."))
A(EX("Example 3.7 &mdash; Protection level with a very low discount fare (variation)", "Moderate-Difficult",
 "Flight of 150 seats. F<sub>H</sub> = Rs 12,000, F<sub>L</sub> = Rs 3,000. High-fare demand ~ Normal(&mu; = 45, &sigma; = 12). (a) Seats to protect; (b) max discount seats; (c) what happens to Q* if F<sub>L</sub> rises to Rs 8,000?",
 "(a) CR = (12000&minus;3000)/12000 = <b>0.75</b> &rArr; z = 0.67. Q* = 45 + 0.67(12) = 45 + 8.04 = <b>53.0 &rarr; protect 53</b>.",
 "(b) Discount seats = 150 &minus; 53 = <b>97</b>.",
 "(c) CR = (12000&minus;8000)/12000 = 0.333 &rArr; z = &minus;0.43. Q* = 45 &minus; 0.43(12) = 45 &minus; 5.2 = <b>39.8 &rarr; 40</b>. When the discount fare gets closer to the full fare, protecting a seat is less attractive, so we protect fewer seats.",
 ans="(a) 53  (b) 97  (c) protect 40 (fewer)"))
A('<h3>3.4 Competition in revenue management (game theory: concepts)</h3>')
A(T(["Approach", "When to use", "Pros", "Cons", "Examples"], [
 ["<b>Nash</b> (simultaneous)", "Symmetric/fragmented market; move at the same time; transparent prices (OTAs); no clear leader", "Stable equilibrium; fair share; easy", "Thin margins; reactive; no leadership edge", "Uber vs Ola surge, Swiggy vs Zomato, budget hotels on OTAs"],
 ["<b>Stackelberg</b> (leader&ndash;follower)", "Clear leader; first-mover advantage; followers must adapt (residual demand)", "Leader captures premium demand, anticipates follower; higher leader profit", "Followers earn less; needs foresight; leader may miscalculate", "Marriott/Taj advance rates, IndiGo hubs, McKinsey fees, Jio entry"],
 ["<b>Collaboration</b>", "High fixed &amp; perishable capacity; few large players; price wars destroy value", "Higher joint profits; stable pricing", "Needs trust &amp; enforcement; may reduce innovation", "Airline alliances, tower sharing, rate-parity agreements, referral networks"]]))
A(UL("<b>Nash:</b> both set prices/room allocations at the same time without seeing the other&rsquo;s choice; equilibrium = neither can improve by changing alone.",
 "<b>Stackelberg:</b> the leader sets first (e.g., advance-booking protection levels), the follower adjusts optimally; the leader shapes residual demand."))
A('</section>')

# ---------------- PART 4 ----------------
A('<section class="part" id="p4"><span class="tag">Part 4</span><h2>Service Facility Layout (slide 47 onwards)</h2><p class="sub">Product layout, process layout, line balancing, bottlenecks, labour utilisation and cost of capacity.</p>')
A('<h3>4.1 Concepts</h3>')
A(UL("<b>Product layout</b> (line flow, like a vehicle assembly line: chassis drop &rarr; engine mounting &rarr; cab mounting &rarr; &hellip;). Used for <b>high volume, low variety</b>: standardised service to many customers (cafeteria line, airport security). Customer is an input moving through stations.",
 "<b>Process layout</b>: functional departments; customers route differently (retail shop, hospital) &rarr; for high variety, low volume.",
 "<b>McDonald&rsquo;s innovations:</b> indoor seating (1950s), drive-through (1970s), breakfast (1980s), play areas (late 1980s), self-service kiosk (2004). <b>4 of 5 concern layout.</b>",
 "<b>Service design factors:</b> (a) objective of service (emergency ward: no traffic, easy approach; petrol pump: bright colour visible from afar); (b) space requirement &amp; location (rural vs urban &rarr; vertical expansion); (c) security (CCTV, biometrics at immigration); (d) flexibility (adapt to new equipment, expansion provision).",
 "<b>Mongolian Grill:</b> customers assemble their own bowls at open-grill/food-prep stations. Objective: raise capacity and throughput with self-service. Result: higher profit; small bottlenecks (&le; 2 min) cleared by cooks directing traffic; repeat customers who understand queues walk to the <i>farthest</i> prep area first and reduce bottlenecks &mdash; customer behaviour affects service quality/flow.",
 "<b>Bottleneck strategy:</b> add parallel workers/equipment at the slowest station, or re-split the tasks, to balance the line &mdash; but every extra worker adds cost, so compare <b>cost per customer</b>."))
A('<h3>4.2 Formula boxes (from the sheet, page 3)</h3>')
A(F("Line balancing formulas",
 "Capacity (per station) = {{Available time|Processing time}}   e.g. 3600 s/hr &divide; time per customer",
 "Station capacity = No. of parallel workers &times; individual capacity ;; Effective processing time = {{Processing time|No. of parallel workers}}",
 "<b>Process capacity = capacity of the bottleneck</b> = min over stations = 3600 / max(effective time)  (= 3600/cycle time)",
 "Ideal cycle time = {{Labour content|No. of workers}}   (perfectly balanced) ;; Labour content = sum of all task times",
 "Labour utilisation (%) = {{Labour content|Cycle time &times; No. of workers}} &times; 100  (cycle time = bottleneck time)",
 "Cost of capacity: cost per customer = {{(No. of workers) &times; (wage per hr)|Process capacity per hr}}"))
A(W("Method", "1) Convert times to a common unit (seconds). 2) Effective time of each station = time &divide; workers. 3) Bottleneck = largest effective time &rArr; cycle time. 4) Capacity/hr = 3600/cycle time. 5) Utilisation = labour content / (cycle time &times; total workers). 6) Cost per customer = workers &times; wage / capacity. 7) Recommend on <b>cost per customer</b> and whether capacity meets demand."))
A('<h3>4.3 Solved examples</h3>')
A(EX("Example 4.1 &mdash; Cafeteria line (class)", "Moderate",
 "Four stations, 1 worker each: drinks 20 s, starters &amp; soup 30 s, main course 40 s, dessert 15 s. Lunch window 1 hr. (a) Capacity and utilisation as-is. (b) Ideal balanced line? (c) Option: double the main-course station.",
 "Labour content = 20+30+40+15 = <b>105 s</b>. 4 workers.",
 "<b>(a) As-is:</b> bottleneck = main course 40 s &rArr; cycle time 40 s &rArr; capacity = 3600/40 = <b>90 customers/hr</b>. Station capacities: 180, 120, 90, 240. Utilisation = 105/(40&times;4) = <b>65.63%</b>.",
 "<b>(b) Ideal:</b> cycle = 105/4 = <b>26.25 s</b> each &rArr; capacity 3600/26.25 = <b>137.14/hr</b>, utilisation <b>100%</b> (theoretical; tasks rarely divide perfectly).",
 "<b>(c) Two workers at main course</b> (effective 20 s): times 20, 30, 20, 15 &rArr; bottleneck 30 s (starters) &rArr; capacity = <b>120/hr</b>; 5 workers: utilisation = 105/(30&times;5) = <b>70%</b>.",
 "Cost effect: workers 4 &rarr; 5 (+25%), capacity 90 &rarr; 120 (+33%) &rArr; cost per customer <i>falls</i> (4X/90 = 0.0444X vs 5X/120 = 0.0417X). Next bottleneck is starters &mdash; add a worker there only if demand &gt; 120/hr.",
 ans="As-is: 90/hr, 65.63%. Ideal: 137.14/hr, 100%. With 2 at main: 120/hr, 70%, cheaper per customer."))
A(EX("Example 4.2 &mdash; Airport security checkpoint (class: proposal question)", "Difficult",
 "Four sequential activities, 1 employee each at Rs 400/hr: document verification 24 s, baggage screening 38 s, security check 40 s, exit verification 20 s. Evaluate these proposals: (P1) add one more employee at security check; (P2) add one more at baggage screening <b>and</b> one more at security check. Should management implement?",
 "<b>Base:</b> labour content = 24+38+40+20 = <b>122 s</b>; bottleneck 40 s &rArr; capacity 3600/40 = <b>90/hr</b>; 4 workers cost 1,600/hr &rArr; <b>Rs 17.78 per passenger</b>; utilisation = 122/(40&times;4) = <b>76.25%</b>.",
 "<b>P1 (security check &times; 2):</b> effective times 24, 38, 20, 20 &rArr; new bottleneck = baggage 38 s &rArr; capacity = 3600/38 = <b>94.74/hr</b>; 5 workers = 2,000/hr &rArr; <b>Rs 21.11/passenger</b> (worse); utilisation = 122/(38&times;5) = 64.2%. <b>Reject P1</b> &mdash; only a 5% capacity gain for 25% more labour.",
 "<b>P2 (baggage &times; 2 and security &times; 2):</b> effective times 24, 19, 20, 20 &rArr; bottleneck = document verification 24 s &rArr; capacity = 3600/24 = <b>150/hr</b>; 6 workers = 2,400/hr &rArr; <b>Rs 16.00/passenger</b>; utilisation = 122/(24&times;6) = <b>84.72%</b>. <b>Accept P2</b>: +67% capacity for +50% labour, and cheaper per passenger.",
 "<i>Extra:</i> adding a 7th worker at document verification (12 s effective) leaves bottleneck at 20 s &rArr; 180/hr, 7 workers &rArr; Rs 15.56/pax, utilisation 87.14% &mdash; still cheaper per passenger if demand exists.",
 ans="Reject P1 (Rs 21.11/pax); implement P2 (Rs 16.00/pax, 150/hr vs 90/hr). Decide with cost per customer AND demand."))
A(EX("Example 4.3 &mdash; Sizing workers to meet demand", "Moderate-Difficult",
 "A three-station service line: verification 30 s, processing 45 s, delivery 20 s. Target throughput = 100 customers/hr. How many workers per station? Capacity and utilisation?",
 "Required cycle time = 3600/100 = <b>36 s</b> per customer.",
 "Workers needed per station = &lceil;time / 36&rceil;: verification &lceil;30/36&rceil; = <b>1</b>; processing &lceil;45/36&rceil; = <b>2</b> (effective 22.5 s); delivery &lceil;20/36&rceil; = <b>1</b>. Total workers = 4.",
 "Effective times 30, 22.5, 20 &rArr; bottleneck = verification 30 s &rArr; capacity = 3600/30 = <b>120/hr</b> (&ge; 100 &#10003;).",
 "Labour content = 30+45+20 = 95 s. Utilisation = 95/(30&times;4) = <b>79.17%</b>. At the target of 100/hr (36 s cycle), labour actually needed = 95/36 = 2.64 workers, so idle labour is unavoidable with discrete workers.",
 ans="1 + 2 + 1 workers; capacity 120/hr; utilisation 79.2%."))
A(EX("Example 4.4 &mdash; Which layout, and why?", "Concept",
 "Why did the cafeteria use a product layout, and how does it differ from a retail shop?",
 "Cafeteria: standard service, high volume in a 1-hour lunch window &rarr; stations arranged in the sequence of service (drinks &rarr; starters &rarr; main &rarr; dessert); efficiency comes from balancing station times; the <i>customer is an input</i> moving along the line. Retail shop: many product categories and customers choose their own route &rarr; process (functional) layout; high variety, low volume.",
 ans="High volume + low variety &rArr; product layout; high variety + low volume &rArr; process layout."))
A('</section>')

# ---------------- PART 5 ----------------
A('<section class="part" id="p5"><span class="tag">Part 5</span><h2>Exam Plan &amp; Checklists</h2>')
A('<h3>2-hour time plan (adapt to marks)</h3>')
A(T(["Minutes", "What to do"], [
 ["0&ndash;5", "Read the whole paper. Mark easy points. Note which model each queue question is."],
 ["5&ndash;55", "Queuing questions (biggest weight). Write givens in per-hour units first."],
 ["55&ndash;90", "Revenue questions. Identify CR, z, &sigma; (root of variance), then the number. For pricing: p = A/2B + c/2, check capacity binding."],
 ["90&ndash;110", "Layout questions: effective times &rarr; bottleneck &rarr; capacity &rarr; utilisation &rarr; cost per customer."],
 ["110&ndash;120", "Theory answers + re-check units, rounding, and that each answer states a <b>decision</b>."]]))
A('<h3>Standard pitfalls</h3>')
A('<ul class="check"><li>&lambda; and &mu; in the same unit and <b>per hour</b>. &ldquo;Every 3 min&rdquo; is arrival <i>interval</i> &rArr; &lambda; = 20/hr.</li>'
  '<li>Check &rho; &lt; 1 for infinite-queue models. If &rho; &ge; 1, say the queue grows without bound.</li>'
  '<li>M/M/1/N: N counts the customer in service. Use &lambda;<sub>eff</sub> for W. &rho; may exceed 1.</li>'
  '<li>M/M/c: P<sub>0</sub> uses &sum; up to c&minus;1 and the last term with (1&minus;&rho;); L<sub>Q</sub> uses r = &lambda;/&mu;.</li>'
  '<li>&ldquo;% time no queue&rdquo; = P<sub>0</sub> + P<sub>1</sub>, not P<sub>0</sub> alone.</li>'
  '<li>Cost questions: waiting cost uses L<sub>Q</sub> if time <i>in queue</i>, L<sub>S</sub> if <i>in system</i>. Compare on the same basis (per hour or per day).</li>'
  '<li>Littlewood: Q* is seats <b>protected</b> for high fare; discount seats = capacity &minus; Q*. Use &sigma; = &radic;variance.</li>'
  '<li>Overbooking: identify which cost is C<sub>u</sub> (empty room / no-show) and which is C<sub>o</sub> (denied guest). Swapping them flips the answer.</li>'
  '<li>Pricing: check whether capacity binds by summing the uncapacitated demands first. Profit uses true c.</li>'
  '<li>Layout: cycle time = bottleneck <i>effective</i> time; utilisation denominator uses total workers (including extra ones).</li>'
  '<li>Round protection levels/workers sensibly and state the rounding; always give a one-line recommendation.</li></ul>')
A('<h3>One-page formula recap</h3>')
A(T(["Topic", "Key formulas"], [
 ["M/M/1", "&rho;=&lambda;/&mu;; P<sub>0</sub>=1&minus;&rho;; P<sub>n</sub>=&rho;<sup>n</sup>P<sub>0</sub>; L<sub>S</sub>=&lambda;/(&mu;&minus;&lambda;); L<sub>Q</sub>=&lambda;<sup>2</sup>/[&mu;(&mu;&minus;&lambda;)]; W<sub>S</sub>=1/(&mu;&minus;&lambda;); W<sub>Q</sub>=&lambda;/[&mu;(&mu;&minus;&lambda;)]; L=&lambda;W"],
 ["M/M/1/N", "P<sub>0</sub>=(1&minus;&rho;)/(1&minus;&rho;<sup>N+1</sup>); P<sub>N</sub>=&rho;<sup>N</sup>P<sub>0</sub>; &lambda;<sub>eff</sub>=&lambda;(1&minus;P<sub>N</sub>); L<sub>Q</sub>=L<sub>S</sub>&minus;&lambda;<sub>eff</sub>/&mu;; W=L/&lambda;<sub>eff</sub>"],
 ["M/M/c", "&rho;=&lambda;/(c&mu;); r=&lambda;/&mu;; P<sub>0</sub> formula; L<sub>Q</sub>=r<sup>c+1</sup>P<sub>0</sub>/[(c&minus;r)<sup>2</sup>(c&minus;1)!]; W<sub>Q</sub>=L<sub>Q</sub>/&lambda;; W<sub>S</sub>=W<sub>Q</sub>+1/&mu;; L<sub>S</sub>=&lambda;W<sub>Q</sub>+&lambda;/&mu;"],
 ["M/D/1", "L<sub>Q</sub>=&lambda;<sup>2</sup>/[2&mu;(&mu;&minus;&lambda;)]; W<sub>Q</sub>=&lambda;/[2&mu;(&mu;&minus;&lambda;)]; L<sub>S</sub>=L<sub>Q</sub>+&lambda;/&mu;; W<sub>S</sub>=W<sub>Q</sub>+1/&mu;"],
 ["Queue economics", "Total cost = server cost + waiting cost (c<sub>w</sub>&times;L or W); choose minimum"],
 ["Littlewood / CR", "C<sub>u</sub>=F<sub>H</sub>&minus;F<sub>L</sub>; C<sub>o</sub>=F<sub>L</sub>; CR=(F<sub>H</sub>&minus;F<sub>L</sub>)/F<sub>H</sub>; Q*=&mu;+z&sigma;; discount seats=Cap&minus;Q*"],
 ["Overbooking", "CR=C<sub>u</sub>/(C<sub>u</sub>+C<sub>o</sub>), C<sub>u</sub>=empty-room loss, C<sub>o</sub>=denied-guest cost; q*=&mu;+z&sigma; or smallest q with cum. P&ge;CR"],
 ["Pricing", "p=A/(2B)+c/2; capacitated: s=(&sum;A/2&minus;Q)/(&sum;B/2), p=A/(2B)+s/2, &lambda;=s&minus;c"],
 ["Layout", "Capacity=time/processing time; eff. time=t/workers; cycle=max eff. time; ideal cycle=labour content/workers; util=LC/(cycle&times;workers)"]]))
A('</section>')
