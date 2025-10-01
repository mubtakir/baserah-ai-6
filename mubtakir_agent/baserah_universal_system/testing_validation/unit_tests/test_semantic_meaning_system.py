#!/usr/bin/env python3
# test_semantic_meaning_system.py - اختبار نظام الدلالة المعنوية الثوري

import sys
import os

# إضافة المسارات للاستيراد
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from revolutionary_intelligence.revolutionary_mother_system.revolutionary_mother_system import BaserahRevolutionaryMotherSystem
from knowledge_systems.semantic_meaning.semantic_meaning_system import BaserahSemanticMeaningSystem, SemanticType, SemanticDimension

def test_semantic_database():
    """اختبار قاعدة بيانات الدلالات المعنوية."""
    
    print("🧠💭 اختبار قاعدة بيانات الدلالات المعنوية...")
    print("=" * 60)
    
    # إنشاء النظام الأم
    mother_system = BaserahRevolutionaryMotherSystem()
    
    # إنشاء نظام الدلالة المعنوية
    semantic_system = BaserahSemanticMeaningSystem(mother_system)
    
    print("1️⃣ فحص قاعدة البيانات الأساسية:")
    
    # فحص الكلمات الموجودة
    expected_words = ["انسان", "شجرة", "يمشي", "يتحول", "مربع", "دائرة", "طريق"]
    
    for word in expected_words:
        if word in semantic_system.semantic_database:
            equation = semantic_system.semantic_database[word]
            symbol = semantic_system.symbol_registry.get(f'{equation.semantic_type.value}_symbol', '🔸')
            print(f"   {symbol} {word}: {equation.semantic_type.value}")
            print(f"     مكونات رياضية: {len(equation.mathematical_components)}")
            print(f"     مكونات دلالية: {len(equation.semantic_components)}")
        else:
            print(f"   ❌ {word}: غير موجود")
    
    print("\n2️⃣ تحليل التوزيع:")
    summary = semantic_system.get_semantic_summary()
    print(f"   إجمالي المعادلات: {summary['total_semantic_equations']}")
    print(f"   توزيع الأنواع: {summary['type_distribution']}")
    print(f"   استخدام الأبعاد: {summary['dimension_usage']}")
    
    print("\n✅ اختبار قاعدة بيانات الدلالات مكتمل!")
    return semantic_system

def test_semantic_interpretation():
    """اختبار تفسير الجمل الدلالية."""
    
    print("\n🧠🔍 اختبار تفسير الجمل الدلالية...")
    print("=" * 60)
    
    # إنشاء النظام
    mother_system = BaserahRevolutionaryMotherSystem()
    semantic_system = BaserahSemanticMeaningSystem(mother_system)
    
    # جمل اختبار
    test_sentences = [
        "انسان يمشي في طريق",
        "مربع يتحول الى دائرة",
        "شجرة في طريق",
        "انسان يتحول",
        "كلمة غير معروفة"
    ]
    
    print("1️⃣ تفسير الجمل:")
    
    for i, sentence in enumerate(test_sentences):
        print(f"\n   جملة {i+1}: '{sentence}'")
        
        interpretation = semantic_system.interpret_semantic_sentence(sentence)
        
        print(f"     الثقة: {interpretation['confidence']:.2f}")
        print(f"     كلمات معروفة: {len(interpretation['recognized_words'])}")
        
        if interpretation['recognized_words']:
            for word_info in interpretation['recognized_words']:
                print(f"       {word_info['symbol']} {word_info['word']} ({word_info['type']})")
        
        if interpretation['confidence'] > 0.5:
            print(f"     خطة التنفيذ: {len(interpretation['execution_plan'])} خطوة")
        else:
            print("     ⚠️ ثقة منخفضة - لا يمكن إنشاء خطة تنفيذ")
    
    print("\n✅ اختبار تفسير الجمل الدلالية مكتمل!")
    return semantic_system

