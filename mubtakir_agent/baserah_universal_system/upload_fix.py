#!/usr/bin/env python3
"""
رفع الإصلاحات إلى Hugging Face
"""

import os
import shutil

def copy_fixed_files():
    """نسخ الملفات المصححة"""
    
    print("🔧 Copying fixed files...")
    
    # Create backup
    if os.path.exists('app_backup.py'):
        os.remove('app_backup.py')
    
    # Copy current app.py as backup
    shutil.copy('app.py', 'app_backup.py')
    print("✅ Backup created: app_backup.py")
    
    # Verify the fix is in place
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "matplotlib.use('Agg')" in content:
        print("✅ matplotlib backend fix: FOUND")
    else:
        print("❌ matplotlib backend fix: MISSING")
        
    if 'type="filepath"' in content:
        print("✅ Gradio filepath type: FOUND")
    else:
        print("❌ Gradio filepath type: MISSING")
        
    if 'tempfile.NamedTemporaryFile' in content:
        print("✅ Temporary file handling: FOUND")
    else:
        print("❌ Temporary file handling: MISSING")
    
    print("\n🎯 Files ready for manual upload to Hugging Face!")
    print("📁 Main file: app.py")
    print("📁 Backup: app_backup.py")
    
    return True

if __name__ == "__main__":
    copy_fixed_files()
