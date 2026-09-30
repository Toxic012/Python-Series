from flask import Flask, request, jsonify
import whois
from datetime import datetime

app = Flask(__name__)

# ---------- HTML + CSS TEMPLATE ----------
html_page = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Whois Lookup</title>
  <style>
    :root {
      --bg: #0f1724;
      --card: #101827;
      --text: #e6eef8;
      --muted: #9aa0b3;
      --accent: #7c5cff;
      --radius: 12px;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: 'Segoe UI', Roboto, sans-serif;
      background: linear-gradient(180deg, #071122 0%, #071522 40%);
      color: var(--text);
      padding: 40px;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }
    .container {
      max-width: 720px;
      width: 100%;
      background: var(--card);
      border-radius: var(--radius);
      padding: 25px;
      box-shadow: 0 0 25px rgba(0,0,0,0.5);
    }
    h1 {
      margin: 0;
      font-size: 26px;
      text-align: center;
    }
    p {
      text-align: center;
      color: var(--muted);
      font-size: 14px;
      margin-top: 5px;
    }
    form {
      margin-top: 20px;
      display: flex;
      gap: 10px;
    }
    input[type="text"] {
      flex: 1;
      padding: 12px;
      border-radius: 8px;
      border: 1px solid rgba(255,255,255,0.1);
      background: rgba(255,255,255,0.05);
      color: var(--text);
      font-size: 15px;
    }
    button {
      padding: 12px 18px;
      background: linear-gradient(90deg, var(--accent), #5ab7ff);
      border: none;
      border-radius: 8px;
      color: #fff;
      font-weight: bold;
      cursor: pointer;
      transition: transform 0.15s ease;
    }
    button:hover { transform: translateY(-2px); }
    .status {
      text-align: center;
      margin-top: 15px;
      font-size: 14px;
      color: var(--muted);
    }
    pre {
      margin-top: 20px;
      background: rgba(255,255,255,0.03);
      padding: 15px;
      border-radius: 8px;
      font-size: 13px;
      overflow-x: auto;
      max-height: 400px;
      white-space: pre-wrap;
      word-wrap: break-word;
      color: #dfeefc;
    }
    footer {
      text-align: center;
      margin-top: 20px;
      font-size: 13px;
      color: var(--muted);
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Whois Lookup</h1>
    <p>Check domain registration details quickly</p>
    <form id="lookupForm" onsubmit="return false;">
      <input id="domainInput" type="text" placeholder="Enter domain — e.g. example.com" />
      <button id="lookupBtn">Lookup</button>
    </form>
    <div id="status" class="status"></div>
    <pre id="result" style="display:none;"></pre>
    <footer>Made with ❤️ using Flask + python-whois</footer>
  </div>

  <script>
    const btn = document.getElementById('lookupBtn');
    const domainInput = document.getElementById('domainInput');
    const status = document.getElementById('status');
    const result = document.getElementById('result');

    btn.addEventListener('click', async () => {
      const domain = domainInput.value.trim();
      if (!domain) {
        status.textContent = "Please enter a domain.";
        return;
      }
      status.textContent = "Looking up...";
      result.style.display = 'none';
      try {
        const res = await fetch('/lookup', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({domain})
        });
        const data = await res.json();
        if (res.ok) {
          status.textContent = "✅ Lookup Successful!";
          result.textContent = JSON.stringify(data.result, null, 2);
          result.style.display = 'block';
        } else {
          status.textContent = "❌ " + (data.error || "Lookup failed");
        }
      } catch (e) {
        status.textContent = "⚠️ Error: " + e.message;
      }
    });
  </script>
</body>
</html>
"""

# ---------- BACKEND ROUTES ----------
@app.route("/")
def index():
    return html_page

@app.route("/lookup", methods=["POST"])
def lookup():
    try:
        domain = (request.json.get("domain") or "").strip()
        if not domain:
            return jsonify({"error": "No domain provided"}), 400

        if domain.startswith("http://") or domain.startswith("https://"):
            domain = domain.split("://", 1)[1]
        domain = domain.split("/", 1)[0]

        w = whois.whois(domain)
        result = convert_whois(w)
        return jsonify({"domain": domain, "result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------- HELPER ----------
def convert_whois(data):
    def fmt(v):
        if isinstance(v, datetime):
            return v.isoformat()
        if isinstance(v, (list, set, tuple)):
            return [fmt(x) for x in v]
        return str(v)
    if isinstance(data, dict):
        return {k: fmt(v) for k, v in data.items()}
    elif hasattr(data, "__dict__"):
        return {k: fmt(v) for k, v in data.__dict__.items()}
    else:
        return str(data)

# ---------- MAIN ----------
if __name__ == "__main__":
    print("🚀 Running on http://127.0.0.1:5000")
    app.run(debug=True)
