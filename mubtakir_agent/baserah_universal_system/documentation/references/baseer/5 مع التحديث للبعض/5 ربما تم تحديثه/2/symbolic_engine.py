#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
محرك المعالجة الرمزية المتقدم لنظام بصيرة

هذا الملف يحتوي على تنفيذ محرك المعالجة الرمزية المتقدم، والذي يوفر قدرات معالجة رمزية
متقدمة تتجاوز ما هو متاح في SymPy التقليدي. يركز هذا المحرك على التعبيرات الرمزية المتطورة،
والتبسيط الذكي، والتحليل الهيكلي، والتوليد الإبداعي.

المؤلف: فريق تطوير نظام بصيرة
الإصدار: 1.0.0
التاريخ: 1 يونيو 2025
"""

import os
import sys
import numpy as np
import sympy as sp
from typing import Dict, List, Tuple, Union, Optional, Any, Callable, Set
import random
import copy
import uuid
from datetime import datetime
import logging
from enum import Enum
from dataclasses import dataclass, field

# إعداد التسجيل
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('symbolic_engine')


class SymbolicEvolutionDirection(str, Enum):
    """اتجاهات تطور التعبيرات الرمزية."""
    SIMPLIFY = "simplify"  # تبسيط التعبير
    EXPAND = "expand"  # توسيع التعبير
    FACTORIZE = "factorize"  # تحليل التعبير إلى عوامل
    GENERALIZE = "generalize"  # تعميم التعبير
    SPECIALIZE = "specialize"  # تخصيص التعبير
    TRANSFORM = "transform"  # تحويل التعبير
    MUTATE = "mutate"  # تغيير عشوائي في التعبير
    OPTIMIZE = "optimize"  # تحسين التعبير


class SymbolicMergeMethod(str, Enum):
    """طرق دمج التعبيرات الرمزية."""
    ADAPTIVE = "adaptive"  # دمج تكيفي
    WEIGHTED = "weighted"  # دمج موزون
    CROSSOVER = "crossover"  # تقاطع
    SEMANTIC = "semantic"  # دمج دلالي
    STRUCTURAL = "structural"  # دمج هيكلي


@dataclass
class SymbolicMetadata:
    """البيانات الوصفية للتعبير الرمزي."""
    expression_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    creation_time: str = field(default_factory=lambda: datetime.now().isoformat())
    last_modified: str = field(default_factory=lambda: datetime.now().isoformat())
    version: int = 1
    complexity: float = 0.0
    semantic_tags: List[str] = field(default_factory=list)
    evolution_history: List[Dict[str, Any]] = field(default_factory=list)
    parent_ids: List[str] = field(default_factory=list)
    custom_properties: Dict[str, Any] = field(default_factory=dict)


class AdvancedSymbolicExpression:
    """تعبير رمزي متقدم مع قدرات تطور ذاتي."""
    
    def __init__(self, expression_str=None, sympy_obj=None, variables=None, metadata=None):
        """
        تهيئة تعبير رمزي متقدم.
        
        Args:
            expression_str: سلسلة التعبير الرمزي
            sympy_obj: كائن SymPy
            variables: قاموس المتغيرات
            metadata: البيانات الوصفية
        """
        if expression_str is None and sympy_obj is None:
            raise ValueError("يجب توفير إما expression_str أو sympy_obj")
        
        self.variables = variables or {}
        
        if sympy_obj is not None:
            self.sympy_expr = sympy_obj
            self.expression_str = str(sympy_obj)
        else:
            try:
                # تحليل سلسلة التعبير
                self.sympy_expr = sp.sympify(expression_str)
                self.expression_str = expression_str
                
                # استخراج المتغيرات تلقائيًا
                free_symbols = self.sympy_expr.free_symbols
                for symbol in free_symbols:
                    var_name = str(symbol)
                    if var_name not in self.variables:
                        self.variables[var_name] = symbol
                
            except Exception as e:
                raise ValueError(f"لا يمكن تحليل التعبير '{expression_str}': {e}")
        
        # تهيئة البيانات الوصفية
        self.metadata = metadata or SymbolicMetadata()
        
        # حساب التعقيد الأولي
        self._update_complexity()
        
        logger.info(f"تم إنشاء تعبير رمزي متقدم: {self.metadata.expression_id}")
    
    def _update_complexity(self):
        """تحديث درجة تعقيد التعبير."""
        try:
            # عد العمليات والمتغيرات والثوابت
            expr_str = str(self.sympy_expr)
            operations = expr_str.count('+') + expr_str.count('-') + expr_str.count('*') + expr_str.count('/') + expr_str.count('**')
            variables_count = len(self.variables)
            constants_count = len([atom for atom in self.sympy_expr.atoms() if atom.is_number])
            
            # حساب درجة التعقيد
            complexity = (operations * 0.5) + (variables_count * 0.3) + (constants_count * 0.1)
            self.metadata.complexity = max(complexity, 0.1)  # الحد الأدنى للتعقيد
        except Exception as e:
            logger.warning(f"فشل في حساب درجة التعقيد: {str(e)}")
            self.metadata.complexity = len(self.expression_str) / 10.0
    
    def to_string(self):
        """إرجاع تمثيل نصي للتعبير."""
        return self.expression_str
    
    def evaluate(self, assignments):
        """
        تقييم التعبير باستخدام قيم المتغيرات المعطاة.
        
        Args:
            assignments: قاموس يربط أسماء المتغيرات بقيمها
            
        Returns:
            نتيجة التقييم
        """
        try:
            # إنشاء قاموس التعويض
            subs_dict = {}
            for var_name, value in assignments.items():
                if var_name in self.variables:
                    subs_dict[self.variables[var_name]] = value
            
            # التعويض والتقييم
            result = float(self.sympy_expr.subs(subs_dict).evalf())
            return result
        except Exception as e:
            logger.error(f"خطأ في التقييم: {str(e)}")
            return None
    
    def evolve(self, direction=SymbolicEvolutionDirection.SIMPLIFY, strength=0.5, constraints=None):
        """
        تطوير التعبير في اتجاه معين مع الحفاظ على القيود.
        
        Args:
            direction: اتجاه التطور
            strength: قوة التطور (0.0 إلى 1.0)
            constraints: قيود التطور
            
        Returns:
            تعبير رمزي متطور
        """
        constraints = constraints or {}
        
        # نسخ البيانات الوصفية وتحديثها
        new_metadata = copy.deepcopy(self.metadata)
        new_metadata.version += 1
        new_metadata.last_modified = datetime.now().isoformat()
        new_metadata.parent_ids.append(self.metadata.expression_id)
        
        # تسجيل عملية التطور
        evolution_record = {
            "direction": direction if isinstance(direction, str) else direction.value,
            "strength": strength,
            "timestamp": datetime.now().isoformat(),
            "parent_id": self.metadata.expression_id
        }
        new_metadata.evolution_history.append(evolution_record)
        
        # تنفيذ التطور حسب الاتجاه
        if direction == SymbolicEvolutionDirection.SIMPLIFY:
            new_expr = self._evolve_simplify(strength, constraints)
        elif direction == SymbolicEvolutionDirection.EXPAND:
            new_expr = self._evolve_expand(strength, constraints)
        elif direction == SymbolicEvolutionDirection.FACTORIZE:
            new_expr = self._evolve_factorize(strength, constraints)
        elif direction == SymbolicEvolutionDirection.GENERALIZE:
            new_expr = self._evolve_generalize(strength, constraints)
        elif direction == SymbolicEvolutionDirection.SPECIALIZE:
            new_expr = self._evolve_specialize(strength, constraints)
        elif direction == SymbolicEvolutionDirection.TRANSFORM:
            new_expr = self._evolve_transform(strength, constraints)
        elif direction == SymbolicEvolutionDirection.MUTATE:
            new_expr = self._evolve_mutate(strength, constraints)
        elif direction == SymbolicEvolutionDirection.OPTIMIZE:
            new_expr = self._evolve_optimize(strength, constraints)
        else:
            raise ValueError(f"اتجاه تطور غير معروف: {direction}")
        
        # إنشاء تعبير رمزي متقدم جديد
        return AdvancedSymbolicExpression(
            sympy_obj=new_expr,
            variables=self.variables.copy(),
            metadata=new_metadata
        )
    
    def _evolve_simplify(self, strength, constraints):
        """تطوير التعبير عن طريق التبسيط."""
        try:
            # تبسيط التعبير
            simplified = sp.simplify(self.sympy_expr)
            
            # إذا كانت قوة التطور أقل من 1.0، نقوم بدمج التعبير الأصلي مع التعبير المبسط
            if strength < 1.0:
                # استخدام التعبير الأصلي بنسبة (1 - strength) والتعبير المبسط بنسبة strength
                result = (1 - strength) * self.sympy_expr + strength * simplified
                return result
            else:
                return simplified
        except Exception as e:
            logger.warning(f"فشل في تبسيط التعبير: {str(e)}")
            return self.sympy_expr
    
    def _evolve_expand(self, strength, constraints):
        """تطوير التعبير عن طريق التوسيع."""
        try:
            # توسيع التعبير
            expanded = sp.expand(self.sympy_expr)
            
            # إذا كانت قوة التطور أقل من 1.0، نقوم بدمج التعبير الأصلي مع التعبير الموسع
            if strength < 1.0:
                # استخدام التعبير الأصلي بنسبة (1 - strength) والتعبير الموسع بنسبة strength
                result = (1 - strength) * self.sympy_expr + strength * expanded
                return result
            else:
                return expanded
        except Exception as e:
            logger.warning(f"فشل في توسيع التعبير: {str(e)}")
            return self.sympy_expr
    
    def _evolve_factorize(self, strength, constraints):
        """تطوير التعبير عن طريق التحليل إلى عوامل."""
        try:
            # تحليل التعبير إلى عوامل
            factorized = sp.factor(self.sympy_expr)
            
            # إذا كانت قوة التطور أقل من 1.0، نقوم بدمج التعبير الأصلي مع التعبير المحلل
            if strength < 1.0:
                # استخدام التعبير الأصلي بنسبة (1 - strength) والتعبير المحلل بنسبة strength
                result = (1 - strength) * self.sympy_expr + strength * factorized
                return result
            else:
                return factorized
        except Exception as e:
            logger.warning(f"فشل في تحليل التعبير إلى عوامل: {str(e)}")
            return self.sympy_expr
    
    def _evolve_generalize(self, strength, constraints):
        """تطوير التعبير عن طريق التعميم."""
        try:
            # استخراج المتغيرات والثوابت
            variables = list(self.variables.values())
            constants = [atom for atom in self.sympy_expr.atoms() if atom.is_number]
            
            # إذا لم تكن هناك ثوابت، لا يمكن التعميم
            if not constants:
                return self.sympy_expr
            
            # اختيار بعض الثوابت للتعميم
            num_constants_to_generalize = max(1, int(len(constants) * strength))
            constants_to_generalize = random.sample(constants, min(num_constants_to_generalize, len(constants)))
            
            # إنشاء متغيرات جديدة للثوابت المختارة
            new_expr = self.sympy_expr
            new_variables = self.variables.copy()
            
            for i, constant in enumerate(constants_to_generalize):
                # إنشاء اسم متغير جديد
                var_name = f"c{i+1}"
                while var_name in new_variables:
                    var_name = f"c{random.randint(1, 100)}"
                
                # إنشاء متغير جديد
                new_var = sp.Symbol(var_name)
                new_variables[var_name] = new_var
                
                # استبدال الثابت بالمتغير الجديد
                new_expr = new_expr.subs(constant, new_var)
            
            return new_expr
        except Exception as e:
            logger.warning(f"فشل في تعميم التعبير: {str(e)}")
            return self.sympy_expr
    
    def _evolve_specialize(self, strength, constraints):
        """تطوير التعبير عن طريق التخصيص."""
        try:
            # استخراج المتغيرات
            variables = list(self.variables.values())
            
            # إذا لم تكن هناك متغيرات، لا يمكن التخصيص
            if not variables:
                return self.sympy_expr
            
            # اختيار بعض المتغيرات للتخصيص
            num_vars_to_specialize = max(1, int(len(variables) * strength))
            vars_to_specialize = random.sample(variables, min(num_vars_to_specialize, len(variables)))
            
            # تخصيص قيم للمتغيرات المختارة
            new_expr = self.sympy_expr
            for var in vars_to_specialize:
                # اختيار قيمة عشوائية
                value = random.uniform(-10, 10)
                
                # استبدال المتغير بالقيمة
                new_expr = new_expr.subs(var, value)
            
            return new_expr
        except Exception as e:
            logger.warning(f"فشل في تخصيص التعبير: {str(e)}")
            return self.sympy_expr
    
    def _evolve_transform(self, strength, constraints):
        """تطوير التعبير عن طريق التحويل."""
        try:
            # اختيار تحويل عشوائي
            transformations = [
                lambda expr: sp.trigsimp(expr),  # تبسيط التعبيرات المثلثية
                lambda expr: sp.powsimp(expr),   # تبسيط الأسس
                lambda expr: sp.logcombine(expr), # دمج اللوغاريتمات
                lambda expr: sp.expand_log(expr), # توسيع اللوغاريتمات
                lambda expr: sp.expand_trig(expr) # توسيع الدوال المثلثية
            ]
            
            # اختيار تحويل عشوائي
            transform = random.choice(transformations)
            
            # تطبيق التحويل
            transformed = transform(self.sympy_expr)
            
            # إذا كانت قوة التطور أقل من 1.0، نقوم بدمج التعبير الأصلي مع التعبير المحول
            if strength < 1.0:
                # استخدام التعبير الأصلي بنسبة (1 - strength) والتعبير المحول بنسبة strength
                result = (1 - strength) * self.sympy_expr + strength * transformed
                return result
            else:
                return transformed
        except Exception as e:
            logger.warning(f"فشل في تحويل التعبير: {str(e)}")
            return self.sympy_expr
    
    def _evolve_mutate(self, strength, constraints):
        """تطوير التعبير عن طريق التغيير العشوائي."""
        try:
            # استخراج المتغيرات والعمليات
            variables = list(self.variables.values())
            
            # إذا لم تكن هناك متغيرات، لا يمكن التغيير
            if not variables:
                return self.sympy_expr
            
            # اختيار عملية عشوائية
            operations = [
                lambda x, y: x + y,  # جمع
                lambda x, y: x - y,  # طرح
                lambda x, y: x * y,  # ضرب
                lambda x, y: x / y,  # قسمة
                lambda x, y: x ** y  # أس
            ]
            
            # اختيار متغير عشوائي وعملية عشوائية
            var = random.choice(variables)
            op = random.choice(operations)
            
            # اختيار قيمة عشوائية
            value = random.uniform(-5, 5)
            
            # تطبيق العملية
            mutation = op(var, value)
            
            # استبدال المتغير بالتغيير
            new_expr = self.sympy_expr.subs(var, mutation)
            
            # إذا كانت قوة التطور أقل من 1.0، نقوم بدمج التعبير الأصلي مع التعبير المتغير
            if strength < 1.0:
                # استخدام التعبير الأصلي بنسبة (1 - strength) والتعبير المتغير بنسبة strength
                result = (1 - strength) * self.sympy_expr + strength * new_expr
                return result
            else:
                return new_expr
        except Exception as e:
            logger.warning(f"فشل في تغيير التعبير: {str(e)}")
            return self.sympy_expr
    
    def _evolve_optimize(self, strength, constraints):
        """تطوير التعبير عن طريق التحسين."""
        try:
            # تبسيط التعبير أولاً
            optimized = sp.simplify(self.sympy_expr)
            
            # ثم تحليله إلى عوامل
            optimized = sp.factor(optimized)
            
            # ثم تبسيط الأسس
            optimized = sp.powsimp(optimized)
            
            # إذا كانت قوة التطور أقل من 1.0، نقوم بدمج التعبير الأصلي مع التعبير المحسن
            if strength < 1.0:
                # استخدام التعبير الأصلي بنسبة (1 - strength) والتعبير المحسن بنسبة strength
                result = (1 - strength) * self.sympy_expr + strength * optimized
                return result
            else:
                return optimized
        except Exception as e:
            logger.warning(f"فشل في تحسين التعبير: {str(e)}")
            return self.sympy_expr
    
    def merge_with(self, other_expression, method=SymbolicMergeMethod.ADAPTIVE, weight=0.5):
        """
        دمج هذا التعبير مع تعبير آخر باستخدام طريقة محددة.
        
        Args:
            other_expression: التعبير الآخر للدمج
            method: طريقة الدمج
            weight: وزن هذا التعبير في الدمج (0.0 إلى 1.0)
            
        Returns:
            تعبير رمزي مدمج
        """
        if not isinstance(other_expression, AdvancedSymbolicExpression):
            raise TypeError("يجب أن يكون التعبير الآخر من نوع AdvancedSymbolicExpression")
        
        # نسخ البيانات الوصفية وتحديثها
        new_metadata = copy.deepcopy(self.metadata)
        new_metadata.version += 1
        new_metadata.last_modified = datetime.now().isoformat()
        new_metadata.parent_ids.extend([self.metadata.expression_id, other_expression.metadata.expression_id])
        
        # تسجيل عملية الدمج
        merge_record = {
            "method": method if isinstance(method, str) else method.value,
            "weight": weight,
            "timestamp": datetime.now().isoformat(),
            "parent_ids": [self.metadata.expression_id, other_expression.metadata.expression_id]
        }
        new_metadata.evolution_history.append(merge_record)
        
        # دمج الوسوم الدلالية
        new_metadata.semantic_tags = list(set(self.metadata.semantic_tags + other_expression.metadata.semantic_tags))
        
        # تنفيذ الدمج حسب الطريقة
        if method == SymbolicMergeMethod.ADAPTIVE:
            new_expr = self._merge_adaptive(other_expression, weight)
        elif method == SymbolicMergeMethod.WEIGHTED:
            new_expr = self._merge_weighted(other_expression, weight)
        elif method == SymbolicMergeMethod.CROSSOVER:
            new_expr = self._merge_crossover(other_expression, weight)
        elif method == SymbolicMergeMethod.SEMANTIC:
            new_expr = self._merge_semantic(other_expression, weight)
        elif method == SymbolicMergeMethod.STRUCTURAL:
            new_expr = self._merge_structural(other_expression, weight)
        else:
            raise ValueError(f"طريقة دمج غير معروفة: {method}")
        
        # دمج المتغيرات
        new_variables = self.variables.copy()
        for var_name, var_symbol in other_expression.variables.items():
            if var_name not in new_variables:
                new_variables[var_name] = var_symbol
        
        # إنشاء تعبير رمزي متقدم جديد
        return AdvancedSymbolicExpression(
            sympy_obj=new_expr,
            variables=new_variables,
            metadata=new_metadata
        )
    
    def _merge_adaptive(self, other_expression, weight):
        """دمج تكيفي مع تعبير آخر."""
        try:
            # حساب تعقيد كل تعبير
            self_complexity = self.metadata.complexity
            other_complexity = other_expression.metadata.complexity
            
            # تعديل الوزن بناءً على التعقيد
            total_complexity = self_complexity + other_complexity
            if total_complexity > 0:
                adaptive_weight = (1 - weight) * (self_complexity / total_complexity) + weight * (other_complexity / total_complexity)
            else:
                adaptive_weight = 0.5
            
            # دمج التعبيرين
            return adaptive_weight * self.sympy_expr + (1 - adaptive_weight) * other_expression.sympy_expr
        except Exception as e:
            logger.warning(f"فشل في الدمج التكيفي: {str(e)}")
            return self.sympy_expr
    
    def _merge_weighted(self, other_expression, weight):
        """دمج موزون مع تعبير آخر."""
        try:
            # دمج التعبيرين بالوزن المحدد
            return weight * self.sympy_expr + (1 - weight) * other_expression.sympy_expr
        except Exception as e:
            logger.warning(f"فشل في الدمج الموزون: {str(e)}")
            return self.sympy_expr
    
    def _merge_crossover(self, other_expression, weight):
        """دمج بالتقاطع مع تعبير آخر."""
        try:
            # تحويل التعبيرين إلى سلاسل
            self_str = str(self.sympy_expr)
            other_str = str(other_expression.sympy_expr)
            
            # اختيار نقطة تقاطع
            crossover_point = int(len(self_str) * weight)
            
            # إنشاء سلسلة جديدة
            new_str = self_str[:crossover_point] + other_str[crossover_point:]
            
            # تحويل السلسلة إلى تعبير
            try:
                new_expr = sp.sympify(new_str)
                return new_expr
            except:
                # إذا فشل التحويل، نستخدم الدمج الموزون
                return self._merge_weighted(other_expression, weight)
        except Exception as e:
            logger.warning(f"فشل في الدمج بالتقاطع: {str(e)}")
            return self.sympy_expr
    
    def _merge_semantic(self, other_expression, weight):
        """دمج دلالي مع تعبير آخر."""
        try:
            # في هذه النسخة البسيطة، نستخدم الدمج الموزون
            # في النسخة المتقدمة، يمكن استخدام معلومات دلالية لتوجيه الدمج
            return self._merge_weighted(other_expression, weight)
        except Exception as e:
            logger.warning(f"فشل في الدمج الدلالي: {str(e)}")
            return self.sympy_expr
    
    def _merge_structural(self, other_expression, weight):
        """دمج هيكلي مع تعبير آخر."""
        try:
            # في هذه النسخة البسيطة، نستخدم الدمج الموزون
            # في النسخة المتقدمة، يمكن تحليل هيكل التعبيرين ودمجهما بطريقة أكثر تعقيدًا
            return self._merge_weighted(other_expression, weight)
        except Exception as e:
            logger.warning(f"فشل في الدمج الهيكلي: {str(e)}")
            return self.sympy_expr
    
    def extract_patterns(self):
        """
        استخراج الأنماط الهيكلية من التعبير.
        
        Returns:
            قاموس يحتوي على الأنماط المستخرجة
        """
        patterns = {}
        
        try:
            # استخراج العمليات
            operations = {
                'addition': [],
                'subtraction': [],
                'multiplication': [],
                'division': [],
                'power': []
            }
            
            # تحليل التعبير لاستخراج العمليات
            expr_str = str(self.sympy_expr)
            
            # استخراج الجمع
            for term in self.sympy_expr.as_ordered_terms():
                operations['addition'].append(str(term))
            
            # استخراج الضرب
            for factor in self.sympy_expr.as_ordered_factors():
                operations['multiplication'].append(str(factor))
            
            # استخراج الأنماط المتكررة
            repeated_patterns = []
            terms = [str(term) for term in self.sympy_expr.as_ordered_terms()]
            for i in range(len(terms)):
                for j in range(i+1, len(terms)):
                    if terms[i] == terms[j]:
                        repeated_patterns.append(terms[i])
            
            # استخراج الأنماط الهيكلية
            structural_patterns = []
            
            # إضافة الأنماط إلى القاموس
            patterns['operations'] = operations
            patterns['repeated_patterns'] = repeated_patterns
            patterns['structural_patterns'] = structural_patterns
            
            return patterns
        except Exception as e:
            logger.warning(f"فشل في استخراج الأنماط: {str(e)}")
            return patterns
    
    def to_semantic_representation(self):
        """
        تحويل التعبير إلى تمثيل دلالي.
        
        Returns:
            قاموس يحتوي على التمثيل الدلالي
        """
        semantic_representation = {}
        
        try:
            # استخراج المتغيرات
            variables = list(self.variables.keys())
            semantic_representation['variables'] = variables
            
            # استخراج العمليات
            operations = []
            expr_str = str(self.sympy_expr)
            if '+' in expr_str:
                operations.append('addition')
            if '-' in expr_str:
                operations.append('subtraction')
            if '*' in expr_str:
                operations.append('multiplication')
            if '/' in expr_str:
                operations.append('division')
            if '**' in expr_str:
                operations.append('power')
            semantic_representation['operations'] = operations
            
            # استخراج الدوال
            functions = []
            if 'sin' in expr_str:
                functions.append('sine')
            if 'cos' in expr_str:
                functions.append('cosine')
            if 'tan' in expr_str:
                functions.append('tangent')
            if 'exp' in expr_str:
                functions.append('exponential')
            if 'log' in expr_str:
                functions.append('logarithm')
            semantic_representation['functions'] = functions
            
            # استخراج التعقيد
            semantic_representation['complexity'] = self.metadata.complexity
            
            # استخراج الوسوم الدلالية
            semantic_representation['semantic_tags'] = self.metadata.semantic_tags
            
            return semantic_representation
        except Exception as e:
            logger.warning(f"فشل في التحويل إلى تمثيل دلالي: {str(e)}")
            return semantic_representation
    
    def simplify(self):
        """
        تبسيط التعبير.
        
        Returns:
            تعبير رمزي مبسط
        """
        return self.evolve(direction=SymbolicEvolutionDirection.SIMPLIFY, strength=1.0)
    
    def expand(self):
        """
        توسيع التعبير.
        
        Returns:
            تعبير رمزي موسع
        """
        return self.evolve(direction=SymbolicEvolutionDirection.EXPAND, strength=1.0)
    
    def factorize(self):
        """
        تحليل التعبير إلى عوامل.
        
        Returns:
            تعبير رمزي محلل إلى عوامل
        """
        return self.evolve(direction=SymbolicEvolutionDirection.FACTORIZE, strength=1.0)
    
    def optimize(self):
        """
        تحسين التعبير.
        
        Returns:
            تعبير رمزي محسن
        """
        return self.evolve(direction=SymbolicEvolutionDirection.OPTIMIZE, strength=1.0)
    
    def mutate(self, strength=0.5):
        """
        تغيير التعبير عشوائياً.
        
        Args:
            strength: قوة التغيير (0.0 إلى 1.0)
            
        Returns:
            تعبير رمزي متغير
        """
        return self.evolve(direction=SymbolicEvolutionDirection.MUTATE, strength=strength)
    
    def to_dict(self):
        """
        تحويل التعبير إلى قاموس.
        
        Returns:
            قاموس يمثل التعبير
        """
        return {
            'expression_str': self.expression_str,
            'variables': {var_name: str(var_symbol) for var_name, var_symbol in self.variables.items()},
            'metadata': {
                'expression_id': self.metadata.expression_id,
                'creation_time': self.metadata.creation_time,
                'last_modified': self.metadata.last_modified,
                'version': self.metadata.version,
                'complexity': self.metadata.complexity,
                'semantic_tags': self.metadata.semantic_tags,
                'evolution_history': self.metadata.evolution_history,
                'parent_ids': self.metadata.parent_ids,
                'custom_properties': self.metadata.custom_properties
            }
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        إنشاء تعبير رمزي من قاموس.
        
        Args:
            data: قاموس يمثل التعبير
            
        Returns:
            تعبير رمزي متقدم
        """
        # استخراج البيانات
        expression_str = data['expression_str']
        variables_data = data['variables']
        metadata_data = data['metadata']
        
        # إنشاء المتغيرات
        variables = {}
        for var_name, var_str in variables_data.items():
            variables[var_name] = sp.Symbol(var_name)
        
        # إنشاء البيانات الوصفية
        metadata = SymbolicMetadata(
            expression_id=metadata_data['expression_id'],
            creation_time=metadata_data['creation_time'],
            last_modified=metadata_data['last_modified'],
            version=metadata_data['version'],
            complexity=metadata_data['complexity'],
            semantic_tags=metadata_data['semantic_tags'],
            evolution_history=metadata_data['evolution_history'],
            parent_ids=metadata_data['parent_ids'],
            custom_properties=metadata_data['custom_properties']
        )
        
        # إنشاء التعبير
        return cls(
            expression_str=expression_str,
            variables=variables,
            metadata=metadata
        )


