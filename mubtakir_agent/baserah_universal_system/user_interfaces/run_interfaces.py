#!/usr/bin/env python3
# run_interfaces.py - تشغيل جميع واجهات النظام الثوري Baserah

import argparse
import sys
import os
import threading
import time
from datetime import datetime

# إضافة المسار للاستيراد
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def run_desktop_gui():
    """تشغيل واجهة سطح المكتب."""
    try:
        from desktop_gui import BaserahDesktopGUI
        print("🖥️ تشغيل واجهة سطح المكتب...")
        app = BaserahDesktopGUI()
        app.run()
    except Exception as e:
        print(f"❌ خطأ في تشغيل واجهة سطح المكتب: {e}")

def run_web_interface():
    """تشغيل واجهة الويب."""
    try:
        from web_interface import BaserahWebInterface
        print("🌐 تشغيل واجهة الويب...")
        web_interface = BaserahWebInterface()
        web_interface.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        print(f"❌ خطأ في تشغيل واجهة الويب: {e}")

def run_api_interface():
    """تشغيل واجهة API."""
    try:
        from api_interface import BaserahAPIInterface
        print("🔌 تشغيل واجهة API...")
        api_interface = BaserahAPIInterface()
        api_interface.run(host='0.0.0.0', port=8000, debug=False)
    except Exception as e:
        print(f"❌ خطأ في تشغيل واجهة API: {e}")

def run_cli_interface():
    """تشغيل واجهة سطر الأوامر."""
    try:
        from cli_interface import BaserahCLI
        print("💻 تشغيل واجهة سطر الأوامر...")
        cli = BaserahCLI()
        cli.run_interactive()
    except Exception as e:
        print(f"❌ خطأ في تشغيل واجهة سطر الأوامر: {e}")

def run_all_interfaces():
    """تشغيل جميع الواجهات في خيوط منفصلة."""
    
    print("🚀 تشغيل جميع واجهات النظام الثوري Baserah")
    print("=" * 60)
    
    # إنشاء خيوط للواجهات
    threads = []
    
    # واجهة API (أولاً)
    api_thread = threading.Thread(target=run_api_interface, name="API-Thread")
    api_thread.daemon = True
    threads.append(("API", api_thread))
    
    # واجهة الويب
    web_thread = threading.Thread(target=run_web_interface, name="Web-Thread")
    web_thread.daemon = True
    threads.append(("Web", web_thread))
    
    # بدء تشغيل الخيوط
    for name, thread in threads:
        print(f"🔄 بدء تشغيل {name}...")
        thread.start()
        time.sleep(2)  # انتظار قصير بين كل واجهة
    
    print("\n✅ تم تشغيل الواجهات التالية:")
    print("   🔌 API: http://localhost:8000")
    print("   🌐 Web: http://localhost:5000")
    
    print("\n📚 الواجهات المتاحة:")
    print("   🖥️  Desktop GUI: python desktop_gui.py")
    print("   💻 CLI: python cli_interface.py interactive")
    
    print("\n⚠️  للخروج اضغط Ctrl+C")
    
    try:
        # انتظار إنهاء الخيوط
        while True:
            time.sleep(1)
            # فحص حالة الخيوط
            active_threads = [name for name, thread in threads if thread.is_alive()]
            if not active_threads:
                print("⚠️ جميع الخيوط توقفت")
                break
    except KeyboardInterrupt:
        print("\n\n⏹️ إيقاف جميع الواجهات...")
        print("👋 وداعاً!")

def show_interface_info():
    """عرض معلومات الواجهات المتاحة."""
    
    print("🌟 واجهات النظام الثوري Baserah")
    print("=" * 50)
    
    interfaces = [
        {
            'name': 'واجهة سطح المكتب (Desktop GUI)',
            'description': 'واجهة رسومية تفاعلية باستخدام Tkinter',
            'command': 'python desktop_gui.py',
            'features': [
                'تفاعل مرئي مع جميع مكونات النظام',
                'رسوم بيانية وتصورات',
                'واجهة سهلة الاستخدام',
                'تحديث فوري للحالة'
            ]
        },
        {
            'name': 'واجهة الويب (Web Interface)',
            'description': 'واجهة ويب حديثة باستخدام Flask و Bootstrap',
            'command': 'python web_interface.py',
            'url': 'http://localhost:5000',
            'features': [
                'واجهة ويب متجاوبة',
                'تصميم عصري وجذاب',
                'إمكانية الوصول من أي متصفح',
                'تفاعل AJAX سريع'
            ]
        },
        {
            'name': 'واجهة API (REST API)',
            'description': 'واجهة API كاملة للتكامل مع التطبيقات الأخرى',
            'command': 'python api_interface.py',
            'url': 'http://localhost:8000',
            'features': [
                'API RESTful كامل',
                'استجابات JSON موحدة',
                'دعم CORS للمتصفحات',
                'سجل عمليات مفصل'
            ]
        },
        {
            'name': 'واجهة سطر الأوامر (CLI)',
            'description': 'واجهة سطر أوامر قوية للمطورين والمتقدمين',
            'command': 'python cli_interface.py --help',
            'features': [
                'أوامر شاملة لجميع المكونات',
                'وضع تفاعلي مباشر',
                'تصدير واستيراد البيانات',
                'مناسبة للأتمتة والسكريبت'
            ]
        }
    ]
    
    for i, interface in enumerate(interfaces, 1):
        print(f"\n{i}. {interface['name']}")
        print(f"   الوصف: {interface['description']}")
        print(f"   الأمر: {interface['command']}")
        
        if 'url' in interface:
            print(f"   الرابط: {interface['url']}")
        
        print("   المميزات:")
        for feature in interface['features']:
            print(f"     • {feature}")
    
    print(f"\n🎯 جميع الواجهات تتصل بنفس النظام الثوري الأساسي")
    print(f"📅 تاريخ الإنشاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """الدالة الرئيسية."""
    
    parser = argparse.ArgumentParser(
        description='🌟 تشغيل واجهات النظام الثوري Baserah',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
أمثلة الاستخدام:
  python run_interfaces.py --desktop          # تشغيل واجهة سطح المكتب
  python run_interfaces.py --web              # تشغيل واجهة الويب
  python run_interfaces.py --api              # تشغيل واجهة API
  python run_interfaces.py --cli              # تشغيل واجهة سطر الأوامر
  python run_interfaces.py --all              # تشغيل جميع الواجهات
  python run_interfaces.py --info             # عرض معلومات الواجهات
        """
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--desktop', action='store_true', help='تشغيل واجهة سطح المكتب')
    group.add_argument('--web', action='store_true', help='تشغيل واجهة الويب')
    group.add_argument('--api', action='store_true', help='تشغيل واجهة API')
    group.add_argument('--cli', action='store_true', help='تشغيل واجهة سطر الأوامر')
    group.add_argument('--all', action='store_true', help='تشغيل جميع الواجهات')
    group.add_argument('--info', action='store_true', help='عرض معلومات الواجهات')
    
    args = parser.parse_args()
    
    print(f"🌟 النظام الثوري Baserah - مشغل الواجهات")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    try:
        if args.desktop:
            run_desktop_gui()
        elif args.web:
            run_web_interface()
        elif args.api:
            run_api_interface()
        elif args.cli:
            run_cli_interface()
        elif args.all:
            run_all_interfaces()
        elif args.info:
            show_interface_info()
            
    except KeyboardInterrupt:
        print("\n\n⏹️ تم إيقاف التشغيل بواسطة المستخدم")
        print("👋 وداعاً!")
    except Exception as e:
        print(f"\n❌ خطأ في التشغيل: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
