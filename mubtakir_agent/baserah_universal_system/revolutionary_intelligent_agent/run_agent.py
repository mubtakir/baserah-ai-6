#!/usr/bin/env python3
# run_agent.py - تشغيل سريع للوكيل المساعد الذكي الثوري

import asyncio
import sys
import os
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# استيراد الوكيل الثوري
from revolutionary_intelligent_agent import (
    RevolutionaryIntelligentAgent,
    create_revolutionary_project,
    create_multiple_revolutionary_projects,
    get_revolutionary_agent_demo
)


def print_banner():
    """طباعة شعار الوكيل الثوري."""
    
    banner = """
🌟════════════════════════════════════════════════════════════════════🌟
🤖                   الوكيل المساعد الذكي الثوري                    🤖
🧬                مدعوم بنظريات باسل الثورية ونظام Baserah              🧬
🚀                يفهم الفكرة وينفذ المشروع كاملاً                   🚀
🌟════════════════════════════════════════════════════════════════════🌟
"""
    
    print(banner)
    print(f"📅 التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔥 النسخة: 1.0.0 - Revolutionary Intelligent Agent")
    print()


def print_menu():
    """طباعة قائمة الخيارات."""
    
    menu = """
🎯 اختر العملية المطلوبة:

1️⃣  إنشاء مشروع ثوري واحد
2️⃣  إنشاء عدة مشاريع ثورية
3️⃣  عرض الوكيل التجريبي
4️⃣  اختبار النظام
5️⃣  عرض معلومات النظام
6️⃣  أمثلة سريعة
0️⃣  خروج

"""
    print(menu)


async def create_single_project():
    """إنشاء مشروع ثوري واحد."""
    
    print("🏗️ إنشاء مشروع ثوري واحد")
    print("=" * 50)
    
    # الحصول على فكرة المشروع
    project_idea = input("💡 أدخل فكرة المشروع: ").strip()
    
    if not project_idea:
        print("❌ يجب إدخال فكرة المشروع!")
        return
    
    # خيارات إضافية
    print("\n🔧 خيارات إضافية (اختيارية):")
    project_type = input("📱 نوع المشروع (web/desktop/api/data_science): ").strip()
    features = input("🌟 الميزات المطلوبة (مفصولة بفواصل): ").strip()
    
    # إعداد المتطلبات
    requirements = {}
    if project_type:
        requirements['type'] = project_type
    if features:
        requirements['features'] = [f.strip() for f in features.split(',')]
    
    print(f"\n🚀 بدء إنشاء المشروع: {project_idea}")
    print("⏳ يرجى الانتظار...")
    
    try:
        # إنشاء المشروع
        result = await create_revolutionary_project(project_idea, requirements)
        
        # عرض النتائج
        print("\n📊 نتائج إنشاء المشروع:")
        print("=" * 50)
        
        if result.get('overall_success', False):
            print("✅ تم إنشاء المشروع بنجاح!")
            
            project_structure = result.get('project_structure', {})
            print(f"📁 ملفات منشأة: {project_structure.get('total_files', 0)}")
            print(f"📂 مجلدات منشأة: {project_structure.get('total_folders', 0)}")
            
            success_metrics = result.get('success_metrics', {})
            print(f"📈 معدل النجاح: {success_metrics.get('overall_success_rate', 0):.1%}")
            
            revolutionary_features = result.get('revolutionary_features', {})
            print(f"💡 رؤى ثورية: {revolutionary_features.get('total_revolutionary_insights', 0)}")
            
            basil_theories = revolutionary_features.get('basil_theories_applied', [])
            if basil_theories:
                print(f"🧬 نظريات باسل المطبقة: {', '.join(basil_theories)}")
            
            print(f"⏱️ وقت التنفيذ: {result.get('execution_time', 0):.2f} ثانية")
            
        else:
            print("❌ فشل في إنشاء المشروع")
            error_msg = result.get('error_message', 'خطأ غير محدد')
            print(f"🔍 السبب: {error_msg}")
        
    except Exception as e:
        print(f"💥 خطأ في إنشاء المشروع: {e}")