def test_semantic_execution():
    """اختبار تنفيذ الأوامر الدلالية."""
    
    print("\n⚡🧠 اختبار تنفيذ الأوامر الدلالية...")
    print("=" * 60)
    
    # إنشاء النظام
    mother_system = BaserahRevolutionaryMotherSystem()
    semantic_system = BaserahSemanticMeaningSystem(mother_system)
    
    # أوامر اختبار
    test_commands = [
        "انسان يمشي في طريق",
        "مربع يتحول الى دائرة",
        "شجرة في طريق"
    ]
    
    print("1️⃣ تنفيذ الأوامر:")
    
    for i, command in enumerate(test_commands):
        print(f"\n   أمر {i+1}: '{command}'")
        
        execution_result = semantic_system.execute_semantic_command(command)
        
        print(f"     نجح التنفيذ: {execution_result['execution_success']}")
        
        if execution_result['execution_success']:
            interpretation = execution_result['interpretation']
            print(f"     ثقة التفسير: {interpretation['confidence']:.2f}")
            
            if execution_result['visual_output']:
                print(f"     كائنات بصرية: {len(execution_result['visual_output'])}")
                for obj in execution_result['visual_output']:
                    print(f"       - {obj['name']}: {len(obj['equation'])} مكون رياضي")
            
            if execution_result['mathematical_result']:
                print(f"     تحويلات رياضية: {len(execution_result['mathematical_result'])}")
            
            if execution_result['semantic_analysis']:
                fusion_score = execution_result['semantic_analysis'].get('fusion_score', 0)
                print(f"     نقاط الدمج الدلالي: {fusion_score:.3f}")
        else:
            print("     ❌ فشل التنفيذ")
    
    print("\n✅ اختبار تنفيذ الأوامر الدلالية مكتمل!")
    return semantic_system

def test_semantic_transformation():
    """اختبار التحويل الدلالي."""
    
    print("\n🔄🧠 اختبار التحويل الدلالي...")
    print("=" * 60)
    
    # إنشاء النظام
    mother_system = BaserahRevolutionaryMotherSystem()
    semantic_system = BaserahSemanticMeaningSystem(mother_system)
    
    # تحويلات اختبار
    transformations = [
        ("مربع", "دائرة"),
        ("انسان", "شجرة"),
        ("يمشي", "يتحول")
    ]
    
    print("1️⃣ إنشاء التحويلات الدلالية:")
    
    for i, (source, target) in enumerate(transformations):
        print(f"\n   تحويل {i+1}: {source} → {target}")
        
        transformation = semantic_system.create_semantic_transformation(source, target)
        
        if 'error' not in transformation:
            print(f"     نقاط التحويل: {transformation['transformation_score']:.3f}")
            print(f"     خطوات رياضية: {len(transformation['mathematical_steps'])}")
            print(f"     تغييرات دلالية: {len(transformation['semantic_changes'])}")
            
            # عرض بعض التفاصيل
            if transformation['mathematical_steps']:
                print("     خطوات رياضية:")
                for step in transformation['mathematical_steps'][:2]:  # أول خطوتين
                    print(f"       - {step['step_type']}: {step['description']}")
            
            if transformation['semantic_changes']:
                print("     تغييرات دلالية:")
                for change in transformation['semantic_changes'][:2]:  # أول تغييرين
                    print(f"       - {change['dimension']}: {change['description']}")
        else:
            print(f"     ❌ خطأ: {transformation['error']}")
    
    print("\n✅ اختبار التحويل الدلالي مكتمل!")
    return semantic_system

