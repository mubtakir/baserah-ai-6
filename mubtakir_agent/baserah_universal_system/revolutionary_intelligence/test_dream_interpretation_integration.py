#!/usr/bin/env python3
# test_dream_interpretation_integration.py - اختبار تكامل محرك تفسير الأحلام

import sys
import os
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد النظام المطور
from revolutionary_intelligence.dream_interpretation_engine import DreamInterpretationEngine
from revolutionary_intelligence.self_developing_cognitive_ai import SelfDevelopingCognitiveAI

def test_dream_interpretation_engine():
    """اختبار محرك تفسير الأحلام الثوري."""
    
    print("🌙✨ اختبار محرك تفسير الأحلام الثوري")
    print("=" * 70)
    print(f"📅 وقت الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        # إنشاء محرك تفسير الأحلام
        print("🏗️ إنشاء محرك تفسير الأحلام...")
        dream_engine = DreamInterpretationEngine("TestDreamEngine")
        print("✅ تم إنشاء المحرك بنجاح!")
        print()
        
        # اختبار 1: تفسير حلم كلاسيكي
        print("🌙 اختبار 1: تفسير حلم كلاسيكي")
        print("-" * 50)
        
        classic_dream = "رأيت نفسي أطير فوق مدينة كبيرة، ثم سقطت فجأة في بحر عميق. كنت أسبح في البحر وأشعر بالخوف، ثم ظهر قارب وأنقذني."
        
        context = {
            'age': 25,
            'mood': 'قلق',
            'life_situation': 'تغيير وظيفة'
        }
        
        interpretation = dream_engine.interpret_dream_comprehensive(classic_dream, context)
        
        print(f"📝 الحلم: {classic_dream}")
        print(f"🎯 درجة الثقة: {interpretation['confidence_score']:.3f}")
        
        # عرض التحليل الرمزي
        symbolic_analysis = interpretation['symbolic_analysis']
        print(f"🔍 التحليل الرمزي:")
        print(f"   الرموز المستخرجة: {len(symbolic_analysis['extracted_symbols'])}")
        print(f"   الوزن الرمزي: {symbolic_analysis['symbolic_weight']:.3f}")
        
        found_symbols = [s for s in symbolic_analysis['symbol_analyses'] if s.get('found')]
        if found_symbols:
            print(f"   الرموز المكتشفة:")
            for symbol in found_symbols[:3]:
                print(f"      • {symbol['symbol']}: {symbol['meaning']}")
                print(f"        التأثير العاطفي: {symbol['emotional_impact']}")
                print(f"        قوة الرمز: {symbol['symbol_strength']:.3f}")
        
        # عرض تحليل الأنماط
        pattern_analysis = interpretation['pattern_analysis']
        print(f"🔄 تحليل الأنماط:")
        print(f"   النمط المهيمن: {pattern_analysis['dominant_pattern']}")
        print(f"   الأنماط الكلاسيكية: {len(pattern_analysis['classic_patterns'])}")
        print(f"   الأنماط المبتكرة: {len(pattern_analysis['innovative_patterns'])}")
        print(f"   الأنماط التطورية: {len(pattern_analysis['evolutionary_patterns'])}")
        
        # عرض التوصيات
        recommendations = interpretation['recommendations']
        print(f"💡 التوصيات ({len(recommendations)}):")
        for i, rec in enumerate(recommendations[:3], 1):
            print(f"   {i}. {rec['recommendation']}")
        
        print()
        
        # اختبار 2: تفسير حلم مبتكر (تقني)
        print("🚀 اختبار 2: تفسير حلم مبتكر (تقني)")
        print("-" * 50)
        
        tech_dream = "حلمت أنني أتحدث مع روبوت ذكي في مدينة مستقبلية. كان الروبوت يطير ويحمل كمبيوتر صغير. فجأة تحولت المدينة إلى شاشة كبيرة وأصبحت جزءاً من الإنترنت."
        
        tech_interpretation = dream_engine.interpret_dream_comprehensive(tech_dream)
        
        print(f"📝 الحلم: {tech_dream}")
        print(f"🎯 درجة الثقة: {tech_interpretation['confidence_score']:.3f}")
        
        # عرض الأنماط المبتكرة
        tech_patterns = tech_interpretation['pattern_analysis']
        innovative_patterns = tech_patterns['innovative_patterns']
        print(f"🚀 الأنماط المبتكرة ({len(innovative_patterns)}):")
        for pattern in innovative_patterns:
            print(f"   • {pattern['name']}: {pattern['keyword']}")
            print(f"     قوة النمط: {pattern['pattern_strength']:.3f}")
        
        # عرض الرؤى التطورية
        evolutionary_insights = tech_interpretation['evolutionary_insights']
        print(f"🧬 الرؤى التطورية:")
        print(f"   عدد الرؤى: {evolutionary_insights['insights_count']}")
        print(f"   النقاط التطورية: {evolutionary_insights['evolutionary_score']:.3f}")
        
        for insight in evolutionary_insights['insights']:
            print(f"   • {insight['type']}: {insight['insight']}")
            print(f"     الثقة: {insight['confidence']:.3f}")
        
        print()
        
        # اختبار 3: تفسير حلم عربي تراثي
        print("🕌 اختبار 3: تفسير حلم عربي تراثي")
        print("-" * 50)
        
        traditional_dream = "رأيت أسداً يمشي في صحراء واسعة تحت نجوم لامعة. كان الأسد يحمل مفتاحاً ذهبياً ويتجه نحو خيمة بيضاء. عندما وصل للخيمة، فتح باباً سرياً وظهر نور ساطع."
        
        traditional_context = {
            'cultural_background': 'عربي',
            'age': 40,
            'spiritual_interest': 'عالي'
        }
        
        traditional_interpretation = dream_engine.interpret_dream_comprehensive(traditional_dream, traditional_context)
        
        print(f"📝 الحلم: {traditional_dream}")
        print(f"🎯 درجة الثقة: {traditional_interpretation['confidence_score']:.3f}")
        
        # عرض التحليل الدلالي
        semantic_analysis = traditional_interpretation['semantic_analysis']
        emotional_context = semantic_analysis['emotional_context']
        print(f"🧠 التحليل الدلالي:")
        print(f"   اكتمال المعنى: {semantic_analysis['semantic_completeness']:.3f}")
        print(f"   المشاعر السائدة: {emotional_context['dominant_emotion']}")
        print(f"   الشدة العاطفية: {emotional_context['emotional_intensity']:.3f}")
        print(f"   التوازن العاطفي: {emotional_context['emotional_balance']:.3f}")
        
        # عرض التكامل الثوري
        integrated_interpretation = traditional_interpretation['integrated_interpretation']
        print(f"🌟 التكامل الثوري:")
        print(f"   نقاط التكامل: {integrated_interpretation['integration_score']:.3f}")
        print(f"   التكامل الثوري: {integrated_interpretation['revolutionary_integration']:.3f}")
        print(f"   جودة التفسير: {integrated_interpretation['interpretation_quality']}")
        print(f"   المعنى المتكامل: {integrated_interpretation['integrated_meaning']}")
        
        print()
        
        # اختبار 4: إحصائيات المحرك
        print("📊 اختبار 4: إحصائيات المحرك")
        print("-" * 50)
        
        engine_stats = dream_engine.get_engine_statistics()
        
        print(f"🏷️ معلومات المحرك:")
        print(f"   الاسم: {engine_stats['engine_info']['name']}")
        print(f"   النوع: {engine_stats['engine_info']['type']}")
        
        print(f"📈 إحصائيات التفسير:")
        interp_stats = engine_stats['interpretation_stats']
        print(f"   الأحلام المفسرة: {interp_stats['dreams_interpreted']}")
        print(f"   الرموز المحللة: {interp_stats['symbols_analyzed']}")
        print(f"   الأنماط المكتشفة: {interp_stats['patterns_discovered']}")
        print(f"   نقاط الدقة: {interp_stats['accuracy_score']:.3f}")
        
        print(f"🗄️ إحصائيات قاعدة البيانات:")
        db_stats = engine_stats['database_stats']
        print(f"   إجمالي الرموز: {db_stats['total_symbols']}")
        print(f"   فئات الرموز: {db_stats['symbol_categories']}")
        print(f"   الأنماط الكلاسيكية: {db_stats['classic_patterns']}")
        print(f"   الأنماط المبتكرة: {db_stats['innovative_patterns']}")
        
        print(f"🕸️ إحصائيات الشبكة:")
        network_stats = engine_stats['network_stats']
        print(f"   عقد الأحلام: {network_stats['dream_nodes']}")
        print(f"   روابط الرموز: {network_stats['symbol_connections']}")
        print(f"   مجموعات الأنماط: {network_stats['pattern_clusters']}")
        
        print(f"🏆 تقييم الأداء: {engine_stats['performance_assessment']}")
        
        print()
        print("🎉 اكتمل اختبار محرك تفسير الأحلام الثوري بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار المحرك: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_integrated_cognitive_dream_system():
    """اختبار النظام المعرفي المتكامل مع تفسير الأحلام."""
    
    print("\n🧠🌙 اختبار النظام المعرفي المتكامل مع تفسير الأحلام")
    print("=" * 70)
    
    try:
        # إنشاء النظام المتكامل
        print("🏗️ إنشاء النظام المعرفي المتكامل...")
        cognitive_ai = SelfDevelopingCognitiveAI("TestDreamCognitiveAI")
        print("✅ تم إنشاء النظام بنجاح!")
        print()
        
        # اختبار التفكير العميق مع تفسير الأحلام
        print("🧠 اختبار التفكير العميق مع تفسير الأحلام")
        print("-" * 50)
        
        dream_input = "حلمت أنني أقف على جبل عالي وأرى مدينة مضيئة بالأنوار. كان هناك طائر كبير يطير حولي ويحمل رسالة. فجأة بدأت أطير مع الطائر نحو المدينة المضيئة."
        
        thinking_result = cognitive_ai.think_deeply_and_develop(
            dream_input,
            thinking_depth=3,
            enable_self_development=True
        )
        
        print(f"📝 المدخل: {dream_input}")
        print(f"🎯 جودة التفكير: {thinking_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {thinking_result['performance_improvement']:.3f}")
        
        # فحص تفسير الأحلام
        if 'dream_interpretation' in thinking_result:
            dream_interp = thinking_result['dream_interpretation']
            print(f"🌙 تفسير الأحلام:")
            print(f"   درجة الثقة: {dream_interp['confidence_score']:.3f}")
            
            symbolic_insights = dream_interp['symbolic_insights']
            print(f"   الرؤى الرمزية:")
            print(f"      رموز مكتشفة: {symbolic_insights['symbols_found']}")
            print(f"      الوزن الرمزي: {symbolic_insights['symbolic_weight']:.3f}")
            print(f"      تفاعلات رمزية: {symbolic_insights['symbol_interactions']}")
            
            pattern_discoveries = dream_interp['pattern_discoveries']
            print(f"   اكتشافات الأنماط:")
            print(f"      النمط المهيمن: {pattern_discoveries['dominant_pattern']}")
            print(f"      أنماط كلاسيكية: {pattern_discoveries['classic_patterns_count']}")
            print(f"      أنماط مبتكرة: {pattern_discoveries['innovative_patterns_count']}")
            print(f"      أنماط تطورية: {pattern_discoveries['evolutionary_patterns_count']}")
            
            recommendations = dream_interp['recommendations']
            print(f"   التوصيات ({len(recommendations)}):")
            for i, rec in enumerate(recommendations[:3], 1):
                print(f"      {i}. {rec.get('recommendation', '')}")
        
        # فحص الاستجابة المحسنة
        language_response = thinking_result['language_response']
        print(f"🗣️ الاستجابة المحسنة:")
        print(f"   {language_response['final_response']}")
        
        print()
        
        # عرض حالة النظام المتكامل
        print("📊 حالة النظام المتكامل مع تفسير الأحلام")
        print("-" * 50)
        
        system_status = cognitive_ai.get_system_status()
        
        print(f"🧠 النواة المعرفية:")
        cognitive_stats = system_status['cognitive_core_status']
        print(f"   الطبقات المعرفية: {cognitive_stats['total_layers']}")
        print(f"   التفاعلات: {cognitive_stats['total_interactions']}")
        print(f"   معدل النجاح: {cognitive_stats['success_rate']:.1%}")
        
        print(f"🌙 محرك تفسير الأحلام:")
        dream_stats = system_status['dream_interpretation_engine_status']
        interp_stats = dream_stats['interpretation_stats']
        print(f"   الأحلام المفسرة: {interp_stats['dreams_interpreted']}")
        print(f"   الرموز المحللة: {interp_stats['symbols_analyzed']}")
        print(f"   الأنماط المكتشفة: {interp_stats['patterns_discovered']}")
        print(f"   نقاط الدقة: {interp_stats['accuracy_score']:.3f}")
        print(f"   تقييم الأداء: {dream_stats['performance_assessment']}")
        
        print()
        print("🎉 اكتمل اختبار النظام المعرفي المتكامل مع تفسير الأحلام بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار النظام المتكامل: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """الدالة الرئيسية للاختبار."""
    
    print("🚀 بدء اختبار تكامل محرك تفسير الأحلام")
    print("🌙 يدمج الطرق المعروفة والمبتكرة لتفسير الأحلام")
    print("🔍 التحليل الرمزي والدلالي المتقدم")
    print("🧮 المعادلات الرياضية التكيفية (بدلاً من الشبكات العصبية)")
    print("🚀 تكامل الخبير/المستكشف التطوري")
    print("🕸️ الشبكة الدلالية المتكاملة")
    print()
    
    # اختبار المحرك المستقل
    engine_success = test_dream_interpretation_engine()
    
    if engine_success:
        # اختبار النظام المتكامل
        integration_success = test_integrated_cognitive_dream_system()
        
        if integration_success:
            print("\n🏆 النتيجة النهائية: نجح الاختبار بامتياز!")
            print("🌟 محرك تفسير الأحلام متكامل مع النظام المعرفي الباهر!")
            print("🚀 النظام جاهز لتفسير الأحلام بطرق ثورية!")
        else:
            print("\n⚠️ النتيجة النهائية: فشل في اختبار التكامل")
    else:
        print("\n❌ النتيجة النهائية: فشل في اختبار المحرك الأساسي")
    
    print("\n" + "=" * 70)
    print("🔬 انتهى اختبار تكامل محرك تفسير الأحلام")
    print(f"📅 وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
