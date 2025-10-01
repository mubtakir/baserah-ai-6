#!/usr/bin/env python3
"""
main.py - نقطة الدخول الرئيسية لنظام بصيرة الثوري
Main Entry Point for Basera Revolutionary AI System

🌟 نقطة دخول موحدة للنظام
🚀 تشغيل مباشر وسهل
🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله

المطور: باسل يحيى عبدالله
"""

import os
import sys
import argparse
from datetime import datetime

def print_banner():
    """طباعة شعار النظام"""
    banner = """
╔══════════════════════════════════════════════════════════════════════╗
║                    🌟 نظام بصيرة الثوري 🌟                        ║
║                  Revolutionary Basera AI System                     ║
║                                                                      ║
║        🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله        ║
║                                                                      ║
║  🧮 رياضيات نقية | 🧬 نظريات ثورية | 🖥️ واجهات متعددة | 🎨 إبداع  ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(banner)
    print(f"📅 التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

def check_python_version():
    """فحص إصدار Python"""
    if sys.version_info < (3, 8):
        print("❌ خطأ: يتطلب Python 3.8 أو أحدث")
        print(f"   الإصدار الحالي: {sys.version}")
        print("   يرجى تحديث Python من: https://python.org/downloads/")
        sys.exit(1)
    else:
        print(f"✅ Python {sys.version.split()[0]} - متوافق")

def check_requirements():
    """فحص المتطلبات الأساسية"""
    print("\n🔍 فحص المتطلبات...")
    
    required_modules = [
        ('numpy', 'الحسابات الرياضية'),
        ('matplotlib', 'الرسوم البيانية'),
        ('gradio', 'الواجهة التفاعلية')
    ]
    
    missing = []
    for module, description in required_modules:
        try:
            __import__(module)
            print(f"✅ {module} - {description}")
        except ImportError:
            print(f"❌ {module} - غير مثبت ({description})")
            missing.append(module)
    
    if missing:
        print(f"\n⚠️ مكتبات مفقودة: {', '.join(missing)}")
        print("💡 لتثبيتها:")
        print("   pip install -r requirements.txt")
        print("   أو: pip install " + " ".join(missing))
        
        choice = input("\n❓ هل تريد المتابعة بدون هذه المكتبات؟ (y/n): ").lower()
        if choice != 'y':
            print("👋 تم إيقاف التشغيل. يرجى تثبيت المتطلبات أولاً.")
            sys.exit(1)
    
    return len(missing) == 0

def show_main_menu():
    """عرض القائمة الرئيسية"""
    print("\n🚀 اختر طريقة التشغيل:")
    print("   1️⃣  واجهة Gradio التفاعلية (الأسهل - موصى به)")
    print("   2️⃣  واجهة سطر الأوامر CLI (للمتقدمين)")
    print("   3️⃣  الواجهة الفنية (للإبداع والتصميم)")
    print("   4️⃣  واجهة API (للمطورين)")
    print("   5️⃣  المُشغل المتقدم (جميع الخيارات)")
    print("   6️⃣  تشغيل الاختبارات الشاملة")
    print("   0️⃣  الخروج")
    print("-" * 50)

def launch_interface(choice):
    """تشغيل الواجهة المختارة"""
    import subprocess
    
    interfaces = {
        '1': {
            'name': 'واجهة Gradio التفاعلية',
            'command': [sys.executable, 'multi_user_interfaces.py', '--interface', 'gradio'],
            'info': 'ستفتح على: http://127.0.0.1:7860'
        },
        '2': {
            'name': 'واجهة سطر الأوامر',
            'command': [sys.executable, 'multi_user_interfaces.py', '--interface', 'cli'],
            'info': 'استخدم أمر "help" للمساعدة'
        },
        '3': {
            'name': 'الواجهة الفنية',
            'command': [sys.executable, 'artistic_inference_interface.py'],
            'info': 'للإبداع الفني واستنباط المعادلات'
        },
        '4': {
            'name': 'واجهة API',
            'command': [sys.executable, 'multi_user_interfaces.py', '--interface', 'api'],
            'info': 'التوثيق على: http://127.0.0.1:8000/docs'
        },
        '5': {
            'name': 'المُشغل المتقدم',
            'command': [sys.executable, 'basera_launcher.py'],
            'info': 'جميع الخيارات والإعدادات المتقدمة'
        },
        '6': {
            'name': 'الاختبارات الشاملة',
            'command': [sys.executable, 'comprehensive_testing_system.py'],
            'info': 'فحص شامل لجميع مكونات النظام'
        }
    }
    
    if choice in interfaces:
        interface = interfaces[choice]
        print(f"\n🚀 تشغيل {interface['name']}...")
        print(f"💡 {interface['info']}")
        print("⏳ جاري التحميل...")
        
        try:
            # التحقق من وجود الملف
            script_file = interface['command'][1]
            script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), script_file)
            if not os.path.exists(script_path):
                print(f"❌ الملف غير موجود: {script_file}")
                print(f"   المسار المتوقع: {script_path}")
                return False

            # تشغيل الواجهة
            subprocess.run(interface['command'], cwd=os.path.dirname(os.path.abspath(__file__)))
            return True
            
        except KeyboardInterrupt:
            print(f"\n⚠️ تم إيقاف {interface['name']} بواسطة المستخدم")
            return True
        except FileNotFoundError as e:
            print(f"❌ خطأ: ملف غير موجود - {e}")
            return False
        except Exception as e:
            print(f"❌ خطأ في تشغيل {interface['name']}: {e}")
            return False
    else:
        print("❌ خيار غير صحيح")
        return False

def quick_start():
    """تشغيل سريع مباشر لواجهة Gradio"""
    print("🚀 تشغيل سريع - واجهة Gradio التفاعلية...")
    return launch_interface('1')

def parse_arguments():
    """تحليل معاملات سطر الأوامر"""
    parser = argparse.ArgumentParser(
        description='نظام بصيرة الثوري - نقطة الدخول الرئيسية',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
أمثلة الاستخدام:
  python main.py                    # القائمة التفاعلية
  python main.py --quick            # تشغيل سريع لواجهة Gradio
  python main.py --interface gradio # تشغيل واجهة محددة
  python main.py --test             # تشغيل الاختبارات
  python main.py --help             # عرض هذه المساعدة

الواجهات المتاحة:
  gradio    - واجهة تفاعلية رسومية (الأسهل)
  cli       - واجهة سطر الأوامر (للمتقدمين)
  artistic  - واجهة فنية (للإبداع)
  api       - واجهة API (للمطورين)
  launcher  - المُشغل المتقدم (جميع الخيارات)
        """
    )
    
    parser.add_argument(
        '--quick', '-q',
        action='store_true',
        help='تشغيل سريع لواجهة Gradio التفاعلية'
    )
    
    parser.add_argument(
        '--interface', '-i',
        choices=['gradio', 'cli', 'artistic', 'api', 'launcher'],
        help='تشغيل واجهة محددة مباشرة'
    )
    
    parser.add_argument(
        '--test', '-t',
        action='store_true',
        help='تشغيل الاختبارات الشاملة'
    )
    
    parser.add_argument(
        '--no-check',
        action='store_true',
        help='تخطي فحص المتطلبات (للخبراء فقط)'
    )
    
    return parser.parse_args()

