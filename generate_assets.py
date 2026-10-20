#!/usr/bin/env python3
"""
Cyberpunk Neon Asset Generator for fauzan667 GitHub Profile
Generates high-tech, futuristic SVG cards with moving neon lighting borders,
glowing cyber HUD elements, celestial neon dragon animations, metrics ridges,
cyber terminals, and native GitHub trophies.
"""

import os
import sys
import math
import xml.etree.ElementTree as ET

# Ensure UTF-8 output even in Windows cmd/PowerShell
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
DIST_DIR = os.path.join(BASE_DIR, "dist")

os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(DIST_DIR, exist_ok=True)


def validate_and_save(svg_content: str, filename: str):
    """Validates SVG XML syntax and saves to both assets/ and dist/."""
    try:
        ET.fromstring(svg_content)
    except ET.ParseError as e:
        print(f"[-] XML Parse Error in {filename}: {e}")
        raise e

    for out_dir in [ASSETS_DIR, DIST_DIR]:
        path = os.path.join(out_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg_content)
    print(f"[+] Successfully generated: {filename}")


# ==============================================================================
# 0. NEON DIVIDER BAR (neon-bar.svg)
# ==============================================================================
def generate_neon_bar() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 24" width="100%" height="24">
  <defs>
    <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#060814" stop-opacity="0"/>
      <stop offset="15%" stop-color="#060814" stop-opacity="0.2"/>
      <stop offset="35%" stop-color="#a855f7"/>
      <stop offset="50%" stop-color="#00f7ff"/>
      <stop offset="65%" stop-color="#00ff88"/>
      <stop offset="85%" stop-color="#060814" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#060814" stop-opacity="0"/>
    </linearGradient>
    <filter id="barGlow" x="-20%" y="-100%" width="140%" height="300%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background Base Line -->
  <line x1="20" y1="12" x2="920" y2="12" stroke="#1e293b" stroke-width="1.2" opacity="0.4"/>

  <!-- Glowing Neon Laser Line -->
  <line x1="40" y1="12" x2="900" y2="12" stroke="url(#barGrad)" stroke-width="2.5" filter="url(#barGlow)"/>

  <!-- Left and Right Cyber Reticles -->
  <circle cx="160" cy="12" r="3.5" fill="#a855f7" filter="url(#barGlow)"/>
  <circle cx="780" cy="12" r="3.5" fill="#00ff88" filter="url(#barGlow)"/>

  <!-- Center Diamond HUD Anchor -->
  <polygon points="470,6 476,12 470,18 464,12" fill="#00f7ff" filter="url(#barGlow)"/>
  <circle cx="470" cy="12" r="1.5" fill="#ffffff"/>

  <!-- Traversal Energy Pulse -->
  <circle cx="470" cy="12" r="4.5" fill="#ffffff" filter="url(#barGlow)">
    <animate attributeName="cx" values="180;760;180" dur="4.2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.8;1;0.8" dur="4.2s" repeatCount="indefinite"/>
  </circle>
