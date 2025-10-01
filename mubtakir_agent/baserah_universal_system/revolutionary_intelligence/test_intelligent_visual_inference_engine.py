#!/usr/bin/env python3
# test_intelligent_visual_inference_engine.py - اختبار محرك الاستنباط البصري الذكي

import sys
import os
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد النظام المطور
from revolutionary_intelligence.intelligent_visual_inference_engine import (
    IntelligentVisualInferenceEngine, ShapeDescriptor, VisualElement
)
from revolutionary_intelligence.self_developing_cognitive_ai import SelfDevelopingCognitiveAI

def test_intelligent_visual_inference_engine():
    """اختبار محرك الاستنباط البصري الذكي."""
    
    print("👁️✨ اختبار محرك الاستنباط البصري الذكي (العين المستنبطة)")
    print("=" * 70)
    print(f"📅 وقت الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🧠 يتعلم من صور قليلة باستخدام السماحية والمسافة الإقليدية")
    print("🔍 نظام ثوري للاستنباط البصري الذكي")
    print()
    
    try:
        # إنشاء محرك الاستنباط البصري الذكي
        print("🏗️ إنشاء محرك الاستنباط البصري الذكي...")
        visual_engine = IntelligentVisualInferenceEngine("TestIntelligentVisualInferenceEngine")
        print("✅ تم إنشاء المحرك بنجاح!")
        print()
        
        # اختبار 1: عرض قاعدة البيانات الأساسية
        print("📊 اختبار 1: عرض قاعدة البيانات الأساسية")
        print("-" * 50)
        
        shapes_db = visual_engine.shapes_database
        print(f"📈 عدد الأشكال في قاعدة البيانات: {len(shapes_db)}")
        
        for shape_name, shape_descriptor in shapes_db.items():
            print(f"🔹 {shape_name}:")
            print(f"   الفئة: {shape_descriptor.category}")
            print(f"   المعادلة الأساسية: {shape_descriptor.base_equation}")
            print(f"   الخصائص: {shape_descriptor.properties}")
            print(f"   الحالات: {shape_descriptor.states}")
            print(f"   متجه الميزات: {shape_descriptor.feature_vector}")
            print(f"   نطاق السماحية: {shape_descriptor.tolerance_range}")
            print()
        
        # اختبار 2: تحليل صورة محاكاة (قطة بيضاء)
        print("🖼️ اختبار 2: تحليل صورة محاكاة (قطة بيضاء)")
        print("-" * 50)
        
        # محاكاة بيانات صورة قطة بيضاء
        simulated_cat_image = "simulated_white_cat_playing"
        
        cat_analysis = visual_engine.analyze_image_intelligently(simulated_cat_image, analysis_depth=3)
        
        print(f"📝 بيانات الصورة: {simulated_cat_image}")
        print(f"🎯 الثقة الإجمالية: {cat_analysis.overall_confidence:.3f}")
        print(f"⏱️ وقت التحليل: {cat_analysis.analysis_time:.3f} ثانية")
        print(f"📊 عدد العناصر المكتشفة: {len(cat_analysis.detected_elements)}")
        
        print(f"📝 وصف المشهد:")
        print(f"   \"{cat_analysis.scene_description}\"")
        
        print(f"🔍 العناصر المكتشفة:")
        for i, element in enumerate(cat_analysis.detected_elements):
            print(f"   {i+1}. {element.shape_name}")
            print(f"      • الموضع: {element.position}")
            print(f"      • الحجم: {element.size}")
            print(f"      • الثقة: {element.confidence:.3f}")
            print(f"      • المسافة الإقليدية: {element.euclidean_distance:.3f}")
            print(f"      • الخصائص: {element.properties}")
        
        # تفاصيل الاستنباط
        inference_details = cat_analysis.inference_details
        print(f"🧠 تفاصيل الاستنباط:")
        print(f"   عدد الميزات المستخرجة: {inference_details.get('extracted_features_count', 0)}")
        print(f"   عدد التطابقات: {inference_details.get('pattern_matches_count', 0)}")
        print(f"   عمق التحليل: {inference_details.get('analysis_depth', 0)}")
        print(f"   السماحية المستخدمة: {inference_details.get('tolerance_used', 0.0)}")
        
        print()
        
        # اختبار 3: إضافة شكل جديد إلى قاعدة البيانات
        print("➕ اختبار 3: إضافة شكل جديد إلى قاعدة البيانات")
        print("-" * 50)
        
        # إنشاء شكل جديد (كلب بني)
        new_shape = ShapeDescriptor(
            name='كلب_بني_يجري',
            category='حيوانات',
            base_equation='σ(ears) + σ(tail) + σ(legs) * σ(running_pose)',
            properties={
                'color': 'بني',
                'size': 'متوسط',
                'ears': 'مدببة',
                'tail': 'متحرك',
                'legs': 'أربعة',
                'pose': 'يجري'
            },
            states={'يجري': 0.9, 'واقف': 0.3, 'نائم': 0.1},
            feature_vector=[0.7, 0.6, 0.8, 0.9, 0.4],  # [ears, tail, legs, body, color]
            tolerance_range=0.14
        )
        
        success = visual_engine.add_shape_to_database(new_shape)
        print(f"✅ إضافة الشكل الجديد: {'نجحت' if success else 'فشلت'}")
        print(f"📈 عدد الأشكال الآن: {len(visual_engine.shapes_database)}")
        
        print()
        
        # اختبار 4: تحليل صورة معقدة (مشهد متعدد العناصر)
        print("🌆 اختبار 4: تحليل صورة معقدة (مشهد متعدد العناصر)")
        print("-" * 50)
        
        # محاكاة مشهد معقد
        complex_scene = "complex_scene_cat_house_tree"
        
        complex_analysis = visual_engine.analyze_image_intelligently(complex_scene, analysis_depth=4)
        
        print(f"📝 بيانات المشهد: {complex_scene}")
        print(f"🎯 الثقة الإجمالية: {complex_analysis.overall_confidence:.3f}")
        print(f"⏱️ وقت التحليل: {complex_analysis.analysis_time:.3f} ثانية")
        print(f"📊 عدد العناصر المكتشفة: {len(complex_analysis.detected_elements)}")
        
        print(f"📝 وصف المشهد المعقد:")
        print(f"   \"{complex_analysis.scene_description}\"")
        
        if complex_analysis.detected_elements:
            print(f"🔍 العناصر في المشهد المعقد:")
            for i, element in enumerate(complex_analysis.detected_elements):
                print(f"   {i+1}. {element.shape_name} (ثقة: {element.confidence:.3f})")
                print(f"      موضع: {element.position}, حجم: {element.size}")
                
                # عرض أهم الخصائص
                important_props = ['color', 'state', 'size']
                props_str = ', '.join(f"{k}: {v}" for k, v in element.properties.items() 
                                    if k in important_props and v)
                if props_str:
                    print(f"      خصائص: {props_str}")
        
        print()
        
        # اختبار 5: اختبار السماحية والمسافة الإقليدية
        print("📐 اختبار 5: اختبار السماحية والمسافة الإقليدية")
        print("-" * 50)
        
        # اختبار مع متجهات ميزات مختلفة
        test_vectors = [
            [0.9, 0.8, 0.7, 0.6, 0.9],  # قريب من قطة بيضاء
            [0.8, 0.7, 0.9, 0.8, 0.1],  # قريب من قطة سوداء نائمة
            [0.5, 0.3, 0.2, 0.4, 0.6],  # بعيد عن كل الأشكال
        ]
        
        reference_vector = shapes_db['قطة_بيضاء'].feature_vector
        
        print(f"🔍 المتجه المرجعي (قطة بيضاء): {reference_vector}")
        print(f"📊 اختبار المسافات الإقليدية:")
        
        for i, test_vector in enumerate(test_vectors):
            distance = visual_engine._calculate_euclidean_distance(test_vector, reference_vector)
            tolerance = shapes_db['قطة_بيضاء'].tolerance_range
            within_tolerance = distance <= tolerance
            
            print(f"   متجه {i+1}: {test_vector}")
            print(f"   المسافة الإقليدية: {distance:.4f}")
            print(f"   ضمن السماحية ({tolerance}): {'✅' if within_tolerance else '❌'}")
            print()
        
        # اختبار 6: إحصائيات المحرك
        print("📊 اختبار 6: إحصائيات المحرك")
        print("-" * 50)
        
        engine_stats = visual_engine.get_engine_statistics()
        
        print(f"🏷️ معلومات المحرك:")
        print(f"   الاسم: {engine_stats['engine_info']['name']}")
        print(f"   النوع: {engine_stats['engine_info']['type']}")
        
        print(f"📈 إحصائيات التحليل:")
        analysis_stats = engine_stats['analysis_stats']
        print(f"   الصور المحللة: {analysis_stats['images_analyzed']}")
        print(f"   العناصر المكتشفة: {analysis_stats['elements_detected']}")
        print(f"   الاستنباطات الناجحة: {analysis_stats['successful_inferences']}")
        print(f"   معدل النجاح: {analysis_stats['success_rate']:.1%}")
        print(f"   متوسط الثقة: {analysis_stats['average_confidence']:.3f}")
        print(f"   متوسط وقت التحليل: {analysis_stats['average_analysis_time']:.3f} ثانية")
        
        print(f"🗄️ إحصائيات قاعدة البيانات:")
        db_stats = engine_stats['database_stats']
        print(f"   الأشكال في قاعدة البيانات: {db_stats['shapes_in_database']}")
        print(f"   الفئات المدعومة: {db_stats['categories_supported']}")
        print(f"   إعدادات السماحية: {db_stats['tolerance_settings']}")
        
        print(f"🛠️ القدرات:")
        capabilities = engine_stats['capabilities']
        print(f"   مستخرجات الميزات: {capabilities['feature_extractors']}")
        print(f"   مُعرِّفات الأنماط: {capabilities['pattern_recognizers']}")
        print(f"   مُركِّبات المشهد: {capabilities['scene_composers']}")
        print(f"   حاسبات الثقة: {capabilities['confidence_calculators']}")
        
        print(f"🌟 الميزات الثورية:")
        rev_features = engine_stats['revolutionary_features']
        print(f"   مطابقة المسافة الإقليدية: {'✅' if rev_features['euclidean_distance_matching'] else '❌'}")
        print(f"   التعرف بالسماحية: {'✅' if rev_features['tolerance_based_recognition'] else '❌'}")
        print(f"   الاستنباط الذكي: {'✅' if rev_features['intelligent_inference'] else '❌'}")
        print(f"   التعلم من صور قليلة: {'✅' if rev_features['few_shot_learning'] else '❌'}")
        print(f"   معادلات Baserah: {'✅' if rev_features['baserah_equations'] else '❌'}")
        print(f"   التركيب الدلالي: {'✅' if rev_features['semantic_composition'] else '❌'}")
        
        print(f"🏆 تقييم الأداء: {engine_stats['performance_assessment']}")
        
        print()
        print("🎉 اكتمل اختبار محرك الاستنباط البصري الذكي بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار المحرك: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_integrated_cognitive_visual_system():
    """اختبار النظام المعرفي المتكامل مع الاستنباط البصري."""
    
    print("\n🧠👁️ اختبار النظام المعرفي المتكامل مع الاستنباط البصري")
    print("=" * 70)
    
    try:
        # إنشاء النظام المتكامل
        print("🏗️ إنشاء النظام المعرفي المتكامل...")
        cognitive_ai = SelfDevelopingCognitiveAI("TestVisualCognitiveAI")
        print("✅ تم إنشاء النظام بنجاح!")
        print()
        
        # اختبار التفكير العميق مع الاستنباط البصري
        print("🧠 اختبار التفكير العميق مع الاستنباط البصري")
        print("-" * 50)
        
        visual_request = {
            'text': 'حلل هذه الصورة واوصف ما تراه فيها',
            'image_data': 'simulated_complex_scene_with_cat_and_house'
        }
        
        thinking_result = cognitive_ai.think_deeply_and_develop(
            visual_request,
            thinking_depth=4,
            enable_self_development=True
        )
        
        print(f"📝 المدخل: {visual_request['text']}")
        print(f"📷 بيانات الصورة: {visual_request['image_data']}")
        print(f"🎯 جودة التفكير: {thinking_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {thinking_result['performance_improvement']:.3f}")
        
        # فحص الاستنباط البصري
        if 'visual_inference' in thinking_result:
            visual_inf = thinking_result['visual_inference']
            print(f"👁️ الاستنباط البصري:")
            print(f"   درجة الثقة: {visual_inf['inference_confidence']:.3f}")
            
            # معلومات استخراج الصورة
            image_extraction = visual_inf['image_data_extraction']
            print(f"   استخراج الصورة:")
            print(f"      وجود الصورة: {'✅' if image_extraction.get('image_found') else '❌'}")
            print(f"      نوع البيانات: {image_extraction.get('data_type', 'غير محدد')}")
            
            # العناصر المكتشفة
            visual_elements = visual_inf.get('visual_elements', [])
            if visual_elements:
                print(f"   العناصر المكتشفة ({len(visual_elements)} عنصر):")
                for i, element in enumerate(visual_elements[:3]):  # أول 3 عناصر
                    print(f"      {i+1}. {element['shape_name']} (ثقة: {element['confidence']:.3f})")
            
            # وصف المشهد
            scene_description = visual_inf.get('scene_description', '')
            if scene_description:
                print(f"   وصف المشهد: \"{scene_description}\"")
            
            # التكامل الدلالي
            semantic_integration = visual_inf.get('semantic_visual_integration', {})
            if semantic_integration:
                matches = semantic_integration.get('semantic_visual_matches', [])
                if matches:
                    print(f"   التكامل الدلالي: {len(matches)} تطابق")
            
            # التكامل الحلمي
            dream_integration = visual_inf.get('dream_visual_integration', {})
            if dream_integration:
                dream_matches = dream_integration.get('dream_visual_matches', [])
                if dream_matches:
                    print(f"   التكامل الحلمي: {len(dream_matches)} تطابق رمزي")
        
        # فحص الاستجابة المحسنة
        language_response = thinking_result['language_response']
        print(f"🗣️ الاستجابة المحسنة:")
        response_preview = language_response['final_response'][:300] + "..." if len(language_response['final_response']) > 300 else language_response['final_response']
        print(f"   {response_preview}")
        
        print()
        
        # عرض حالة النظام المتكامل
        print("📊 حالة النظام المتكامل مع الاستنباط البصري")
        print("-" * 50)
        
        system_status = cognitive_ai.get_system_status()
        
        print(f"🧠 النواة المعرفية:")
        cognitive_stats = system_status['cognitive_core_status']
        print(f"   الطبقات المعرفية: {cognitive_stats['total_layers']}")
        print(f"   التفاعلات: {cognitive_stats['total_interactions']}")
        print(f"   معدل النجاح: {cognitive_stats['success_rate']:.1%}")
        
        print(f"👁️ محرك الاستنباط البصري الذكي:")
        visual_stats = system_status['intelligent_visual_inference_engine_status']
        analysis_stats = visual_stats['analysis_stats']
        print(f"   الصور المحللة: {analysis_stats['images_analyzed']}")
        print(f"   العناصر المكتشفة: {analysis_stats['elements_detected']}")
        print(f"   معدل النجاح: {analysis_stats['success_rate']:.1%}")
        print(f"   متوسط الثقة: {analysis_stats['average_confidence']:.3f}")
        print(f"   تقييم الأداء: {visual_stats['performance_assessment']}")
        
        db_stats = visual_stats['database_stats']
        print(f"   قاعدة البيانات: {db_stats['shapes_in_database']} شكل، {db_stats['categories_supported']} فئة")
        
        print()
        print("🎉 اكتمل اختبار النظام المعرفي المتكامل مع الاستنباط البصري بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار النظام المتكامل: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """الدالة الرئيسية للاختبار."""
    
    print("🚀 بدء اختبار محرك الاستنباط البصري الذكي")
    print("👁️ العين المستنبطة - نظام ثوري يتعلم من صور قليلة")
    print("📐 يستخدم السماحية والمسافة الإقليدية للتعرف الذكي")
    print("🧠 مدمج مع النظام المعرفي الباهر")
    print()
    
    # اختبار المحرك المستقل
    engine_success = test_intelligent_visual_inference_engine()
    
    if engine_success:
        # اختبار النظام المتكامل
        integration_success = test_integrated_cognitive_visual_system()
        
        if integration_success:
            print("\n🏆 النتيجة النهائية: نجح الاختبار بامتياز!")
            print("🌟 محرك الاستنباط البصري الذكي متكامل مع النظام المعرفي الباهر!")
            print("👁️ العين المستنبطة جاهزة للاستنباط البصري الثوري!")
        else:
            print("\n⚠️ النتيجة النهائية: فشل في اختبار التكامل")
    else:
        print("\n❌ النتيجة النهائية: فشل في اختبار المحرك الأساسي")
    
    print("\n" + "=" * 70)
    print("🔬 انتهى اختبار محرك الاستنباط البصري الذكي")
    print(f"📅 وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
