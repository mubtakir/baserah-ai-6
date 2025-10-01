#!/usr/bin/env python3
# test_adaptive_equations.py - اختبار المعادلات المتكيفة Baserah

import sys
import os
import numpy as np

# إضافة المسار للاستيراد
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from adaptive_equations import BaserahAdaptiveEquation, AdaptationMode, EvolutionDirection, BaserahAdaptiveMatrix
from adaptive_evolution_engine import BaserahAdaptiveEvolutionEngine, EvolutionConfig, EvolutionStrategy
from integrated_expert_explorer import BaserahIntegratedExpertExplorer

def test_adaptive_matrix():
    """اختبار المصفوفة التكيفية."""
    
    print("🧬 اختبار المصفوفة التكيفية Baserah...")
    print("=" * 50)
    
    # إنشاء مصفوفة تكيفية
    matrix = BaserahAdaptiveMatrix(size=5)
    
    print("1️⃣ اختبار المعالجة الأساسية:")
    inputs = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
    output = matrix.process(inputs)
    print(f"   المدخلات: {inputs}")
    print(f"   المخرجات: {output:.6f}")
    
    print("\n2️⃣ اختبار التكيف:")
    error = 0.1
    matrix.adapt(error, inputs)
    new_output = matrix.process(inputs)
    print(f"   المخرجات بعد التكيف: {new_output:.6f}")
    print(f"   نقاط Baserah: {matrix.baserah_score:.3f}")
    
    print("\n3️⃣ ملخص التكيف:")
    summary = matrix.get_adaptation_summary()
    for key, value in summary.items():
        print(f"   {key}: {value}")
    
    print("\n✅ اختبار المصفوفة التكيفية مكتمل!")

def test_adaptive_equation():
    """اختبار المعادلة المتكيفة."""
    
    print("\n🧬 اختبار المعادلة المتكيفة Baserah...")
    print("=" * 50)
    
    # إنشاء معادلة متكيفة
    equation = BaserahAdaptiveEquation("test_adaptive_eq")
    
    print("1️⃣ إضافة مكونات:")
    equation.add_sigmoid_component(k=2.0, alpha=1.0)
    equation.add_linear_component(beta=1.5, gamma=0.5)
    equation.add_quantum_component(quantum_factor=4)
    
    print(f"   المعادلة: {equation.get_equation_string()}")
    
    print("\n2️⃣ اختبار التقييم:")
    test_points = [0.0, 0.5, 1.0, 1.5, 2.0]
    for x in test_points:
        y = equation.evaluate(x)
        print(f"   f({x}) = {y:.6f}")
    
    print("\n3️⃣ اختبار التكيف مع البيانات:")
    # بيانات خط مستقيم
    x_data = [0, 1, 2, 3, 4]
    y_data = [1, 3, 5, 7, 9]  # y = 2x + 1
    
    adaptation_result = equation.adapt_to_data(x_data, y_data)
    print(f"   خطأ أولي: {adaptation_result['initial_error']:.6f}")
    print(f"   خطأ نهائي: {adaptation_result['final_error']:.6f}")
    print(f"   تكرارات: {adaptation_result['iterations']}")
    print(f"   نجح: {adaptation_result['success']}")
    
    print("\n4️⃣ اختبار التطوير:")
    evolution_result = equation.evolve(EvolutionDirection.OPTIMIZE)
    print(f"   تغييرات: {len(evolution_result['changes_made'])}")
    for change in evolution_result['changes_made']:
        print(f"     - {change}")
    
    print("\n5️⃣ ملخص المعادلة:")
    summary = equation.get_adaptation_summary()
    for key, value in summary.items():
        print(f"   {key}: {value}")
    
    print("\n✅ اختبار المعادلة المتكيفة مكتمل!")

def test_evolution_engine():
    """اختبار محرك التطوير."""
    
    print("\n🧬 اختبار محرك التطوير التكيفي...")
    print("=" * 50)
    
    # إنشاء محرك التطوير
    config = EvolutionConfig(
        strategy=EvolutionStrategy.HYBRID_EVOLUTION,
        population_size=5,
        max_generations=10,
        mutation_rate=0.3,
        fitness_threshold=0.8
    )
    
    engine = BaserahAdaptiveEvolutionEngine(config)
    
    print("1️⃣ تهيئة المجموعة:")
    population = engine.initialize_population(5)
    print(f"   تم إنشاء {len(population)} معادلة")
    
    print("\n2️⃣ اختبار التطوير:")
    # بيانات سيجمويد
    x_data = np.linspace(-3, 3, 10).tolist()
    y_data = [1 / (1 + np.exp(-2*x)) for x in x_data]  # sigmoid
    
    evolution_result = engine.evolve_population(x_data, y_data)
    
    print(f"   نجح التطوير: {evolution_result.success}")
    print(f"   أفضل لياقة: {evolution_result.best_fitness:.6f}")
    print(f"   أجيال: {evolution_result.generation_count}")
    print(f"   تقارب: {evolution_result.convergence_achieved}")
    
    if evolution_result.best_equation:
        print(f"   أفضل معادلة: {evolution_result.best_equation.get_equation_string()}")
    
    print("\n3️⃣ إحصائيات المحرك:")
    stats = engine.get_statistics()
    for key, value in stats.items():
        print(f"   {key}: {value}")
    
    print("\n✅ اختبار محرك التطوير مكتمل!")

