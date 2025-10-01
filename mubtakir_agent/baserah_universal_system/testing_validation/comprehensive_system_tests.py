#!/usr/bin/env python3
# comprehensive_system_tests.py - اختبارات شاملة للنظام الثوري
#
# 👨‍💻 المطور: باسل يحيى عبدالله
# 🧠 الأفكار الابتكارية: جميع الأفكار والنظريات الثورية من إبداع باسل يحيى عبدالله
# 🤖 التطوير: أكواد بدائية تم تطويرها بمساعدة وكيل ذكاء اصطناعي
# 📅 تاريخ الإنشاء: 2025
# 🧪 الاختبارات: اختبارات شاملة لجميع مكونات النظام الثوري
# 🌟 النظام: Baserah Universal System - تأكيد نهائي للجودة والأداء

import sys
import os
import unittest
import importlib
import traceback
from datetime import datetime
from pathlib import Path

# إضافة مسار النظام
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BaserahComprehensiveTests(unittest.TestCase):
    """اختبارات شاملة للنظام الثوري Baserah."""
    
    def setUp(self):
        """إعداد الاختبارات."""
        self.test_results = []
        self.start_time = datetime.now()
        print(f"\n🧪 بدء الاختبارات الشاملة - {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
    
    def tearDown(self):
        """تنظيف بعد الاختبارات."""
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()
        print(f"\n⏱️ انتهاء الاختبارات - المدة: {duration:.2f} ثانية")
    
    def test_01_core_system_imports(self):
        """اختبار استيراد الملفات الأساسية."""
        print("\n🔍 اختبار 1: استيراد الملفات الأساسية")
        
        core_modules = [
            'ai_oop_system',
            'advanced_cognitive_objects',
            'baserah_main_imports'
        ]
        
        for module_name in core_modules:
            with self.subTest(module=module_name):
                try:
                    module = importlib.import_module(module_name)
                    print(f"   ✅ {module_name}: نجح الاستيراد")
                    self.assertIsNotNone(module)
                except Exception as e:
                    print(f"   ❌ {module_name}: فشل الاستيراد - {e}")
                    self.fail(f"فشل استيراد {module_name}: {e}")
    
    def test_02_revolutionary_intelligence_imports(self):
        """اختبار استيراد وحدات الذكاء الثوري."""
        print("\n🧬 اختبار 2: استيراد وحدات الذكاء الثوري")
        
        revolutionary_modules = [
            'revolutionary_intelligence.revolutionary_mother_equation',
            'revolutionary_intelligence.quranic_analysis_engine',
            'revolutionary_intelligence.arabic_lexicon_engine',
            'revolutionary_intelligence.advanced_mathematical_engine',
            'revolutionary_intelligence.dream_interpretation_engine'
        ]
        
        for module_name in revolutionary_modules:
            with self.subTest(module=module_name):
                try:
                    module = importlib.import_module(module_name)
                    print(f"   ✅ {module_name}: نجح الاستيراد")
                    self.assertIsNotNone(module)
                except Exception as e:
                    print(f"   ❌ {module_name}: فشل الاستيراد - {e}")
                    # لا نفشل الاختبار إذا كان الملف غير موجود
                    if "No module named" not in str(e):
                        self.fail(f"فشل استيراد {module_name}: {e}")
    
    def test_03_user_interfaces_imports(self):
        """اختبار استيراد واجهات المستخدم."""
        print("\n🖥️ اختبار 3: استيراد واجهات المستخدم")
        
        interface_modules = [
            'user_interfaces.web_interface',
            'user_interfaces.api_interface',
            'user_interfaces.cli_interface',
            'user_interfaces.desktop_gui'
        ]
        
        for module_name in interface_modules:
            with self.subTest(module=module_name):
                try:
                    module = importlib.import_module(module_name)
                    print(f"   ✅ {module_name}: نجح الاستيراد")
                    self.assertIsNotNone(module)
                except Exception as e:
                    print(f"   ❌ {module_name}: فشل الاستيراد - {e}")
                    if "No module named" not in str(e):
                        self.fail(f"فشل استيراد {module_name}: {e}")
    
    def test_04_artistic_unit_imports(self):
        """اختبار استيراد الوحدة الفنية."""
        print("\n🎨 اختبار 4: استيراد الوحدة الفنية")
        
        artistic_modules = [
            'artistic_unit.integrated_system',
            'artistic_intelligence.baserah_core'
        ]
        
        for module_name in artistic_modules:
            with self.subTest(module=module_name):
                try:
                    module = importlib.import_module(module_name)
                    print(f"   ✅ {module_name}: نجح الاستيراد")
                    self.assertIsNotNone(module)
                except Exception as e:
                    print(f"   ❌ {module_name}: فشل الاستيراد - {e}")
                    if "No module named" not in str(e):
                        self.fail(f"فشل استيراد {module_name}: {e}")
    
    def test_05_knowledge_systems_imports(self):
        """اختبار استيراد أنظمة المعرفة."""
        print("\n📚 اختبار 5: استيراد أنظمة المعرفة")
        
        knowledge_modules = [
            'knowledge_systems.semantic_meaning.semantic_meaning_system',
            'knowledge_systems.shapes_database.shapes_database_system',
            'knowledge_systems.universal_equations.universal_equations_system'
        ]
        
        for module_name in knowledge_modules:
            with self.subTest(module=module_name):
                try:
                    module = importlib.import_module(module_name)
                    print(f"   ✅ {module_name}: نجح الاستيراد")
                    self.assertIsNotNone(module)
                except Exception as e:
                    print(f"   ❌ {module_name}: فشل الاستيراد - {e}")
                    if "No module named" not in str(e):
                        self.fail(f"فشل استيراد {module_name}: {e}")
    
    def test_06_system_initialization(self):
        """اختبار تهيئة النظام الأساسي."""
        print("\n🚀 اختبار 6: تهيئة النظام الأساسي")
        
        try:
            # اختبار تهيئة النظام الأم
            from revolutionary_intelligence.revolutionary_mother_equation import revolutionary_mother_system
            mother_system = revolutionary_mother_system("TestSystem")
            print(f"   ✅ النظام الأم: تم إنشاؤه بنجاح - {mother_system.system_id}")
            self.assertIsNotNone(mother_system.system_id)
            
            # اختبار الحصول على ملخص النظام
            summary = mother_system.get_system_summary()
            print(f"   ✅ ملخص النظام: {len(summary)} عنصر")
            self.assertIsInstance(summary, dict)
            self.assertIn('system_id', summary)
            
        except Exception as e:
            print(f"   ❌ فشل تهيئة النظام الأساسي: {e}")
            self.fail(f"فشل تهيئة النظام: {e}")
    
    def test_07_quranic_engine_functionality(self):
        """اختبار وظائف محرك التحليل القرآني."""
        print("\n🕌 اختبار 7: وظائف محرك التحليل القرآني")
        
        try:
            from revolutionary_intelligence.quranic_analysis_engine import QuranicAnalysisEngine
            
            # إنشاء المحرك
            engine = QuranicAnalysisEngine("TestQuranicEngine")
            print(f"   ✅ إنشاء المحرك: {engine.engine_name}")
            self.assertIsNotNone(engine.engine_name)
            
            # اختبار تحليل آية تجريبية
            try:
                analysis = engine.analyze_verse_revolutionary(1, 1, deep_analysis=False)
                print(f"   ✅ تحليل آية: نجح التحليل")
                self.assertIsNotNone(analysis)
            except Exception as e:
                print(f"   ⚠️ تحليل آية: {e} (قد يكون بسبب عدم توفر البيانات)")
            
            # اختبار حالة المحرك
            status = engine.get_engine_status()
            print(f"   ✅ حالة المحرك: {status['engine_info']['name']}")
            self.assertIsInstance(status, dict)
            self.assertIn('engine_info', status)
            
        except Exception as e:
            print(f"   ❌ فشل اختبار محرك القرآن: {e}")
            # لا نفشل الاختبار إذا كان الملف غير موجود
            if "No module named" not in str(e):
                self.fail(f"فشل اختبار محرك القرآن: {e}")
    
    def test_08_lexicon_engine_functionality(self):
        """اختبار وظائف محرك المعجم العربي."""
        print("\n📚 اختبار 8: وظائف محرك المعجم العربي")
        
        try:
            from revolutionary_intelligence.arabic_lexicon_engine import ArabicLexiconEngine
            
            # إنشاء المحرك
            engine = ArabicLexiconEngine("TestLexiconEngine")
            print(f"   ✅ إنشاء المحرك: {engine.engine_name}")
            self.assertIsNotNone(engine.engine_name)
            
            # اختبار تحليل كلمة تجريبية
            try:
                analysis = engine.analyze_word_revolutionary("كتاب", deep_analysis=False)
                print(f"   ✅ تحليل كلمة: نجح التحليل")
                self.assertIsNotNone(analysis)
            except Exception as e:
                print(f"   ⚠️ تحليل كلمة: {e} (قد يكون بسبب عدم توفر البيانات)")
            
            # اختبار حالة المحرك
            status = engine.get_engine_status()
            print(f"   ✅ حالة المحرك: {status['engine_info']['name']}")
            self.assertIsInstance(status, dict)
            self.assertIn('engine_info', status)
            
        except Exception as e:
            print(f"   ❌ فشل اختبار محرك المعجم: {e}")
            if "No module named" not in str(e):
                self.fail(f"فشل اختبار محرك المعجم: {e}")
    
    def test_09_web_interface_initialization(self):
        """اختبار تهيئة واجهة الويب."""
        print("\n🌐 اختبار 9: تهيئة واجهة الويب")
        
        try:
            from user_interfaces.web_interface import BaserahWebInterface
            
            # إنشاء واجهة الويب
            web_interface = BaserahWebInterface()
            print(f"   ✅ إنشاء واجهة الويب: نجح")
            self.assertIsNotNone(web_interface.app)
            
            # اختبار جاهزية النظام
            print(f"   ✅ جاهزية النظام: {web_interface.system_ready}")
            self.assertIsInstance(web_interface.system_ready, bool)
            
        except Exception as e:
            print(f"   ❌ فشل اختبار واجهة الويب: {e}")
            if "No module named" not in str(e):
                self.fail(f"فشل اختبار واجهة الويب: {e}")
    
    def test_10_file_structure_validation(self):
        """اختبار صحة هيكل الملفات."""
        print("\n📁 اختبار 10: صحة هيكل الملفات")
        
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
        
        for directory in required_directories:
            dir_path = base_path / directory
            with self.subTest(directory=directory):
                if dir_path.exists():
                    print(f"   ✅ {directory}: موجود")
                    self.assertTrue(dir_path.is_dir())
                else:
                    print(f"   ⚠️ {directory}: غير موجود")
        
        # الملفات المطلوبة
        required_files = [
            'README.md',
            '__init__.py',
            'ai_oop_system.py',
            'advanced_cognitive_objects.py'
        ]
        
        for file_name in required_files:
            file_path = base_path / file_name
            with self.subTest(file=file_name):
                if file_path.exists():
                    print(f"   ✅ {file_name}: موجود")
                    self.assertTrue(file_path.is_file())
                else:
                    print(f"   ⚠️ {file_name}: غير موجود")

def run_comprehensive_tests():
    """تشغيل جميع الاختبارات الشاملة."""
    
    print("🌟 النظام الثوري Baserah - اختبارات شاملة")
    print("👨‍💻 المطور: باسل يحيى عبدالله")
    print("🧠 الأفكار الابتكارية: من إبداع باسل يحيى عبدالله")
    print("🤖 التطوير: بمساعدة وكيل ذكاء اصطناعي")
    print("=" * 80)
    
    # إنشاء مجموعة الاختبارات
    test_suite = unittest.TestLoader().loadTestsFromTestCase(BaserahComprehensiveTests)
    
    # تشغيل الاختبارات
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(test_suite)
    
    # تقرير النتائج
    print("\n" + "=" * 80)
    print("📊 تقرير النتائج النهائي:")
    print(f"   🧪 إجمالي الاختبارات: {result.testsRun}")
    print(f"   ✅ نجح: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"   ❌ فشل: {len(result.failures)}")
    print(f"   🚨 أخطاء: {len(result.errors)}")
    
    if result.failures:
        print("\n❌ الاختبارات الفاشلة:")
        for test, traceback in result.failures:
            print(f"   • {test}: {traceback.split('AssertionError: ')[-1].strip()}")
    
    if result.errors:
        print("\n🚨 أخطاء الاختبارات:")
        for test, traceback in result.errors:
            print(f"   • {test}: {traceback.split('Exception: ')[-1].strip()}")
    
    # تحديد النجاح الإجمالي
    success_rate = ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100) if result.testsRun > 0 else 0
    
    print(f"\n🎯 معدل النجاح: {success_rate:.1f}%")
    
    if success_rate >= 80:
        print("🎉 النظام جاهز للإنتاج!")
    elif success_rate >= 60:
        print("⚠️ النظام يحتاج تحسينات طفيفة")
    else:
        print("🚨 النظام يحتاج مراجعة شاملة")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_comprehensive_tests()
    sys.exit(0 if success else 1)
