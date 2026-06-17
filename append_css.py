css_to_append = """
/* ── DESIGN 5 SECTIONS (HOMEPAGE) ── */
@keyframes fadeLeft{from{opacity:0;transform:translateX(-24px);}to{opacity:1;transform:translateX(0);}}
@keyframes fadeRight{from{opacity:0;transform:translateX(24px);}to{opacity:1;transform:translateX(0);}}
@keyframes float{0%,100%{transform:translateY(0);}50%{transform:translateY(-8px);}}

/* HERO D5 */
.hero-d5{min-height:90vh;padding-top:40px;display:grid;grid-template-columns:1fr 1fr;overflow:hidden;background:#fafaf8;}
.hero-left-d5{padding:80px 60px;display:flex;flex-direction:column;justify-content:center;background:#fafaf8;}
.h-eyebrow-d5{font-size:0.7rem;letter-spacing:3px;text-transform:uppercase;color:#2e7d32;font-weight:700;margin-bottom:20px;display:flex;align-items:center;gap:8px;animation:fadeLeft .5s ease both;}
.h-eyebrow-d5::before{content:'';display:inline-block;width:24px;height:2px;background:#2e7d32;}
.hero-left-d5 h1{font-size:clamp(2.4rem,3.8vw,4rem);font-weight:900;line-height:1.05;letter-spacing:-2px;margin-bottom:20px;color:#1a1a1a;animation:fadeLeft .5s .1s ease both;}
.hero-left-d5 h1 em{color:#2e7d32;font-style:normal;}
.h-desc-d5{font-size:1rem;color:#666;line-height:1.8;max-width:400px;margin-bottom:32px;animation:fadeLeft .5s .2s ease both;}

.owner-card-d5{display:flex;align-items:center;gap:16px;background:#fff;border:1px solid #e8e8e4;border-radius:10px;padding:18px 22px;margin-bottom:32px;box-shadow:0 2px 16px rgba(0,0,0,0.05);animation:fadeLeft .5s .3s ease both;}
.owner-thumb-d5{width:52px;height:52px;border-radius:50%;object-fit:cover;object-position:center top;border:2px solid #2e7d32;}
.owner-info-d5{flex:1;}
.owner-name-d5{font-weight:800;font-size:0.92rem;color:#1a1a1a;}
.owner-role-d5{font-size:0.75rem;color:#888;margin-top:2px;}
.owner-quote-d5{font-style:italic;font-size:0.8rem;color:#555;margin-top:6px;line-height:1.5;}

.hero-btns-d5{display:flex;gap:12px;margin-bottom:28px;animation:fadeLeft .5s .4s ease both;}
.btn-main-d5{background:#2e7d32;color:#fff;padding:14px 28px;border-radius:4px;font-weight:700;font-size:0.92rem;text-decoration:none;transition:all .2s;display:inline-block;}
.btn-main-d5:hover{background:#1b5e20;transform:translateY(-2px);box-shadow:0 8px 20px rgba(46,125,50,0.3);}
.btn-outline-d5{border:1.5px solid #ccc;color:#555;padding:13px 24px;border-radius:4px;font-weight:600;font-size:0.88rem;text-decoration:none;transition:all .2s;display:inline-block;}
.btn-outline-d5:hover{border-color:#1a1a1a;color:#1a1a1a;}

.trust-row-d5{display:flex;gap:24px;flex-wrap:wrap;animation:fadeLeft .5s .5s ease both;}
.trust-item-d5{font-size:0.78rem;color:#888;display:flex;align-items:center;gap:6px;}
.trust-item-d5::before{content:'✓';color:#2e7d32;font-weight:900;font-size:0.9rem;}

.hero-right-d5{position:relative;background:#f0f0ec;overflow:hidden;}
.hero-right-bg-d5{position:absolute;inset:0;display:grid;grid-template-rows:65% 35%;}
.portrait-zone-d5{position:relative;overflow:hidden; height:100%;}
.portrait-zone-d5 img{width:100%;height:100%;object-fit:cover;object-position:center top;}
.portrait-overlay-d5{position:absolute;inset:0;background:linear-gradient(to bottom,transparent 50%,#f0f0ec 100%);}

.house-strip-d5{display:grid;grid-template-columns:repeat(3,1fr);gap:3px;padding:3px;}
.house-strip-d5 .hs-d5{overflow:hidden;aspect-ratio:4/3;border-radius:4px; height: 100%;}
.house-strip-d5 .hs-d5 img{width:100%;height:100%;object-fit:cover;transition:transform .5s;}
.house-strip-d5 .hs-d5:hover img{transform:scale(1.06);}

.badge-float-d5{position:absolute;top:40px;right:32px;background:#fff;border-radius:10px;padding:14px 18px;box-shadow:0 8px 32px rgba(0,0,0,0.12);text-align:center;animation:float 4s ease-in-out infinite;}
.badge-num-d5{font-size:1.6rem;font-weight:900;color:#2e7d32;line-height:1;}
.badge-label-d5{font-size:0.65rem;color:#888;text-transform:uppercase;letter-spacing:1.5px;margin-top:3px;}

.divider-strip-d5{background:#2e7d32;padding:18px 60px;display:flex;justify-content:center;gap:60px;flex-wrap:wrap;}
.ds-item-d5{text-align:center;}
.ds-num-d5{font-size:1.2rem;font-weight:900;color:#fff;}
.ds-label-d5{font-size:0.7rem;color:rgba(255,255,255,0.65);text-transform:uppercase;letter-spacing:1.5px;margin-top:2px;}

.about-d5{padding:90px 60px;background:#fff;display:grid;grid-template-columns:1fr 1fr;gap:70px;align-items:center;max-width:1200px;margin:0 auto;}
.about-img-wrap-d5{position:relative;}
.about-img-frame-d5{border-radius:3px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,0.1);}
.about-img-frame-d5 img{width:100%;display:block;object-fit:cover;object-position:center top;max-height:500px;}
.about-accent-d5{position:absolute;bottom:-20px;right:-20px;width:120px;height:120px;background:#2e7d32;border-radius:3px;z-index:-1;}
.about-label-d5{font-size:0.68rem;letter-spacing:3px;text-transform:uppercase;color:#2e7d32;font-weight:700;margin-bottom:16px;display:flex;align-items:center;gap:8px;}
.about-label-d5::before{content:'';display:inline-block;width:20px;height:2px;background:#2e7d32;}
.about-text-d5 h2{font-size:clamp(1.8rem,3vw,2.8rem);font-weight:900;letter-spacing:-1.5px;line-height:1.1;margin-bottom:20px;color:#1a1a1a;}
.about-bio-d5{color:#666;line-height:1.85;font-size:0.95rem;margin-bottom:28px;}
.about-list-d5{list-style:none;display:flex;flex-direction:column;gap:10px;padding:0;margin:0;}
.about-list-d5 li{display:flex;align-items:flex-start;gap:10px;color:#444;font-size:0.9rem;line-height:1.6;}
.about-list-d5 li::before{content:'→';color:#2e7d32;font-weight:700;flex-shrink:0;margin-top:1px;}

.properties-d5{padding:90px 60px;background:#fafaf8;}
.prop-inner-d5{max-width:1100px;margin:0 auto;}
.section-header-d5{margin-bottom:50px;}
.sec-tag-d5{font-size:0.68rem;letter-spacing:3px;text-transform:uppercase;color:#2e7d32;font-weight:700;margin-bottom:12px;display:flex;align-items:center;gap:8px;}
.sec-tag-d5::before{content:'';display:inline-block;width:20px;height:2px;background:#2e7d32;}
.sec-h-d5{font-size:clamp(1.8rem,3vw,2.8rem);font-weight:900;letter-spacing:-1.5px;color:#1a1a1a;margin-bottom:10px;}
.sec-sub-d5{color:#888;font-size:0.92rem;max-width:480px;line-height:1.7;}
.prop-grid-d5{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;}
.pcard-d5{border-radius:6px;overflow:hidden;background:#fff;box-shadow:0 2px 20px rgba(0,0,0,0.06);transition:transform .3s,box-shadow .3s;}
.pcard-d5:hover{transform:translateY(-4px);box-shadow:0 12px 40px rgba(0,0,0,0.1);}
.pcard-img-d5{aspect-ratio:4/3;overflow:hidden;}
.pcard-img-d5 img{width:100%;height:100%;object-fit:cover;transition:transform .5s;}
.pcard-d5:hover .pcard-img-d5 img{transform:scale(1.05);}
.pcard-body-d5{padding:18px 20px;}
.pcard-tag-d5{display:inline-block;background:#e8f5e9;color:#2e7d32;padding:3px 10px;border-radius:3px;font-size:0.68rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;margin-bottom:8px;}
.pcard-title-d5{font-weight:700;font-size:0.92rem;color:#1a1a1a;margin-bottom:4px;}
.pcard-desc-d5{font-size:0.8rem;color:#888;line-height:1.5;}

.process-d5{padding:90px 60px;background:#fff;}
.process-inner-d5{max-width:900px;margin:0 auto;}
.process-steps-d5{margin-top:50px;display:flex;flex-direction:column;gap:1px;background:#e8e8e4;border-radius:8px;overflow:hidden;}
.ps-d5{background:#fff;padding:36px 40px;display:grid;grid-template-columns:56px 1fr;gap:24px;align-items:start;transition:background .2s;}
.ps-d5:hover{background:#fafaf8;}
.ps-num-d5{width:48px;height:48px;border-radius:50%;background:#e8f5e9;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:1rem;color:#2e7d32;flex-shrink:0;}
.ps-d5 h3{font-size:1.05rem;font-weight:800;margin-bottom:6px;color:#1a1a1a;}
.ps-d5 p{color:#777;font-size:0.88rem;line-height:1.7;margin:0;}

.cta-d5{padding:90px 60px;background:#1a1a1a;display:grid;grid-template-columns:1fr auto;align-items:center;gap:40px;}
.cta-text-d5 h2{font-size:clamp(2rem,3.5vw,3rem);font-weight:900;color:#fff;letter-spacing:-2px;line-height:1.1;margin-bottom:10px;}
.cta-text-d5 p{color:#888;font-size:0.95rem;line-height:1.7;margin:0;}
.cta-action-d5{text-align:right;}
.cta-action-d5 a{display:inline-block;background:#2e7d32;color:#fff;padding:18px 44px;border-radius:4px;font-weight:700;font-size:1rem;text-decoration:none;transition:all .2s;white-space:nowrap;}
.cta-action-d5 a:hover{background:#1b5e20;transform:translateY(-2px);box-shadow:0 10px 28px rgba(46,125,50,0.4);}
.cta-sub-d5{font-size:0.75rem;color:#555;margin-top:10px;text-align:right;}

.reveal{opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s ease;}
.reveal.visible{opacity:1;transform:translateY(0);}
.reveal-left{opacity:0;transform:translateX(-18px);transition:opacity .6s ease,transform .6s ease;}
.reveal-left.visible{opacity:1;transform:translateX(0);}
.reveal-right{opacity:0;transform:translateX(18px);transition:opacity .6s ease,transform .6s ease;}
.reveal-right.visible{opacity:1;transform:translateX(0);}

@media(max-width:860px){
  .hero-d5{grid-template-columns:1fr;}
  .hero-right-d5{min-height:50vw;}
  .about-d5{grid-template-columns:1fr;padding:60px 28px;}
  .about-accent-d5{display:none;}
  .prop-grid-d5{grid-template-columns:1fr;}
  .cta-d5{grid-template-columns:1fr;gap:24px;}
  .cta-action-d5{text-align:left;}
  .cta-sub-d5{text-align:left;}
  .hero-left-d5{padding:60px 24px;}
  .properties-d5,.process-d5{padding:60px 24px;}
  .divider-strip-d5{gap:28px;padding:18px 24px;}
}
"""

with open('/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css', 'a') as f:
    f.write(css_to_append)

print("Appended design5 CSS to style.css")
