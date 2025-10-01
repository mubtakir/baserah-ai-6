#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
معادلة الشكل المتقدمة لنظام بصيرة

هذا الملف يحتوي على تنفيذ متقدم لمعادلة الشكل، مع التركيز على التمثيل متعدد الأبعاد،
والتطور الذاتي، والتكامل مع المفاهيم الدلالية والكمية.

المؤلف: فريق تطوير نظام بصيرة
الإصدار: 1.0.0
التاريخ: 1 يونيو 2025
"""

import os
import sys
import numpy as np
import sympy as sp
import scipy.optimize as optimize
from typing import Dict, List, Tuple, Union, Optional, Any, Callable, Set
import random
import copy
import uuid
from datetime import datetime
import logging
from enum import Enum
from dataclasses import dataclass, field

# استيراد من الوحدات الأخرى
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.symbolic_engine import AdvancedSymbolicExpression, SymbolicMetadata
from core.adaptive_calculus import QuantumAdaptiveCalculus, CalculusContext
from core.equation_evolution import AdvancedEquationEvolution, EvolutionContext, EvolutionStrategy, EvolutionDirection

# إعداد التسجيل
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("advanced_shape_equation")


class ShapeDimension(str, Enum):
    """أبعاد الشكل."""
    GEOMETRIC = "geometric"  # بعد هندسي
    TOPOLOGICAL = "topological"  # بعد طوبولوجي
    SEMANTIC = "semantic"  # بعد دلالي
    TEMPORAL = "temporal"  # بعد زمني
    QUANTUM = "quantum"  # بعد كمي
    CONCEPTUAL = "conceptual"  # بعد مفاهيمي
    EMOTIONAL = "emotional"  # بعد عاطفي
    SOCIAL = "social"  # بعد اجتماعي


@dataclass
class ShapeComponent:
    """مكون الشكل."""
    dimension: ShapeDimension  # البعد
    expression: AdvancedSymbolicExpression  # التعبير الرمزي
    weight: float = 1.0  # الوزن
    metadata: Dict[str, Any] = field(default_factory=dict)  # بيانات وصفية


@dataclass
class ShapeMetadata(SymbolicMetadata):
    """بيانات وصفية لمعادلة الشكل المتقدمة."""
    shape_type: str = "unknown"  # نوع الشكل
    dimensions_represented: Set[ShapeDimension] = field(default_factory=set)  # الأبعاد الممثلة
    semantic_tags: List[str] = field(default_factory=list)  # العلامات الدلالية
    temporal_properties: Dict[str, Any] = field(default_factory=dict)  # الخصائص الزمنية
    quantum_properties: Dict[str, Any] = field(default_factory=dict)  # الخصائص الكمية
    conceptual_links: List[str] = field(default_factory=list)  # الروابط المفاهيمية
    emotional_valence: float = 0.0  # التكافؤ العاطفي
    social_context: Dict[str, Any] = field(default_factory=dict)  # السياق الاجتماعي


class AdaptiveMatrix:
    """مصفوفة تكيفية تستخدم في عمليات تحويل الأبعاد."""
    
    def __init__(self, rows, cols):
        """
        تهيئة المصفوفة التكيفية.
        
        Args:
            rows: عدد الصفوف
            cols: عدد الأعمدة
        """
        self.rows = rows
        self.cols = cols
        self.data = np.zeros((rows, cols))
        self.gradients = np.zeros((rows, cols))
        self.learning_rate = 0.01
    
    def update(self, gradients):
        """
        تحديث المصفوفة باستخدام التدرجات.
        
        Args:
            gradients: التدرجات
        """
        self.gradients = gradients
        self.data -= self.learning_rate * self.gradients
    
    def get_data(self):
        """
        الحصول على بيانات المصفوفة.
        
        Returns:
            بيانات المصفوفة
        """
        return self.data


class AdvancedShapeEquation:
    """
    معادلة الشكل المتقدمة لنظام بصيرة.
    
    تمثل هذه الفئة شكلاً متعدد الأبعاد باستخدام مجموعة من المكونات،
    كل مكون يمثل بعداً معيناً باستخدام تعبير رمزي متقدم.
    """
    
    def __init__(self, components: Optional[List[ShapeComponent]] = None, metadata: Optional[ShapeMetadata] = None):
        """
        تهيئة معادلة الشكل المتقدمة.
        
        Args:
            components: قائمة مكونات الشكل
            metadata: بيانات وصفية للشكل
        """
        self.components: Dict[ShapeDimension, ShapeComponent] = {}
        if components:
            for comp in components:
                self.add_component(comp)
        
        self.metadata = metadata or ShapeMetadata(
            equation_id=f"shape_{uuid.uuid4()}",
            creation_date=datetime.now().isoformat()
        )
        
        # تهيئة آليات التطور
        self.evolution_engine = AdvancedEquationEvolution()
        
        # تهيئة نموذج التحويل بين الأبعاد
        self.dimension_transform_model = self._initialize_dimension_transform_model()
        
        logger.info(f"تم تهيئة معادلة الشكل المتقدمة: {self.metadata.equation_id}")
    
    def _initialize_dimension_transform_model(self):
        """
        تهيئة نموذج التحويل بين الأبعاد.
        
        Returns:
            نموذج التحويل بين الأبعاد
        """
        # إنشاء مصفوفات التحويل بين الأبعاد
        num_dimensions = len(ShapeDimension)
        model = {
            'dimension_to_hidden': AdaptiveMatrix(num_dimensions, 16),
            'hidden_to_hidden': AdaptiveMatrix(16, 16),
            'hidden_to_dimension': AdaptiveMatrix(16, num_dimensions)
        }
        
        # تهيئة المصفوفات بقيم عشوائية
        for key in model:
            model[key].data = np.random.randn(*model[key].data.shape) * 0.1
        
        return model
    
    def add_component(self, component: ShapeComponent):
        """
        إضافة مكون إلى معادلة الشكل.
        
        Args:
            component: المكون المراد إضافته
        """
        if not isinstance(component, ShapeComponent):
            raise TypeError("يجب أن يكون المكون من نوع ShapeComponent")
        
        self.components[component.dimension] = component
        self.metadata.dimensions_represented.add(component.dimension)
        self._update_metadata()
        logger.info(f"تمت إضافة مكون البعد {component.dimension} إلى الشكل {self.metadata.equation_id}")
    
    def get_component(self, dimension: ShapeDimension) -> Optional[ShapeComponent]:
        """
        الحصول على مكون بعد معين.
        
        Args:
            dimension: البعد المطلوب
            
        Returns:
            مكون البعد أو None إذا لم يكن موجوداً
        """
        return self.components.get(dimension)
    
    def remove_component(self, dimension: ShapeDimension):
        """
        إزالة مكون بعد معين.
        
        Args:
            dimension: البعد المراد إزالته
        """
        if dimension in self.components:
            del self.components[dimension]
            self.metadata.dimensions_represented.discard(dimension)
            self._update_metadata()
            logger.info(f"تمت إزالة مكون البعد {dimension} من الشكل {self.metadata.equation_id}")
    
    def evolve_component(self, dimension: ShapeDimension, context: EvolutionContext) -> Optional[ShapeComponent]:
        """
        تطوير مكون بعد معين.
        
        Args:
            dimension: البعد المراد تطويره
            context: سياق التطور
            
        Returns:
            المكون المتطور أو None إذا فشل التطور
        """
        component = self.get_component(dimension)
        if component is None:
            logger.warning(f"لا يمكن تطوير مكون غير موجود: {dimension}")
            return None
        
        # تطوير التعبير الرمزي للمكون
        result = self.evolution_engine.evolve_equation(
            component.expression,
            context.direction,
            context.strength,
            context
        )
        
        if result.success:
            # تحديث تعبير المكون
            component.expression = result.evolved_equation
            self._update_metadata()
            logger.info(f"تم تطوير مكون البعد {dimension} بنجاح")
            return component
        else:
            logger.error(f"فشل تطوير مكون البعد {dimension}: {result.message}")
            return None
    
    def evolve_shape(self, context: EvolutionContext):
        """
        تطوير الشكل بأكمله عن طريق تطوير مكوناته.
        
        Args:
            context: سياق التطور
        """
        logger.info(f"بدء تطوير الشكل {self.metadata.equation_id} باستخدام استراتيجية {context.strategy}")
        
        evolved_components = []
        for dimension in list(self.components.keys()):  # استخدام نسخة من المفاتيح للسماح بالتعديل
            evolved_component = self.evolve_component(dimension, context)
            if evolved_component:
                evolved_components.append(evolved_component)
        
        # يمكن إضافة آليات تطور أكثر تعقيداً هنا، مثل إضافة/إزالة أبعاد
        if context.strategy == EvolutionStrategy.REVOLUTIONARY:
            self._apply_revolutionary_shape_evolution(context)
        
        self._update_metadata()
        logger.info(f"اكتمل تطوير الشكل {self.metadata.equation_id}")
    
    def _apply_revolutionary_shape_evolution(self, context: EvolutionContext):
        """
        تطبيق تطور ثوري على مستوى الشكل.
        
        Args:
            context: سياق التطور
        """
        revolutionary_type = context.custom_properties.get("revolutionary_shape_type", "dimensional_emergence")
        
        if revolutionary_type == "dimensional_emergence":
            # ظهور بعد جديد
            available_dimensions = set(ShapeDimension) - self.metadata.dimensions_represented
            if available_dimensions:
                new_dimension = random.choice(list(available_dimensions))
                
                # إنشاء تعبير رمزي بسيط للبعد الجديد
                # يمكن أن يكون أكثر تعقيداً، ربما يعتمد على الأبعاد الموجودة
                var_name = new_dimension.value[0]  # استخدام الحرف الأول من اسم البعد كمتغير
                new_expr = AdvancedSymbolicExpression(expression_str=f"{var_name}**2 + 1")
                
                # إنشاء المكون الجديد
                new_component = ShapeComponent(
                    dimension=new_dimension,
                    expression=new_expr,
                    weight=random.uniform(0.5, 1.0)
                )
                
                # إضافة المكون الجديد
                self.add_component(new_component)
                logger.info(f"تطور ثوري: ظهر بعد جديد {new_dimension} في الشكل {self.metadata.equation_id}")
        
        elif revolutionary_type == "dimensional_collapse":
            # انهيار بعد
            if len(self.components) > 1:
                dimension_to_collapse = random.choice(list(self.components.keys()))
                self.remove_component(dimension_to_collapse)
                logger.info(f"تطور ثوري: انهار بعد {dimension_to_collapse} في الشكل {self.metadata.equation_id}")
        
        elif revolutionary_type == "dimensional_fusion":
            # اندماج أبعاد
            if len(self.components) > 1:
                dim1, dim2 = random.sample(list(self.components.keys()), 2)
                comp1 = self.get_component(dim1)
                comp2 = self.get_component(dim2)
                
                if comp1 and comp2:
                    # دمج تعبيري المكونين
                    merged_expr = self._merge_expressions(
                        [comp1.expression, comp2.expression],
                        weights=[comp1.weight, comp2.weight]
                    )
                    
                    # إنشاء مكون جديد للبعد المدمج (يمكن اختيار أحد البعدين أو إنشاء بعد جديد)
                    fused_dimension = dim1  # اختيار البعد الأول كبعد مدمج
                    fused_component = ShapeComponent(
                        dimension=fused_dimension,
                        expression=merged_expr,
                        weight=(comp1.weight + comp2.weight) / 2,
                        metadata={
                            "fused_from": [dim1.value, dim2.value],
                            **comp1.metadata,
                            **comp2.metadata
                        }
                    )
                    
                    # إزالة المكونين الأصليين وإضافة المكون المدمج
                    self.remove_component(dim1)
                    self.remove_component(dim2)
                    self.add_component(fused_component)
                    logger.info(f"تطور ثوري: اندمج البعدان {dim1} و {dim2} في البعد {fused_dimension} في الشكل {self.metadata.equation_id}")
    
    def _merge_expressions(self, expressions, weights=None):
        """
        دمج تعبيرات رمزية.
        
        Args:
            expressions: قائمة التعبيرات الرمزية
            weights: أوزان التعبيرات (اختياري)
            
        Returns:
            التعبير الرمزي المدمج
        """
        if not expressions:
            return AdvancedSymbolicExpression(expression_str="0")
        
        if len(expressions) == 1:
            return expressions[0]
        
        # تحديد الأوزان
        if weights is None:
            weights = [1.0] * len(expressions)
        
        # تطبيع الأوزان
        total_weight = sum(weights)
        if total_weight == 0:
            normalized_weights = [1.0 / len(expressions)] * len(expressions)
        else:
            normalized_weights = [w / total_weight for w in weights]
        
        # دمج التعبيرات
        combined_expr = 0
        all_variables = {}
        for i, expr in enumerate(expressions):
            weight = normalized_weights[i]
            combined_expr += weight * expr.expression
            all_variables.update(expr.variables)
        
        return AdvancedSymbolicExpression(
            expression_obj=combined_expr,
            variables=all_variables
        )
    
    def transform_dimension(self, source_dimension: ShapeDimension, target_dimension: ShapeDimension) -> Optional[ShapeComponent]:
        """
        تحويل بعد إلى بعد آخر.
        
        Args:
            source_dimension: البعد المصدر
            target_dimension: البعد الهدف
            
        Returns:
            مكون البعد الهدف أو None إذا فشل التحويل
        """
        source_component = self.get_component(source_dimension)
        if source_component is None:
            logger.warning(f"البعد المصدر {source_dimension} غير موجود")
            return None
        
        # استخراج خصائص البعد المصدر
        source_features = self._extract_dimension_features(source_component)
        
        # تحويل الخصائص إلى البعد الهدف
        target_features = self._transform_features(source_features, source_dimension, target_dimension)
        
        # إنشاء تعبير رمزي للبعد الهدف
        target_expr = self._create_expression_from_features(target_features, target_dimension)
        
        # إنشاء مكون البعد الهدف
        target_component = ShapeComponent(
            dimension=target_dimension,
            expression=target_expr,
            weight=source_component.weight,
            metadata={
                "transformed_from": source_dimension.value,
                **source_component.metadata
            }
        )
        
        return target_component
    
    def _extract_dimension_features(self, component: ShapeComponent) -> np.ndarray:
        """
        استخراج خصائص البعد.
        
        Args:
            component: مكون البعد
            
        Returns:
            مصفوفة الخصائص
        """
        # استخراج خصائص من التعبير الرمزي
        expr_str = str(component.expression.expression)
        
        # خصائص بسيطة
        features = np.zeros(8)
        
        # التعقيد
        features[0] = component.expression.metadata.complexity
        
        # عدد المتغيرات
        features[1] = len(component.expression.variables)
        
        # وجود دوال مثلثية
        features[2] = 1.0 if any(f in expr_str for f in ['sin', 'cos', 'tan']) else 0.0
        
        # وجود دوال أسية
        features[3] = 1.0 if any(f in expr_str for f in ['exp', 'log']) else 0.0
        
        # وجود جذور
        features[4] = 1.0 if 'sqrt' in expr_str else 0.0
        
        # وجود أعداد مركبة
        features[5] = 1.0 if any(f in expr_str for f in ['I', 'i']) else 0.0
        
        # وزن المكون
        features[6] = component.weight
        
        # رقم البعد
        features[7] = list(ShapeDimension).index(component.dimension)
        
        return features
    
    def _transform_features(self, source_features: np.ndarray, source_dimension: ShapeDimension, target_dimension: ShapeDimension) -> np.ndarray:
        """
        تحويل خصائص البعد.
        
        Args:
            source_features: خصائص البعد المصدر
            source_dimension: البعد المصدر
            target_dimension: البعد الهدف
            
        Returns:
            خصائص البعد الهدف
        """
        # تحويل الخصائص باستخدام نموذج التحويل
        # التمرير الأمامي عبر الشبكة
        h1 = np.tanh(np.dot(source_features, self.dimension_transform_model['dimension_to_hidden'].data))
        h2 = np.tanh(np.dot(h1, self.dimension_transform_model['hidden_to_hidden'].data))
        target_features = np.dot(h2, self.dimension_transform_model['hidden_to_dimension'].data)
        
        # تعديل رقم البعد
        target_features[7] = list(ShapeDimension).index(target_dimension)
        
        return target_features
    
    def _create_expression_from_features(self, features: np.ndarray, dimension: ShapeDimension) -> AdvancedSymbolicExpression:
        """
        إنشاء تعبير رمزي من الخصائص.
        
        Args:
            features: خصائص البعد
            dimension: البعد
            
        Returns:
            التعبير الرمزي
        """
        # إنشاء متغيرات
        var_name = dimension.value[0]  # استخدام الحرف الأول من اسم البعد كمتغير
        var = sp.Symbol(var_name)
        
        # إنشاء تعبير بناءً على الخصائص
        expr = var
        
        # التعقيد
        complexity = int(max(1, min(5, features[0])))
        
        # إضافة حدود متعددة الحدود
        for i in range(1, complexity + 1):
            coef = np.random.uniform(-1, 1)
            expr += coef * var ** i
        
        # إضافة دوال مثلثية
        if features[2] > 0.5:
            expr += np.random.uniform(-1, 1) * sp.sin(var)
        
        # إضافة دوال أسية
        if features[3] > 0.5:
            expr += np.random.uniform(-1, 1) * sp.exp(var * 0.1)
        
        # إضافة جذور
        if features[4] > 0.5:
            expr += np.random.uniform(-1, 1) * sp.sqrt(sp.Abs(var) + 0.1)
        
        # إضافة أعداد مركبة
        if features[5] > 0.5:
            expr += np.random.uniform(-1, 1) * sp.I * var
        
        # إنشاء التعبير الرمزي
        return AdvancedSymbolicExpression(
            expression_obj=expr,
            variables={var_name: var}
        )
    
    def evaluate(self, point: Dict[str, float], dimension: Optional[ShapeDimension] = None) -> Union[float, Dict[ShapeDimension, float]]:
        """
        تقييم معادلة الشكل عند نقطة معينة.
        
        Args:
            point: نقطة التقييم (قاموس بأسماء المتغيرات وقيمها)
            dimension: البعد المراد تقييمه (اختياري، لتقييم بعد واحد)
            
        Returns:
            قيمة المعادلة عند النقطة (إما قيمة واحدة إذا تم تحديد بعد، أو قاموس بالقيم لكل بعد)
        """
        if dimension:
            component = self.get_component(dimension)
            if component:
                try:
                    return component.expression.evaluate(point)
                except Exception as e:
                    logger.error(f"خطأ في تقييم البعد {dimension}: {str(e)}")
                    return np.nan  # أو قيمة أخرى تشير إلى خطأ
            else:
                logger.warning(f"البعد {dimension} غير موجود في الشكل")
                return np.nan
        else:
            # تقييم جميع الأبعاد
            results = {}
            for dim, comp in self.components.items():
                try:
                    results[dim] = comp.expression.evaluate(point)
                except Exception as e:
                    logger.error(f"خطأ في تقييم البعد {dim}: {str(e)}")
                    results[dim] = np.nan
            return results
    
    def get_combined_expression(self, weights: Optional[Dict[ShapeDimension, float]] = None) -> AdvancedSymbolicExpression:
        """
        الحصول على تعبير رمزي مدمج يمثل الشكل بأكمله.
        
        Args:
            weights: أوزان اختيارية للأبعاد (إذا لم يتم توفيرها، تستخدم أوزان المكونات)
            
        Returns:
            تعبير رمزي مدمج
        """
        if not self.components:
            return AdvancedSymbolicExpression(expression_str="0")
        
        # تحديد الأوزان
        if weights is None:
            component_weights = {dim: comp.weight for dim, comp in self.components.items()}
        else:
            component_weights = weights
        
        # تطبيع الأوزان
        total_weight = sum(component_weights.values())
        if total_weight == 0:
            normalized_weights = {dim: 1.0 / len(self.components) for dim in self.components}
        else:
            normalized_weights = {dim: w / total_weight for dim, w in component_weights.items()}
        
        # دمج التعبيرات
        combined_expr = 0
        all_variables = {}
        for dim, comp in self.components.items():
            weight = normalized_weights.get(dim, 0)
            combined_expr += weight * comp.expression.expression
            all_variables.update(comp.expression.variables)
        
        return AdvancedSymbolicExpression(
            expression_obj=combined_expr,
            variables=all_variables
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        تحويل معادلة الشكل إلى قاموس.
        
        Returns:
            قاموس يمثل معادلة الشكل
        """
        return {
            "metadata": self.metadata.to_dict(),
            "components": {
                dim.value: {
                    "expression": comp.expression.to_dict(),
                    "weight": comp.weight,
                    "metadata": comp.metadata
                }
                for dim, comp in self.components.items()
            }
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AdvancedShapeEquation":
        """
        إنشاء معادلة شكل من قاموس.
        
        Args:
            data: قاموس يمثل معادلة الشكل
            
        Returns:
            كائن AdvancedShapeEquation
        """
        metadata = ShapeMetadata.from_dict(data.get("metadata", {}))
        components_data = data.get("components", {})
        
        components = []
        for dim_str, comp_data in components_data.items():
            try:
                dimension = ShapeDimension(dim_str)
                expression = AdvancedSymbolicExpression.from_dict(comp_data.get("expression", {}))
                weight = comp_data.get("weight", 1.0)
                comp_metadata = comp_data.get("metadata", {})
                
                components.append(ShapeComponent(
                    dimension=dimension,
                    expression=expression,
                    weight=weight,
                    metadata=comp_metadata
                ))
            except ValueError:
                logger.warning(f"تجاهل بعد غير معروف: {dim_str}")
            except Exception as e:
                logger.error(f"خطأ في تحميل المكون {dim_str}: {str(e)}")
        
        return cls(components=components, metadata=metadata)
    
    def _update_metadata(self):
        """
        تحديث البيانات الوصفية للشكل بناءً على مكوناته.
        """
        self.metadata.dimensions_represented = set(self.components.keys())
        
        # تحديث التعقيد (يمكن استخدام متوسط التعقيد أو المجموع)
        if self.components:
            total_complexity = sum(comp.expression.metadata.complexity * comp.weight for comp in self.components.values())
            total_weight = sum(comp.weight for comp in self.components.values())
            self.metadata.complexity = total_complexity / total_weight if total_weight else 0
        else:
            self.metadata.complexity = 0
        
        # تحديث العلامات الدلالية (دمج العلامات من المكونات)
        all_tags = set()
        for comp in self.components.values():
            if hasattr(comp.expression.metadata, 'semantic_tags'):
                all_tags.update(comp.expression.metadata.semantic_tags)
        self.metadata.semantic_tags = list(all_tags)
        
        # تحديث نوع الشكل
        self._determine_shape_type()
    
    def _determine_shape_type(self):
        """
        تحديد نوع الشكل بناءً على مكوناته.
        """
        # تحديد نوع الشكل بناءً على الأبعاد الممثلة
        if not self.components:
            self.metadata.shape_type = "empty"
            return
        
        # تحديد نوع الشكل بناءً على البعد الهندسي
        geometric_component = self.get_component(ShapeDimension.GEOMETRIC)
        if geometric_component:
            expr_str = str(geometric_component.expression.expression)
            
            if "circle" in expr_str or "sphere" in expr_str or "x**2 + y**2" in expr_str:
                self.metadata.shape_type = "circular"
            elif "square" in expr_str or "rectangle" in expr_str or "box" in expr_str:
                self.metadata.shape_type = "rectangular"
            elif "triangle" in expr_str:
                self.metadata.shape_type = "triangular"
            elif "polygon" in expr_str:
                self.metadata.shape_type = "polygonal"
            elif "curve" in expr_str or "spline" in expr_str:
                self.metadata.shape_type = "curved"
            else:
                self.metadata.shape_type = "geometric"
        
        # تحديد نوع الشكل بناءً على الأبعاد الأخرى
        elif ShapeDimension.TOPOLOGICAL in self.components:
            self.metadata.shape_type = "topological"
        elif ShapeDimension.SEMANTIC in self.components:
            self.metadata.shape_type = "semantic"
        elif ShapeDimension.TEMPORAL in self.components:
            self.metadata.shape_type = "temporal"
        elif ShapeDimension.QUANTUM in self.components:
            self.metadata.shape_type = "quantum"
        elif ShapeDimension.CONCEPTUAL in self.components:
            self.metadata.shape_type = "conceptual"
        elif ShapeDimension.EMOTIONAL in self.components:
            self.metadata.shape_type = "emotional"
        elif ShapeDimension.SOCIAL in self.components:
            self.metadata.shape_type = "social"
        else:
            self.metadata.shape_type = "unknown"
        
        # تحديث نوع الشكل بناءً على عدد الأبعاد
        num_dimensions = len(self.components)
        if num_dimensions > 3:
            self.metadata.shape_type = f"multidimensional_{self.metadata.shape_type}"
        
        # تحديث نوع الشكل بناءً على الخصائص الكمية
        quantum_component = self.get_component(ShapeDimension.QUANTUM)
        if quantum_component:
            expr_str = str(quantum_component.expression.expression)
            if "I" in expr_str or "i" in expr_str:  # وجود الوحدة التخيلية
                self.metadata.shape_type = f"quantum_{self.metadata.shape_type}"
    
    def visualize(self, dimension: Optional[ShapeDimension] = None, resolution: int = 100, range_min: float = -5.0, range_max: float = 5.0):
        """
        تصور الشكل.
        
        Args:
            dimension: البعد المراد تصوره (اختياري، لتصور بعد واحد)
            resolution: دقة التصور
            range_min: الحد الأدنى للنطاق
            range_max: الحد الأعلى للنطاق
            
        Returns:
            بيانات التصور
        """
        # تحديد البعد المراد تصوره
        if dimension:
            components = {dimension: self.get_component(dimension)} if self.get_component(dimension) else {}
        else:
            components = self.components
        
        if not components:
            logger.warning("لا توجد مكونات للتصور")
            return None
        
        # إنشاء نقاط التقييم
        x = np.linspace(range_min, range_max, resolution)
        y = np.linspace(range_min, range_max, resolution)
        X, Y = np.meshgrid(x, y)
        
        # تقييم المكونات
        visualization_data = {}
        for dim, comp in components.items():
            try:
                # إنشاء نقاط التقييم
                points = []
                for i in range(resolution):
                    for j in range(resolution):
                        # تحديد أسماء المتغيرات
                        var_names = list(comp.expression.variables.keys())
                        if len(var_names) >= 2:
                            point = {var_names[0]: X[i, j], var_names[1]: Y[i, j]}
                            for k in range(2, len(var_names)):
                                point[var_names[k]] = 0.0  # تعيين المتغيرات الإضافية إلى صفر
                        elif len(var_names) == 1:
                            point = {var_names[0]: X[i, j]}
                        else:
                            continue
                        
                        points.append(point)
                
                # تقييم النقاط
                values = np.zeros((resolution, resolution))
                for idx, point in enumerate(points):
                    i, j = idx // resolution, idx % resolution
                    try:
                        values[i, j] = comp.expression.evaluate(point)
                    except:
                        values[i, j] = np.nan
                
                # تخزين البيانات
                visualization_data[dim] = {
                    'X': X,
                    'Y': Y,
                    'Z': values
                }
            except Exception as e:
                logger.error(f"خطأ في تصور البعد {dim}: {str(e)}")
        
        return visualization_data
    
    def get_command_representation(self, dimension: Optional[ShapeDimension] = None) -> List[str]:
        """
        الحصول على تمثيل الشكل بصيغة أوامر.
        
        Args:
            dimension: البعد المراد تمثيله (اختياري، لتمثيل بعد واحد)
            
        Returns:
            قائمة الأوامر
        """
        # تحديد البعد المراد تمثيله
        if dimension:
            components = {dimension: self.get_component(dimension)} if self.get_component(dimension) else {}
        else:
            components = self.components
        
        if not components:
            return ["# لا توجد مكونات للتمثيل"]
        
        # إنشاء قائمة الأوامر
        commands = []
        
        # إضافة أوامر البداية
        commands.append("PEN_UP")
        commands.append("SET_THICKNESS 2")
        
        # إضافة أوامر لكل بعد
        for dim, comp in components.items():
            # إضافة تعليق للبعد
            commands.append(f"# بعد {dim.value}")
            
            # تحديد لون البعد
            color = self._get_dimension_color(dim)
            commands.append(f"SET_COLOR_HEX {color}")
            
            # تحديد نوع الشكل بناءً على التعبير
            expr_str = str(comp.expression.expression)
            
            if "circle" in expr_str or "sphere" in expr_str or "x**2 + y**2" in expr_str:
                # دائرة
                radius = random.uniform(1.0, 3.0)
                commands.append(f"MOVE_TO 0 0")
                commands.append("PEN_DOWN")
                commands.append(f"CIRCLE {radius}")
                commands.append("PEN_UP")
            
            elif "square" in expr_str or "rectangle" in expr_str or "box" in expr_str:
                # مستطيل
                width = random.uniform(2.0, 4.0)
                height = random.uniform(2.0, 4.0)
                commands.append(f"MOVE_TO {-width/2} {-height/2}")
                commands.append("PEN_DOWN")
                commands.append(f"RECTANGLE {width} {height}")
                commands.append("PEN_UP")
            
            elif "triangle" in expr_str:
                # مثلث
                size = random.uniform(2.0, 4.0)
                commands.append(f"MOVE_TO {-size/2} {-size/2}")
                commands.append("PEN_DOWN")
                commands.append(f"LINE_TO {size/2} {-size/2}")
                commands.append(f"LINE_TO 0 {size/2}")
                commands.append(f"LINE_TO {-size/2} {-size/2}")
                commands.append("CLOSE_PATH")
                commands.append("PEN_UP")
            
            elif "sin" in expr_str or "cos" in expr_str:
                # منحنى جيبي
                commands.append(f"MOVE_TO {-4} 0")
                commands.append("PEN_DOWN")
                for x in np.linspace(-4, 4, 20):
                    y = np.sin(x) if "sin" in expr_str else np.cos(x)
                    commands.append(f"LINE_TO {x} {y}")
                commands.append("PEN_UP")
            
            elif "exp" in expr_str:
                # منحنى أسي
                commands.append(f"MOVE_TO {-4} 0")
                commands.append("PEN_DOWN")
                for x in np.linspace(-4, 2, 20):
                    y = np.exp(x) if x < 2 else 6  # تحديد الارتفاع الأقصى
                    commands.append(f"LINE_TO {x} {y}")
                commands.append("PEN_UP")
            
            else:
                # منحنى عام
                commands.append(f"MOVE_TO {-4} 0")
                commands.append("PEN_DOWN")
                for x in np.linspace(-4, 4, 20):
                    # استخدام قيمة عشوائية للتوضيح
                    y = random.uniform(-2, 2)
                    commands.append(f"LINE_TO {x} {y}")
                commands.append("PEN_UP")
        
        return commands
    
    def _get_dimension_color(self, dimension: ShapeDimension) -> str:
        """
        الحصول على لون البعد.
        
        Args:
            dimension: البعد
            
        Returns:
            اللون بصيغة HEX
        """
        # تعيين لون لكل بعد
        colors = {
            ShapeDimension.GEOMETRIC: "#FF0000",  # أحمر
            ShapeDimension.TOPOLOGICAL: "#00FF00",  # أخضر
            ShapeDimension.SEMANTIC: "#0000FF",  # أزرق
            ShapeDimension.TEMPORAL: "#FFFF00",  # أصفر
            ShapeDimension.QUANTUM: "#FF00FF",  # أرجواني
            ShapeDimension.CONCEPTUAL: "#00FFFF",  # سماوي
            ShapeDimension.EMOTIONAL: "#FFA500",  # برتقالي
            ShapeDimension.SOCIAL: "#800080"  # بنفسجي
        }
        
        return colors.get(dimension, "#000000")  # أسود افتراضي


# اختبار الوحدة
if __name__ == "__main__":
    # إنشاء معادلة شكل متقدمة
    # إنشاء مكون هندسي
    geometric_expr = AdvancedSymbolicExpression(expression_str="x**2 + y**2 - 4")
    geometric_component = ShapeComponent(
        dimension=ShapeDimension.GEOMETRIC,
        expression=geometric_expr,
        weight=1.0
    )
    
    # إنشاء مكون دلالي
    semantic_expr = AdvancedSymbolicExpression(expression_str="s**2 - t")
    semantic_component = ShapeComponent(
        dimension=ShapeDimension.SEMANTIC,
        expression=semantic_expr,
        weight=0.8
    )
    
    # إنشاء معادلة الشكل
    shape_equation = AdvancedShapeEquation(
        components=[geometric_component, semantic_component]
    )
    
    # تطوير الشكل
    context = EvolutionContext(
        strategy=EvolutionStrategy.DIRECTED,
        direction=EvolutionDirection.EXTEND,
        strength=0.5
    )
    shape_equation.evolve_shape(context)
    
    # تقييم الشكل
    point = {"x": 1.0, "y": 1.0, "s": 2.0, "t": 1.0}
    result = shape_equation.evaluate(point)
    
    # طباعة النتيجة
    print(f"نتيجة التقييم: {result}")
    
    # الحصول على تمثيل الأوامر
    commands = shape_equation.get_command_representation()
    print("\nتمثيل الأوامر:")
    for cmd in commands:
        print(cmd)
