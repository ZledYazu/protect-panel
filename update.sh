#### **📄 update.sh**
```bash
#!/bin/bash
echo "🔄 Updating Protect Panel..."
git pull
pip install -r requirements.txt --upgrade
echo "✅ Update complete!"