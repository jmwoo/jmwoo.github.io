---
title: Weight
---

<div id="weight-container">
  <div id="weight-header">
    <div id="weight-current">
      <span id="weight-value">--</span>
      <span id="weight-unit">lbs</span>
    </div>
    <div id="weight-change">
      <span id="change-value">--</span>
      <span id="change-percent">(--)</span>
    </div>
  </div>

  <div id="weight-ranges">
    <button class="range-btn" data-range="1D">1D</button>
    <button class="range-btn" data-range="5D">5D</button>
    <button class="range-btn" data-range="1M">1M</button>
    <button class="range-btn" data-range="6M">6M</button>
    <button class="range-btn" data-range="YTD">YTD</button>
    <button class="range-btn active" data-range="1Y">1Y</button>
    <button class="range-btn" data-range="5Y">5Y</button>
    <button class="range-btn" data-range="MAX">MAX</button>
  </div>

  <div id="weight-chart"></div>
</div>

<style>
#weight-container {
  width: 100%;
}

#weight-header {
  margin-bottom: 1rem;
}

#weight-current {
  font-size: 2rem;
  font-weight: 600;
}

#weight-value {
  color: #333;
}

#weight-unit {
  color: #666;
  font-size: 1rem;
  margin-left: 0.25rem;
}

#weight-change {
  font-size: 0.95rem;
  margin-top: 0.25rem;
}

#change-value, #change-percent {
  color: #666;
}

#weight-change.positive #change-value,
#weight-change.positive #change-percent {
  color: #666;
}

#weight-change.negative #change-value,
#weight-change.negative #change-percent {
  color: #666;
}

#weight-ranges {
  display: flex;
  gap: 0.25rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.range-btn {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 4px;
  padding: 0.4rem 0.8rem;
  font-family: inherit;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.2s;
  color: #333;
}

.range-btn:hover {
  background: #e9ecef;
}

.range-btn.active {
  background: #2e7bcf;
  border-color: #2e7bcf;
  color: white;
}

#weight-chart {
  width: 100%;
  height: 400px;
  border-radius: 6px;
}

#weight-chart table,
#weight-chart tr,
#weight-chart td {
  color: #333;
  background: transparent;
  border: none;
  padding: 0;
  margin: 0;
}

@media (max-width: 768px) {
  #weight-chart {
    height: 300px;
  }

  #weight-current {
    font-size: 1.6rem;
  }

  .range-btn {
    padding: 0.3rem 0.6rem;
    font-size: 0.8rem;
  }
}
</style>

<script src="https://unpkg.com/lightweight-charts@4.1.0/dist/lightweight-charts.standalone.production.js"></script>

