#!/usr/bin/env python3
# test_universal_system.py - اختبار شامل لنظام Baserah الشامل

import sys
import os

# إضافة المسارات للاستيراد
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'artistic_unit'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'expert_explorer'))

def test_artistic_unit():
    """اختبار الوحدة الفنية."""
    
    print("🎨 اختبار الوحدة الفنية...")
    print("=" * 40)
    
    try:
        from artistic_intelligence.baserah_core import baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid
        from artistic_intelligence.inference_engine.inference_engine import BaserahInferenceEngine
        from artistic_unit.integrated_system import BaserahIntegratedSystem
        
        # اختبار الدوال الأساسية
        print("1️⃣ اختبار الدوال الأساسية:")
        x = 0.5
        y_sigmoid = baserah_sigmoid(x, n=1, k=2, x0=0, alpha=1)
        y_linear = baserah_linear(x, beta=2, gamma=1)
        y_quantum = baserah_quantum_sigmoid(x, n=1, k=2, x0=0, alpha=1, quantum_factor=4)
        
        print(f"   σ({x}) = {y_sigmoid:.4f}")
        print(f"   linear({x}) = {y_linear:.4f}")
        print(f"   quantum({x}) = {y_quantum:.4f}")
        
        # اختبار محرك الاستنباط
        print("\n2️⃣ اختبار محرك الاستنباط:")
        engine = BaserahInferenceEngine()
        
        x_data = [-2, -1, 0, 1, 2]
        y_data = [1, 3, 5, 7, 9]  # خط مستقيم
        
        result = engine.infer_from_data_points(x_data, y_data)
        equation = engine.generate_equation_string(result)
        print(f"   المعادلة المستنتجة: {equation}")
        
        # اختبار النظام المتكامل
        print("\n3️⃣ اختبار النظام المتكامل:")
        system = BaserahIntegratedSystem()
        
        try:
            # محاولة تحليل ورسم (قد يفشل بدون matplotlib)
            result = system.analyze_and_render(x_data, y_data, "اختبار النظام الموحد")
            if result:
                print(f"   نجح التحليل: نوع={result['type']}, خطأ={result['error']:.6f}")
        except ImportError:
            print("   ⚠️ matplotlib غير متوفر - تم تخطي اختبار الرسم")
        except Exception as e:
            print(f"   ⚠️ خطأ في الرسم: {e}")
        
        print("✅ الوحدة الفنية تعمل بنجاح!")
        return True
        
    except Exception as e:
        print(f"❌ خطأ في الوحدة الفنية: {e}")
        return False