async def create_multiple_projects():
    """إنشاء عدة مشاريع ثورية."""
    
    print("🚀 إنشاء عدة مشاريع ثورية")
    print("=" * 50)
    
    # الحصول على قائمة المشاريع
    print("💡 أدخل أفكار المشاريع (اضغط Enter مرتين للانتهاء):")
    
    projects = []
    while True:
        project = input(f"المشروع {len(projects) + 1}: ").strip()
        if not project:
            break
        projects.append(project)
    
    if not projects:
        print("❌ يجب إدخال مشروع واحد على الأقل!")
        return
    
    print(f"\n🚀 بدء إنشاء {len(projects)} مشروع ثوري...")
    print("⏳ يرجى الانتظار...")
    
    try:
        # إنشاء المشاريع
        result = await create_multiple_revolutionary_projects(projects)
        
        # عرض النتائج
        print("\n📊 نتائج إنشاء المشاريع:")
        print("=" * 50)
        
        total_projects = result.get('total_projects', 0)
        successful_projects = result.get('successful_projects', 0)
        failed_projects = result.get('failed_projects', 0)
        
        print(f"📋 إجمالي المشاريع: {total_projects}")
        print(f"✅ مشاريع ناجحة: {successful_projects}")
        print(f"❌ مشاريع فاشلة: {failed_projects}")
        
        batch_stats = result.get('batch_statistics', {})
        success_rate = batch_stats.get('success_rate', 0)
        completion_time = batch_stats.get('completion_time', 0)
        
        print(f"📈 معدل النجاح: {success_rate:.1%}")
        print(f"⏱️ وقت الإنجاز: {completion_time:.2f} ثانية")
        
        # عرض تفاصيل المشاريع
        projects_results = result.get('projects_results', [])
        if projects_results:
            print("\n📋 تفاصيل المشاريع:")
            for i, project_result in enumerate(projects_results, 1):
                project_idea = project_result.get('project_info', {}).get('project_idea', f'مشروع {i}')
                success = project_result.get('overall_success', False)
                status = "✅ نجح" if success else "❌ فشل"
                print(f"  {i}. {project_idea}: {status}")
        
    except Exception as e:
        print(f"💥 خطأ في إنشاء المشاريع: {e}")


def show_demo_agent():
    """عرض الوكيل التجريبي."""
    
    print("🎭 عرض الوكيل التجريبي")
    print("=" * 50)
    
    try:
        # إنشاء وكيل تجريبي
        demo_agent = get_revolutionary_agent_demo()
        
        # عرض حالة الوكيل
        status = demo_agent.get_agent_status()
        
        print(f"🤖 اسم الوكيل: {status['agent_info']['name']}")
        print(f"📦 الإصدار: {status['agent_info']['version']}")
        print(f"🏆 تقييم الأداء: {status['performance_assessment']}")
        
        print("\n🛠️ القدرات المتاحة:")
        capabilities = status['capabilities']
        for capability, enabled in capabilities.items():
            if enabled:
                print(f"  ✅ {capability}")
        
        print("\n🌟 الميزات الثورية:")
        revolutionary_features = status['revolutionary_features']
        for feature, enabled in revolutionary_features.items():
            if enabled:
                print(f"  🔥 {feature}")
        
        print("\n📊 الإحصائيات:")
        stats = status['statistics']
        print(f"  📁 مشاريع منشأة: {stats['projects_created']}")
        print(f"  📄 ملفات مولدة: {stats['total_files_generated']}")
        print(f"  💡 رؤى ثورية: {stats['revolutionary_insights_generated']}")
        print(f"  🧬 تطبيقات نظريات باسل: {stats['basil_theories_applications']}")
        
    except Exception as e:
        print(f"💥 خطأ في عرض الوكيل التجريبي: {e}")