def main():
    """الدالة الرئيسية"""
    # تحليل المعاملات
    args = parse_arguments()

    # طباعة الشعار
    print_banner()

    # فحص إصدار Python
    check_python_version()

    # فحص المتطلبات (إلا إذا تم تخطيها)
    if not args.no_check:
        requirements_ok = check_requirements()
        if not requirements_ok:
            print("⚠️ بعض المكتبات مفقودة، قد تواجه مشاكل في التشغيل")
    
    try:
        # التشغيل حسب المعاملات
        if args.quick:
            # تشغيل سريع
            return quick_start()

        elif args.interface:
            # تشغيل واجهة محددة
            interface_map = {
                'gradio': '1',
                'cli': '2',
                'artistic': '3',
                'api': '4',
                'launcher': '5'
            }
            if args.interface in interface_map:
                return launch_interface(interface_map[args.interface])
            else:
                print(f"❌ واجهة غير معروفة: {args.interface}")
                print("الواجهات المتاحة: gradio, cli, artistic, api, launcher")
                return False

        elif args.test:
            # تشغيل الاختبارات
            return launch_interface('6')

        else:
            # القائمة التفاعلية
            while True:
                show_main_menu()
                choice = input("🎯 اختر رقم الخيار: ").strip()

                if choice == '0':
                    print("\n👋 شكراً لاستخدام نظام بصيرة الثوري!")
                    print("🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله")
                    break
                elif choice in ['1', '2', '3', '4', '5', '6']:
                    success = launch_interface(choice)
                    if not success:
                        print("\n⚠️ فشل في تشغيل الواجهة. يرجى المحاولة مرة أخرى.")
                    print("\n" + "="*50)
                else:
                    print("❌ خيار غير صحيح. يرجى اختيار رقم من 0 إلى 6")
                    
    except KeyboardInterrupt:
        print("\n\n⚠️ تم إيقاف التشغيل بواسطة المستخدم")
    except Exception as e:
        print(f"\n❌ خطأ عام: {e}")
        print("💡 تأكد من وجود جميع ملفات النظام في نفس المجلد")

if __name__ == "__main__":
    main()
