#!/bin/bash
echo "🚀 Setting up Protect Panel V1.0.0..."
git clone https://github.com/ZledYazu/protect-panel.git
cd protect-panel
pip install -r requirements.txt
echo ""
echo "✅ Setup complete!"
echo "📌 Run: python protect-panel.py"