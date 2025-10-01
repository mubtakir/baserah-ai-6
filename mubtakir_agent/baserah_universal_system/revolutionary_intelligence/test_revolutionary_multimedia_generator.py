#!/usr/bin/env python3
# test_revolutionary_multimedia_generator.py - اختبار مولد الوسائط المتعددة الثوري

import sys
import os
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد النظام المطور
from revolutionary_intelligence.revolutionary_multimedia_generator import (
    RevolutionaryMultimediaGenerator, MultimediaGenerationConfig, 
    MultimediaType, GenerationMode
)
from revolutionary_intelligence.self_developing_cognitive_ai import SelfDevelopingCognitiveAI

def test_revolutionary_multimedia_generator():
    """اختبار مولد الوسائط المتعددة الثوري."""
    
    print("🎨✨ اختبار مولد الوسائط المتعددة الثوري")
    print("=" * 70)
    print(f"📅 وقت الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🧬 مدعوم بنظريات باسل الثورية والوحدة الفنية")
    print("🌟 يدمج التحليل الدلالي وتفسير الأحلام مع التوليد البصري")
    print()
    
    try:
        # إنشاء مولد الوسائط المتعددة الثوري
        print("🏗️ إنشاء مولد الوسائط المتعددة الثوري...")
        multimedia_generator = RevolutionaryMultimediaGenerator("TestRevolutionaryMultimediaGenerator")
        print("✅ تم إنشاء المولد بنجاح!")
        print()
        
        # اختبار 1: توليد صورة بسيطة
        print("🖼️ اختبار 1: توليد صورة بسيطة")
        print("-" * 50)
        
        simple_config = MultimediaGenerationConfig(
            media_type=MultimediaType.IMAGE,
            generation_mode=GenerationMode.TEXT_TO_MEDIA,
            prompt="منظر طبيعي جميل مع جبال زرقاء وسماء صافية",
            width=512,
            height=512,
            quality="high"
        )
        
        simple_result = multimedia_generator.generate_multimedia_revolutionary(simple_config)
        
        print(f"📝 المدخل: {simple_config.prompt}")
        print(f"📱 نوع الوسائط: {simple_config.media_type.name}")
        print(f"🎯 نمط التوليد: {simple_config.generation_mode.name}")
        print(f"🎯 درجة الثقة: {simple_result.confidence_score:.3f}")
        print(f"⏱️ وقت التوليد: {simple_result.generation_time:.3f} ثانية")
        
        # عرض التحليل الثوري
        revolutionary_analysis = simple_result.revolutionary_analysis
        print(f"🧬 التحليل الثوري:")
        applied_theories = revolutionary_analysis.get('applied_theories', [])
        print(f"   النظريات المطبقة: {', '.join(applied_theories) if applied_theories else 'لا توجد'}")
        print(f"   درجة الجمال الرياضي: {revolutionary_analysis.get('mathematical_beauty_score', 0.0):.3f}")
        
        visual_transformations = revolutionary_analysis.get('visual_transformations', [])
        if visual_transformations:
            print(f"   التحويلات البصرية: {', '.join(visual_transformations)}")
        
        # عرض الميزات الفنية
        artistic_features = simple_result.artistic_features
        print(f"🎨 الميزات الفنية:")
        for feature_name, feature_value in artistic_features.items():
            print(f"   {feature_name}: {feature_value}")
        
        # عرض معلومات الملف
        if os.path.exists(simple_result.file_path):
            file_size = os.path.getsize(simple_result.file_path)
            print(f"📁 الملف المولد: {os.path.basename(simple_result.file_path)} ({file_size} بايت)")
        else:
            print("❌ لم يتم إنشاء الملف")
        
        print()
        
        # اختبار 2: توليد تصور رياضي مع نظريات باسل
        print("🧮 اختبار 2: توليد تصور رياضي مع نظريات باسل")
        print("-" * 50)
        
        mathematical_config = MultimediaGenerationConfig(
            media_type=MultimediaType.MATHEMATICAL_VISUALIZATION,
            generation_mode=GenerationMode.REVOLUTIONARY_PATTERN,
            prompt="تصور بصري لنظرية ثنائية الصفر مع توازن الأضداد والتعامد",
            width=1024,
            height=1024,
            quality="ultra",
            revolutionary_features={
                'apply_zero_duality': True,
                'apply_perpendicular_opposites': True,
                'mathematical_beauty': True
            }
        )
        
        mathematical_result = multimedia_generator.generate_multimedia_revolutionary(mathematical_config)
        
        print(f"📝 المدخل: {mathematical_config.prompt}")
        print(f"📱 نوع الوسائط: {mathematical_config.media_type.name}")
        print(f"🎯 نمط التوليد: {mathematical_config.generation_mode.name}")
        print(f"🎯 درجة الثقة: {mathematical_result.confidence_score:.3f}")
        print(f"⏱️ وقت التوليد: {mathematical_result.generation_time:.3f} ثانية")
        
        # عرض التحليل الثوري المتقدم
        math_revolutionary_analysis = mathematical_result.revolutionary_analysis
        print(f"🧬 التحليل الثوري المتقدم:")
        math_applied_theories = math_revolutionary_analysis.get('applied_theories', [])
        print(f"   النظريات المطبقة: {', '.join(math_applied_theories)}")
        print(f"   درجة الجمال الرياضي: {math_revolutionary_analysis.get('mathematical_beauty_score', 0.0):.3f}")
        
        # عرض معاملات المعادلات
        equation_parameters = math_revolutionary_analysis.get('equation_parameters', {})
        if equation_parameters:
            print(f"   معاملات المعادلات:")
            for theory_name, params in equation_parameters.items():
                print(f"      {theory_name}: {len(params)} معاملات")
        
        print()
        
        # اختبار 3: توليد تصور حلم إبداعي
        print("🌙 اختبار 3: توليد تصور حلم إبداعي")
        print("-" * 50)
        
        dream_config = MultimediaGenerationConfig(
            media_type=MultimediaType.DREAM_VISUALIZATION,
            generation_mode=GenerationMode.DREAM_TO_MEDIA,
            prompt="حلمت أنني أطير فوق مدينة من الضوء الذهبي، والنجوم تتراقص حولي مثل فراشات مضيئة",
            width=768,
            height=768,
            quality="high",
            style="dreamy",
            artistic_parameters={
                'dream_intensity': 0.9,
                'symbolic_elements': ['طيران', 'ضوء', 'نجوم', 'فراشات'],
                'emotional_tone': 'سعيد'
            }
        )
        
        dream_result = multimedia_generator.generate_multimedia_revolutionary(dream_config)
        
        print(f"📝 المدخل: {dream_config.prompt}")
        print(f"📱 نوع الوسائط: {dream_config.media_type.name}")
        print(f"🎯 نمط التوليد: {dream_config.generation_mode.name}")
        print(f"🎯 درجة الثقة: {dream_result.confidence_score:.3f}")
        
        # عرض التحليل الدلالي
        semantic_analysis = dream_result.metadata.get('semantic_analysis', {})
        if semantic_analysis:
            print(f"🧠 التحليل الدلالي:")
            print(f"   اكتمال المعنى: {semantic_analysis.get('semantic_completeness', 0.0):.3f}")
            
            visual_keywords = semantic_analysis.get('visual_keywords', [])
            if visual_keywords:
                print(f"   الكلمات البصرية: {', '.join(visual_keywords[:5])}")
            
            color_analysis = semantic_analysis.get('color_analysis', {})
            mentioned_colors = color_analysis.get('mentioned_colors', [])
            if mentioned_colors:
                print(f"   الألوان المذكورة: {', '.join(mentioned_colors)}")
        
        # عرض تحليل الأحلام
        dream_analysis = dream_result.metadata.get('dream_analysis', {})
        if dream_analysis:
            print(f"🌙 تحليل الأحلام:")
            print(f"   درجة الثقة: {dream_analysis.get('confidence_score', 0.0):.3f}")
            
            symbolic_insights = dream_analysis.get('symbolic_insights', {})
            if symbolic_insights.get('symbols_found', 0) > 0:
                print(f"   رموز مكتشفة: {symbolic_insights['symbols_found']}")
                dominant_symbols = symbolic_insights.get('dominant_symbols', [])
                if dominant_symbols:
                    print(f"   الرموز المهيمنة: {', '.join(dominant_symbols)}")
        
        print()
        
        # اختبار 4: إحصائيات المولد
        print("📊 اختبار 4: إحصائيات المولد")
        print("-" * 50)
        
        generator_stats = multimedia_generator.get_generator_statistics()
        
        print(f"🏷️ معلومات المولد:")
        print(f"   الاسم: {generator_stats['generator_info']['name']}")
        print(f"   النوع: {generator_stats['generator_info']['type']}")
        
        print(f"📈 إحصائيات التوليد:")
        gen_stats = generator_stats['generation_stats']
        print(f"   الوسائط المولدة: {gen_stats['media_generated']}")
        print(f"   الصور المنشأة: {gen_stats['images_created']}")
        print(f"   الفيديوهات المنشأة: {gen_stats['videos_created']}")
        print(f"   الأنيميشن المنشأ: {gen_stats['animations_created']}")
        print(f"   الأنماط الثورية المستخدمة: {gen_stats['revolutionary_patterns_used']}")
        print(f"   متوسط وقت التوليد: {gen_stats['average_generation_time']:.3f} ثانية")
        print(f"   متوسط درجة الثقة: {gen_stats['average_confidence_score']:.3f}")
        
        print(f"🛠️ القدرات:")
        capabilities = generator_stats['capabilities']
        print(f"   أنواع الوسائط: {capabilities['multimedia_types']}")
        print(f"   أنماط التوليد: {capabilities['generation_modes']}")
        print(f"   استراتيجيات التوليد: {capabilities['generation_strategies']}")
        print(f"   الأنماط الثورية: {capabilities['revolutionary_patterns']}")
        print(f"   مستويات الجودة: {capabilities['quality_levels']}")
        
        print(f"🌟 الميزات الثورية:")
        rev_features = generator_stats['revolutionary_features']
        print(f"   نظريات باسل المدعومة: {', '.join(rev_features['basil_theories_supported'])}")
        print(f"   تكامل الوحدة الفنية: {'✅' if rev_features['artistic_unit_integration'] else '❌'}")
        print(f"   التحليل الدلالي: {'✅' if rev_features['semantic_analysis'] else '❌'}")
        print(f"   تفسير الأحلام: {'✅' if rev_features['dream_interpretation'] else '❌'}")
        print(f"   التصور الرياضي: {'✅' if rev_features['mathematical_visualization'] else '❌'}")
        print(f"   الأنماط الفنية: {'✅' if rev_features['artistic_patterns'] else '❌'}")
        
        print(f"🏆 تقييم الأداء: {generator_stats['performance_assessment']}")
        
        print()
        print("🎉 اكتمل اختبار مولد الوسائط المتعددة الثوري بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار المولد: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_integrated_cognitive_multimedia_system():
    """اختبار النظام المعرفي المتكامل مع توليد الوسائط المتعددة."""
    
    print("\n🧠🎨 اختبار النظام المعرفي المتكامل مع توليد الوسائط المتعددة")
    print("=" * 70)
    
    try:
        # إنشاء النظام المتكامل
        print("🏗️ إنشاء النظام المعرفي المتكامل...")
        cognitive_ai = SelfDevelopingCognitiveAI("TestMultimediaCognitiveAI")
        print("✅ تم إنشاء النظام بنجاح!")
        print()
        
        # اختبار التفكير العميق مع توليد الوسائط
        print("🧠 اختبار التفكير العميق مع توليد الوسائط المتعددة")
        print("-" * 50)
        
        multimedia_request = "ارسم لي صورة فنية تجمع بين الجمال الطبيعي والرياضيات، مع ألوان زرقاء وذهبية، وأشكال هندسية متناغمة تعكس نظريات باسل الثورية"
        
        thinking_result = cognitive_ai.think_deeply_and_develop(
            multimedia_request,
            thinking_depth=4,
            enable_self_development=True
        )
        
        print(f"📝 المدخل: {multimedia_request}")
        print(f"🎯 جودة التفكير: {thinking_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {thinking_result['performance_improvement']:.3f}")
        
        # فحص توليد الوسائط المتعددة
        if 'multimedia_generation' in thinking_result:
            multimedia_gen = thinking_result['multimedia_generation']
            print(f"🎨 توليد الوسائط المتعددة:")
            print(f"   درجة الثقة: {multimedia_gen['confidence_score']:.3f}")
            
            media_config = multimedia_gen['media_config_extraction']
            if hasattr(media_config, 'media_type'):
                print(f"   التكوين المستخرج:")
                print(f"      نوع الوسائط: {media_config.media_type.name}")
                print(f"      نمط التوليد: {media_config.generation_mode.name}")
                print(f"      الأبعاد: {media_config.width}x{media_config.height}")
                print(f"      الجودة: {media_config.quality}")
            
            multimedia_analysis = multimedia_gen.get('multimedia_analysis', {})
            if multimedia_analysis:
                print(f"   تحليل الوسائط:")
                print(f"      وجود الملف: {'✅' if multimedia_analysis.get('file_exists') else '❌'}")
                print(f"      حجم الملف: {multimedia_analysis.get('file_size', 0)} بايت")
                
            artistic_features = multimedia_gen.get('artistic_features', {})
            if artistic_features:
                print(f"   الميزات الفنية:")
                for feature_name, feature_value in artistic_features.items():
                    print(f"      {feature_name}: {feature_value}")
            
            final_media = multimedia_gen.get('final_media', '')
            if final_media:
                print(f"   الملف النهائي: {os.path.basename(final_media)}")
        
        # فحص الاستجابة المحسنة
        language_response = thinking_result['language_response']
        print(f"🗣️ الاستجابة المحسنة:")
        response_preview = language_response['final_response'][:300] + "..." if len(language_response['final_response']) > 300 else language_response['final_response']
        print(f"   {response_preview}")
        
        print()
        
        # عرض حالة النظام المتكامل
        print("📊 حالة النظام المتكامل مع توليد الوسائط المتعددة")
        print("-" * 50)
        
        system_status = cognitive_ai.get_system_status()
        
        print(f"🧠 النواة المعرفية:")
        cognitive_stats = system_status['cognitive_core_status']
        print(f"   الطبقات المعرفية: {cognitive_stats['total_layers']}")
        print(f"   التفاعلات: {cognitive_stats['total_interactions']}")
        print(f"   معدل النجاح: {cognitive_stats['success_rate']:.1%}")
        
        print(f"🎨 مولد الوسائط المتعددة الثوري:")
        multimedia_stats = system_status['revolutionary_multimedia_generator_status']
        gen_stats = multimedia_stats['generation_stats']
        print(f"   الوسائط المولدة: {gen_stats['media_generated']}")
        print(f"   الصور المنشأة: {gen_stats['images_created']}")
        print(f"   الأنماط الثورية: {gen_stats['revolutionary_patterns_used']}")
        print(f"   متوسط الثقة: {gen_stats['average_confidence_score']:.3f}")
        print(f"   تقييم الأداء: {multimedia_stats['performance_assessment']}")
        
        print()
        print("🎉 اكتمل اختبار النظام المعرفي المتكامل مع توليد الوسائط المتعددة بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار النظام المتكامل: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """الدالة الرئيسية للاختبار."""
    
    print("🚀 بدء اختبار مولد الوسائط المتعددة الثوري")
    print("🧬 مدعوم بنظريات باسل الثورية والوحدة الفنية")
    print("🌟 يدمج التحليل الدلالي وتفسير الأحلام مع التوليد البصري")
    print("🎨 توليد الصور والفيديو والأنيميشن والتصور الرياضي")
    print()
    
    # اختبار المولد المستقل
    generator_success = test_revolutionary_multimedia_generator()
    
    if generator_success:
        # اختبار النظام المتكامل
        integration_success = test_integrated_cognitive_multimedia_system()
        
        if integration_success:
            print("\n🏆 النتيجة النهائية: نجح الاختبار بامتياز!")
            print("🌟 مولد الوسائط المتعددة الثوري متكامل مع النظام المعرفي الباهر!")
            print("🚀 النظام جاهز لتوليد الوسائط بطرق ثورية!")
        else:
            print("\n⚠️ النتيجة النهائية: فشل في اختبار التكامل")
    else:
        print("\n❌ النتيجة النهائية: فشل في اختبار المولد الأساسي")
    
    print("\n" + "=" * 70)
    print("🔬 انتهى اختبار مولد الوسائط المتعددة الثوري")
    print(f"📅 وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
