#!/usr/bin/env python3
# integrated_expert_explorer.py - النظام المتكامل للخبير والمستكشف Baserah

import uuid
import numpy as np
from datetime import datetime
from typing import Dict, List, Tuple, Union, Optional, Any

from .baserah_expert_core import (
    BaserahExpertCore, BaserahKnowledgeItem, BaserahInferenceContext, 
    BaserahInferenceResult, KnowledgeType, InferenceMethod
)
from .baserah_explorer_core import (
    BaserahExplorerCore, BaserahEquation, ExplorationConfig,
    ExplorationResult, ExplorationMode
)
from .knowledge_manager import BaserahKnowledgeManager, KnowledgeCluster, KnowledgeRelationship
from .pattern_discoverer import BaserahPatternDiscoverer, DiscoveredPattern
from .adaptive_equations import BaserahAdaptiveEquation, AdaptationMode, EvolutionDirection
from .adaptive_evolution_engine import BaserahAdaptiveEvolutionEngine, EvolutionConfig, EvolutionStrategy

class BaserahIntegratedExpertExplorer:
    """
    النظام المتكامل للخبير والمستكشف Baserah النقي
    يجمع بين النظام الخبير والمستكشف التطوري في نظام واحد متكامل
    """
    
    def __init__(self):
        """تهيئة النظام المتكامل."""
        # المكونات الأساسية
        self.expert_core = BaserahExpertCore()
        self.explorer_core = BaserahExplorerCore()
        self.knowledge_manager = BaserahKnowledgeManager()
        self.pattern_discoverer = BaserahPatternDiscoverer()

        # المكونات المتكيفة الثورية
        self.adaptive_evolution_engine = BaserahAdaptiveEvolutionEngine()
        self.adaptive_equations: List[BaserahAdaptiveEquation] = []
        
        # إعدادات النظام
        self.auto_learning = True
        self.auto_pattern_discovery = True
        self.integration_level = "full"  # full, partial, minimal
        
        # إحصائيات التكامل
        self.integration_cycles = 0
        self.successful_integrations = 0
        self.knowledge_equation_links = 0
        
        print("🧠🔍 تم تهيئة النظام المتكامل للخبير والمستكشف Baserah النقي")
        print("🧬 يشمل المعادلات المتكيفة الثورية!")
    
    def run_integrated_cycle(self, 
                           inference_context: Optional[BaserahInferenceContext] = None,
                           exploration_config: Optional[ExplorationConfig] = None) -> Dict[str, Any]:
        """تشغيل دورة متكاملة للخبير والمستكشف."""
        
        self.integration_cycles += 1
        print(f"🔄 بدء الدورة المتكاملة #{self.integration_cycles}")
        
        cycle_results = {
            'cycle_number': self.integration_cycles,
            'timestamp': datetime.now().isoformat(),
            'inference_result': None,
            'exploration_result': None,
            'patterns_discovered': [],
            'new_knowledge_items': 0,
            'new_equations': 0,
            'integration_success': False
        }
        
        try:
            # المرحلة 1: الاستدلال الخبير
            if inference_context is None:
                inference_context = BaserahInferenceContext(
                    method=InferenceMethod.HYBRID_CHAINING,
                    max_depth=5,
                    confidence_threshold=0.6
                )
            
            print("🧠 تشغيل النظام الخبير...")
            inference_result = self.expert_core.infer(inference_context)
            cycle_results['inference_result'] = inference_result
            
            # المرحلة 2: الاستكشاف التطوري
            if exploration_config is None:
                exploration_config = ExplorationConfig(
                    mode=ExplorationMode.GUIDED,
                    budget=20,
                    fitness_threshold=0.5
                )
            
            print("🔍 تشغيل المستكشف التطوري...")
            exploration_result = self.explorer_core.explore(exploration_config)
            cycle_results['exploration_result'] = exploration_result
            
            # المرحلة 3: دمج النتائج
            print("🔗 دمج نتائج الخبير والمستكشف...")
            integration_success = self._integrate_results(inference_result, exploration_result)
            cycle_results['integration_success'] = integration_success
            
            # المرحلة 4: اكتشاف الأنماط
            if self.auto_pattern_discovery:
                print("🔍 اكتشاف الأنماط...")
                all_equations = list(self.knowledge_manager.equations.values())
                if all_equations:
                    patterns = self.pattern_discoverer.discover_equation_patterns(all_equations)
                    cycle_results['patterns_discovered'] = patterns
                    
                    # إضافة الأنماط كمعرفة
                    for pattern in patterns:
                        knowledge_item = BaserahKnowledgeItem(
                            type=KnowledgeType.BASERAH_PATTERN,
                            content={
                                'pattern_type': pattern.pattern_type,
                                'description': pattern.description,
                                'properties': pattern.properties
                            },
                            relevance_score=pattern.confidence,
                            baserah_weight=pattern.support / 10.0
                        )
                        self.knowledge_manager.add_knowledge_item(knowledge_item)
                        cycle_results['new_knowledge_items'] += 1
            
            # المرحلة 5: التعلم التكيفي
            if self.auto_learning and inference_result.success:
                print("📚 تطبيق التعلم التكيفي...")
                self.expert_core.learn_from_inference(inference_context, inference_result)
            
            # تحديث الإحصائيات
            if integration_success:
                self.successful_integrations += 1
            
            cycle_results['new_equations'] = len(exploration_result.discovered_equations) if exploration_result.success else 0
            
            print(f"✅ اكتملت الدورة المتكاملة #{self.integration_cycles}")
            
        except Exception as e:
            print(f"❌ خطأ في الدورة المتكاملة: {e}")
            cycle_results['error'] = str(e)
        
        return cycle_results
    
    def _integrate_results(self, inference_result: BaserahInferenceResult, 
                          exploration_result: ExplorationResult) -> bool:
        """دمج نتائج الاستدلال والاستكشاف."""
        
        integration_success = False
        
        try:
            # إضافة المعادلات المكتشفة إلى قاعدة المعرفة
            if exploration_result.success and exploration_result.discovered_equations:
                for equation in exploration_result.discovered_equations:
                    self.knowledge_manager.add_equation(equation)
                    
                    # ربط المعادلة بالحقائق المستنتجة
                    if inference_result.success and inference_result.derived_facts:
                        for fact_id in inference_result.derived_facts:
                            relationship = KnowledgeRelationship(
                                source_id=fact_id,
                                target_id=equation.id,
                                relationship_type="supports",
                                strength=equation.fitness,
                                confidence=inference_result.confidence
                            )
                            self.knowledge_manager.add_relationship(relationship)
                            self.knowledge_equation_links += 1
                
                integration_success = True
            
            # إنشاء معرفة جديدة من نتائج الاستدلال
            if inference_result.success and inference_result.derived_facts:
                for fact_id in inference_result.derived_facts:
                    # التحقق من عدم وجود الحقيقة مسبقاً
                    if fact_id not in self.knowledge_manager.knowledge_items:
                        knowledge_item = BaserahKnowledgeItem(
                            id=fact_id,
                            type=KnowledgeType.FACT,
                            content=f"حقيقة مستنتجة: {fact_id}",
                            relevance_score=inference_result.confidence,
                            baserah_weight=inference_result.baserah_score / 10.0
                        )
                        self.knowledge_manager.add_knowledge_item(knowledge_item)
                
                integration_success = True
            
        except Exception as e:
            print(f"❌ خطأ في دمج النتائج: {e}")
            integration_success = False
        
        return integration_success
    
    def guided_exploration_with_expert(self, goal: str, max_cycles: int = 5) -> Dict[str, Any]:
        """استكشاف موجه بواسطة النظام الخبير."""
        
        print(f"🎯 بدء الاستكشاف الموجه للهدف: {goal}")
        
        results = {
            'goal': goal,
            'cycles_completed': 0,
            'total_equations_discovered': 0,
            'total_patterns_discovered': 0,
            'goal_achieved': False,
            'cycle_results': []
        }
        
        for cycle in range(max_cycles):
            print(f"\n--- الدورة {cycle + 1} من {max_cycles} ---")
            
            # إعداد سياق الاستدلال مع الهدف
            inference_context = BaserahInferenceContext(
                method=InferenceMethod.BACKWARD_CHAINING,
                goal=goal,
                max_depth=8,
                confidence_threshold=0.7
            )
            
            # إعداد تكوين الاستكشاف الموجه
            exploration_config = ExplorationConfig(
                mode=ExplorationMode.GUIDED,
                budget=30,
                fitness_threshold=0.6,
                max_complexity=5.0
            )
            
            # تشغيل الدورة المتكاملة
            cycle_result = self.run_integrated_cycle(inference_context, exploration_config)
            results['cycle_results'].append(cycle_result)
            results['cycles_completed'] += 1
            
            # تحديث الإحصائيات
            if cycle_result.get('exploration_result') and cycle_result['exploration_result'].success:
                results['total_equations_discovered'] += len(cycle_result['exploration_result'].discovered_equations)
            
            results['total_patterns_discovered'] += len(cycle_result.get('patterns_discovered', []))
            
            # فحص تحقق الهدف
            if cycle_result.get('inference_result') and cycle_result['inference_result'].success:
                if goal in cycle_result['inference_result'].derived_facts:
                    results['goal_achieved'] = True
                    print(f"🎉 تم تحقيق الهدف في الدورة {cycle + 1}!")
                    break
        
        return results
    
    def discover_equation_from_knowledge(self, knowledge_type: KnowledgeType) -> List[BaserahEquation]:
        """اكتشاف معادلات من نوع معرفة معين."""
        
        print(f"🔍 اكتشاف معادلات من معرفة نوع: {knowledge_type}")
        
        # البحث عن المعرفة من النوع المحدد
        knowledge_items = self.knowledge_manager.search_knowledge_by_type(knowledge_type)
        
        if not knowledge_items:
            print(f"⚠️ لم يتم العثور على معرفة من نوع {knowledge_type}")
            return []
        
        discovered_equations = []
        
        # استكشاف موجه بناءً على المعرفة
        for item in knowledge_items[:5]:  # أخذ أول 5 عناصر
            exploration_config = ExplorationConfig(
                mode=ExplorationMode.FOCUSED,
                budget=15,
                fitness_threshold=0.5,
                custom_properties={'guided_by_knowledge': item.id}
            )
            
            exploration_result = self.explorer_core.explore(exploration_config)
            
            if exploration_result.success:
                for equation in exploration_result.discovered_equations:
                    # ربط المعادلة بالمعرفة
                    equation.metadata['source_knowledge'] = item.id
                    equation.metadata['source_knowledge_type'] = knowledge_type.value
                    
                    discovered_equations.append(equation)
                    self.knowledge_manager.add_equation(equation)
                    
                    # إنشاء علاقة
                    relationship = KnowledgeRelationship(
                        source_id=item.id,
                        target_id=equation.id,
                        relationship_type="generates",
                        strength=equation.fitness,
                        confidence=0.8
                    )
                    self.knowledge_manager.add_relationship(relationship)
        
        print(f"✅ تم اكتشاف {len(discovered_equations)} معادلة من المعرفة")
        return discovered_equations

    def create_adaptive_equation_from_data(self, x_data: List[float], y_data: List[float]) -> BaserahAdaptiveEquation:
        """إنشاء معادلة متكيفة من البيانات."""

        print(f"🧬 إنشاء معادلة متكيفة من {len(x_data)} نقطة بيانات")

        # إنشاء معادلة متكيفة جديدة
        adaptive_eq = BaserahAdaptiveEquation(f"adaptive_from_data_{uuid.uuid4()}")

        # تحليل البيانات لتحديد النمط
        x_array = np.array(x_data)
        y_array = np.array(y_data)

        # فحص النمط الخطي
        if len(x_data) >= 2:
            linear_fit = np.polyfit(x_array, y_array, 1)
            linear_error = np.mean(np.abs(y_array - np.polyval(linear_fit, x_array)))

            if linear_error < 0.1:  # نمط خطي واضح
                adaptive_eq.add_linear_component(beta=linear_fit[0], gamma=linear_fit[1])
                print(f"   📈 تم اكتشاف نمط خطي: y = {linear_fit[0]:.3f}x + {linear_fit[1]:.3f}")
            else:
                # إضافة مكونات متنوعة للأنماط المعقدة
                adaptive_eq.add_sigmoid_component(k=2.0, alpha=np.max(y_array))
                adaptive_eq.add_linear_component(beta=linear_fit[0], gamma=linear_fit[1])
                adaptive_eq.add_quantum_component(quantum_factor=4)
                print(f"   🌊 تم اكتشاف نمط معقد: مكونات متعددة")

        # تكيف المعادلة مع البيانات
        adaptation_result = adaptive_eq.adapt_to_data(x_data, y_data)

        # إضافة للمجموعة
        self.adaptive_equations.append(adaptive_eq)

        # ربط بقاعدة المعرفة
        self.knowledge_manager.add_equation(adaptive_eq)

        print(f"✅ تم إنشاء معادلة متكيفة: خطأ نهائي={adaptation_result['final_error']:.6f}")

        return adaptive_eq

    def evolve_adaptive_equations(self, x_data: List[float], y_data: List[float],
                                 population_size: int = 10) -> Dict[str, Any]:
        """تطوير مجموعة من المعادلات المتكيفة."""

        print(f"🧬 بدء تطوير مجموعة من {population_size} معادلة متكيفة")

        # تكوين التطوير
        evolution_config = EvolutionConfig(
            strategy=EvolutionStrategy.HYBRID_EVOLUTION,
            population_size=population_size,
            max_generations=30,
            mutation_rate=0.3,
            crossover_rate=0.7,
            fitness_threshold=0.8
        )

        # تحديث محرك التطوير
        self.adaptive_evolution_engine.config = evolution_config

        # تطوير المجموعة
        evolution_result = self.adaptive_evolution_engine.evolve_population(x_data, y_data)

        # إضافة أفضل المعادلات للمجموعة
        if evolution_result.best_equation:
            self.adaptive_equations.append(evolution_result.best_equation)
            self.knowledge_manager.add_equation(evolution_result.best_equation)

        # إضافة أفضل 3 معادلات
        best_equations = self.adaptive_evolution_engine.get_best_equations(3)
        for eq in best_equations:
            if eq not in self.adaptive_equations:
                self.adaptive_equations.append(eq)
                self.knowledge_manager.add_equation(eq)

        result = {
            'evolution_success': evolution_result.success,
            'best_fitness': evolution_result.best_fitness,
            'generations': evolution_result.generation_count,
            'convergence': evolution_result.convergence_achieved,
            'best_equation': evolution_result.best_equation,
            'total_adaptive_equations': len(self.adaptive_equations)
        }

        print(f"✅ انتهى التطوير: أفضل لياقة={evolution_result.best_fitness:.6f}, "
              f"أجيال={evolution_result.generation_count}")

        return result

    def adaptive_learning_cycle(self, x_data: List[float], y_data: List[float]) -> Dict[str, Any]:
        """دورة تعلم تكيفية متكاملة."""

        print(f"🔄 بدء دورة التعلم التكيفية المتكاملة")

        cycle_results = {
            'timestamp': datetime.now().isoformat(),
            'data_points': len(x_data),
            'adaptive_equation_created': False,
            'evolution_performed': False,
            'patterns_discovered': 0,
            'knowledge_items_added': 0,
            'success': False
        }

        try:
            # المرحلة 1: إنشاء معادلة متكيفة من البيانات
            print("1️⃣ إنشاء معادلة متكيفة من البيانات...")
            adaptive_eq = self.create_adaptive_equation_from_data(x_data, y_data)
            cycle_results['adaptive_equation_created'] = True

            # المرحلة 2: تطوير مجموعة معادلات
            print("2️⃣ تطوير مجموعة معادلات متكيفة...")
            evolution_result = self.evolve_adaptive_equations(x_data, y_data, population_size=8)
            cycle_results['evolution_performed'] = evolution_result['evolution_success']

            # المرحلة 3: اكتشاف أنماط في المعادلات المتكيفة
            print("3️⃣ اكتشاف أنماط في المعادلات المتكيفة...")
            if self.adaptive_equations:
                # تحويل المعادلات المتكيفة لتنسيق BaserahEquation للتحليل
                baserah_equations = []
                for adaptive_eq in self.adaptive_equations:
                    # إنشاء BaserahEquation مكافئة
                    baserah_eq = BaserahEquation(
                        id=adaptive_eq.id,
                        equation_type="adaptive",
                        components=adaptive_eq.components,
                        complexity=len(adaptive_eq.components),
                        fitness=adaptive_eq.current_fitness
                    )
                    baserah_equations.append(baserah_eq)

                patterns = self.pattern_discoverer.discover_equation_patterns(baserah_equations)
                cycle_results['patterns_discovered'] = len(patterns)

                # إضافة الأنماط كمعرفة
                for pattern in patterns:
                    knowledge_item = BaserahKnowledgeItem(
                        type=KnowledgeType.BASERAH_PATTERN,
                        content={
                            'pattern_type': pattern.pattern_type,
                            'description': pattern.description,
                            'adaptive_context': True,
                            'properties': pattern.properties
                        },
                        relevance_score=pattern.confidence,
                        baserah_weight=pattern.support / 10.0
                    )
                    self.knowledge_manager.add_knowledge_item(knowledge_item)
                    cycle_results['knowledge_items_added'] += 1

            # المرحلة 4: تحسين المعادلات بناءً على الأنماط المكتشفة
            print("4️⃣ تحسين المعادلات بناءً على الأنماط...")
            for adaptive_eq in self.adaptive_equations[-3:]:  # أحدث 3 معادلات
                evolution_result = adaptive_eq.evolve(EvolutionDirection.OPTIMIZE)
                if evolution_result['success']:
                    print(f"   🔧 تم تحسين المعادلة {adaptive_eq.id}")

            cycle_results['success'] = True

        except Exception as e:
            print(f"❌ خطأ في دورة التعلم التكيفية: {e}")
            cycle_results['error'] = str(e)

        print(f"✅ انتهت دورة التعلم التكيفية: نجح={cycle_results['success']}")

        return cycle_results
    
    def analyze_system_performance(self) -> Dict[str, Any]:
        """تحليل أداء النظام المتكامل."""
        
        # إحصائيات النظام الخبير
        expert_stats = self.expert_core.get_statistics()
        
        # إحصائيات المستكشف
        explorer_stats = self.explorer_core.get_statistics()
        
        # إحصائيات مدير المعرفة
        knowledge_stats = self.knowledge_manager.get_statistics()
        
        # إحصائيات مكتشف الأنماط
        pattern_stats = self.pattern_discoverer.get_pattern_summary()

        # إحصائيات المعادلات المتكيفة
        adaptive_stats = self.adaptive_evolution_engine.get_statistics()
        
        # إحصائيات التكامل
        integration_success_rate = self.successful_integrations / max(1, self.integration_cycles)
        
        return {
            'integration_statistics': {
                'total_cycles': self.integration_cycles,
                'successful_integrations': self.successful_integrations,
                'integration_success_rate': integration_success_rate,
                'knowledge_equation_links': self.knowledge_equation_links
            },
            'expert_statistics': expert_stats,
            'explorer_statistics': explorer_stats,
            'knowledge_statistics': knowledge_stats,
            'pattern_statistics': pattern_stats,
            'adaptive_evolution_statistics': adaptive_stats,
            'system_health': {
                'overall_performance': (expert_stats.get('success_rate', 0) + 
                                      explorer_stats.get('success_rate', 0) + 
                                      integration_success_rate) / 3,
                'knowledge_growth_rate': knowledge_stats.get('total_knowledge_items', 0) / max(1, self.integration_cycles),
                'equation_discovery_rate': knowledge_stats.get('total_equations', 0) / max(1, self.integration_cycles),
                'pattern_discovery_rate': pattern_stats.get('total_patterns', 0) / max(1, self.integration_cycles),
                'adaptive_equations_count': len(self.adaptive_equations),
                'adaptive_evolution_success_rate': adaptive_stats.get('success_rate', 0)
            }
        }
    
    def save_integrated_system(self, base_path: str):
        """حفظ النظام المتكامل الكامل."""
        try:
            # حفظ قاعدة المعرفة
            knowledge_path = f"{base_path}_knowledge_base.json"
            self.knowledge_manager.export_knowledge_base(knowledge_path)
            
            # حفظ قاعدة معرفة النظام الخبير
            expert_kb_path = f"{base_path}_expert_knowledge.json"
            self.expert_core.save_knowledge_base(expert_kb_path)
            
            # حفظ المعادلات المكتشفة
            equations_path = f"{base_path}_discovered_equations.json"
            self.explorer_core.save_discovered_equations(equations_path)
            
            print(f"💾 تم حفظ النظام المتكامل: {base_path}")
            
        except Exception as e:
            print(f"❌ خطأ في حفظ النظام المتكامل: {e}")
    
    def load_integrated_system(self, base_path: str):
        """تحميل النظام المتكامل الكامل."""
        try:
            # تحميل قاعدة المعرفة
            knowledge_path = f"{base_path}_knowledge_base.json"
            self.knowledge_manager.import_knowledge_base(knowledge_path)
            
            # تحميل قاعدة معرفة النظام الخبير
            expert_kb_path = f"{base_path}_expert_knowledge.json"
            self.expert_core.load_knowledge_base(expert_kb_path)
            
            # تحميل المعادلات المكتشفة
            equations_path = f"{base_path}_discovered_equations.json"
            self.explorer_core.load_discovered_equations(equations_path)
            
            print(f"📂 تم تحميل النظام المتكامل: {base_path}")
            
        except Exception as e:
            print(f"❌ خطأ في تحميل النظام المتكامل: {e}")
    
    def get_system_summary(self) -> str:
        """الحصول على ملخص النظام المتكامل."""
        
        stats = self.analyze_system_performance()
        
        summary = f"""
🧠🔍🧬 ملخص النظام المتكامل للخبير والمستكشف والمعادلات المتكيفة Baserah

📊 إحصائيات التكامل:
   • دورات التكامل: {stats['integration_statistics']['total_cycles']}
   • نجح منها: {stats['integration_statistics']['successful_integrations']}
   • معدل النجاح: {stats['integration_statistics']['integration_success_rate']:.2%}
   • روابط المعرفة-المعادلات: {stats['integration_statistics']['knowledge_equation_links']}

🧠 النظام الخبير:
   • عمليات الاستدلال: {stats['expert_statistics']['total_inferences']}
   • معدل النجاح: {stats['expert_statistics']['success_rate']:.2%}
   • متوسط الثقة: {stats['expert_statistics']['average_confidence']:.3f}

🔍 المستكشف التطوري:
   • عمليات الاستكشاف: {stats['explorer_statistics']['total_explorations']}
   • معدل النجاح: {stats['explorer_statistics']['success_rate']:.2%}
   • معادلات مكتشفة: {stats['explorer_statistics']['total_equations_discovered']}

📚 مدير المعرفة:
   • عناصر المعرفة: {stats['knowledge_statistics']['total_knowledge_items']}
   • المعادلات: {stats['knowledge_statistics']['total_equations']}
   • العلاقات: {stats['knowledge_statistics']['total_relationships']}
   • المجموعات: {stats['knowledge_statistics']['total_clusters']}

🔍 مكتشف الأنماط:
   • أنماط مكتشفة: {stats['pattern_statistics']['total_patterns']}
   • معدل النجاح: {stats['pattern_statistics']['success_rate']:.2%}

🧬 المعادلات المتكيفة الثورية:
   • معادلات متكيفة: {stats['system_health']['adaptive_equations_count']}
   • تطويرات ناجحة: {stats['adaptive_evolution_statistics']['successful_evolutions']}
   • معدل نجاح التطوير: {stats['adaptive_evolution_statistics']['success_rate']:.2%}
   • أفضل لياقة محققة: {stats['adaptive_evolution_statistics']['best_fitness_achieved']:.3f}

🎯 صحة النظام:
   • الأداء العام: {stats['system_health']['overall_performance']:.2%}
   • معدل نمو المعرفة: {stats['system_health']['knowledge_growth_rate']:.1f} عنصر/دورة
   • معدل اكتشاف المعادلات: {stats['system_health']['equation_discovery_rate']:.1f} معادلة/دورة
   • معدل اكتشاف الأنماط: {stats['system_health']['pattern_discovery_rate']:.1f} نمط/دورة
        """
        
        return summary.strip()
