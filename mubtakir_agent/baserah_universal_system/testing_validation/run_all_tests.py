#!/usr/bin/env python3
# run_all_tests.py - تشغيل جميع اختبارات النظام الثوري
#
# 👨‍💻 المطور: باسل يحيى عبدالله
# 🧠 الأفكار الابتكارية: جميع الأفكار والنظريات الثورية من إبداع باسل يحيى عبدالله
# 🤖 التطوير: أكواد بدائية تم تطويرها بمساعدة وكيل ذكاء اصطناعي
# 📅 تاريخ الإنشاء: 2025
# 🧪 الاختبارات: تشغيل شامل لجميع اختبارات النظام الثوري
# 🌟 النظام: Baserah Universal System - تأكيد نهائي شامل

import sys
import os
import subprocess
import time
from datetime import datetime
from pathlib import Path

def print_header():
    """طباعة رأس التقرير."""
    print("🌟" * 40)
    print("🌟 النظام الثوري Baserah - اختبارات شاملة نهائية 🌟")
    print("🌟" * 40)
    print()
    print("👨‍💻 المطور: باسل يحيى عبدالله")
    print("🧠 الأفكار الابتكارية: جميع الأفكار والنظريات الثورية من إبداع باسل يحيى عبدالله")
    print("🤖 التطوير: أكواد بدائية تم تطويرها بمساعدة وكيل ذكاء اصطناعي")
    print("📅 تاريخ الإنشاء: 2025")
    print("🌟 النظام: Baserah Universal System - نظام ثوري نقي")
    print()
    print("🧬 النظريات الثورية:")
    print("   • نظرية ثنائية الصفر (Zero Duality Theory)")
    print("   • نظرية تعامد الأضداد (Perpendicular Opposites Theory)")
    print("   • نظرية الفتائل (Filament Theory)")
    print()
    print("🎯 المنهجية: sigmoid + linear فقط، بدون AI تقليدي")
    print("=" * 80)

def run_test_file(test_file_path, test_name):
    """تشغيل ملف اختبار واحد."""
    print(f"\n🧪 تشغيل {test_name}...")
    print("-" * 60)
    
    start_time = time.time()
    
    try:
        # تشغيل الاختبار
        result = subprocess.run([
            sys.executable, test_file_path
        ], capture_output=True, text=True, timeout=300)
        
        end_time = time.time()
        duration = end_time - start_time
        
        # طباعة النتائج
        if result.returncode == 0:
            print(f"✅ {test_name}: نجح")
            print(f"⏱️ المدة: {duration:.2f} ثانية")
            
            # طباعة ملخص النتائج
            output_lines = result.stdout.split('\n')
            for line in output_lines:
                if 'معدل النجاح:' in line or 'معدل نجاح' in line:
                    print(f"📊 {line.strip()}")
                elif 'إجمالي الاختبارات:' in line:
                    print(f"🧪 {line.strip()}")
                elif 'نجح:' in line and 'فشل:' in line:
                    print(f"📈 {line.strip()}")
            
            return True, duration, result.stdout
        else:
            print(f"❌ {test_name}: فشل")
            print(f"⏱️ المدة: {duration:.2f} ثانية")
            print(f"🚨 رمز الخطأ: {result.returncode}")
            
            # طباعة أخطاء مختصرة
            if result.stderr:
                error_lines = result.stderr.split('\n')[:5]  # أول 5 أسطر فقط
                for line in error_lines:
                    if line.strip():
                        print(f"   ❌ {line.strip()}")
            
            return False, duration, result.stderr
            
    except subprocess.TimeoutExpired:
        print(f"⏰ {test_name}: انتهت المهلة الزمنية (5 دقائق)")
        return False, 300, "انتهت المهلة الزمنية"
    except Exception as e:
        print(f"🚨 {test_name}: خطأ في التشغيل - {e}")
        return False, 0, str(e)

