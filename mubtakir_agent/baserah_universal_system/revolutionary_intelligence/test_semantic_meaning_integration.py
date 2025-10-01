#!/usr/bin/env python3
# test_semantic_meaning_integration.py - اختبار تكامل محرك الدلالة المعنوية

import sys
import os
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد النظام المطور
from revolutionary_intelligence.semantic_meaning_engine import SemanticMeaningEngine
from revolutionary_intelligence.self_developing_cognitive_ai import SelfDevelopingCognitiveAI

def test_semantic_meaning_engine():
    """اختبار محرك الدلالة المعنوية الثوري."""
    
    print("🧠✨ اختبار محرك الدلالة المعنوية الثوري")
    print("=" * 70)
    print(f"📅 وقت الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        # إنشاء محرك الدلالة المعنوية
        print("🏗️ إنشاء محرك الدلالة المعنوية...")
        semantic_engine = SemanticMeaningEngine("TestSemanticEngine")
        print("✅ تم إنشاء المحرك بنجاح!")
        print()
        
        # اختبار 1: إنشاء معادلة دلالية
        print("🧮 اختبار 1: إنشاء معادلة دلالية")
        print("-" * 50)
        
        word = "إنسان"
        shape_equation = "sigmoid(x) + linear(y)"
        non_mathematical_terms = {
            'psychological': 'تفكير وإدراك',
            'emotional': 'مشاعر وأحاسيس',
            'social': 'تفاعل اجتماعي',
            'physical': 'جسم مادي'
        }
        
        semantic_equation = semantic_engine.create_semantic_equation(
            word, shape_equation, non_mathematical_terms
        )
        
        print(f"📝 الكلمة: {semantic_equation['word']}")
        print(f"🧮 معادلة الشكل: {semantic_equation['shape_equation']}")
        print(f"🧠 نوع المعادلة: {semantic_equation['equation_type']}")
        print(f"⚖️ الوزن الدلالي: {semantic_equation['semantic_weight']:.3f}")
        print(f"🔄 عامل التكيف: {semantic_equation['adaptability_factor']:.3f}")
        print()
        
        # اختبار 2: تحليل جملة دلالياً
        print("📝 اختبار 2: تحليل جملة دلالياً")
        print("-" * 50)
        
        sentence = "إنسان يمشي في طريق جميل"
        sentence_analysis = semantic_engine.parse_semantic_sentence(sentence)
        
        print(f"📝 الجملة: {sentence_analysis['original_sentence']}")
        print(f"👥 الكائنات: {len(sentence_analysis['entities'])}")
        print(f"⚡ الأفعال: {len(sentence_analysis['actions'])}")
        print(f"🔗 العلاقات: {len(sentence_analysis['relations'])}")
        print(f"🔣 التمثيل الرمزي: {sentence_analysis['symbolic_representation']}")
        print(f"📊 اكتمال المعنى: {sentence_analysis['meaning_completeness']:.3f}")
        
        print(f"🏗️ الهيكل الدلالي:")
        structure = sentence_analysis['semantic_structure']
        if structure['subject']:
            print(f"   الفاعل: {structure['subject'].get('word', 'غير محدد')}")
        if structure['predicate']:
            print(f"   المسند: {structure['predicate'].get('word', 'غير محدد')}")
        if structure['object']:
            print(f"   المفعول: {structure['object'].get('word', 'غير محدد')}")
        
        print()
        
        # اختبار 3: التعلم من نصوص الإنترنت
        print("🌐 اختبار 3: التعلم من نصوص الإنترنت")
        print("-" * 50)
        
        internet_texts = [
            "الطالب يدرس في المكتبة",
            "المعلم يشرح الدرس للطلاب",
            "الكتاب يحتوي على معلومات مفيدة",
            "الطلاب يحبون القراءة والتعلم",
            "المدرسة مكان للتعليم والتربية"
        ]
        
        learning_result = semantic_engine.learn_from_internet_text(internet_texts)
        
        print(f"📊 نتائج التعلم:")
        print(f"   📝 نصوص معالجة: {learning_result['texts_processed']}")
        print(f"   🔗 علاقات جديدة: {learning_result['new_associations']}")
        print(f"   📈 نمو الشبكة: {learning_result['network_growth']:.3f}")
        print(f"   🎯 أنماط مكتشفة: {len(learning_result['discovered_patterns'])}")
        
        print(f"🧠 شبكة العصف الذهني:")
        brainstorming = learning_result['brainstorming_network']
        if brainstorming.get('central_concepts'):
            print(f"   🎯 المفاهيم المركزية: {', '.join(brainstorming['central_concepts'][:5])}")
        
        if brainstorming.get('creative_connections'):
            print(f"   💡 الروابط الإبداعية:")
            for i, connection in enumerate(brainstorming['creative_connections'][:3], 1):
                path = ' → '.join(connection['path'])
                score = connection['creativity_score']
                print(f"      {i}. {path} (إبداع: {score:.3f})")
        
        print()
        
        # اختبار 4: توليد تحويل دلالي
        print("🔄 اختبار 4: توليد تحويل دلالي")
        print("-" * 50)
        
        # إضافة مفهوم آخر أولاً
        semantic_engine.create_semantic_equation(
            "شجرة",
            "exponential(growth)",
            {
                'physical': 'نمو وأوراق',
                'environmental': 'طبيعة وبيئة',
                'symbolic': 'حياة ونمو'
            }
        )
        
        transformation = semantic_engine.generate_semantic_transformation("إنسان", "شجرة")
        
        print(f"🔄 التحويل: {transformation['source_concept']} → {transformation['target_concept']}")
        print(f"🧮 معادلة المصدر: {transformation['source_equation']}")
        print(f"🧮 معادلة الهدف: {transformation['target_equation']}")
        print(f"🎯 إمكانية التحويل: {transformation['transformation_feasibility']:.3f}")
        
        print(f"📋 خطوات التحويل:")
        for i, step in enumerate(transformation['transformation_steps'], 1):
            print(f"   {i}. {step}")
        
        print(f"🔧 التكيفات المطلوبة:")
        for adaptation in transformation['required_adaptations']:
            print(f"   • {adaptation}")
        
        print()
        
        # اختبار 5: إحصائيات المحرك
        print("📊 اختبار 5: إحصائيات المحرك")
        print("-" * 50)
        
        engine_stats = semantic_engine.get_engine_statistics()
        
        print(f"🏷️ معلومات المحرك:")
        print(f"   الاسم: {engine_stats['engine_info']['name']}")
        print(f"   النوع: {engine_stats['engine_info']['type']}")
        
        print(f"🗄️ إحصائيات قاعدة البيانات:")
        db_stats = engine_stats['database_stats']
        print(f"   الكائنات: {db_stats['total_entities']}")
        print(f"   الأفعال: {db_stats['total_actions']}")
        print(f"   العلاقات: {db_stats['total_relations']}")
        print(f"   المشاعر: {db_stats['total_emotions']}")
        print(f"   المفاهيم: {db_stats['total_concepts']}")
        
        print(f"🕸️ إحصائيات الشبكة:")
        network_stats = engine_stats['network_stats']
        print(f"   العقد: {network_stats['total_nodes']}")
        print(f"   الروابط: {network_stats['total_edges']}")
        print(f"   التعقيد: {network_stats['network_complexity']:.3f}")
        print(f"   المجموعات: {network_stats['clusters_count']}")
        
        print(f"📚 إحصائيات التعلم:")
        learning_stats = engine_stats['learning_stats']
        print(f"   النصوص المعالجة: {learning_stats['processed_texts']}")
        print(f"   الأنماط المتعلمة: {learning_stats['learned_patterns']}")
        print(f"   دورات التعلم: {learning_stats['learning_iterations']}")
        
        print(f"🏆 تقييم الأداء: {engine_stats['performance_assessment']}")
        
        print()
        print("🎉 اكتمل اختبار محرك الدلالة المعنوية الثوري بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار المحرك: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_integrated_cognitive_system():
    """اختبار النظام المعرفي المتكامل مع الدلالة المعنوية."""
    
    print("\n🧠🔗 اختبار النظام المعرفي المتكامل")
    print("=" * 60)
    
    try:
        # إنشاء النظام المتكامل
        print("🏗️ إنشاء النظام المعرفي المتكامل...")
        cognitive_ai = SelfDevelopingCognitiveAI("TestIntegratedCognitiveAI")
        print("✅ تم إنشاء النظام بنجاح!")
        print()
        
        # اختبار التفكير العميق مع الدلالة المعنوية
        print("🧠 اختبار التفكير العميق مع الدلالة المعنوية")
        print("-" * 50)
        
        complex_input = "كيف يمكن للإنسان أن يتحول من حالة الجهل إلى حالة المعرفة؟"
        
        thinking_result = cognitive_ai.think_deeply_and_develop(
            complex_input,
            thinking_depth=2,
            enable_self_development=True
        )
        
        print(f"📝 المدخل: {complex_input}")
        print(f"🎯 جودة التفكير: {thinking_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {thinking_result['performance_improvement']:.3f}")
        
        # عرض التحليل الدلالي
        if 'semantic_analysis' in thinking_result:
            semantic = thinking_result['semantic_analysis']
            print(f"🧠 التحليل الدلالي:")
            print(f"   📊 اكتمال المعنى: {semantic.get('semantic_completeness', 0.0):.3f}")
            print(f"   🧮 معادلات دلالية: {len(semantic.get('semantic_equations', {}))}")
            print(f"   🔄 تحويلات معنوية: {len(semantic.get('meaning_transformations', {}))}")
            
            # عرض المعادلات الدلالية
            if semantic.get('semantic_equations'):
                print(f"   📋 المعادلات المكتشفة:")
                for word, equation in semantic['semantic_equations'].items():
                    print(f"      {word}: {equation.get('equation_type', 'unknown')}")
        
        # عرض الاستجابة المحسنة
        language_response = thinking_result['language_response']
        print(f"🗣️ الاستجابة:")
        print(f"   {language_response['final_response']}")
        
        if 'semantic_enhancement' in language_response:
            enhancement = language_response['semantic_enhancement']
            print(f"✨ التحسين الدلالي:")
            print(f"   اكتمال دلالي: {enhancement['semantic_completeness']:.3f}")
            print(f"   معادلات: {enhancement['equations_count']}")
            print(f"   تحويلات: {enhancement['transformations_count']}")
        
        print()
        
        # عرض حالة النظام المتكامل
        print("📊 حالة النظام المتكامل")
        print("-" * 50)
        
        system_status = cognitive_ai.get_system_status()
        
        print(f"🧠 النواة المعرفية:")
        cognitive_stats = system_status['cognitive_core_status']
        print(f"   التفاعلات: {cognitive_stats['total_interactions']}")
        print(f"   معدل النجاح: {cognitive_stats['success_rate']:.1%}")
        
        print(f"🗣️ النماذج اللغوية:")
        for model_name, model_stats in system_status['language_models_status'].items():
            print(f"   {model_name}: {model_stats['total_generations']} توليد")
        
        print(f"🧠 محرك الدلالة المعنوية:")
        semantic_stats = system_status['semantic_meaning_engine_status']
        db_stats = semantic_stats['database_stats']
        network_stats = semantic_stats['network_stats']
        print(f"   قاعدة البيانات: {sum(db_stats.values())} عنصر")
        print(f"   الشبكة: {network_stats['total_nodes']} عقدة، {network_stats['total_edges']} رابط")
        print(f"   التعقيد: {network_stats['network_complexity']:.3f}")
        print(f"   التقييم: {semantic_stats['performance_assessment']}")
        
        print()
        print("🎉 اكتمل اختبار النظام المعرفي المتكامل بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار النظام المتكامل: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """الدالة الرئيسية للاختبار."""
    
    print("🚀 بدء اختبار تكامل محرك الدلالة المعنوية")
    print("🔬 وفقاً للرؤية الثورية من ملف 'دلالة معنوية.txt'")
    print("🧮 ربط الدلالة بالشكل والمعادلات")
    print("🕸️ بناء شبكة علاقات معقدة تشبه العصف الذهني")
    print("🔄 معادلة الشكل العام + حدود غير رياضية")
    print()
    
    # اختبار المحرك المستقل
    engine_success = test_semantic_meaning_engine()
    
    if engine_success:
        # اختبار النظام المتكامل
        integration_success = test_integrated_cognitive_system()
        
        if integration_success:
            print("\n🏆 النتيجة النهائية: نجح الاختبار بامتياز!")
            print("🌟 محرك الدلالة المعنوية متكامل مع النظام المعرفي الباهر!")
            print("🚀 النظام جاهز للتطبيقات المتقدمة!")
        else:
            print("\n⚠️ النتيجة النهائية: فشل في اختبار التكامل")
    else:
        print("\n❌ النتيجة النهائية: فشل في اختبار المحرك الأساسي")
    
    print("\n" + "=" * 70)
    print("🔬 انتهى اختبار تكامل محرك الدلالة المعنوية")
    print(f"📅 وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
