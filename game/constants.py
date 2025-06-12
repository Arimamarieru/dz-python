# ── размеры поля ───────────────────────────────────────
DEFAULT_WIDTH   = 20
DEFAULT_HEIGHT  = 10

# ── тайлы карты ────────────────────────────────────────
TILE_EMPTY      = '🟩'
TILE_TREE       = '🌲'
TILE_FIRE       = '🔥'
TILE_ASH        = '⬛'
TILE_RIVER      = '🌊'
TILE_HELICOPTER = '🚁'
TILE_HOSPITAL   = '🏥'
TILE_SHOP       = '🏪'

# ── вероятности (на один тик) ─────────────────────────
TREE_GROW_BASE  = 0.01
FIRE_START_BASE = 0.002   # реже вспыхивает
FIRE_SPREAD_CH  = 0.15    # медленнее ползёт
LIGHTNING_CH    = 0.003   # реже молния

# ── вертолёт и экономика ──────────────────────────────
START_LIVES     = 3       # начальные жизни
START_CAP       = 1       # ёмкость бака
HEAL_COST       = 3       # очков за +1 жизнь
UPGRADE_COST    = 5       # очков за +1 вместимость

# ── файлы / клавиши ───────────────────────────────────
SAVE_FILE        = 'save.json'
WATER_RELOAD_KEY = 'e'  
EXTINGUISH_KEY   = 'q'
HEAL_KEY         = 'h'
UPGRADE_KEY      = 'u'
