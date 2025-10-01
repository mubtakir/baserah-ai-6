#!/usr/bin/env python3
# test_intelligent_adaptation.py - اختبار التكيف الذكي بقيادة النظام الخبير/المستكشف

import sys
import os
from datetime import datetime

# إضافة المسار للاستيراد
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_expert_explorer_system():
    """اختبار النظام الخبير/المستكشف."""
    
    print("🧠🔍 اختبار النظام الخبير/المستكشف...")
    print("-" * 50)
    
    try:
        from revolutionary_intelligence.expert_explorer_system.expert_explorer.integrated_expert_explorer import BaserahIntegratedExpertExplorer
        
        # إنشاء النظام الخبير/المستكشف
        expert_system = BaserahIntegratedExpertExplorer()
        
        print(f"✅ تم إنشاء النظام الخبير/المستكشف")
        print(f"   معادلات متكيفة: {len(expert_system.adaptive_equations)}")
        
        # اختبار إنشاء معادلة متكيفة
        x_data = [0, 1, 2, 3, 4]
        y_data = [0, 1, 4, 9, 16]  # دالة تربيعية
        
        print(f"\n🧬 اختبار إنشاء معادلة متكيفة...")
        adaptive_eq = expert_system.create_adaptive_equation_from_data(x_data, y_data)
        
        if adaptive_eq:
            print(f"✅ تم إنشاء معادلة متكيفة: {adaptive_eq.id}")
            print(f"   مكونات: {len(adaptive_eq.components)}")
            print(f"   لياقة: {adaptive_eq.current_fitness:.4f}")
        
        # اختبار تطوير المعادلات
        print(f"\n🔧 اختبار تطوير المعادلات...")
        evolution_result = expert_system.evolve_adaptive_equations(x_data, y_data, population_size=5)
        
        if evolution_result['evolution_success']:
            print(f"✅ نجح التطوير:")
            print(f"   أفضل لياقة: {evolution_result['best_fitness']:.4f}")
            print(f"   أجيال: {evolution_result['generations']}")
            print(f"   إجمالي المعادلات: {evolution_result['total_adaptive_equations']}")
        
        return expert_system
        
    except ImportError as e:
        print(f"❌ فشل استيراد النظام الخبير/المستكشف: {e}")
        return None
    except Exception as e:
        print(f"❌ خطأ في اختبار النظام الخبير/المستكشف: {e}")
        return None

def test_mother_system_integration():
    """اختبار تكامل النظام الأم مع النظام الخبير/المستكشف."""
    
    print("\n🌟 اختبار تكامل النظام الأم...")
    print("-" * 50)
    
    try:
        from revolutionary_intelligence.revolutionary_mother_system.revolutionary_mother_system import BaserahRevolutionaryMotherSystem
        
        # إنشاء النظام الأم
        mother_system = BaserahRevolutionaryMotherSystem()
        
        print(f"✅ تم إنشاء النظام الأم: {mother_system.system_id}")
        
        # فحص النظام الخبير/المستكشف
        if mother_system.expert_explorer_system:
            print(f"✅ النظام الخبير/المستكشف متاح")
            print(f"   معادلات متكيفة: {len(mother_system.expert_explorer_system.adaptive_equations)}")
        else:
            print(f"⚠️ النظام الخبير/المستكشف غير متاح")
        
        # فحص قاعدة بيانات الأشكال
        if mother_system.shapes_database:
            print(f"✅ قاعدة بيانات الأشكال متاحة")
            print(f"   إجمالي الأشكال: {len(mother_system.shapes_database.shapes)}")
        else:
            print(f"⚠️ قاعدة بيانات الأشكال غير متاحة")
        
        return mother_system
        
    except Exception as e:
        print(f"❌ خطأ في اختبار النظام الأم: {e}")
        return None

