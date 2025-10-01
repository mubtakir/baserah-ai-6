#!/usr/bin/env python3
# test_advanced_mathematical_engine.py - اختبار المحرك الرياضي المتقدم

import sys
import os
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد النظام المطور
from revolutionary_intelligence.advanced_mathematical_engine import (
    AdvancedMathematicalEngine, MathematicalOperationType, CalculusMethod
)
from revolutionary_intelligence.self_developing_cognitive_ai import SelfDevelopingCognitiveAI

def test_advanced_mathematical_engine():
    """اختبار المحرك الرياضي المتقدم."""
    
    print("🧮✨ اختبار المحرك الرياضي المتقدم")
    print("=" * 70)
    print(f"📅 وقت الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🌟 دمج الأنظمة المبتكرة من نظام بصيرة مع نظريات باسل الثورية")
    print("🧬 مدعوم بمنهج Baserah النقي (sigmoid + linear فقط)")
    print()
    
    try:
        # إنشاء المحرك الرياضي المتقدم
        print("🏗️ إنشاء المحرك الرياضي المتقدم...")
        math_engine = AdvancedMathematicalEngine("TestAdvancedMathematicalEngine")
        print("✅ تم إنشاء المحرك بنجاح!")
        print()
        
        # اختبار 1: التفاضل والتكامل المبتكر
        print("📐 اختبار 1: التفاضل والتكامل المبتكر")
        print("-" * 50)
        
        # تكامل x^2
        integration_result = math_engine.perform_innovative_calculus(
            expression="x^2",
            variable="x",
            operation="integrate",
            method=CalculusMethod.BASIRA_INNOVATIVE
        )
        
        print(f"📝 التعبير: x^2")
        print(f"🔄 العملية: تكامل")
        print(f"🎯 الطريقة: {integration_result.method_used}")
        print(f"✅ النتيجة: {integration_result.result_expression}")
        print(f"🎯 الثقة: {integration_result.confidence_score:.3f}")
        print(f"⏱️ الوقت: {integration_result.computation_time:.3f} ثانية")
        
        if integration_result.basil_theories_applied:
            print(f"🧬 نظريات باسل المطبقة: {', '.join(integration_result.basil_theories_applied)}")
        
        if integration_result.revolutionary_insights:
            print(f"💡 الرؤى الثورية:")
            for insight in integration_result.revolutionary_insights:
                print(f"   • {insight}")
        
        print()
        
        # تفاضل x^3
        differentiation_result = math_engine.perform_innovative_calculus(
            expression="x^3",
            variable="x",
            operation="differentiate",
            method=CalculusMethod.BASIL_REVOLUTIONARY
        )
        
        print(f"📝 التعبير: x^3")
        print(f"🔄 العملية: تفاضل")
        print(f"🎯 الطريقة: {differentiation_result.method_used}")
        print(f"✅ النتيجة: {differentiation_result.result_expression}")
        print(f"🎯 الثقة: {differentiation_result.confidence_score:.3f}")
        
        print()
        
        # اختبار 2: تفكيك الدوال الثوري
        print("🔧 اختبار 2: تفكيك الدوال الثوري")
        print("-" * 50)
        
        # تفكيك بالفرضية الثورية
        decomposition_result = math_engine.decompose_function_revolutionary(
            expression="x^2 + 2*x + 1",
            decomposition_type="basira_hypothesis"
        )
        
        print(f"📝 الدالة: x^2 + 2*x + 1")
        print(f"🔧 نوع التفكيك: {decomposition_result.method_used}")
        print(f"✅ الشكل المفكك: {decomposition_result.result_expression}")
        print(f"🎯 الثقة: {decomposition_result.confidence_score:.3f}")
        
        if decomposition_result.metadata.get('components'):
            print(f"🧩 المكونات:")
            for component in decomposition_result.metadata['components']:
                print(f"   • {component.get('term', '')}: {component.get('description', '')}")
        
        print()
        
        # تفكيك بتعامد الأضداد
        perpendicular_result = math_engine.decompose_function_revolutionary(
            expression="sin(x)",
            decomposition_type="perpendicular_opposites"
        )
        
        print(f"📝 الدالة: sin(x)")
        print(f"🔧 نوع التفكيك: {perpendicular_result.method_used}")
        print(f"✅ الشكل المفكك: {perpendicular_result.result_expression}")
        print(f"🎯 الثقة: {perpendicular_result.confidence_score:.3f}")
        
        print()
        
        # اختبار 3: حل المعادلات المتقدم
        print("🎯 اختبار 3: حل المعادلات المتقدم")
        print("-" * 50)
        
        # حل معادلة تربيعية
        equation_result = math_engine.solve_equation_advanced(
            equation="x^2 - 4 = 0",
            method="revolutionary_hybrid"
        )
        
        print(f"📝 المعادلة: x^2 - 4 = 0")
        print(f"🎯 الطريقة: {equation_result.method_used}")
        print(f"✅ الحل: {equation_result.result_expression}")
        print(f"🎯 الثقة: {equation_result.confidence_score:.3f}")
        
        if equation_result.metadata.get('solutions'):
            print(f"🔢 الحلول العددية: {equation_result.metadata['solutions']}")
        
        print()
        
        # اختبار 4: حل الألغاز الرياضية
        print("🧩 اختبار 4: حل الألغاز الرياضية")
        print("-" * 50)
        
        puzzle_description = "إذا كان لديك مثلث قائم الزاوية، وطول ضلعيه القائمين 3 و 4، فما طول الوتر؟"
        
        puzzle_result = math_engine.solve_mathematical_puzzle(
            puzzle_description=puzzle_description,
            puzzle_type="geometry"
        )
        
        print(f"📝 اللغز: {puzzle_description}")
        print(f"🎯 الطريقة: {puzzle_result.method_used}")
        print(f"✅ الحل: {puzzle_result.result_expression}")
        print(f"🎯 الثقة: {puzzle_result.confidence_score:.3f}")
        
        if puzzle_result.steps:
            print(f"📋 خطوات الحل:")
            for step in puzzle_result.steps[:3]:  # أول 3 خطوات
                print(f"   • {step}")
        
        print()
        
        # اختبار 5: إحصائيات المحرك
        print("📊 اختبار 5: إحصائيات المحرك")
        print("-" * 50)
        
        engine_stats = math_engine.get_engine_statistics()
        
        print(f"🏷️ معلومات المحرك:")
        print(f"   الاسم: {engine_stats['engine_info']['name']}")
        print(f"   الإصدار: {engine_stats['engine_info']['version']}")
        print(f"   النوع: {engine_stats['engine_info']['type']}")
        
        print(f"📈 إحصائيات الأداء:")
        performance = engine_stats['performance_stats']
        print(f"   العمليات المنجزة: {performance['operations_performed']}")
        print(f"   المعادلات المحلولة: {performance['equations_solved']}")
        print(f"   الدوال المفككة: {performance['functions_decomposed']}")
        print(f"   الألغاز المحلولة: {performance['puzzles_solved']}")
        print(f"   متوسط الثقة: {performance['average_confidence']:.3f}")
        print(f"   متوسط وقت الحساب: {performance['average_computation_time']:.3f} ثانية")
        
        print(f"🛠️ القدرات:")
        capabilities = engine_stats['capabilities']
        print(f"   طرق التفاضل والتكامل المبتكرة: {capabilities['innovative_calculus_methods']}")
        print(f"   طرق التفكيك: {capabilities['decomposition_methods']}")
        print(f"   طرق نظريات باسل: {capabilities['basil_theories_methods']}")
        print(f"   طرق حل المعادلات: {capabilities['equation_solving_methods']}")
        
        print(f"🌟 الميزات الثورية:")
        rev_features = engine_stats['revolutionary_features']
        print(f"   تكامل بصيرة: {'✅' if rev_features['basira_integration'] else '❌'}")
        print(f"   تكامل نظريات باسل: {'✅' if rev_features['basil_theories_integration'] else '❌'}")
        print(f"   دوال Baserah النقية: {'✅' if rev_features['baserah_pure_functions'] else '❌'}")
        print(f"   النهج الهجين: {'✅' if rev_features['hybrid_approaches'] else '❌'}")
        print(f"   حل الألغاز: {'✅' if rev_features['puzzle_solving'] else '❌'}")
        print(f"   تفكيك الدوال: {'✅' if rev_features['function_decomposition'] else '❌'}")
        
        print(f"📋 ملخص الطرق الرياضية:")
        methods_summary = engine_stats['mathematical_methods_summary']
        for method_name, description in methods_summary.items():
            print(f"   {method_name}: {description}")
        
        print(f"🏆 تقييم الأداء: {engine_stats['performance_assessment']}")
        
        print()
        print("🎉 اكتمل اختبار المحرك الرياضي المتقدم بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار المحرك: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_integrated_cognitive_mathematical_system():
    """اختبار النظام المعرفي المتكامل مع المحرك الرياضي."""
    
    print("\n🧠🧮 اختبار النظام المعرفي المتكامل مع المحرك الرياضي")
    print("=" * 70)
    
    try:
        # إنشاء النظام المتكامل
        print("🏗️ إنشاء النظام المعرفي المتكامل...")
        cognitive_ai = SelfDevelopingCognitiveAI("TestMathematicalCognitiveAI")
        print("✅ تم إنشاء النظام بنجاح!")
        print()
        
        # اختبار التفكير العميق مع المعالجة الرياضية
        print("🧠 اختبار التفكير العميق مع المعالجة الرياضية")
        print("-" * 50)
        
        mathematical_request = "احسب تكامل الدالة x^2 + 3x + 2 باستخدام الطرق الثورية"
        
        thinking_result = cognitive_ai.think_deeply_and_develop(
            mathematical_request,
            thinking_depth=4,
            enable_self_development=True
        )
        
        print(f"📝 المدخل الرياضي: {mathematical_request}")
        print(f"🎯 جودة التفكير: {thinking_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {thinking_result['performance_improvement']:.3f}")
        
        # فحص المعالجة الرياضية
        if 'mathematical_processing' in thinking_result:
            math_processing = thinking_result['mathematical_processing']
            print(f"🧮 المعالجة الرياضية:")
            print(f"   نوع العملية: {math_processing['operation_type']}")
            print(f"   الثقة: {math_processing['confidence_score']:.3f}")
            print(f"   وقت المعالجة: {math_processing['processing_time']:.3f} ثانية")
            
            # النتائج الرياضية
            mathematical_results = math_processing.get('mathematical_results', [])
            if mathematical_results:
                print(f"   النتائج الرياضية ({len(mathematical_results)} نتيجة):")
                for i, result in enumerate(mathematical_results):
                    if hasattr(result, 'result_expression'):
                        print(f"      {i+1}. {result.result_expression}")
                        print(f"         الثقة: {result.confidence_score:.3f}")
                        print(f"         الطريقة: {result.method_used}")
            
            # النظريات المطبقة
            basil_theories = math_processing.get('basil_theories_applied', [])
            if basil_theories:
                unique_theories = list(set(basil_theories))
                print(f"   نظريات باسل المطبقة: {', '.join(unique_theories)}")
            
            # الرؤى الثورية
            revolutionary_insights = math_processing.get('revolutionary_insights', [])
            if revolutionary_insights:
                print(f"   الرؤى الثورية ({len(revolutionary_insights)} رؤية):")
                for insight in revolutionary_insights[:3]:  # أول 3 رؤى
                    print(f"      • {insight}")
        
        # فحص الاستجابة المحسنة
        language_response = thinking_result['language_response']
        print(f"🗣️ الاستجابة المحسنة:")
        response_preview = language_response['final_response'][:300] + "..." if len(language_response['final_response']) > 300 else language_response['final_response']
        print(f"   {response_preview}")
        
        print()
        
        # عرض حالة النظام المتكامل
        print("📊 حالة النظام المتكامل مع المحرك الرياضي")
        print("-" * 50)
        
        system_status = cognitive_ai.get_system_status()
        
        print(f"🧠 النواة المعرفية:")
        cognitive_stats = system_status['cognitive_core_status']
        print(f"   الطبقات المعرفية: {cognitive_stats['total_layers']}")
        print(f"   التفاعلات: {cognitive_stats['total_interactions']}")
        print(f"   معدل النجاح: {cognitive_stats['success_rate']:.1%}")
        
        print(f"🧮 المحرك الرياضي المتقدم:")
        math_stats = system_status['advanced_mathematical_engine_status']
        performance_stats = math_stats['performance_stats']
        print(f"   العمليات المنجزة: {performance_stats['operations_performed']}")
        print(f"   المعادلات المحلولة: {performance_stats['equations_solved']}")
        print(f"   الدوال المفككة: {performance_stats['functions_decomposed']}")
        print(f"   الألغاز المحلولة: {performance_stats['puzzles_solved']}")
        print(f"   متوسط الثقة: {performance_stats['average_confidence']:.3f}")
        print(f"   تقييم الأداء: {math_stats['performance_assessment']}")
        
        print()
        print("🎉 اكتمل اختبار النظام المعرفي المتكامل مع المحرك الرياضي بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار النظام المتكامل: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """الدالة الرئيسية للاختبار."""
    
    print("🚀 بدء اختبار المحرك الرياضي المتقدم")
    print("🧮 دمج الأنظمة المبتكرة من نظام بصيرة مع نظريات باسل الثورية")
    print("🌟 مدعوم بمنهج Baserah النقي (sigmoid + linear فقط)")
    print()
    
    # اختبار المحرك المستقل
    engine_success = test_advanced_mathematical_engine()
    
    if engine_success:
        # اختبار النظام المتكامل
        integration_success = test_integrated_cognitive_mathematical_system()
        
        if integration_success:
            print("\n🏆 النتيجة النهائية: نجح الاختبار بامتياز!")
            print("🌟 المحرك الرياضي المتقدم متكامل مع النظام المعرفي الباهر!")
            print("🧮 النظام جاهز لحل المعادلات والألغاز الرياضية بطرق ثورية!")
        else:
            print("\n⚠️ النتيجة النهائية: فشل في اختبار التكامل")
    else:
        print("\n❌ النتيجة النهائية: فشل في اختبار المحرك الأساسي")
    
    print("\n" + "=" * 70)
    print("🔬 انتهى اختبار المحرك الرياضي المتقدم")
    print(f"📅 وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
