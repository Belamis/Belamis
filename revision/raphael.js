/*
 * Belamis — lancement des révisions.
 * Séquence calée sur le son (assets/transition.mp3, 15,7 s) :
 *   0    → 4,6 s  pluie d'étoiles filantes, qui finissent par converger
 *   4,6  → 9,2 s  trou noir : les étoiles nourrissent le disque d'accrétion
 *   9,2  → 9,8 s  effondrement
 *   9,8 s         explosion
 *   9,8 s → ∞     naissance de Raphaël : cœur dodécagonal doré, anneaux de runes,
 *                 tourbillon de lumière. Cette scène reste en fond de l'espace.
 */
(() => {
  "use strict";

  const TL = { converge: 3.0, holeIn: 4.2, meteorsEnd: 4.6, spinUp: 7.5, shrink: 8.4, collapse: 9.2, boom: 9.8, uiIn: 12.0 };

  const layer = document.getElementById("launch-layer");
  const canvas = document.getElementById("launch");
  const ctx = canvas.getContext("2d");
  const skipBtn = document.getElementById("skip");
  const soundBtn = document.getElementById("sound");
  const backBtn = document.getElementById("back");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const rand = (a, b) => a + Math.random() * (b - a);
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const lerp = (a, b, t) => a + (b - a) * t;
  const easeOutCubic = (t) => 1 - Math.pow(1 - t, 3);
  const easeInCubic = (t) => t * t * t;
  const easeOutBack = (t) => { const c1 = 1.6, c3 = c1 + 1; return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2); };
  const phase = (t, a, b) => clamp((t - a) / (b - a), 0, 1);

  let W = 0, H = 0, DPR = 1, cx = 0, cy = 0, R = 0, diag = 0;
  let running = false, raf = 0, t0 = 0, lastNow = 0, uiShown = false, boomDone = false;
  let audio = null, muted = false;

  // ---------- Sprites et fonds pré-calculés ----------
  function glowSprite(r, g, b) {
    const c = document.createElement("canvas");
    c.width = c.height = 64;
    const x = c.getContext("2d");
    const gr = x.createRadialGradient(32, 32, 0, 32, 32, 32);
    gr.addColorStop(0, `rgba(${r},${g},${b},1)`);
    gr.addColorStop(0.25, `rgba(${r},${g},${b},0.55)`);
    gr.addColorStop(1, `rgba(${r},${g},${b},0)`);
    x.fillStyle = gr;
    x.fillRect(0, 0, 64, 64);
    return c;
  }
  const SPR = {
    white: glowSprite(255, 255, 255),
    gold: glowSprite(255, 200, 90),
    teal: glowSprite(40, 190, 175),
    green: glowSprite(110, 210, 110),
    amber: glowSprite(240, 150, 50),
    pink: glowSprite(230, 70, 150),
  };

  let skyBg = null, holeBg = null;

  function offscreen(w, h) {
    const c = document.createElement("canvas");
    c.width = Math.round(w * DPR);
    c.height = Math.round(h * DPR);
    const x = c.getContext("2d");
    x.setTransform(DPR, 0, 0, DPR, 0, 0);
    return [c, x];
  }

  // Ciel bleu nuit des étoiles filantes
  function buildSky() {
    const [c, x] = offscreen(W, H);
    const g = x.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, "#040c2a");
    g.addColorStop(0.55, "#0d2c78");
    g.addColorStop(1, "#1a55b8");
    x.fillStyle = g;
    x.fillRect(0, 0, W, H);
    for (let i = 0; i < 380; i++) {
      x.fillStyle = `rgba(255,255,255,${rand(0.2, 0.8)})`;
      const s = Math.random() < 0.92 ? rand(0.5, 1.2) : rand(1.4, 2.2);
      x.fillRect(rand(0, W), rand(0, H), s, s);
    }
    // silhouette d'horizon, discrète
    x.fillStyle = "#020616";
    x.beginPath();
    x.moveTo(0, H);
    for (let i = 0; i <= 24; i++) x.lineTo((i / 24) * W, H - 18 - Math.sin(i * 1.7) * 8 - Math.sin(i * 0.6) * 10);
    x.lineTo(W, H);
    x.fill();
    return c;
  }

  // Espace profond du trou noir : nébuleuse rose, bande laiteuse, étoiles denses
  function buildHoleBg() {
    const [c, x] = offscreen(W, H);
    x.fillStyle = "#07040a";
    x.fillRect(0, 0, W, H);
    x.globalCompositeOperation = "lighter";
    // bande de la voie lactée, en diagonale
    for (let i = 0; i < 70; i++) {
      const u = Math.random();
      const px = lerp(W * 0.25, W * 1.05, u) + rand(-60, 60);
      const py = lerp(H * 0.45, -H * 0.05, u) + rand(-50, 50);
      const s = rand(60, 180);
      x.globalAlpha = rand(0.05, 0.14);
      x.drawImage(SPR.white, px - s, py - s, s * 2, s * 2);
    }
    // nuages roses
    for (let i = 0; i < 45; i++) {
      const px = Math.random() < 0.5 ? rand(0, W * 0.3) : rand(W * 0.7, W);
      const py = rand(0, H);
      const s = rand(40, 140);
      x.globalAlpha = rand(0.06, 0.18);
      x.drawImage(SPR.pink, px - s, py - s, s * 2, s * 2);
    }
    // halo rougeâtre sous le disque
    x.globalAlpha = 0.35;
    x.drawImage(SPR.amber, cx - W * 0.6, cy - H * 0.2, W * 1.2, H * 1.1);
    x.globalAlpha = 1;
    x.globalCompositeOperation = "source-over";
    for (let i = 0; i < 1400; i++) {
      x.fillStyle = `rgba(255,255,255,${rand(0.15, 0.9)})`;
      const s = Math.random() < 0.95 ? rand(0.4, 1.3) : rand(1.5, 2.4);
      x.fillRect(rand(0, W), rand(0, H), s, s);
    }
    return c;
  }

  // ---------- Écriture runique (glyphes inventés, tracés à la main) ----------
  let seed = 1;
  const srand = () => (seed = (seed * 16807) % 2147483647) / 2147483647;

  function drawGlyph(x, h) {
    const gx = [-0.28, 0, 0.28], gy = [-0.5, -0.17, 0.17, 0.5];
    const pt = () => [gx[Math.floor(srand() * 3)] * h, gy[Math.floor(srand() * 4)] * h];
    x.beginPath();
    if (srand() < 0.75) {
      const sx = gx[Math.floor(srand() * 3)] * h;
      x.moveTo(sx, -0.5 * h);
      x.lineTo(sx, 0.5 * h);
    }
    const n = 1 + Math.floor(srand() * 3);
    for (let i = 0; i < n; i++) {
      const [ax, ay] = pt(), [bx, by] = pt();
      if (ax === bx && ay === by) continue;
      x.moveTo(ax, ay);
      x.lineTo(bx, by);
    }
    x.stroke();
    const extra = srand();
    if (extra < 0.22) {
      const [ax, ay] = pt();
      x.beginPath();
      x.arc(ax, ay, h * 0.12, 0, Math.PI * 2);
      x.stroke();
    } else if (extra < 0.42) {
      const [ax, ay] = pt();
      x.beginPath();
      x.arc(ax, ay, h * 0.2, srand() * Math.PI, srand() * Math.PI + Math.PI);
      x.stroke();
    }
  }

  function makeRing(r, h, ringSeed) {
    const rd = Math.min(DPR, 1.5);
    const half = r + h;
    const size = Math.ceil(half * 2 * rd) + 8;
    const c = document.createElement("canvas");
    c.width = c.height = size;
    const x = c.getContext("2d");
    x.setTransform(rd, 0, 0, rd, size / 2, size / 2);
    x.lineCap = "round";
    x.lineJoin = "round";
    x.strokeStyle = "#ffd27a";
    x.shadowColor = "rgba(255,140,30,0.95)";
    x.shadowBlur = h * 0.45 * rd;
    // filets du cercle
    x.lineWidth = 1;
    for (const k of [-0.68, 0.68]) {
      x.beginPath();
      x.arc(0, 0, r + h * k, 0, Math.PI * 2);
      x.stroke();
    }
    x.lineWidth = Math.max(1.1, h * 0.085);
    seed = ringSeed;
    const n = Math.floor((Math.PI * 2 * r) / (h * 0.74));
    for (let i = 0; i < n; i++) {
      if (srand() < 0.06) continue; // petits blancs, comme une phrase
      x.save();
      x.rotate((i / n) * Math.PI * 2);
      x.translate(0, -r);
      drawGlyph(x, h);
      x.restore();
    }
    return { c, size: size / rd };
  }

  // ---------- Éléments dynamiques ----------
  let meteors = [], disk = [], burst = [], shocks = [], bokeh = [], rays = [], motes = [], rings = [];
  let spawnAcc = 0;

  function newMeteor() {
    const scale = clamp(W / 1280, 0.6, 1.4);
    const dir = [-0.78, 0.62];
    const p = Math.random() < 0.65 ? [rand(W * 0.15, W * 1.25), rand(-H * 0.35, -20)] : [rand(W + 20, W * 1.35), rand(-H * 0.2, H * 0.7)];
    const sp = rand(650, 1450) * scale;
    return { x: p[0], y: p[1], vx: dir[0] * sp, vy: dir[1] * sp, sp, len: rand(90, 320) * scale, s: rand(1, 2.6), flare: Math.random() < 0.3, dead: false };
  }

  function build() {
    const small = Math.min(W, H) < 700;
    meteors = [];
    burst = [];
    shocks = [];
    spawnAcc = 0;
    disk = Array.from({ length: small ? 900 : 1600 }, () => {
      const r = 0.14 + Math.pow(Math.random(), 0.75) * 0.86;
      return { r, th: rand(0, Math.PI * 2), w: 0.9 / Math.pow(r, 1.5), s: rand(0.8, 2.2) };
    });
    const cols = [SPR.teal, SPR.green, SPR.amber, SPR.teal, SPR.gold];
    bokeh = Array.from({ length: small ? 70 : 120 }, () => ({
      a: rand(0, Math.PI * 2), d: rand(0.28, 0.95), s: rand(0.03, 0.11), w: rand(0.05, 0.16), spr: cols[Math.floor(Math.random() * cols.length)], al: rand(0.25, 0.7),
    }));
    rays = Array.from({ length: small ? 50 : 80 }, () => ({ a: rand(0, Math.PI * 2), len: rand(0.35, 1.2), w: Math.random() < 0.85 ? rand(0.5, 1.2) : rand(1.5, 2.5), al: rand(0.2, 0.75), sp: rand(0.5, 2.5), p: rand(0, 6.28) }));
    motes = Array.from({ length: small ? 60 : 110 }, () => newMote(true));
  }

  function newMote(anywhere) {
    return { a: rand(0, Math.PI * 2), d: anywhere ? rand(0.2, 1) : rand(0.05, 0.25), v: rand(0.04, 0.16), s: rand(1, 3), p: rand(0, 6.28) };
  }

  function buildRings() {
    rings = [
      { ...makeRing(R * 1.32, R * 0.16, 11), speed: 0.06, delay: 0.0 },
      { ...makeRing(R * 1.66, R * 0.2, 23), speed: -0.04, delay: 0.25 },
      { ...makeRing(R * 2.02, R * 0.22, 37), speed: 0.028, delay: 0.5 },
      { ...makeRing(R * 2.45, R * 0.2, 53), speed: -0.018, delay: 0.75 },
    ];
  }

  function resize() {
    DPR = Math.min(window.devicePixelRatio || 1, 2);
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = Math.round(W * DPR);
    canvas.height = Math.round(H * DPR);
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    cx = W / 2;
    cy = H * (W < 700 ? 0.36 : 0.42);
    R = Math.min(W, H) * (W < 700 ? 0.15 : 0.17);
    diag = Math.hypot(W, H);
    skyBg = buildSky();
    holeBg = buildHoleBg();
    buildRings();
  }

  // ---------- Scène 1 : étoiles filantes ----------
  function updateMeteors(t, dt) {
    // cadence : ça s'intensifie, puis ça se tarit dans le trou noir
    let rate = 0;
    if (t < TL.meteorsEnd) rate = 10 + t * 12;
    else if (t < 7.2) rate = lerp(60, 0, phase(t, TL.meteorsEnd, 7.2));
    spawnAcc += rate * dt;
    while (spawnAcc > 1) { meteors.push(newMeteor()); spawnAcc--; }

    const pull = phase(t, TL.converge, TL.meteorsEnd + 0.4);
    const holeR = R * 2.6 * diskGrowth(t);
    for (const m of meteors) {
      if (pull > 0) {
        const dx = cx - m.x, dy = cy - m.y, d = Math.hypot(dx, dy) || 1;
        // on vise légèrement à côté du centre pour que la chute tourne en spirale
        const tx = (dx / d) * 0.82 - (dy / d) * 0.57, ty = (dy / d) * 0.82 + (dx / d) * 0.57;
        const k = Math.min(1, pull * dt * 3.2);
        m.vx = lerp(m.vx, tx * m.sp, k);
        m.vy = lerp(m.vy, ty * m.sp, k);
        if (t > TL.holeIn && d < holeR * 0.55) m.dead = true;
      }
      m.x += m.vx * dt;
      m.y += m.vy * dt;
      if (m.x < -400 || m.y > H + 400 || m.x > W + 800 || m.y < -800) m.dead = true;
    }
    meteors = meteors.filter((m) => !m.dead);
  }

  function drawMeteors(alpha) {
    if (alpha <= 0) return;
    ctx.globalCompositeOperation = "lighter";
    ctx.lineCap = "round";
    for (const m of meteors) {
      const sp = Math.hypot(m.vx, m.vy) || 1;
      const ex = m.x - (m.vx / sp) * m.len, ey = m.y - (m.vy / sp) * m.len;
      const g = ctx.createLinearGradient(m.x, m.y, ex, ey);
      g.addColorStop(0, `rgba(255,255,255,${0.95 * alpha})`);
      g.addColorStop(0.3, `rgba(200,225,255,${0.45 * alpha})`);
      g.addColorStop(1, "rgba(180,210,255,0)");
      ctx.strokeStyle = g;
      ctx.lineWidth = m.s;
      ctx.beginPath();
      ctx.moveTo(m.x, m.y);
      ctx.lineTo(ex, ey);
      ctx.stroke();
      const gs = m.s * 9;
      ctx.globalAlpha = alpha;
      ctx.drawImage(SPR.white, m.x - gs, m.y - gs, gs * 2, gs * 2);
      if (m.flare) {
        const f = m.s * 12;
        ctx.strokeStyle = `rgba(255,255,255,${0.55 * alpha})`;
        ctx.lineWidth = 0.8;
        ctx.beginPath();
        ctx.moveTo(m.x - f, m.y); ctx.lineTo(m.x + f, m.y);
        ctx.moveTo(m.x, m.y - f); ctx.lineTo(m.x, m.y + f);
        ctx.moveTo(m.x - f * 0.5, m.y - f * 0.5); ctx.lineTo(m.x + f * 0.5, m.y + f * 0.5);
        ctx.moveTo(m.x - f * 0.5, m.y + f * 0.5); ctx.lineTo(m.x + f * 0.5, m.y - f * 0.5);
        ctx.stroke();
      }
      ctx.globalAlpha = 1;
    }
    ctx.globalCompositeOperation = "source-over";
  }

  // ---------- Scène 2 : trou noir ----------
  const TILT = -0.26, FLAT = 0.3;
  const diskGrowth = (t) => easeOutCubic(phase(t, TL.holeIn, TL.holeIn + 2.2));
  const diskShrink = (t) => 1 - easeInCubic(phase(t, TL.shrink, TL.boom)) * 0.985;
  const DISK_COLORS = [
    [0.3, "255,250,238"],
    [0.5, "255,222,150"],
    [0.74, "255,150,60"],
    [1.01, "225,72,40"],
  ];

  function drawDiskHalf(Dr, front, alpha) {
    const c = Math.cos(TILT), s = Math.sin(TILT);
    let bucket = 0;
    for (const [limit, col] of DISK_COLORS) {
      ctx.fillStyle = `rgba(${col},${alpha * (bucket < 2 ? 0.9 : 0.7)})`;
      for (const p of disk) {
        if (p.r >= limit || (bucket > 0 && p.r < DISK_COLORS[bucket - 1][0])) continue;
        const sn = Math.sin(p.th);
        if ((sn > 0) !== front) continue;
        const x = Math.cos(p.th) * p.r * Dr, y = sn * p.r * Dr * FLAT;
        const px = cx + x * c - y * s, py = cy + x * s + y * c;
        ctx.fillRect(px, py, p.s, p.s);
      }
      bucket++;
    }
  }

  function drawBlackHole(t, dt) {
    const grow = diskGrowth(t), shrink = diskShrink(t);
    const scale = grow * shrink;
    if (scale <= 0.002 || t > TL.boom) return;
    const Dr = R * 2.6 * scale;
    const spin = 1 + Math.pow(phase(t, TL.spinUp, TL.boom), 2) * 7;
    for (const p of disk) p.th += p.w * dt * 0.9 * spin;
    const bright = 1 + phase(t, TL.shrink, TL.boom) * 1.5;

    ctx.globalCompositeOperation = "lighter";
    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate(TILT);
    ctx.scale(1, FLAT);
    let g = ctx.createRadialGradient(0, 0, 0, 0, 0, Dr * 1.35);
    g.addColorStop(0, `rgba(255,245,220,${0.9 * grow})`);
    g.addColorStop(0.3, `rgba(255,200,120,${0.55 * grow})`);
    g.addColorStop(0.65, `rgba(240,110,40,${0.3 * grow})`);
    g.addColorStop(1, "rgba(200,50,30,0)");
    ctx.fillStyle = g;
    ctx.beginPath();
    ctx.arc(0, 0, Dr * 1.35, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();

    drawDiskHalf(Dr, false, Math.min(1, grow * bright));
    ctx.globalCompositeOperation = "source-over";

    // horizon des événements + anneau de photons
    const hr = Dr * 0.11;
    ctx.globalCompositeOperation = "lighter";
    ctx.strokeStyle = `rgba(255,255,255,${0.9 * grow})`;
    ctx.lineWidth = Math.max(1.5, hr * 0.18);
    ctx.beginPath();
    ctx.ellipse(cx, cy - hr * 0.35, hr * 1.9, hr * 1.2, TILT, Math.PI, Math.PI * 2);
    ctx.stroke();
    ctx.globalCompositeOperation = "source-over";
    ctx.fillStyle = "#000";
    ctx.beginPath();
    ctx.arc(cx, cy, hr, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = `rgba(255,240,220,${0.7 * grow})`;
    ctx.lineWidth = 1.5;
    ctx.stroke();

    ctx.globalCompositeOperation = "lighter";
    drawDiskHalf(Dr, true, Math.min(1, grow * bright));
    ctx.globalCompositeOperation = "source-over";
  }

  // ---------- Scène 3 : effondrement + explosion ----------
  function triggerBoom() {
    boomDone = true;
    const n = Math.min(W, H) < 700 ? 420 : 750;
    for (let i = 0; i < n; i++) {
      const a = rand(0, Math.PI * 2), v = rand(150, 1500) * clamp(W / 1280, 0.6, 1.4);
      const white = Math.random() < 0.35;
      burst.push({ x: cx, y: cy, vx: Math.cos(a) * v, vy: Math.sin(a) * v, life: rand(0.7, 1.8), max: 0, s: rand(1, 3.2), col: white ? "255,255,245" : "255,200,90" });
    }
    burst.forEach((b) => (b.max = b.life));
    shocks = [0, 0.14, 0.34].map((d) => ({ d }));
  }

  function drawCollapse(t) {
    const k = phase(t, TL.collapse, TL.boom);
    if (k <= 0 || t > TL.boom + 0.05) return;
    const s = 4 + easeInCubic(k) * R * 0.9;
    ctx.globalCompositeOperation = "lighter";
    ctx.globalAlpha = 0.5 + k * 0.5;
    ctx.drawImage(SPR.white, cx - s, cy - s, s * 2, s * 2);
    ctx.globalAlpha = 1;
    ctx.globalCompositeOperation = "source-over";
  }

  function drawBoom(t, dt) {
    if (!boomDone) return;
    const e = t - TL.boom;
    ctx.globalCompositeOperation = "lighter";
    for (const sh of shocks) {
      const p = clamp((e - sh.d) / 1.8, 0, 1);
      if (p <= 0 || p >= 1) continue;
      const r = easeOutCubic(p) * diag * 0.75;
      ctx.strokeStyle = `rgba(255,215,140,${(1 - p) * 0.8})`;
      ctx.lineWidth = (1 - p) * 22 + 1;
      ctx.beginPath();
      ctx.arc(cx, cy, r, 0, Math.PI * 2);
      ctx.stroke();
    }
    for (let i = burst.length - 1; i >= 0; i--) {
      const b = burst[i];
      b.x += b.vx * dt; b.y += b.vy * dt;
      b.vx *= 0.975; b.vy *= 0.975;
      b.life -= dt;
      if (b.life <= 0) { burst.splice(i, 1); continue; }
      const a = b.life / b.max;
      ctx.fillStyle = `rgba(${b.col},${a})`;
      ctx.fillRect(b.x, b.y, b.s, b.s);
    }
    ctx.globalCompositeOperation = "source-over";
  }

  // ---------- Scène 4 : Raphaël ----------
  function drawRaphaelBg(t, dt, alpha) {
    if (alpha <= 0) return;
    const g = ctx.createRadialGradient(cx, cy, 0, cx, cy, diag * 0.6);
    g.addColorStop(0, `rgba(70,40,8,${alpha})`);
    g.addColorStop(0.35, `rgba(22,26,14,${alpha})`);
    g.addColorStop(1, `rgba(3,14,16,${alpha})`);
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, W, H);

    // tourbillon de lumières floues, comme un tunnel
    ctx.globalCompositeOperation = "lighter";
    const half = diag * 0.5;
    for (const b of bokeh) {
      b.a += b.w * dt * (1 + (1 - alpha) * 4);
      const d = b.d * half;
      const x = cx + Math.cos(b.a) * d, y = cy + Math.sin(b.a) * d * 0.8;
      const s = b.s * half * (0.6 + b.d);
      ctx.globalAlpha = b.al * alpha * 0.55;
      ctx.drawImage(b.spr, x - s, y - s, s * 2, s * 2);
    }
    ctx.globalAlpha = 1;
    ctx.globalCompositeOperation = "source-over";
  }

  function drawRaphaelRays(t, k) {
    if (k <= 0) return;
    ctx.globalCompositeOperation = "lighter";
    const spin = t * 0.02;
    for (const r of rays) {
      const a = r.a + spin;
      const al = r.al * (0.55 + 0.45 * Math.sin(t * r.sp + r.p)) * k;
      const r0 = R * 0.3, r1 = r.len * diag * (0.3 + 0.7 * k);
      const x0 = cx + Math.cos(a) * r0, y0 = cy + Math.sin(a) * r0;
      const x1 = cx + Math.cos(a) * r1, y1 = cy + Math.sin(a) * r1;
      const g = ctx.createLinearGradient(x0, y0, x1, y1);
      g.addColorStop(0, `rgba(255,248,215,${al})`);
      g.addColorStop(0.45, `rgba(255,205,110,${al * 0.45})`);
      g.addColorStop(1, "rgba(255,180,80,0)");
      ctx.strokeStyle = g;
      ctx.lineWidth = r.w;
      ctx.beginPath();
      ctx.moveTo(x0, y0);
      ctx.lineTo(x1, y1);
      ctx.stroke();
    }
    ctx.globalCompositeOperation = "source-over";
  }

  function drawRings(t, e) {
    ctx.globalCompositeOperation = "lighter";
    for (const r of rings) {
      const k = easeOutCubic(clamp((e - 0.3 - r.delay) / 1.4, 0, 1));
      if (k <= 0) continue;
      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(t * r.speed + (1 - k) * 1.2 * Math.sign(r.speed));
      const s = lerp(1.35, 1, k);
      ctx.scale(s, s);
      ctx.globalAlpha = k * (0.8 + 0.2 * Math.sin(t * 1.3 + r.delay * 9));
      ctx.drawImage(r.c, -r.size / 2, -r.size / 2, r.size, r.size);
      ctx.restore();
    }
    ctx.globalAlpha = 1;
    ctx.globalCompositeOperation = "source-over";
  }

  function dodecagon(r, rot) {
    ctx.beginPath();
    for (let i = 0; i < 12; i++) {
      const a = rot + (i / 12) * Math.PI * 2;
      const x = cx + Math.cos(a) * r, y = cy + Math.sin(a) * r;
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.closePath();
  }

  function drawCore(t, e) {
    const k = easeOutBack(clamp(e / 1.3, 0, 1));
    if (k <= 0) return;
    const pulse = 1 + Math.sin(t * 2.4) * 0.025 + Math.sin(t * 6.1) * 0.01;
    const r = R * k * pulse;
    const rot = t * 0.08;

    // intérieur incandescent
    let g = ctx.createRadialGradient(cx, cy, 0, cx, cy, r);
    g.addColorStop(0, "rgba(255,255,240,1)");
    g.addColorStop(0.25, "rgba(255,236,170,0.95)");
    g.addColorStop(0.6, "rgba(245,170,60,0.75)");
    g.addColorStop(1, "rgba(190,100,20,0.55)");
    ctx.fillStyle = g;
    dodecagon(r, rot);
    ctx.fill();

    ctx.globalCompositeOperation = "lighter";
    // rayons internes
    ctx.lineCap = "round";
    for (let i = 0; i < 36; i++) {
      const a = i * 2.39996 + t * 0.15;
      const len = r * (0.5 + 0.45 * Math.abs(Math.sin(t * 1.7 + i)));
      ctx.strokeStyle = `rgba(255,255,235,${0.25 + 0.25 * Math.sin(t * 3 + i)})`;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx + Math.cos(a) * len, cy + Math.sin(a) * len);
      ctx.stroke();
    }
    // étincelles qui dansent dans le cœur
    for (let i = 0; i < 40; i++) {
      const a = i * 1.7 + t * (0.3 + (i % 5) * 0.08);
      const d = r * (0.15 + ((i * 53) % 70) / 100);
      const s = 2 + (i % 3) * 2;
      ctx.globalAlpha = 0.4 + 0.4 * Math.sin(t * 4 + i);
      ctx.drawImage(SPR.gold, cx + Math.cos(a) * d - s, cy + Math.sin(a) * d - s, s * 2, s * 2);
    }
    ctx.globalAlpha = 1;

    // l'anneau dodécagonal blanc, épais et lumineux
    ctx.lineJoin = "round";
    const layers = [[r * 0.28, "rgba(255,190,90,0.12)"], [r * 0.15, "rgba(255,225,160,0.35)"], [r * 0.075, "rgba(255,250,230,0.9)"], [r * 0.03, "rgba(255,255,255,1)"]];
    for (const [w, col] of layers) {
      ctx.strokeStyle = col;
      ctx.lineWidth = w;
      dodecagon(r, rot);
      ctx.stroke();
    }
    // halo global
    const hs = r * 3.2;
    ctx.globalAlpha = 0.55;
    ctx.drawImage(SPR.gold, cx - hs, cy - hs, hs * 2, hs * 2);
    ctx.globalAlpha = 1;
    ctx.globalCompositeOperation = "source-over";
  }

  function drawMotes(t, dt, k) {
    if (k <= 0) return;
    ctx.globalCompositeOperation = "lighter";
    const half = diag * 0.5;
    for (let i = 0; i < motes.length; i++) {
      const m = motes[i];
      m.d += m.v * dt;
      m.a += dt * 0.05;
      if (m.d > 1.1) { motes[i] = newMote(false); continue; }
      const x = cx + Math.cos(m.a) * m.d * half, y = cy + Math.sin(m.a) * m.d * half * 0.85;
      const s = m.s * 3;
      ctx.globalAlpha = k * clamp(m.d * 4, 0, 1) * (1 - m.d / 1.1) * (0.6 + 0.4 * Math.sin(t * 3 + m.p));
      ctx.drawImage(SPR.gold, x - s, y - s, s * 2, s * 2);
    }
    ctx.globalAlpha = 1;
    ctx.globalCompositeOperation = "source-over";
  }

  // ---------- Boucle ----------
  function clock(now) {
    return (now - t0) / 1000;
  }

  function frame(now) {
    if (!running) return;
    const dt = Math.min((now - lastNow) / 1000, 0.05);
    lastNow = now;
    const t = clock(now);

    ctx.globalCompositeOperation = "source-over";
    ctx.globalAlpha = 1;
    ctx.clearRect(0, 0, W, H);

    // le ciel bleu apparaît par-dessus l'accueil, puis cède la place à l'espace profond
    const skyA = phase(t, 0, 0.9) * (1 - phase(t, 4.0, 5.4));
    const holeA = phase(t, 4.0, 5.4) * (1 - phase(t, 9.0, 9.8));
    const blackA = phase(t, 0, 0.9);
    if (blackA > 0 && t < TL.boom + 2) {
      ctx.fillStyle = `rgba(2,2,6,${blackA})`;
      ctx.fillRect(0, 0, W, H);
    }
    if (skyA > 0) { ctx.globalAlpha = skyA; ctx.drawImage(skyBg, 0, 0, W, H); ctx.globalAlpha = 1; }
    if (holeA > 0) { ctx.globalAlpha = holeA; ctx.drawImage(holeBg, 0, 0, W, H); ctx.globalAlpha = 1; }

    const e = t - TL.boom;
    // tremblement à l'explosion
    const shake = boomDone ? Math.max(0, 1 - e / 0.9) * 14 : 0;
    const baseX = W / 2, baseY = H * (W < 700 ? 0.36 : 0.42);
    cx = baseX + (shake ? rand(-shake, shake) : 0);
    cy = baseY + (shake ? rand(-shake, shake) : 0);

    if (t < TL.boom) {
      updateMeteors(t, dt);
      drawBlackHole(t, dt);
      drawMeteors(Math.min(1, phase(t, 0.2, 0.8)));
      drawCollapse(t);
    } else {
      if (!boomDone) triggerBoom();
      const born = clamp(e / 1.6, 0, 1);
      drawRaphaelBg(t, dt, born);
      drawRaphaelRays(t, easeOutCubic(clamp(e / 2, 0, 1)));
      drawRings(t, e);
      drawMotes(t, dt, born);
      drawCore(t, e);
      drawBoom(t, dt);
      // flash blanc de l'explosion
      const flash = Math.max(0, 1 - e / 1.3);
      if (flash > 0) {
        ctx.fillStyle = `rgba(255,252,240,${Math.pow(flash, 1.6) * 0.95})`;
        ctx.fillRect(0, 0, W, H);
      }
    }

    if (!uiShown && t >= TL.uiIn) showUI();
    raf = requestAnimationFrame(frame);
  }

  // ---------- Son ----------
  function fadeOutAudio(ms) {
    if (!audio) return;
    const a = audio, start = a.volume, t = performance.now();
    const step = (now) => {
      const k = clamp((now - t) / ms, 0, 1);
      a.volume = clamp(start * (1 - k), 0, 1);
      if (k < 1) requestAnimationFrame(step); else a.pause();
    };
    requestAnimationFrame(step);
  }

  function updateSoundBtn() {
    soundBtn.setAttribute("aria-pressed", String(!muted));
    soundBtn.querySelector("span").textContent = muted ? "Son coupé" : "Son activé";
    soundBtn.classList.toggle("muted", muted);
  }

  soundBtn.addEventListener("click", () => {
    muted = !muted;
    if (audio) audio.muted = muted;
    updateSoundBtn();
  });

  // ---------- Lancement / sortie ----------
  function showUI() {
    uiShown = true;
    layer.classList.add("born");
    skipBtn.hidden = true;
  }

  function launch({ withSound = true, direct = false } = {}) {
    if (running) return;
    window.__belamisPaused = true;
    document.body.classList.add("launching");
    layer.hidden = false;
    layer.classList.remove("born");
    skipBtn.hidden = false;
    uiShown = false;
    boomDone = false;
    resize();
    build();

    const begin = () => {
      running = true;
      t0 = performance.now();
      lastNow = t0;
      if (direct || reduceMotion) {
        // arrivée directe sur Raphaël, sans flash
        t0 -= (TL.boom + 3) * 1000;
        boomDone = true;
      }
      raf = requestAnimationFrame(frame);
    };

    if (withSound && !direct) {
      audio = new Audio("assets/transition.mp3");
      audio.muted = muted;
      audio.volume = 1;
      // le chrono démarre avec le son, pour que l'explosion tombe au bon moment
      audio.play().then(begin, begin);
    } else {
      begin();
    }
  }

  function skip() {
    if (!running) return;
    const t = clock(performance.now());
    if (t < TL.boom + 3) {
      t0 = performance.now() - (TL.boom + 3) * 1000;
      boomDone = true;
      burst = [];
      shocks = [];
    }
    fadeOutAudio(700);
  }

  function exit() {
    running = false;
    cancelAnimationFrame(raf);
    fadeOutAudio(400);
    layer.hidden = true;
    layer.classList.remove("born");
    document.body.classList.remove("launching");
    window.__belamisPaused = false;
    try { history.replaceState(null, "", location.pathname + location.search); } catch (_) { /* cadre restreint */ }
  }

  skipBtn.addEventListener("click", skip);
  backBtn.addEventListener("click", exit);
  window.addEventListener("keydown", (e) => {
    if (!running || document.body.classList.contains("studying")) return;
    if (e.key === "Escape") uiShown ? exit() : skip();
  });

  // appelé par auth.js, une fois la connexion réglée (compte ou invité)
  window.BelamisLaunch = () => launch();

  let resizeTimer;
  window.addEventListener("resize", () => {
    if (!running) return;
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => { resize(); build(); }, 150);
  });

  updateSoundBtn();
  // un ancien lien « #revision » ramène désormais à l'accueil : l'animation se joue à chaque lancement
  if (location.hash === "#revision") { try { history.replaceState(null, "", location.pathname + location.search); } catch (_) { /* cadre restreint */ } }
})();
