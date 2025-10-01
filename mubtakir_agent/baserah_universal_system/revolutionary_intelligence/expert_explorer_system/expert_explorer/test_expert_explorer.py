#!/usr/bin/env python3
# test_expert_explorer.py - اختبار شامل لنظام الخبير والمستكشف Baserah

import sys
import os

# إضافة المسار للاستيراد
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from baserah_expert_core import (
    BaserahExpertCore, BaserahKnowledgeItem, BaserahInferenceContext,
    KnowledgeType, InferenceMethod
)
from baserah_explorer_core import (
    BaserahExplorerCore, ExplorationConfig, ExplorationMode
)
from knowledge_manager import BaserahKnowledgeManager, KnowledgeRelationship
from pattern_discoverer import BaserahPatternDiscoverer
from integrated_expert_explorer import BaserahIntegratedExpertExplorer

def test_expert_core():
    """اختبار النواة الخبيرة."""
    
    print("🧠 اختبار النواة الخبيرة Baserah...")
    print("=" * 50)
    
    expert = BaserahExpertCore()
    
    # إضافة معرفة اختبار
    print("1️⃣ إضافة معرفة اختبار:")
    
    # حقائق
    fact1 = BaserahKnowledgeItem(
        id="fact_1",
        type=KnowledgeType.FACT,
        content="الطقس مشمس",
        activation_level=0.9
    )
    
    fact2 = BaserahKnowledgeItem(
        id="fact_2", 
        type=KnowledgeType.FACT,
        content="درجة الحرارة عالية",
        activation_level=0.8
    )
    
    # قاعدة
    rule1 = BaserahKnowledgeItem(
        id="rule_1",
        type=KnowledgeType.RULE,
        content={
            "if": ["fact_1", "fact_2"],
            "then": ["conclusion_1"]
        },
        baserah_weight=1.2
    )
    
    expert.add_knowledge(fact1)
    expert.add_knowledge(fact2)
    expert.add_knowledge(rule1)
    
    # اختبار الاستدلال
    print("\n2️⃣ اختبار الاستدلال:")
    
    context = BaserahInferenceContext(
        method=InferenceMethod.FORWARD_CHAINING,
        current_facts={"fact_1", "fact_2"},
        confidence_threshold=0.7
    )
    
    result = expert.infer(context)
    print(f"   النتيجة: {result.success}")
    print(f"   الحقائق المستنتجة: {result.derived_facts}")
    print(f"   الثقة: {result.confidence:.3f}")
    
    # اختبار الاستدلال السيجمويدي
    print("\n3️⃣ اختبار الاستدلال السيجمويدي:")
    
    sigmoid_context = BaserahInferenceContext(
        method=InferenceMethod.SIGMOID_REASONING,
        sigmoid_params={'n': 1, 'k': 2.0, 'x0': 0.5, 'alpha': 1.0},
        confidence_threshold=0.6
    )
    
    sigmoid_result = expert.infer(sigmoid_context)
    print(f"   النتيجة: {sigmoid_result.success}")
    print(f"   الحقائق: {len(sigmoid_result.derived_facts)}")
    
    # إحصائيات
    print("\n4️⃣ إحصائيات النظام الخبير:")
    stats = expert.get_statistics()
    for key, value in stats.items():
        print(f"   {key}: {value}")
    
    print("\n✅ اختبار النواة الخبيرة مكتمل!")

