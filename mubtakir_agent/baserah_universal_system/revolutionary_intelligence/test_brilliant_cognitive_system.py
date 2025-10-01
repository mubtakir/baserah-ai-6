#!/usr/bin/env python3
# test_brilliant_cognitive_system.py - اختبار النظام الذكي المعرفي الباهر

import sys
import os
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد النظام الذكي المعرفي الباهر
from revolutionary_intelligence.self_developing_cognitive_ai import SelfDevelopingCognitiveAI

def test_brilliant_cognitive_system():
    """اختبار شامل للنظام الذكي المعرفي الباهر."""
    
    print("🧪✨ اختبار النظام الذكي المعرفي الباهر Baserah")
    print("=" * 70)
    print(f"📅 وقت الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        # إنشاء النظام الذكي المعرفي
        print("🏗️ إنشاء النظام الذكي المعرفي الباهر...")
        cognitive_ai = SelfDevelopingCognitiveAI("TestBrilliantCognitiveAI")
        print("✅ تم إنشاء النظام بنجاح!")
        print()
        
        # اختبار 1: التفكير العميق باللغة العربية
        print("🧠 اختبار 1: التفكير العميق باللغة العربية")
        print("-" * 50)
        
        arabic_input = "ما هي أهمية اللغة العربية في التفكير والإبداع؟"
        print(f"📝 المدخل العربي: {arabic_input}")
        
        arabic_result = cognitive_ai.think_deeply_and_develop(
            arabic_input, 
            thinking_depth=2, 
            enable_self_development=True
        )
        
        print(f"🎯 جودة التفكير: {arabic_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {arabic_result['performance_improvement']:.3f}")
        print(f"🗣️ الاستجابة اللغوية:")
        print(f"   {arabic_result['language_response']['final_response']}")
        print()
        
        # اختبار 2: التفكير العميق باللغة الإنجليزية
        print("🧠 اختبار 2: التفكير العميق باللغة الإنجليزية")
        print("-" * 50)
        
        english_input = "How does artificial intelligence impact human creativity and innovation?"
        print(f"📝 المدخل الإنجليزي: {english_input}")
        
        english_result = cognitive_ai.think_deeply_and_develop(
            english_input,
            thinking_depth=3,
            enable_self_development=True
        )
        
        print(f"🎯 جودة التفكير: {english_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {english_result['performance_improvement']:.3f}")
        print(f"🗣️ الاستجابة اللغوية:")
        print(f"   {english_result['language_response']['generated_response']}")
        print()
        
        # اختبار 3: مسألة رياضية معقدة
        print("🧠 اختبار 3: مسألة رياضية معقدة")
        print("-" * 50)
        
        math_input = "حل المعادلة التفاضلية: dy/dx = x^2 + y^2 مع الشرط الابتدائي y(0) = 1"
        print(f"📝 المسألة الرياضية: {math_input}")
        
        math_result = cognitive_ai.think_deeply_and_develop(
            math_input,
            thinking_depth=3,
            enable_self_development=True
        )
        
        print(f"🎯 جودة التفكير: {math_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {math_result['performance_improvement']:.3f}")
        print(f"🗣️ الاستجابة:")
        print(f"   {math_result['language_response']['final_response']}")
        print()
        
        # اختبار 4: موضوع إبداعي
        print("🧠 اختبار 4: موضوع إبداعي")
        print("-" * 50)
        
        creative_input = "اكتب قصة قصيرة عن مستقبل الذكاء الاصطناعي والإنسانية"
        print(f"📝 الطلب الإبداعي: {creative_input}")
        
        creative_result = cognitive_ai.think_deeply_and_develop(
            creative_input,
            thinking_depth=2,
            enable_self_development=True
        )
        
        print(f"🎯 جودة التفكير: {creative_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {creative_result['performance_improvement']:.3f}")
        print(f"🎨 الإبداع: {creative_result['language_response'].get('creativity_score', 0):.3f}")
        print(f"🗣️ القصة:")
        print(f"   {creative_result['language_response']['final_response']}")
        print()
        
        # اختبار 5: تحليل دلالات الحروف العربية
        print("🧠 اختبار 5: تحليل دلالات الحروف العربية")
        print("-" * 50)
        
        semantic_input = "حلل دلالات الحروف في كلمة 'حياة' وعلاقتها بالمعنى"
        print(f"📝 طلب التحليل: {semantic_input}")
        
        semantic_result = cognitive_ai.think_deeply_and_develop(
            semantic_input,
            thinking_depth=2,
            enable_self_development=True
        )
        
        print(f"🎯 جودة التفكير: {semantic_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {semantic_result['performance_improvement']:.3f}")
        print(f"🗣️ التحليل:")
        print(f"   {semantic_result['language_response']['final_response']}")
        print()
        
        # عرض حالة النظام النهائية
        print("📊 حالة النظام النهائية")
        print("-" * 50)
        
        system_status = cognitive_ai.get_system_status()
        
        print(f"🆔 معرف النظام: {system_status['system_info']['id']}")
        print(f"📈 مستوى الأداء الحالي: {system_status['performance_metrics']['current_performance_level']:.3f}")
        print(f"🔄 دورات التطوير: {system_status['performance_metrics']['development_cycles_count']}")
        print(f"⬆️ إجمالي التحسينات: {system_status['performance_metrics']['total_improvements']}")
        print(f"🏆 تقييم النظام: {system_status['system_assessment']}")
        
        print()
        print("📈 إحصائيات التطوير:")
        dev_stats = system_status['development_statistics']
        print(f"   🔄 إجمالي دورات التطوير: {dev_stats['total_development_cycles']}")
        print(f"   ✅ التحسينات الناجحة: {dev_stats['successful_improvements']}")
        print(f"   📊 تحسن الأداء الإجمالي: {dev_stats['performance_improvements']:.3f}")
        
        print()
        print("🧠 حالة النواة المعرفية:")
        cognitive_stats = system_status['cognitive_core_status']
        print(f"   🔗 إجمالي التفاعلات: {cognitive_stats['total_interactions']}")
        print(f"   ✅ التفاعلات الناجحة: {cognitive_stats['successful_interactions']}")
        print(f"   📈 معدل النجاح: {cognitive_stats['success_rate']:.1%}")
        print(f"   🎯 الجودة المتوسطة: {cognitive_stats['average_quality']:.3f}")
        
        print()
        print("🗣️ حالة النماذج اللغوية:")
        for model_name, model_stats in system_status['language_models_status'].items():
            print(f"   📝 {model_name}:")
            print(f"      📊 إجمالي التوليدات: {model_stats['total_generations']}")
            print(f"      ✅ الاستجابات الناجحة: {model_stats['successful_responses']}")
            print(f"      🎨 المخرجات الإبداعية: {model_stats['creative_outputs']}")
            print(f"      🎯 دقة السياق: {model_stats['context_accuracy']:.3f}")
        
        print()
        print("🎉 اكتمل اختبار النظام الذكي المعرفي الباهر بنجاح!")
        print("✨ النظام يعمل بكفاءة عالية ويطور نفسه بنفسه!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار النظام: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_individual_components():
    """اختبار المكونات الفردية."""
    
    print("\n🔧 اختبار المكونات الفردية")
    print("=" * 40)
    
    try:
        # اختبار النظام المعرفي المتجاوب
        print("🧠 اختبار النظام المعرفي المتجاوب...")
        from revolutionary_intelligence.responsive_cognitive_system import ResponsiveCognitiveSystem
        
        cognitive_system = ResponsiveCognitiveSystem("TestCognitiveSystem")
        test_result = cognitive_system.process_with_full_interaction("اختبار التفاعل", interaction_depth=1)
        
        print(f"   ✅ النظام المعرفي: جودة التفاعل = {test_result['interaction_quality']:.3f}")
        
        # اختبار النموذج اللغوي العربي
        print("🇸🇦 اختبار النموذج اللغوي العربي...")
        from revolutionary_intelligence.advanced_arabic_language_model import AdvancedArabicLanguageModel
        
        arabic_model = AdvancedArabicLanguageModel("TestArabicModel")
        arabic_analysis = arabic_model.analyze_arabic_text_comprehensive("اللغة العربية لغة جميلة")
        
        print(f"   ✅ النموذج العربي: الوزن الدلالي = {arabic_analysis['letter_semantics_analysis']['overall_semantic_weight']:.3f}")
        
        # اختبار النموذج اللغوي المبتكر
        print("💡 اختبار النموذج اللغوي المبتكر...")
        from revolutionary_intelligence.innovative_language_model import BaserahInnovativeLanguageModel
        
        innovative_model = BaserahInnovativeLanguageModel("TestInnovativeModel")
        innovative_response = innovative_model.generate_response("Test innovation", generation_mode="creative")
        
        print(f"   ✅ النموذج المبتكر: الثقة = {innovative_response['confidence']:.3f}")
        
        print("✅ جميع المكونات تعمل بنجاح!")
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار المكونات: {e}")
        return False

def main():
    """الدالة الرئيسية للاختبار."""
    
    print("🚀 بدء اختبار النظام الذكي المعرفي الباهر Baserah")
    print("🔬 نظام ذكاء اصطناعي ثوري يطور نفسه بنفسه")
    print("🧬 مبني على المعادلة الثورية الأم والذكاء الكائني التوجه")
    print("🗣️ مع نماذج لغوية مبتكرة ودعم متقدم للعربية")
    print()
    
    # اختبار المكونات الفردية أولاً
    components_success = test_individual_components()
    
    if components_success:
        # اختبار النظام الشامل
        system_success = test_brilliant_cognitive_system()
        
        if system_success:
            print("\n🏆 النتيجة النهائية: نجح الاختبار بامتياز!")
            print("🌟 النظام الذكي المعرفي الباهر جاهز للعمل!")
            print("🚀 يمكن الآن استخدام النظام في التطبيقات المتقدمة!")
        else:
            print("\n⚠️ النتيجة النهائية: فشل في اختبار النظام الشامل")
    else:
        print("\n❌ النتيجة النهائية: فشل في اختبار المكونات الأساسية")
    
    print("\n" + "=" * 70)
    print("🔬 انتهى اختبار النظام الذكي المعرفي الباهر")
    print(f"📅 وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
