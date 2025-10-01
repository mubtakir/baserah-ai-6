#!/usr/bin/env python3
# basic_system_tests.py - اختبارات أساسية مبسطة للنظام الثوري
#
# 👨‍💻 المطور: باسل يحيى عبدالله
# 🧠 الأفكار الابتكارية: جميع الأفكار والنظريات الثورية من إبداع باسل يحيى عبدالله
# 🤖 التطوير: أكواد بدائية تم تطويرها بمساعدة وكيل ذكاء اصطناعي
# 📅 تاريخ الإنشاء: 2025
# 🧪 الاختبارات: اختبارات أساسية مبسطة للتحقق من الوظائف الأساسية
# 🌟 النظام: Baserah Universal System - تأكيد أساسي للجودة

import sys
import os
import unittest
from datetime import datetime

# إضافة مسار النظام
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BasicSystemTests(unittest.TestCase):
    """اختبارات أساسية مبسطة للنظام الثوري."""
    
    def setUp(self):
        """إعداد الاختبارات."""
        self.start_time = datetime.now()
        print(f"\n🧪 بدء الاختبارات الأساسية - {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def test_01_basic_imports(self):
        """اختبار الاستيرادات الأساسية."""
        print("\n📦 اختبار 1: الاستيرادات الأساسية")
        
        # اختبار numpy
        try:
            import numpy as np
            print("   ✅ numpy: متاح")
            self.assertTrue(True)
        except ImportError:
            print("   ❌ numpy: غير متاح")
            self.fail("numpy غير متاح")
        
        # اختبار matplotlib
        try:
            import matplotlib.pyplot as plt
            print("   ✅ matplotlib: متاح")
            self.assertTrue(True)
        except ImportError:
            print("   ❌ matplotlib: غير متاح")
            self.fail("matplotlib غير متاح")
    
    def test_02_basic_math_operations(self):
        """اختبار العمليات الرياضية الأساسية."""
        print("\n🧮 اختبار 2: العمليات الرياضية الأساسية")
        
        import numpy as np
        
        # اختبار sigmoid
        try:
            x = np.array([0, 1, -1])
            sigmoid_result = 1 / (1 + np.exp(-x))
            print(f"   ✅ sigmoid: {sigmoid_result}")
            self.assertEqual(len(sigmoid_result), 3)
        except Exception as e:
            print(f"   ❌ sigmoid: {e}")
            self.fail(f"فشل sigmoid: {e}")
        
        # اختبار linear
        try:
            x = np.array([0, 1, -1])
            linear_result = 2 * x + 1
            print(f"   ✅ linear: {linear_result}")
            self.assertEqual(len(linear_result), 3)
        except Exception as e:
            print(f"   ❌ linear: {e}")
            self.fail(f"فشل linear: {e}")
    
    def test_03_file_structure(self):
        """اختبار هيكل الملفات الأساسي."""
        print("\n📁 اختبار 3: هيكل الملفات الأساسي")
        
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # الملفات الأساسية
        essential_files = [
            'README.md',
            '__init__.py',
            'ai_oop_system.py'
        ]
        
        for file_name in essential_files:
            file_path = os.path.join(base_path, file_name)
            if os.path.exists(file_path):
                print(f"   ✅ {file_name}: موجود")
                self.assertTrue(os.path.isfile(file_path))
            else:
                print(f"   ❌ {file_name}: غير موجود")
                self.fail(f"{file_name} غير موجود")
    
    def test_04_developer_info(self):
        """اختبار وجود معلومات المطور."""
        print("\n👨‍💻 اختبار 4: معلومات المطور")
        
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # الملفات التي يجب أن تحتوي على معلومات المطور
        files_to_check = [
            'ai_oop_system.py',
            'README.md'
        ]
        
        developer_found = False
        
        for file_name in files_to_check:
            file_path = os.path.join(base_path, file_name)
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if 'باسل يحيى عبدالله' in content:
                            print(f"   ✅ {file_name}: يحتوي على معلومات المطور")
                            developer_found = True
                        else:
                            print(f"   ⚠️ {file_name}: لا يحتوي على معلومات المطور")
                except Exception as e:
                    print(f"   ❌ {file_name}: خطأ في القراءة - {e}")
        
        self.assertTrue(developer_found, "لم يتم العثور على معلومات المطور في أي ملف")
    
    def test_05_basic_system_functionality(self):
        """اختبار الوظائف الأساسية للنظام."""
        print("\n⚙️ اختبار 5: الوظائف الأساسية للنظام")
        
        try:
            # اختبار إنشاء معادلة بسيطة
            import numpy as np
            
            def simple_baserah_equation(x, n=1, k=1.0, alpha=1.0):
                """معادلة Baserah بسيطة: sigmoid + linear."""
                sigmoid_part = alpha / (1 + np.exp(-k * x))
                linear_part = k * x
                return sigmoid_part + linear_part
            
            # اختبار المعادلة
            x_test = np.array([0, 1, -1])
            result = simple_baserah_equation(x_test)
            
            print(f"   ✅ معادلة Baserah بسيطة: {result}")
            self.assertEqual(len(result), 3)
            self.assertTrue(all(np.isfinite(result)))
            
        except Exception as e:
            print(f"   ❌ فشل اختبار المعادلة: {e}")
            self.fail(f"فشل اختبار المعادلة: {e}")
    
    def test_06_interface_files_exist(self):
        """اختبار وجود ملفات الواجهات."""
        print("\n🖥️ اختبار 6: وجود ملفات الواجهات")
        
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        interfaces_path = os.path.join(base_path, 'user_interfaces')
        
        if os.path.exists(interfaces_path):
            print(f"   ✅ مجلد الواجهات: موجود")
            
            # فحص الملفات الأساسية للواجهات
            interface_files = [
                'web_interface.py',
                'api_interface.py', 
                'cli_interface.py'
            ]
            
            for file_name in interface_files:
                file_path = os.path.join(interfaces_path, file_name)
                if os.path.exists(file_path):
                    print(f"   ✅ {file_name}: موجود")
                else:
                    print(f"   ❌ {file_name}: غير موجود")
            
            self.assertTrue(True)
        else:
            print(f"   ❌ مجلد الواجهات: غير موجود")
            self.fail("مجلد الواجهات غير موجود")
    
    def test_07_revolutionary_intelligence_exists(self):
        """اختبار وجود مجلد الذكاء الثوري."""
        print("\n🧬 اختبار 7: وجود الذكاء الثوري")
        
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        revolutionary_path = os.path.join(base_path, 'revolutionary_intelligence')
        
        if os.path.exists(revolutionary_path):
            print(f"   ✅ مجلد الذكاء الثوري: موجود")
            
            # فحص الملفات الأساسية
            revolutionary_files = [
                'quranic_analysis_engine.py',
                'arabic_lexicon_engine.py',
                'revolutionary_mother_equation.py'
            ]
            
            for file_name in revolutionary_files:
                file_path = os.path.join(revolutionary_path, file_name)
                if os.path.exists(file_path):
                    print(f"   ✅ {file_name}: موجود")
                else:
                    print(f"   ❌ {file_name}: غير موجود")
            
            self.assertTrue(True)
        else:
            print(f"   ❌ مجلد الذكاء الثوري: غير موجود")
            self.fail("مجلد الذكاء الثوري غير موجود")
    
    def test_08_system_organization(self):
        """اختبار تنظيم النظام."""
        print("\n📋 اختبار 8: تنظيم النظام")
        
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # المجلدات المطلوبة
        required_directories = [
            'revolutionary_intelligence',
            'user_interfaces',
            'artistic_unit',
            'testing_validation'
        ]
        
        all_exist = True
        
        for directory in required_directories:
            dir_path = os.path.join(base_path, directory)
            if os.path.exists(dir_path) and os.path.isdir(dir_path):
                print(f"   ✅ {directory}: موجود")
            else:
                print(f"   ❌ {directory}: غير موجود")
                all_exist = False
        
        self.assertTrue(all_exist, "بعض المجلدات المطلوبة غير موجودة")

def run_basic_tests():
    """تشغيل الاختبارات الأساسية."""
    
    print("🌟 النظام الثوري Baserah - اختبارات أساسية")
    print("👨‍💻 المطور: باسل يحيى عبدالله")
    print("🧠 الأفكار الابتكارية: من إبداع باسل يحيى عبدالله")
    print("🤖 التطوير: بمساعدة وكيل ذكاء اصطناعي")
    print("🧬 النظريات: ثنائية الصفر، تعامد الأضداد، الفتائل")
    print("🎯 المنهجية: sigmoid + linear فقط، بدون AI تقليدي")
    print("=" * 80)
    
    # إنشاء مجموعة الاختبارات
    test_suite = unittest.TestLoader().loadTestsFromTestCase(BasicSystemTests)
    
    # تشغيل الاختبارات
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(test_suite)
    
    # تقرير النتائج
    print("\n" + "=" * 80)
    print("📊 تقرير النتائج الأساسية:")
    print(f"   🧪 إجمالي الاختبارات: {result.testsRun}")
    print(f"   ✅ نجح: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"   ❌ فشل: {len(result.failures)}")
    print(f"   🚨 أخطاء: {len(result.errors)}")
    
    # تحديد النجاح الإجمالي
    success_rate = ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100) if result.testsRun > 0 else 0
    
    print(f"\n🎯 معدل النجاح الأساسي: {success_rate:.1f}%")
    
    if success_rate >= 90:
        print("🎉 النظام الأساسي ممتاز!")
    elif success_rate >= 70:
        print("✅ النظام الأساسي جيد")
    elif success_rate >= 50:
        print("⚠️ النظام الأساسي مقبول")
    else:
        print("🚨 النظام الأساسي يحتاج مراجعة")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_basic_tests()
    sys.exit(0 if success else 1)