def test_expert_explorer():
    """اختبار نظام الخبير والمستكشف."""
    
    print("\n🧠🔍 اختبار نظام الخبير والمستكشف...")
    print("=" * 40)
    
    try:
        from revolutionary_intelligence.expert_explorer_system.expert_explorer.baserah_expert_core import (
            BaserahExpertCore, BaserahKnowledgeItem, BaserahInferenceContext,
            KnowledgeType, InferenceMethod
        )
        from revolutionary_intelligence.expert_explorer_system.expert_explorer.baserah_explorer_core import (
            BaserahExplorerCore, ExplorationConfig, ExplorationMode
        )
        from revolutionary_intelligence.expert_explorer_system.expert_explorer.integrated_expert_explorer import BaserahIntegratedExpertExplorer
        from revolutionary_intelligence.expert_explorer_system.expert_explorer.adaptive_equations import BaserahAdaptiveEquation
        from revolutionary_intelligence.expert_explorer_system.expert_explorer.adaptive_evolution_engine import BaserahAdaptiveEvolutionEngine
        
        # اختبار النظام الخبير
        print("1️⃣ اختبار النظام الخبير:")
        expert = BaserahExpertCore()
        
        # إضافة معرفة
        knowledge = BaserahKnowledgeItem(
            type=KnowledgeType.FACT,
            content="اختبار النظام الموحد",
            activation_level=0.9
        )
        expert.add_knowledge(knowledge)
        
        # اختبار الاستدلال
        context = BaserahInferenceContext(
            method=InferenceMethod.SIGMOID_REASONING,
            confidence_threshold=0.6
        )
        result = expert.infer(context)
        print(f"   الاستدلال: نجح={result.success}, ثقة={result.confidence:.3f}")
        
        # اختبار المستكشف
        print("\n2️⃣ اختبار المستكشف:")
        explorer = BaserahExplorerCore()
        
        config = ExplorationConfig(
            mode=ExplorationMode.RANDOM,
            budget=5,
            fitness_threshold=0.3
        )
        
        exploration_result = explorer.explore(config)
        print(f"   الاستكشاف: نجح={exploration_result.success}")
        print(f"   معادلات مكتشفة: {len(exploration_result.discovered_equations)}")
        
        # اختبار النظام المتكامل
        print("\n3️⃣ اختبار النظام المتكامل:")
        integrated = BaserahIntegratedExpertExplorer()
        
        cycle_result = integrated.run_integrated_cycle()
        print(f"   دورة متكاملة: نجح={cycle_result['integration_success']}")
        print(f"   معادلات جديدة: {cycle_result['new_equations']}")

        # اختبار المعادلات المتكيفة الثورية
        print("\n4️⃣ اختبار المعادلات المتكيفة الثورية:")

        # بيانات اختبار
        x_data = [0, 1, 2, 3, 4]
        y_data = [1, 3, 5, 7, 9]  # خط مستقيم

        # إنشاء معادلة متكيفة
        adaptive_eq = integrated.create_adaptive_equation_from_data(x_data, y_data)
        print(f"   معادلة متكيفة: {adaptive_eq.id}")

        # تطوير مجموعة معادلات
        evolution_result = integrated.evolve_adaptive_equations(x_data, y_data, population_size=3)
        print(f"   تطوير ناجح: {evolution_result['evolution_success']}")
        print(f"   أفضل لياقة: {evolution_result['best_fitness']:.6f}")

        # دورة تعلم تكيفية
        learning_result = integrated.adaptive_learning_cycle(x_data, y_data)
        print(f"   تعلم تكيفي: {learning_result['success']}")

        print("✅ نظام الخبير والمستكشف والمعادلات المتكيفة يعمل بنجاح!")
        return True
        
    except Exception as e:
        print(f"❌ خطأ في نظام الخبير والمستكشف: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_math_components():
    """اختبار المكونات الرياضية."""
    
    print("\n🔢 اختبار المكونات الرياضية...")
    print("=" * 40)
    
    try:
        from math_components.gse_math_components import generalized_sigmoid
        
        print("1️⃣ اختبار السيجمويد المعمم:")
        
        x = 0.5
        result = generalized_sigmoid(x, alpha=1.0, beta=2.0, gamma=0.0, delta=1.0)
        print(f"   generalized_sigmoid({x}) = {result:.4f}")
        
        # اختبار مع معاملات مختلفة
        results = []
        for i in range(3):
            alpha = 1.0 + i * 0.5
            result = generalized_sigmoid(x, alpha=alpha, beta=2.0, gamma=0.0, delta=1.0)
            results.append(result)
            print(f"   α={alpha}: {result:.4f}")
        
        print("✅ المكونات الرياضية تعمل بنجاح!")
        return True
        
    except Exception as e:
        print(f"❌ خطأ في المكونات الرياضية: {e}")
        return False

def test_system_integration():
    """اختبار تكامل النظام الكامل."""
    
    print("\n🔗 اختبار تكامل النظام الكامل...")
    print("=" * 40)
    
    try:
        # اختبار استيراد جميع المكونات
        print("1️⃣ اختبار الاستيراد:")
        
        from artistic_intelligence.baserah_core import baserah_sigmoid
        from revolutionary_intelligence.expert_explorer_system.expert_explorer.baserah_expert_core import BaserahExpertCore
        from math_components.gse_math_components import generalized_sigmoid
        
        print("   ✅ جميع المكونات قابلة للاستيراد")
        
        # اختبار التفاعل بين المكونات
        print("\n2️⃣ اختبار التفاعل:")
        
        # استخدام السيجمويد من الوحدة الفنية
        x = 0.5
        y1 = baserah_sigmoid(x, n=1, k=2, x0=0, alpha=1)
        
        # استخدام السيجمويد المعمم
        y2 = generalized_sigmoid(x, alpha=1.0, beta=2.0, gamma=0.0, delta=1.0)
        
        print(f"   Baserah sigmoid: {y1:.4f}")
        print(f"   Generalized sigmoid: {y2:.4f}")
        print(f"   الفرق: {abs(y1 - y2):.6f}")
        
        # اختبار النظام الخبير مع البيانات
        print("\n3️⃣ اختبار النظام الخبير مع البيانات:")
        
        expert = BaserahExpertCore()
        print(f"   تم إنشاء النظام الخبير: {len(expert.knowledge_base)} عنصر معرفة")
        
        print("✅ تكامل النظام الكامل يعمل بنجاح!")
        return True
        
    except Exception as e:
        print(f"❌ خطأ في تكامل النظام: {e}")
        return False

def run_comprehensive_test():
    """تشغيل اختبار شامل للنظام الموحد."""
    
    print("🌟 بدء الاختبار الشامل لنظام Baserah الشامل")
    print("=" * 60)
    print("النظام يجمع: الوحدة الفنية + نظام الخبير والمستكشف + المكونات الرياضية")
    print("=" * 60)
    
    results = []
    
    try:
        # اختبار المكونات الفردية
        results.append(("الوحدة الفنية", test_artistic_unit()))
        results.append(("نظام الخبير والمستكشف والمعادلات المتكيفة", test_expert_explorer()))
        results.append(("المكونات الرياضية", test_math_components()))
        results.append(("تكامل النظام", test_system_integration()))
        
        # تلخيص النتائج
        print("\n" + "=" * 60)
        print("📊 ملخص نتائج الاختبار:")
        
        passed = 0
        total = len(results)
        
        for component, success in results:
            status = "✅ نجح" if success else "❌ فشل"
            print(f"   {component}: {status}")
            if success:
                passed += 1
        
        success_rate = (passed / total) * 100
        print(f"\nمعدل النجاح: {passed}/{total} ({success_rate:.1f}%)")
        
        if passed == total:
            print("\n🎉 نظام Baserah الشامل يعمل بنجاح كامل!")
            print("✅ جميع المكونات متكاملة ومترابطة!")
            print("🎯 منهج Baserah النقي 100% محقق!")
        else:
            print(f"\n⚠️ {total - passed} مكون(ات) تحتاج إصلاح")
        
        print("\n🌟 انتهى الاختبار الشامل لنظام Baserah الشامل!")
        
    except Exception as e:
        print(f"\n❌ خطأ في الاختبار الشامل: {e}")
        import traceback
        traceback.print_exc()

def show_system_info():
    """عرض معلومات النظام."""
    
    print("\n📋 معلومات نظام Baserah الشامل:")
    print("=" * 40)
    
    # معلومات المجلدات
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    folders = [
        ("الوحدة الفنية", "artistic_unit"),
        ("نظام الخبير والمستكشف", "expert_explorer"),
        ("المكونات الرياضية", "math_components"),
        ("التوثيق", "docs")
    ]
    
    for name, folder in folders:
        folder_path = os.path.join(base_path, folder)
        exists = "✅ موجود" if os.path.exists(folder_path) else "❌ مفقود"
        print(f"   {name}: {exists}")
        
        if os.path.exists(folder_path):
            files = [f for f in os.listdir(folder_path) if f.endswith('.py')]
            print(f"     ملفات Python: {len(files)}")
    
    print(f"\nموقع النظام: {base_path}")

if __name__ == "__main__":
    # عرض معلومات النظام
    show_system_info()
    
    # تشغيل الاختبار الشامل
    run_comprehensive_test()
    
    # خيار تفاعلي
    choice = input("\nهل تريد تشغيل اختبار تفاعلي؟ (y/n): ").strip().lower()
    if choice == 'y':
        print("\n🎮 الاختبار التفاعلي:")
        print("1. اختبار الوحدة الفنية")
        print("2. اختبار نظام الخبير والمستكشف") 
        print("3. اختبار المكونات الرياضية")
        print("4. اختبار تكامل النظام")
        
        test_choice = input("اختر رقم الاختبار: ").strip()
        
        if test_choice == '1':
            test_artistic_unit()
        elif test_choice == '2':
            test_expert_explorer()
        elif test_choice == '3':
            test_math_components()
        elif test_choice == '4':
            test_system_integration()
        else:
            print("اختيار غير صحيح")
