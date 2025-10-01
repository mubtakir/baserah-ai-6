#!/usr/bin/env python3
# pattern_discoverer.py - مكتشف الأنماط Baserah النقي

import math
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Union, Optional, Any, Set
from dataclasses import dataclass, field
from collections import Counter, defaultdict

from .baserah_expert_core import BaserahKnowledgeItem, KnowledgeType
from .baserah_explorer_core import BaserahEquation

@dataclass
class DiscoveredPattern:
    """نمط مكتشف Baserah."""
    id: str = field(default_factory=lambda: f"pattern_{uuid.uuid4()}")
    pattern_type: str = "general"
    description: str = ""
    confidence: float = 1.0
    support: int = 1  # عدد العناصر التي تدعم النمط
    items: List[str] = field(default_factory=list)  # العناصر المرتبطة بالنمط
    properties: Dict[str, Any] = field(default_factory=dict)
    discovery_method: str = "automatic"
    creation_date: str = field(default_factory=lambda: datetime.now().isoformat())
    metadata: Dict[str, Any] = field(default_factory=dict)

class BaserahPatternDiscoverer:
    """
    مكتشف الأنماط Baserah النقي
    يكتشف الأنماط في المعرفة والمعادلات باستخدام منهج Baserah فقط
    """
    
    def __init__(self):
        """تهيئة مكتشف الأنماط Baserah."""
        self.discovered_patterns: List[DiscoveredPattern] = []
        self.pattern_history: List[Dict[str, Any]] = []
        
        # إعدادات الاكتشاف
        self.min_support = 2  # الحد الأدنى لدعم النمط
        self.min_confidence = 0.5  # الحد الأدنى للثقة
        
        # إحصائيات
        self.discovery_count = 0
        self.successful_discoveries = 0
        
        print("🔍 تم تهيئة مكتشف الأنماط Baserah النقي")
    
    def discover_equation_patterns(self, equations: List[BaserahEquation]) -> List[DiscoveredPattern]:
        """اكتشاف الأنماط في المعادلات."""
        if not equations:
            return []
        
        self.discovery_count += 1
        print(f"🔍 بدء اكتشاف أنماط المعادلات #{self.discovery_count}")
        
        patterns = []
        
        # نمط أنواع المكونات
        component_patterns = self._discover_component_type_patterns(equations)
        patterns.extend(component_patterns)
        
        # نمط التعقيد
        complexity_patterns = self._discover_complexity_patterns(equations)
        patterns.extend(complexity_patterns)
        
        # نمط المتغيرات
        variable_patterns = self._discover_variable_patterns(equations)
        patterns.extend(variable_patterns)
        
        # نمط المعاملات
        parameter_patterns = self._discover_parameter_patterns(equations)
        patterns.extend(parameter_patterns)
        
        # نمط عوامل التكميم
        quantum_patterns = self._discover_quantum_patterns(equations)
        patterns.extend(quantum_patterns)
        
        # نمط اللياقة
        fitness_patterns = self._discover_fitness_patterns(equations)
        patterns.extend(fitness_patterns)
        
        # حفظ الأنماط المكتشفة
        self.discovered_patterns.extend(patterns)
        
        if patterns:
            self.successful_discoveries += 1
        
        # تسجيل الاكتشاف
        self.pattern_history.append({
            'timestamp': datetime.now().isoformat(),
            'input_equations': len(equations),
            'patterns_discovered': len(patterns),
            'discovery_method': 'equation_analysis'
        })
        
        print(f"✅ تم اكتشاف {len(patterns)} نمط في المعادلات")
        return patterns
    
    def _discover_component_type_patterns(self, equations: List[BaserahEquation]) -> List[DiscoveredPattern]:
        """اكتشاف أنماط أنواع المكونات."""
        patterns = []
        
        # إحصاء أنواع المكونات
        component_counts = Counter()
        component_combinations = Counter()
        
        for equation in equations:
            eq_components = [comp['type'] for comp in equation.components]
            
            # عد الأنواع الفردية
            for comp_type in eq_components:
                component_counts[comp_type] += 1
            
            # عد التركيبات
            if len(eq_components) > 1:
                combination = tuple(sorted(eq_components))
                component_combinations[combination] += 1
        
        # إنشاء أنماط للأنواع الشائعة
        for comp_type, count in component_counts.items():
            if count >= self.min_support:
                confidence = count / len(equations)
                if confidence >= self.min_confidence:
                    pattern = DiscoveredPattern(
                        pattern_type="component_type",
                        description=f"نمط مكون {comp_type}: يظهر في {count} معادلة",
                        confidence=confidence,
                        support=count,
                        items=[eq.id for eq in equations if any(comp['type'] == comp_type for comp in eq.components)],
                        properties={
                            'component_type': comp_type,
                            'frequency': count,
                            'percentage': confidence * 100
                        },
                        discovery_method="component_type_analysis"
                    )
                    patterns.append(pattern)
        
        # إنشاء أنماط للتركيبات الشائعة
        for combination, count in component_combinations.items():
            if count >= self.min_support:
                confidence = count / len(equations)
                if confidence >= self.min_confidence:
                    pattern = DiscoveredPattern(
                        pattern_type="component_combination",
                        description=f"نمط تركيب {'+'.join(combination)}: يظهر في {count} معادلة",
                        confidence=confidence,
                        support=count,
                        items=[eq.id for eq in equations if tuple(sorted([comp['type'] for comp in eq.components])) == combination],
                        properties={
                            'combination': list(combination),
                            'frequency': count,
                            'percentage': confidence * 100
                        },
                        discovery_method="component_combination_analysis"
                    )
                    patterns.append(pattern)
        
        return patterns
    
    def _discover_complexity_patterns(self, equations: List[BaserahEquation]) -> List[DiscoveredPattern]:
        """اكتشاف أنماط التعقيد."""
        patterns = []
        
        if not equations:
            return patterns
        
        complexities = [eq.complexity for eq in equations]
        avg_complexity = sum(complexities) / len(complexities)
        min_complexity = min(complexities)
        max_complexity = max(complexities)
        
        # تجميع المعادلات حسب مستوى التعقيد
        complexity_groups = {
            'simple': [eq for eq in equations if eq.complexity <= avg_complexity * 0.7],
            'moderate': [eq for eq in equations if avg_complexity * 0.7 < eq.complexity <= avg_complexity * 1.3],
            'complex': [eq for eq in equations if eq.complexity > avg_complexity * 1.3]
        }
        
        for group_name, group_equations in complexity_groups.items():
            if len(group_equations) >= self.min_support:
                confidence = len(group_equations) / len(equations)
                if confidence >= self.min_confidence:
                    pattern = DiscoveredPattern(
                        pattern_type="complexity_level",
                        description=f"نمط تعقيد {group_name}: {len(group_equations)} معادلة",
                        confidence=confidence,
                        support=len(group_equations),
                        items=[eq.id for eq in group_equations],
                        properties={
                            'complexity_level': group_name,
                            'average_complexity': sum(eq.complexity for eq in group_equations) / len(group_equations),
                            'count': len(group_equations),
                            'percentage': confidence * 100
                        },
                        discovery_method="complexity_analysis"
                    )
                    patterns.append(pattern)
        
        return patterns
    
    def _discover_variable_patterns(self, equations: List[BaserahEquation]) -> List[DiscoveredPattern]:
        """اكتشاف أنماط المتغيرات."""
        patterns = []
        
        # إحصاء المتغيرات
        variable_counts = Counter()
        variable_combinations = Counter()
        
        for equation in equations:
            variables = list(equation.variables)
            
            # عد المتغيرات الفردية
            for variable in variables:
                variable_counts[variable] += 1
            
            # عد تركيبات المتغيرات
            if len(variables) > 1:
                combination = tuple(sorted(variables))
                variable_combinations[combination] += 1
        
        # أنماط المتغيرات الشائعة
        for variable, count in variable_counts.items():
            if count >= self.min_support:
                confidence = count / len(equations)
                if confidence >= self.min_confidence:
                    pattern = DiscoveredPattern(
                        pattern_type="variable_usage",
                        description=f"نمط متغير {variable}: يستخدم في {count} معادلة",
                        confidence=confidence,
                        support=count,
                        items=[eq.id for eq in equations if variable in eq.variables],
                        properties={
                            'variable': variable,
                            'frequency': count,
                            'percentage': confidence * 100
                        },
                        discovery_method="variable_analysis"
                    )
                    patterns.append(pattern)
        
        return patterns
    
    def _discover_parameter_patterns(self, equations: List[BaserahEquation]) -> List[DiscoveredPattern]:
        """اكتشاف أنماط المعاملات."""
        patterns = []
        
        # تجميع المعاملات حسب النوع
        sigmoid_params = {'n': [], 'k': [], 'x0': [], 'alpha': []}
        linear_params = {'beta': [], 'gamma': []}
        
        for equation in equations:
            for component in equation.components:
                if component['type'] == 'sigmoid':
                    params = component['params']
                    for param_name in sigmoid_params:
                        if param_name in params:
                            sigmoid_params[param_name].append(params[param_name])
                elif component['type'] == 'linear':
                    params = component['params']
                    for param_name in linear_params:
                        if param_name in params:
                            linear_params[param_name].append(params[param_name])
        
        # تحليل أنماط معاملات السيجمويد
        for param_name, values in sigmoid_params.items():
            if len(values) >= self.min_support:
                avg_value = sum(values) / len(values)
                
                # تجميع القيم المتشابهة
                similar_values = [v for v in values if abs(v - avg_value) <= abs(avg_value) * 0.2]
                
                if len(similar_values) >= self.min_support:
                    confidence = len(similar_values) / len(values)
                    if confidence >= self.min_confidence:
                        pattern = DiscoveredPattern(
                            pattern_type="sigmoid_parameter",
                            description=f"نمط معامل سيجمويد {param_name}: قيم متشابهة حول {avg_value:.3f}",
                            confidence=confidence,
                            support=len(similar_values),
                            properties={
                                'parameter_name': param_name,
                                'average_value': avg_value,
                                'similar_values_count': len(similar_values),
                                'total_values_count': len(values),
                                'percentage': confidence * 100
                            },
                            discovery_method="sigmoid_parameter_analysis"
                        )
                        patterns.append(pattern)
        
        # تحليل أنماط المعاملات الخطية
        for param_name, values in linear_params.items():
            if len(values) >= self.min_support:
                avg_value = sum(values) / len(values)
                
                # تجميع القيم المتشابهة
                similar_values = [v for v in values if abs(v - avg_value) <= abs(avg_value) * 0.2]
                
                if len(similar_values) >= self.min_support:
                    confidence = len(similar_values) / len(values)
                    if confidence >= self.min_confidence:
                        pattern = DiscoveredPattern(
                            pattern_type="linear_parameter",
                            description=f"نمط معامل خطي {param_name}: قيم متشابهة حول {avg_value:.3f}",
                            confidence=confidence,
                            support=len(similar_values),
                            properties={
                                'parameter_name': param_name,
                                'average_value': avg_value,
                                'similar_values_count': len(similar_values),
                                'total_values_count': len(values),
                                'percentage': confidence * 100
                            },
                            discovery_method="linear_parameter_analysis"
                        )
                        patterns.append(pattern)
        
        return patterns
    
    def _discover_quantum_patterns(self, equations: List[BaserahEquation]) -> List[DiscoveredPattern]:
        """اكتشاف أنماط عوامل التكميم."""
        patterns = []
        
        # جمع عوامل التكميم
        quantum_factors = []
        quantum_equations = []
        
        for equation in equations:
            for component in equation.components:
                if component['type'] == 'quantum_sigmoid':
                    quantum_factor = component['params'].get('quantum_factor', 1)
                    quantum_factors.append(quantum_factor)
                    if equation not in quantum_equations:
                        quantum_equations.append(equation)
        
        if not quantum_factors:
            return patterns
        
        # إحصاء عوامل التكميم
        qf_counts = Counter(quantum_factors)
        
        for qf, count in qf_counts.items():
            if count >= self.min_support:
                confidence = count / len(quantum_factors)
                if confidence >= self.min_confidence:
                    pattern = DiscoveredPattern(
                        pattern_type="quantum_factor",
                        description=f"نمط عامل تكميم {qf}: يستخدم {count} مرة",
                        confidence=confidence,
                        support=count,
                        items=[eq.id for eq in equations if any(
                            comp['type'] == 'quantum_sigmoid' and comp['params'].get('quantum_factor') == qf
                            for comp in eq.components
                        )],
                        properties={
                            'quantum_factor': qf,
                            'frequency': count,
                            'percentage': confidence * 100,
                            'step_size': 1.0 / qf if qf > 0 else 1.0
                        },
                        discovery_method="quantum_factor_analysis"
                    )
                    patterns.append(pattern)
        
        return patterns
    
    def _discover_fitness_patterns(self, equations: List[BaserahEquation]) -> List[DiscoveredPattern]:
        """اكتشاف أنماط اللياقة."""
        patterns = []
        
        # تصفية المعادلات التي لها قيم لياقة
        fitness_equations = [eq for eq in equations if eq.fitness > 0]
        
        if len(fitness_equations) < self.min_support:
            return patterns
        
        fitness_values = [eq.fitness for eq in fitness_equations]
        avg_fitness = sum(fitness_values) / len(fitness_values)
        
        # تجميع المعادلات حسب مستوى اللياقة
        fitness_groups = {
            'high_fitness': [eq for eq in fitness_equations if eq.fitness >= avg_fitness * 1.2],
            'medium_fitness': [eq for eq in fitness_equations if avg_fitness * 0.8 <= eq.fitness < avg_fitness * 1.2],
            'low_fitness': [eq for eq in fitness_equations if eq.fitness < avg_fitness * 0.8]
        }
        
        for group_name, group_equations in fitness_groups.items():
            if len(group_equations) >= self.min_support:
                confidence = len(group_equations) / len(fitness_equations)
                if confidence >= self.min_confidence:
                    pattern = DiscoveredPattern(
                        pattern_type="fitness_level",
                        description=f"نمط لياقة {group_name}: {len(group_equations)} معادلة",
                        confidence=confidence,
                        support=len(group_equations),
                        items=[eq.id for eq in group_equations],
                        properties={
                            'fitness_level': group_name,
                            'average_fitness': sum(eq.fitness for eq in group_equations) / len(group_equations),
                            'count': len(group_equations),
                            'percentage': confidence * 100
                        },
                        discovery_method="fitness_analysis"
                    )
                    patterns.append(pattern)
        
        return patterns
    
    def discover_knowledge_patterns(self, knowledge_items: List[BaserahKnowledgeItem]) -> List[DiscoveredPattern]:
        """اكتشاف الأنماط في عناصر المعرفة."""
        if not knowledge_items:
            return []
        
        patterns = []
        
        # نمط أنواع المعرفة
        type_counts = Counter(item.type for item in knowledge_items)
        
        for knowledge_type, count in type_counts.items():
            if count >= self.min_support:
                confidence = count / len(knowledge_items)
                if confidence >= self.min_confidence:
                    pattern = DiscoveredPattern(
                        pattern_type="knowledge_type",
                        description=f"نمط نوع معرفة {knowledge_type.value}: {count} عنصر",
                        confidence=confidence,
                        support=count,
                        items=[item.id for item in knowledge_items if item.type == knowledge_type],
                        properties={
                            'knowledge_type': knowledge_type.value,
                            'frequency': count,
                            'percentage': confidence * 100
                        },
                        discovery_method="knowledge_type_analysis"
                    )
                    patterns.append(pattern)
        
        return patterns
    
    def get_pattern_summary(self) -> Dict[str, Any]:
        """الحصول على ملخص الأنماط المكتشفة."""
        if not self.discovered_patterns:
            return {'total_patterns': 0}
        
        # إحصاء أنواع الأنماط
        pattern_type_counts = Counter(pattern.pattern_type for pattern in self.discovered_patterns)
        
        # إحصاء طرق الاكتشاف
        discovery_method_counts = Counter(pattern.discovery_method for pattern in self.discovered_patterns)
        
        # متوسط الثقة والدعم
        avg_confidence = sum(pattern.confidence for pattern in self.discovered_patterns) / len(self.discovered_patterns)
        avg_support = sum(pattern.support for pattern in self.discovered_patterns) / len(self.discovered_patterns)
        
        return {
            'total_patterns': len(self.discovered_patterns),
            'pattern_type_distribution': dict(pattern_type_counts),
            'discovery_method_distribution': dict(discovery_method_counts),
            'average_confidence': avg_confidence,
            'average_support': avg_support,
            'discovery_count': self.discovery_count,
            'successful_discoveries': self.successful_discoveries,
            'success_rate': self.successful_discoveries / max(1, self.discovery_count)
        }
    
    def get_patterns_by_type(self, pattern_type: str) -> List[DiscoveredPattern]:
        """الحصول على الأنماط حسب النوع."""
        return [pattern for pattern in self.discovered_patterns if pattern.pattern_type == pattern_type]
    
    def get_high_confidence_patterns(self, min_confidence: float = 0.8) -> List[DiscoveredPattern]:
        """الحصول على الأنماط عالية الثقة."""
        return [pattern for pattern in self.discovered_patterns if pattern.confidence >= min_confidence]