class SymbolicExpressionFactory:
    """مصنع التعبيرات الرمزية المتقدمة."""
    
    @staticmethod
    def create_constant(value):
        """
        إنشاء تعبير رمزي ثابت.
        
        Args:
            value: قيمة الثابت
            
        Returns:
            تعبير رمزي متقدم
        """
        return AdvancedSymbolicExpression(expression_str=str(value))
    
    @staticmethod
    def create_variable(name):
        """
        إنشاء تعبير رمزي متغير.
        
        Args:
            name: اسم المتغير
            
        Returns:
            تعبير رمزي متقدم
        """
        return AdvancedSymbolicExpression(expression_str=name)
    
    @staticmethod
    def create_polynomial(variable, degree, coefficients=None):
        """
        إنشاء تعبير رمزي متعدد حدود.
        
        Args:
            variable: اسم المتغير
            degree: درجة متعدد الحدود
            coefficients: معاملات متعدد الحدود (اختياري)
            
        Returns:
            تعبير رمزي متقدم
        """
        if coefficients is None:
            # إنشاء معاملات عشوائية
            coefficients = [random.uniform(-10, 10) for _ in range(degree + 1)]
        
        # إنشاء متعدد الحدود
        x = sp.Symbol(variable)
        polynomial = sum(coef * x ** i for i, coef in enumerate(coefficients))
        
        return AdvancedSymbolicExpression(sympy_obj=polynomial)
    
    @staticmethod
    def create_trigonometric(variable, function_type='sin', amplitude=1.0, frequency=1.0, phase=0.0):
        """
        إنشاء تعبير رمزي مثلثي.
        
        Args:
            variable: اسم المتغير
            function_type: نوع الدالة المثلثية ('sin', 'cos', 'tan')
            amplitude: السعة
            frequency: التردد
            phase: الطور
            
        Returns:
            تعبير رمزي متقدم
        """
        x = sp.Symbol(variable)
        
        if function_type == 'sin':
            expr = amplitude * sp.sin(frequency * x + phase)
        elif function_type == 'cos':
            expr = amplitude * sp.cos(frequency * x + phase)
        elif function_type == 'tan':
            expr = amplitude * sp.tan(frequency * x + phase)
        else:
            raise ValueError(f"نوع دالة مثلثية غير معروف: {function_type}")
        
        return AdvancedSymbolicExpression(sympy_obj=expr)
    
    @staticmethod
    def create_exponential(variable, base=sp.E, coefficient=1.0):
        """
        إنشاء تعبير رمزي أسي.
        
        Args:
            variable: اسم المتغير
            base: الأساس
            coefficient: المعامل
            
        Returns:
            تعبير رمزي متقدم
        """
        x = sp.Symbol(variable)
        expr = coefficient * base ** x
        
        return AdvancedSymbolicExpression(sympy_obj=expr)
    
    @staticmethod
    def create_logarithmic(variable, base=sp.E, coefficient=1.0):
        """
        إنشاء تعبير رمزي لوغاريتمي.
        
        Args:
            variable: اسم المتغير
            base: الأساس
            coefficient: المعامل
            
        Returns:
            تعبير رمزي متقدم
        """
        x = sp.Symbol(variable)
        
        if base == sp.E:
            expr = coefficient * sp.log(x)
        else:
            expr = coefficient * sp.log(x, base)
        
        return AdvancedSymbolicExpression(sympy_obj=expr)
    
    @staticmethod
    def create_random_expression(variables=None, complexity=0.5, include_functions=True):
        """
        إنشاء تعبير رمزي عشوائي.
        
        Args:
            variables: قائمة أسماء المتغيرات
            complexity: درجة التعقيد (0.0 إلى 1.0)
            include_functions: تضمين الدوال
            
        Returns:
            تعبير رمزي متقدم
        """
        if variables is None:
            variables = ['x', 'y', 'z']
        
        # إنشاء رموز للمتغيرات
        symbols = {var: sp.Symbol(var) for var in variables}
        
        # تحديد عدد العمليات بناءً على التعقيد
        num_operations = max(1, int(10 * complexity))
        
        # إنشاء تعبير أولي
        expr = random.choice(list(symbols.values()))
        
        # إضافة عمليات عشوائية
        for _ in range(num_operations):
            # اختيار عملية عشوائية
            operation = random.choice(['+', '-', '*', '/', '**'])
            
            # اختيار متغير عشوائي أو ثابت
            if random.random() < 0.7:  # 70% احتمال اختيار متغير
                operand = random.choice(list(symbols.values()))
            else:  # 30% احتمال اختيار ثابت
                operand = random.uniform(-5, 5)
            
            # تطبيق العملية
            if operation == '+':
                expr = expr + operand
            elif operation == '-':
                expr = expr - operand
            elif operation == '*':
                expr = expr * operand
            elif operation == '/':
                # تجنب القسمة على صفر
                if isinstance(operand, float) and abs(operand) < 0.1:
                    operand = 1.0
                expr = expr / operand
            elif operation == '**':
                # تقييد الأس لتجنب التعقيد الزائد
                if isinstance(operand, float):
                    operand = max(-3, min(3, operand))
                expr = expr ** operand
        
        # إضافة دوال إذا كان مطلوبًا
        if include_functions and complexity > 0.3:
            # اختيار دالة عشوائية
            function = random.choice(['sin', 'cos', 'exp', 'log'])
            
            if function == 'sin':
                expr = sp.sin(expr)
            elif function == 'cos':
                expr = sp.cos(expr)
            elif function == 'exp':
                expr = sp.exp(expr)
            elif function == 'log':
                # تجنب اللوغاريتم السالب
                expr = sp.log(sp.Abs(expr))
        
        return AdvancedSymbolicExpression(sympy_obj=expr)


# اختبار الوحدة
if __name__ == "__main__":
    # إنشاء تعبير رمزي بسيط
    expr1 = AdvancedSymbolicExpression(expression_str="x**2 + 2*x + 1")
    print(f"التعبير الأصلي: {expr1.to_string()}")
    
    # تبسيط التعبير
    expr2 = expr1.simplify()
    print(f"التعبير المبسط: {expr2.to_string()}")
    
    # تطوير التعبير
    expr3 = expr1.evolve(direction=SymbolicEvolutionDirection.EXPAND, strength=0.8)
    print(f"التعبير المتطور: {expr3.to_string()}")
    
    # دمج تعبيرين
    expr4 = AdvancedSymbolicExpression(expression_str="x**2 - 1")
    expr5 = expr1.merge_with(expr4, method=SymbolicMergeMethod.WEIGHTED, weight=0.7)
    print(f"التعبير المدمج: {expr5.to_string()}")
    
    # إنشاء تعبير عشوائي
    expr6 = SymbolicExpressionFactory.create_random_expression(variables=['x', 'y'], complexity=0.7)
    print(f"التعبير العشوائي: {expr6.to_string()}")