async def run_tests():
    """تشغيل اختبارات النظام."""
    
    print("🧪 تشغيل اختبارات النظام")
    print("=" * 50)
    
    try:
        # استيراد واختبار الوحدات
        print("📦 اختبار استيراد الوحدات...")
        
        from revolutionary_intelligent_agent import (
            RevolutionaryIntelligentAgent,
            RevolutionaryAgentCore,
            BaserahContentGenerator
        )
        
        print("✅ تم استيراد جميع الوحدات بنجاح")
        
        # اختبار إنشاء الوكيل
        print("\n🤖 اختبار إنشاء الوكيل...")
        agent = RevolutionaryIntelligentAgent("TestAgent")
        print("✅ تم إنشاء الوكيل بنجاح")
        
        # اختبار حالة الوكيل
        print("\n📊 اختبار حالة الوكيل...")
        status = agent.get_agent_status()
        assert 'agent_info' in status
        assert 'capabilities' in status
        print("✅ حالة الوكيل صحيحة")
        
        # اختبار مولد المحتوى
        print("\n✍️ اختبار مولد المحتوى...")
        content_generator = BaserahContentGenerator()
        readme_content = content_generator.generate_readme_content("مشروع اختبار", {})
        assert len(readme_content) > 100
        print("✅ مولد المحتوى يعمل بنجاح")
        
        print("\n🎉 جميع الاختبارات نجحت!")
        
    except Exception as e:
        print(f"💥 فشل في الاختبارات: {e}")


def show_system_info():
    """عرض معلومات النظام."""
    
    print("ℹ️ معلومات النظام")
    print("=" * 50)
    
    try:
        from revolutionary_intelligent_agent import get_system_info
        
        system_info = get_system_info()
        
        print(f"📛 اسم النظام: {system_info['name']}")
        print(f"📦 الإصدار: {system_info['version']}")
        print(f"👨‍💻 المطور: {system_info['author']}")
        print(f"📄 الوصف: {system_info['description']}")
        print(f"⚖️ الترخيص: {system_info['license']}")
        
        print("\n🛠️ القدرات:")
        for capability in system_info['capabilities']:
            print(f"  ✅ {capability}")
        
        print("\n🌟 الميزات الثورية:")
        for feature, enabled in system_info['revolutionary_features'].items():
            if enabled:
                print(f"  🔥 {feature}")
        
        print("\n📱 أنواع المشاريع المدعومة:")
        for project_type in system_info['supported_project_types']:
            print(f"  📋 {project_type}")
        
    except Exception as e:
        print(f"💥 خطأ في عرض معلومات النظام: {e}")


def show_examples():
    """عرض أمثلة سريعة."""
    
    print("📚 أمثلة سريعة للاستخدام")
    print("=" * 50)
    
    try:
        from revolutionary_intelligent_agent import get_usage_examples
        
        examples = get_usage_examples()
        
        print("1️⃣ الاستخدام الأساسي:")
        print(examples['basic_usage'])
        
        print("\n2️⃣ الدالة السريعة:")
        print(examples['quick_function'])
        
        print("\n3️⃣ المشاريع المتعددة:")
        print(examples['multiple_projects'])
        
        print("\n4️⃣ الوكيل التجريبي:")
        print(examples['demo_agent'])
        
    except Exception as e:
        print(f"💥 خطأ في عرض الأمثلة: {e}")


async def main():
    """الدالة الرئيسية."""
    
    print_banner()
    
    while True:
        print_menu()
        
        try:
            choice = input("🎯 اختر رقم العملية: ").strip()
            
            if choice == '1':
                await create_single_project()
            elif choice == '2':
                await create_multiple_projects()
            elif choice == '3':
                show_demo_agent()
            elif choice == '4':
                await run_tests()
            elif choice == '5':
                show_system_info()
            elif choice == '6':
                show_examples()
            elif choice == '0':
                print("\n👋 شكراً لاستخدام الوكيل المساعد الثوري!")
                print("🌟 نراكم في المستقبل الثوري!")
                break
            else:
                print("❌ خيار غير صحيح! يرجى اختيار رقم من القائمة.")
            
            input("\n⏸️ اضغط Enter للمتابعة...")
            print("\n" + "="*70 + "\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 تم إيقاف البرنامج بواسطة المستخدم")
            break
        except Exception as e:
            print(f"\n💥 خطأ غير متوقع: {e}")
            input("⏸️ اضغط Enter للمتابعة...")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 وداعاً!")
    except Exception as e:
        print(f"💥 خطأ في تشغيل البرنامج: {e}")