def test_artistic_unit_inheritance():
    """اختبار وراثة الوحدة الفنية للنظام الخبير/المستكشف."""
    
    print("\n🎨 اختبار وراثة الوحدة الفنية...")
    print("-" * 50)
    
    try:
        from artistic_unit.integrated_system import BaserahIntegratedSystem
        from revolutionary_intelligence.revolutionary_mother_system.revolutionary_mother_system import BaserahRevolutionaryMotherSystem, InheritanceType
        
        # إنشاء النظام الأم والوحدة الفنية
        mother_system = BaserahRevolutionaryMotherSystem()
        artistic_unit = BaserahIntegratedSystem()
        
        print(f"✅ تم إنشاء النظام الأم والوحدة الفنية")
        
        # وراثة قاعدة بيانات الأشكال
        if mother_system.shapes_database:
            shapes_inheritance = mother_system.inherit_shapes_to_unit(artistic_unit, InheritanceType.ARTISTIC_UNIT)
            if shapes_inheritance['success']:
                print(f"✅ تم وراثة قاعدة بيانات الأشكال:")
                print(f"   أشكال موروثة: {shapes_inheritance['shapes_inherited']}")
        
        # وراثة النظام الخبير/المستكشف
        if mother_system.expert_explorer_system:
            expert_inheritance = mother_system.inherit_expert_explorer_to_unit(artistic_unit, InheritanceType.ARTISTIC_UNIT)
            if expert_inheritance['success']:
                print(f"✅ تم وراثة النظام الخبير/المستكشف:")
                print(f"   معادلات متكيفة موروثة: {expert_inheritance['adaptive_equations_inherited']}")
                print(f"   الذكاء التكيفي: {'مفعل' if artistic_unit.adaptive_intelligence_enabled else 'غير مفعل'}")
        
        return artistic_unit, mother_system
        
    except Exception as e:
        print(f"❌ خطأ في اختبار وراثة الوحدة الفنية: {e}")
        return None, None

def test_intelligent_visual_adaptation():
    """اختبار التكيف البصري الذكي."""
    
    print("\n🧠🎨 اختبار التكيف البصري الذكي...")
    print("-" * 50)
    
    artistic_unit, mother_system = test_artistic_unit_inheritance()
    
    if not artistic_unit or not artistic_unit.adaptive_intelligence_enabled:
        print("❌ الوحدة الفنية أو الذكاء التكيفي غير متاح")
        return False
    
    try:
        # اختبار التكيف الذكي بين الأشكال
        print("🔄 اختبار التكيف الذكي من مربع إلى دائرة...")
        
        intelligent_adaptation = artistic_unit.create_intelligent_visual_adaptation(
            "square_basic", "circle_basic", steps=10
        )
        
        if intelligent_adaptation:
            print(f"✅ تم إنشاء تكيف بصري ذكي:")
            print(f"   خطوات: {len(intelligent_adaptation)}")
            
            # فحص التحسينات الذكية
            enhanced_steps = [step for step in intelligent_adaptation if 'enhancement_factor' in step]
            print(f"   خطوات محسنة ذكياً: {len(enhanced_steps)}")
            
            if enhanced_steps:
                avg_enhancement = sum(step['enhancement_factor'] for step in enhanced_steps) / len(enhanced_steps)
                print(f"   متوسط عامل التحسين: {avg_enhancement:.3f}")
            
            return True
        else:
            print("❌ فشل في إنشاء التكيف البصري الذكي")
            return False
            
    except Exception as e:
        print(f"❌ خطأ في اختبار التكيف البصري الذكي: {e}")
        return False

def test_adaptive_learning_cycle():
    """اختبار دورة التعلم التكيفية."""
    
    print("\n🔄 اختبار دورة التعلم التكيفية...")
    print("-" * 50)
    
    expert_system = test_expert_explorer_system()
    
    if not expert_system:
        print("❌ النظام الخبير/المستكشف غير متاح")
        return False
    
    try:
        # بيانات اختبار معقدة
        x_data = [-2, -1, 0, 1, 2, 3, 4]
        y_data = [0.1, 0.3, 0.5, 0.7, 0.9, 0.95, 0.99]  # منحنى سيجمويد
        
        print("🧠 تشغيل دورة التعلم التكيفية...")
        learning_result = expert_system.adaptive_learning_cycle(x_data, y_data)
        
        if learning_result['success']:
            print(f"✅ نجحت دورة التعلم التكيفية:")
            print(f"   معادلة متكيفة: {'نعم' if learning_result['adaptive_equation_created'] else 'لا'}")
            print(f"   تطوير: {'نعم' if learning_result['evolution_performed'] else 'لا'}")
            print(f"   أنماط مكتشفة: {learning_result['patterns_discovered']}")
            print(f"   عناصر معرفة مضافة: {learning_result['knowledge_items_added']}")
            
            # فحص المعادلات المتكيفة الجديدة
            print(f"   إجمالي المعادلات المتكيفة: {len(expert_system.adaptive_equations)}")
            
            return True
        else:
            print(f"❌ فشلت دورة التعلم التكيفية")
            return False
            
    except Exception as e:
        print(f"❌ خطأ في اختبار دورة التعلم التكيفية: {e}")
        return False

