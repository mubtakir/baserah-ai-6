#!/usr/bin/env python3
"""
مُشغل نظام بصيرة الثوري المبسط
Simplified Basera AI System Launcher

🌟 نظام متكامل لتشغيل نظام بصيرة بسهولة
🚀 واجهة مبسطة للمستخدمين
🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله

المطور: باسل يحيى عبدالله
"""

import os
import sys
import subprocess
import time
from datetime import datetime

def print_header():
    """طباعة رأس النظام"""
    print("=" * 70)
    print("🌟 نظام بصيرة الثوري - مُشغل مبسط")
    print("🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله")
    print("📅 التاريخ:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("=" * 70)

def check_requirements():
    """فحص المتطلبات"""
    print("\n🔍 فحص المتطلبات...")
    
    # فحص Python
    python_version = sys.version_info
    if python_version.major >= 3 and python_version.minor >= 8:
        print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    else:
        print(f"❌ Python {python_version.major}.{python_version.minor} - يتطلب Python 3.8+")
        return False
    
    # فحص المكتبات الأساسية
    required_modules = ['numpy', 'matplotlib', 'gradio']
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module}")
        except ImportError:
            print(f"❌ {module} - غير مثبت")
            missing_modules.append(module)
    
    if missing_modules:
        print(f"\n⚠️ مكتبات مفقودة: {', '.join(missing_modules)}")
        print("💡 قم بتشغيل: pip install -r requirements.txt")
        return False
    
    return True

def run_tests():
    """تشغيل الاختبارات"""
    print("\n🧪 تشغيل اختبارات سريعة...")
    
    test_files = [
        "revolutionary_mother_equation.py",
        "complete_multi_layer_thinking_core.py",
        "advanced_mathematical_components.py"
    ]
    
    passed = 0
    total = len(test_files)
    
    for test_file in test_files:
        if os.path.exists(test_file):
            try:
                result = subprocess.run([sys.executable, test_file], 
                                      capture_output=True, text=True, timeout=30)
                if result.returncode == 0:
                    print(f"✅ {test_file}")
                    passed += 1
                else:
                    print(f"❌ {test_file}")
            except subprocess.TimeoutExpired:
                print(f"⏰ {test_file} - انتهت المهلة")
            except Exception as e:
                print(f"❌ {test_file} - خطأ: {e}")
        else:
            print(f"❌ {test_file} - غير موجود")
    
    print(f"\n📊 نتائج الاختبار: {passed}/{total} نجح")
    return passed >= total // 2  # نجاح إذا نجح نصف الاختبارات على الأقل

def show_menu():
    """عرض القائمة الرئيسية"""
    print("\n🚀 خيارات التشغيل:")
    print("   1️⃣  تشغيل واجهة Gradio التفاعلية")
    print("   2️⃣  تشغيل واجهة سطر الأوامر (CLI)")
    print("   3️⃣  تشغيل الواجهة الفنية")
    print("   4️⃣  تشغيل اختبارات شاملة")
    print("   5️⃣  اختبار المعادلة الأم الثورية")
    print("   6️⃣  اختبار النواة التفكيرية")
    print("   7️⃣  عرض معلومات النظام")
    print("   0️⃣  الخروج")
    print("-" * 50)

def launch_gradio():
    """تشغيل واجهة Gradio"""
    print("\n🎨 تشغيل واجهة Gradio التفاعلية...")
    try:
        subprocess.run([sys.executable, "multi_user_interfaces.py", "--interface", "gradio"])
    except KeyboardInterrupt:
        print("\n⚠️ تم إيقاف واجهة Gradio")
    except Exception as e:
        print(f"❌ خطأ في تشغيل Gradio: {e}")

def launch_cli():
    """تشغيل واجهة CLI"""
    print("\n🖥️ تشغيل واجهة سطر الأوامر...")
    try:
        subprocess.run([sys.executable, "multi_user_interfaces.py", "--interface", "cli"])
    except KeyboardInterrupt:
        print("\n⚠️ تم إيقاف واجهة CLI")
    except Exception as e:
        print(f"❌ خطأ في تشغيل CLI: {e}")

def launch_artistic():
    """تشغيل الواجهة الفنية"""
    print("\n🎨 تشغيل الواجهة الفنية...")
    try:
        subprocess.run([sys.executable, "artistic_inference_interface.py"])
    except KeyboardInterrupt:
        print("\n⚠️ تم إيقاف الواجهة الفنية")
    except Exception as e:
        print(f"❌ خطأ في تشغيل الواجهة الفنية: {e}")

