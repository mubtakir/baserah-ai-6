#!/usr/bin/env python3
# test_revolutionary_agent.py - اختبار الوكيل المساعد الذكي الثوري

import asyncio
import sys
import os
from datetime import datetime
import tempfile
import shutil

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد الوكيل الثوري
from revolutionary_intelligent_agent import (
    RevolutionaryIntelligentAgent,
    create_revolutionary_project,
    create_multiple_revolutionary_projects,
    get_revolutionary_agent_demo
)


async def test_revolutionary_agent_basic():
    """اختبار أساسي للوكيل المساعد الثوري."""
    
    print("🧪 اختبار أساسي للوكيل المساعد الثوري")
    print("=" * 60)
    
    try:
        # إنشاء الوكيل
        agent = RevolutionaryIntelligentAgent("TestRevolutionaryAgent")
        
        # التحقق من التهيئة
        assert agent.agent_name == "TestRevolutionaryAgent"
        assert agent.version.startswith("1.0.0")
        assert hasattr(agent, 'agent_core')
        assert hasattr(agent, 'content_generator')
        
        print("✅ تم إنشاء الوكيل بنجاح")
        
        # اختبار حالة الوكيل
        status = agent.get_agent_status()
        
        assert 'agent_info' in status
        assert 'capabilities' in status
        assert 'statistics' in status
        assert 'revolutionary_features' in status
        
        print("✅ حالة الوكيل صحيحة")
        
        # التحقق من القدرات
        capabilities = status['capabilities']
        required_capabilities = [
            'project_understanding', 'project_creation', 'code_generation',
            'cognitive_intelligence', 'revolutionary_thinking', 'baserah_integration'
        ]
        
        for capability in required_capabilities:
            assert capabilities.get(capability, False), f"القدرة مفقودة: {capability}"
        
        print("✅ جميع القدرات المطلوبة متوفرة")
        
        # التحقق من الميزات الثورية
        revolutionary_features = status['revolutionary_features']
        assert revolutionary_features['baserah_pure_approach']
        assert revolutionary_features['basil_theories_integration']
        assert revolutionary_features['cognitive_deep_thinking']
        
        print("✅ الميزات الثورية مفعلة")
        
        return True
        
    except Exception as e:
        print(f"❌ فشل الاختبار الأساسي: {e}")
        return False


async def test_project_creation():
    """اختبار إنشاء مشروع ثوري."""
    
    print("\n🏗️ اختبار إنشاء مشروع ثوري")
    print("=" * 60)
    
    try:
        # إنشاء مجلد مؤقت للاختبار
        with tempfile.TemporaryDirectory() as temp_dir:
            # تغيير المجلد الحالي للمجلد المؤقت
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                # إنشاء الوكيل
                agent = RevolutionaryIntelligentAgent("ProjectTestAgent")
                
                # فكرة مشروع بسيطة للاختبار
                project_idea = "حاسبة رياضية ثورية مدعومة بنظام Baserah"
                project_requirements = {
                    'type': 'desktop_application',
                    'language': 'python',
                    'features': ['basic_calculations', 'baserah_functions', 'basil_theories']
                }
                
                print(f"📋 إنشاء مشروع: {project_idea}")
                
                # إنشاء المشروع
                result = await agent.understand_and_create_project(project_idea, project_requirements)
                
                # التحقق من النتائج
                assert 'project_info' in result
                assert 'project_summary' in result
                assert 'success_metrics' in result
                assert 'revolutionary_features' in result
                assert 'project_structure' in result
                
                print("✅ تم إنشاء المشروع بنجاح")
                
                # التحقق من الهيكلية
                project_structure = result['project_structure']
                assert project_structure['total_files'] > 0
                assert project_structure['total_folders'] > 0
                
                print(f"📁 ملفات منشأة: {project_structure['total_files']}")
                print(f"📂 مجلدات منشأة: {project_structure['total_folders']}")
                
                # التحقق من الميزات الثورية
                revolutionary_features = result['revolutionary_features']
                assert revolutionary_features['baserah_integration']
                assert revolutionary_features['cognitive_intelligence']
                assert len(revolutionary_features['revolutionary_insights']) > 0
                
                print("✅ الميزات الثورية مطبقة")
                
                # التحقق من معدل النجاح
                success_rate = result['success_metrics']['overall_success_rate']
                assert success_rate > 0.5, f"معدل نجاح منخفض: {success_rate}"
                
                print(f"📈 معدل النجاح: {success_rate:.1%}")
                
                # التحقق من وجود الملفات المهمة
                files_created = project_structure['files_created']
                important_files = ['README.md', 'requirements.txt', 'main.py']
                
                for important_file in important_files:
                    file_found = any(important_file in file_path for file_path in files_created)
                    if file_found:
                        print(f"✅ ملف مهم موجود: {important_file}")
                    else:
                        print(f"⚠️ ملف مهم مفقود: {important_file}")
                
                return True
                
            finally:
                # العودة للمجلد الأصلي
                os.chdir(original_cwd)
        
    except Exception as e:
        print(f"❌ فشل اختبار إنشاء المشروع: {e}")
        return False