def test_system_health_and_statistics():
    """اختبار صحة النظام والإحصائيات."""
    
    print("\n📊 اختبار صحة النظام والإحصائيات...")
    print("-" * 50)
    
    try:
        from revolutionary_intelligence.revolutionary_mother_system.revolutionary_mother_system import BaserahRevolutionaryMotherSystem
        
        mother_system = BaserahRevolutionaryMotherSystem()
        
        # الحصول على ملخص النظام
        summary = mother_system.get_system_summary()
        
        print(f"✅ ملخص النظام الأم:")
        print(f"   معرف النظام: {summary['system_id']}")
        print(f"   إجمالي الوراثات: {summary['total_inheritances']}")
        print(f"   إجمالي التكيفات: {summary['total_adaptations']}")
        print(f"   نقاء Baserah: {summary['baserah_purity']:.1%}")
        
        # معلومات قاعدة بيانات الأشكال
        shapes_info = summary.get('shapes_database', {})
        if shapes_info:
            print(f"\n📊 قاعدة بيانات الأشكال:")
            print(f"   إجمالي الأشكال: {shapes_info.get('total_shapes', 0)}")
            print(f"   الأشكال المتحركة: {shapes_info.get('animated_shapes', 0)}")
            print(f"   متوسط الجمال الرياضي: {shapes_info.get('mathematical_beauty_average', 0):.3f}")
        
        # اختبار النظام الخبير/المستكشف إذا كان متاحاً
        if mother_system.expert_explorer_system:
            expert_stats = mother_system.expert_explorer_system.get_system_statistics()
            print(f"\n🧠 إحصائيات النظام الخبير/المستكشف:")
            
            system_health = expert_stats.get('system_health', {})
            print(f"   معادلات متكيفة: {system_health.get('adaptive_equations_count', 0)}")
            print(f"   معدل نجاح التكامل: {system_health.get('integration_success_rate', 0):.2%}")
            print(f"   معدل نمو المعرفة: {system_health.get('knowledge_growth_rate', 0):.2f}")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار صحة النظام: {e}")
        return False

def run_comprehensive_intelligent_adaptation_test():
    """تشغيل اختبار شامل للتكيف الذكي."""
    
    print("🧠🔍 اختبار شامل للتكيف الذكي بقيادة النظام الخبير/المستكشف")
    print("=" * 80)
    print(f"📅 تاريخ الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    test_results = {
        'expert_explorer_system': False,
        'mother_system_integration': False,
        'artistic_unit_inheritance': False,
        'intelligent_visual_adaptation': False,
        'adaptive_learning_cycle': False,
        'system_health': False
    }
    
    try:
        # تشغيل جميع الاختبارات
        print("🧪 تشغيل اختبارات التكيف الذكي...")
        
        test_results['expert_explorer_system'] = test_expert_explorer_system() is not None
        test_results['mother_system_integration'] = test_mother_system_integration() is not None
        test_results['artistic_unit_inheritance'] = test_artistic_unit_inheritance()[0] is not None
        test_results['intelligent_visual_adaptation'] = test_intelligent_visual_adaptation()
        test_results['adaptive_learning_cycle'] = test_adaptive_learning_cycle()
        test_results['system_health'] = test_system_health_and_statistics()
        
        # ملخص النتائج
        print("\n" + "=" * 80)
        print("📊 ملخص نتائج اختبار التكيف الذكي:")
        print("=" * 80)
        
        passed_tests = sum(test_results.values())
        total_tests = len(test_results)
        
        for test_name, result in test_results.items():
            status = "✅ نجح" if result else "❌ فشل"
            print(f"   {test_name}: {status}")
        
        success_rate = passed_tests / total_tests
        print(f"\n📈 معدل النجاح: {success_rate:.1%} ({passed_tests}/{total_tests})")
        
        if success_rate >= 0.8:
            print(f"\n🎉 التكيف الذكي يعمل بنجاح!")
            print(f"✅ المعادلات المتكيفة يقودها النظام الخبير/المستكشف!")
            print(f"🧠 الذكاء التكيفي مفعل في الوحدة الفنية!")
            print(f"🔄 دورة التعلم التكيفية تعمل!")
            print(f"🌟 النظام الثوري متكامل!")
        elif success_rate >= 0.5:
            print(f"\n⚠️ التكيف الذكي يعمل جزئياً")
            print(f"🔧 يحتاج تحسينات في بعض المكونات")
        else:
            print(f"\n❌ التكيف الذكي يحتاج إصلاحات")
            print(f"🛠️ مراجعة التكامل بين المكونات مطلوبة")
        
        return success_rate >= 0.8
        
    except Exception as e:
        print(f"\n❌ خطأ في اختبار التكيف الذكي: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    run_comprehensive_intelligent_adaptation_test()
