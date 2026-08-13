return (
  <div className="container">
    <h1>💸 Currency Converter ✨</h1>

    <input
      type="number"
      value={amount}
      onChange={(e) => setAmount(Number(e.target.value))}
      placeholder="Enter amount"
    />

    <div className="selectors">
      <select
        value={fromCurrency}
        onChange={(e) => setFromCurrency(e.target.value)}
      >
        <option value="USD">🇺🇸 USD</option>
        <option value="EUR">🇪🇺 EUR</option>
        <option value="GBP">🇬🇧 GBP</option>
        <option value="JPY">🇯🇵 JPY</option>
      </select>

      <span className="arrow">➜</span>

      <select
        value={toCurrency}
        onChange={(e) => setToCurrency(e.target.value)}
      >
        <option value="USD">🇺🇸 USD</option>
        <option value="EUR">🇪🇺 EUR</option>
        <option value="GBP">🇬🇧 GBP</option>
        <option value="JPY">🇯🇵 JPY</option>
      </select>
    </div>

    <div className="result-card">
      <p>Converted Amount</p>
      <h2>
        {convertedAmounts[toCurrency].toFixed(2)} {toCurrency}
      </h2>
    </div>
  </div>
);