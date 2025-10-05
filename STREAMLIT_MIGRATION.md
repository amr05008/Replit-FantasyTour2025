# Streamlit Cloud Migration Guide

## Overview
This document records the complete migration process from Replit to Streamlit Cloud deployment for the Fantasy Tour de France 2025 application.

---

## What is Streamlit Cloud?

Streamlit Cloud is a free hosting platform built specifically for Streamlit apps by the same company that makes Streamlit. It's designed to deploy directly from GitHub repositories with zero configuration needed.

**Key features:**
- **Free tier** includes 1 app with unlimited viewers
- **Auto-deploys** on every git push to your main branch
- **Built-in secrets management** (for API keys, though you don't need it)
- **Custom subdomains** like `yourapp.streamlit.app`
- **Analytics** showing visitor stats and app usage
- **Logs viewer** for debugging

---

## Complete Migration Task List

### **Pre-Deployment Setup**

1. **Renamed dependencies file**
   - Changed `dependencies.txt` → `requirements.txt` (Python standard naming)
   ```bash
   mv dependencies.txt requirements.txt
   ```

2. **Added missing dependency**
   - Added `plotly>=5.0.0` to `requirements.txt` (was being used but not listed)

3. **Moved configuration file**
   - Created `.streamlit/` directory
   - Moved `config.toml` → `.streamlit/config.toml` (Streamlit convention)
   ```bash
   mkdir -p .streamlit
   mv config.toml .streamlit/config.toml
   ```

4. **Committed initial changes**
   ```bash
   git add -A
   git commit -m "Prepare for Streamlit Cloud deployment"
   ```

5. **Pushed to GitHub**
   ```bash
   git push origin main
   ```

### **Troubleshooting & Fixes**

6. **Fixed port configuration issue**
   - **Problem:** Error message on deployment:
     ```
     ❗️ The service has encountered an error while checking the health of the Streamlit app:
     Get "http://localhost:8501/healthz": dial tcp 127.0.0.1:8501: connect: connection refused
     ```
   - **Root cause:** Replit-specific port configuration (`port = 5000`) conflicted with Streamlit Cloud's expected port (8501)
   - **Solution:** Edited `.streamlit/config.toml`:
     - Removed `port = 5000`
     - Removed `address = "0.0.0.0"`
     - Kept only `headless = true` setting

7. **Committed configuration fix**
   ```bash
   git add .streamlit/config.toml
   git commit -m "Fix Streamlit Cloud deployment - remove port override"
   ```

8. **Pushed fix to GitHub**
   ```bash
   git push origin main
   ```
   - This triggered automatic redeployment on Streamlit Cloud

### **Streamlit Cloud Deployment Steps**

9. **Deployed application**
   - Visited [share.streamlit.io](https://share.streamlit.io)
   - Signed in with GitHub
   - Clicked "New app"
   - Filled in deployment form:
     - **Repository:** `Replit-FantasyTour2025`
     - **Branch:** `main`
     - **Main file path:** `app.py`
     - **App URL:** Custom subdomain choice
   - Clicked "Deploy!"

10. **Verified deployment**
    - Waited 2-3 minutes for initial deployment
    - After config fix: Health check passed
    - Confirmed app is live and accessible

---

## Key Differences: Replit vs Streamlit Cloud

| Feature | Replit | Streamlit Cloud |
|---------|--------|-----------------|
| **Port** | Custom (5000) | Default (8501) |
| **Deployment** | Manual start command | Automatic from GitHub |
| **Updates** | Manual redeploy | Auto-deploy on git push |
| **Configuration** | Custom config needed | Minimal config required |
| **URL** | `*.replit.app` | `*.streamlit.app` |

---

## Files Changed

### **New/Renamed Files:**
- ✅ `requirements.txt` (renamed from `dependencies.txt`)
- ✅ `.streamlit/config.toml` (moved from root `config.toml`)

### **Modified Files:**
- ✅ `requirements.txt` - Added `plotly>=5.0.0`
- ✅ `.streamlit/config.toml` - Removed port/address overrides

### **No Changes Required:**
- ✅ `app.py` - Works perfectly as-is
- ✅ Google Sheets URLs - Still public and accessible
- ✅ All other project files

---

## Post-Deployment Management

### **Updating Your App:**
Just push to GitHub - Streamlit Cloud auto-deploys:
```bash
# Make changes to app.py or other files
git add .
git commit -m "Your update message"
git push origin main
# Streamlit Cloud automatically redeploys in ~2 minutes
```

### **Accessing Your App Dashboard:**
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click on your app name to see:
   - **Logs** - Real-time application logs
   - **Analytics** - Viewer counts and usage stats
   - **Settings** - Branch, Python version, advanced config
   - **Reboot** - Restart the app manually
   - **Delete** - Remove the deployment

### **Custom Domain (Optional):**
In app settings, you can add a custom domain (e.g., `tdf.yoursite.com`)
- Requires DNS CNAME configuration

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"No module named 'plotly'"** | Add `plotly>=5.0.0` to `requirements.txt` |
| **Health check fails (port 8501 error)** | Remove `port` setting from `.streamlit/config.toml` |
| **App won't start** | Check logs in Streamlit Cloud dashboard |
| **GitHub repo not showing** | Re-authorize GitHub permissions in Streamlit Cloud settings |

---

## Free Tier Limits

Your app easily fits within the free tier:
- ✅ **1 public app**
- ✅ **Unlimited viewers**
- ✅ **1 GB RAM** (your app uses ~200MB)
- ✅ **1 CPU core** (plenty for 5 participants)
- ✅ **Community support**

---

## Quick Reference: Migration Checklist

```bash
# 1. Rename dependencies file
mv dependencies.txt requirements.txt

# 2. Add missing dependency
echo "plotly>=5.0.0" >> requirements.txt

# 3. Move config file
mkdir -p .streamlit
mv config.toml .streamlit/config.toml

# 4. Remove port overrides from .streamlit/config.toml
# Keep only: [server]\nheadless = true

# 5. Commit and push
git add .
git commit -m "Prepare for Streamlit Cloud"
git push origin main

# 6. Deploy at share.streamlit.io
```

---

## Result

✅ **Successfully migrated from Replit to Streamlit Cloud**
- Zero code changes to `app.py` required
- Only configuration adjustments needed
- Automatic deployments now enabled
- App accessible at custom `*.streamlit.app` URL

---

## Repository Information

- **GitHub Repository:** https://github.com/amr05008/Replit-FantasyTour2025
- **Original Platform:** Replit
- **Current Platform:** Streamlit Cloud
- **Migration Date:** October 4, 2025
- **Migration Assistant:** Claude Code

---

## Related Documentation

See also:
- [CLAUDE.md](CLAUDE.md) - Project overview and architecture
- [README.md](README.md) - User-facing documentation
- [replit.md](replit.md) - Development history on Replit
- [BACKUP_STEPS.md](BACKUP_STEPS.md) - Git backup instructions
