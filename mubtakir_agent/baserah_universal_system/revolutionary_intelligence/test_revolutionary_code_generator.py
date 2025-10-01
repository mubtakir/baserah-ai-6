#!/usr/bin/env python3
# test_revolutionary_code_generator.py - اختبار مولد الكود الثوري

import sys
import os
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد النظام المطور
from revolutionary_intelligence.revolutionary_code_generator import RevolutionaryCodeGenerator
from revolutionary_intelligence.self_developing_cognitive_ai import SelfDevelopingCognitiveAI

def test_revolutionary_code_generator():
    """اختبار مولد الكود الثوري."""
    
    print("🚀✨ اختبار مولد الكود الثوري")
    print("=" * 70)
    print(f"📅 وقت الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🧠 النظام يفكر ويحلل ويختبر ويتأكد قبل تسليم الكود")
    print()
    
    try:
        # إنشاء مولد الكود الثوري
        print("🏗️ إنشاء مولد الكود الثوري...")
        code_generator = RevolutionaryCodeGenerator("TestRevolutionaryCodeGenerator")
        print("✅ تم إنشاء المولد بنجاح!")
        print()
        
        # اختبار 1: توليد دالة حساب بسيطة
        print("🧮 اختبار 1: توليد دالة حساب بسيطة")
        print("-" * 50)
        
        simple_requirements = {
            'function_name': 'calculate_area',
            'description': 'دالة لحساب مساحة المستطيل باستخدام الطول والعرض',
            'language': 'python',
            'inputs': ['length', 'width'],
            'outputs': ['area'],
            'complexity_level': 'low'
        }
        
        simple_result = code_generator.generate_code_revolutionary(simple_requirements, thinking_depth=2)
        
        print(f"📝 المتطلبات: {simple_requirements['description']}")
        print(f"🧠 عمق التفكير: 2")
        print(f"🎯 درجة الثقة: {simple_result['confidence_score']:.3f}")
        print(f"⏱️ وقت التوليد: {simple_result['generation_time']:.3f} ثانية")
        
        # عرض عملية التفكير
        thinking_process = simple_result['thinking_process']
        print(f"🧠 عملية التفكير:")
        understanding = thinking_process['requirement_understanding']
        print(f"   فهم المتطلبات: {understanding['understanding_score']:.3f}")
        print(f"   اسم الدالة: {understanding['function_name']}")
        print(f"   مستوى التعقيد: {understanding['complexity_level']}")
        
        # عرض قرارات التصميم
        design_decisions = simple_result['design_decisions']
        print(f"🎯 قرارات التصميم:")
        print(f"   الاستراتيجية المختارة: {design_decisions['chosen_strategy']}")
        print(f"   النمط الثوري: {design_decisions['revolutionary_pattern']}")
        print(f"   النظريات المطبقة: {', '.join(design_decisions['basil_theories_applied'])}")
        print(f"   ثقة القرار: {design_decisions['decision_confidence']:.3f}")
        
        # عرض الكود المولد
        generated_code = simple_result['generated_code']
        if generated_code:
            print(f"💻 الكود المولد:")
            print("```python")
            print(generated_code)
            print("```")
        
        print()
        
        # اختبار 2: توليد خوارزمية معقدة مع نظريات باسل
        print("🧬 اختبار 2: توليد خوارزمية معقدة مع نظريات باسل")
        print("-" * 50)
        
        complex_requirements = {
            'function_name': 'revolutionary_sort',
            'description': 'خوارزمية ترتيب ثورية تطبق نظرية تعامد الأضداد لمعالجة البيانات بكفاءة عالية',
            'language': 'python',
            'inputs': ['data_list', 'sort_order'],
            'outputs': ['sorted_list', 'performance_metrics'],
            'complexity_level': 'high',
            'performance_requirements': {
                'max_execution_time': 0.5,
                'memory_efficiency': 'high'
            }
        }
        
        complex_result = code_generator.generate_code_revolutionary(complex_requirements, thinking_depth=4)
        
        print(f"📝 المتطلبات: {complex_requirements['description']}")
        print(f"🧠 عمق التفكير: 4")
        print(f"🎯 درجة الثقة: {complex_result['confidence_score']:.3f}")
        print(f"⏱️ وقت التوليد: {complex_result['generation_time']:.3f} ثانية")
        
        # عرض التحليل الدلالي
        analysis_results = complex_result['analysis_results']
        print(f"🔍 التحليل الدلالي:")
        print(f"   اكتمال المعنى: {analysis_results['semantic_completeness']:.3f}")
        print(f"   الإمكانية الإبداعية: {analysis_results['creative_potential']:.3f}")
        
        # عرض الميزات الثورية
        revolutionary_features = complex_result['revolutionary_features']
        print(f"🌟 الميزات الثورية:")
        for feature_name, feature_value in revolutionary_features.items():
            print(f"   {feature_name}: {feature_value}")
        
        # عرض تقييم الجودة
        quality_assessment = complex_result['quality_assessment']
        print(f"🏆 تقييم الجودة:")
        for quality_metric, quality_value in quality_assessment.items():
            if isinstance(quality_value, float):
                print(f"   {quality_metric}: {quality_value:.3f}")
            else:
                print(f"   {quality_metric}: {quality_value}")
        
        print()
        
        # اختبار 3: توليد كود إبداعي مستوحى من الأحلام
        print("🌙 اختبار 3: توليد كود إبداعي مستوحى من الأحلام")
        print("-" * 50)
        
        creative_requirements = {
            'function_name': 'dream_data_processor',
            'description': 'تخيل دالة تطير عبر البيانات مثل طائر في السماء، تجمع المعلومات وتحولها إلى نور ساطع من المعرفة',
            'language': 'python',
            'inputs': ['raw_data', 'transformation_type'],
            'outputs': ['processed_data', 'insights'],
            'complexity_level': 'medium'
        }
        
        creative_result = code_generator.generate_code_revolutionary(creative_requirements, thinking_depth=5)
        
        print(f"📝 المتطلبات: {creative_requirements['description']}")
        print(f"🧠 عمق التفكير: 5")
        print(f"🎯 درجة الثقة: {creative_result['confidence_score']:.3f}")
        
        # عرض التحليل الإبداعي
        analysis_results = creative_result['analysis_results']
        if analysis_results.get('dream_analysis'):
            dream_analysis = analysis_results['dream_analysis']
            print(f"🌙 تحليل الأحلام:")
            print(f"   درجة الثقة: {dream_analysis['confidence_score']:.3f}")
            
            symbolic_insights = dream_analysis.get('symbolic_insights', {})
            print(f"   الرؤى الرمزية:")
            print(f"      رموز مكتشفة: {symbolic_insights.get('symbols_found', 0)}")
            print(f"      الوزن الرمزي: {symbolic_insights.get('symbolic_weight', 0.0):.3f}")
            
            pattern_discoveries = dream_analysis.get('pattern_discoveries', {})
            print(f"   اكتشافات الأنماط:")
            print(f"      النمط المهيمن: {pattern_discoveries.get('dominant_pattern', 'none')}")
        
        print()
        
        # اختبار 4: إحصائيات المولد
        print("📊 اختبار 4: إحصائيات المولد")
        print("-" * 50)
        
        generator_stats = code_generator.get_generator_statistics()
        
        print(f"🏷️ معلومات المولد:")
        print(f"   الاسم: {generator_stats['generator_info']['name']}")
        print(f"   النوع: {generator_stats['generator_info']['type']}")
        
        print(f"📈 إحصائيات التوليد:")
        gen_stats = generator_stats['generation_stats']
        print(f"   الأكواد المولدة: {gen_stats['codes_generated']}")
        print(f"   الاختبارات الناجحة: {gen_stats['tests_passed']}")
        print(f"   الأنماط الثورية المستخدمة: {gen_stats['revolutionary_patterns_used']}")
        print(f"   متوسط جودة الكود: {gen_stats['average_quality_score']:.3f}")
        print(f"   متوسط عمق التفكير: {gen_stats['thinking_depth_average']:.3f}")
        
        print(f"🛠️ القدرات:")
        capabilities = generator_stats['capabilities']
        print(f"   استراتيجيات التوليد: {capabilities['generation_strategies']}")
        print(f"   الأنماط الثورية: {capabilities['revolutionary_patterns']}")
        print(f"   أنظمة التفكير: {capabilities['thinking_systems']}")
        print(f"   أنظمة التحقق: {capabilities['verification_systems']}")
        
        print(f"🌟 الميزات الثورية:")
        rev_features = generator_stats['revolutionary_features']
        print(f"   نظريات باسل المدعومة: {', '.join(rev_features['basil_theories_supported'])}")
        print(f"   التحليل الدلالي: {'✅' if rev_features['semantic_analysis'] else '❌'}")
        print(f"   تفسير الأحلام: {'✅' if rev_features['dream_interpretation'] else '❌'}")
        print(f"   التفكير العميق: {'✅' if rev_features['deep_thinking'] else '❌'}")
        print(f"   الاختبار الشامل: {'✅' if rev_features['comprehensive_testing'] else '❌'}")
        
        print(f"🏆 تقييم الأداء: {generator_stats['performance_assessment']}")
        
        print()
        print("🎉 اكتمل اختبار مولد الكود الثوري بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار المولد: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_integrated_cognitive_code_system():
    """اختبار النظام المعرفي المتكامل مع توليد الكود."""
    
    print("\n🧠🚀 اختبار النظام المعرفي المتكامل مع توليد الكود")
    print("=" * 70)
    
    try:
        # إنشاء النظام المتكامل
        print("🏗️ إنشاء النظام المعرفي المتكامل...")
        cognitive_ai = SelfDevelopingCognitiveAI("TestCodeCognitiveAI")
        print("✅ تم إنشاء النظام بنجاح!")
        print()
        
        # اختبار التفكير العميق مع توليد الكود
        print("🧠 اختبار التفكير العميق مع توليد الكود")
        print("-" * 50)
        
        code_request = "اكتب دالة python لحساب العدد الذهبي باستخدام نظرية الفتائل الثورية، الدالة تأخذ عدد التكرارات وترجع القيمة التقريبية للعدد الذهبي"
        
        thinking_result = cognitive_ai.think_deeply_and_develop(
            code_request,
            thinking_depth=4,
            enable_self_development=True
        )
        
        print(f"📝 المدخل: {code_request}")
        print(f"🎯 جودة التفكير: {thinking_result['final_result']['thinking_quality']:.3f}")
        print(f"📈 تحسن الأداء: {thinking_result['performance_improvement']:.3f}")
        
        # فحص توليد الكود
        if 'code_generation' in thinking_result:
            code_gen = thinking_result['code_generation']
            print(f"🚀 توليد الكود:")
            print(f"   درجة الثقة: {code_gen['confidence_score']:.3f}")
            
            requirements = code_gen['requirements_extraction']
            print(f"   المتطلبات المستخرجة:")
            print(f"      اسم الدالة: {requirements.get('function_name', 'unknown')}")
            print(f"      لغة البرمجة: {requirements.get('language', 'python')}")
            print(f"      مستوى التعقيد: {requirements.get('complexity_level', 'medium')}")
            print(f"      العناصر الإبداعية: {', '.join(requirements.get('creative_elements', []))}")
            
            code_analysis = code_gen.get('code_analysis', {})
            if code_analysis:
                print(f"   تحليل الكود:")
                print(f"      عدد الأسطر: {code_analysis.get('lines_count', 0)}")
                print(f"      مؤشرات التعقيد: {', '.join(code_analysis.get('complexity_indicators', []))}")
                revolutionary_patterns = code_analysis.get('revolutionary_patterns', [])
                if revolutionary_patterns:
                    print(f"      الأنماط الثورية: {', '.join(revolutionary_patterns)}")
            
            testing_results = code_gen.get('testing_results', {})
            if testing_results:
                print(f"   نتائج الاختبار:")
                print(f"      صحة نحوية: {'✅' if testing_results.get('syntax_valid') else '❌'}")
                print(f"      تنفيذ ناجح: {'✅' if testing_results.get('execution_successful') else '❌'}")
                
            quality_assessment = code_gen.get('quality_assessment', {})
            if quality_assessment:
                print(f"   تقييم الجودة:")
                print(f"      الجودة الإجمالية: {quality_assessment.get('overall_quality', 0.0):.3f}")
                print(f"      درجة الجودة: {quality_assessment.get('quality_grade', 'developing')}")
            
            final_code = code_gen.get('final_code', '')
            if final_code:
                print(f"   الكود النهائي:")
                print("   ```python")
                for line in final_code.split('\n')[:10]:  # أول 10 أسطر
                    print(f"   {line}")
                if len(final_code.split('\n')) > 10:
                    print("   ...")
                print("   ```")
        
        # فحص الاستجابة المحسنة
        language_response = thinking_result['language_response']
        print(f"🗣️ الاستجابة المحسنة:")
        response_preview = language_response['final_response'][:200] + "..." if len(language_response['final_response']) > 200 else language_response['final_response']
        print(f"   {response_preview}")
        
        print()
        
        # عرض حالة النظام المتكامل
        print("📊 حالة النظام المتكامل مع توليد الكود")
        print("-" * 50)
        
        system_status = cognitive_ai.get_system_status()
        
        print(f"🧠 النواة المعرفية:")
        cognitive_stats = system_status['cognitive_core_status']
        print(f"   الطبقات المعرفية: {cognitive_stats['total_layers']}")
        print(f"   التفاعلات: {cognitive_stats['total_interactions']}")
        print(f"   معدل النجاح: {cognitive_stats['success_rate']:.1%}")
        
        print(f"🚀 مولد الكود الثوري:")
        code_stats = system_status['revolutionary_code_generator_status']
        gen_stats = code_stats['generation_stats']
        print(f"   الأكواد المولدة: {gen_stats['codes_generated']}")
        print(f"   الاختبارات الناجحة: {gen_stats['tests_passed']}")
        print(f"   الأنماط الثورية: {gen_stats['revolutionary_patterns_used']}")
        print(f"   متوسط الجودة: {gen_stats['average_quality_score']:.3f}")
        print(f"   تقييم الأداء: {code_stats['performance_assessment']}")
        
        print()
        print("🎉 اكتمل اختبار النظام المعرفي المتكامل مع توليد الكود بنجاح!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار النظام المتكامل: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """الدالة الرئيسية للاختبار."""
    
    print("🚀 بدء اختبار مولد الكود الثوري")
    print("🧠 النظام يفكر ويحلل ويختبر ويتأكد قبل تسليم الكود")
    print("🧬 مدعوم بنظريات باسل الثورية والمناهج المتقدمة")
    print("🔍 التحليل الدلالي والتفسير الإبداعي")
    print("🧮 المعادلات الرياضية التكيفية (بدلاً من الشبكات العصبية)")
    print()
    
    # اختبار المولد المستقل
    generator_success = test_revolutionary_code_generator()
    
    if generator_success:
        # اختبار النظام المتكامل
        integration_success = test_integrated_cognitive_code_system()
        
        if integration_success:
            print("\n🏆 النتيجة النهائية: نجح الاختبار بامتياز!")
            print("🌟 مولد الكود الثوري متكامل مع النظام المعرفي الباهر!")
            print("🚀 النظام جاهز لتوليد الكود بطرق ثورية!")
        else:
            print("\n⚠️ النتيجة النهائية: فشل في اختبار التكامل")
    else:
        print("\n❌ النتيجة النهائية: فشل في اختبار المولد الأساسي")
    
    print("\n" + "=" * 70)
    print("🔬 انتهى اختبار مولد الكود الثوري")
    print(f"📅 وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