async def test_multiple_projects():
    """اختبار إنشاء عدة مشاريع."""
    
    print("\n🚀 اختبار إنشاء عدة مشاريع")
    print("=" * 60)
    
    try:
        # قائمة مشاريع للاختبار
        projects_list = [
            "آلة حاسبة بسيطة مدعومة بـ Baserah",
            "تطبيق قائمة مهام ثوري",
            "محول وحدات رياضي"
        ]
        
        print(f"📋 إنشاء {len(projects_list)} مشروع...")
        
        # استخدام الدالة السريعة
        result = await create_multiple_revolutionary_projects(projects_list, "BatchTestAgent")
        
        # التحقق من النتائج
        assert 'batch_id' in result
        assert 'total_projects' in result
        assert 'successful_projects' in result
        assert 'projects_results' in result
        
        print("✅ تم إنشاء الدفعة بنجاح")
        
        # التحقق من الإحصائيات
        total_projects = result['total_projects']
        successful_projects = result['successful_projects']
        success_rate = result['batch_statistics']['success_rate']
        
        print(f"📊 إجمالي المشاريع: {total_projects}")
        print(f"✅ مشاريع ناجحة: {successful_projects}")
        print(f"📈 معدل النجاح: {success_rate:.1%}")
        
        assert total_projects == len(projects_list)
        assert successful_projects >= 0
        assert 0 <= success_rate <= 1
        
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار المشاريع المتعددة: {e}")
        return False


async def test_quick_functions():
    """اختبار الدوال السريعة."""
    
    print("\n⚡ اختبار الدوال السريعة")
    print("=" * 60)
    
    try:
        # اختبار الدالة السريعة لإنشاء مشروع
        project_idea = "تطبيق بسيط للاختبار"
        
        print(f"📋 اختبار الدالة السريعة: {project_idea}")
        
        result = await create_revolutionary_project(project_idea, {}, "QuickTestAgent")
        
        # التحقق من النتائج
        assert 'project_info' in result
        assert result['project_info']['project_idea'] == project_idea
        
        print("✅ الدالة السريعة تعمل بنجاح")
        
        # اختبار الوكيل التجريبي
        demo_agent = get_revolutionary_agent_demo()
        
        assert demo_agent.agent_name == "DemoRevolutionaryAgent"
        assert hasattr(demo_agent, 'agent_core')
        
        print("✅ الوكيل التجريبي يعمل بنجاح")
        
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار الدوال السريعة: {e}")
        return False


async def test_agent_state_management():
    """اختبار إدارة حالة الوكيل."""
    
    print("\n💾 اختبار إدارة حالة الوكيل")
    print("=" * 60)
    
    try:
        # إنشاء الوكيل
        agent = RevolutionaryIntelligentAgent("StateTestAgent")
        
        # تعديل بعض الإحصائيات للاختبار
        agent.agent_statistics['projects_created'] = 5
        agent.agent_statistics['total_files_generated'] = 50
        agent.projects_history.append({
            'project_id': 'test123',
            'project_idea': 'مشروع اختبار',
            'creation_time': datetime.now().isoformat(),
            'success': True
        })
        
        # حفظ الحالة
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp_file:
            temp_file_path = temp_file.name
        
        try:
            saved_path = agent.save_agent_state(temp_file_path)
            assert saved_path == temp_file_path
            assert os.path.exists(temp_file_path)
            
            print("✅ تم حفظ حالة الوكيل")
            
            # إنشاء وكيل جديد وتحميل الحالة
            new_agent = RevolutionaryIntelligentAgent("NewStateTestAgent")
            
            # التحقق من الحالة الأولية
            assert new_agent.agent_statistics['projects_created'] == 0
            assert len(new_agent.projects_history) == 0
            
            # تحميل الحالة
            load_success = new_agent.load_agent_state(temp_file_path)
            assert load_success
            
            # التحقق من استعادة البيانات
            assert new_agent.agent_statistics['projects_created'] == 5
            assert new_agent.agent_statistics['total_files_generated'] == 50
            assert len(new_agent.projects_history) == 1
            assert new_agent.projects_history[0]['project_id'] == 'test123'
            
            print("✅ تم تحميل حالة الوكيل بنجاح")
            
            return True
            
        finally:
            # تنظيف الملف المؤقت
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
        
    except Exception as e:
        print(f"❌ فشل اختبار إدارة الحالة: {e}")
        return False