def run_comprehensive_tests():
    """تشغيل الاختبارات الشاملة"""
    print("\n🧪 تشغيل الاختبارات الشاملة...")
    try:
        subprocess.run([sys.executable, "comprehensive_testing_system.py"])
    except KeyboardInterrupt:
        print("\n⚠️ تم إيقاف الاختبارات")
    except Exception as e:
        print(f"❌ خطأ في تشغيل الاختبارات: {e}")

def test_component(filename, name):
    """اختبار مكون محدد"""
    print(f"\n🧪 اختبار {name}...")
    if not os.path.exists(filename):
        print(f"❌ الملف غير موجود: {filename}")
        return
    
    try:
        result = subprocess.run([sys.executable, filename], 
                              capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            print(f"✅ نجح اختبار {name}")
            if result.stdout:
                # عرض أول 500 حرف من النتيجة
                output = result.stdout[:500] + "..." if len(result.stdout) > 500 else result.stdout
                print(f"📊 النتيجة:\n{output}")
        else:
            print(f"❌ فشل اختبار {name}")
            if result.stderr:
                print(f"🔍 الخطأ: {result.stderr[:300]}")
    except subprocess.TimeoutExpired:
        print(f"⏰ انتهت مهلة اختبار {name}")
    except Exception as e:
        print(f"❌ خطأ في اختبار {name}: {e}")

def show_system_info():
    """عرض معلومات النظام"""
    print("\n🌟 معلومات نظام بصيرة الثوري:")
    print("-" * 50)
    print(f"🧬 المطور: باسل يحيى عبدالله")
    print(f"🐍 إصدار Python: {sys.version.split()[0]}")
    print(f"💻 نظام التشغيل: {os.name}")
    print(f"📁 المجلد الحالي: {os.getcwd()}")
    
    # حساب عدد الملفات
    py_files = [f for f in os.listdir('.') if f.endswith('.py')]
    print(f"📊 عدد ملفات Python: {len(py_files)}")
    
    # حساب الحجم الإجمالي
    total_size = 0
    for filename in py_files:
        try:
            total_size += os.path.getsize(filename)
        except:
            pass
    
    print(f"📊 الحجم الإجمالي: {total_size/1024:.1f} KB")
    
    print(f"\n🎯 الميزات الرئيسية:")
    print(f"   🧮 رياضيات نقية بدون مكتبات AI تقليدية")
    print(f"   🧬 تطبيق 3 نظريات ثورية مبتكرة")
    print(f"   🖥️ واجهات مستخدم متعددة")
    print(f"   🧪 نظام اختبار شامل")
    print(f"   🎨 وحدات فنية متقدمة")

def main():
    """الدالة الرئيسية"""
    print_header()
    
    # فحص المتطلبات
    if not check_requirements():
        print("\n❌ فشل فحص المتطلبات. يرجى تثبيت المكتبات المطلوبة.")
        return
    
    # تشغيل اختبارات سريعة
    if not run_tests():
        print("\n⚠️ بعض الاختبارات فشلت، لكن يمكن المتابعة.")
    
    # القائمة الرئيسية
    while True:
        show_menu()
        try:
            choice = input("🎯 اختر رقم الخيار: ").strip()
            
            if choice == "0":
                print("\n👋 شكراً لاستخدام نظام بصيرة الثوري!")
                print("🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله")
                break
            elif choice == "1":
                launch_gradio()
            elif choice == "2":
                launch_cli()
            elif choice == "3":
                launch_artistic()
            elif choice == "4":
                run_comprehensive_tests()
            elif choice == "5":
                test_component("revolutionary_mother_equation.py", "المعادلة الأم الثورية")
            elif choice == "6":
                test_component("complete_multi_layer_thinking_core.py", "النواة التفكيرية")
            elif choice == "7":
                show_system_info()
            else:
                print("❌ خيار غير صحيح. يرجى اختيار رقم من 0 إلى 7")
                
        except KeyboardInterrupt:
            print("\n\n⚠️ تم إيقاف التشغيل بواسطة المستخدم")
            break
        except Exception as e:
            print(f"❌ خطأ: {e}")

if __name__ == "__main__":
    main()