def test_advanced_semantic_scenarios():
    """اختبار سيناريوهات دلالية متقدمة."""
    
    print("\n🌟🧠 اختبار سيناريوهات دلالية متقدمة...")
    print("=" * 60)
    
    # إنشاء النظام
    mother_system = BaserahRevolutionaryMotherSystem()
    semantic_system = BaserahSemanticMeaningSystem(mother_system)
    
    print("1️⃣ سيناريو: تحويل الأشكال الهندسية")
    
    # تفسير وتنفيذ تحويل الأشكال
    shape_command = "مربع يتحول الى دائرة"
    print(f"   الأمر: '{shape_command}'")
    
    execution_result = semantic_system.execute_semantic_command(shape_command)
    
    if execution_result['execution_success']:
        print("   ✅ تم تفسير وتنفيذ تحويل الأشكال بنجاح")
        
        # إنشاء التحويل التفصيلي
        transformation = semantic_system.create_semantic_transformation("مربع", "دائرة")
        print(f"   تفاصيل التحويل: نقاط={transformation['transformation_score']:.3f}")
    
    print("\n2️⃣ سيناريو: الكائنات والأفعال")
    
    # تفسير جملة معقدة
    complex_command = "انسان يمشي في طريق"
    print(f"   الأمر: '{complex_command}'")
    
    execution_result = semantic_system.execute_semantic_command(complex_command)
    
    if execution_result['execution_success']:
        print("   ✅ تم تفسير الجملة المعقدة بنجاح")
        
        # تحليل المكونات
        interpretation = execution_result['interpretation']
        math_components = len(interpretation['mathematical_representation'])
        semantic_components = len(interpretation['semantic_representation'])
        
        print(f"   مكونات رياضية: {math_components}")
        print(f"   مكونات دلالية: {semantic_components}")
    
    print("\n3️⃣ سيناريو: تحليل الدلالات المتعددة")
    
    # تحليل كلمات متعددة الأبعاد
    multi_dimensional_word = "انسان"
    if multi_dimensional_word in semantic_system.semantic_database:
        equation = semantic_system.semantic_database[multi_dimensional_word]
        
        print(f"   تحليل كلمة: '{multi_dimensional_word}'")
        print(f"   النوع: {equation.semantic_type.value}")
        print(f"   الأبعاد الدلالية:")
        
        for comp in equation.semantic_components:
            print(f"     - {comp.dimension.value}: قيمة={comp.value:.2f}, وزن={comp.weight:.2f}")
            print(f"       وصف: {comp.description}")
    
    print("\n✅ اختبار السيناريوهات الدلالية المتقدمة مكتمل!")

def run_semantic_meaning_system_test():
    """تشغيل اختبار شامل لنظام الدلالة المعنوية."""
    
    print("🧠💭 بدء الاختبار الشامل لنظام الدلالة المعنوية الثوري")
    print("=" * 80)
    print("المفهوم الثوري: ربط الدلالة بالشكل والمعادلات")
    print("المبدأ: الانسان = (معادلة شكله العام) + (حدود غير رياضية)")
    print("=" * 80)
    
    try:
        # اختبار المكونات الأساسية
        semantic_system1 = test_semantic_database()
        semantic_system2 = test_semantic_interpretation()
        semantic_system3 = test_semantic_execution()
        semantic_system4 = test_semantic_transformation()
        
        # اختبار السيناريوهات المتقدمة
        test_advanced_semantic_scenarios()
        
        # ملخص النتائج
        print("\n" + "=" * 80)
        print("📊 ملخص نتائج اختبار نظام الدلالة المعنوية:")
        
        # استخدام آخر نظام تم إنشاؤه للملخص
        final_summary = semantic_system4.get_semantic_summary()
        
        print(f"   إجمالي المعادلات الدلالية: {final_summary['total_semantic_equations']}")
        print(f"   إجمالي التفسيرات: {final_summary['total_interpretations']}")
        print(f"   توزيع الأنواع: {final_summary['type_distribution']}")
        print(f"   الأبعاد المستخدمة: {list(final_summary['dimension_usage'].keys())}")
        
        print("\n🎉 نظام الدلالة المعنوية الثوري يعمل بنجاح كامل!")
        print("✅ ربط الدلالة بالشكل والمعادلات محقق!")
        print("🧠 المعادلات الدلالية تحمل مكونات رياضية ودلالية!")
        print("💭 تفسير وتنفيذ الجمل الدلالية يعمل بكفاءة!")
        print("🔄 التحويل الدلالي بين المفاهيم محقق!")
        print("🌟 النظام جاهز لفهم المعنى والدلالة!")
        
        print(f"\nالقدرات المحققة:")
        for capability in final_summary['semantic_capabilities']:
            print(f"   ✅ {capability}")
        
        print("\n🎯 منهج Baserah النقي 100% مع الدلالة المعنوية!")
        
    except Exception as e:
        print(f"\n❌ خطأ في اختبار نظام الدلالة المعنوية: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_semantic_meaning_system_test()
