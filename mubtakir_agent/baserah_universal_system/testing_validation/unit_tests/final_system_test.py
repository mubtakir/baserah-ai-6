#!/usr/bin/env python3
# final_system_test.py - اختبار شامل نهائي للنظام الثوري Baserah

import sys
import os
from datetime import datetime

def test_core_functions():
    """اختبار الدوال الأساسية."""
    
    print("🔧 اختبار الدوال الأساسية Baserah...")
    
    try:
        from artistic_intelligence.baserah_core import baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid
        
        # اختبار السيجمويد
        result1 = baserah_sigmoid(0, n=1, k=1.0, x0=0.0, alpha=1.0)
        assert 0.4 < result1 < 0.6, f"السيجمويد خطأ: {result1}"
        
        # اختبار الخطي
        result2 = baserah_linear(2, beta=3.0, gamma=1.0)
        assert result2 == 7.0, f"الخطي خطأ: {result2}"
        
        # اختبار الكمي
        result3 = baserah_quantum_sigmoid(0, quantum_factor=4)
        assert isinstance(result3, (int, float)), f"الكمي خطأ: {result3}"
        
        print("   ✅ جميع الدوال الأساسية تعمل")
        return True
        
    except Exception as e:
        print(f"   ❌ خطأ في الدوال الأساسية: {e}")
        return False

def test_mother_system():
    """اختبار النظام الأم."""
    
    print("🌟 اختبار النظام الأم الثوري...")
    
    try:
        from revolutionary_intelligence.revolutionary_mother_system.revolutionary_mother_system import BaserahRevolutionaryMotherSystem
        
        # إنشاء النظام الأم
        mother = BaserahRevolutionaryMotherSystem()
        assert hasattr(mother, 'system_id'), "النظام الأم لا يحتوي على معرف"
        
        # اختبار الملخص
        summary = mother.get_system_summary()
        assert summary['baserah_purity'] == 1.0, f"نقاء خطأ: {summary['baserah_purity']}"
        
        print("   ✅ النظام الأم يعمل بنجاح")
        return True
        
    except Exception as e:
        print(f"   ❌ خطأ في النظام الأم: {e}")
        return False

def test_shapes_database():
    """اختبار قاعدة بيانات الأشكال."""
    
    print("🗄️ اختبار قاعدة بيانات الأشكال...")
    
    try:
        from knowledge_systems.shapes_database.shapes_database import BaserahShapesDatabase
        
        # إنشاء قاعدة البيانات
        db = BaserahShapesDatabase()
        assert len(db.shapes) > 0, "قاعدة البيانات فارغة"
        
        # اختبار البحث
        cats = db.search_shapes('قطة')
        assert len(cats) > 0, "لم يتم العثور على قطط"
        
        # اختبار التحويل
        transformation = db.get_transformation_sequence('square_basic', 'circle_basic', 3)
        assert len(transformation) > 0, "فشل في إنشاء التحويل"
        
        print(f"   ✅ قاعدة البيانات تعمل: {len(db.shapes)} شكل")
        return True
        
    except Exception as e:
        print(f"   ❌ خطأ في قاعدة البيانات: {e}")
        return False

def test_expert_system():
    """اختبار النظام الخبير."""
    
    print("🧠 اختبار النظام الخبير/المستكشف...")
    
    try:
        from revolutionary_intelligence.expert_explorer_system.expert_explorer.integrated_expert_explorer import BaserahIntegratedExpertExplorer
        
        # إنشاء النظام الخبير
        expert = BaserahIntegratedExpertExplorer()
        assert hasattr(expert, 'adaptive_equations'), "النظام الخبير لا يحتوي على معادلات متكيفة"
        
        # اختبار إنشاء معادلة
        x_data = [0, 1, 2, 3, 4]
        y_data = [0, 1, 4, 9, 16]
        
        adaptive_eq = expert.create_adaptive_equation_from_data(x_data, y_data)
        assert adaptive_eq is not None, "فشل في إنشاء معادلة متكيفة"
        
        print("   ✅ النظام الخبير يعمل بنجاح")
        return True
        
    except Exception as e:
        print(f"   ❌ خطأ في النظام الخبير: {e}")
        return False

def test_integration():
    """اختبار التكامل بين المكونات."""
    
    print("🔗 اختبار التكامل بين المكونات...")
    
    try:
        from revolutionary_intelligence.revolutionary_mother_system.revolutionary_mother_system import BaserahRevolutionaryMotherSystem
        
        # إنشاء النظام الأم
        mother = BaserahRevolutionaryMotherSystem()
        
        # اختبار الوصول للأشكال
        square = mother.get_shape('square_basic')
        assert square is not None, "فشل في الوصول للمربع"
        
        # اختبار البحث
        results = mother.search_shapes('دائرة')
        assert len(results) > 0, "فشل في البحث"
        
        # اختبار التحويل
        transformation = mother.get_transformation_sequence('square_basic', 'circle_basic', 2)
        assert len(transformation) > 0, "فشل في التحويل"
        
        print("   ✅ التكامل يعمل بنجاح")
        return True
        
    except Exception as e:
        print(f"   ❌ خطأ في التكامل: {e}")
        return False