<script>
(function() {
  // Hardcoded weight data - will eventually fetch from remote
  const weightData = [
    { date: '2026-01-05', weight: 227.5 },
    { date: '2026-01-06', weight: 224.4 },
    { date: '2026-01-07', weight: 224.2 },
    { date: '2026-01-18', weight: 225.3 },
  ];

  // Convert to lightweight-charts format
  function toChartData(data) {
    return data.map(d => ({
      time: d.date,
      value: d.weight
    }));
  }

  // Filter data by range
  function filterByRange(data, range) {
    const now = new Date();
    let startDate;

    switch (range) {
      case '1D':
        startDate = new Date(now);
        startDate.setDate(startDate.getDate() - 1);
        break;
      case '5D':
        startDate = new Date(now);
        startDate.setDate(startDate.getDate() - 5);
        break;
      case '1M':
        startDate = new Date(now);
        startDate.setMonth(startDate.getMonth() - 1);
        break;
      case '6M':
        startDate = new Date(now);
        startDate.setMonth(startDate.getMonth() - 6);
        break;
      case 'YTD':
        startDate = new Date(now.getFullYear(), 0, 1);
        break;
      case '1Y':
        startDate = new Date(now);
        startDate.setFullYear(startDate.getFullYear() - 1);
        break;
      case '5Y':
        startDate = new Date(now);
        startDate.setFullYear(startDate.getFullYear() - 5);
        break;
      case 'MAX':
      default:
        return data;
    }

    return data.filter(d => new Date(d.date) >= startDate);
  }

  // Update header display
  function updateHeader(filteredData) {
    if (filteredData.length === 0) return;

    const latest = filteredData[filteredData.length - 1];
    const first = filteredData[0];
    const change = latest.weight - first.weight;
    const changePercent = ((change / first.weight) * 100).toFixed(2);

    document.getElementById('weight-value').textContent = latest.weight.toFixed(1);
    document.getElementById('change-value').textContent =
      (change >= 0 ? '+' : '') + change.toFixed(1) + ' lbs';
    document.getElementById('change-percent').textContent =
      '(' + (change >= 0 ? '+' : '') + changePercent + '%)';

    const changeEl = document.getElementById('weight-change');
    changeEl.classList.remove('positive', 'negative');
    changeEl.classList.add(change >= 0 ? 'positive' : 'negative');
  }

  // Initialize chart
  const chartContainer = document.getElementById('weight-chart');
  const chart = LightweightCharts.createChart(chartContainer, {
    layout: {
      background: { type: 'solid', color: '#ffffff' },
      textColor: '#333',
      fontFamily: "'Consolas', 'Monaco', 'Courier New', monospace",
    },
    grid: {
      vertLines: { color: '#f0f0f0' },
      horzLines: { color: '#f0f0f0' },
    },
    crosshair: {
      mode: LightweightCharts.CrosshairMode.Normal,
      vertLine: {
        color: '#2e7bcf',
        width: 1,
        style: LightweightCharts.LineStyle.Dashed,
        labelBackgroundColor: '#2e7bcf',
      },
      horzLine: {
        color: '#2e7bcf',
        width: 1,
        style: LightweightCharts.LineStyle.Dashed,
        labelBackgroundColor: '#2e7bcf',
      },
    },
    rightPriceScale: {
      borderColor: '#e9ecef',
    },
    timeScale: {
      borderColor: '#e9ecef',
      timeVisible: false,
    },
    handleScale: {
      mouseWheel: true,
      pinch: true,
    },
    handleScroll: {
      mouseWheel: true,
      pressedMouseMove: true,
      horzTouchDrag: true,
      vertTouchDrag: false,
    },
  });

  const lineSeries = chart.addLineSeries({
    color: '#2e7bcf',
    lineWidth: 2,
    crosshairMarkerVisible: true,
    crosshairMarkerRadius: 5,
    crosshairMarkerBorderColor: '#2e7bcf',
    crosshairMarkerBackgroundColor: '#ffffff',
    lastValueVisible: false,
    priceLineVisible: false,
    priceFormat: {
      type: 'custom',
      formatter: (price) => price.toFixed(1) + ' lbs',
    },
  });

  // Set initial data
  let currentRange = '1Y';
  function setRange(range) {
    currentRange = range;
    const filtered = filterByRange(weightData, range);
    lineSeries.setData(toChartData(filtered));
    updateHeader(filtered);
    chart.timeScale().fitContent();

    // Update active button
    document.querySelectorAll('.range-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.range === range);
    });
  }

  // Subscribe to crosshair move for live updates
  chart.subscribeCrosshairMove((param) => {
    if (param.time) {
      const data = param.seriesData.get(lineSeries);
      if (data) {
        document.getElementById('weight-value').textContent = data.value.toFixed(1);
      }
    } else {
      // Mouse left chart, show latest value
      const filtered = filterByRange(weightData, currentRange);
      if (filtered.length > 0) {
        document.getElementById('weight-value').textContent =
          filtered[filtered.length - 1].weight.toFixed(1);
      }
    }
  });

  // Range button handlers
  document.querySelectorAll('.range-btn').forEach(btn => {
    btn.addEventListener('click', () => setRange(btn.dataset.range));
  });

  // Handle resize
  const resizeObserver = new ResizeObserver(entries => {
    for (const entry of entries) {
      chart.applyOptions({
        width: entry.contentRect.width,
        height: entry.contentRect.height,
      });
    }
  });
  resizeObserver.observe(chartContainer);

  // Initialize
  setRange('1Y');
})();
</script>
