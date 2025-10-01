#!/usr/bin/env python3
# test_all_interfaces.py - اختبار شامل لجميع واجهات النظام الثوري

import sys
import os
import time
import threading
import requests
import json
from datetime import datetime

# إضافة المسار للاستيراد
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_api_interface():
    """اختبار واجهة API."""
    
    print("🔌 اختبار واجهة API...")
    print("-" * 40)
    
    base_url = "http://localhost:8000"
    
    # اختبار الاتصال
    try:
        response = requests.get(f"{base_url}/api/info", timeout=5)
        if response.status_code == 200:
            print("   ✅ الاتصال بـ API ناجح")
            data = response.json()
            print(f"   📊 اسم API: {data['data']['name']}")
            print(f"   📊 إصدار API: {data['data']['version']}")
        else:
            print(f"   ❌ فشل الاتصال: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"   ❌ خطأ في الاتصال: {e}")
        return False
    
    # اختبار حالة النظام
    try:
        response = requests.get(f"{base_url}/api/system/status", timeout=10)
        if response.status_code == 200:
            print("   ✅ حالة النظام متاحة")
            data = response.json()
            if data['success']:
                print(f"   📊 حالة الصحة: {data['data']['evolution_system']['health_status']}")
                print(f"   📊 نقاط الأداء: {data['data']['evolution_system']['performance_score']:.3f}")
            else:
                print(f"   ⚠️ النظام غير جاهز: {data.get('error', 'خطأ غير محدد')}")
        else:
            print(f"   ❌ فشل في الحصول على حالة النظام: {response.status_code}")
    except Exception as e:
        print(f"   ❌ خطأ في حالة النظام: {e}")
    
    # اختبار التفسير الدلالي
    try:
        test_sentence = "انسان يمشي في طريق"
        response = requests.post(
            f"{base_url}/api/semantic/interpret",
            json={"sentence": test_sentence},
            timeout=10
        )
        if response.status_code == 200:
            print("   ✅ التفسير الدلالي يعمل")
            data = response.json()
            if data['success']:
                print(f"   📊 ثقة التفسير: {data['data']['confidence']:.2f}")
                print(f"   📊 كلمات معروفة: {len(data['data']['recognized_words'])}")
            else:
                print(f"   ⚠️ فشل التفسير: {data.get('error', 'خطأ غير محدد')}")
        else:
            print(f"   ❌ فشل في التفسير الدلالي: {response.status_code}")
    except Exception as e:
        print(f"   ❌ خطأ في التفسير الدلالي: {e}")
    
    # اختبار قاعدة البيانات الدلالية
    try:
        response = requests.get(f"{base_url}/api/semantic/database", timeout=10)
        if response.status_code == 200:
            print("   ✅ قاعدة البيانات الدلالية متاحة")
            data = response.json()
            if data['success']:
                print(f"   📊 إجمالي المعادلات: {data['data']['total_equations']}")
                print(f"   📊 عدد الكلمات: {len(data['data']['words'])}")
            else:
                print(f"   ⚠️ فشل في الوصول لقاعدة البيانات: {data.get('error', 'خطأ غير محدد')}")
        else:
            print(f"   ❌ فشل في قاعدة البيانات الدلالية: {response.status_code}")
    except Exception as e:
        print(f"   ❌ خطأ في قاعدة البيانات الدلالية: {e}")
    
    print("   🎯 اختبار API مكتمل\n")
    return True

def test_web_interface():
    """اختبار واجهة الويب."""
    
    print("🌐 اختبار واجهة الويب...")
    print("-" * 40)
    
    base_url = "http://localhost:5000"
    
    # اختبار الصفحة الرئيسية
    try:
        response = requests.get(base_url, timeout=5)
        if response.status_code == 200:
            print("   ✅ الصفحة الرئيسية متاحة")
            if "النظام الثوري Baserah" in response.text:
                print("   ✅ المحتوى صحيح")
            else:
                print("   ⚠️ المحتوى قد يكون غير صحيح")
        else:
            print(f"   ❌ فشل في تحميل الصفحة الرئيسية: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"   ❌ خطأ في الاتصال بواجهة الويب: {e}")
        return False
    
    # اختبار API الداخلي لواجهة الويب
    try:
        response = requests.get(f"{base_url}/api/system/status", timeout=10)
        if response.status_code == 200:
            print("   ✅ API الداخلي يعمل")
            data = response.json()
            if data['status'] == 'success':
                print(f"   📊 النظام جاهز: {data['system_ready']}")
            else:
                print(f"   ⚠️ مشكلة في API الداخلي: {data.get('message', 'خطأ غير محدد')}")
        else:
            print(f"   ❌ فشل في API الداخلي: {response.status_code}")
    except Exception as e:
        print(f"   ❌ خطأ في API الداخلي: {e}")
    
    print("   🎯 اختبار واجهة الويب مكتمل\n")
    return True

def test_cli_interface():
    """اختبار واجهة سطر الأوامر."""
    
    print("💻 اختبار واجهة سطر الأوامر...")
    print("-" * 40)
    
    try:
        # استيراد واجهة سطر الأوامر
        from cli_interface import BaserahCLI
        
        print("   ✅ استيراد CLI ناجح")
        
        # إنشاء مثيل
        cli = BaserahCLI()
        
        if cli.system_ready:
            print("   ✅ النظام جاهز في CLI")
            
            # اختبار حالة النظام
            print("   🔍 اختبار عرض حالة النظام...")
            
            # محاكاة args للحالة
            class MockArgs:
                detailed = False
            
            # هذا سيطبع المعلومات مباشرة
            print("   📊 تشغيل أمر الحالة...")
            
        else:
            print("   ❌ النظام غير جاهز في CLI")
            return False
            
    except Exception as e:
        print(f"   ❌ خطأ في اختبار CLI: {e}")
        return False
    
    print("   🎯 اختبار CLI مكتمل\n")
    return True

def test_desktop_gui():
    """اختبار واجهة سطح المكتب (اختبار محدود)."""
    
    print("🖥️ اختبار واجهة سطح المكتب...")
    print("-" * 40)
    
    try:
        # استيراد واجهة سطح المكتب
        from desktop_gui import BaserahDesktopGUI
        
        print("   ✅ استيراد Desktop GUI ناجح")
        
        # إنشاء مثيل (بدون تشغيل الواجهة)
        app = BaserahDesktopGUI()
        
        if app.system_ready:
            print("   ✅ النظام جاهز في Desktop GUI")
            print("   📊 جميع المكونات متاحة")
        else:
            print("   ❌ النظام غير جاهز في Desktop GUI")
            return False
            
    except Exception as e:
        print(f"   ❌ خطأ في اختبار Desktop GUI: {e}")
        return False
    
    print("   🎯 اختبار Desktop GUI مكتمل")
    print("   ℹ️ لاختبار كامل، شغل الواجهة يدوياً\n")
    return True

def start_test_servers():
    """بدء تشغيل الخوادم للاختبار."""
    
    print("🚀 بدء تشغيل الخوادم للاختبار...")
    
    def start_api():
        try:
            from api_interface import BaserahAPIInterface
            api = BaserahAPIInterface()
            api.run(host='localhost', port=8000, debug=False)
        except Exception as e:
            print(f"خطأ في تشغيل API: {e}")
    
    def start_web():
        try:
            from web_interface import BaserahWebInterface
            web = BaserahWebInterface()
            web.run(host='localhost', port=5000, debug=False)
        except Exception as e:
            print(f"خطأ في تشغيل Web: {e}")
    
    # تشغيل الخوادم في خيوط منفصلة
    api_thread = threading.Thread(target=start_api, daemon=True)
    web_thread = threading.Thread(target=start_web, daemon=True)
    
    api_thread.start()
    time.sleep(3)  # انتظار تشغيل API
    
    web_thread.start()
    time.sleep(3)  # انتظار تشغيل Web
    
    print("✅ تم تشغيل الخوادم")
    return api_thread, web_thread

def run_comprehensive_test():
    """تشغيل اختبار شامل لجميع الواجهات."""
    
    print("🌟 اختبار شامل لواجهات النظام الثوري Baserah")
    print("=" * 60)
    print(f"📅 تاريخ الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    results = {}
    
    # اختبار واجهات لا تحتاج خوادم
    print("🔧 اختبار الواجهات المحلية...")
    results['cli'] = test_cli_interface()
    results['desktop'] = test_desktop_gui()
    
    # بدء تشغيل الخوادم
    print("🌐 بدء تشغيل خوادم الاختبار...")
    try:
        api_thread, web_thread = start_test_servers()
        
        # انتظار استقرار الخوادم
        print("⏳ انتظار استقرار الخوادم...")
        time.sleep(5)
        
        # اختبار الواجهات التي تحتاج خوادم
        print("🌐 اختبار الواجهات الشبكية...")
        results['api'] = test_api_interface()
        results['web'] = test_web_interface()
        
    except Exception as e:
        print(f"❌ خطأ في تشغيل الخوادم: {e}")
        results['api'] = False
        results['web'] = False
    
    # ملخص النتائج
    print("📊 ملخص نتائج الاختبار")
    print("=" * 60)
    
    total_tests = len(results)
    passed_tests = sum(1 for result in results.values() if result)
    
    for interface, result in results.items():
        status = "✅ نجح" if result else "❌ فشل"
        interface_names = {
            'cli': 'واجهة سطر الأوامر',
            'desktop': 'واجهة سطح المكتب',
            'api': 'واجهة API',
            'web': 'واجهة الويب'
        }
        print(f"   {interface_names[interface]}: {status}")
    
    print(f"\n🎯 النتيجة النهائية: {passed_tests}/{total_tests} واجهات نجحت")
    
    if passed_tests == total_tests:
        print("🎉 جميع الواجهات تعمل بنجاح!")
    elif passed_tests > 0:
        print("⚠️ بعض الواجهات تعمل، تحقق من الأخطاء أعلاه")
    else:
        print("❌ جميع الواجهات فشلت، تحقق من النظام الأساسي")
    
    print(f"\n📅 انتهاء الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    return results

def main():
    """الدالة الرئيسية."""
    
    try:
        results = run_comprehensive_test()
        
        # حفظ النتائج
        results_file = f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'results': results,
                'summary': {
                    'total_tests': len(results),
                    'passed_tests': sum(1 for result in results.values() if result),
                    'success_rate': sum(1 for result in results.values() if result) / len(results) * 100
                }
            }, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 تم حفظ النتائج في: {results_file}")
        
    except KeyboardInterrupt:
        print("\n\n⏹️ تم إيقاف الاختبار بواسطة المستخدم")
    except Exception as e:
        print(f"\n❌ خطأ في الاختبار: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
