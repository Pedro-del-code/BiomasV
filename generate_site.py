biomes = [
    {
        "id": "amazonia",
        "name": "Amazônia",
        "area": "4,1 milhões km²",
        "coverage": "49%",
        "color": "#1a472a",
        "accent": "#52b788",
        "light": "#d8f3dc",
        "icon": "🌿",
        "states": "AM, PA, AC, RO, RR, AP, MT, TO, MA",
        "climate": "Equatorial úmido",
        "fauna": ["Onça-pintada", "Boto-cor-de-rosa", "Arara-azul", "Tartaruga-da-amazônia"],
        "flora": ["Seringueira", "Vitória-régia", "Açaí", "Castanheira-do-pará"],
        "threats": ["Desmatamento", "Garimpo ilegal", "Queimadas"],
        "description": "A maior floresta tropical do mundo, o pulmão do planeta. Abriga cerca de 10% de todas as espécies vivas da Terra e regula o clima de toda a América do Sul através dos chamados 'rios voadores'.",
        "shape": "M0,60 L20,20 L60,10 L100,30 L120,60 L110,100 L70,120 L30,110 L0,80 Z",
        "gradient": ["#1a472a", "#2d6a4f", "#40916c"],
    },
    {
        "id": "cerrado",
        "name": "Cerrado",
        "area": "2 milhões km²",
        "coverage": "24%",
        "color": "#7c4f00",
        "accent": "#e8a020",
        "light": "#fff3cd",
        "icon": "🌾",
        "states": "GO, MT, MS, MG, BA, TO, MA, PI, SP, PR, RO, PA, AM",
        "climate": "Tropical sazonal",
        "fauna": ["Lobo-guará", "Tamanduá-bandeira", "Ema", "Cervo-do-pantanal"],
        "flora": ["Ipê-amarelo", "Buriti", "Pequi", "Barbatimão"],
        "threats": ["Agropecuária", "Monocultura", "Fogo"],
        "description": "A savana mais biodiversa do mundo e o segundo maior bioma brasileiro. Conhecido como 'berço das águas', é onde nascem as principais bacias hidrográficas do Brasil, como São Francisco, Paraná e Araguaia.",
        "shape": "M10,40 L50,10 L90,20 L110,50 L100,90 L60,110 L20,100 L0,70 Z",
        "gradient": ["#7c4f00", "#a0522d", "#c8832a"],
    },
    {
        "id": "mata-atlantica",
        "name": "Mata Atlântica",
        "area": "1,1 milhão km²",
        "coverage": "13%",
        "color": "#1b4332",
        "accent": "#74c69d",
        "light": "#d8f3dc",
        "icon": "🦋",
        "states": "ES, RJ, SP, PR, SC, RS, BA, MG e outros litorâneos",
        "climate": "Tropical e Subtropical úmido",
        "fauna": ["Mico-leão-dourado", "Muriqui", "Jaguarundi", "Sabiá-laranjeira"],
        "flora": ["Pau-brasil", "Jequitibá-rosa", "Araucária", "Bromélia"],
        "threats": ["Urbanização", "Fragmentação", "Desmatamento"],
        "description": "Um dos hotspots de biodiversidade mais ameaçados do planeta. Restam apenas 12% de sua cobertura original, mas ainda abriga mais de 20.000 espécies de plantas e é lar de 72% da população brasileira.",
        "shape": "M5,30 L30,5 L70,15 L100,40 L95,80 L70,105 L30,100 L5,75 Z",
        "gradient": ["#1b4332", "#2d6a4f", "#52b788"],
    },
    {
        "id": "caatinga",
        "name": "Caatinga",
        "area": "844 mil km²",
        "coverage": "10%",
        "color": "#6b3a2a",
        "accent": "#e07b39",
        "light": "#fde8d8",
        "icon": "🌵",
        "states": "CE, PI, RN, PB, PE, AL, SE, BA, MG",
        "climate": "Semiárido",
        "fauna": ["Ararinha-azul", "Gato-do-mato", "Tatu-bola", "Preá"],
        "flora": ["Mandacaru", "Umbu", "Juazeiro", "Palma-forrageira"],
        "threats": ["Desertificação", "Superexploração", "Seca"],
        "description": "O único bioma exclusivamente brasileiro e a única savana semiárida tropical do mundo. Resiliente e única, a caatinga ('mata branca' em tupi) abriga espécies adaptadas à escassez extrema de água.",
        "shape": "M15,35 L45,8 L80,18 L105,45 L100,80 L75,105 L35,98 L8,70 Z",
        "gradient": ["#6b3a2a", "#8b4513", "#c0632a"],
    },
    {
        "id": "pampa",
        "name": "Pampa",
        "area": "176 mil km²",
        "coverage": "2%",
        "color": "#3d5a1a",
        "accent": "#a8c957",
        "light": "#f0f7e0",
        "icon": "🐎",
        "states": "RS",
        "climate": "Subtropical úmido",
        "fauna": ["Veado-campeiro", "Graxaim-do-campo", "Seriema", "Tatu-peludo"],
        "flora": ["Capim-caninha", "Erva-mate", "Espinilho", "Coronilha"],
        "threats": ["Pecuária intensiva", "Monocultura de soja", "Silvicultura"],
        "description": "Os campos sulinos que se estendem pela Argentina e Uruguai. O menor bioma brasileiro em território nacional, caracterizado por campos abertos, coxilhas onduladas e rica biodiversidade de gramíneas nativas.",
        "shape": "M10,45 L45,12 L85,22 L108,50 L95,85 L65,108 L28,100 L5,72 Z",
        "gradient": ["#3d5a1a", "#4a7a25", "#6ba535"],
    },
    {
        "id": "pantanal",
        "name": "Pantanal",
        "area": "150 mil km²",
        "coverage": "1,76%",
        "color": "#005f73",
        "accent": "#0abdc6",
        "light": "#caf0f8",
        "icon": "🐊",
        "states": "MT, MS",
        "climate": "Tropical continental",
        "fauna": ["Onça-pintada", "Tuiuiú", "Capivara", "Jacaré-do-pantanal"],
        "flora": ["Cambará", "Bocaiúva", "Paratudo", "Camalote"],
        "threats": ["Queimadas", "Seca", "Pecuária extensiva"],
        "description": "A maior planície alagável do mundo e o maior berçário natural do planeta. Patrimônio Natural da Humanidade pela UNESCO, concentra a maior densidade de onças-pintadas do mundo e 650 espécies de aves.",
        "shape": "M8,42 L42,10 L82,20 L110,48 L102,84 L68,110 L25,102 L5,68 Z",
        "gradient": ["#005f73", "#0a7a8c", "#1a9eaa"],
    },
    {
        "id": "oceanico",
        "name": "Zona Marinha",
        "area": "3,5 milhões km²",
        "coverage": "Zona Econômica",
        "color": "#023e8a",
        "accent": "#48cae4",
        "light": "#caf0f8",
        "icon": "🐋",
        "states": "Todo o litoral brasileiro — 7.491 km",
        "climate": "Oceânico tropical e subtropical",
        "fauna": ["Tartaruga-marinha", "Baleia-jubarte", "Peixe-boi-marinho", "Manta-raia"],
        "flora": ["Manguezal", "Restinga", "Recifes de coral", "Algas marinhas"],
        "threats": ["Poluição plástica", "Pesca predatória", "Branqueamento de corais"],
        "description": "O Brasil possui uma das maiores zonas econômicas exclusivas do mundo. Nossos oceanos abrigam o Arquipélago de Fernando de Noronha, o Atol das Rocas e recifes coralinos únicos no Atlântico Sul.",
        "shape": "M5,50 L25,15 L65,8 L100,28 L115,60 L105,95 L70,115 L25,108 L0,80 Z",
        "gradient": ["#023e8a", "#0353a4", "#0466c8"],
    },
]

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Biomas do Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg: #0d0d0d;
      --surface: #141414;
      --border: rgba(255,255,255,0.08);
      --text: #f0ece4;
      --muted: #888;
    }

    html { scroll-behavior: smooth; }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'DM Sans', sans-serif;
      font-weight: 300;
      overflow-x: hidden;
    }

    /* ── HERO ── */
    .hero {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
      padding: 4rem 2rem;
      text-align: center;
    }

    .hero-bg {
      position: absolute; inset: 0;
      background: radial-gradient(ellipse 80% 60% at 50% 40%, #0f3d1a 0%, #0d0d0d 70%);
    }

    .hero-noise {
      position: absolute; inset: 0;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
      opacity: 0.5;
    }

    .hero-label {
      position: relative;
      font-size: 0.7rem;
      letter-spacing: 0.35em;
      text-transform: uppercase;
      color: #52b788;
      margin-bottom: 1.5rem;
      opacity: 0;
      animation: fadeUp 0.8s 0.2s forwards;
    }

    .hero h1 {
      position: relative;
      font-family: 'Playfair Display', serif;
      font-size: clamp(3.5rem, 10vw, 9rem);
      font-weight: 900;
      line-height: 0.92;
      letter-spacing: -0.03em;
      opacity: 0;
      animation: fadeUp 0.9s 0.4s forwards;
    }

    .hero h1 em {
      font-style: italic;
      color: #52b788;
    }

    .hero-sub {
      position: relative;
      max-width: 540px;
      margin: 2rem auto 0;
      font-size: 1rem;
      color: var(--muted);
      line-height: 1.7;
      opacity: 0;
      animation: fadeUp 0.9s 0.6s forwards;
    }

    .hero-scroll {
      position: absolute;
      bottom: 2.5rem;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.65rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--muted);
      opacity: 0;
      animation: fadeUp 1s 1s forwards;
    }

    .scroll-line {
      width: 1px;
      height: 40px;
      background: linear-gradient(to bottom, #52b788, transparent);
      animation: scrollPulse 2s infinite;
    }

    /* ── STATS BAR ── */
    .stats-bar {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
    }

    .stat {
      padding: 2rem;
      text-align: center;
      border-right: 1px solid var(--border);
    }
    .stat:last-child { border-right: none; }

    .stat-number {
      font-family: 'Playfair Display', serif;
      font-size: 2.5rem;
      font-weight: 700;
      color: #52b788;
    }

    .stat-label {
      font-size: 0.7rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--muted);
      margin-top: 0.3rem;
    }

    /* ── GRID SECTION ── */
    .section-header {
      padding: 5rem 4rem 3rem;
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      border-bottom: 1px solid var(--border);
    }

    .section-title {
      font-family: 'Playfair Display', serif;
      font-size: clamp(2rem, 4vw, 3.5rem);
      font-weight: 700;
      line-height: 1.1;
    }

    .section-count {
      font-size: 0.7rem;
      letter-spacing: 0.2em;
      color: var(--muted);
      text-transform: uppercase;
      padding-bottom: 0.5rem;
    }

    .biomes-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
    }

    /* ── BIOME CARD ── */
    .biome-card {
      border-right: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
      padding: 0;
      overflow: hidden;
      cursor: pointer;
      position: relative;
      transition: background 0.3s;
    }

    .biome-card:hover { background: rgba(255,255,255,0.02); }

    .card-visual {
      height: 220px;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .card-bg-gradient {
      position: absolute; inset: 0;
      opacity: 0.85;
      transition: opacity 0.4s, transform 0.4s;
    }

    .biome-card:hover .card-bg-gradient {
      opacity: 1;
      transform: scale(1.03);
    }

    .card-svg {
      position: relative;
      z-index: 1;
      transition: transform 0.4s;
      filter: drop-shadow(0 12px 32px rgba(0,0,0,0.5));
    }

    .biome-card:hover .card-svg { transform: scale(1.06) translateY(-4px); }

    .card-area-badge {
      position: absolute;
      bottom: 1rem;
      right: 1rem;
      background: rgba(0,0,0,0.5);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 2rem;
      padding: 0.3rem 0.8rem;
      font-size: 0.65rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      z-index: 2;
    }

    .card-icon {
      position: absolute;
      top: 1rem;
      left: 1rem;
      font-size: 1.5rem;
      z-index: 2;
    }

    .card-body {
      padding: 1.8rem 2rem;
    }

    .card-number {
      font-size: 0.65rem;
      letter-spacing: 0.25em;
      color: var(--muted);
      text-transform: uppercase;
      margin-bottom: 0.4rem;
    }

    .card-name {
      font-family: 'Playfair Display', serif;
      font-size: 1.8rem;
      font-weight: 700;
      line-height: 1.1;
      margin-bottom: 1rem;
    }

    .card-desc {
      font-size: 0.85rem;
      color: #aaa;
      line-height: 1.7;
      margin-bottom: 1.5rem;
    }

    .card-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      margin-bottom: 1.5rem;
    }

    .tag {
      font-size: 0.65rem;
      letter-spacing: 0.08em;
      padding: 0.25rem 0.7rem;
      border-radius: 2rem;
      border: 1px solid var(--border);
      color: var(--muted);
      text-transform: uppercase;
    }

    .card-details {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      padding-top: 1.2rem;
      border-top: 1px solid var(--border);
    }

    .detail-group { }

    .detail-label {
      font-size: 0.6rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 0.3rem;
    }

    .detail-items {
      display: flex;
      flex-direction: column;
      gap: 0.15rem;
    }

    .detail-item {
      font-size: 0.75rem;
      color: #ccc;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .detail-item::before {
      content: '';
      width: 4px; height: 4px;
      border-radius: 50%;
      flex-shrink: 0;
    }

    .card-footer {
      padding: 1rem 2rem;
      border-top: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .climate-chip {
      font-size: 0.65rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--muted);
    }

    .coverage-bar {
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .bar-track {
      width: 80px;
      height: 2px;
      background: var(--border);
      border-radius: 2px;
      overflow: hidden;
    }

    .bar-fill {
      height: 100%;
      border-radius: 2px;
      transition: width 1s ease;
    }

    .coverage-pct {
      font-size: 0.7rem;
      color: var(--muted);
      min-width: 32px;
      text-align: right;
    }

    /* ── THREATS ── */
    .threats-section {
      display: grid;
      grid-template-columns: 1fr 1fr;
    }

    .threats-left {
      padding: 4rem;
      border-right: 1px solid var(--border);
    }

    .threats-right {
      padding: 4rem;
    }

    .threats-title {
      font-family: 'Playfair Display', serif;
      font-size: 2rem;
      margin-bottom: 2rem;
    }

    .threat-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .threat-item {
      display: flex;
      align-items: center;
      gap: 1rem;
      padding: 1rem;
      border: 1px solid var(--border);
      border-radius: 4px;
      font-size: 0.85rem;
    }

    .threat-dot {
      width: 8px; height: 8px;
      border-radius: 50%;
      background: #e07b39;
      flex-shrink: 0;
    }

    /* ── FOOTER ── */
    footer {
      padding: 4rem;
      border-top: 1px solid var(--border);
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
    }

    .footer-brand {
      font-family: 'Playfair Display', serif;
      font-size: 1.5rem;
      font-weight: 700;
    }

    .footer-brand span { color: #52b788; }

    .footer-copy {
      font-size: 0.75rem;
      color: var(--muted);
      margin-top: 0.5rem;
      line-height: 1.6;
    }

    .footer-right {
      text-align: right;
      font-size: 0.75rem;
      color: var(--muted);
      line-height: 1.9;
    }

    /* ── ANIMATIONS ── */
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(24px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes scrollPulse {
      0%, 100% { opacity: 0.4; }
      50% { opacity: 1; }
    }

    /* ── RESPONSIVE ── */
    @media (max-width: 768px) {
      .stats-bar { grid-template-columns: 1fr; }
      .stat { border-right: none; border-bottom: 1px solid var(--border); }
      .section-header { padding: 3rem 1.5rem 2rem; flex-direction: column; align-items: flex-start; gap: 0.5rem; }
      .biomes-grid { grid-template-columns: 1fr; }
      .threats-section { grid-template-columns: 1fr; }
      .threats-left { border-right: none; border-bottom: 1px solid var(--border); padding: 2rem 1.5rem; }
      .threats-right { padding: 2rem 1.5rem; }
      footer { grid-template-columns: 1fr; }
      .footer-right { text-align: left; }
      .card-details { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

<!-- HERO -->
<section class="hero">
  <div class="hero-bg"></div>
  <div class="hero-noise"></div>
  <p class="hero-label">República Federativa do Brasil</p>
  <h1>Biomas<br><em>do Brasil</em></h1>
  <p class="hero-sub">
    Do Equador ao Pampa, da Caatinga aos oceanos — sete ecossistemas que definem a maior biodiversidade do planeta.
  </p>
  <div class="hero-scroll">
    <div class="scroll-line"></div>
    Explorar
  </div>
</section>

<!-- STATS -->
<div class="stats-bar">
  <div class="stat">
    <div class="stat-number">7</div>
    <div class="stat-label">Biomas reconhecidos</div>
  </div>
  <div class="stat">
    <div class="stat-number">~1/5</div>
    <div class="stat-label">Das espécies do planeta</div>
  </div>
  <div class="stat">
    <div class="stat-number">8,5M</div>
    <div class="stat-label">km² de território</div>
  </div>
</div>

<!-- GRID -->
<div class="section-header">
  <h2 class="section-title">Os Sete<br>Ecossistemas</h2>
  <span class="section-count">07 biomas catalogados</span>
</div>

<div class="biomes-grid">
"""

all_threats = []
for b in biomes:
    for t in b["threats"]:
        if t not in all_threats:
            all_threats.append(t)

for i, b in enumerate(biomes):
    num = str(i + 1).zfill(2)
    g1, g2, g3 = b["gradient"]
    
    # coverage bar width (terrestrial biomes: max ~49%, marine special)
    try:
        cov_float = float(b["coverage"].replace("%","").replace(",","."))
        bar_w = min(int(cov_float / 50 * 100), 100)
    except:
        bar_w = 70

    fauna_items = "".join([f'<div class="detail-item" style="--dot-color:{b["accent"]}">{f}</div>' for f in b["fauna"][:3]])
    flora_items = "".join([f'<div class="detail-item" style="--dot-color:{b["accent"]}">{f}</div>' for f in b["flora"][:3]])

    tags_html = "".join([f'<span class="tag" style="border-color:{b["accent"]}33;color:{b["accent"]}">{t}</span>' for t in b["threats"]])

    html_content += f"""
  <article class="biome-card">
    <div class="card-visual">
      <div class="card-bg-gradient" style="background: linear-gradient(135deg, {g1} 0%, {g2} 50%, {g3} 100%);"></div>
      <span class="card-icon">{b["icon"]}</span>
      <svg class="card-svg" width="140" height="140" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="{b['shape']}" fill="{b['accent']}" opacity="0.25"/>
        <path d="{b['shape']}" stroke="{b['accent']}" stroke-width="1.5" fill="none" opacity="0.9"/>
        <path d="{b['shape']}" fill="{b['accent']}" opacity="0.08"/>
      </svg>
      <div class="card-area-badge">{b["area"]}</div>
    </div>
    <div class="card-body">
      <div class="card-number">Bioma {num}</div>
      <h2 class="card-name" style="color:{b['accent']}">{b["name"]}</h2>
      <p class="card-desc">{b["description"]}</p>
      <div class="card-tags">{tags_html}</div>
      <div class="card-details">
        <div class="detail-group">
          <div class="detail-label">Fauna emblema</div>
          <div class="detail-items">
            {"".join([f'<div class="detail-item"><span style="display:inline-block;width:4px;height:4px;border-radius:50%;background:{b["accent"]};flex-shrink:0"></span>{f}</div>' for f in b["fauna"][:3]])}
          </div>
        </div>
        <div class="detail-group">
          <div class="detail-label">Flora nativa</div>
          <div class="detail-items">
            {"".join([f'<div class="detail-item"><span style="display:inline-block;width:4px;height:4px;border-radius:50%;background:{b["accent"]};flex-shrink:0"></span>{f}</div>' for f in b["flora"][:3]])}
          </div>
        </div>
      </div>
    </div>
    <div class="card-footer">
      <span class="climate-chip">☁ {b["climate"]}</span>
      <div class="coverage-bar">
        <div class="bar-track">
          <div class="bar-fill" style="width:{bar_w}%;background:{b['accent']};"></div>
        </div>
        <span class="coverage-pct">{b["coverage"]}</span>
      </div>
    </div>
  </article>
"""

html_content += """
</div>

<!-- THREATS -->
<div class="threats-section" style="border-top:1px solid var(--border);margin-top:2rem;">
  <div class="threats-left">
    <h3 class="threats-title">Ameaças aos<br><em style="font-style:italic;color:#e07b39">Ecossistemas</em></h3>
    <p style="font-size:0.85rem;color:#888;line-height:1.7;margin-bottom:2rem;">
      A biodiversidade brasileira enfrenta pressões crescentes que ameaçam o equilíbrio de ecossistemas únicos no mundo.
    </p>
    <ul class="threat-list">
"""

unique_threats = []
for b in biomes:
    for t in b["threats"]:
        if t not in unique_threats:
            unique_threats.append(t)

for t in unique_threats[:8]:
    html_content += f"""
      <li class="threat-item">
        <div class="threat-dot"></div>
        {t}
      </li>
"""

html_content += """
    </ul>
  </div>
  <div class="threats-right">
    <div style="padding:2rem;background:rgba(255,255,255,0.02);border:1px solid var(--border);border-radius:4px;margin-bottom:1.5rem;">
      <div style="font-size:0.65rem;letter-spacing:0.2em;text-transform:uppercase;color:#888;margin-bottom:0.5rem">Dados críticos</div>
      <div style="font-family:'Playfair Display',serif;font-size:3rem;font-weight:700;color:#e07b39">88%</div>
      <div style="font-size:0.85rem;color:#888;margin-top:0.3rem">da Mata Atlântica já foi destruída</div>
    </div>
    <div style="padding:2rem;background:rgba(255,255,255,0.02);border:1px solid var(--border);border-radius:4px;margin-bottom:1.5rem;">
      <div style="font-size:0.65rem;letter-spacing:0.2em;text-transform:uppercase;color:#888;margin-bottom:0.5rem">Espécies ameaçadas</div>
      <div style="font-family:'Playfair Display',serif;font-size:3rem;font-weight:700;color:#e8a020">+1.200</div>
      <div style="font-size:0.85rem;color:#888;margin-top:0.3rem">espécies em risco de extinção no Brasil</div>
    </div>
    <div style="padding:2rem;background:rgba(255,255,255,0.02);border:1px solid var(--border);border-radius:4px;">
      <div style="font-size:0.65rem;letter-spacing:0.2em;text-transform:uppercase;color:#888;margin-bottom:0.5rem">Área desmatada/ano</div>
      <div style="font-family:'Playfair Display',serif;font-size:3rem;font-weight:700;color:#48cae4">~11K</div>
      <div style="font-size:0.85rem;color:#888;margin-top:0.3rem">km² de Amazônia desmatados por ano (média)</div>
    </div>
  </div>
</div>

<!-- FOOTER -->
<footer>
  <div>
    <div class="footer-brand">Biomas <span>Brasil</span></div>
    <p class="footer-copy">
      Um guia visual e educativo sobre os ecossistemas que compõem a nação megadiversa.<br>
      Gerado com Python · Hospedado no Render.
    </p>
  </div>
  <div class="footer-right">
    Amazônia · Cerrado · Mata Atlântica<br>
    Caatinga · Pampa · Pantanal<br>
    Zona Marinha
  </div>
</footer>

</body>
</html>
"""

with open("/home/claude/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ index.html gerado com sucesso!")
print(f"   {len(biomes)} biomas incluídos")
print(f"   {len(html_content)} caracteres")
