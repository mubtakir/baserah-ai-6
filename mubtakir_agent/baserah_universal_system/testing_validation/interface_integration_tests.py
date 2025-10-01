#!/usr/bin/env python3
# interface_integration_tests.py - اختبارات تكامل الواجهات
#
# 👨‍💻 المطور: باسل يحيى عبدالله
# 🧠 الأفكار الابتكارية: جميع الأفكار والنظريات الثورية من إبداع باسل يحيى عبدالله
# 🤖 التطوير: أكواد بدائية تم تطويرها بمساعدة وكيل ذكاء اصطناعي
# 📅 تاريخ الإنشاء: 2025
# 🧪 الاختبارات: اختبارات تكامل الواجهات مع المحركات الثورية
# 🌟 النظام: Baserah Universal System - تأكيد تكامل الواجهات

import sys
import os
import unittest
import json
from datetime import datetime

# إضافة مسار النظام
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class InterfaceIntegrationTests(unittest.TestCase):
    """اختبارات تكامل الواجهات مع المحركات."""
    
    def setUp(self):
        """إعداد الاختبارات."""
        self.start_time = datetime.now()
        print(f"\n🔗 بدء اختبارات تكامل الواجهات - {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def test_01_web_interface_quranic_integration(self):
        """اختبار تكامل واجهة الويب مع محرك القرآن."""
        print("\n🌐🕌 اختبار 1: تكامل واجهة الويب مع محرك القرآن")
        
        try:
            from user_interfaces.web_interface import BaserahWebInterface
            
            # إنشاء واجهة الويب
            web_interface = BaserahWebInterface()
            print("   ✅ إنشاء واجهة الويب: نجح")
            
            # التحقق من وجود محرك القرآن
            if hasattr(web_interface, 'quranic_engine'):
                print("   ✅ محرك القرآن: مدمج في واجهة الويب")
                self.assertIsNotNone(web_interface.quranic_engine)
                
                # التحقق من اسم المحرك
                engine_name = web_interface.quranic_engine.engine_name
                print(f"   ✅ اسم المحرك: {engine_name}")
                self.assertIn("Web", engine_name)
            else:
                print("   ❌ محرك القرآن: غير مدمج في واجهة الويب")
                self.fail("محرك القرآن غير مدمج في واجهة الويب")
                
        except Exception as e:
            print(f"   ❌ فشل اختبار تكامل واجهة الويب مع القرآن: {e}")
            self.fail(f"فشل التكامل: {e}")
    
    def test_02_web_interface_lexicon_integration(self):
        """اختبار تكامل واجهة الويب مع محرك المعجم."""
        print("\n🌐📚 اختبار 2: تكامل واجهة الويب مع محرك المعجم")
        
        try:
            from user_interfaces.web_interface import BaserahWebInterface
            
            # إنشاء واجهة الويب
            web_interface = BaserahWebInterface()
            print("   ✅ إنشاء واجهة الويب: نجح")
            
            # التحقق من وجود محرك المعجم
            if hasattr(web_interface, 'lexicon_engine'):
                print("   ✅ محرك المعجم: مدمج في واجهة الويب")
                self.assertIsNotNone(web_interface.lexicon_engine)
                
                # التحقق من اسم المحرك
                engine_name = web_interface.lexicon_engine.engine_name
                print(f"   ✅ اسم المحرك: {engine_name}")
                self.assertIn("Web", engine_name)
            else:
                print("   ❌ محرك المعجم: غير مدمج في واجهة الويب")
                self.fail("محرك المعجم غير مدمج في واجهة الويب")
                
        except Exception as e:
            print(f"   ❌ فشل اختبار تكامل واجهة الويب مع المعجم: {e}")
            self.fail(f"فشل التكامل: {e}")
    
    def test_03_api_interface_quranic_integration(self):
        """اختبار تكامل واجهة API مع محرك القرآن."""
        print("\n🔌🕌 اختبار 3: تكامل واجهة API مع محرك القرآن")
        
        try:
            from user_interfaces.api_interface import BaserahAPIInterface
            
            # إنشاء واجهة API
            api_interface = BaserahAPIInterface()
            print("   ✅ إنشاء واجهة API: نجح")
            
            # التحقق من وجود محرك القرآن
            if hasattr(api_interface, 'quranic_engine'):
                print("   ✅ محرك القرآن: مدمج في واجهة API")
                self.assertIsNotNone(api_interface.quranic_engine)
                
                # التحقق من اسم المحرك
                engine_name = api_interface.quranic_engine.engine_name
                print(f"   ✅ اسم المحرك: {engine_name}")
                self.assertIn("API", engine_name)
            else:
                print("   ❌ محرك القرآن: غير مدمج في واجهة API")
                self.fail("محرك القرآن غير مدمج في واجهة API")
                
        except Exception as e:
            print(f"   ❌ فشل اختبار تكامل واجهة API مع القرآن: {e}")
            self.fail(f"فشل التكامل: {e}")
    
    def test_04_api_interface_lexicon_integration(self):
        """اختبار تكامل واجهة API مع محرك المعجم."""
        print("\n🔌📚 اختبار 4: تكامل واجهة API مع محرك المعجم")
        
        try:
            from user_interfaces.api_interface import BaserahAPIInterface
            
            # إنشاء واجهة API
            api_interface = BaserahAPIInterface()
            print("   ✅ إنشاء واجهة API: نجح")
            
            # التحقق من وجود محرك المعجم
            if hasattr(api_interface, 'lexicon_engine'):
                print("   ✅ محرك المعجم: مدمج في واجهة API")
                self.assertIsNotNone(api_interface.lexicon_engine)
                
                # التحقق من اسم المحرك
                engine_name = api_interface.lexicon_engine.engine_name
                print(f"   ✅ اسم المحرك: {engine_name}")
                self.assertIn("API", engine_name)
            else:
                print("   ❌ محرك المعجم: غير مدمج في واجهة API")
                self.fail("محرك المعجم غير مدمج في واجهة API")
                
        except Exception as e:
            print(f"   ❌ فشل اختبار تكامل واجهة API مع المعجم: {e}")
            self.fail(f"فشل التكامل: {e}")
    
    def test_05_cli_interface_quranic_integration(self):
        """اختبار تكامل واجهة CLI مع محرك القرآن."""
        print("\n💻🕌 اختبار 5: تكامل واجهة CLI مع محرك القرآن")
        
        try:
            from user_interfaces.cli_interface import BaserahCLI
            
            # إنشاء واجهة CLI
            cli_interface = BaserahCLI()
            print("   ✅ إنشاء واجهة CLI: نجح")
            
            # التحقق من وجود محرك القرآن
            if hasattr(cli_interface, 'quranic_engine'):
                print("   ✅ محرك القرآن: مدمج في واجهة CLI")
                self.assertIsNotNone(cli_interface.quranic_engine)
                
                # التحقق من اسم المحرك
                engine_name = cli_interface.quranic_engine.engine_name
                print(f"   ✅ اسم المحرك: {engine_name}")
                self.assertIn("CLI", engine_name)
            else:
                print("   ❌ محرك القرآن: غير مدمج في واجهة CLI")
                self.fail("محرك القرآن غير مدمج في واجهة CLI")
                
        except Exception as e:
            print(f"   ❌ فشل اختبار تكامل واجهة CLI مع القرآن: {e}")
            self.fail(f"فشل التكامل: {e}")
    
    def test_06_cli_interface_lexicon_integration(self):
        """اختبار تكامل واجهة CLI مع محرك المعجم."""
        print("\n💻📚 اختبار 6: تكامل واجهة CLI مع محرك المعجم")
        
        try:
            from user_interfaces.cli_interface import BaserahCLI
            
            # إنشاء واجهة CLI
            cli_interface = BaserahCLI()
            print("   ✅ إنشاء واجهة CLI: نجح")
            
            # التحقق من وجود محرك المعجم
            if hasattr(cli_interface, 'lexicon_engine'):
                print("   ✅ محرك المعجم: مدمج في واجهة CLI")
                self.assertIsNotNone(cli_interface.lexicon_engine)
                
                # التحقق من اسم المحرك
                engine_name = cli_interface.lexicon_engine.engine_name
                print(f"   ✅ اسم المحرك: {engine_name}")
                self.assertIn("CLI", engine_name)
            else:
                print("   ❌ محرك المعجم: غير مدمج في واجهة CLI")
                self.fail("محرك المعجم غير مدمج في واجهة CLI")
                
        except Exception as e:
            print(f"   ❌ فشل اختبار تكامل واجهة CLI مع المعجم: {e}")
            self.fail(f"فشل التكامل: {e}")
    
    def test_07_interface_consistency(self):
        """اختبار اتساق المحركات عبر الواجهات."""
        print("\n🔄 اختبار 7: اتساق المحركات عبر الواجهات")
        
        try:
            from user_interfaces.web_interface import BaserahWebInterface
            from user_interfaces.api_interface import BaserahAPIInterface
            from user_interfaces.cli_interface import BaserahCLI
            
            # إنشاء جميع الواجهات
            web_interface = BaserahWebInterface()
            api_interface = BaserahAPIInterface()
            cli_interface = BaserahCLI()
            
            print("   ✅ إنشاء جميع الواجهات: نجح")
            
            # التحقق من اتساق محرك القرآن
            if (hasattr(web_interface, 'quranic_engine') and 
                hasattr(api_interface, 'quranic_engine') and 
                hasattr(cli_interface, 'quranic_engine')):
                
                print("   ✅ محرك القرآن: متسق عبر جميع الواجهات")
                
                # التحقق من أن جميع المحركات من نفس النوع
                web_type = type(web_interface.quranic_engine).__name__
                api_type = type(api_interface.quranic_engine).__name__
                cli_type = type(cli_interface.quranic_engine).__name__
                
                print(f"   ✅ أنواع المحركات: Web={web_type}, API={api_type}, CLI={cli_type}")
                self.assertEqual(web_type, api_type)
                self.assertEqual(api_type, cli_type)
            else:
                print("   ❌ محرك القرآن: غير متسق عبر الواجهات")
            
            # التحقق من اتساق محرك المعجم
            if (hasattr(web_interface, 'lexicon_engine') and 
                hasattr(api_interface, 'lexicon_engine') and 
                hasattr(cli_interface, 'lexicon_engine')):
                
                print("   ✅ محرك المعجم: متسق عبر جميع الواجهات")
                
                # التحقق من أن جميع المحركات من نفس النوع
                web_type = type(web_interface.lexicon_engine).__name__
                api_type = type(api_interface.lexicon_engine).__name__
                cli_type = type(cli_interface.lexicon_engine).__name__
                
                print(f"   ✅ أنواع المحركات: Web={web_type}, API={api_type}, CLI={cli_type}")
                self.assertEqual(web_type, api_type)
                self.assertEqual(api_type, cli_type)
            else:
                print("   ❌ محرك المعجم: غير متسق عبر الواجهات")
                
        except Exception as e:
            print(f"   ❌ فشل اختبار اتساق الواجهات: {e}")
            self.fail(f"فشل اختبار الاتساق: {e}")
    
    def test_08_interface_functionality(self):
        """اختبار وظائف الواجهات الأساسية."""
        print("\n⚙️ اختبار 8: وظائف الواجهات الأساسية")
        
        try:
            from user_interfaces.web_interface import BaserahWebInterface
            
            # إنشاء واجهة الويب
            web_interface = BaserahWebInterface()
            print("   ✅ إنشاء واجهة الويب: نجح")
            
            # التحقق من Flask app
            if hasattr(web_interface, 'app'):
                print("   ✅ Flask app: موجود")
                self.assertIsNotNone(web_interface.app)
                
                # التحقق من المسارات المضافة
                routes = [rule.rule for rule in web_interface.app.url_map.iter_rules()]
                
                # التحقق من مسارات القرآن
                quran_routes = [route for route in routes if '/api/quran/' in route]
                if quran_routes:
                    print(f"   ✅ مسارات القرآن: {len(quran_routes)} مسار")
                    self.assertGreater(len(quran_routes), 0)
                else:
                    print("   ❌ مسارات القرآن: غير موجودة")
                
                # التحقق من مسارات المعجم
                lexicon_routes = [route for route in routes if '/api/lexicon/' in route]
                if lexicon_routes:
                    print(f"   ✅ مسارات المعجم: {len(lexicon_routes)} مسار")
                    self.assertGreater(len(lexicon_routes), 0)
                else:
                    print("   ❌ مسارات المعجم: غير موجودة")
            else:
                print("   ❌ Flask app: غير موجود")
                self.fail("Flask app غير موجود")
                
        except Exception as e:
            print(f"   ❌ فشل اختبار وظائف الواجهات: {e}")
            self.fail(f"فشل اختبار الوظائف: {e}")

def run_interface_integration_tests():
    """تشغيل اختبارات تكامل الواجهات."""
    
    print("🌟 النظام الثوري Baserah - اختبارات تكامل الواجهات")
    print("👨‍💻 المطور: باسل يحيى عبدالله")
    print("🧠 الأفكار الابتكارية: من إبداع باسل يحيى عبدالله")
    print("🤖 التطوير: بمساعدة وكيل ذكاء اصطناعي")
    print("=" * 80)
    
    # إنشاء مجموعة الاختبارات
    test_suite = unittest.TestLoader().loadTestsFromTestCase(InterfaceIntegrationTests)
    
    # تشغيل الاختبارات
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(test_suite)
    
    # تقرير النتائج
    print("\n" + "=" * 80)
    print("📊 تقرير نتائج تكامل الواجهات:")
    print(f"   🧪 إجمالي الاختبارات: {result.testsRun}")
    print(f"   ✅ نجح: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"   ❌ فشل: {len(result.failures)}")
    print(f"   🚨 أخطاء: {len(result.errors)}")
    
    # تحديد النجاح الإجمالي
    success_rate = ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100) if result.testsRun > 0 else 0
    
    print(f"\n🎯 معدل نجاح التكامل: {success_rate:.1f}%")
    
    if success_rate >= 90:
        print("🎉 التكامل مثالي!")
    elif success_rate >= 70:
        print("✅ التكامل جيد")
    else:
        print("⚠️ التكامل يحتاج تحسين")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_interface_integration_tests()
    sys.exit(0 if success else 1)