def check_system_structure():
    """فحص هيكل النظام."""
    print("\n📁 فحص هيكل النظام...")
    print("-" * 60)
    
    base_path = Path(__file__).parent.parent
    
    # المجلدات المطلوبة
    required_directories = [
        'revolutionary_intelligence',
        'user_interfaces', 
        'artistic_unit',
        'artistic_intelligence',
        'knowledge_systems',
        'testing_validation',
        'utilities_tools',
        'documentation'
    ]
    
    # الملفات المطلوبة
    required_files = [
        'README.md',
        '__init__.py',
        'ai_oop_system.py',
        'advanced_cognitive_objects.py'
    ]
    
    structure_ok = True
    
    print("📂 فحص المجلدات:")
    for directory in required_directories:
        dir_path = base_path / directory
        if dir_path.exists() and dir_path.is_dir():
            print(f"   ✅ {directory}")
        else:
            print(f"   ❌ {directory} - غير موجود")
            structure_ok = False
    
    print("\n📄 فحص الملفات:")
    for file_name in required_files:
        file_path = base_path / file_name
        if file_path.exists() and file_path.is_file():
            print(f"   ✅ {file_name}")
        else:
            print(f"   ❌ {file_name} - غير موجود")
            structure_ok = False
    
    # فحص الملفات المهمة للمطور
    print("\n👨‍💻 فحص معلومات المطور:")
    developer_files = [
        'ai_oop_system.py',
        'revolutionary_intelligence/quranic_analysis_engine.py',
        'revolutionary_intelligence/arabic_lexicon_engine.py',
        'revolutionary_intelligence/revolutionary_mother_equation.py',
        'user_interfaces/web_interface.py'
    ]
    
    for file_name in developer_files:
        file_path = base_path / file_name
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if 'باسل يحيى عبدالله' in content:
                        print(f"   ✅ {file_name} - يحتوي على معلومات المطور")
                    else:
                        print(f"   ⚠️ {file_name} - لا يحتوي على معلومات المطور")
            except Exception as e:
                print(f"   ❌ {file_name} - خطأ في القراءة: {e}")
        else:
            print(f"   ❌ {file_name} - غير موجود")
    
    return structure_ok

