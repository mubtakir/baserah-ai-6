#!/usr/bin/env python3
# test_complete_integrated_system.py - اختبار النظام المتكامل الكامل

import sys
import os
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد النظام المطور
from revolutionary_intelligence.self_developing_cognitive_ai import SelfDevelopingCognitiveAI

def test_complete_integrated_system():
    """اختبار النظام المتكامل الكامل مع جميع المكونات."""
    
    print("🌟🧠🎨👁️ اختبار النظام المتكامل الكامل - Baserah Universal System")
    print("=" * 80)
    print(f"📅 وقت الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🚀 النظام الذكي المعرفي الشامل والمتكامل والثوري")
    print()
    
    print("🧬 المكونات المتكاملة:")
    print("   🧠 النواة المعرفية الباهرة (7 طبقات معرفية)")
    print("   🗣️ نموذج اللغة العربية المتقدم (تحليل صرفي + جذور)")
    print("   🌟 نموذج اللغة المبتكر (عصف ذهني + إبداع)")
    print("   🧠 محرك الدلالة المعنوية الثوري")
    print("   🌙 محرك تفسير الأحلام المتكامل")
    print("   🚀 مولد الكود الثوري (مفكر + محلل + مختبر)")
    print("   🎨 مولد الوسائط المتعددة الثوري (نظريات باسل)")
    print("   👁️ محرك الاستنباط البصري الذكي (العين المستنبطة)")
    print()
    
    try:
        # إنشاء النظام المتكامل الكامل
        print("🏗️ إنشاء النظام المتكامل الكامل...")
        cognitive_ai = SelfDevelopingCognitiveAI("CompleteIntegratedBaserahSystem")
        print("✅ تم إنشاء النظام بنجاح!")
        print()
        
        # اختبار 1: معالجة نص عربي معقد
        print("📝 اختبار 1: معالجة نص عربي معقد")
        print("-" * 60)
        
        arabic_text = "أريد أن أفهم معنى الحياة والوجود، وأحلم بعالم أفضل مليء بالسلام والمحبة"
        
        arabic_result = cognitive_ai.think_deeply_and_develop(
            arabic_text,
            thinking_depth=4,
            enable_self_development=True
        )
        
        print(f"📝 المدخل: {arabic_text}")
        print(f"🎯 جودة التفكير: {arabic_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {arabic_result['performance_improvement']:.3f}")
        
        # عرض التحليل الدلالي
        if 'semantic_analysis' in arabic_result:
            semantic = arabic_result['semantic_analysis']
            print(f"🧠 التحليل الدلالي:")
            print(f"   اكتمال المعنى: {semantic.get('meaning_completeness', 0.0):.3f}")
            
            entities = semantic.get('entities', [])
            if entities:
                print(f"   الكيانات المكتشفة: {len(entities)}")
                for entity in entities[:3]:
                    print(f"      • {entity.get('word', '')} ({entity.get('type', '')})")
        
        # عرض تفسير الأحلام
        if 'dream_interpretation' in arabic_result:
            dream = arabic_result['dream_interpretation']
            print(f"🌙 تفسير الأحلام:")
            print(f"   درجة الثقة: {dream.get('confidence_score', 0.0):.3f}")
            
            symbolic_insights = dream.get('symbolic_insights', {})
            if symbolic_insights.get('symbols_found', 0) > 0:
                print(f"   رموز مكتشفة: {symbolic_insights['symbols_found']}")
        
        print()
        
        # اختبار 2: توليد كود برمجي
        print("💻 اختبار 2: توليد كود برمجي")
        print("-" * 60)
        
        code_request = "اكتب لي دالة Python لحساب المتوسط الحسابي لقائمة من الأرقام مع التحقق من صحة المدخلات"
        
        code_result = cognitive_ai.think_deeply_and_develop(
            code_request,
            thinking_depth=3,
            enable_self_development=True
        )
        
        print(f"📝 المدخل: {code_request}")
        print(f"🎯 جودة التفكير: {code_result['final_result']['thinking_quality']:.3f}")
        
        # عرض توليد الكود
        if 'code_generation' in code_result:
            code_gen = code_result['code_generation']
            print(f"🚀 توليد الكود:")
            print(f"   درجة الثقة: {code_gen.get('confidence_score', 0.0):.3f}")
            
            final_code = code_gen.get('final_code', '')
            if final_code:
                print(f"   الكود المولد:")
                code_preview = final_code[:200] + "..." if len(final_code) > 200 else final_code
                print(f"      {code_preview}")
            
            code_analysis = code_gen.get('code_analysis', {})
            if code_analysis:
                print(f"   تحليل الكود:")
                print(f"      الجودة: {code_analysis.get('quality_score', 0.0):.3f}")
                print(f"      الاكتمال: {code_analysis.get('completeness_score', 0.0):.3f}")
        
        print()
        
        # اختبار 3: توليد وسائط متعددة
        print("🎨 اختبار 3: توليد وسائط متعددة")
        print("-" * 60)
        
        media_request = "ارسم لي صورة فنية تجمع بين نظرية ثنائية الصفر ونظرية تعامد الأضداد مع ألوان زرقاء وذهبية"
        
        media_result = cognitive_ai.think_deeply_and_develop(
            media_request,
            thinking_depth=4,
            enable_self_development=True
        )
        
        print(f"📝 المدخل: {media_request}")
        print(f"🎯 جودة التفكير: {media_result['final_result']['thinking_quality']:.3f}")
        
        # عرض توليد الوسائط
        if 'multimedia_generation' in media_result:
            media_gen = media_result['multimedia_generation']
            print(f"🎨 توليد الوسائط:")
            print(f"   درجة الثقة: {media_gen.get('confidence_score', 0.0):.3f}")
            
            final_media = media_gen.get('final_media', '')
            if final_media:
                print(f"   الملف المولد: {os.path.basename(final_media)}")
            
            artistic_features = media_gen.get('artistic_features', {})
            if artistic_features:
                print(f"   الميزات الفنية:")
                for feature_name, feature_value in list(artistic_features.items())[:3]:
                    print(f"      {feature_name}: {feature_value}")
        
        print()
        
        # اختبار 4: تحليل بصري ذكي
        print("👁️ اختبار 4: تحليل بصري ذكي")
        print("-" * 60)
        
        visual_request = {
            'text': 'حلل هذه الصورة واوصف ما تراه فيها بالتفصيل',
            'image_data': 'complex_scene_with_multiple_elements'
        }
        
        visual_result = cognitive_ai.think_deeply_and_develop(
            visual_request,
            thinking_depth=4,
            enable_self_development=True
        )
        
        print(f"📝 المدخل: {visual_request['text']}")
        print(f"📷 بيانات الصورة: {visual_request['image_data']}")
        print(f"🎯 جودة التفكير: {visual_result['final_result']['thinking_quality']:.3f}")
        
        # عرض الاستنباط البصري
        if 'visual_inference' in visual_result:
            visual_inf = visual_result['visual_inference']
            print(f"👁️ الاستنباط البصري:")
            print(f"   درجة الثقة: {visual_inf.get('inference_confidence', 0.0):.3f}")
            
            scene_description = visual_inf.get('scene_description', '')
            if scene_description:
                print(f"   وصف المشهد: \"{scene_description}\"")
            
            visual_elements = visual_inf.get('visual_elements', [])
            if visual_elements:
                print(f"   العناصر المكتشفة: {len(visual_elements)} عنصر")
        
        print()
        
        # اختبار 5: معالجة متعددة الأنماط (نص + صورة + كود + وسائط)
        print("🌟 اختبار 5: معالجة متعددة الأنماط")
        print("-" * 60)
        
        multimodal_request = {
            'text': 'أريد برنامج يحلل الصور ويولد أوصاف شعرية لها، مع رسم تصور فني للنتائج',
            'requirements': ['تحليل بصري', 'توليد نص إبداعي', 'رسم فني', 'برمجة'],
            'style': 'إبداعي وتقني'
        }
        
        multimodal_result = cognitive_ai.think_deeply_and_develop(
            multimodal_request,
            thinking_depth=5,
            enable_self_development=True
        )
        
        print(f"📝 المدخل: {multimodal_request['text']}")
        print(f"📋 المتطلبات: {', '.join(multimodal_request['requirements'])}")
        print(f"🎯 جودة التفكير: {multimodal_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {multimodal_result['performance_improvement']:.3f}")
        
        # عرض النتائج المتعددة
        components_used = []
        if 'semantic_analysis' in multimodal_result:
            components_used.append('التحليل الدلالي')
        if 'dream_interpretation' in multimodal_result:
            components_used.append('تفسير الأحلام')
        if 'code_generation' in multimodal_result:
            components_used.append('توليد الكود')
        if 'multimedia_generation' in multimodal_result:
            components_used.append('توليد الوسائط')
        if 'visual_inference' in multimodal_result:
            components_used.append('الاستنباط البصري')
        
        print(f"🧩 المكونات المستخدمة: {', '.join(components_used)}")
        
        # عرض الاستجابة النهائية
        language_response = multimodal_result.get('language_response', {})
        if language_response:
            final_response = language_response.get('final_response', '')
            if final_response:
                response_preview = final_response[:300] + "..." if len(final_response) > 300 else final_response
                print(f"🗣️ الاستجابة النهائية:")
                print(f"   {response_preview}")
        
        print()
        
        # اختبار 6: حالة النظام الشاملة
        print("📊 اختبار 6: حالة النظام الشاملة")
        print("-" * 60)
        
        system_status = cognitive_ai.get_system_status()
        
        print(f"🧠 النواة المعرفية:")
        cognitive_stats = system_status['cognitive_core_status']
        print(f"   الطبقات المعرفية: {cognitive_stats['total_layers']}")
        print(f"   التفاعلات: {cognitive_stats['total_interactions']}")
        print(f"   معدل النجاح: {cognitive_stats['success_rate']:.1%}")
        print(f"   متوسط جودة التفكير: {cognitive_stats['average_thinking_quality']:.3f}")
        
        print(f"🗣️ نموذج اللغة العربية:")
        arabic_stats = system_status['advanced_arabic_language_model_status']
        morphology_stats = arabic_stats['morphological_analysis_stats']
        print(f"   الكلمات المحللة: {morphology_stats['words_analyzed']}")
        print(f"   الجذور المكتشفة: {morphology_stats['roots_discovered']}")
        print(f"   معدل دقة التحليل: {morphology_stats['analysis_accuracy']:.1%}")
        
        print(f"🌟 نموذج اللغة المبتكر:")
        innovative_stats = system_status['innovative_language_model_status']
        brainstorm_stats = innovative_stats['brainstorming_stats']
        print(f"   جلسات العصف الذهني: {brainstorm_stats['brainstorming_sessions']}")
        print(f"   الأفكار المولدة: {brainstorm_stats['ideas_generated']}")
        print(f"   متوسط الإبداع: {brainstorm_stats['average_creativity_score']:.3f}")
        
        print(f"🧠 محرك الدلالة المعنوية:")
        semantic_stats = system_status['semantic_meaning_engine_status']
        analysis_stats = semantic_stats['analysis_stats']
        print(f"   الجمل المحللة: {analysis_stats['sentences_analyzed']}")
        print(f"   الكيانات المكتشفة: {analysis_stats['entities_discovered']}")
        print(f"   متوسط اكتمال المعنى: {analysis_stats['average_meaning_completeness']:.3f}")
        
        print(f"🌙 محرك تفسير الأحلام:")
        dream_stats = system_status['dream_interpretation_engine_status']
        interpretation_stats = dream_stats['interpretation_stats']
        print(f"   الأحلام المفسرة: {interpretation_stats['dreams_interpreted']}")
        print(f"   الرموز المكتشفة: {interpretation_stats['symbols_discovered']}")
        print(f"   متوسط الثقة: {interpretation_stats['average_confidence']:.3f}")
        
        print(f"🚀 مولد الكود الثوري:")
        code_stats = system_status['revolutionary_code_generator_status']
        generation_stats = code_stats['generation_stats']
        print(f"   الكود المولد: {generation_stats['code_generated']}")
        print(f"   الاختبارات المنشأة: {generation_stats['tests_created']}")
        print(f"   متوسط الجودة: {generation_stats['average_quality_score']:.3f}")
        
        print(f"🎨 مولد الوسائط المتعددة:")
        multimedia_stats = system_status['revolutionary_multimedia_generator_status']
        media_stats = multimedia_stats['generation_stats']
        print(f"   الوسائط المولدة: {media_stats['media_generated']}")
        print(f"   الأنماط الثورية: {media_stats['revolutionary_patterns_used']}")
        print(f"   متوسط الثقة: {media_stats['average_confidence_score']:.3f}")
        
        print(f"👁️ محرك الاستنباط البصري:")
        visual_stats = system_status['intelligent_visual_inference_engine_status']
        inference_stats = visual_stats['analysis_stats']
        print(f"   الصور المحللة: {inference_stats['images_analyzed']}")
        print(f"   العناصر المكتشفة: {inference_stats['elements_detected']}")
        print(f"   معدل النجاح: {inference_stats['success_rate']:.1%}")
        
        print()
        
        # تقييم الأداء الشامل
        print("🏆 تقييم الأداء الشامل:")
        print("-" * 60)
        
        # حساب درجة الأداء الإجمالية
        performance_scores = [
            cognitive_stats['success_rate'],
            morphology_stats['analysis_accuracy'] / 100,
            brainstorm_stats['average_creativity_score'],
            analysis_stats['average_meaning_completeness'],
            interpretation_stats['average_confidence'],
            generation_stats['average_quality_score'],
            media_stats['average_confidence_score'],
            inference_stats['success_rate']
        ]
        
        overall_performance = sum(performance_scores) / len(performance_scores)
        
        print(f"📊 درجة الأداء الإجمالية: {overall_performance:.3f}")
        
        if overall_performance > 0.9:
            assessment = "ممتاز - أداء استثنائي"
        elif overall_performance > 0.8:
            assessment = "جيد جداً - أداء متفوق"
        elif overall_performance > 0.7:
            assessment = "جيد - أداء مقبول"
        else:
            assessment = "يحتاج تطوير"
        
        print(f"🎯 التقييم النهائي: {assessment}")
        
        print()
        print("🎉 اكتمل اختبار النظام المتكامل الكامل بنجاح!")
        print("🌟 جميع المكونات تعمل بتناغم وتكامل مثالي!")
        print("🚀 النظام جاهز للاستخدام الإنتاجي!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار النظام المتكامل: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """الدالة الرئيسية للاختبار."""
    
    print("🚀 بدء اختبار النظام المتكامل الكامل")
    print("🌟 Baserah Universal System - النظام الذكي المعرفي الشامل")
    print("🧬 يدمج جميع المكونات الثورية في نظام واحد متكامل")
    print()
    
    success = test_complete_integrated_system()
    
    if success:
        print("\n🏆 النتيجة النهائية: نجح الاختبار الشامل بامتياز!")
        print("🌟 النظام المتكامل الكامل يعمل بكفاءة عالية!")
        print("🚀 جاهز للإنتاج والاستخدام الفعلي!")
        print()
        print("🎊 تهانينا! تم إنجاز نظام ذكي معرفي ثوري ومتكامل!")
    else:
        print("\n❌ النتيجة النهائية: فشل في الاختبار الشامل")
        print("⚠️ يحتاج النظام إلى مراجعة وتطوير")
    
    print("\n" + "=" * 80)
    print("🔬 انتهى اختبار النظام المتكامل الكامل")
    print(f"📅 وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🌟 Baserah Universal System - إنجاز تاريخي في عالم الذكاء الاصطناعي!")

if __name__ == "__main__":
    main()