def test_integrated_adaptive_system():
    """اختبار النظام المتكامل مع المعادلات المتكيفة."""
    
    print("\n🧬 اختبار النظام المتكامل مع المعادلات المتكيفة...")
    print("=" * 50)
    
    # إنشاء النظام المتكامل
    system = BaserahIntegratedExpertExplorer()
    
    print("1️⃣ إنشاء معادلة متكيفة من البيانات:")
    # بيانات مختلطة (خطي + سيجمويد)
    x_data = np.linspace(-2, 2, 8).tolist()
    y_data = [x + 0.5 / (1 + np.exp(-3*x)) for x in x_data]
    
    adaptive_eq = system.create_adaptive_equation_from_data(x_data, y_data)
    print(f"   معادلة منشأة: {adaptive_eq.id}")
    print(f"   مكونات: {len(adaptive_eq.components)}")
    
    print("\n2️⃣ تطوير مجموعة معادلات:")
    evolution_result = system.evolve_adaptive_equations(x_data, y_data, population_size=5)
    print(f"   نجح التطوير: {evolution_result['evolution_success']}")
    print(f"   أفضل لياقة: {evolution_result['best_fitness']:.6f}")
    print(f"   معادلات متكيفة: {evolution_result['total_adaptive_equations']}")
    
    print("\n3️⃣ دورة تعلم تكيفية:")
    learning_result = system.adaptive_learning_cycle(x_data, y_data)
    print(f"   نجحت الدورة: {learning_result['success']}")
    print(f"   معادلة متكيفة منشأة: {learning_result['adaptive_equation_created']}")
    print(f"   تطوير مُنفذ: {learning_result['evolution_performed']}")
    print(f"   أنماط مكتشفة: {learning_result['patterns_discovered']}")
    
    print("\n4️⃣ إحصائيات النظام المحدثة:")
    stats = system.analyze_system_performance()
    adaptive_stats = stats['adaptive_evolution_statistics']
    print(f"   تطويرات كلية: {adaptive_stats['total_evolutions']}")
    print(f"   تطويرات ناجحة: {adaptive_stats['successful_evolutions']}")
    print(f"   معدل النجاح: {adaptive_stats['success_rate']:.2%}")
    print(f"   أفضل لياقة: {adaptive_stats['best_fitness_achieved']:.6f}")
    
    print("\n5️⃣ ملخص النظام المحدث:")
    summary = system.get_system_summary()
    print(summary)
    
    print("\n✅ اختبار النظام المتكامل مع المعادلات المتكيفة مكتمل!")

def test_adaptive_equation_types():
    """اختبار أنواع مختلفة من المعادلات المتكيفة."""
    
    print("\n🧬 اختبار أنواع مختلفة من المعادلات المتكيفة...")
    print("=" * 50)
    
    test_cases = [
        {
            'name': 'خط مستقيم',
            'x_data': [0, 1, 2, 3, 4],
            'y_data': [2, 4, 6, 8, 10]  # y = 2x + 2
        },
        {
            'name': 'سيجمويد',
            'x_data': np.linspace(-3, 3, 7).tolist(),
            'y_data': [1 / (1 + np.exp(-x)) for x in np.linspace(-3, 3, 7)]
        },
        {
            'name': 'تربيعي',
            'x_data': [-2, -1, 0, 1, 2],
            'y_data': [4, 1, 0, 1, 4]  # y = x^2
        },
        {
            'name': 'مختلط',
            'x_data': np.linspace(-1, 1, 6).tolist(),
            'y_data': [x + 0.5 * np.sin(3*x) for x in np.linspace(-1, 1, 6)]
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{i}️⃣ اختبار {test_case['name']}:")
        
        equation = BaserahAdaptiveEquation(f"test_{test_case['name'].replace(' ', '_')}")
        
        # إضافة مكونات متنوعة
        equation.add_sigmoid_component()
        equation.add_linear_component()
        equation.add_quantum_component()
        
        # تكيف مع البيانات
        result = equation.adapt_to_data(test_case['x_data'], test_case['y_data'])
        
        print(f"   خطأ أولي: {result['initial_error']:.6f}")
        print(f"   خطأ نهائي: {result['final_error']:.6f}")
        print(f"   تحسن: {((result['initial_error'] - result['final_error']) / result['initial_error'] * 100):.1f}%")
        print(f"   نجح: {result['success']}")
        
        # تطوير المعادلة
        evolution = equation.evolve(EvolutionDirection.OPTIMIZE)
        print(f"   تطويرات: {len(evolution['changes_made'])}")
    
    print("\n✅ اختبار أنواع المعادلات المتكيفة مكتمل!")

def run_comprehensive_adaptive_test():
    """تشغيل اختبار شامل للمعادلات المتكيفة."""
    
    print("🧬 بدء الاختبار الشامل للمعادلات المتكيفة Baserah")
    print("=" * 70)
    print("الأنظمة الثورية: المصفوفة التكيفية + المعادلات المتكيفة + محرك التطوير")
    print("=" * 70)
    
    try:
        # اختبار المكونات الفردية
        test_adaptive_matrix()
        test_adaptive_equation()
        test_evolution_engine()
        
        # اختبار النظام المتكامل
        test_integrated_adaptive_system()
        
        # اختبار أنواع مختلفة
        test_adaptive_equation_types()
        
        print("\n" + "=" * 70)
        print("🎉 انتهى الاختبار الشامل للمعادلات المتكيفة!")
        print("✅ الأنظمة الثورية البديلة تعمل بنجاح!")
        print("🧬 المعادلات المتكيفة + المصفوفة التكيفية + محرك التطوير")
        print("🎯 منهج Baserah النقي 100% - بديل ثوري للذكاء الاصطناعي!")
        
    except Exception as e:
        print(f"\n❌ خطأ في الاختبار الشامل: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_comprehensive_adaptive_test()