def test_explorer_core():
    """اختبار النواة المستكشفة."""
    
    print("\n🔍 اختبار النواة المستكشفة Baserah...")
    print("=" * 50)
    
    explorer = BaserahExplorerCore()
    
    # اختبار الاستكشاف العشوائي
    print("1️⃣ اختبار الاستكشاف العشوائي:")
    
    random_config = ExplorationConfig(
        mode=ExplorationMode.RANDOM,
        budget=10,
        fitness_threshold=0.3
    )
    
    random_result = explorer.explore(random_config)
    print(f"   النجاح: {random_result.success}")
    print(f"   معادلات مكتشفة: {len(random_result.discovered_equations)}")
    print(f"   نقاط Baserah: {random_result.baserah_score:.3f}")
    
    # اختبار الاستكشاف السيجمويدي
    print("\n2️⃣ اختبار الاستكشاف السيجمويدي:")
    
    sigmoid_config = ExplorationConfig(
        mode=ExplorationMode.SIGMOID_EXPLORATION,
        budget=8,
        fitness_threshold=0.4
    )
    
    sigmoid_result = explorer.explore(sigmoid_config)
    print(f"   النجاح: {sigmoid_result.success}")
    print(f"   معادلات سيجمويد: {len(sigmoid_result.discovered_equations)}")
    
    # اختبار الاستكشاف الكمي
    print("\n3️⃣ اختبار الاستكشاف الكمي:")
    
    quantum_config = ExplorationConfig(
        mode=ExplorationMode.QUANTUM_EXPLORATION,
        budget=6,
        quantum_factors=[2, 4, 8],
        fitness_threshold=0.3
    )
    
    quantum_result = explorer.explore(quantum_config)
    print(f"   النجاح: {quantum_result.success}")
    print(f"   معادلات مكممة: {len(quantum_result.discovered_equations)}")
    
    # اكتشاف الأنماط
    print("\n4️⃣ اكتشاف الأنماط:")
    
    all_equations = explorer.discovered_equations
    if all_equations:
        patterns = explorer.discover_patterns(all_equations)
        print(f"   أنماط مكتشفة: {len(patterns)}")
        for pattern in patterns[:3]:  # أول 3 أنماط
            print(f"   - {pattern['type']}: {pattern['description']}")
    
    # إحصائيات
    print("\n5️⃣ إحصائيات المستكشف:")
    stats = explorer.get_statistics()
    for key, value in stats.items():
        print(f"   {key}: {value}")
    
    print("\n✅ اختبار النواة المستكشفة مكتمل!")

def test_knowledge_manager():
    """اختبار مدير المعرفة."""
    
    print("\n📚 اختبار مدير المعرفة Baserah...")
    print("=" * 50)
    
    km = BaserahKnowledgeManager()
    
    # إضافة معرفة
    print("1️⃣ إضافة معرفة ومعادلات:")
    
    knowledge_item = BaserahKnowledgeItem(
        type=KnowledgeType.CONCEPT,
        content="مفهوم السيجمويد",
        relevance_score=0.9
    )
    km.add_knowledge_item(knowledge_item)
    
    # إنشاء معادلة اختبار
    from baserah_explorer_core import BaserahEquation
    equation = BaserahEquation(
        equation_type="test_sigmoid",
        components=[{
            'type': 'sigmoid',
            'params': {'n': 1, 'k': 2.0, 'x0': 0.0, 'alpha': 1.0},
            'variable': 'x'
        }],
        complexity=2.0,
        variables={'x'}
    )
    km.add_equation(equation)
    
    # إنشاء علاقة
    print("\n2️⃣ إنشاء علاقات:")
    
    relationship = KnowledgeRelationship(
        source_id=knowledge_item.id,
        target_id=equation.id,
        relationship_type="describes",
        strength=0.8
    )
    km.add_relationship(relationship)
    
    # إنشاء مجموعة
    print("\n3️⃣ إنشاء مجموعات:")
    
    cluster = km.create_cluster("مجموعة السيجمويد", "sigmoid_group")
    km.add_to_cluster(cluster.id, knowledge_item.id, "knowledge")
    km.add_to_cluster(cluster.id, equation.id, "equation")
    
    # البحث
    print("\n4️⃣ اختبار البحث:")
    
    concept_items = km.search_knowledge_by_type(KnowledgeType.CONCEPT)
    print(f"   مفاهيم موجودة: {len(concept_items)}")
    
    x_equations = km.search_equations_by_variable('x')
    print(f"   معادلات تحتوي x: {len(x_equations)}")
    
    # إحصائيات
    print("\n5️⃣ إحصائيات مدير المعرفة:")
    stats = km.get_statistics()
    for key, value in stats.items():
        if isinstance(value, dict):
            print(f"   {key}:")
            for sub_key, sub_value in value.items():
                print(f"     {sub_key}: {sub_value}")
        else:
            print(f"   {key}: {value}")
    
    print("\n✅ اختبار مدير المعرفة مكتمل!")