def generate_final_report(test_results, total_duration):
    """إنشاء التقرير النهائي."""
    print("\n" + "🎯" * 40)
    print("🎯 التقرير النهائي الشامل 🎯")
    print("🎯" * 40)
    
    total_tests = len(test_results)
    successful_tests = sum(1 for result in test_results if result['success'])
    failed_tests = total_tests - successful_tests
    
    print(f"\n📊 إحصائيات الاختبارات:")
    print(f"   🧪 إجمالي مجموعات الاختبارات: {total_tests}")
    print(f"   ✅ نجح: {successful_tests}")
    print(f"   ❌ فشل: {failed_tests}")
    print(f"   ⏱️ إجمالي الوقت: {total_duration:.2f} ثانية")
    
    success_rate = (successful_tests / total_tests * 100) if total_tests > 0 else 0
    print(f"   🎯 معدل النجاح الإجمالي: {success_rate:.1f}%")
    
    print(f"\n📋 تفاصيل النتائج:")
    for result in test_results:
        status = "✅" if result['success'] else "❌"
        print(f"   {status} {result['name']}: {result['duration']:.2f}s")
    
    print(f"\n🌟 تقييم النظام:")
    if success_rate >= 90:
        print("   🎉 ممتاز! النظام جاهز للإنتاج")
        system_status = "ممتاز"
    elif success_rate >= 80:
        print("   ✅ جيد جداً! النظام يعمل بكفاءة عالية")
        system_status = "جيد جداً"
    elif success_rate >= 70:
        print("   👍 جيد! النظام يعمل مع بعض التحسينات المطلوبة")
        system_status = "جيد"
    elif success_rate >= 50:
        print("   ⚠️ مقبول! النظام يحتاج تحسينات")
        system_status = "مقبول"
    else:
        print("   🚨 ضعيف! النظام يحتاج مراجعة شاملة")
        system_status = "يحتاج مراجعة"
    
    # حفظ التقرير في ملف
    report_content = f"""# تقرير الاختبارات النهائي - النظام الثوري Baserah

## معلومات المطور
- **المطور**: باسل يحيى عبدالله
- **الأفكار الابتكارية**: جميع الأفكار والنظريات الثورية من إبداع باسل يحيى عبدالله
- **التطوير**: أكواد بدائية تم تطويرها بمساعدة وكيل ذكاء اصطناعي
- **تاريخ الاختبار**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## النظريات الثورية المطبقة
- نظرية ثنائية الصفر (Zero Duality Theory)
- نظرية تعامد الأضداد (Perpendicular Opposites Theory)  
- نظرية الفتائل (Filament Theory)

## نتائج الاختبارات
- **إجمالي مجموعات الاختبارات**: {total_tests}
- **نجح**: {successful_tests}
- **فشل**: {failed_tests}
- **معدل النجاح**: {success_rate:.1f}%
- **إجمالي الوقت**: {total_duration:.2f} ثانية
- **تقييم النظام**: {system_status}

## تفاصيل النتائج
"""
    
    for result in test_results:
        status = "✅ نجح" if result['success'] else "❌ فشل"
        report_content += f"- **{result['name']}**: {status} ({result['duration']:.2f}s)\n"
    
    report_content += f"""
## الخلاصة
النظام الثوري Baserah تم اختباره بشكل شامل ومعدل النجاح {success_rate:.1f}%.
النظام يطبق منهجية ثورية نقية باستخدام sigmoid + linear فقط، بدون AI تقليدي.

---
*تم إنشاء هذا التقرير تلقائياً بواسطة النظام الثوري Baserah*
"""
    
    # حفظ التقرير
    report_path = Path(__file__).parent / f"final_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        print(f"\n📄 تم حفظ التقرير في: {report_path}")
    except Exception as e:
        print(f"\n❌ فشل حفظ التقرير: {e}")
    
    return success_rate >= 70

def main():
    """الدالة الرئيسية لتشغيل جميع الاختبارات."""
    
    # طباعة الرأس
    print_header()
    
    # فحص هيكل النظام
    structure_ok = check_system_structure()
    if not structure_ok:
        print("\n🚨 تحذير: هيكل النظام غير مكتمل!")
    
    # قائمة الاختبارات
    test_files = [
        {
            'path': Path(__file__).parent / 'comprehensive_system_tests.py',
            'name': 'الاختبارات الشاملة للنظام'
        },
        {
            'path': Path(__file__).parent / 'interface_integration_tests.py', 
            'name': 'اختبارات تكامل الواجهات'
        }
    ]
    
    # تشغيل الاختبارات
    test_results = []
    total_start_time = time.time()
    
    for test_info in test_files:
        if test_info['path'].exists():
            success, duration, output = run_test_file(test_info['path'], test_info['name'])
            test_results.append({
                'name': test_info['name'],
                'success': success,
                'duration': duration,
                'output': output
            })
        else:
            print(f"\n⚠️ ملف الاختبار غير موجود: {test_info['path']}")
            test_results.append({
                'name': test_info['name'],
                'success': False,
                'duration': 0,
                'output': 'ملف غير موجود'
            })
    
    total_duration = time.time() - total_start_time
    
    # إنشاء التقرير النهائي
    overall_success = generate_final_report(test_results, total_duration)
    
    # النتيجة النهائية
    if overall_success:
        print("\n🎉 تهانينا! النظام الثوري Baserah اجتاز الاختبارات بنجاح!")
        print("🚀 النظام جاهز للاستخدام والتطوير المستقبلي!")
        return 0
    else:
        print("\n⚠️ النظام يحتاج بعض التحسينات قبل الإنتاج")
        print("🔧 يرجى مراجعة الأخطاء وإعادة تشغيل الاختبارات")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