</svg>'''


# ==============================================================================
# 1. CYBERPUNK HOLOGRAM HEADER (header.svg)
# Clean, aesthetic, no lightning icon, no cluttered top status bar
# ==============================================================================
def generate_header() -> str:
    # Equalizer Bars for HUD Sides
    eq_left = []
    eq_right = []
    bar_heights = [
        ("12;36;20;46;28;12", "1.6s"),
        ("26;14;42;18;48;26", "1.9s"),
        ("16;44;24;32;14;16", "1.4s"),
        ("38;20;48;28;16;38", "2.1s"),
        ("20;40;14;44;30;20", "1.7s"),
        ("30;16;38;22;42;30", "1.5s"),
        ("14;34;20;48;24;14", "1.8s"),
    ]
    for idx, (vals, dur) in enumerate(bar_heights):
        xl = 48 + idx * 14
        xr = 800 + idx * 14
        eq_left.append(f'''<rect x="{xl}" y="88" width="6" height="26" rx="3" fill="#00f7ff" opacity="0.85" filter="url(#glowNeon)">
          <animate attributeName="height" values="{vals}" dur="{dur}" repeatCount="indefinite"/>
          <animate attributeName="y" values="{88 - 6};{88 - 20};{88 - 10};{88 - 24};{88 - 12};{88 - 6}" dur="{dur}" repeatCount="indefinite"/>
        </rect>''')
        eq_right.append(f'''<rect x="{xr}" y="88" width="6" height="26" rx="3" fill="#a855f7" opacity="0.85" filter="url(#glowNeon)">
          <animate attributeName="height" values="{vals}" dur="{dur}" repeatCount="indefinite"/>
          <animate attributeName="y" values="{88 - 6};{88 - 20};{88 - 10};{88 - 24};{88 - 12};{88 - 6}" dur="{dur}" repeatCount="indefinite"/>
        </rect>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 220" width="100%">
  <defs>
    <!-- Lighting Border Gradient -->
    <linearGradient id="headBorderNeon" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f7ff"/>
      <stop offset="50%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#00ff88"/>
    </linearGradient>

    <!-- Text Glow Filter -->
    <filter id="glowNeon" x="-20%" y="-30%" width="140%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="deepCyanGlow" x="-30%" y="-50%" width="160%" height="200%">
      <feGaussianBlur stdDeviation="10" result="blur1"/>
      <feGaussianBlur stdDeviation="4" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur1"/>
        <feMergeNode in="blur2"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Subtle Cyber Grid Pattern -->
    <pattern id="cyberGridHead" width="22" height="22" patternUnits="userSpaceOnUse">
      <path d="M 22 0 L 0 0 0 22" fill="none" stroke="#00f7ff" stroke-width="0.5" stroke-opacity="0.06"/>
      <circle cx="22" cy="0" r="0.8" fill="#00f7ff" fill-opacity="0.2"/>
    </pattern>
  </defs>

  <style>
    .title-font {{ font-family: 'Segoe UI', -apple-system, Roboto, Ubuntu, sans-serif; font-weight: 900; }}
    .mono-font {{ font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', Courier, monospace; }}
  </style>

  <!-- Card Background -->
  <rect x="6" y="6" width="928" height="208" rx="18" fill="#060814" stroke="#1e293b" stroke-width="1.8"/>
  <rect x="6" y="6" width="928" height="208" rx="18" fill="url(#cyberGridHead)"/>

  <!-- Animated Neon Lighting Border -->
  <rect x="6" y="6" width="928" height="208" rx="18" fill="none" stroke="url(#headBorderNeon)" stroke-width="3.2" filter="url(#glowNeon)" stroke-dasharray="240 320" stroke-linecap="round">
    <animate attributeName="stroke-dashoffset" from="0" to="-1120" dur="5s" repeatCount="indefinite"/>
  </rect>

  <!-- Corner HUD Tech Brackets -->
  <path d="M 18,34 L 18,18 L 34,18" stroke="#00f7ff" stroke-width="2.5" fill="none"/>
  <circle cx="18" cy="18" r="2.5" fill="#00f7ff"/>
  <path d="M 922,34 L 922,18 L 906,18" stroke="#a855f7" stroke-width="2.5" fill="none"/>
  <circle cx="922" cy="18" r="2.5" fill="#a855f7"/>
  <path d="M 18,186 L 18,202 L 34,202" stroke="#00ff88" stroke-width="2.5" fill="none"/>
  <circle cx="18" cy="202" r="2.5" fill="#00ff88"/>
  <path d="M 922,186 L 922,202 L 906,202" stroke="#00f7ff" stroke-width="2.5" fill="none"/>
  <circle cx="922" cy="202" r="2.5" fill="#00f7ff"/>

  <!-- SIDE EQUALIZERS (Holographic Audio Spectrum) -->
  {"".join(eq_left)}
  {"".join(eq_right)}

  <!-- Decorative Cyber Crosshairs (Low Opacity) -->
  <g opacity="0.25">
    <circle cx="110" cy="95" r="26" fill="none" stroke="#00f7ff" stroke-width="0.8" stroke-dasharray="3 3"/>
    <line x1="110" y1="65" x2="110" y2="125" stroke="#00f7ff" stroke-width="0.8"/>
    <line x1="80" y1="95" x2="140" y2="95" stroke="#00f7ff" stroke-width="0.8"/>

    <circle cx="830" cy="95" r="26" fill="none" stroke="#a855f7" stroke-width="0.8" stroke-dasharray="3 3"/>
    <line x1="830" y1="65" x2="830" y2="125" stroke="#a855f7" stroke-width="0.8"/>
    <line x1="800" y1="95" x2="860" y2="95" stroke="#a855f7" stroke-width="0.8"/>
  </g>

  <!-- PURE AESTHETIC NAME: Fauzan (NO ICONS, NO PETIR, CLEAN NEON GLOW) -->
  <!-- Glowing Shadow Layer 1 (Electric Cyan Deep Glow) -->
  <text x="470" y="88" fill="#00f7ff" class="title-font" font-size="64" letter-spacing="4" text-anchor="middle" filter="url(#deepCyanGlow)">
    Fauzan
  </text>
  <!-- Glowing Shadow Layer 2 (Neon Purple Glitch Layer) -->
  <text x="470" y="88" fill="#a855f7" class="title-font" font-size="64" letter-spacing="4" text-anchor="middle" filter="url(#glowNeon)" opacity="0.85">
    Fauzan
    <animate attributeName="dx" values="0;2;-2;1;0" dur="3.5s" repeatCount="indefinite"/>
  </text>
  <!-- Foreground Crisp Text with Neon Stroke and Subtle Glitch Breathing -->
  <text x="470" y="88" fill="#ffffff" stroke="#00f7ff" stroke-width="1.2" class="title-font" font-size="64" letter-spacing="4" text-anchor="middle">
    Fauzan
    <animate attributeName="opacity" values="1;0.92;1;0.96;1;0.88;1" dur="2.8s" repeatCount="indefinite"/>
  </text>

  <!-- SUBTITLE ANIMASI TYPING ALA CYBERPUNK -->
  <g transform="translate(470, 122)">
    <text x="0" y="0" fill="#93c5fd" class="mono-font" font-size="16" font-weight="600" letter-spacing="1.2" text-anchor="middle">
      Full-Stack Web Developer • Software Engineer • Tech Enthusiast
      <tspan fill="#00f7ff" font-weight="900"> █<animate attributeName="opacity" values="1;0;1" dur="0.85s" repeatCount="indefinite"/></tspan>
    </text>
  </g>

  <!-- Decorative Divider Under Subtitle -->
  <line x1="220" y1="142" x2="720" y2="142" stroke="url(#headBorderNeon)" stroke-width="1.2" opacity="0.6"/>
  <circle cx="470" cy="142" r="3" fill="#00ff88" filter="url(#glowNeon)"/>

  <!-- BOTTOM CYBER STATUS CAPSULES (Clean, No Emojis, No Petir) -->
  <!-- Capsule 1: FULL-STACK ARCHITECT -->
  <rect x="42" y="160" width="202" height="34" rx="9" fill="#0b122b" stroke="#00f7ff" stroke-width="1.2" stroke-opacity="0.6"/>
  <circle cx="58" cy="177" r="3.5" fill="#00f7ff" filter="url(#glowNeon)"/>
  <text x="70" y="181" fill="#e0f2fe" class="mono-font" font-size="11" font-weight="700">FULL-STACK ARCHITECT</text>

  <!-- Capsule 2: PRODUCTION QUALITY -->
  <rect x="258" y="160" width="202" height="34" rx="9" fill="#0b122b" stroke="#00ff88" stroke-width="1.2" stroke-opacity="0.6"/>
  <circle cx="274" cy="177" r="3.5" fill="#00ff88" filter="url(#glowNeon)"/>
  <text x="286" y="181" fill="#dcfce7" class="mono-font" font-size="11" font-weight="700">PRODUCTION GRADE</text>

  <!-- Capsule 3: AI-AUGMENTED WORKFLOW -->
  <rect x="474" y="160" width="208" height="34" rx="9" fill="#0b122b" stroke="#a855f7" stroke-width="1.2" stroke-opacity="0.6"/>
  <circle cx="490" cy="177" r="3.5" fill="#a855f7" filter="url(#glowNeon)"/>
  <text x="502" y="181" fill="#f3e8ff" class="mono-font" font-size="11" font-weight="700">AI-AUGMENTED FLOW</text>

  <!-- Capsule 4: READY TO DEPLOY -->
  <rect x="696" y="160" width="202" height="34" rx="9" fill="#0b122b" stroke="#f43f5e" stroke-width="1.2" stroke-opacity="0.6"/>
  <circle cx="712" cy="177" r="3.5" fill="#f43f5e" filter="url(#glowNeon)"/>
  <text x="724" y="181" fill="#ffe4e6" class="mono-font" font-size="11" font-weight="700">READY TO DEPLOY</text>

  <!-- Bottom Laser Sweep Line -->
  <line x1="30" y1="202" x2="910" y2="202" stroke="#1e293b" stroke-width="1"/>
  <circle cx="470" cy="202" r="3" fill="#00f7ff" filter="url(#glowNeon)">
    <animate attributeName="cx" values="60;880;60" dur="6s" repeatCount="indefinite"/>
  </circle>
</svg>'''


# ==============================================================================
# 2. FLOATING CORE TECH STACK & ARSENAL (tech-stack.svg)
# ==============================================================================
TECH_ICONS = {
    # Group 01: Languages & Core Technologies
    "PHP": '''<ellipse cx="27" cy="27" rx="20" ry="13" fill="#777bb4" fill-opacity="0.2" stroke="#777bb4" stroke-width="2"/>
        <text x="27" y="32" font-family="'Segoe UI', Roboto, sans-serif" font-weight="900" font-style="italic" font-size="14" fill="#ffffff" text-anchor="middle">php</text>''',

    "Laravel": '''<path d="M 27 13 L 41 20 L 41 35 L 27 42 L 13 35 L 13 20 Z" fill="none" stroke="#ff2d20" stroke-width="2.2"/>
        <path d="M 27 13 L 27 28 L 41 35" fill="none" stroke="#ff2d20" stroke-width="2.2"/>
        <path d="M 27 28 L 13 35" fill="none" stroke="#ff2d20" stroke-width="2.2"/>
        <path d="M 20 16.5 L 34 23.5" fill="none" stroke="#ff5544" stroke-width="1.8"/>
        <circle cx="27" cy="28" r="2.5" fill="#ff2d20"/>''',

    "HTML5": '''<polygon points="16,13 38,13 36,37 27,41 18,37" fill="#e34f26" fill-opacity="0.2" stroke="#e34f26" stroke-width="2"/>
        <polygon points="27,16 34.5,16 33,35 27,37.5" fill="#e34f26"/>
        <text x="27" y="31" font-family="'Segoe UI', sans-serif" font-weight="900" font-size="15" fill="#ffffff" text-anchor="middle">5</text>''',

    "CSS3": '''<polygon points="16,13 38,13 36,37 27,41 18,37" fill="#1572b6" fill-opacity="0.2" stroke="#1572b6" stroke-width="2"/>
        <polygon points="27,16 34.5,16 33,35 27,37.5" fill="#1572b6"/>
        <text x="27" y="31" font-family="'Segoe UI', sans-serif" font-weight="900" font-size="15" fill="#ffffff" text-anchor="middle">3</text>''',

    "JavaScript": '''<rect x="15" y="15" width="24" height="24" rx="5" fill="#f7df1e"/>
        <text x="27" y="33" font-family="'Segoe UI', Arial, sans-serif" font-weight="900" font-size="15" fill="#060814" text-anchor="middle">JS</text>''',

    "TypeScript": '''<rect x="15" y="15" width="24" height="24" rx="5" fill="#3178c6"/>
        <text x="27" y="33" font-family="'Segoe UI', Arial, sans-serif" font-weight="900" font-size="15" fill="#ffffff" text-anchor="middle">TS</text>''',

    "React": '''<ellipse cx="27" cy="27" rx="15" ry="6" fill="none" stroke="#00f7ff" stroke-width="1.8"/>
        <ellipse cx="27" cy="27" rx="15" ry="6" fill="none" stroke="#00f7ff" stroke-width="1.8" transform="rotate(60 27 27)"/>
        <ellipse cx="27" cy="27" rx="15" ry="6" fill="none" stroke="#00f7ff" stroke-width="1.8" transform="rotate(120 27 27)"/>
        <circle cx="27" cy="27" r="3" fill="#00f7ff"/>''',

    "Next.js": '''<circle cx="27" cy="27" r="14" fill="#060814" stroke="#ffffff" stroke-width="2"/>
        <path d="M 22 35 L 22 19 L 31.5 34" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round"/>
        <line x1="31.5" y1="19" x2="31.5" y2="26" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round"/>''',

    "Node.js": '''<polygon points="27,13 39,20 39,34 27,41 15,34 15,20" fill="none" stroke="#22c55e" stroke-width="2"/>
        <path d="M 21 29 Q 27 20 33 24 Q 27 35 21 29 Z" fill="#22c55e"/>''',

    "Python": '''<g transform="translate(1,0)">
          <path d="M 25 14 C 20 14 18 16 18 19 L 18 22 L 26 22 L 26 23 L 16 23 C 13 23 11 25 11 28 C 11 32 13 33 16 33 L 18 33 L 18 30 C 18 27 20 25 23 25 L 29 25 C 31 25 33 23 33 21 L 33 17 C 33 14 30 14 25 14 Z" fill="#38bdf8"/>
          <circle cx="21" cy="18" r="1.2" fill="#060814"/>
          <path d="M 27 40 C 32 40 34 38 34 35 L 34 32 L 26 32 L 26 31 L 36 31 C 39 31 41 29 41 26 C 41 22 39 21 36 21 L 34 21 L 34 24 C 34 27 32 29 29 29 L 23 29 C 21 29 19 31 19 33 L 19 37 C 19 40 22 40 27 40 Z" fill="#facc15"/>
          <circle cx="31" cy="36" r="1.2" fill="#060814"/>
        </g>''',

    # Group 02: Database & Cloud Environment
    "MySQL": '''<ellipse cx="27" cy="18" rx="13" ry="5" fill="none" stroke="#00758f" stroke-width="1.8"/>
        <path d="M 14 18 L 14 26 C 14 28.5 19.8 30.8 27 30.8 C 34.2 30.8 40 28.5 40 26 L 40 18" fill="none" stroke="#00758f" stroke-width="1.8"/>
        <path d="M 14 26 L 14 34 C 14 36.5 19.8 38.8 27 38.8 C 34.2 38.8 40 36.5 40 34 L 40 26" fill="none" stroke="#00f7ff" stroke-width="1.8"/>
        <path d="M 22 23 Q 27 18 32 22 Q 30 27 25 29" fill="none" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>''',

    "PostgreSQL": '''<circle cx="27" cy="27" r="14" fill="#336791" fill-opacity="0.25" stroke="#336791" stroke-width="2"/>
        <path d="M 21 21 C 24 18 30 18 33 21 C 36 24 35 29 32 31 C 30 33 28 34 28 38 C 27 38 26 38 26 36 C 26 34 27 32 28 30" fill="none" stroke="#60a5fa" stroke-width="2" stroke-linecap="round"/>
        <circle cx="23" cy="24" r="1.5" fill="#93c5fd"/>
        <path d="M 18 26 C 17 30 20 34 23 35" fill="none" stroke="#93c5fd" stroke-width="1.6"/>''',

    "MongoDB": '''<path d="M 27 13 C 27 13 17 22 17 29 C 17 35 21.5 39 27 41 C 32.5 39 37 35 37 29 C 37 22 27 13 27 13 Z" fill="#00ed64" fill-opacity="0.2" stroke="#00ed64" stroke-width="2"/>
        <path d="M 27 15 L 27 39" stroke="#00ed64" stroke-width="1.8" stroke-linecap="round"/>
        <path d="M 27 25 C 24 28 22 30 21 32" stroke="#00ed64" stroke-width="1.2"/>
        <path d="M 27 22 C 30 25 32 27 33 29" stroke="#00ed64" stroke-width="1.2"/>''',

    "Git": '''<g transform="translate(1,0)">
          <rect x="18" y="18" width="16" height="16" rx="3.5" transform="rotate(45 26 26)" fill="#f05032"/>
          <line x1="21" y1="21" x2="31" y2="31" stroke="#ffffff" stroke-width="2"/>
          <line x1="26" y1="26" x2="31" y2="21" stroke="#ffffff" stroke-width="2"/>
          <circle cx="21" cy="21" r="2.2" fill="#ffffff"/>
          <circle cx="31" cy="31" r="2.2" fill="#ffffff"/>
          <circle cx="31" cy="21" r="2.2" fill="#ffffff"/>
        </g>''',

    "GitHub": '''<g transform="translate(1,1)">
          <path d="M 26 13 C 18.8 13 13 18.8 13 26 C 13 31.8 16.7 36.6 22 38.3 C 22.6 38.5 22.8 38 22.8 37.7 L 22.8 35.6 C 19.2 36.4 18.4 33.9 18.4 33.9 C 17.8 32.4 17 32 17 32 C 15.8 31.2 17.1 31.2 17.1 31.2 C 18.4 31.3 19.1 32.6 19.1 32.6 C 20.3 34.6 22.2 34 23 33.7 C 23.1 32.8 23.5 32.2 23.9 31.8 C 21 31.5 18 30.4 18 25.3 C 18 23.9 18.5 22.7 19.3 21.8 C 19.2 21.4 18.7 20.1 19.5 18.3 C 19.5 18.3 20.6 18 23 19.6 C 24 19.3 25.1 19.2 26.2 19.2 C 27.3 19.2 28.4 19.3 29.4 19.6 C 31.8 18 32.9 18.3 32.9 18.3 C 33.7 20.1 33.2 21.4 33.1 21.8 C 33.9 22.7 34.4 23.9 34.4 25.3 C 34.4 30.4 31.4 31.5 28.5 31.8 C 29 32.2 29.4 33.1 29.4 34.3 L 29.4 37.7 C 29.4 38 29.6 38.5 30.2 38.3 C 35.3 36.6 39 31.8 39 26 C 39 18.8 33.2 13 26 13 Z" fill="#f0f6fc"/>
        </g>''',

    "VS Code": '''<path d="M 37 14 L 28 22 L 23 18 L 17 22 L 15 24 L 17 26 L 23 30 L 28 26 L 37 34 L 40 32 L 40 16 Z" fill="none" stroke="#007acc" stroke-width="2" stroke-linejoin="round"/>
        <path d="M 37 14 L 22 27 L 17 24 L 28 32 L 37 34 Z" fill="#007acc" opacity="0.6"/>
        <path d="M 37 14 L 40 16 L 40 32 L 37 34 Z" fill="#007acc"/>
        <path d="M 28 22 L 37 14 L 37 34 L 28 26 Z" fill="#38bdf8" opacity="0.8"/>''',

    "Figma": '''<rect x="18" y="14" width="9" height="9" rx="4.5" fill="#f24e1e"/>
        <rect x="27" y="14" width="9" height="9" rx="4.5" fill="#ff7262"/>
        <rect x="18" y="23" width="9" height="9" rx="4.5" fill="#a259ff"/>
        <circle cx="31.5" cy="27.5" r="4.5" fill="#1abcfe"/>
        <path d="M 18 32 H 27 V 36.5 A 4.5 4.5 0 0 1 18 36.5 Z" fill="#0acf83"/>''',

    "Vercel": '''<polygon points="27,15 39,37 15,37" fill="#ffffff"/>''',

    "Docker": '''<path d="M 13 29 C 13 35 19 37 28 37 C 37 37 41 32 41 29 C 39 28.5 36 29 34 28 C 33 26 35 24 36 23 C 33 23 30 25 29 27 C 25 27 22 27 18 29 C 16 29 14 29 13 29 Z" fill="#2496ed"/>
        <circle cx="18" cy="31" r="1.3" fill="#ffffff"/>
        <rect x="19" y="23" width="3.2" height="3.2" fill="#38bdf8"/>
        <rect x="23.5" y="23" width="3.2" height="3.2" fill="#38bdf8"/>
        <rect x="28" y="23" width="3.2" height="3.2" fill="#38bdf8"/>
        <rect x="23.5" y="19" width="3.2" height="3.2" fill="#38bdf8"/>
        <rect x="28" y="19" width="3.2" height="3.2" fill="#38bdf8"/>''',

    # Group 03: AI Coding Assistants & Agents
    "ChatGPT": '''<g transform="translate(27,27) scale(0.95)">
        <path d="M 0 -13 C 4 -13 8 -10 9 -6 L 9 -2 L 12 -2 C 15 -2 17 1 16 4 L 14 8 L 16 10 C 18 12 17 16 14 17 L 11 18 L 10 21 C 8 24 5 25 2 24 L -2 22 L -4 24 C -7 26 -11 25 -12 22 L -13 18 L -16 18 C -19 17 -20 13 -18 10 L -16 8 L -18 5 C -20 2 -18 -2 -15 -3 L -11 -3 L -10 -7 C -9 -11 -5 -13 0 -13 Z" fill="none" stroke="#00a67e" stroke-width="2"/>
        <circle cx="0" cy="0" r="4.5" fill="#00a67e" fill-opacity="0.35" stroke="#00a67e" stroke-width="1.8"/>
      </g>''',

    "Gemini": '''<path d="M 27 13 C 27 20.5 21.5 26 14 27 C 21.5 28 27 33.5 27 41 C 27 33.5 32.5 28 40 27 C 32.5 26 27 20.5 27 13 Z" fill="url(#geminiGrad)" filter="url(#techSoftGlow)"/>''',

    "Claude": '''<g transform="translate(27,27)">
        <line x1="0" y1="-12" x2="0" y2="12" stroke="#d97706" stroke-width="3" stroke-linecap="round"/>
        <line x1="-12" y1="0" x2="12" y2="0" stroke="#d97706" stroke-width="3" stroke-linecap="round"/>
        <line x1="-8.5" y1="-8.5" x2="8.5" y2="8.5" stroke="#d97706" stroke-width="3" stroke-linecap="round"/>
        <line x1="-8.5" y1="8.5" x2="8.5" y2="-8.5" stroke="#d97706" stroke-width="3" stroke-linecap="round"/>
        <circle cx="0" cy="0" r="3.2" fill="#fbbf24"/>
      </g>''',

    "Antigravity": '''<g transform="translate(27,27)">
        <circle cx="0" cy="0" r="12" fill="none" stroke="#a855f7" stroke-width="1.8" stroke-dasharray="8 4"/>
        <polygon points="0,-9 7.8,4.5 -7.8,4.5" fill="none" stroke="#00f7ff" stroke-width="1.8"/>
        <polygon points="0,9 -7.8,-4.5 7.8,-4.5" fill="none" stroke="#a855f7" stroke-width="1.2"/>
        <circle cx="0" cy="0" r="2.8" fill="#00ff88" filter="url(#techSoftGlow)"/>
      </g>''',

    "GitHub Copilot": '''<path d="M 19 25 C 19 20 22.6 16 27 16 C 31.4 16 35 20 35 25 C 35 28 34 30 32 32 L 32 35 C 32 36 31 37 30 37 L 24 37 C 23 37 22 36 22 35 L 22 32 C 20 30 19 28 19 25 Z" fill="none" stroke="#ffffff" stroke-width="2"/>
        <path d="M 21 24 C 21 22 23.5 21 27 21 C 30.5 21 33 22 33 24 C 33 26 30.5 27 27 27 C 23.5 27 21 26 21 24 Z" fill="#a855f7" stroke="#00f7ff" stroke-width="1.2"/>
        <circle cx="24" cy="24" r="1" fill="#ffffff"/>
        <circle cx="30" cy="24" r="1" fill="#ffffff"/>''',

    "Cursor": '''<path d="M 20 16 L 20 34 L 25 29 L 30 36 L 33 34 L 28 27 L 34 26 Z" fill="#00f7ff" stroke="#0b1126" stroke-width="1.5"/>''',

    "Perplexity": '''<g transform="translate(27,27)">
        <rect x="-10" y="-3" width="20" height="6" rx="3" fill="none" stroke="#22d3ee" stroke-width="1.8"/>
        <rect x="-3" y="-10" width="6" height="20" rx="3" fill="none" stroke="#22d3ee" stroke-width="1.8"/>
        <circle cx="0" cy="0" r="2.5" fill="#00f7ff"/>
      </g>'''
}

def generate_tech_stack() -> str:
    groups = [
        {
            "num": "01",
            "title": "Languages &amp; Core Technologies",
            "color": "#00f7ff",
            "tools": [
                ("PHP", "#777bb4"),
                ("Laravel", "#ff2d20"),
                ("HTML5", "#e34f26"),
                ("CSS3", "#1572b6"),
                ("JavaScript", "#f7df1e"),
                ("TypeScript", "#3178c6"),
                ("React", "#00f7ff"),
                ("Next.js", "#ffffff"),
                ("Node.js", "#22c55e"),
                ("Python", "#38bdf8"),
            ],
        },
        {
            "num": "02",
            "title": "Database &amp; Cloud Environment",
            "color": "#a855f7",
            "tools": [
                ("MySQL", "#00758f"),
                ("PostgreSQL", "#336791"),
                ("MongoDB", "#00ed64"),
                ("Git", "#f05032"),
                ("GitHub", "#f0f6fc"),
                ("VS Code", "#007acc"),
                ("Figma", "#f24e1e"),
                ("Vercel", "#ffffff"),
                ("Docker", "#2496ed"),
            ],
        },
        {
            "num": "03",
            "title": "AI Coding Assistants &amp; Agents",
            "color": "#00ff88",
            "tools": [
                ("ChatGPT", "#00a67e"),
                ("Gemini", "#00f7ff"),
                ("Claude", "#d97706"),
                ("Antigravity", "#a855f7"),
                ("GitHub Copilot", "#ffffff"),
                ("Cursor", "#00f7ff"),
                ("Perplexity", "#22d3ee"),
            ],
        },
    ]

    rendered_groups = []
    current_y = 100

    tile_size = 54
    tile_gap = 28
    start_x = 62

    for g in groups:
        g_color = g["color"]
        header_svg = f'''
    <!-- Group {g["num"]} Header -->
    <g transform="translate(32, {current_y})">
      <circle cx="8" cy="14" r="5" fill="{g_color}" filter="url(#techGlow)"/>
      <line x1="16" y1="14" x2="40" y2="14" stroke="{g_color}" stroke-width="1.8"/>
      <rect x="42" y="0" width="34" height="26" rx="6" fill="{g_color}" fill-opacity="0.15" stroke="{g_color}" stroke-width="1.2"/>
      <text x="59" y="18" fill="{g_color}" font-family="monospace" font-size="13" font-weight="900" text-anchor="middle">{g["num"]}</text>
      <text x="88" y="18" fill="#f8fafc" font-family="'Segoe UI', -apple-system, sans-serif" font-size="16" font-weight="700" letter-spacing="0.5">{g["title"]}</text>
      <line x1="390" y1="14" x2="870" y2="14" stroke="#1e293b" stroke-width="1.2" stroke-dasharray="4 4"/>
      <circle cx="870" cy="14" r="3" fill="{g_color}" opacity="0.6"/>
    </g>'''

        badge_y = current_y + 36
        badge_items = []

        for idx, (tool_name, tool_color) in enumerate(g["tools"]):
            bx = start_x + idx * (tile_size + tile_gap)
            icon_svg = TECH_ICONS.get(tool_name, f'''<circle cx="27" cy="27" r="10" fill="{tool_color}"/>''')

            badge_items.append(f'''
      <!-- Tool Tile: {tool_name} (Logo Only) -->
      <g transform="translate({bx}, {badge_y})">
        <title>{tool_name}</title>
        <ellipse cx="27" cy="50" rx="20" ry="5" fill="{tool_color}" opacity="0.32" filter="url(#techSoftGlow)"/>
        <rect x="0" y="0" width="{tile_size}" height="{tile_size}" rx="12" fill="#0b1126" stroke="#1e293b" stroke-width="1.2"/>
        <rect x="0" y="0" width="{tile_size}" height="{tile_size}" rx="12" fill="none" stroke="{tool_color}" stroke-width="1.2" stroke-opacity="0.45"/>
        <path d="M 6 4 Q 27 12 48 4" stroke="#ffffff" stroke-width="0.8" stroke-opacity="0.18" fill="none"/>
        <circle cx="45" cy="9" r="1.8" fill="{tool_color}" opacity="0.75"/>
        {icon_svg}
      </g>''')

        rendered_groups.append(header_svg + "\n" + "".join(badge_items))
        current_y = badge_y + tile_size + 26

    total_height = current_y + 16

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 {total_height}" width="100%">
  <defs>
    <linearGradient id="techBorderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f7ff"/>
      <stop offset="35%" stop-color="#a855f7"/>
      <stop offset="70%" stop-color="#00ff88"/>
      <stop offset="100%" stop-color="#ff0055"/>
    </linearGradient>

    <linearGradient id="geminiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f7ff"/>
      <stop offset="100%" stop-color="#a855f7"/>
    </linearGradient>

    <filter id="techGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="techSoftGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <pattern id="techGrid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#a855f7" stroke-width="0.5" stroke-opacity="0.05"/>
    </pattern>
  </defs>

  <!-- Card Background -->
  <rect x="6" y="6" width="928" height="{total_height - 12}" rx="18" fill="#060814" stroke="#1e293b" stroke-width="1.8"/>
  <rect x="6" y="6" width="928" height="{total_height - 12}" rx="18" fill="url(#techGrid)"/>

  <!-- Animated Neon Lighting Border -->
  <rect x="6" y="6" width="928" height="{total_height - 12}" rx="18" fill="none" stroke="url(#techBorderGrad)" stroke-width="3.2" filter="url(#techGlow)" stroke-dasharray="260 340" stroke-linecap="round">
    <animate attributeName="stroke-dashoffset" from="0" to="-1200" dur="5.5s" repeatCount="indefinite"/>
  </rect>

  <!-- Corner Brackets -->
  <path d="M 18,36 L 18,18 L 36,18" stroke="#00f7ff" stroke-width="2.5" fill="none"/>
  <circle cx="18" cy="18" r="2.5" fill="#00f7ff"/>
  <path d="M 922,36 L 922,18 L 904,18" stroke="#a855f7" stroke-width="2.5" fill="none"/>
  <circle cx="922" cy="18" r="2.5" fill="#a855f7"/>
  <path d="M 18,{total_height - 36} L 18,{total_height - 18} L 36,{total_height - 18}" stroke="#00ff88" stroke-width="2.5" fill="none"/>
  <circle cx="18" cy="{total_height - 18}" r="2.5" fill="#00ff88"/>
  <path d="M 922,{total_height - 36} L 922,{total_height - 18} L 904,{total_height - 18}" stroke="#ff0055" stroke-width="2.5" fill="none"/>
  <circle cx="922" cy="{total_height - 18}" r="2.5" fill="#ff0055"/>

  <!-- Title Header Bar -->
  <g transform="translate(470, 48)">
    <circle cx="-210" cy="-6" r="4" fill="#00f7ff" filter="url(#techGlow)"/>
    <text x="0" y="0" fill="#ffffff" font-family="'Segoe UI', -apple-system, sans-serif" font-size="22" font-weight="900" letter-spacing="2" text-anchor="middle">
      • CORE TECH STACK &amp; ARSENAL •
    </text>
    <circle cx="210" cy="-6" r="4" fill="#00ff88" filter="url(#techGlow)"/>
    <text x="0" y="20" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600" letter-spacing="1.5" text-anchor="middle">
      SYSTEM DIAGNOSTICS // 26 CORE ENGINES &amp; AI AGENT RIGS
    </text>
  </g>

  <!-- Glowing Scanner Line under Title -->
  <line x1="80" y1="78" x2="860" y2="78" stroke="url(#techBorderGrad)" stroke-width="1.5" opacity="0.7"/>

  <!-- Render All 3 Groups -->
  {"".join(rendered_groups)}
</svg>'''


# ==============================================================================
# 3. CELESTIAL NEON DRAGON (NAGA) CONTRIBUTION GAME (neon-viper.svg / neon-dragon.svg)
# Upgraded from viper to majestic Eastern Cyber Dragon with horns, whiskers, claws,
# dorsal spines, and chasing the Flaming Sacred Pearl of Wisdom!
# ==============================================================================
def generate_neon_dragon() -> str:
    # 45 columns x 7 rows = 315 contribution cells
    dots = []
    for col in range(45):
        for row in range(7):
            cx = 40 + col * 19.3
            cy = 100 + row * 20.8
            seed = (col * 11 + row * 17 + (col ^ row)) % 100
            if seed > 86:
                color, op = "#00ff88", "0.9"
            elif seed > 62:
                color, op = "#00f7ff", "0.75"
            elif seed > 40:
                color, op = "#a855f7", "0.6"
            elif seed > 22:
                color, op = "#064e3b", "0.55"
            else:
                color, op = "#10182b", "0.5"
            dots.append(
                f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.2" fill="{color}" fill-opacity="{op}"/>'
            )

    # 38 Tapered Dragon Segments with Glowing Dorsal Spines/Fins
    segments = []
    num_segments = 38
    for i in range(num_segments - 1, 0, -1):
        t = i / num_segments
        rx = 13.0 * (1 - t * 0.72)
        ry = 9.2 * (1 - t * 0.72)
        delay = -(11.5 - i * 0.068)
        fill = "url(#dragonScale1)" if i % 2 == 0 else "url(#dragonScale2)"

        # Dorsal Spines (Duri Punggung Naga Bercahaya)
        spine_h = 10.0 * (1 - t * 0.5)
        tail_flame = ""
        if i >= 35:
            # Fiery Tail Plumes at the very tip
            tail_flame = f'''
        <path d="M 0,0 C -12,-8 -24,-14 -36,-8 C -26,-2 -16,-1 -8,0 C -16,1 -26,2 -36,8 C -24,14 -12,8 0,0 Z" fill="url(#dragonFlameGrad)" filter="url(#dragonGlow)"/>'''

        segments.append(f'''
      <!-- Dragon Segment {i} -->
      <g>
        <!-- Serrated Dorsal Spine Fin -->
        <polygon points="{-rx*0.25:.1f},{-ry*0.85:.1f} 0,{-ry - spine_h:.1f} {rx*0.25:.1f},{-ry*0.85:.1f}" fill="#00f7ff" stroke="#a855f7" stroke-width="0.8" filter="url(#dragonSoftGlow)"/>
        <!-- Main Dragon Body Scale -->
        <ellipse rx="{rx:.2f}" ry="{ry:.2f}" fill="{fill}" stroke="#022c22" stroke-width="0.8" filter="url(#dragonSoftGlow)"/>
        <!-- Ventral & Dorsal Neon Luminescence -->
        <ellipse rx="{rx * 0.5:.2f}" ry="{ry * 0.35:.2f}" fill="#38bdf8" fill-opacity="0.55"/>
        <line x1="{-rx*0.4:.1f}" y1="0" x2="{rx*0.4:.1f}" y2="0" stroke="#00ff88" stroke-width="0.8" opacity="0.8"/>
        {tail_flame}
        <animateMotion dur="11.5s" begin="{delay:.3f}s" repeatCount="indefinite" rotate="auto">
          <mpath href="#dragonPath"/>
        </animateMotion>
      </g>''')

    # 4 Dynamic Dragon Claws (Cakar Naga dengan Kuku Tajam Bercahaya)
    claw_configs = [
        (9, -1, "Front Left Claw"),
        (13, 1, "Front Right Claw"),
        (23, -1, "Rear Left Claw"),
        (27, 1, "Rear Right Claw"),
    ]
    claws = []
    for seg_idx, side, label in claw_configs:
        claw_delay = -(11.5 - seg_idx * 0.068)
        t = seg_idx / num_segments
        ry_cur = 9.2 * (1 - t * 0.72)
        y_elbow = side * (ry_cur + 8)
        y_wrist = side * (ry_cur + 16)
        y_claw = side * (ry_cur + 24)

        claws.append(f'''
      <!-- {label} -->
      <g>
        <!-- Arm Limb -->
        <path d="M 0,{side*ry_cur*0.6:.1f} Q {side*6:.1f},{y_elbow:.1f} {side*12:.1f},{y_wrist:.1f}" stroke="#047857" stroke-width="2.6" stroke-linecap="round" fill="none"/>
        <!-- 3 Sharp Neon Talons -->
        <path d="M {side*12:.1f},{y_wrist:.1f} L {side*20:.1f},{y_claw - 4*side:.1f} M {side*12:.1f},{y_wrist:.1f} L {side*22:.1f},{y_claw:.1f} M {side*12:.1f},{y_wrist:.1f} L {side*18:.1f},{y_claw + 4*side:.1f}" stroke="#fde047" stroke-width="1.8" stroke-linecap="round" filter="url(#dragonSoftGlow)"/>
        <animateMotion dur="11.5s" begin="{claw_delay:.3f}s" repeatCount="indefinite" rotate="auto">
          <mpath href="#dragonPath"/>
        </animateMotion>
      </g>''')

    # Majestic Dragon Head with Horns, Flowing Whiskers, Fangs, and Fiery Mane
    head_svg = '''
    <g filter="url(#dragonGlow)">
      <!-- Flowing Whiskers (Kumis Naga Melambai) -->
      <path d="M 16,-3 C 28,-14 40,-8 56,-18 C 42,-9 30,-9 18,-2" stroke="#00f7ff" stroke-width="1.8" fill="none" filter="url(#dragonSoftGlow)">
        <animate attributeName="d" values="M 16,-3 C 28,-14 40,-8 56,-18 C 42,-9 30,-9 18,-2; M 16,-3 C 28,-8 38,-14 56,-10 C 40,-5 28,-7 18,-2; M 16,-3 C 28,-14 40,-8 56,-18 C 42,-9 30,-9 18,-2" dur="2.2s" repeatCount="indefinite"/>
      </path>
      <path d="M 16,3 C 28,14 40,8 56,18 C 42,9 30,9 18,2" stroke="#fde047" stroke-width="1.8" fill="none" filter="url(#dragonSoftGlow)">
        <animate attributeName="d" values="M 16,3 C 28,14 40,8 56,18 C 42,9 30,9 18,2; M 16,3 C 28,8 38,14 56,10 C 40,5 28,7 18,2; M 16,3 C 28,14 40,8 56,18 C 42,9 30,9 18,2" dur="2.2s" repeatCount="indefinite"/>
      </path>

      <!-- Bifurcated Dragon Antlers (Tanduk Naga Bercabang) -->
      <!-- Upper Horn -->
      <path d="M -6,-9 C -12,-20 -22,-28 -34,-32 M -18,-22 C -26,-26 -30,-24 -36,-22" stroke="#fde047" stroke-width="2.5" stroke-linecap="round" fill="none" filter="url(#dragonSoftGlow)"/>
      <!-- Lower Horn -->
      <path d="M -6,9 C -12,20 -22,28 -34,32 M -18,22 C -26,26 -30,24 -36,22" stroke="#00f7ff" stroke-width="2.5" stroke-linecap="round" fill="none" filter="url(#dragonSoftGlow)"/>

      <!-- Dragon Head Silhouette & Snout -->
      <path d="M -16,-9 C -6,-15 12,-11 22,-2 C 24,0 24,2 22,4 C 12,13 -6,17 -16,11 C -22,7 -22,-5 -16,-9 Z" fill="url(#dragonHeadGrad)" stroke="#00ff88" stroke-width="1.4"/>

      <!-- Glowing Fangs -->
      <polygon points="14,-2 18,2 12,0" fill="#ffffff" filter="url(#dragonSoftGlow)"/>
      <polygon points="14,2 18,-2 12,0" fill="#ffffff" filter="url(#dragonSoftGlow)"/>
      <polygon points="20,-1 23,2 19,0" fill="#fde047"/>

      <!-- Dragon Mane Flaring Backwards -->
      <path d="M -12,-9 C -22,-16 -28,-8 -38,-14 C -28,-5 -20,-7 -14,-3 Z" fill="url(#dragonManeGrad)"/>
      <path d="M -12,9 C -22,16 -28,8 -38,14 C -28,5 -20,7 -14,3 Z" fill="url(#dragonManeGrad)"/>

      <!-- Fierce Glowing Dragon Eyes with Flame Trails -->
      <ellipse cx="4" cy="-5" rx="3.2" ry="2" fill="#fde047" filter="url(#dragonSoftGlow)"/>
      <ellipse cx="4" cy="5" rx="3.2" ry="2" fill="#fde047" filter="url(#dragonSoftGlow)"/>
      <line x1="3" y1="-5" x2="5.5" y2="-5" stroke="#050505" stroke-width="1.2"/>
      <line x1="3" y1="5" x2="5.5" y2="5" stroke="#050505" stroke-width="1.2"/>
      <path d="M 2,-5 L -7,-9" stroke="#ff0055" stroke-width="1.5" opacity="0.85"/>
      <path d="M 2,5 L -7,9" stroke="#ff0055" stroke-width="1.5" opacity="0.85"/>

      <animateMotion dur="11.5s" begin="0s" repeatCount="indefinite" rotate="auto">
        <mpath href="#dragonPath"/>
      </animateMotion>
    </g>'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 370" width="100%">
  <defs>
    <!-- Lighting Border Gradient -->
    <linearGradient id="dragonBorderNeon" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f7ff"/>
      <stop offset="50%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#00ff88"/>
    </linearGradient>

    <!-- Head & Scale Gradients -->
    <linearGradient id="dragonHeadGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="50%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#00ff88"/>
    </linearGradient>

    <linearGradient id="dragonManeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#00f7ff"/>
    </linearGradient>

    <linearGradient id="dragonFlameGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff0055"/>
      <stop offset="50%" stop-color="#fde047"/>
      <stop offset="100%" stop-color="#00ff88"/>
    </linearGradient>

    <radialGradient id="dragonScale1" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#4ade80"/>
      <stop offset="60%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#064e3b"/>
    </radialGradient>

    <radialGradient id="dragonScale2" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="60%" stop-color="#065f46"/>
      <stop offset="100%" stop-color="#022c22"/>
    </radialGradient>

    <filter id="dragonGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="dragonSoftGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Dynamic Sinuous Dragon Path -->
    <path id="dragonPath" d="M 65,130 C 150,70 210,230 310,135 C 410,45 470,235 575,145 C 670,55 740,225 815,125 C 850,70 735,60 615,185 C 495,255 360,70 220,195 C 125,245 35,175 65,130 Z"/>
  </defs>

  <style>
    .title-font {{ font-family: 'Segoe UI', -apple-system, sans-serif; font-weight: 900; }}
    .mono-font {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
  </style>

  <!-- Card Background -->
  <rect x="6" y="6" width="928" height="358" rx="18" fill="#060814" stroke="#1e293b" stroke-width="1.8"/>

  <!-- Animated Neon Lighting Border -->
  <rect x="6" y="6" width="928" height="358" rx="18" fill="none" stroke="url(#dragonBorderNeon)" stroke-width="3.2" filter="url(#dragonGlow)" stroke-dasharray="260 330" stroke-linecap="round">
    <animate attributeName="stroke-dashoffset" from="0" to="-1180" dur="5.2s" repeatCount="indefinite"/>
  </rect>

  <!-- Corner Brackets -->
  <path d="M 18,36 L 18,18 L 36,18" stroke="#00f7ff" stroke-width="2.5" fill="none"/>
  <circle cx="18" cy="18" r="2.5" fill="#00f7ff"/>
  <path d="M 922,36 L 922,18 L 904,18" stroke="#a855f7" stroke-width="2.5" fill="none"/>
  <circle cx="922" cy="18" r="2.5" fill="#a855f7"/>
  <path d="M 18,334 L 18,352 L 36,352" stroke="#00ff88" stroke-width="2.5" fill="none"/>
  <circle cx="18" cy="352" r="2.5" fill="#00ff88"/>
  <path d="M 922,334 L 922,352 L 904,352" stroke="#00f7ff" stroke-width="2.5" fill="none"/>
  <circle cx="922" cy="352" r="2.5" fill="#00f7ff"/>

  <!-- Header Section -->
  <g transform="translate(36, 42)">
    <circle cx="4" cy="0" r="6" fill="#00ff88" filter="url(#dragonGlow)"/>
    <text x="22" y="5" fill="#ffffff" class="title-font" font-size="17" letter-spacing="1">🐉 CELESTIAL NEON DRAGON • CONTRIBUTION HARVESTER</text>
    <text x="22" y="24" fill="#94a3b8" class="mono-font" font-size="11">@fauzan667 | LEGENDARY MATRIX DRAGON ENGINE | 120 FPS</text>
  </g>

  <!-- Top Right Indicators -->
  <g transform="translate(900, 42)">
    <text x="0" y="3" fill="#00f7ff" class="mono-font" font-size="12" font-weight="700" text-anchor="end">DRAGON SPIRIT: AWAKENED</text>
    <text x="0" y="23" fill="#00ff88" class="mono-font" font-size="13" font-weight="900" text-anchor="end">⚡ HARVESTING CELESTIAL CORES</text>
  </g>

  <!-- Divider Line -->
  <line x1="36" y1="76" x2="904" y2="76" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Contribution Grid (315 Glowing Cells) -->
  {"".join(dots)}

  <!-- THE SACRED CELESTIAL DRAGON PEARLS (Chased by the Dragon) -->
  <!-- Pearl 1 at (310, 135) -->
  <g transform="translate(310, 135)">
    <circle cx="0" cy="0" r="14" fill="none" stroke="#fde047" stroke-width="1.4" stroke-dasharray="6 4" filter="url(#dragonGlow)">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="8" fill="#ff0055" filter="url(#dragonGlow)">
      <animate attributeName="r" values="6;10;6" dur="1.2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="4" fill="#ffffff" filter="url(#dragonSoftGlow)"/>
  </g>

  <!-- Pearl 2 at (575, 145) -->
  <g transform="translate(575, 145)">
    <circle cx="0" cy="0" r="14" fill="none" stroke="#00f7ff" stroke-width="1.4" stroke-dasharray="6 4" filter="url(#dragonGlow)">
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="2.8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="8" fill="#fde047" filter="url(#dragonGlow)">
      <animate attributeName="r" values="6;10;6" dur="1.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="4" fill="#ffffff" filter="url(#dragonSoftGlow)"/>
  </g>

  <!-- Pearl 3 at (815, 125) -->
  <g transform="translate(815, 125)">
    <circle cx="0" cy="0" r="12" fill="none" stroke="#00ff88" stroke-width="1.2" stroke-dasharray="4 4" filter="url(#dragonGlow)">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="7" fill="#00f7ff" filter="url(#dragonGlow)">
      <animate attributeName="r" values="5;9;5" dur="1.3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="3.5" fill="#ffffff"/>
  </g>

  <!-- Pearl 4 at (220, 195) -->
  <g transform="translate(220, 195)">
    <circle cx="0" cy="0" r="12" fill="none" stroke="#a855f7" stroke-width="1.2" stroke-dasharray="4 4" filter="url(#dragonGlow)">
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="2.6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="7" fill="#a855f7" filter="url(#dragonGlow)">
      <animate attributeName="r" values="5;9;5" dur="1.6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="3.5" fill="#ffffff"/>
  </g>

  <!-- Dragon Body & Claws -->
  {"".join(segments)}
  {"".join(claws)}
  {head_svg}

  <!-- Bottom Energy Meter Panel -->
  <g transform="translate(36, 276)">
    <text x="0" y="0" fill="#00f7ff" class="mono-font" font-size="10.5" font-weight="700">CELESTIAL DRAGON QI &amp; CONTRIBUTION HARVESTER</text>
    <text x="868" y="0" fill="#a855f7" class="mono-font" font-size="10.5" font-weight="700" text-anchor="end">TIERS: HATCHLING ➔ WYRM ➔ MATRIX LEVIATHAN ➔ [CELESTIAL DRAGON MAX]</text>
    
    <rect x="0" y="10" width="868" height="12" rx="6" fill="#0b1126" stroke="#1e293b" stroke-width="1.2"/>
    <rect x="0" y="10" width="680" height="12" rx="6" fill="url(#dragonBorderNeon)" filter="url(#dragonSoftGlow)">
      <animate attributeName="width" values="240;840;240" dur="7.5s" repeatCount="indefinite"/>
    </rect>

    <text x="0" y="38" fill="#64748b" class="mono-font" font-size="9.5">DRAGON QI: 100% // CELESTIAL SYNC: OPTIMAL // SACRED PEARLS: HARVESTING</text>
    <text x="868" y="38" fill="#00ff88" class="mono-font" font-size="9.5" font-weight="700" text-anchor="end">OVERDRIVE: 9,842 XP</text>
  </g>
</svg>'''


# ==============================================================================
# 4. DEVELOPER METRICS, STREAK & VELOCITY RIDGE (metrics-dashboard.svg)
# ==============================================================================
def generate_metrics_dashboard() -> str:
    points = [
        (340, 415),
        (425, 365),
        (510, 385),
        (595, 335),
        (680, 360),
        (765, 320),
        (850, 350),
    ]
    path_d = f"M 340,440 L 340,415 C 380,365 400,365 425,365 C 460,365 480,385 510,385 C 550,385 570,335 595,335 C 635,335 655,360 680,360 C 720,360 740,320 765,320 C 805,320 825,350 850,350 L 850,440 Z"
    stroke_d = f"M 340,415 C 380,365 400,365 425,365 C 460,365 480,385 510,385 C 550,385 570,335 595,335 C 635,335 655,360 680,360 C 720,360 740,320 765,320 C 805,320 825,350 850,350"

    peak_dots = []
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    commits = ["24", "42", "35", "54", "40", "58", "46"]
    for i, (px, py) in enumerate(points):
        peak_dots.append(f'''
      <circle cx="{px}" cy="{py}" r="4.5" fill="#00f7ff" filter="url(#metricGlow)"/>
      <circle cx="{px}" cy="{py}" r="2" fill="#ffffff"/>
      <text x="{px}" y="{py - 10}" fill="#38bdf8" font-family="monospace" font-size="10" font-weight="700" text-anchor="middle">{commits[i]}</text>
      <text x="{px}" y="456" fill="#64748b" font-family="monospace" font-size="10" text-anchor="middle">{days[i]}</text>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 800" width="100%">
  <defs>
    <linearGradient id="metricBorderNeon" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f7ff"/>
      <stop offset="35%" stop-color="#a855f7"/>
      <stop offset="70%" stop-color="#00ff88"/>
      <stop offset="100%" stop-color="#f43f5e"/>
    </linearGradient>

    <linearGradient id="ridgeAreaGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00f7ff" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#a855f7" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#060814" stop-opacity="0"/>
    </linearGradient>

    <filter id="metricGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="softGlowMetric" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    .title-font {{ font-family: 'Segoe UI', -apple-system, sans-serif; font-weight: 900; }}
    .mono-font {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
  </style>

  <!-- Base Canvas -->
  <rect x="6" y="6" width="928" height="788" rx="18" fill="#060814" stroke="#1e293b" stroke-width="1.8"/>

  <!-- Animated Neon Lighting Border for Whole Dashboard -->
  <rect x="6" y="6" width="928" height="788" rx="18" fill="none" stroke="url(#metricBorderNeon)" stroke-width="3.2" filter="url(#metricGlow)" stroke-dasharray="280 360" stroke-linecap="round">
    <animate attributeName="stroke-dashoffset" from="0" to="-1280" dur="6s" repeatCount="indefinite"/>
  </rect>

  <!-- Corner Brackets -->
  <path d="M 18,36 L 18,18 L 36,18" stroke="#00f7ff" stroke-width="2.5" fill="none"/>
  <circle cx="18" cy="18" r="2.5" fill="#00f7ff"/>
  <path d="M 922,36 L 922,18 L 904,18" stroke="#a855f7" stroke-width="2.5" fill="none"/>
  <circle cx="922" cy="18" r="2.5" fill="#a855f7"/>
  <path d="M 18,764 L 18,782 L 36,782" stroke="#00ff88" stroke-width="2.5" fill="none"/>
  <circle cx="18" cy="782" r="2.5" fill="#00ff88"/>
  <path d="M 922,764 L 922,782 L 904,782" stroke="#f43f5e" stroke-width="2.5" fill="none"/>
  <circle cx="922" cy="782" r="2.5" fill="#f43f5e"/>

  <!-- TOP BANNER: 📊 DEVELOPER METRICS & LIVE ACTIVITY -->
  <g transform="translate(470, 44)">
    <circle cx="-230" cy="-6" r="4" fill="#00f7ff" filter="url(#metricGlow)"/>
    <text x="0" y="0" fill="#ffffff" class="title-font" font-size="21" letter-spacing="2" text-anchor="middle">
      📊 DEVELOPER METRICS &amp; LIVE ACTIVITY
    </text>
    <circle cx="230" cy="-6" r="4" fill="#00ff88" filter="url(#metricGlow)"/>
    <text x="0" y="20" fill="#94a3b8" class="mono-font" font-size="11" font-weight="600" letter-spacing="1.5" text-anchor="middle">
      TELEMETRY // CODE FREQUENCY // REPO MATRIX // SYSTEM VITAL SIGNS
    </text>
  </g>

  <!-- CARD 1: STREAK & CONTRIBUTIONS SHOWCASE -->
  <g transform="translate(24, 84)">
    <rect x="0" y="0" width="892" height="162" rx="14" fill="#0a0f24" stroke="#1e293b" stroke-width="1.4"/>
    <rect x="0" y="0" width="892" height="162" rx="14" fill="none" stroke="url(#metricBorderNeon)" stroke-width="2" filter="url(#softGlowMetric)" stroke-dasharray="160 260">
      <animate attributeName="stroke-dashoffset" from="0" to="-840" dur="4.8s" repeatCount="indefinite"/>
    </rect>

    <!-- Left Column: Total Contributions -->
    <g transform="translate(30, 24)">
      <circle cx="10" cy="12" r="5" fill="#00ff88" filter="url(#metricGlow)"/>
      <text x="24" y="16" fill="#94a3b8" class="mono-font" font-size="11.5" font-weight="700">TOTAL CONTRIBUTIONS</text>
      <text x="0" y="68" fill="#00ff88" class="title-font" font-size="44" filter="url(#softGlowMetric)">2,840+</text>
      <text x="0" y="94" fill="#64748b" class="mono-font" font-size="10.5">LIFETIME COMMITS &amp; PR EVENTS</text>
      <rect x="0" y="106" width="200" height="8" rx="4" fill="#1e293b"/>
      <rect x="0" y="106" width="168" height="8" rx="4" fill="#00ff88" filter="url(#softGlowMetric)"/>
    </g>

    <!-- Center Column: Rotating Neon Ring & Current Streak -->
    <g transform="translate(446, 81)">
      <circle cx="0" cy="0" r="56" fill="none" stroke="#00f7ff" stroke-width="2.5" stroke-dasharray="8 6" filter="url(#metricGlow)">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="12s" repeatCount="indefinite"/>
      </circle>
      <circle cx="0" cy="0" r="46" fill="none" stroke="#a855f7" stroke-width="1.8" stroke-dasharray="5 5">
        <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="8s" repeatCount="indefinite"/>
      </circle>
      <circle cx="0" cy="0" r="38" fill="#060814" stroke="#00f7ff" stroke-width="1"/>
      <text x="0" y="-8" fill="#ff7000" font-size="18" text-anchor="middle">🔥</text>
      <text x="0" y="14" fill="#00f7ff" class="title-font" font-size="20" letter-spacing="1" text-anchor="middle">68</text>
      <text x="0" y="27" fill="#93c5fd" class="mono-font" font-size="8.5" font-weight="700" text-anchor="middle">DAYS</text>
      <text x="0" y="70" fill="#38bdf8" class="mono-font" font-size="11" font-weight="700" text-anchor="middle">CURRENT ACTIVE STREAK</text>
    </g>

    <!-- Right Column: Longest Streak -->
    <g transform="translate(640, 24)">
      <circle cx="10" cy="12" r="5" fill="#a855f7" filter="url(#metricGlow)"/>
      <text x="24" y="16" fill="#94a3b8" class="mono-font" font-size="11.5" font-weight="700">LONGEST STREAK RECORD</text>
      <text x="0" y="68" fill="#c084fc" class="title-font" font-size="44" filter="url(#softGlowMetric)">142 DAYS</text>
      <text x="0" y="94" fill="#64748b" class="mono-font" font-size="10.5">CONSISTENCY SCORE: 99.2% (S-TIER)</text>
      <rect x="0" y="106" width="200" height="8" rx="4" fill="#1e293b"/>
      <rect x="0" y="106" width="188" height="8" rx="4" fill="#a855f7" filter="url(#softGlowMetric)"/>
    </g>
  </g>

  <!-- CARD 2: WEEKLY VELOCITY RIDGE AREA CHART -->
  <g transform="translate(24, 264)">
    <rect x="0" y="0" width="892" height="236" rx="14" fill="#0a0f24" stroke="#1e293b" stroke-width="1.4"/>
    <rect x="0" y="0" width="892" height="236" rx="14" fill="none" stroke="url(#metricBorderNeon)" stroke-width="2" filter="url(#softGlowMetric)" stroke-dasharray="180 280">
      <animate attributeName="stroke-dashoffset" from="0" to="-920" dur="5s" repeatCount="indefinite"/>
    </rect>

    <circle cx="28" cy="24" r="4.5" fill="#00f7ff" filter="url(#metricGlow)"/>
    <text x="42" y="28" fill="#ffffff" class="title-font" font-size="14" letter-spacing="1">WEEKLY VELOCITY RIDGE // CODING ACTIVITY SPECTRUM</text>
    <text x="864" y="28" fill="#00ff88" class="mono-font" font-size="11" font-weight="700" text-anchor="end">PEAK: 58 COMMITS / DAY</text>
    <line x1="20" y1="44" x2="872" y2="44" stroke="#1e293b" stroke-width="1"/>

    <!-- Left Telemetry Summary -->
    <g transform="translate(24, 66)">
      <text x="0" y="14" fill="#94a3b8" class="mono-font" font-size="11">AVERAGE VELOCITY:</text>
      <text x="0" y="36" fill="#00f7ff" class="mono-font" font-size="16" font-weight="900">38.4 COMMITS / D</text>

      <text x="0" y="66" fill="#94a3b8" class="mono-font" font-size="11">ACTIVE CODING TIME:</text>
      <text x="0" y="88" fill="#00ff88" class="mono-font" font-size="16" font-weight="900">56.8 HRS / WEEK</text>

      <text x="0" y="118" fill="#94a3b8" class="mono-font" font-size="11">EFFICIENCY FACTOR:</text>
      <text x="0" y="140" fill="#c084fc" class="mono-font" font-size="16" font-weight="900">4.92x [OPTIMAL]</text>
    </g>

    <line x1="240" y1="56" x2="240" y2="216" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 4"/>

    <!-- Area Chart Area -->
    <line x1="260" y1="80" x2="860" y2="80" stroke="#1e293b" stroke-width="0.8" stroke-dasharray="3 3"/>
    <line x1="260" y1="120" x2="860" y2="120" stroke="#1e293b" stroke-width="0.8" stroke-dasharray="3 3"/>
    <line x1="260" y1="160" x2="860" y2="160" stroke="#1e293b" stroke-width="0.8" stroke-dasharray="3 3"/>
    <line x1="260" y1="200" x2="860" y2="200" stroke="#1e293b" stroke-width="1.2"/>

    <g transform="translate(-60, -230)">
      <path d="{path_d}" fill="url(#ridgeAreaGrad)"/>
      <path d="{stroke_d}" fill="none" stroke="#00f7ff" stroke-width="3" filter="url(#metricGlow)"/>
      {"".join(peak_dots)}

      <line x1="340" y1="300" x2="340" y2="440" stroke="#00ff88" stroke-width="2" filter="url(#metricGlow)" opacity="0.8">
        <animate attributeName="x1" values="340;850;340" dur="4.8s" repeatCount="indefinite"/>
        <animate attributeName="x2" values="340;850;340" dur="4.8s" repeatCount="indefinite"/>
      </line>
    </g>
  </g>

  <!-- CARD 3 & 4: SPLIT BOTTOM CARDS -->
  <!-- CARD 3 (Left): GITHUB CORE STATS -->
  <g transform="translate(24, 520)">
    <rect x="0" y="0" width="436" height="250" rx="14" fill="#0a0f24" stroke="#1e293b" stroke-width="1.4"/>
    <rect x="0" y="0" width="436" height="250" rx="14" fill="none" stroke="url(#metricBorderNeon)" stroke-width="2" filter="url(#softGlowMetric)" stroke-dasharray="140 220">
      <animate attributeName="stroke-dashoffset" from="0" to="-720" dur="4.5s" repeatCount="indefinite"/>
    </rect>

    <circle cx="22" cy="24" r="4" fill="#00ff88" filter="url(#metricGlow)"/>
    <text x="34" y="28" fill="#ffffff" class="title-font" font-size="13" letter-spacing="1">GITHUB CORE STATS</text>
    <text x="414" y="28" fill="#64748b" class="mono-font" font-size="10" text-anchor="end">@fauzan667</text>
    <line x1="16" y1="42" x2="420" y2="42" stroke="#1e293b" stroke-width="1"/>

    <!-- Rotating Radar Scanner -->
    <g transform="translate(360, 115)">
      <circle cx="0" cy="0" r="32" fill="none" stroke="#00f7ff" stroke-width="1" stroke-dasharray="3 3"/>
      <circle cx="0" cy="0" r="20" fill="none" stroke="#a855f7" stroke-width="0.8"/>
      <circle cx="0" cy="0" r="8" fill="none" stroke="#00ff88" stroke-width="0.8"/>
      <line x1="-32" y1="0" x2="32" y2="0" stroke="#1e293b" stroke-width="0.8"/>
      <line x1="0" y1="-32" x2="0" y2="32" stroke="#1e293b" stroke-width="0.8"/>
      <line x1="0" y1="0" x2="28" y2="-16" stroke="#00ff88" stroke-width="2" filter="url(#metricGlow)">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="3s" repeatCount="indefinite"/>
      </line>
    </g>

    <g transform="translate(24, 68)">
      <text x="0" y="0" fill="#94a3b8" class="mono-font" font-size="11.5">★ Total Stars Earned:</text>
      <text x="180" y="0" fill="#fde047" class="mono-font" font-size="12" font-weight="700">120+</text>

      <text x="0" y="32" fill="#94a3b8" class="mono-font" font-size="11.5">⚡ Total Commits:</text>
      <text x="180" y="32" fill="#00ff88" class="mono-font" font-size="12" font-weight="700">2,840+</text>

      <text x="0" y="64" fill="#94a3b8" class="mono-font" font-size="11.5">🔀 Pull Requests:</text>
      <text x="180" y="64" fill="#00f7ff" class="mono-font" font-size="12" font-weight="700">85 Merged</text>

      <text x="0" y="96" fill="#94a3b8" class="mono-font" font-size="11.5">✔ Issues Resolved:</text>
      <text x="180" y="96" fill="#c084fc" class="mono-font" font-size="12" font-weight="700">46 Closed</text>

      <text x="0" y="128" fill="#94a3b8" class="mono-font" font-size="11.5">📦 Contributed Repos:</text>
      <text x="180" y="128" fill="#38bdf8" class="mono-font" font-size="12" font-weight="700">32 Repos</text>

      <line x1="0" y1="145" x2="390" y2="145" stroke="#1e293b" stroke-width="1"/>
      <text x="0" y="162" fill="#00ff88" class="mono-font" font-size="11" font-weight="900">DEVELOPER TIER: S+ ARCHITECT</text>
    </g>
  </g>

  <!-- CARD 4 (Right): MOST USED LANGUAGES -->
  <g transform="translate(480, 520)">
    <rect x="0" y="0" width="436" height="250" rx="14" fill="#0a0f24" stroke="#1e293b" stroke-width="1.4"/>
    <rect x="0" y="0" width="436" height="250" rx="14" fill="none" stroke="url(#metricBorderNeon)" stroke-width="2" filter="url(#softGlowMetric)" stroke-dasharray="140 220">
      <animate attributeName="stroke-dashoffset" from="0" to="-720" dur="4.5s" repeatCount="indefinite"/>
    </rect>

    <circle cx="22" cy="24" r="4" fill="#00f7ff" filter="url(#metricGlow)"/>
    <text x="34" y="28" fill="#ffffff" class="title-font" font-size="13" letter-spacing="1">MOST USED LANGUAGES</text>
    <text x="414" y="28" fill="#64748b" class="mono-font" font-size="10" text-anchor="end">CODE RADAR</text>
    <line x1="16" y1="42" x2="420" y2="42" stroke="#1e293b" stroke-width="1"/>

    <g transform="translate(24, 66)">
      <text x="0" y="0" fill="#e2e8f0" class="mono-font" font-size="11" font-weight="600">PHP / Laravel</text>
      <text x="388" y="0" fill="#00f7ff" class="mono-font" font-size="11" font-weight="700" text-anchor="end">38%</text>
      <rect x="0" y="8" width="388" height="7" rx="3.5" fill="#1e293b"/>
      <rect x="0" y="8" width="147" height="7" rx="3.5" fill="#00f7ff" filter="url(#softGlowMetric)"/>

      <text x="0" y="32" fill="#e2e8f0" class="mono-font" font-size="11" font-weight="600">JavaScript / TypeScript</text>
      <text x="388" y="32" fill="#a855f7" class="mono-font" font-size="11" font-weight="700" text-anchor="end">27%</text>
      <rect x="0" y="40" width="388" height="7" rx="3.5" fill="#1e293b"/>
      <rect x="0" y="40" width="105" height="7" rx="3.5" fill="#a855f7" filter="url(#softGlowMetric)"/>

      <text x="0" y="64" fill="#e2e8f0" class="mono-font" font-size="11" font-weight="600">Python</text>
      <text x="388" y="64" fill="#00ff88" class="mono-font" font-size="11" font-weight="700" text-anchor="end">18%</text>
      <rect x="0" y="72" width="388" height="7" rx="3.5" fill="#1e293b"/>
      <rect x="0" y="72" width="70" height="7" rx="3.5" fill="#00ff88" filter="url(#softGlowMetric)"/>

      <text x="0" y="96" fill="#e2e8f0" class="mono-font" font-size="11" font-weight="600">HTML5 &amp; CSS3</text>
      <text x="388" y="96" fill="#ff7000" class="mono-font" font-size="11" font-weight="700" text-anchor="end">11%</text>
      <rect x="0" y="104" width="388" height="7" rx="3.5" fill="#1e293b"/>
      <rect x="0" y="104" width="43" height="7" rx="3.5" fill="#ff7000" filter="url(#softGlowMetric)"/>

      <text x="0" y="128" fill="#e2e8f0" class="mono-font" font-size="11" font-weight="600">SQL &amp; Others</text>
      <text x="388" y="128" fill="#f43f5e" class="mono-font" font-size="11" font-weight="700" text-anchor="end">6%</text>
      <rect x="0" y="136" width="388" height="7" rx="3.5" fill="#1e293b"/>
      <rect x="0" y="136" width="23" height="7" rx="3.5" fill="#f43f5e" filter="url(#softGlowMetric)"/>

      <line x1="0" y1="152" x2="388" y2="152" stroke="#1e293b" stroke-width="1"/>
      <text x="194" y="167" fill="#64748b" class="mono-font" font-size="10" text-anchor="middle">SYNTAX MATRIX // 100% COMPILED</text>
    </g>
  </g>
</svg>'''


# ==============================================================================
# 5. HOLOGRAPHIC RPG SKILL RADAR & SYSTEM TERMINAL (cyber-terminal.svg)
# ==============================================================================
def generate_cyber_terminal() -> str:
    radar_poly = "105,81 164,121 138,186 70,188 45,121"

    def calc_poly(r):
        pts = []
        for i in range(5):
            angle = -math.pi / 2 + i * (2 * math.pi / 5)
            x = 105 + r * math.cos(angle)
            y = 140 + r * math.sin(angle)
            pts.append(f"{x:.1f},{y:.1f}")
        return " ".join(pts)

    poly_outer = calc_poly(65)
    poly_mid = calc_poly(45)
    poly_inner = calc_poly(25)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 450" width="100%">
  <defs>
    <linearGradient id="termBorderNeon" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f7ff"/>
      <stop offset="50%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#00ff88"/>
    </linearGradient>

    <linearGradient id="radarFillGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f7ff" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#a855f7" stop-opacity="0.3"/>
    </linearGradient>

    <filter id="termGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="termSoftGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    .title-font {{ font-family: 'Segoe UI', -apple-system, sans-serif; font-weight: 900; }}
    .mono-font {{ font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }}
  </style>

  <!-- Window Container -->
  <rect x="6" y="6" width="928" height="438" rx="18" fill="#060814" stroke="#1e293b" stroke-width="1.8"/>

  <!-- Animated Neon Lighting Border -->
  <rect x="6" y="6" width="928" height="438" rx="18" fill="none" stroke="url(#termBorderNeon)" stroke-width="3.2" filter="url(#termGlow)" stroke-dasharray="260 340" stroke-linecap="round">
    <animate attributeName="stroke-dashoffset" from="0" to="-1200" dur="5.5s" repeatCount="indefinite"/>
  </rect>

  <!-- Corner Brackets -->
  <path d="M 18,36 L 18,18 L 36,18" stroke="#00f7ff" stroke-width="2.5" fill="none"/>
  <circle cx="18" cy="18" r="2.5" fill="#00f7ff"/>
  <path d="M 922,36 L 922,18 L 904,18" stroke="#a855f7" stroke-width="2.5" fill="none"/>
  <circle cx="922" cy="18" r="2.5" fill="#a855f7"/>
  <path d="M 18,414 L 18,432 L 36,432" stroke="#00ff88" stroke-width="2.5" fill="none"/>
  <circle cx="18" cy="432" r="2.5" fill="#00ff88"/>
  <path d="M 922,414 L 922,432 L 904,432" stroke="#00f7ff" stroke-width="2.5" fill="none"/>
  <circle cx="922" cy="432" r="2.5" fill="#00f7ff"/>

  <!-- Terminal Window Header -->
  <rect x="20" y="20" width="900" height="36" rx="8" fill="#0a0f24" stroke="#1e293b" stroke-width="1"/>
  <circle cx="42" cy="38" r="5" fill="#ff5555" filter="url(#termSoftGlow)"/>
  <circle cx="60" cy="38" r="5" fill="#ffb86c" filter="url(#termSoftGlow)"/>
  <circle cx="78" cy="38" r="5" fill="#50fa7b" filter="url(#termSoftGlow)"/>

  <text x="470" y="42" fill="#00f7ff" class="mono-font" font-size="12" font-weight="700" letter-spacing="1" text-anchor="middle">
    fauzan@cyber-rig: ~ (zsh) // HYPRLAND NEON HUD
  </text>
  <text x="900" y="42" fill="#64748b" class="mono-font" font-size="10" text-anchor="end">SEC: LEVEL-5 // 8ms</text>

  <line x1="460" y1="68" x2="460" y2="424" stroke="#1e293b" stroke-width="1.2" stroke-dasharray="4 4"/>

  <!-- LEFT PANEL: DEVELOPER RPG SKILL RADAR & ATTRIBUTE BARS -->
  <g transform="translate(30, 72)">
    <circle cx="10" cy="12" r="4.5" fill="#00ff88" filter="url(#termGlow)"/>
    <text x="24" y="16" fill="#ffffff" class="title-font" font-size="14" letter-spacing="1">DEVELOPER RPG ATTRIBUTES</text>
    <text x="410" y="16" fill="#a855f7" class="mono-font" font-size="10.5" font-weight="700" text-anchor="end">[LVL.99 ARCHITECT]</text>
    <line x1="0" y1="28" x2="410" y2="28" stroke="#1e293b" stroke-width="1"/>

    <!-- Polygonal Skill Radar Diagram -->
    <g transform="translate(0, 10)">
      <polygon points="{poly_outer}" fill="none" stroke="#1e293b" stroke-width="1"/>
      <polygon points="{poly_mid}" fill="none" stroke="#1e293b" stroke-width="0.8"/>
      <polygon points="{poly_inner}" fill="none" stroke="#1e293b" stroke-width="0.8"/>

      <line x1="105" y1="140" x2="105" y2="75" stroke="#1e293b" stroke-width="0.8"/>
      <line x1="105" y1="140" x2="167" y2="120" stroke="#1e293b" stroke-width="0.8"/>
      <line x1="105" y1="140" x2="143" y2="193" stroke="#1e293b" stroke-width="0.8"/>
      <line x1="105" y1="140" x2="67" y2="193" stroke="#1e293b" stroke-width="0.8"/>
      <line x1="105" y1="140" x2="43" y2="120" stroke="#1e293b" stroke-width="0.8"/>

      <polygon points="{radar_poly}" fill="url(#radarFillGrad)" stroke="#00f7ff" stroke-width="2" filter="url(#termSoftGlow)"/>
      <circle cx="105" cy="140" r="3" fill="#ffffff" filter="url(#termSoftGlow)"/>

      <text x="105" y="68" fill="#00f7ff" class="mono-font" font-size="9" font-weight="700" text-anchor="middle">FRONTEND</text>
      <text x="178" y="122" fill="#a855f7" class="mono-font" font-size="9" font-weight="700">BACKEND</text>
      <text x="150" y="206" fill="#00ff88" class="mono-font" font-size="9" font-weight="700">DATABASE</text>
      <text x="60" y="206" fill="#ff7000" class="mono-font" font-size="9" font-weight="700" text-anchor="end">UI/UX</text>
      <text x="32" y="122" fill="#38bdf8" class="mono-font" font-size="9" font-weight="700" text-anchor="end">AI-CODING</text>
    </g>

    <!-- Attribute Progress Bars -->
    <g transform="translate(210, 48)">
      <text x="0" y="0" fill="#94a3b8" class="mono-font" font-size="10" font-weight="600">Frontend Architecture</text>
      <text x="195" y="0" fill="#00f7ff" class="mono-font" font-size="10" font-weight="700" text-anchor="end">92%</text>
      <rect x="0" y="6" width="195" height="5" rx="2.5" fill="#1e293b"/>
      <rect x="0" y="6" width="179" height="5" rx="2.5" fill="#00f7ff" filter="url(#termSoftGlow)"/>

      <text x="0" y="26" fill="#94a3b8" class="mono-font" font-size="10" font-weight="600">Backend &amp; REST APIs</text>
      <text x="195" y="26" fill="#a855f7" class="mono-font" font-size="10" font-weight="700" text-anchor="end">96%</text>
      <rect x="0" y="32" width="195" height="5" rx="2.5" fill="#1e293b"/>
      <rect x="0" y="32" width="187" height="5" rx="2.5" fill="#a855f7" filter="url(#termSoftGlow)"/>

      <text x="0" y="52" fill="#94a3b8" class="mono-font" font-size="10" font-weight="600">Database Optimization</text>
      <text x="195" y="52" fill="#00ff88" class="mono-font" font-size="10" font-weight="700" text-anchor="end">88%</text>
      <rect x="0" y="58" width="195" height="5" rx="2.5" fill="#1e293b"/>
      <rect x="0" y="58" width="171" height="5" rx="2.5" fill="#00ff88" filter="url(#termSoftGlow)"/>

      <text x="0" y="78" fill="#94a3b8" class="mono-font" font-size="10" font-weight="600">UI/UX &amp; Neon Styling</text>
      <text x="195" y="78" fill="#ff7000" class="mono-font" font-size="10" font-weight="700" text-anchor="end">94%</text>
      <rect x="0" y="84" width="195" height="5" rx="2.5" fill="#1e293b"/>
      <rect x="0" y="84" width="183" height="5" rx="2.5" fill="#ff7000" filter="url(#termSoftGlow)"/>

      <text x="0" y="104" fill="#94a3b8" class="mono-font" font-size="10" font-weight="600">AI-Augmented Coding</text>
      <text x="195" y="104" fill="#38bdf8" class="mono-font" font-size="10" font-weight="700" text-anchor="end">98%</text>
      <rect x="0" y="110" width="195" height="5" rx="2.5" fill="#1e293b"/>
      <rect x="0" y="110" width="191" height="5" rx="2.5" fill="#38bdf8" filter="url(#termSoftGlow)"/>
    </g>

    <!-- Bottom Quote Panel -->
    <rect x="0" y="258" width="410" height="74" rx="8" fill="#0a0f24" stroke="#1e293b" stroke-width="1"/>
    <text x="14" y="280" fill="#00f7ff" class="mono-font" font-size="10.5" font-weight="700">CYBER WARLOCK PHILOSOPHY:</text>
    <text x="14" y="299" fill="#93c5fd" class="mono-font" font-size="10">"Code is not just logic; it is electric art carved</text>
    <text x="14" y="316" fill="#93c5fd" class="mono-font" font-size="10">into silicon, running at the speed of thought."</text>
  </g>

  <!-- RIGHT PANEL: INTERACTIVE CYBER TERMINAL WINDOW (neofetch) -->
  <g transform="translate(485, 72)">
    <text x="0" y="16" fill="#00ff88" class="mono-font" font-size="12" font-weight="700">
      fauzan@cyber-rig<tspan fill="#ffffff">:</tspan><tspan fill="#00f7ff">~</tspan><tspan fill="#ffffff">$ neofetch --cyber-spec</tspan>
    </text>
    <line x1="0" y1="28" x2="430" y2="28" stroke="#1e293b" stroke-width="1"/>

    <!-- Left ASCII Cyber Emblem -->
    <g transform="translate(0, 48)">
      <text x="0" y="16" fill="#00f7ff" class="mono-font" font-size="11" font-weight="900" filter="url(#termSoftGlow)">███████╗</text>
      <text x="0" y="32" fill="#00f7ff" class="mono-font" font-size="11" font-weight="900" filter="url(#termSoftGlow)">██╔════╝</text>
      <text x="0" y="48" fill="#a855f7" class="mono-font" font-size="11" font-weight="900" filter="url(#termSoftGlow)">█████╗</text>
      <text x="0" y="64" fill="#a855f7" class="mono-font" font-size="11" font-weight="900" filter="url(#termSoftGlow)">██╔══╝</text>
      <text x="0" y="80" fill="#00ff88" class="mono-font" font-size="11" font-weight="900" filter="url(#termSoftGlow)">██║</text>
      <text x="0" y="96" fill="#00ff88" class="mono-font" font-size="11" font-weight="900" filter="url(#termSoftGlow)">╚═╝</text>

      <text x="0" y="122" fill="#64748b" class="mono-font" font-size="9">RIG-667</text>
      <text x="0" y="136" fill="#00f7ff" class="mono-font" font-size="9" font-weight="700">ONLINE</text>
    </g>

    <!-- Neofetch Specs List -->
    <g transform="translate(95, 46)">
      <text x="0" y="14" fill="#00f7ff" class="mono-font" font-size="12" font-weight="900">fauzan</text>
      <text x="50" y="14" fill="#94a3b8" class="mono-font" font-size="12">@</text>
      <text x="60" y="14" fill="#a855f7" class="mono-font" font-size="12" font-weight="900">cyber-rig</text>
      <line x1="0" y1="20" x2="310" y2="20" stroke="#334155" stroke-width="1"/>

      <text x="0" y="38" fill="#00ff88" class="mono-font" font-size="10.5" font-weight="700">OS:</text>
      <text x="75" y="38" fill="#e2e8f0" class="mono-font" font-size="10.5">Arch Linux / CyberOS x86_64</text>

      <text x="0" y="56" fill="#00ff88" class="mono-font" font-size="10.5" font-weight="700">HOST:</text>
      <text x="75" y="56" fill="#e2e8f0" class="mono-font" font-size="10.5">Neural Quantum Rig 9000</text>

      <text x="0" y="74" fill="#00ff88" class="mono-font" font-size="10.5" font-weight="700">KERNEL:</text>
      <text x="75" y="74" fill="#e2e8f0" class="mono-font" font-size="10.5">6.11.2-cyber-hardened</text>

      <text x="0" y="92" fill="#00ff88" class="mono-font" font-size="10.5" font-weight="700">UPTIME:</text>
      <text x="75" y="92" fill="#e2e8f0" class="mono-font" font-size="10.5">999 Days, 42 Mins (Perpetual)</text>

      <text x="0" y="110" fill="#00ff88" class="mono-font" font-size="10.5" font-weight="700">SHELL:</text>
      <text x="75" y="110" fill="#e2e8f0" class="mono-font" font-size="10.5">zsh 5.9 (pure-cyber)</text>

      <text x="0" y="128" fill="#00ff88" class="mono-font" font-size="10.5" font-weight="700">EDITOR:</text>
      <text x="75" y="128" fill="#e2e8f0" class="mono-font" font-size="10.5">VS Code / Cursor / Neovim</text>

      <text x="0" y="146" fill="#00ff88" class="mono-font" font-size="10.5" font-weight="700">WM/DE:</text>
      <text x="75" y="146" fill="#e2e8f0" class="mono-font" font-size="10.5">Hyprland (Neon Wayland)</text>

      <text x="0" y="164" fill="#00ff88" class="mono-font" font-size="10.5" font-weight="700">CPU:</text>
      <text x="75" y="164" fill="#e2e8f0" class="mono-font" font-size="10.5">Neural Cortex 16-Core @ 5.4GHz</text>

      <text x="0" y="182" fill="#00ff88" class="mono-font" font-size="10.5" font-weight="700">GPU:</text>
      <text x="75" y="182" fill="#e2e8f0" class="mono-font" font-size="10.5">RTX 5090 Holographic Matrix</text>

      <text x="0" y="200" fill="#00ff88" class="mono-font" font-size="10.5" font-weight="700">MEMORY:</text>
      <text x="75" y="200" fill="#e2e8f0" class="mono-font" font-size="10.5">64GB DDR5 @ 6400MT/s</text>

      <text x="0" y="218" fill="#00ff88" class="mono-font" font-size="10.5" font-weight="700">STATUS:</text>
      <text x="75" y="218" fill="#00f7ff" class="mono-font" font-size="10.5" font-weight="700">CODING THE FUTURE // NO BUGS</text>

      <!-- Terminal 8 Neon Color Blocks -->
      <g transform="translate(0, 236)">
        <rect x="0" y="0" width="22" height="13" rx="3" fill="#060814"/>
        <rect x="26" y="0" width="22" height="13" rx="3" fill="#ff5555"/>
        <rect x="52" y="0" width="22" height="13" rx="3" fill="#00ff88"/>
        <rect x="78" y="0" width="22" height="13" rx="3" fill="#fde047"/>
        <rect x="104" y="0" width="22" height="13" rx="3" fill="#00f7ff"/>
        <rect x="130" y="0" width="22" height="13" rx="3" fill="#a855f7"/>
        <rect x="156" y="0" width="22" height="13" rx="3" fill="#ff7000"/>
        <rect x="182" y="0" width="22" height="13" rx="3" fill="#ffffff"/>
      </g>
    </g>

    <!-- Blinking Terminal Prompt Ready for Input -->
    <g transform="translate(0, 314)">
      <line x1="0" y1="0" x2="430" y2="0" stroke="#1e293b" stroke-width="1"/>
      <text x="0" y="20" fill="#00ff88" class="mono-font" font-size="11.5" font-weight="700">
        fauzan@cyber-rig<tspan fill="#ffffff">:</tspan><tspan fill="#00f7ff">~</tspan><tspan fill="#ffffff">$ </tspan>
        <tspan fill="#00f7ff" font-weight="900">█<animate attributeName="opacity" values="1;0;1" dur="0.9s" repeatCount="indefinite"/></tspan>
      </text>
    </g>
  </g>
</svg>'''


# ==============================================================================
# 6. NATIVE CYBER TROPHIES & ACHIEVEMENTS (trophies.svg)
# 100% self-hosted SVG - Fixes the broken 3rd party vercel link in photo 2
# ==============================================================================
def generate_trophies() -> str:
    trophies = [
        {
            "title": "REPO ARCHITECT",
            "grade": "RANK S+",
            "desc": "32+ REPOSITORIES",
            "color": "#fde047",
            "icon": '''
              <polygon points="0,-16 14,-6 8,14 -8,14 -14,-6" fill="url(#trophyGoldGrad)" stroke="#fde047" stroke-width="1.2" filter="url(#trophySoftGlow)"/>
              <circle cx="0" cy="0" r="4.5" fill="#ffffff"/>''',
        },
        {
            "title": "COMMIT TITAN",
            "grade": "RANK S+",
            "desc": "2,840+ COMMITS",
            "color": "#00ff88",
            "icon": '''
              <polygon points="3,-17 -7,0 1,0 -3,17 7,0 -1,0" fill="#00ff88" filter="url(#trophyGlow)"/>''',
        },
        {
            "title": "STREAK MASTER",
            "grade": "RANK S",
            "desc": "142D RECORD",
            "color": "#a855f7",
            "icon": '''
              <circle cx="0" cy="0" r="15" fill="none" stroke="#a855f7" stroke-width="2" stroke-dasharray="5 3"/>
              <circle cx="0" cy="0" r="10" fill="#060814"/>
              <text x="0" y="6" font-size="15" text-anchor="middle">🔥</text>''',
        },
        {
            "title": "PR SPECIALIST",
            "grade": "RANK A+",
            "desc": "85+ MERGED PRS",
            "color": "#00f7ff",
            "icon": '''
              <circle cx="-6" cy="8" r="3.5" fill="#00f7ff" filter="url(#trophySoftGlow)"/>
              <circle cx="6" cy="-8" r="3.5" fill="#00f7ff" filter="url(#trophySoftGlow)"/>
              <path d="M -6,5 L -6,-2 Q -6,-8 0,-8 L 3,-8" fill="none" stroke="#00f7ff" stroke-width="2"/>
              <line x1="-6" y1="5" x2="-6" y2="14" stroke="#00f7ff" stroke-width="2"/>''',
        },
        {
            "title": "DRAGON SLAYER",
            "grade": "RANK MAX",
            "desc": "120 FPS ENGINE",
            "color": "#ff0055",
            "icon": '''
              <path d="M 0,-16 C 9,-11 14,-2 9,7 C 4,16 -6,16 -11,9 C -16,2 -7,-9 0,-16 Z" fill="url(#trophyPinkGrad)" stroke="#ff0055" stroke-width="1.2" filter="url(#trophySoftGlow)"/>
              <circle cx="0" cy="0" r="3.5" fill="#fde047"/>''',
        },
        {
            "title": "STAR PIONEER",
            "grade": "RANK S",
            "desc": "120+ STARS",
            "color": "#f59e0b",
            "icon": '''
              <polygon points="0,-16 4.5,-5 16,-5 7,2 11,14 0,7 -11,14 -7,2 -16,-5 -4.5,-5" fill="url(#trophyGoldGrad)" stroke="#fde047" stroke-width="1.2" filter="url(#trophySoftGlow)"/>''',
        },
    ]

    card_items = []
    # 6 trophies spread across 880px (width ~136px each, spacing 12px)
    start_x = 34
    spacing = 144
    for idx, t in enumerate(trophies):
        bx = start_x + idx * spacing
        card_items.append(f'''
    <!-- Trophy {idx+1}: {t["title"]} -->
    <g transform="translate({bx}, 62)">
      <!-- Outer Card Box -->
      <rect x="0" y="0" width="134" height="114" rx="12" fill="#0b1126" stroke="#1e293b" stroke-width="1.2"/>
      <rect x="0" y="0" width="134" height="114" rx="12" fill="none" stroke="{t["color"]}" stroke-width="1" stroke-opacity="0.35"/>

      <!-- Glowing Base Pedestal -->
      <ellipse cx="67" cy="46" rx="28" ry="6" fill="{t["color"]}" opacity="0.2" filter="url(#trophySoftGlow)"/>

      <!-- Center Icon -->
      <g transform="translate(67, 40)">
        {t["icon"]}
      </g>

      <!-- Grade Rank Badge -->
      <rect x="36" y="68" width="62" height="18" rx="5" fill="{t["color"]}" fill-opacity="0.15" stroke="{t["color"]}" stroke-width="1"/>
      <text x="67" y="81" fill="{t["color"]}" font-family="monospace" font-size="10" font-weight="900" text-anchor="middle">{t["grade"]}</text>

      <!-- Title & Desc -->
      <text x="67" y="96" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">{t["title"]}</text>
      <text x="67" y="107" fill="#64748b" font-family="monospace" font-size="8.5" text-anchor="middle">{t["desc"]}</text>
    </g>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 196" width="100%">
  <defs>
    <linearGradient id="trophyBorderNeon" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f7ff"/>
      <stop offset="35%" stop-color="#a855f7"/>
      <stop offset="70%" stop-color="#00ff88"/>
      <stop offset="100%" stop-color="#fde047"/>
    </linearGradient>

    <linearGradient id="trophyGoldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="60%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>

    <linearGradient id="trophyPinkGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fda4af"/>
      <stop offset="60%" stop-color="#f43f5e"/>
      <stop offset="100%" stop-color="#881337"/>
    </linearGradient>

    <filter id="trophyGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="trophySoftGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    .title-font {{ font-family: 'Segoe UI', -apple-system, sans-serif; font-weight: 900; }}
    .mono-font {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
  </style>

  <!-- Card Background -->
  <rect x="6" y="6" width="928" height="184" rx="16" fill="#060814" stroke="#1e293b" stroke-width="1.8"/>

  <!-- Animated Neon Lighting Border -->
  <rect x="6" y="6" width="928" height="184" rx="16" fill="none" stroke="url(#trophyBorderNeon)" stroke-width="3" filter="url(#trophyGlow)" stroke-dasharray="220 300" stroke-linecap="round">
    <animate attributeName="stroke-dashoffset" from="0" to="-1040" dur="5s" repeatCount="indefinite"/>
  </rect>

  <!-- Corner Brackets -->
  <path d="M 18,32 L 18,18 L 32,18" stroke="#00f7ff" stroke-width="2.2" fill="none"/>
  <circle cx="18" cy="18" r="2.2" fill="#00f7ff"/>
  <path d="M 922,32 L 922,18 L 908,18" stroke="#a855f7" stroke-width="2.2" fill="none"/>
  <circle cx="922" cy="18" r="2.2" fill="#a855f7"/>
  <path d="M 18,164 L 18,178 L 32,178" stroke="#00ff88" stroke-width="2.2" fill="none"/>
  <circle cx="18" cy="178" r="2.2" fill="#00ff88"/>
  <path d="M 922,164 L 922,178 L 908,178" stroke="#fde047" stroke-width="2.2" fill="none"/>
  <circle cx="922" cy="178" r="2.2" fill="#fde047"/>

  <!-- Card Header -->
  <g transform="translate(470, 34)">
    <circle cx="-210" cy="-4" r="4" fill="#fde047" filter="url(#trophyGlow)"/>
    <text x="0" y="0" fill="#ffffff" class="title-font" font-size="16" letter-spacing="1.5" text-anchor="middle">
      🏆 GITHUB TROPHIES &amp; ACHIEVEMENTS
    </text>
    <circle cx="210" cy="-4" r="4" fill="#00ff88" filter="url(#trophyGlow)"/>
    <text x="0" y="16" fill="#94a3b8" class="mono-font" font-size="10" font-weight="600" letter-spacing="1" text-anchor="middle">
      VERIFIED DEVELOPER RIG // ELITE REPOSITORY MERITS
    </text>
  </g>

  <!-- Render All 6 Trophies -->
  {"".join(card_items)}
</svg>'''


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
def main():
    print("=" * 60)
    print("[*] CYBERPUNK NEON ASSET GENERATOR (fauzan667)")
    print("=" * 60)

    # 0. Neon Bar Divider
    validate_and_save(generate_neon_bar(), "neon-bar.svg")

    # 1. Header (Clean, Aesthetic, No Petir, No top bar)
    header_svg = generate_header()
    validate_and_save(header_svg, "header.svg")
    validate_and_save(header_svg, "cyber-header.svg")

    # 2. Tech Stack & Arsenal
    validate_and_save(generate_tech_stack(), "tech-stack.svg")

    # 3. Celestial Neon Dragon (Replaced Snake with Eastern Dragon)
    dragon_svg = generate_neon_dragon()
    validate_and_save(dragon_svg, "neon-viper.svg")
    validate_and_save(dragon_svg, "neon-dragon.svg")
    with open(os.path.join(DIST_DIR, "github-contribution-grid-snake.svg"), "w", encoding="utf-8") as f:
        f.write(dragon_svg)
    print("[+] Successfully generated: github-contribution-grid-snake.svg in dist/")

    # 4. Metrics Dashboard
    validate_and_save(generate_metrics_dashboard(), "metrics-dashboard.svg")

    # 5. Holographic RPG Skill Radar & Cyber Terminal
    validate_and_save(generate_cyber_terminal(), "cyber-terminal.svg")


    print("=" * 60)
    print("[SUCCESS] All Cyberpunk Neon SVG Assets successfully generated!")
    print(f"[>] Target Assets: {ASSETS_DIR}")
    print(f"[>] Target Dist:   {DIST_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