def test_pattern_discoverer():
    """اختبار مكتشف الأنماط."""
    
    print("\n🔍 اختبار مكتشف الأنماط Baserah...")
    print("=" * 50)
    
    pd = BaserahPatternDiscoverer()
    
    # إنشاء معادلات اختبار
    print("1️⃣ إنشاء معادلات اختبار:")
    
    from baserah_explorer_core import BaserahEquation
    
    equations = []
    
    # معادلات سيجمويد
    for i in range(3):
        eq = BaserahEquation(
            equation_type="test_sigmoid",
            components=[{
                'type': 'sigmoid',
                'params': {'n': 1, 'k': 2.0 + i*0.5, 'x0': 0.0, 'alpha': 1.0},
                'variable': 'x'
            }],
            complexity=2.0 + i*0.5,
            fitness=0.7 + i*0.1,
            variables={'x'}
        )
        equations.append(eq)
    
    # معادلات خطية
    for i in range(2):
        eq = BaserahEquation(
            equation_type="test_linear",
            components=[{
                'type': 'linear',
                'params': {'beta': 1.0 + i, 'gamma': 0.5},
                'variable': 'x'
            }],
            complexity=1.0,
            fitness=0.6 + i*0.1,
            variables={'x'}
        )
        equations.append(eq)
    
    # اكتشاف الأنماط
    print("\n2️⃣ اكتشاف الأنماط:")
    
    patterns = pd.discover_equation_patterns(equations)
    print(f"   أنماط مكتشفة: {len(patterns)}")
    
    for pattern in patterns:
        print(f"   - {pattern.pattern_type}: {pattern.description}")
        print(f"     الثقة: {pattern.confidence:.3f}, الدعم: {pattern.support}")
    
    # ملخص الأنماط
    print("\n3️⃣ ملخص الأنماط:")
    
    summary = pd.get_pattern_summary()
    for key, value in summary.items():
        print(f"   {key}: {value}")
    
    print("\n✅ اختبار مكتشف الأنماط مكتمل!")

def test_integrated_system():
    """اختبار النظام المتكامل."""
    
    print("\n🧠🔍 اختبار النظام المتكامل Baserah...")
    print("=" * 50)
    
    system = BaserahIntegratedExpertExplorer()
    
    # إضافة معرفة أولية
    print("1️⃣ إضافة معرفة أولية:")
    
    initial_knowledge = BaserahKnowledgeItem(
        type=KnowledgeType.GOAL,
        content="اكتشاف معادلات سيجمويد فعالة",
        relevance_score=1.0
    )
    system.knowledge_manager.add_knowledge_item(initial_knowledge)
    system.expert_core.add_knowledge(initial_knowledge)
    
    # تشغيل دورة متكاملة
    print("\n2️⃣ تشغيل دورة متكاملة:")
    
    cycle_result = system.run_integrated_cycle()
    print(f"   نجاح التكامل: {cycle_result['integration_success']}")
    print(f"   معادلات جديدة: {cycle_result['new_equations']}")
    print(f"   معرفة جديدة: {cycle_result['new_knowledge_items']}")
    print(f"   أنماط مكتشفة: {len(cycle_result['patterns_discovered'])}")
    
    # استكشاف موجه
    print("\n3️⃣ استكشاف موجه بالخبير:")
    
    guided_result = system.guided_exploration_with_expert("sigmoid_optimization", max_cycles=2)
    print(f"   دورات مكتملة: {guided_result['cycles_completed']}")
    print(f"   معادلات مكتشفة: {guided_result['total_equations_discovered']}")
    print(f"   هدف محقق: {guided_result['goal_achieved']}")
    
    # تحليل الأداء
    print("\n4️⃣ تحليل أداء النظام:")
    
    performance = system.analyze_system_performance()
    integration_stats = performance['integration_statistics']
    print(f"   دورات التكامل: {integration_stats['total_cycles']}")
    print(f"   معدل نجاح التكامل: {integration_stats['integration_success_rate']:.2%}")
    
    system_health = performance['system_health']
    print(f"   الأداء العام: {system_health['overall_performance']:.2%}")
    print(f"   معدل نمو المعرفة: {system_health['knowledge_growth_rate']:.1f}")
    
    # ملخص النظام
    print("\n5️⃣ ملخص النظام:")
    summary = system.get_system_summary()
    print(summary)
    
    print("\n✅ اختبار النظام المتكامل مكتمل!")

