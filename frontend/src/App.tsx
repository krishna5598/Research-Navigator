import "./App.css";

function App() {
  return (
    <div className="app">
      <div className="container">

        <h1>AI Research Navigator</h1>

        <div className="section">
          <label>Requirement</label>

          <textarea
            placeholder="Describe what you are looking for..."
            rows={6}
          />
        </div>

        <div className="section">
          <label>Search Requirements</label>

          <div className="checkbox-grid">

            <label>
              <input type="checkbox" />
              Repositories
            </label>

            <label>
              <input type="checkbox" />
              Documentation
            </label>

            <label>
              <input type="checkbox" />
              Research Papers
            </label>

            <label>
              <input type="checkbox" />
              Datasets
            </label>

            <label>
              <input type="checkbox" />
              Blogs
            </label>

            <label>
              <input type="checkbox" />
              Stack Overflow
            </label>

          </div>
        </div>

        <div className="section">
          <label>Website (Optional)</label>

          <input
            type="text"
            placeholder="https://huggingface.co"
          />
        </div>

        <button className="search-btn">
          Search
        </button>

        <div className="results">

          <h2>Results</h2>

          <p>
            Search results will appear here...
          </p>

        </div>

      </div>
    </div>
  );
}

export default App;