#!/usr/bin/env python3
# test_revolutionary_content_transformer.py - اختبار محول المحتوى الثوري

import sys
import os
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد النظام المطور
from revolutionary_intelligence.revolutionary_content_transformer import (
    RevolutionaryContentTransformer, ContentTransformationConfig, 
    ContentType, EnhancementLevel
)
from revolutionary_intelligence.self_developing_cognitive_ai import SelfDevelopingCognitiveAI

def test_revolutionary_content_transformer():
    """اختبار محول المحتوى الثوري."""
    
    print("📚✨ اختبار محول المحتوى الثوري")
    print("=" * 70)
    print(f"📅 وقت الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🎨 يحول المحتوى الخام إلى إخراج فني باهر")
    print("🧬 مدعوم بنظريات باسل الثورية والوحدة الفنية")
    print()
    
    try:
        # إنشاء محول المحتوى الثوري
        print("🏗️ إنشاء محول المحتوى الثوري...")
        content_transformer = RevolutionaryContentTransformer("TestRevolutionaryContentTransformer")
        print("✅ تم إنشاء المحول بنجاح!")
        print()
        
        # اختبار 1: تحويل مقال تعليمي بسيط
        print("📖 اختبار 1: تحويل مقال تعليمي بسيط")
        print("-" * 50)
        
        simple_article = """
        # مقدمة في الذكاء الاصطناعي
        
        الذكاء الاصطناعي هو مجال علمي يهدف إلى إنشاء أنظمة قادرة على محاكاة الذكاء البشري.
        
        ## المفاهيم الأساسية
        
        يشمل الذكاء الاصطناعي عدة مفاهيم مهمة:
        - التعلم الآلي: قدرة الآلة على التعلم من البيانات
        - الشبكات العصبية: نماذج مستوحاة من الدماغ البشري
        - معالجة اللغة الطبيعية: فهم وتوليد اللغة البشرية
        
        ## التطبيقات العملية
        
        يستخدم الذكاء الاصطناعي في مجالات متنوعة مثل:
        - الطب: تشخيص الأمراض وتطوير العلاجات
        - التعليم: أنظمة التعلم التكيفي
        - النقل: السيارات ذاتية القيادة
        
        ## الخاتمة
        
        الذكاء الاصطناعي مجال سريع التطور يحمل إمكانيات هائلة لتحسين حياة البشر.
        """
        
        simple_config = ContentTransformationConfig(
            content_type=ContentType.EDUCATIONAL_MATERIAL,
            enhancement_level=EnhancementLevel.ADVANCED,
            include_visualizations=True,
            include_diagrams=True,
            include_illustrations=True,
            include_interactive_elements=True,
            apply_revolutionary_theories=True
        )
        
        simple_result = content_transformer.transform_content_revolutionary(simple_article, simple_config)
        
        print(f"📝 المحتوى الأصلي: {len(simple_article)} حرف")
        print(f"✨ المحتوى المحسن: {len(simple_result.enhanced_content)} حرف")
        print(f"📈 نسبة التحسين: {len(simple_result.enhanced_content) / len(simple_article):.2f}x")
        print(f"🎯 جودة التحسين: {simple_result.enhancement_quality:.3f}")
        print(f"⏱️ وقت التحويل: {simple_result.transformation_time:.3f} ثانية")
        
        # عرض العناصر المولدة
        print(f"🎨 العناصر المولدة:")
        print(f"   الرسوم التوضيحية: {len(simple_result.visualizations)}")
        print(f"   المخططات: {len(simple_result.diagrams)}")
        print(f"   الصور الفنية: {len(simple_result.illustrations)}")
        print(f"   العناصر التفاعلية: {len(simple_result.interactive_elements)}")
        
        # عرض الميزات الثورية
        revolutionary_features = simple_result.revolutionary_features
        print(f"🧬 الميزات الثورية:")
        applied_patterns = revolutionary_features.get('applied_patterns', [])
        print(f"   الأنماط المطبقة: {', '.join(applied_patterns) if applied_patterns else 'لا توجد'}")
        print(f"   درجة الجمال الثوري: {revolutionary_features.get('revolutionary_beauty_score', 0.0):.3f}")
        
        # عرض مجلد الإخراج
        if os.path.exists(simple_result.output_directory):
            files_count = len(os.listdir(simple_result.output_directory))
            print(f"📁 مجلد الإخراج: {os.path.basename(simple_result.output_directory)} ({files_count} ملف)")
        
        print()
        
        # اختبار 2: تحويل كتاب مع مستوى فني
        print("📚 اختبار 2: تحويل كتاب مع مستوى فني")
        print("-" * 50)
        
        book_content = """
        # كتاب: أسرار الكون والوجود
        
        ## الفصل الأول: نشأة الكون
        
        في البدء كان الانفجار العظيم، حدث كوني هائل غير مجرى التاريخ إلى الأبد.
        تشكلت النجوم والمجرات في رقصة كونية معقدة تحكمها قوانين الفيزياء.
        
        ### النظريات الأساسية
        
        - نظرية الانفجار العظيم
        - نظرية النسبية العامة
        - ميكانيكا الكم
        
        ## الفصل الثاني: الحياة والوعي
        
        الحياة معجزة كونية نادرة، والوعي هو أعظم ألغاز الوجود.
        كيف نشأ الوعي من المادة؟ هذا سؤال يحير العلماء والفلاسفة.
        
        ### مستويات الوعي
        
        - الوعي الأساسي: الإدراك البسيط
        - الوعي الذاتي: معرفة الذات
        - الوعي الكوني: الاتصال بالكل
        
        ## الفصل الثالث: المستقبل والتطور
        
        إلى أين نتجه؟ ما هو مصير الكون والحياة؟
        التطور مستمر، والمستقبل مليء بالإمكانيات اللامحدودة.
        """
        
        book_config = ContentTransformationConfig(
            content_type=ContentType.BOOK,
            enhancement_level=EnhancementLevel.ARTISTIC,
            include_visualizations=True,
            include_diagrams=True,
            include_illustrations=True,
            include_animations=True,
            include_interactive_elements=True,
            apply_revolutionary_theories=True,
            style="artistic",
            target_audience="general"
        )
        
        book_result = content_transformer.transform_content_revolutionary(book_content, book_config)
        
        print(f"📝 المحتوى الأصلي: {len(book_content)} حرف")
        print(f"✨ المحتوى المحسن: {len(book_result.enhanced_content)} حرف")
        print(f"📈 نسبة التحسين: {len(book_result.enhanced_content) / len(book_content):.2f}x")
        print(f"🎯 جودة التحسين: {book_result.enhancement_quality:.3f}")
        print(f"⏱️ وقت التحويل: {book_result.transformation_time:.3f} ثانية")
        
        # عرض التفاصيل المتقدمة
        print(f"🎨 العناصر المولدة المتقدمة:")
        print(f"   الرسوم التوضيحية: {len(book_result.visualizations)}")
        print(f"   المخططات: {len(book_result.diagrams)}")
        print(f"   الصور الفنية: {len(book_result.illustrations)}")
        print(f"   العناصر التفاعلية: {len(book_result.interactive_elements)}")
        
        # عرض العناصر التفاعلية بالتفصيل
        if book_result.interactive_elements:
            print(f"⚡ العناصر التفاعلية بالتفصيل:")
            for i, element in enumerate(book_result.interactive_elements):
                element_type = element.get('type', 'unknown')
                element_title = element.get('title', f'عنصر {i+1}')
                print(f"   {i+1}. {element_type}: {element_title}")
                
                features = element.get('features', [])
                if features:
                    print(f"      الميزات: {', '.join(features[:3])}")
        
        # عرض الميزات الثورية المتقدمة
        book_revolutionary_features = book_result.revolutionary_features
        print(f"🧬 الميزات الثورية المتقدمة:")
        book_applied_patterns = book_revolutionary_features.get('applied_patterns', [])
        print(f"   الأنماط المطبقة: {', '.join(book_applied_patterns)}")
        print(f"   درجة الجمال الثوري: {book_revolutionary_features.get('revolutionary_beauty_score', 0.0):.3f}")
        
        # عرض معاملات الأنماط
        pattern_parameters = book_revolutionary_features.get('pattern_parameters', {})
        if pattern_parameters:
            print(f"   معاملات الأنماط:")
            for pattern_name, params in pattern_parameters.items():
                print(f"      {pattern_name}: {len(params)} معامل")
        
        print()
        
        # اختبار 3: إحصائيات المحول
        print("📊 اختبار 3: إحصائيات المحول")
        print("-" * 50)
        
        transformer_stats = content_transformer.get_transformer_statistics()
        
        print(f"🏷️ معلومات المحول:")
        print(f"   الاسم: {transformer_stats['transformer_info']['name']}")
        print(f"   النوع: {transformer_stats['transformer_info']['type']}")
        
        print(f"📈 إحصائيات التحويل:")
        transformation_stats = transformer_stats['transformation_stats']
        print(f"   المحتوى المحول: {transformation_stats['content_transformed']}")
        print(f"   الرسوم التوضيحية: {transformation_stats['visualizations_created']}")
        print(f"   المخططات: {transformation_stats['diagrams_generated']}")
        print(f"   الصور الفنية: {transformation_stats['illustrations_made']}")
        print(f"   العناصر التفاعلية: {transformation_stats['interactive_elements_added']}")
        print(f"   متوسط جودة التحسين: {transformation_stats['average_enhancement_quality']:.3f}")
        print(f"   متوسط وقت التحويل: {transformation_stats['average_transformation_time']:.3f} ثانية")
        print(f"   الأنماط الثورية المطبقة: {transformation_stats['revolutionary_patterns_applied']}")
        
        print(f"🛠️ القدرات:")
        capabilities = transformer_stats['capabilities']
        print(f"   أنواع المحتوى: {capabilities['content_types']}")
        print(f"   مستويات التحسين: {capabilities['enhancement_levels']}")
        print(f"   استراتيجيات التحويل: {capabilities['transformation_strategies']}")
        print(f"   الأنماط الثورية: {capabilities['revolutionary_patterns']}")
        
        print(f"🌟 الميزات الثورية:")
        rev_features = transformer_stats['revolutionary_features']
        print(f"   تكامل نظريات باسل: {'✅' if rev_features['basil_theories_integration'] else '❌'}")
        print(f"   تكامل الوحدة الفنية: {'✅' if rev_features['artistic_unit_integration'] else '❌'}")
        print(f"   التحليل الدلالي: {'✅' if rev_features['semantic_analysis'] else '❌'}")
        print(f"   تفسير الأحلام: {'✅' if rev_features['dream_interpretation'] else '❌'}")
        print(f"   توليد الوسائط المتعددة: {'✅' if rev_features['multimedia_generation'] else '❌'}")
        print(f"   الاستنباط البصري: {'✅' if rev_features['visual_inference'] else '❌'}")
        print(f"   العناصر التفاعلية: {'✅' if rev_features['interactive_elements'] else '❌'}")
        
        print(f"🏆 تقييم الأداء: {transformer_stats['performance_assessment']}")
        
        print()
        print("🎉 اكتمل اختبار محول المحتوى الثوري بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار المحول: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_integrated_cognitive_content_system():
    """اختبار النظام المعرفي المتكامل مع تحويل المحتوى."""
    
    print("\n🧠📚 اختبار النظام المعرفي المتكامل مع تحويل المحتوى")
    print("=" * 70)
    
    try:
        # إنشاء النظام المتكامل
        print("🏗️ إنشاء النظام المعرفي المتكامل...")
        cognitive_ai = SelfDevelopingCognitiveAI("TestContentCognitiveAI")
        print("✅ تم إنشاء النظام بنجاح!")
        print()
        
        # اختبار التفكير العميق مع تحويل المحتوى
        print("🧠 اختبار التفكير العميق مع تحويل المحتوى")
        print("-" * 50)
        
        content_request = {
            'text': 'حول هذا المحتوى إلى إخراج فني باهر مع رسوم توضيحية وعناصر تفاعلية',
            'content': """
            # دليل تعلم البرمجة
            
            البرمجة هي فن وعلم كتابة التعليمات للحاسوب.
            
            ## الخطوات الأساسية
            
            1. فهم المشكلة
            2. تصميم الحل
            3. كتابة الكود
            4. اختبار البرنامج
            
            ## لغات البرمجة الشائعة
            
            - Python: سهلة التعلم ومتعددة الاستخدامات
            - JavaScript: لغة الويب الأساسية
            - Java: قوية ومستقرة للتطبيقات الكبيرة
            """
        }
        
        thinking_result = cognitive_ai.think_deeply_and_develop(
            content_request,
            thinking_depth=4,
            enable_self_development=True
        )
        
        print(f"📝 المدخل: {content_request['text']}")
        print(f"📄 طول المحتوى: {len(content_request['content'])} حرف")
        print(f"🎯 جودة التفكير: {thinking_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {thinking_result['performance_improvement']:.3f}")
        
        # فحص تحويل المحتوى
        if 'content_transformation' in thinking_result:
            content_trans = thinking_result['content_transformation']
            print(f"📚 تحويل المحتوى:")
            print(f"   جودة التحويل: {content_trans['transformation_quality']:.3f}")
            
            # معلومات استخراج المحتوى
            content_extraction = content_trans['content_extraction']
            print(f"   استخراج المحتوى:")
            print(f"      وجود المحتوى: {'✅' if content_extraction.get('content_found') else '❌'}")
            print(f"      طول المحتوى: {content_extraction.get('content_length', 0)} حرف")
            
            # تحليل التحسين
            enhancement_analysis = content_trans.get('enhancement_analysis', {})
            if enhancement_analysis:
                print(f"   تحليل التحسين:")
                print(f"      نسبة التحسين: {enhancement_analysis.get('improvement_ratio', 0.0):.2f}x")
                print(f"      العناصر البصرية: {enhancement_analysis.get('visual_elements_count', 0)}")
                print(f"      العناصر التفاعلية: {enhancement_analysis.get('interactive_elements_count', 0)}")
            
            # العناصر البصرية
            visual_elements = content_trans.get('visual_elements', [])
            if visual_elements:
                print(f"   العناصر البصرية ({len(visual_elements)} عنصر):")
                for i, element in enumerate(visual_elements[:3]):  # أول 3 عناصر
                    print(f"      {i+1}. {element['type']}: {element['description']}")
            
            # الميزات التفاعلية
            interactive_features = content_trans.get('interactive_features', [])
            if interactive_features:
                print(f"   الميزات التفاعلية ({len(interactive_features)} ميزة):")
                for i, feature in enumerate(interactive_features[:3]):  # أول 3 ميزات
                    print(f"      {i+1}. {feature['type']}: {feature['title']}")
            
            # مجلد الإخراج
            output_directory = content_trans.get('output_directory', '')
            if output_directory:
                print(f"   مجلد الإخراج: {os.path.basename(output_directory)}")
        
        # فحص الاستجابة المحسنة
        language_response = thinking_result['language_response']
        print(f"🗣️ الاستجابة المحسنة:")
        response_preview = language_response['final_response'][:300] + "..." if len(language_response['final_response']) > 300 else language_response['final_response']
        print(f"   {response_preview}")
        
        print()
        
        # عرض حالة النظام المتكامل
        print("📊 حالة النظام المتكامل مع تحويل المحتوى")
        print("-" * 50)
        
        system_status = cognitive_ai.get_system_status()
        
        print(f"🧠 النواة المعرفية:")
        cognitive_stats = system_status['cognitive_core_status']
        print(f"   الطبقات المعرفية: {cognitive_stats['total_layers']}")
        print(f"   التفاعلات: {cognitive_stats['total_interactions']}")
        print(f"   معدل النجاح: {cognitive_stats['success_rate']:.1%}")
        
        print(f"📚 محول المحتوى الثوري:")
        content_stats = system_status['revolutionary_content_transformer_status']
        transformation_stats = content_stats['transformation_stats']
        print(f"   المحتوى المحول: {transformation_stats['content_transformed']}")
        print(f"   العناصر البصرية: {transformation_stats['visualizations_created'] + transformation_stats['diagrams_generated'] + transformation_stats['illustrations_made']}")
        print(f"   العناصر التفاعلية: {transformation_stats['interactive_elements_added']}")
        print(f"   متوسط الجودة: {transformation_stats['average_enhancement_quality']:.3f}")
        print(f"   تقييم الأداء: {content_stats['performance_assessment']}")
        
        print()
        print("🎉 اكتمل اختبار النظام المعرفي المتكامل مع تحويل المحتوى بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار النظام المتكامل: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """الدالة الرئيسية للاختبار."""
    
    print("🚀 بدء اختبار محول المحتوى الثوري")
    print("📚 يحول المحتوى الخام إلى إخراج فني باهر")
    print("🎨 مع شروحات ومخططات وصور توضيحية وعناصر تفاعلية")
    print("🧬 مدعوم بنظريات باسل الثورية والوحدة الفنية")
    print()
    
    # اختبار المحول المستقل
    transformer_success = test_revolutionary_content_transformer()
    
    if transformer_success:
        # اختبار النظام المتكامل
        integration_success = test_integrated_cognitive_content_system()
        
        if integration_success:
            print("\n🏆 النتيجة النهائية: نجح الاختبار بامتياز!")
            print("🌟 محول المحتوى الثوري متكامل مع النظام المعرفي الباهر!")
            print("📚 النظام جاهز لتحويل المحتوى بطرق ثورية!")
        else:
            print("\n⚠️ النتيجة النهائية: فشل في اختبار التكامل")
    else:
        print("\n❌ النتيجة النهائية: فشل في اختبار المحول الأساسي")
    
    print("\n" + "=" * 70)
    print("🔬 انتهى اختبار محول المحتوى الثوري")
    print(f"📅 وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
