#!/usr/bin/env bash
# Jalankan server lokal: ./scripts/serve.sh [port]
cd "$(dirname "$0")/.." && python3 -m http.server "${1:-8000}"