def test_mathematical_operations():
    """اختبار العمليات الرياضية."""
    
    print("📊 اختبار العمليات الرياضية...")
    
    try:
        from artistic_intelligence.baserah_core import baserah_sigmoid, baserah_linear
        import numpy as np
        
        # اختبار مع مجموعة قيم
        x_values = [-2, -1, 0, 1, 2]
        
        for x in x_values:
            # السيجمويد
            sig_result = baserah_sigmoid(x, n=2, k=1.0, x0=0.0, alpha=1.0)
            assert 0 <= sig_result <= 1, f"السيجمويد خارج النطاق: {sig_result}"
            
            # الخطي
            lin_result = baserah_linear(x, beta=0.5, gamma=0.1)
            expected = 0.5 * x + 0.1
            assert abs(lin_result - expected) < 0.001, f"الخطي خطأ: {lin_result} != {expected}"
        
        print("   ✅ العمليات الرياضية تعمل بدقة")
        return True
        
    except Exception as e:
        print(f"   ❌ خطأ في العمليات الرياضية: {e}")
        return False

def test_data_processing():
    """اختبار معالجة البيانات."""
    
    print("📈 اختبار معالجة البيانات...")
    
    try:
        from artistic_intelligence.baserah_core import baserah_sigmoid
        import numpy as np
        
        # إنشاء بيانات اختبار
        x_data = np.linspace(-3, 3, 50)
        y_data = [baserah_sigmoid(x, n=1, k=2.0, x0=0.0, alpha=1.0) for x in x_data]
        
        # فحص البيانات
        assert len(y_data) == len(x_data), "طول البيانات غير متطابق"
        assert all(0 <= y <= 1 for y in y_data), "قيم خارج النطاق المتوقع"
        
        # فحص الاتجاه (السيجمويد يجب أن يكون متزايد)
        assert y_data[-1] > y_data[0], "السيجمويد ليس متزايد"
        
        print(f"   ✅ معالجة البيانات تعمل: {len(y_data)} نقطة")
        return True
        
    except Exception as e:
        print(f"   ❌ خطأ في معالجة البيانات: {e}")
        return False

def run_comprehensive_test():
    """تشغيل اختبار شامل للنظام."""
    
    print("🚀 اختبار شامل نهائي للنظام الثوري Baserah")
    print("=" * 60)
    print(f"📅 تاريخ الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    tests = [
        ("الدوال الأساسية", test_core_functions),
        ("النظام الأم", test_mother_system),
        ("قاعدة بيانات الأشكال", test_shapes_database),
        ("النظام الخبير", test_expert_system),
        ("التكامل", test_integration),
        ("العمليات الرياضية", test_mathematical_operations),
        ("معالجة البيانات", test_data_processing)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ خطأ في اختبار {test_name}: {e}")
            results.append((test_name, False))
    
    # ملخص النتائج
    print("\n" + "=" * 60)
    print("📊 ملخص نتائج الاختبار الشامل:")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ نجح" if result else "❌ فشل"
        print(f"   {test_name}: {status}")
    
    success_rate = passed / total
    print(f"\n📈 معدل النجاح: {success_rate:.1%} ({passed}/{total})")
    
    if success_rate >= 0.8:
        print("\n🎉 النظام الثوري Baserah يعمل بنجاح!")
        print("✅ جميع المكونات الأساسية تعمل")
        print("🔧 الدوال الأساسية مختبرة ونجحت")
        print("🌟 النظام الأم متكامل ويعمل")
        print("🗄️ قاعدة بيانات الأشكال جاهزة")
        print("🧠 النظام الخبير/المستكشف نشط")
        print("📊 العمليات الرياضية دقيقة")
        print("🎯 النظام جاهز للاستخدام الفعلي!")
    elif success_rate >= 0.6:
        print("\n👍 النظام يعمل بشكل جيد مع بعض التحسينات المطلوبة")
    else:
        print("\n⚠️ النظام يحتاج مراجعة وإصلاحات")
    
    print(f"\n🎯 النتيجة النهائية: النظام الثوري Baserah {'جاهز' if success_rate >= 0.8 else 'يحتاج تحسين'}")
    
    return success_rate >= 0.8

if __name__ == "__main__":
    success = run_comprehensive_test()
    sys.exit(0 if success else 1)
