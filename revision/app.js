/*
 * Belamis — accueil animé.
 * Tout l'univers est dessiné sur un <canvas> 2D, sans dépendance :
 *   nébuleuse dérivante, champ d'étoiles, rayons de lumière, fragments
 *   carrés qui fusent vers la caméra, icosaèdre en fil de fer, anneaux
 *   orbitaux et cœur lumineux pulsant.
 */
(() => {
  "use strict";

  const canvas = document.getElementById("cosmos");
  const ctx = canvas.getContext("2d");
  // les animations se jouent sauf si l’élève choisit « réduites » dans Paramètres
  let reduceMotion = Boolean(window.BelamisPrefs && window.BelamisPrefs.get("motion") === "reduit");
  if (window.BelamisPrefs) window.BelamisPrefs.onChange((k, v) => { if (k === "motion") reduceMotion = v === "reduit"; });

  let W = 0, H = 0, DPR = 1, cx = 0, cy = 0, R = 0, K = 0;
  const isSmall = () => Math.min(window.innerWidth, window.innerHeight) < 700;

  // ---------- Utilitaires ----------
  const rand = (a, b) => a + Math.random() * (b - a);
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const lerp = (a, b, t) => a + (b - a) * t;
  const easeOutCubic = (t) => 1 - Math.pow(1 - t, 3);
  const easeOutBack = (t) => {
    const c1 = 1.4, c3 = c1 + 1;
    return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2);
  };

  function rotate(p, ax, ay, az) {
    let [x, y, z] = p;
    // rotation Y
    let c = Math.cos(ay), s = Math.sin(ay);
    [x, z] = [x * c + z * s, -x * s + z * c];
    // rotation X
    c = Math.cos(ax); s = Math.sin(ax);
    [y, z] = [y * c - z * s, y * s + z * c];
    // rotation Z
    c = Math.cos(az); s = Math.sin(az);
    [x, y] = [x * c - y * s, x * s + y * c];
    return [x, y, z];
  }

  // ---------- Icosaèdre ----------
  const PHI = (1 + Math.sqrt(5)) / 2;
  const ICO_V = [
    [-1, PHI, 0], [1, PHI, 0], [-1, -PHI, 0], [1, -PHI, 0],
    [0, -1, PHI], [0, 1, PHI], [0, -1, -PHI], [0, 1, -PHI],
    [PHI, 0, -1], [PHI, 0, 1], [-PHI, 0, -1], [-PHI, 0, 1],
  ].map((v) => {
    const l = Math.hypot(v[0], v[1], v[2]);
    return v.map((c) => c / l);
  });
  const ICO_E = (() => {
    const edges = [];
    let min = Infinity;
    for (let i = 0; i < ICO_V.length; i++)
      for (let j = i + 1; j < ICO_V.length; j++) {
        const d = Math.hypot(ICO_V[i][0] - ICO_V[j][0], ICO_V[i][1] - ICO_V[j][1], ICO_V[i][2] - ICO_V[j][2]);
        min = Math.min(min, d);
      }
    for (let i = 0; i < ICO_V.length; i++)
      for (let j = i + 1; j < ICO_V.length; j++) {
        const d = Math.hypot(ICO_V[i][0] - ICO_V[j][0], ICO_V[i][1] - ICO_V[j][1], ICO_V[i][2] - ICO_V[j][2]);
        if (d < min * 1.01) edges.push([i, j]);
      }
    return edges;
  })();

  // ---------- Éléments de la scène ----------
  const NEBULA = [
    { x: -0.32, y: -0.28, r: 0.55, c: [120, 210, 60], a: 0.55, s: 0.07, p: 0.0 },
    { x: 0.05, y: 0.36, r: 0.6, c: [210, 225, 50], a: 0.5, s: 0.05, p: 1.3 },
    { x: -0.42, y: 0.1, r: 0.35, c: [40, 200, 190], a: 0.45, s: 0.09, p: 2.1 },
    { x: 0.42, y: 0.02, r: 0.38, c: [210, 60, 110], a: 0.28, s: 0.06, p: 3.7 },
    { x: 0.3, y: -0.36, r: 0.4, c: [60, 110, 220], a: 0.3, s: 0.08, p: 4.4 },
    { x: -0.12, y: 0.12, r: 0.3, c: [230, 255, 170], a: 0.35, s: 0.11, p: 5.2 },
    { x: 0.38, y: 0.42, r: 0.35, c: [110, 200, 70], a: 0.35, s: 0.05, p: 0.8 },
  ];

  let stars = [], rays = [], shards = [], sparks = [];

  function build() {
    const small = isSmall();
    const nStars = small ? 160 : 320;
    const nRays = small ? 60 : 110;
    const nShards = small ? 70 : 150;

    stars = Array.from({ length: nStars }, () => ({
      x: Math.random(), y: Math.random(),
      r: Math.random() < 0.9 ? rand(0.3, 1.1) : rand(1.2, 2),
      a: rand(0.2, 0.9), tw: rand(0.5, 3), p: rand(0, 6.28), d: rand(0.2, 1),
    }));

    rays = Array.from({ length: nRays }, () => ({
      a: rand(0, Math.PI * 2),
      len: rand(0.35, 1.25),
      w: Math.random() < 0.85 ? rand(0.4, 1) : rand(1.2, 2.2),
      alpha: rand(0.12, 0.6),
      sp: rand(0.4, 2.5),
      p: rand(0, 6.28),
      drift: rand(-0.02, 0.02),
    }));

    shards = Array.from({ length: nShards }, () => newShard(true));
    sparks = [];
  }

  function newShard(anywhere) {
    const ang = rand(0, Math.PI * 2);
    const rad = rand(0.12, 1.4);
    return {
      x: Math.cos(ang) * rad,
      y: Math.sin(ang) * rad * 0.8,
      z: anywhere ? rand(0.15, 4) : rand(3.4, 4.2),
      rot: rand(0, Math.PI),
      vr: rand(-0.8, 0.8),
      size: rand(0.6, 2.2),
      aspect: Math.random() < 0.5 ? 1 : rand(0.4, 1.6),
      filled: Math.random() < 0.35,
      tint: Math.random() < 0.15 ? [200, 255, 140] : [255, 255, 255],
    };
  }

  // ---------- Dimensionnement ----------
  function resize() {
    DPR = Math.min(window.devicePixelRatio || 1, 2);
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = Math.round(W * DPR);
    canvas.height = Math.round(H * DPR);
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    R = Math.min(W, H) * (W < 700 ? 0.3 : 0.25);
    K = Math.min(W, H) * 0.5;
  }

  // ---------- Interaction ----------
  const mouse = { x: 0, y: 0, tx: 0, ty: 0 };
  let scrollT = 0, scrollSmooth = 0;
  let burst = 0;

  window.addEventListener("pointermove", (e) => {
    mouse.tx = (e.clientX / W) * 2 - 1;
    mouse.ty = (e.clientY / H) * 2 - 1;
  }, { passive: true });

  window.addEventListener("scroll", () => {
    scrollT = clamp(window.scrollY / H, 0, 1.5);
    document.querySelector(".nav").classList.toggle("scrolled", window.scrollY > 30);
  }, { passive: true });

  // Un clic sur le fond déclenche une onde et une gerbe d'étincelles.
  window.addEventListener("pointerdown", (e) => {
    if (e.target.closest("a, button")) return;
    burst = 1;
    for (let i = 0; i < 40; i++) {
      const a = rand(0, Math.PI * 2), v = rand(80, 420);
      sparks.push({ x: e.clientX, y: e.clientY, vx: Math.cos(a) * v, vy: Math.sin(a) * v, life: 1, s: rand(1, 3) });
    }
  });

  // ---------- Rendu ----------
  function drawNebula(t) {
    ctx.globalCompositeOperation = "lighter";
    const base = Math.max(W, H);
    for (const n of NEBULA) {
      const x = cx + (n.x + Math.sin(t * n.s + n.p) * 0.05) * W - mouse.x * 30;
      const y = cy + (n.y + Math.cos(t * n.s * 1.3 + n.p) * 0.05) * H - mouse.y * 20;
      const r = n.r * base * (1 + Math.sin(t * n.s * 2 + n.p) * 0.08);
      const g = ctx.createRadialGradient(x, y, 0, x, y, r);
      const [cr, cg, cb] = n.c;
      g.addColorStop(0, `rgba(${cr},${cg},${cb},${n.a * 0.55})`);
      g.addColorStop(0.45, `rgba(${cr},${cg},${cb},${n.a * 0.2})`);
      g.addColorStop(1, `rgba(${cr},${cg},${cb},0)`);
      ctx.fillStyle = g;
      ctx.fillRect(0, 0, W, H);
    }
    ctx.globalCompositeOperation = "source-over";
  }

  function drawStars(t) {
    for (const s of stars) {
      const x = s.x * W - mouse.x * 14 * s.d;
      const y = s.y * H - mouse.y * 10 * s.d;
      const a = s.a * (0.55 + 0.45 * Math.sin(t * s.tw + s.p));
      ctx.fillStyle = `rgba(255,255,255,${a})`;
      ctx.fillRect(x, y, s.r, s.r);
    }
  }

  function drawRays(t, intro) {
    ctx.globalCompositeOperation = "lighter";
    const diag = Math.hypot(W, H);
    const spin = t * 0.015;
    for (const r of rays) {
      const a = r.a + spin + Math.sin(t * 0.2 + r.p) * r.drift;
      const flick = 0.55 + 0.45 * Math.sin(t * r.sp + r.p);
      const alpha = r.alpha * flick * intro * (1 + burst * 0.8);
      if (alpha < 0.01) continue;
      const r0 = R * 0.12;
      const r1 = r.len * diag * (0.6 + 0.4 * intro);
      const x0 = cx + Math.cos(a) * r0, y0 = cy + Math.sin(a) * r0;
      const x1 = cx + Math.cos(a) * r1, y1 = cy + Math.sin(a) * r1;
      const g = ctx.createLinearGradient(x0, y0, x1, y1);
      g.addColorStop(0, `rgba(255,255,250,${alpha})`);
      g.addColorStop(0.5, `rgba(235,255,220,${alpha * 0.5})`);
      g.addColorStop(1, "rgba(255,255,255,0)");
      ctx.strokeStyle = g;
      ctx.lineWidth = r.w;
      ctx.beginPath();
      ctx.moveTo(x0, y0);
      ctx.lineTo(x1, y1);
      ctx.stroke();
    }
    ctx.globalCompositeOperation = "source-over";
  }

  function updateShards(dt, speed) {
    for (let i = 0; i < shards.length; i++) {
      const s = shards[i];
      s.z -= dt * 0.35 * speed;
      s.rot += s.vr * dt;
      if (s.z < 0.12) shards[i] = newShard(false);
    }
  }

  function drawShards(intro) {
    // du plus loin au plus proche
    shards.sort((a, b) => b.z - a.z);
    for (const s of shards) {
      const px = cx + (s.x / s.z) * K - mouse.x * 40 / s.z;
      const py = cy + (s.y / s.z) * K - mouse.y * 30 / s.z;
      if (px < -80 || px > W + 80 || py < -80 || py > H + 80) continue;
      const size = (s.size / s.z) * K * 0.018;
      const fadeIn = clamp((4.2 - s.z) / 1.2, 0, 1);
      const fadeOut = clamp((s.z - 0.12) / 0.4, 0, 1);
      const a = fadeIn * fadeOut * intro;
      if (a < 0.02) continue;
      const [r, g, b] = s.tint;
      ctx.save();
      ctx.translate(px, py);
      ctx.rotate(s.rot);
      const w = size, h = size * s.aspect;
      if (s.filled) {
        ctx.fillStyle = `rgba(${r},${g},${b},${a * 0.55})`;
        ctx.fillRect(-w / 2, -h / 2, w, h);
      } else {
        ctx.fillStyle = `rgba(${r},${g},${b},${a * 0.08})`;
        ctx.fillRect(-w / 2, -h / 2, w, h);
        ctx.strokeStyle = `rgba(${r},${g},${b},${a * 0.6})`;
        ctx.lineWidth = 1;
        ctx.strokeRect(-w / 2, -h / 2, w, h);
      }
      ctx.restore();
    }
  }

  function project(p, radius) {
    const fov = 3.2;
    const z = p[2];
    const sc = fov / (fov + z);
    return { x: cx + p[0] * radius * sc, y: cy + p[1] * radius * sc, z, sc };
  }

  function drawPolyhedron(t, scale, ax, ay, az, alpha, glowDots) {
    const radius = R * scale;
    const pts = ICO_V.map((v) => project(rotate(v, ax, ay, az), radius));

    ctx.lineCap = "round";
    for (const [i, j] of ICO_E) {
      const a = pts[i], b = pts[j];
      const depth = (a.z + b.z) / 2; // -1 (devant) .. 1 (derrière)
      const k = 0.35 + 0.65 * (1 - (depth + 1) / 2);
      ctx.strokeStyle = `rgba(245,250,240,${alpha * k})`;
      ctx.lineWidth = 0.6 + k * 0.9;
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.lineTo(b.x, b.y);
      ctx.stroke();
    }

    if (!glowDots) return;
    ctx.globalCompositeOperation = "lighter";
    for (const p of pts) {
      const k = 0.4 + 0.6 * (1 - (p.z + 1) / 2);
      const rr = 2 + k * 2.5;
      const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, rr * 4);
      g.addColorStop(0, `rgba(255,255,255,${alpha * k})`);
      g.addColorStop(0.3, `rgba(220,255,190,${alpha * k * 0.4})`);
      g.addColorStop(1, "rgba(200,255,150,0)");
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(p.x, p.y, rr * 4, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalCompositeOperation = "source-over";
  }

  // Anneau « griffonné » autour du cœur, comme sur l'image de référence
  function drawRing(t, radius, tiltX, tiltZ, spin, alpha, wobble, seed) {
    const N = 160;
    for (let pass = 0; pass < 2; pass++) {
      ctx.beginPath();
      for (let i = 0; i <= N; i++) {
        const u = (i / N) * Math.PI * 2;
        const w = 1 + wobble * Math.sin(u * 7 + t * 1.5 + seed + pass * 2)
                    + wobble * 0.6 * Math.sin(u * 13 - t * 2.1 + seed * 2);
        const p = rotate([Math.cos(u + spin) * w, Math.sin(u + spin) * w, 0], tiltX, 0, tiltZ);
        const q = project(p, radius);
        if (i === 0) ctx.moveTo(q.x, q.y); else ctx.lineTo(q.x, q.y);
      }
      ctx.strokeStyle = `rgba(250,255,245,${alpha * (pass ? 0.45 : 0.85)})`;
      ctx.lineWidth = pass ? 0.8 : 1.6;
      ctx.setLineDash(pass ? [2, 7] : [40, 6, 3, 6]);
      ctx.lineDashOffset = -t * 30 * (pass ? -1 : 1);
      ctx.stroke();
    }
    ctx.setLineDash([]);
  }

  function drawCore(t, intro) {
    const pulse = 1 + Math.sin(t * 2.2) * 0.06 + Math.sin(t * 5.3) * 0.025 + burst * 0.4;
    const r = R * 0.42 * pulse * intro;
    ctx.globalCompositeOperation = "lighter";

    // halo large
    let g = ctx.createRadialGradient(cx, cy, 0, cx, cy, r * 2.4);
    g.addColorStop(0, "rgba(255,255,240,0.55)");
    g.addColorStop(0.25, "rgba(210,255,190,0.18)");
    g.addColorStop(1, "rgba(120,220,160,0)");
    ctx.fillStyle = g;
    ctx.beginPath(); ctx.arc(cx, cy, r * 2.4, 0, Math.PI * 2); ctx.fill();

    // noyau brûlant
    g = ctx.createRadialGradient(cx, cy, 0, cx, cy, r * 0.8);
    g.addColorStop(0, "rgba(255,255,255,1)");
    g.addColorStop(0.2, "rgba(255,255,255,0.95)");
    g.addColorStop(0.5, "rgba(245,255,235,0.45)");
    g.addColorStop(1, "rgba(220,255,210,0)");
    ctx.fillStyle = g;
    ctx.beginPath(); ctx.arc(cx, cy, r * 0.8, 0, Math.PI * 2); ctx.fill();

    // petits éclats en orbite serrée autour du noyau
    for (let i = 0; i < 14; i++) {
      const a = t * (0.6 + (i % 3) * 0.25) + i * 2.4;
      const d = r * (0.35 + ((i * 37) % 10) / 22);
      const x = cx + Math.cos(a) * d, y = cy + Math.sin(a) * d * 0.8;
      const s = 2 + (i % 4);
      ctx.fillStyle = `rgba(255,255,255,${0.35 + 0.3 * Math.sin(t * 3 + i)})`;
      ctx.fillRect(x - s / 2, y - s / 2, s, s * 0.7);
    }
    ctx.globalCompositeOperation = "source-over";
  }

  function drawSparks(dt) {
    ctx.globalCompositeOperation = "lighter";
    for (let i = sparks.length - 1; i >= 0; i--) {
      const s = sparks[i];
      s.x += s.vx * dt; s.y += s.vy * dt;
      s.vx *= 0.96; s.vy *= 0.96;
      s.life -= dt * 1.3;
      if (s.life <= 0) { sparks.splice(i, 1); continue; }
      ctx.fillStyle = `rgba(220,255,170,${s.life})`;
      ctx.fillRect(s.x - s.s / 2, s.y - s.s / 2, s.s, s.s);
    }
    ctx.globalCompositeOperation = "source-over";
  }

  // ---------- Boucle ----------
  const start = performance.now();
  let last = start;

  function frame(now) {
    // en pause pendant que l'espace de révision occupe l'écran
    if (window.__belamisPaused) {
      last = now;
      requestAnimationFrame(frame);
      return;
    }
    const dt = Math.min((now - last) / 1000, 0.05);
    last = now;
    const t = (now - start) / 1000;
    const intro = reduceMotion ? 1 : easeOutCubic(clamp(t / 2.4, 0, 1));
    const pop = reduceMotion ? 1 : easeOutBack(clamp((t - 0.3) / 1.8, 0, 1));

    mouse.x = lerp(mouse.x, mouse.tx, 0.05);
    mouse.y = lerp(mouse.y, mouse.ty, 0.05);
    scrollSmooth = lerp(scrollSmooth, scrollT, 0.08);
    burst = Math.max(0, burst - dt * 1.6);

    cx = W / 2 - mouse.x * 18;
    cy = H * (W < 700 ? 0.34 : 0.4) - mouse.y * 14 - scrollSmooth * H * 0.12;

    // fond
    ctx.fillStyle = "#03040a";
    ctx.fillRect(0, 0, W, H);

    drawNebula(t);
    drawStars(t);
    drawRays(t, intro);

    // les fragments accélèrent au scroll et au clic (effet de « warp »)
    const warp = 1 + scrollSmooth * 4 + burst * 6;
    updateShards(dt, reduceMotion ? 0.15 : warp);
    drawShards(intro);

    // icosaèdre principal + un second, plus grand et plus discret, en contre-rotation
    const ax = t * 0.21 + mouse.y * 0.5;
    const ay = t * 0.33 + mouse.x * 0.6;
    const zoom = 1 + scrollSmooth * 0.35;
    drawPolyhedron(t, 1.55 * pop * zoom, -ax * 0.6, -ay * 0.5, t * 0.05, 0.18 * intro, false);
    drawPolyhedron(t, 1.0 * pop * zoom, ax, ay, 0.2, 0.9 * intro, true);

    drawCore(t, intro);

    drawRing(t, R * 0.55 * pop * zoom, 1.15 + Math.sin(t * 0.4) * 0.15, 0.5 + mouse.x * 0.2, t * 0.6, 0.9 * intro, 0.035, 0);
    drawRing(t, R * 0.48 * pop * zoom, 0.3, -0.9 + Math.sin(t * 0.3) * 0.2, -t * 0.8, 0.55 * intro, 0.05, 3);

    drawSparks(dt);

    // l'univers s'assombrit quand on descend, pour laisser respirer le contenu
    if (scrollSmooth > 0.01) {
      ctx.fillStyle = `rgba(3,4,10,${Math.min(scrollSmooth, 1) * 0.45})`;
      ctx.fillRect(0, 0, W, H);
    }

    // flash d'ouverture
    if (!reduceMotion && t < 1.2) {
      ctx.fillStyle = `rgba(255,255,255,${Math.max(0, 1 - t / 1.2) * 0.9})`;
      ctx.fillRect(0, 0, W, H);
    }

    requestAnimationFrame(frame);
  }

  // ---------- Texte « murmuré » tapé en boucle ----------
  const PHRASES = [
    "Réviser, c'est —",
    "Réviser, c'est — comprendre.",
    "Réviser, c'est — relier les idées.",
    "Réviser, c'est — prendre confiance.",
    "Réviser, c'est — réussir le CRPE.",
  ];
  const typedEl = document.getElementById("typed");

  function typeLoop() {
    if (reduceMotion) { typedEl.textContent = PHRASES[PHRASES.length - 1]; return; }
    let pi = 0, ci = 0, deleting = false;
    const prefix = "Réviser, c'est — ";
    const tick = () => {
      const full = PHRASES[pi];
      if (!deleting) {
        ci++;
        typedEl.textContent = full.slice(0, ci);
        if (ci >= full.length) {
          deleting = true;
          return setTimeout(tick, pi === 0 ? 900 : 2200);
        }
        return setTimeout(tick, rand(45, 95));
      }
      // on n'efface que la fin, le début reste affiché
      const keep = full.length > prefix.length ? prefix.length : full.length;
      ci--;
      typedEl.textContent = full.slice(0, ci);
      if (ci <= keep) {
        deleting = false;
        pi = (pi + 1) % PHRASES.length;
        if (pi === 0) pi = 1;
        return setTimeout(tick, 350);
      }
      setTimeout(tick, 30);
    };
    setTimeout(tick, 1200);
  }

  // ---------- Apparitions au scroll + cartes réactives ----------
  function setupReveal() {
    const els = document.querySelectorAll(".reveal");
    if (!("IntersectionObserver" in window)) {
      els.forEach((el) => el.classList.add("in"));
      return;
    }
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
    }, { rootMargin: "0px 0px 160px 0px" });
    els.forEach((el) => io.observe(el));

    document.querySelectorAll(".card").forEach((card) => {
      card.addEventListener("pointermove", (e) => {
        const b = card.getBoundingClientRect();
        const x = (e.clientX - b.left) / b.width, y = (e.clientY - b.top) / b.height;
        card.style.setProperty("--mx", `${x * 100}%`);
        card.style.setProperty("--my", `${y * 100}%`);
        if (!reduceMotion) card.style.transform = `perspective(800px) rotateX(${(0.5 - y) * 8}deg) rotateY(${(x - 0.5) * 8}deg)`;
      });
      card.addEventListener("pointerleave", () => { card.style.transform = ""; });
    });

    // boutons « magnétiques »
    if (!reduceMotion) {
      document.querySelectorAll(".cta .btn").forEach((btn) => {
        btn.addEventListener("pointermove", (e) => {
          const b = btn.getBoundingClientRect();
          const x = e.clientX - b.left - b.width / 2, y = e.clientY - b.top - b.height / 2;
          btn.style.transform = `translate(${x * 0.18}px, ${y * 0.25}px)`;
        });
        btn.addEventListener("pointerleave", () => { btn.style.transform = ""; });
      });
    }
  }

  // ---------- Démarrage ----------
  let resizeTimer;
  window.addEventListener("resize", () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => { resize(); build(); }, 120);
  });

  resize();
  build();
  requestAnimationFrame(frame);
  requestAnimationFrame(() => document.body.classList.add("ready"));
  typeLoop();
  setupReveal();
})();
