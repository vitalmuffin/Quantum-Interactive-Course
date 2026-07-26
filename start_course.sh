#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
PORT="${1:-8000}"
echo "Serving Quantum – Das Kleinste verstehen at http://localhost:${PORT}/"
echo "Stop with Ctrl+C."
python3 -m http.server "$PORT"