async def test_performance_assessment():
    """اختبار تقييم الأداء."""
    
    print("\n📊 اختبار تقييم الأداء")
    print("=" * 60)
    
    try:
        # إنشاء الوكيل
        agent = RevolutionaryIntelligentAgent("PerformanceTestAgent")
        
        # اختبار تقييم الأداء للوكيل الجديد
        performance = agent._assess_agent_performance()
        assert performance == 'new'
        print("✅ تقييم الوكيل الجديد: new")
        
        # محاكاة بعض المشاريع الناجحة
        agent.agent_statistics['projects_created'] = 3
        agent.agent_statistics['average_project_success_rate'] = 0.85
        
        performance = agent._assess_agent_performance()
        assert performance == 'very_good'
        print("✅ تقييم الوكيل المتقدم: very_good")
        
        # محاكاة المزيد من المشاريع
        agent.agent_statistics['projects_created'] = 10
        agent.agent_statistics['average_project_success_rate'] = 0.95
        
        performance = agent._assess_agent_performance()
        assert performance == 'excellent'
        print("✅ تقييم الوكيل الممتاز: excellent")
        
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار تقييم الأداء: {e}")
        return False


async def run_all_tests():
    """تشغيل جميع الاختبارات."""
    
    print("🧪✨ بدء اختبارات الوكيل المساعد الذكي الثوري")
    print("🧬 مدعوم بنظام Baserah ونظريات باسل الثورية")
    print("=" * 70)
    print(f"📅 وقت الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    tests = [
        ("الاختبار الأساسي", test_revolutionary_agent_basic),
        ("اختبار إنشاء المشروع", test_project_creation),
        ("اختبار المشاريع المتعددة", test_multiple_projects),
        ("اختبار الدوال السريعة", test_quick_functions),
        ("اختبار إدارة الحالة", test_agent_state_management),
        ("اختبار تقييم الأداء", test_performance_assessment)
    ]
    
    results = []
    
    for test_name, test_function in tests:
        print(f"🔬 تشغيل {test_name}...")
        try:
            result = await test_function()
            results.append((test_name, result))
            if result:
                print(f"✅ نجح {test_name}")
            else:
                print(f"❌ فشل {test_name}")
        except Exception as e:
            print(f"💥 خطأ في {test_name}: {e}")
            results.append((test_name, False))
        
        print()
    
    # ملخص النتائج
    print("📊 ملخص نتائج الاختبارات")
    print("=" * 70)
    
    passed_tests = sum(1 for _, result in results if result)
    total_tests = len(results)
    success_rate = passed_tests / total_tests
    
    for test_name, result in results:
        status = "✅ نجح" if result else "❌ فشل"
        print(f"{status} {test_name}")
    
    print()
    print(f"📈 النتيجة الإجمالية:")
    print(f"   اختبارات ناجحة: {passed_tests}/{total_tests}")
    print(f"   معدل النجاح: {success_rate:.1%}")
    
    if success_rate >= 0.8:
        print("🏆 النتيجة النهائية: ممتاز!")
        print("🌟 الوكيل المساعد الثوري جاهز للاستخدام!")
    elif success_rate >= 0.6:
        print("👍 النتيجة النهائية: جيد")
        print("⚠️ بعض التحسينات مطلوبة")
    else:
        print("⚠️ النتيجة النهائية: يحتاج تطوير")
        print("🔧 مراجعة وإصلاح مطلوب")
    
    print()
    print("🔬 انتهت اختبارات الوكيل المساعد الثوري")
    print(f"📅 وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    asyncio.run(run_all_tests())
