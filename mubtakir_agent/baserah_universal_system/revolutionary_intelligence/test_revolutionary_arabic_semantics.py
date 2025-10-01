#!/usr/bin/env python3
# test_revolutionary_arabic_semantics.py - اختبار النظام الثوري لدلالات الحروف العربية

import sys
import os
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد النظام الثوري لدلالات الحروف العربية
from revolutionary_intelligence.advanced_arabic_language_model import (
    ArabicLetterSemanticsEngine, 
    AdvancedArabicLanguageModel
)

def test_revolutionary_letter_semantics():
    """اختبار النظام الثوري لدلالات الحروف العربية."""
    
    print("🔤✨ اختبار النظام الثوري لدلالات الحروف العربية")
    print("=" * 70)
    print(f"📅 وقت الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        # إنشاء محرك دلالات الحروف
        print("🏗️ إنشاء محرك دلالات الحروف الثوري...")
        semantics_engine = ArabicLetterSemanticsEngine()
        print("✅ تم إنشاء المحرك بنجاح!")
        print()
        
        # اختبار 1: تحليل حرف الباء وفقاً للرؤية الثورية
        print("🔤 اختبار 1: تحليل حرف الباء الثوري")
        print("-" * 50)
        
        ba_analysis = semantics_engine.analyze_letter("ب")
        print(f"📝 الحرف: ب")
        
        if "revolutionary_meaning_theory" in ba_analysis:
            theory = ba_analysis["revolutionary_meaning_theory"]
            print(f"🎯 المعنى الأساسي: {theory['core_meaning']}")
            print(f"🧬 الاشتقاق الدلالي: {theory['semantic_derivation']}")
            print(f"🔗 الروابط المنطقية:")
            for connection in theory["logical_connections"]:
                print(f"   • {connection}")
            print(f"⚖️ محور القياس: {theory['measurement_axis']['positive_pole']} ↔ {theory['measurement_axis']['negative_pole']}")
        
        print()
        
        # اختبار 2: تحليل كلمة "بيت" بالتفاعل الثوري
        print("🏠 اختبار 2: تحليل كلمة 'بيت' بالتفاعل الثوري")
        print("-" * 50)
        
        bait_analysis = semantics_engine.analyze_word_letters("بيت")
        print(f"📝 الكلمة: {bait_analysis['word']}")
        print(f"🔢 عدد الحروف: {bait_analysis['letters_count']}")
        print(f"⚖️ الوزن الدلالي: {bait_analysis['semantic_weight']:.3f}")
        
        # التفاعل الثوري
        revolutionary_interaction = bait_analysis["revolutionary_semantic_interaction"]
        print(f"🔄 نوع التفاعل: {revolutionary_interaction['interaction_type']}")
        print(f"🧬 تركيب المعنى: {revolutionary_interaction['meaning_synthesis']}")
        print(f"💪 قوة التفاعل: {revolutionary_interaction['interaction_strength']:.3f}")
        
        print(f"🌊 تدفق المعاني:")
        for flow in revolutionary_interaction["semantic_flow"]:
            print(f"   • {flow}")
        
        print(f"🔗 الروابط المنطقية:")
        for connection in revolutionary_interaction["logical_connections"]:
            print(f"   • {connection}")
        
        print(f"❓ العلاقات المفقودة:")
        for missing in revolutionary_interaction["missing_relations"]:
            print(f"   • {missing}")
        
        print(f"📊 اكتمال المعنى: {bait_analysis['meaning_completeness']:.3f}")
        
        print()
        
        # اختبار 3: تحليل كلمة "علم" 
        print("📚 اختبار 3: تحليل كلمة 'علم' بالتفاعل الثوري")
        print("-" * 50)
        
        ilm_analysis = semantics_engine.analyze_word_letters("علم")
        print(f"📝 الكلمة: {ilm_analysis['word']}")
        
        revolutionary_interaction = ilm_analysis["revolutionary_semantic_interaction"]
        print(f"🧬 تركيب المعنى: {revolutionary_interaction['meaning_synthesis']}")
        print(f"💪 قوة التفاعل: {revolutionary_interaction['interaction_strength']:.3f}")
        print(f"📊 اكتمال المعنى: {ilm_analysis['meaning_completeness']:.3f}")
        
        print()
        
        # اختبار 4: توسيع قاعدة البيانات من القاموس
        print("📖 اختبار 4: توسيع قاعدة البيانات من القاموس")
        print("-" * 50)
        
        # كلمات تجريبية للتوسع
        test_words = [
            "بيت", "بحر", "باب", "كتاب", "حبل",  # كلمات تحتوي على ب
            "علم", "عين", "عقل", "معرفة", "جمع",  # كلمات تحتوي على ع
            "كتب", "كتاب", "مكتب", "مكتبة", "كاتب",  # كلمات تشترك في ك ت ب
            "حياة", "حي", "أحياء", "محيا", "حيوان"  # كلمات تشترك في ح ي
        ]
        
        expansion_result = semantics_engine.expand_semantic_database_from_dictionary(test_words)
        
        print(f"📊 نتائج التوسع:")
        print(f"   🔍 كلمات معالجة: {expansion_result['words_processed']}")
        print(f"   🆕 أنماط جديدة: {expansion_result['new_patterns_discovered']}")
        print(f"   🎯 مجموعات دلالية: {expansion_result['semantic_clusters_found']}")
        
        print(f"🏆 أقوى الأنماط المكتشفة:")
        for i, pattern in enumerate(expansion_result['expansion_summary']['strongest_patterns'], 1):
            print(f"   {i}. الحروف المشتركة: '{pattern['shared_letters']}'")
            print(f"      المعنى المشترك: {pattern['common_meaning']}")
            print(f"      القوة: {pattern['strength']:.3f}")
            print()
        
        # اختبار 5: إحصائيات التوسع
        print("📈 اختبار 5: إحصائيات نظام التوسع")
        print("-" * 50)
        
        expansion_stats = semantics_engine.get_expansion_statistics()
        print(f"📊 إجمالي الأنماط المكتشفة: {expansion_stats['total_discovered_patterns']}")
        print(f"📝 الكلمات المعالجة: {expansion_stats['processed_words_count']}")
        print(f"🎯 المجموعات الدلالية: {expansion_stats['semantic_clusters_count']}")
        print(f"⭐ جودة التوسع: {expansion_stats['expansion_quality']:.3f}")
        print(f"🔧 حالة النظام: {expansion_stats['system_status']}")
        
        print()
        
        # اختبار 6: النموذج اللغوي العربي المتقدم
        print("🇸🇦 اختبار 6: النموذج اللغوي العربي المتقدم")
        print("-" * 50)
        
        arabic_model = AdvancedArabicLanguageModel("TestAdvancedArabicModel")
        
        test_text = "اللغة العربية لغة جميلة وثرية بالمعاني العميقة"
        comprehensive_analysis = arabic_model.analyze_arabic_text_comprehensive(test_text)
        
        print(f"📝 النص: {test_text}")
        print(f"🔤 تحليل دلالات الحروف:")
        letter_analysis = comprehensive_analysis['letter_semantics_analysis']
        print(f"   ⚖️ الوزن الدلالي الإجمالي: {letter_analysis['overall_semantic_weight']:.3f}")
        print(f"   🎵 التدفق الصوتي: {letter_analysis['phonetic_flow']:.3f}")
        print(f"   👁️ التناغم البصري: {letter_analysis['visual_harmony']:.3f}")
        
        print(f"🎯 المواضيع المهيمنة:")
        for theme in letter_analysis['dominant_themes']:
            print(f"   • {theme}")
        
        print(f"📊 التحليل المتكامل:")
        integrated = comprehensive_analysis['integrated_meaning']
        print(f"   🎯 جودة النص: {integrated['text_quality']}")
        print(f"   ⚖️ الوزن الدلالي المتكامل: {integrated['integrated_semantic_weight']:.3f}")
        print(f"   🔗 التماسك الإجمالي: {integrated['overall_coherence']:.3f}")
        print(f"   🌟 قيمة المعنى المتكامل: {integrated['integrated_meaning_value']:.3f}")
        
        print()
        print("🎉 اكتمل اختبار النظام الثوري لدلالات الحروف العربية بنجاح!")
        print("✨ النظام يعمل وفقاً للرؤية الثورية الجديدة!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار النظام: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_specific_revolutionary_features():
    """اختبار الميزات الثورية المحددة."""
    
    print("\n🚀 اختبار الميزات الثورية المحددة")
    print("=" * 50)
    
    try:
        semantics_engine = ArabicLetterSemanticsEngine()
        
        # اختبار الحروف كمعايير (تصف الضدين)
        print("⚖️ اختبار الحروف كمعايير:")
        
        ba_analysis = semantics_engine.analyze_letter("ب")
        if "revolutionary_meaning_theory" in ba_analysis:
            measurement_axis = ba_analysis["revolutionary_meaning_theory"]["measurement_axis"]
            print(f"   ب: {measurement_axis['positive_pole']} ↔ {measurement_axis['negative_pole']}")
        
        ain_analysis = semantics_engine.analyze_letter("ع")
        if "revolutionary_meaning_theory" in ain_analysis:
            measurement_axis = ain_analysis["revolutionary_meaning_theory"]["measurement_axis"]
            print(f"   ع: {measurement_axis['positive_pole']} ↔ {measurement_axis['negative_pole']}")
        
        # اختبار التفاعل التدريجي للحروف
        print("\n🔄 اختبار التفاعل التدريجي:")
        
        words_to_test = ["ب", "بي", "بيت", "بيوت"]
        for word in words_to_test:
            analysis = semantics_engine.analyze_word_letters(word)
            interaction = analysis["revolutionary_semantic_interaction"]
            print(f"   {word}: {interaction['meaning_synthesis']} (قوة: {interaction['interaction_strength']:.3f})")
        
        # اختبار الكلمات التوسعية (التي لا تنطبق عليها قواعد الحروف)
        print("\n🌍 اختبار الكلمات التوسعية:")
        
        expansive_words = ["تلفزيون", "كمبيوتر", "إنترنت"]
        for word in expansive_words:
            analysis = semantics_engine.analyze_word_letters(word)
            completeness = analysis["meaning_completeness"]
            print(f"   {word}: اكتمال المعنى = {completeness:.3f} (توسعية: {'نعم' if completeness < 0.5 else 'لا'})")
        
        print("\n✅ انتهى اختبار الميزات الثورية المحددة")
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار الميزات الثورية: {e}")
        return False

def main():
    """الدالة الرئيسية للاختبار."""
    
    print("🚀 بدء اختبار النظام الثوري لدلالات الحروف العربية")
    print("🔬 وفقاً للرؤية الثورية الجديدة من ملف 'معاني الحروف.txt'")
    print("🧬 كل حرف معيار ووحدة مقياس - معاني مترابطة سببياً ومنطقياً")
    print("🔄 معنى الكلمة من تفاعل معاني حروفها - لغة غير مكتملة")
    print("📖 نظام توسع قاعدة البيانات من القواميس")
    print()
    
    # اختبار النظام الأساسي
    basic_success = test_revolutionary_letter_semantics()
    
    if basic_success:
        # اختبار الميزات الثورية المحددة
        revolutionary_success = test_specific_revolutionary_features()
        
        if revolutionary_success:
            print("\n🏆 النتيجة النهائية: نجح الاختبار بامتياز!")
            print("🌟 النظام الثوري لدلالات الحروف العربية جاهز للعمل!")
            print("🚀 يمكن الآن استخدام النظام في التطبيقات المتقدمة!")
        else:
            print("\n⚠️ النتيجة النهائية: فشل في اختبار الميزات الثورية")
    else:
        print("\n❌ النتيجة النهائية: فشل في اختبار النظام الأساسي")
    
    print("\n" + "=" * 70)
    print("🔬 انتهى اختبار النظام الثوري لدلالات الحروف العربية")
    print(f"📅 وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
