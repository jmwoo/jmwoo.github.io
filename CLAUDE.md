# CLAUDE.md

## Project Overview

Personal website hosted on GitHub Pages. Jekyll-based static site with a separate React diet app.

## Architecture

- **Generator**: Jekyll (GitHub Pages native)
- **Styling**: Custom CSS, monospace fonts (Consolas, Monaco), responsive grid
- **React app**: Diet tracker at `/diet/` (compiled, source not in this repo)
- **Layout**: `_layouts/default.html` with optional sidebar system via front matter

## Key Files

- `training.md` - Workout plan (currently static markdown)
- `weight.md` - Weight tracking with interactive chart
- `invest.md` - Investment allocations
- `schedule.md`, `sleep.md`, `about.md`, `resume.md` - Other content pages
- `_config.yml` - Jekyll configuration

## Weight Page (`/weight`)

Interactive weight tracking chart using [Lightweight Charts](https://www.tradingview.com/lightweight-charts/) (TradingView).

**Features:**
- Google Finance-style line chart with crosshair hover
- Time range selectors: 1D, 5D, 1M, 6M, YTD, 1Y, 5Y, MAX
- Header shows current weight + change from period start
- Site theme colors (blue #2e7bcf, monospace fonts)

**Data format:**
```js
const weightData = [
  { date: '2026-01-05', weight: 227.5 },
  // ...
];
```

**Note:** Chart requires CSS overrides for table elements inside `#weight-chart` to prevent site styles from affecting axis labels.

## Data Backend (Supabase)

**Decision:** Use Supabase for all dynamic data (weight, workouts, etc.)

### Setup
- **Database:** Supabase Postgres
- **Auth:** Google OAuth (only owner's Google account can write)
- **Access:** Public read, authenticated write via Row Level Security

### Schema (planned)
```sql
-- Weight tracking
CREATE TABLE weight (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  date DATE NOT NULL,
  weight DECIMAL NOT NULL,
  user_id UUID REFERENCES auth.users(id),
  created_at TIMESTAMPTZ DEFAULT now()
);

-- RLS policies
ALTER TABLE weight ENABLE ROW LEVEL SECURITY;
CREATE POLICY "public read" ON weight FOR SELECT USING (true);
CREATE POLICY "owner write" ON weight FOR ALL USING (auth.uid() = user_id);
```

### Client Integration
- Supabase JS client loaded via CDN
- Fetch data on page load (public, no auth needed)
- Write data requires Google sign-in (form UI, owner only)

### TODO
- [ ] Create Supabase project
- [ ] Enable Google OAuth provider
- [ ] Create `weight` table with RLS policies
- [ ] Update `weight.md` to fetch from Supabase
- [ ] Add weight entry form (authenticated)

## Future Features

1. **Workout tracking** - Same pattern, new table
2. **Other data** - Extensible to any tracked metrics