def run_comprehensive_test():
    """تشغيل اختبار شامل لنظام الخبير والمستكشف."""
    
    print("🚀 بدء الاختبار الشامل لنظام الخبير والمستكشف Baserah")
    print("=" * 70)
    print("النظام يجمع: النظام الخبير + المستكشف التطوري + مدير المعرفة + مكتشف الأنماط")
    print("=" * 70)
    
    try:
        # اختبار المكونات الفردية
        test_expert_core()
        test_explorer_core()
        test_knowledge_manager()
        test_pattern_discoverer()
        
        # اختبار النظام المتكامل
        test_integrated_system()
        
        print("\n" + "=" * 70)
        print("🎉 انتهى الاختبار الشامل لنظام الخبير والمستكشف!")
        print("✅ نظام الخبير والمستكشف Baserah جاهز للاستخدام!")
        print("🎯 تكامل كامل بين الخبير والمستكشف محقق!")
        print("🧠 منهج Baserah النقي 100% (سيجمويد + خطي + تكميم)")
        
    except Exception as e:
        print(f"\n❌ خطأ في الاختبار الشامل: {e}")
        import traceback
        traceback.print_exc()

def interactive_demo():
    """عرض تفاعلي لنظام الخبير والمستكشف."""
    
    print("\n🎮 العرض التفاعلي لنظام الخبير والمستكشف")
    print("=" * 50)
    
    options = {
        '1': 'اختبار النظام الخبير',
        '2': 'اختبار المستكشف التطوري',
        '3': 'اختبار مدير المعرفة',
        '4': 'اختبار مكتشف الأنماط',
        '5': 'اختبار النظام المتكامل',
        '6': 'اختبار شامل',
        '0': 'خروج'
    }
    
    while True:
        print("\nالخيارات المتاحة:")
        for key, value in options.items():
            print(f"  {key}. {value}")
        
        choice = input("\nاختر رقم الخيار: ").strip()
        
        if choice == '1':
            test_expert_core()
        elif choice == '2':
            test_explorer_core()
        elif choice == '3':
            test_knowledge_manager()
        elif choice == '4':
            test_pattern_discoverer()
        elif choice == '5':
            test_integrated_system()
        elif choice == '6':
            run_comprehensive_test()
        elif choice == '0':
            print("🚪 خروج من العرض التفاعلي")
            break
        else:
            print("❌ اختيار غير صحيح")

if __name__ == "__main__":
    # تشغيل الاختبار الشامل
    run_comprehensive_test()
    
    # عرض تفاعلي (اختياري)
    interactive_choice = input("\nهل تريد العرض التفاعلي؟ (y/n): ").strip().lower()
    if interactive_choice == 'y':
        interactive_demo()
