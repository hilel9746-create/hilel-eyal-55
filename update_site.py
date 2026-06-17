import re

# Update index.html
with open('/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/index.html', 'r') as f:
    html = f.read()

new_content = """<!-- ══ HERO ══ -->
<div class="hero-d5">
  <div class="hero-left-d5">
    <div class="h-eyebrow-d5">Ohio's Direct Cash Home Buyer</div>
    <h1>Sell Your Home.<br><em>Skip the</em><br>Hassle.</h1>
    <p class="h-desc-d5">As-is. No repairs, no fees, no agent commissions. A direct cash offer and closing on the date you choose.</p>

    <div class="owner-card-d5">
      <img src="https://cashbuyersohio.net/assets/images/hero-owner-professional.png" alt="Hilel" class="owner-thumb-d5"/>
      <div class="owner-info-d5">
        <div class="owner-name-d5">Hilel — Founder &amp; Owner</div>
        <div class="owner-role-d5">Hilel 1 LLC · Direct Buyer</div>
        <div class="owner-quote-d5">"You deal with me personally from first call to closing — no call centers, no middlemen."</div>
      </div>
    </div>

    <div class="hero-btns-d5">
      <a href="appointment.html" class="btn-main-d5">💰 Get My Cash Offer</a>
      <a href="about.html" class="btn-outline-d5">Learn More ↓</a>
    </div>

    <div class="trust-row-d5">
      <div class="trust-item-d5">Cash Offer in 24 Hours</div>
      <div class="trust-item-d5">Close in 7–14 Days</div>
      <div class="trust-item-d5">Zero Agent Fees</div>
      <div class="trust-item-d5">No Repairs Needed</div>
    </div>
  </div>

  <div class="hero-right-d5">
    <div class="hero-right-bg-d5">
      <div class="portrait-zone-d5">
        <img src="https://cashbuyersohio.net/assets/images/hero-owner-professional.png" alt="Hilel, Founder"/>
        <div class="portrait-overlay-d5"></div>
      </div>
      <div class="house-strip-d5">
        <div class="hs-d5"><img src="https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=400&q=80" alt="home"/></div>
        <div class="hs-d5"><img src="https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=400&q=80" alt="home"/></div>
        <div class="hs-d5"><img src="https://images.unsplash.com/photo-1449844908441-8829872d2607?w=400&q=80" alt="home"/></div>
      </div>
    </div>
    <div class="badge-float-d5">
      <div class="badge-num-d5">24h</div>
      <div class="badge-label-d5">Cash Offer</div>
    </div>
  </div>
</div>

<!-- DIVIDER -->
<div class="divider-strip-d5">
  <div class="ds-item-d5"><div class="ds-num-d5">24 Hrs</div><div class="ds-label-d5">Cash Offer</div></div>
  <div class="ds-item-d5"><div class="ds-num-d5">7–14 Days</div><div class="ds-label-d5">To Close</div></div>
  <div class="ds-item-d5"><div class="ds-num-d5">$0</div><div class="ds-label-d5">Agent Fees</div></div>
  <div class="ds-item-d5"><div class="ds-num-d5">As-Is</div><div class="ds-label-d5">No Repairs</div></div>
</div>

<!-- ABOUT -->
<div class="about-d5">
  <div class="about-img-wrap-d5 reveal-left">
    <div class="about-img-frame-d5">
      <img src="https://cashbuyersohio.net/assets/images/hero-owner-professional.png" alt="Hilel — Founder"/>
    </div>
    <div class="about-accent-d5"></div>
  </div>
  <div class="about-text-d5 reveal-right">
    <div class="about-label-d5">Who You're Dealing With</div>
    <h2>A Real Person.<br>Not a Call Center.</h2>
    <p class="about-bio-d5">I'm Hilel, owner of Hilel 1 LLC and the person who handles every single deal personally. When you call, you get me. When you sign, you sign with me. When you close, I'm there.</p>
    <ul class="about-list-d5">
      <li>Personal attention from your first call through closing</li>
      <li>Fair cash offer based on your home's actual condition</li>
      <li>Close on the date that works for your schedule</li>
      <li>No repairs, no cleaning, no showings required</li>
      <li>Full transparency — no hidden fees or last-minute changes</li>
    </ul>
  </div>
</div>

<!-- PROPERTIES -->
<div class="properties-d5">
  <div class="prop-inner-d5">
    <div class="section-header-d5 reveal">
      <div class="sec-tag-d5">Properties We Buy</div>
      <h2 class="sec-h-d5">Any Home.<br>Any Condition.</h2>
      <p class="sec-sub-d5">From move-in ready to properties needing major work — we make fair cash offers across Ohio.</p>
    </div>
    <div class="prop-grid-d5">
      <div class="pcard-d5 reveal">
        <div class="pcard-img-d5"><img src="https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=600&q=80" alt="Single family home"/></div>
        <div class="pcard-body-d5"><div class="pcard-tag-d5">Single Family</div><div class="pcard-title-d5">Move-In Ready Homes</div><div class="pcard-desc-d5">Great condition or just needs some love — we'll make a fair offer either way.</div></div>
      </div>
      <div class="pcard-d5 reveal">
        <div class="pcard-img-d5"><img src="https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=600&q=80" alt="Fixer upper"/></div>
        <div class="pcard-body-d5"><div class="pcard-tag-d5">Needs Repairs</div><div class="pcard-title-d5">Fixer-Uppers Welcome</div><div class="pcard-desc-d5">Don't spend a dollar on repairs. Sell it exactly as it sits today.</div></div>
      </div>
      <div class="pcard-d5 reveal">
        <div class="pcard-img-d5"><img src="https://images.unsplash.com/photo-1449844908441-8829872d2607?w=600&q=80" alt="Any condition"/></div>
        <div class="pcard-body-d5"><div class="pcard-tag-d5">Any Situation</div><div class="pcard-title-d5">Difficult Situations</div><div class="pcard-desc-d5">Inherited property, relocation, financial pressure — we can help.</div></div>
      </div>
    </div>
  </div>
</div>

<!-- PROCESS -->
<div class="process-d5">
  <div class="process-inner-d5">
    <div class="section-header-d5 reveal">
      <div class="sec-tag-d5">How It Works</div>
      <h2 class="sec-h-d5">Three Steps.<br>Done.</h2>
    </div>
    <div class="process-steps-d5">
      <div class="ps-d5 reveal">
        <div class="ps-num-d5">1</div>
        <div>
          <h3>Tell Me About Your Home</h3>
          <p>Call or fill out a quick form. I personally review every property — no automated systems, no pressure, no obligation.</p>
        </div>
      </div>
      <div class="ps-d5 reveal">
        <div class="ps-num-d5">2</div>
        <div>
          <h3>Get a Written Cash Offer</h3>
          <p>Within 24 hours you receive a written, no-obligation cash offer. No lowball games — a fair price based on real market data.</p>
        </div>
      </div>
      <div class="ps-d5 reveal">
        <div class="ps-num-d5">3</div>
        <div>
          <h3>Close on Your Timeline</h3>
          <p>You pick the closing date. I handle all the paperwork. Cash in your hands — in as little as 7 days or whenever you're ready.</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- CTA -->
<div class="cta-d5">
  <div class="cta-text-d5 reveal-left">
    <h2>Ready to Get<br>Your Offer?</h2>
    <p>No fees. No repairs. No waiting. Just a real conversation with a real person and a fair cash offer.</p>
  </div>
  <div class="cta-action-d5 reveal-right">
    <a href="appointment.html">Book a Call →</a>
    <div class="cta-sub-d5">No obligation · Cash offer in 24 hours</div>
  </div>
</div>
"""

html = re.sub(r'<!-- ══ HERO ══ -->.*?(?=<!-- ══ FOOTER ══ -->)', new_content, html, flags=re.DOTALL)

# Also replace the script at the bottom
new_script = """<script>
  document.getElementById('hamburger').addEventListener('click', function() {
    document.getElementById('nav-links').classList.toggle('active');
  });

  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('visible'); });
  }, {threshold: 0.1});
  document.querySelectorAll('.reveal,.reveal-left,.reveal-right').forEach(el => io.observe(el));
</script>"""

html = re.sub(r'<script>.*?hamburger.*?</script>', new_script, html, flags=re.DOTALL)

with open('/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/index.html', 'w') as f:
    f.write(html)

print("Updated index.html")
