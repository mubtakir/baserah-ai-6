#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
محرك المعالجة الرمزية المتقدم لنظام بصيرة

هذا الملف يحتوي على تعريف فئة AdvancedSymbolicExpression التي توفر
قدرات معالجة رمزية متقدمة مع آليات تطور ذاتي للتعبيرات الرمزية.

المؤلف: فريق تطوير نظام بصيرة
الإصدار: 1.0.0
التاريخ: 2 يونيو 2025
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
import json

# إعداد التسجيل
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("symbolic_engine")


class SymbolicMetadata:
    """
    فئة البيانات الوصفية للتعبيرات الرمزية.
    """
    
    def __init__(self):
        """تهيئة البيانات الوصفية."""
        self.equation_id = str(uuid.uuid4())
        self.creation_date = datetime.now().isoformat()
        self.last_modified = self.creation_date
        self.version = "1.0.0"
        self.is_revolutionary = False
        self.semantic_tags = []
        self.domains = []
        self.operations = []
        self.complexity = 0.0
        self.properties = {}
    
    def to_dict(self) -> Dict[str, Any]:
        """
        تحويل البيانات الوصفية إلى قاموس.
        
        Returns:
            قاموس يمثل البيانات الوصفية
        """
        return {
            "equation_id": self.equation_id,
            "creation_date": self.creation_date,
            "last_modified": self.last_modified,
            "version": self.version,
            "is_revolutionary": self.is_revolutionary,
            "semantic_tags": self.semantic_tags,
            "domains": self.domains,
            "operations": self.operations,
            "complexity": self.complexity,
            "properties": self.properties
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SymbolicMetadata':
        """
        إنشاء بيانات وصفية من قاموس.
        
        Args:
            data: قاموس يمثل البيانات الوصفية
            
        Returns:
            كائن البيانات الوصفية
        """
        metadata = cls()
        
        metadata.equation_id = data.get("equation_id", str(uuid.uuid4()))
        metadata.creation_date = data.get("creation_date", datetime.now().isoformat())
        metadata.last_modified = data.get("last_modified", datetime.now().isoformat())
        metadata.version = data.get("version", "1.0.0")
        metadata.is_revolutionary = data.get("is_revolutionary", False)
        metadata.semantic_tags = data.get("semantic_tags", [])
        metadata.domains = data.get("domains", [])
        metadata.operations = data.get("operations", [])
        metadata.complexity = data.get("complexity", 0.0)
        metadata.properties = data.get("properties", {})
        
        return metadata


class AdvancedSymbolicExpression:
    """
    فئة التعبيرات الرمزية المتقدمة مع قدرات تطور ذاتي.
    """
    
    def __init__(self, expression_str: Optional[str] = None, expression_obj: Optional[sp.Expr] = None):
        """
        تهيئة التعبير الرمزي.
        
        Args:
            expression_str: سلسلة نصية تمثل التعبير الرمزي
            expression_obj: كائن SymPy يمثل التعبير الرمزي
        """
        self.metadata = SymbolicMetadata()
        self.variables = set()
        
        if expression_str is not None:
            self._init_from_string(expression_str)
        elif expression_obj is not None:
            self._init_from_object(expression_obj)
        else:
            # إنشاء تعبير افتراضي
            x = sp.Symbol('x')
            self.expression = x
            self.variables = {x}
            self.metadata.operations = []
            self.metadata.complexity = 1.0
    
    def _init_from_string(self, expression_str: str):
        """
        تهيئة التعبير الرمزي من سلسلة نصية.
        
        Args:
            expression_str: سلسلة نصية تمثل التعبير الرمزي
        """
        try:
            # تحليل التعبير
            self.expression = sp.sympify(expression_str)
            
            # استخراج المتغيرات
            self.variables = set(self.expression.free_symbols)
            
            # استخراج العمليات
            self.metadata.operations = self._extract_operations(self.expression)
            
            # حساب التعقيد
            self.metadata.complexity = self._calculate_complexity(self.expression)
            
        except Exception as e:
            logger.error(f"خطأ في تحليل التعبير: {str(e)}")
            # إنشاء تعبير افتراضي
            x = sp.Symbol('x')
            self.expression = x
            self.variables = {x}
            self.metadata.operations = []
            self.metadata.complexity = 1.0
    
    def _init_from_object(self, expression_obj: sp.Expr):
        """
        تهيئة التعبير الرمزي من كائن SymPy.
        
        Args:
            expression_obj: كائن SymPy يمثل التعبير الرمزي
        """
        self.expression = expression_obj
        
        # استخراج المتغيرات
        self.variables = set(self.expression.free_symbols)
        
        # استخراج العمليات
        self.metadata.operations = self._extract_operations(self.expression)
        
        # حساب التعقيد
        self.metadata.complexity = self._calculate_complexity(self.expression)
    
    def _extract_operations(self, expr: sp.Expr) -> List[str]:
        """
        استخراج العمليات من التعبير الرمزي.
        
        Args:
            expr: التعبير الرمزي
            
        Returns:
            قائمة بالعمليات
        """
        operations = set()
        
        # تحديد نوع التعبير
        if isinstance(expr, sp.Add):
            operations.add("add")
        elif isinstance(expr, sp.Mul):
            operations.add("multiply")
        elif isinstance(expr, sp.Pow):
            operations.add("power")
        elif isinstance(expr, sp.sin):
            operations.add("sin")
        elif isinstance(expr, sp.cos):
            operations.add("cos")
        elif isinstance(expr, sp.tan):
            operations.add("tan")
        elif isinstance(expr, sp.exp):
            operations.add("exp")
        elif isinstance(expr, sp.log):
            operations.add("log")
        
        # استخراج العمليات من التعبيرات الفرعية
        for arg in expr.args:
            operations.update(self._extract_operations(arg))
        
        return list(operations)
    
    def _calculate_complexity(self, expr: sp.Expr) -> float:
        """
        حساب تعقيد التعبير الرمزي.
        
        Args:
            expr: التعبير الرمزي
            
        Returns:
            درجة التعقيد
        """
        # عدد العمليات
        operation_count = len(self._extract_operations(expr))
        
        # عدد المتغيرات
        variable_count = len(expr.free_symbols)
        
        # عمق التعبير
        depth = self._calculate_depth(expr)
        
        # حساب التعقيد
        complexity = 0.3 * operation_count + 0.2 * variable_count + 0.5 * depth
        
        return complexity
    
    def _calculate_depth(self, expr: sp.Expr, current_depth: int = 1) -> int:
        """
        حساب عمق التعبير الرمزي.
        
        Args:
            expr: التعبير الرمزي
            current_depth: العمق الحالي
            
        Returns:
            عمق التعبير
        """
        if len(expr.args) == 0:
            return current_depth
        
        depths = [self._calculate_depth(arg, current_depth + 1) for arg in expr.args]
        
        return max(depths)
    
    def evaluate(self, variable_values: Dict[str, float]) -> float:
        """
        تقييم التعبير الرمزي باستخدام قيم المتغيرات.
        
        Args:
            variable_values: قاموس يحتوي على قيم المتغيرات
            
        Returns:
            نتيجة التقييم
        """
        # تحويل أسماء المتغيرات إلى كائنات Symbol
        symbol_values = {}
        
        for var_name, value in variable_values.items():
            symbol = sp.Symbol(var_name)
            symbol_values[symbol] = value
        
        # تقييم التعبير
        result = float(self.expression.subs(symbol_values))
        
        return result
    
    def simplify(self) -> 'AdvancedSymbolicExpression':
        """
        تبسيط التعبير الرمزي.
        
        Returns:
            التعبير المبسط
        """
        simplified_expr = sp.simplify(self.expression)
        
        result = AdvancedSymbolicExpression(expression_obj=simplified_expr)
        result.metadata = copy.deepcopy(self.metadata)
        result.metadata.last_modified = datetime.now().isoformat()
        
        return result
    
    def expand(self) -> 'AdvancedSymbolicExpression':
        """
        توسيع التعبير الرمزي.
        
        Returns:
            التعبير الموسع
        """
        expanded_expr = sp.expand(self.expression)
        
        result = AdvancedSymbolicExpression(expression_obj=expanded_expr)
        result.metadata = copy.deepcopy(self.metadata)
        result.metadata.last_modified = datetime.now().isoformat()
        
        return result
    
    def factor(self) -> 'AdvancedSymbolicExpression':
        """
        تحليل التعبير الرمزي إلى عوامل.
        
        Returns:
            التعبير المحلل
        """
        factored_expr = sp.factor(self.expression)
        
        result = AdvancedSymbolicExpression(expression_obj=factored_expr)
        result.metadata = copy.deepcopy(self.metadata)
        result.metadata.last_modified = datetime.now().isoformat()
        
        return result
    
    def differentiate(self, variable: str) -> 'AdvancedSymbolicExpression':
        """
        اشتقاق التعبير الرمزي بالنسبة لمتغير.
        
        Args:
            variable: اسم المتغير
            
        Returns:
            المشتقة
        """
        symbol = sp.Symbol(variable)
        
        if symbol not in self.variables:
            logger.warning(f"المتغير {variable} غير موجود في التعبير")
            return copy.deepcopy(self)
        
        derivative = sp.diff(self.expression, symbol)
        
        result = AdvancedSymbolicExpression(expression_obj=derivative)
        result.metadata = copy.deepcopy(self.metadata)
        result.metadata.last_modified = datetime.now().isoformat()
        
        return result
    
    def integrate(self, variable: str) -> 'AdvancedSymbolicExpression':
        """
        تكامل التعبير الرمزي بالنسبة لمتغير.
        
        Args:
            variable: اسم المتغير
            
        Returns:
            التكامل
        """
        symbol = sp.Symbol(variable)
        
        if symbol not in self.variables and variable != "":
            logger.warning(f"المتغير {variable} غير موجود في التعبير")
            return copy.deepcopy(self)
        
        integral = sp.integrate(self.expression, symbol)
        
        result = AdvancedSymbolicExpression(expression_obj=integral)
        result.metadata = copy.deepcopy(self.metadata)
        result.metadata.last_modified = datetime.now().isoformat()
        
        return result
    
    def substitute(self, variable: str, value: Union[str, float]) -> 'AdvancedSymbolicExpression':
        """
        استبدال متغير بقيمة أو تعبير آخر.
        
        Args:
            variable: اسم المتغير
            value: القيمة أو التعبير
            
        Returns:
            التعبير بعد الاستبدال
        """
        symbol = sp.Symbol(variable)
        
        if symbol not in self.variables:
            logger.warning(f"المتغير {variable} غير موجود في التعبير")
            return copy.deepcopy(self)
        
        if isinstance(value, str):
            value_expr = sp.sympify(value)
        else:
            value_expr = value
        
        substituted = self.expression.subs(symbol, value_expr)
        
        result = AdvancedSymbolicExpression(expression_obj=substituted)
        result.metadata = copy.deepcopy(self.metadata)
        result.metadata.last_modified = datetime.now().isoformat()
        
        return result
    
    def combine(self, other: 'AdvancedSymbolicExpression', operation: str = "add") -> 'AdvancedSymbolicExpression':
        """
        دمج التعبير مع تعبير آخر باستخدام عملية محددة.
        
        Args:
            other: التعبير الآخر
            operation: العملية (add, multiply, divide, subtract, power)
            
        Returns:
            التعبير المدمج
        """
        if operation == "add":
            combined_expr = self.expression + other.expression
        elif operation == "multiply":
            combined_expr = self.expression * other.expression
        elif operation == "divide":
            combined_expr = self.expression / other.expression
        elif operation == "subtract":
            combined_expr = self.expression - other.expression
        elif operation == "power":
            combined_expr = self.expression ** other.expression
        else:
            logger.warning(f"العملية {operation} غير مدعومة")
            return copy.deepcopy(self)
        
        result = AdvancedSymbolicExpression(expression_obj=combined_expr)
        
        # دمج البيانات الوصفية
        result.metadata = copy.deepcopy(self.metadata)
        result.metadata.last_modified = datetime.now().isoformat()
        result.metadata.operations = list(set(self.metadata.operations + other.metadata.operations + [operation]))
        result.metadata.semantic_tags = list(set(self.metadata.semantic_tags + other.metadata.semantic_tags))
        result.metadata.domains = list(set(self.metadata.domains + other.metadata.domains))
        
        return result
    
    def mutate(self, mutation_rate: float = 0.1) -> 'AdvancedSymbolicExpression':
        """
        تطفير التعبير الرمزي.
        
        Args:
            mutation_rate: معدل الطفرة
            
        Returns:
            التعبير المطفر
        """
        # نسخ التعبير
        mutated = copy.deepcopy(self)
        
        # اختيار عملية الطفرة
        mutation_type = random.choice(["add_term", "remove_term", "change_operation", "change_constant"])
        
        if mutation_type == "add_term":
            # إضافة حد جديد
            term = self._generate_random_term()
            mutated = self.combine(term, "add")
        
        elif mutation_type == "remove_term" and isinstance(self.expression, sp.Add) and len(self.expression.args) > 1:
            # إزالة حد
            terms = list(self.expression.args)
            term_to_remove = random.choice(terms)
            remaining_terms = sp.Add(*[term for term in terms if term != term_to_remove])
            mutated = AdvancedSymbolicExpression(expression_obj=remaining_terms)
            mutated.metadata = copy.deepcopy(self.metadata)
        
        elif mutation_type == "change_operation" and len(self.metadata.operations) > 0:
            # تغيير عملية
            old_op = random.choice(self.metadata.operations)
            new_op = random.choice(["sin", "cos", "exp", "log", "sqrt"])
            
            if old_op == "sin" and "sin" in str(self.expression):
                mutated = AdvancedSymbolicExpression(expression_str=str(self.expression).replace("sin", new_op))
            elif old_op == "cos" and "cos" in str(self.expression):
                mutated = AdvancedSymbolicExpression(expression_str=str(self.expression).replace("cos", new_op))
            elif old_op == "exp" and "exp" in str(self.expression):
                mutated = AdvancedSymbolicExpression(expression_str=str(self.expression).replace("exp", new_op))
            elif old_op == "log" and "log" in str(self.expression):
                mutated = AdvancedSymbolicExpression(expression_str=str(self.expression).replace("log", new_op))
            
            mutated.metadata = copy.deepcopy(self.metadata)
        
        elif mutation_type == "change_constant":
            # تغيير ثابت
            constants = []
            
            # البحث عن الثوابت في التعبير
            for atom in self.expression.atoms():
                if atom.is_number:
                    constants.append(atom)
            
            if constants:
                # اختيار ثابت عشوائي
                constant = random.choice(constants)
                
                # توليد ثابت جديد
                new_constant = constant * (1 + random.uniform(-mutation_rate, mutation_rate))
                
                # استبدال الثابت
                mutated_expr = self.expression.subs(constant, new_constant)
                mutated = AdvancedSymbolicExpression(expression_obj=mutated_expr)
                mutated.metadata = copy.deepcopy(self.metadata)
        
        # تحديث البيانات الوصفية
        mutated.metadata.last_modified = datetime.now().isoformat()
        
        return mutated
    
    def _generate_random_term(self) -> 'AdvancedSymbolicExpression':
        """
        توليد حد عشوائي.
        
        Returns:
            الحد العشوائي
        """
        # اختيار متغير عشوائي من المتغيرات الموجودة
        if self.variables:
            variable = random.choice(list(self.variables))
        else:
            variable = sp.Symbol('x')
        
        # اختيار عملية عشوائية
        operation = random.choice(["identity", "sin", "cos", "exp", "power"])
        
        # توليد ثابت عشوائي
        constant = random.uniform(-2.0, 2.0)
        
        # إنشاء الحد
        if operation == "identity":
            term = constant * variable
        elif operation == "sin":
            term = constant * sp.sin(variable)
        elif operation == "cos":
            term = constant * sp.cos(variable)
        elif operation == "exp":
            term = constant * sp.exp(variable)
        elif operation == "power":
            power = random.randint(2, 3)
            term = constant * variable ** power
        
        return AdvancedSymbolicExpression(expression_obj=term)
    
    def crossover(self, other: 'AdvancedSymbolicExpression') -> Tuple['AdvancedSymbolicExpression', 'AdvancedSymbolicExpression']:
        """
        تقاطع التعبير مع تعبير آخر.
        
        Args:
            other: التعبير الآخر
            
        Returns:
            زوج من التعبيرات الناتجة عن التقاطع
        """
        # تحويل التعبيرات إلى سلاسل نصية
        expr1_str = str(self.expression)
        expr2_str = str(other.expression)
        
        # اختيار نقطة التقاطع
        point1 = random.randint(1, len(expr1_str) - 1)
        point2 = random.randint(1, len(expr2_str) - 1)
        
        # إنشاء التعبيرات الجديدة
        new_expr1_str = expr1_str[:point1] + expr2_str[point2:]
        new_expr2_str = expr2_str[:point2] + expr1_str[point1:]
        
        try:
            # إنشاء التعبيرات الجديدة
            child1 = AdvancedSymbolicExpression(expression_str=new_expr1_str)
            child2 = AdvancedSymbolicExpression(expression_str=new_expr2_str)
            
            # تحديث البيانات الوصفية
            child1.metadata = copy.deepcopy(self.metadata)
            child1.metadata.last_modified = datetime.now().isoformat()
            child1.metadata.equation_id = str(uuid.uuid4())
            
            child2.metadata = copy.deepcopy(other.metadata)
            child2.metadata.last_modified = datetime.now().isoformat()
            child2.metadata.equation_id = str(uuid.uuid4())
            
            return child1, child2
        
        except Exception as e:
            logger.error(f"خطأ في التقاطع: {str(e)}")
            return copy.deepcopy(self), copy.deepcopy(other)
    
    def calculate_similarity(self, other: 'AdvancedSymbolicExpression') -> float:
        """
        حساب التشابه بين التعبير وتعبير آخر.
        
        Args:
            other: التعبير الآخر
            
        Returns:
            درجة التشابه (0.0 - 1.0)
        """
        # حساب التشابه بين المتغيرات
        variables1 = self.variables
        variables2 = other.variables
        
        if not variables1 and not variables2:
            variables_similarity = 1.0
        elif not variables1 or not variables2:
            variables_similarity = 0.0
        else:
            common_variables = variables1.intersection(variables2)
            variables_similarity = len(common_variables) / max(len(variables1), len(variables2))
        
        # حساب التشابه بين العمليات
        operations1 = set(self.metadata.operations)
        operations2 = set(other.metadata.operations)
        
        if not operations1 and not operations2:
            operations_similarity = 1.0
        elif not operations1 or not operations2:
            operations_similarity = 0.0
        else:
            common_operations = operations1.intersection(operations2)
            operations_similarity = len(common_operations) / max(len(operations1), len(operations2))
        
        # حساب التشابه بين التعقيد
        complexity1 = self.metadata.complexity
        complexity2 = other.metadata.complexity
        
        complexity_similarity = 1.0 - min(abs(complexity1 - complexity2) / max(complexity1, complexity2, 1.0), 1.0)
        
        # حساب التشابه الإجمالي
        similarity = 0.4 * variables_similarity + 0.4 * operations_similarity + 0.2 * complexity_similarity
        
        return similarity
    
    def extract_patterns(self) -> Dict[str, Any]:
        """
        استخراج الأنماط من التعبير الرمزي.
        
        Returns:
            قاموس يحتوي على الأنماط المستخرجة
        """
        patterns = {
            "symmetry": self._check_symmetry(),
            "periodicity": self._check_periodicity(),
            "singularities": self._find_singularities(),
            "zeros": self._find_zeros(),
            "growth_rate": self._estimate_growth_rate()
        }
        
        return patterns
    
    def _check_symmetry(self) -> Dict[str, bool]:
        """
        التحقق من تناظر التعبير.
        
        Returns:
            قاموس يحتوي على معلومات التناظر
        """
        symmetry = {
            "even": False,
            "odd": False,
            "origin": False,
            "x_axis": False,
            "y_axis": False
        }
        
        # التحقق من التناظر الزوجي والفردي
        for var in self.variables:
            # التناظر الزوجي: f(-x) = f(x)
            try:
                neg_var = self.substitute(str(var), f"-{var}")
                if self.expression == neg_var.expression:
                    symmetry["even"] = True
                
                # التناظر الفردي: f(-x) = -f(x)
                if self.expression == -neg_var.expression:
                    symmetry["odd"] = True
            except Exception:
                pass
        
        # التناظر حول المحاور والأصل يتطلب تحليلاً أكثر تعقيداً
        # ويمكن تنفيذه في إصدارات مستقبلية
        
        return symmetry
    
    def _check_periodicity(self) -> Dict[str, Any]:
        """
        التحقق من دورية التعبير.
        
        Returns:
            قاموس يحتوي على معلومات الدورية
        """
        periodicity = {
            "is_periodic": False,
            "period": None,
            "variables": []
        }
        
        # التحقق من وجود دوال دورية
        periodic_functions = ["sin", "cos", "tan"]
        
        for func in periodic_functions:
            if func in self.metadata.operations:
                periodicity["is_periodic"] = True
                break
        
        # تحديد الفترة والمتغيرات الدورية يتطلب تحليلاً أكثر تعقيداً
        # ويمكن تنفيذه في إصدارات مستقبلية
        
        return periodicity
    
    def _find_singularities(self) -> List[Dict[str, Any]]:
        """
        البحث عن نقاط الانفصال في التعبير.
        
        Returns:
            قائمة بنقاط الانفصال
        """
        singularities = []
        
        # البحث عن المقامات
        try:
            # تحليل التعبير إلى بسط ومقام
            numerator, denominator = self.expression.as_numer_denom()
            
            # البحث عن جذور المقام
            if denominator != 1:
                for var in self.variables:
                    try:
                        solutions = sp.solve(denominator, var)
                        
                        for solution in solutions:
                            singularity = {
                                "variable": str(var),
                                "value": str(solution),
                                "type": "pole"
                            }
                            
                            singularities.append(singularity)
                    except Exception:
                        pass
        except Exception:
            pass
        
        return singularities
    
    def _find_zeros(self) -> List[Dict[str, Any]]:
        """
        البحث عن أصفار التعبير.
        
        Returns:
            قائمة بأصفار التعبير
        """
        zeros = []
        
        # البحث عن جذور التعبير
        for var in self.variables:
            try:
                solutions = sp.solve(self.expression, var)
                
                for solution in solutions:
                    zero = {
                        "variable": str(var),
                        "value": str(solution)
                    }
                    
                    zeros.append(zero)
            except Exception:
                pass
        
        return zeros
    
    def _estimate_growth_rate(self) -> Dict[str, Any]:
        """
        تقدير معدل نمو التعبير.
        
        Returns:
            قاموس يحتوي على معلومات معدل النمو
        """
        growth_rate = {
            "type": "unknown",
            "order": 0
        }
        
        # تقدير نوع النمو
        if "exp" in self.metadata.operations:
            growth_rate["type"] = "exponential"
        elif "log" in self.metadata.operations:
            growth_rate["type"] = "logarithmic"
        elif "power" in self.metadata.operations:
            growth_rate["type"] = "polynomial"
            
            # تقدير درجة كثير الحدود
            try:
                for var in self.variables:
                    degree = sp.degree(self.expression, var)
                    
                    if degree > growth_rate["order"]:
                        growth_rate["order"] = degree
            except Exception:
                pass
        
        return growth_rate
    
    def to_semantic_representation(self) -> Dict[str, Any]:
        """
        تحويل التعبير إلى تمثيل دلالي.
        
        Returns:
            قاموس يمثل التمثيل الدلالي
        """
        # استخراج الأنماط
        patterns = self.extract_patterns()
        
        # إنشاء التمثيل الدلالي
        semantic_representation = {
            "equation_id": self.metadata.equation_id,
            "expression": str(self.expression),
            "variables": [str(var) for var in self.variables],
            "operations": self.metadata.operations,
            "complexity": self.metadata.complexity,
            "patterns": patterns,
            "semantic_tags": self.metadata.semantic_tags,
            "domains": self.metadata.domains,
            "properties": self.metadata.properties
        }
        
        return semantic_representation
    
    def from_semantic_representation(self, semantic_representation: Dict[str, Any]) -> 'AdvancedSymbolicExpression':
        """
        إنشاء تعبير من تمثيل دلالي.
        
        Args:
            semantic_representation: التمثيل الدلالي
            
        Returns:
            التعبير الرمزي
        """
        # إنشاء التعبير
        expression = AdvancedSymbolicExpression(expression_str=semantic_representation["expression"])
        
        # تحديث البيانات الوصفية
        expression.metadata.equation_id = semantic_representation["equation_id"]
        expression.metadata.operations = semantic_representation["operations"]
        expression.metadata.complexity = semantic_representation["complexity"]
        expression.metadata.semantic_tags = semantic_representation["semantic_tags"]
        expression.metadata.domains = semantic_representation["domains"]
        expression.metadata.properties = semantic_representation["properties"]
        
        return expression
    
    def to_json(self) -> str:
        """
        تحويل التعبير إلى سلسلة JSON.
        
        Returns:
            سلسلة JSON
        """
        data = {
            "expression": str(self.expression),
            "metadata": self.metadata.to_dict(),
            "variables": [str(var) for var in self.variables]
        }
        
        return json.dumps(data, ensure_ascii=False, indent=4)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'AdvancedSymbolicExpression':
        """
        إنشاء تعبير من سلسلة JSON.
        
        Args:
            json_str: سلسلة JSON
            
        Returns:
            التعبير الرمزي
        """
        data = json.loads(json_str)
        
        # إنشاء التعبير
        expression = cls(expression_str=data["expression"])
        
        # تحديث البيانات الوصفية
        expression.metadata = SymbolicMetadata.from_dict(data["metadata"])
        
        return expression
    
    def __str__(self) -> str:
        """
        تحويل التعبير إلى سلسلة نصية.
        
        Returns:
            سلسلة نصية تمثل التعبير
        """
        return str(self.expression)
    
    def __repr__(self) -> str:
        """
        تمثيل التعبير.
        
        Returns:
            تمثيل التعبير
        """
        return f"AdvancedSymbolicExpression({str(self.expression)})"


class SymbolicExpressionFactory:
    """
    مصنع لإنشاء أنواع مختلفة من التعبيرات الرمزية.
    """
    
    @staticmethod
    def create_random_expression(variables: List[str] = None, complexity: float = 2.0) -> AdvancedSymbolicExpression:
        """
        إنشاء تعبير رمزي عشوائي.
        
        Args:
            variables: قائمة بأسماء المتغيرات
            complexity: درجة التعقيد
            
        Returns:
            التعبير الرمزي العشوائي
        """
        if variables is None:
            variables = ["x", "y"]
        
        # إنشاء رموز للمتغيرات
        symbols = [sp.Symbol(var) for var in variables]
        
        # تحديد عدد الحدود
        num_terms = max(1, int(complexity))
        
        # إنشاء الحدود
        terms = []
        
        for _ in range(num_terms):
            # اختيار متغير عشوائي
            var = random.choice(symbols)
            
            # اختيار عملية عشوائية
            operation = random.choice(["identity", "sin", "cos", "exp", "power"])
            
            # توليد ثابت عشوائي
            constant = random.uniform(-2.0, 2.0)
            
            # إنشاء الحد
            if operation == "identity":
                term = constant * var
            elif operation == "sin":
                term = constant * sp.sin(var)
            elif operation == "cos":
                term = constant * sp.cos(var)
            elif operation == "exp":
                term = constant * sp.exp(var)
            elif operation == "power":
                power = random.randint(2, 3)
                term = constant * var ** power
            
            terms.append(term)
        
        # دمج الحدود
        expression = sum(terms)
        
        return AdvancedSymbolicExpression(expression_obj=expression)
    
    @staticmethod
    def create_polynomial(variables: List[str] = None, degree: int = 2) -> AdvancedSymbolicExpression:
        """
        إنشاء كثير حدود.
        
        Args:
            variables: قائمة بأسماء المتغيرات
            degree: درجة كثير الحدود
            
        Returns:
            كثير الحدود
        """
        if variables is None:
            variables = ["x"]
        
        # إنشاء رموز للمتغيرات
        symbols = [sp.Symbol(var) for var in variables]
        
        # إنشاء كثير الحدود
        polynomial = 0
        
        for i in range(degree + 1):
            # توليد معامل عشوائي
            coefficient = random.uniform(-2.0, 2.0)
            
            # إنشاء الحد
            if i == 0:
                term = coefficient
            else:
                # اختيار متغير عشوائي
                var = random.choice(symbols)
                
                term = coefficient * var ** i
            
            polynomial += term
        
        return AdvancedSymbolicExpression(expression_obj=polynomial)
    
    @staticmethod
    def create_trigonometric(variables: List[str] = None, num_terms: int = 2) -> AdvancedSymbolicExpression:
        """
        إنشاء تعبير مثلثي.
        
        Args:
            variables: قائمة بأسماء المتغيرات
            num_terms: عدد الحدود
            
        Returns:
            التعبير المثلثي
        """
        if variables is None:
            variables = ["x"]
        
        # إنشاء رموز للمتغيرات
        symbols = [sp.Symbol(var) for var in variables]
        
        # إنشاء التعبير المثلثي
        expression = 0
        
        for _ in range(num_terms):
            # اختيار متغير عشوائي
            var = random.choice(symbols)
            
            # اختيار دالة مثلثية عشوائية
            trig_func = random.choice([sp.sin, sp.cos, sp.tan])
            
            # توليد معامل عشوائي
            coefficient = random.uniform(-2.0, 2.0)
            
            # توليد تردد عشوائي
            frequency = random.uniform(0.5, 2.0)
            
            # إنشاء الحد
            term = coefficient * trig_func(frequency * var)
            
            expression += term
        
        return AdvancedSymbolicExpression(expression_obj=expression)
    
    @staticmethod
    def create_exponential(variables: List[str] = None) -> AdvancedSymbolicExpression:
        """
        إنشاء تعبير أسي.
        
        Args:
            variables: قائمة بأسماء المتغيرات
            
        Returns:
            التعبير الأسي
        """
        if variables is None:
            variables = ["x"]
        
        # إنشاء رموز للمتغيرات
        symbols = [sp.Symbol(var) for var in variables]
        
        # اختيار متغير عشوائي
        var = random.choice(symbols)
        
        # توليد معامل عشوائي
        coefficient = random.uniform(-2.0, 2.0)
        
        # توليد معامل أسي عشوائي
        exponent_coefficient = random.uniform(-1.0, 1.0)
        
        # إنشاء التعبير الأسي
        expression = coefficient * sp.exp(exponent_coefficient * var)
        
        return AdvancedSymbolicExpression(expression_obj=expression)
    
    @staticmethod
    def create_logarithmic(variables: List[str] = None) -> AdvancedSymbolicExpression:
        """
        إنشاء تعبير لوغاريتمي.
        
        Args:
            variables: قائمة بأسماء المتغيرات
            
        Returns:
            التعبير اللوغاريتمي
        """
        if variables is None:
            variables = ["x"]
        
        # إنشاء رموز للمتغيرات
        symbols = [sp.Symbol(var) for var in variables]
        
        # اختيار متغير عشوائي
        var = random.choice(symbols)
        
        # توليد معامل عشوائي
        coefficient = random.uniform(-2.0, 2.0)
        
        # إنشاء التعبير اللوغاريتمي
        expression = coefficient * sp.log(sp.Abs(var))
        
        return AdvancedSymbolicExpression(expression_obj=expression)
    
    @staticmethod
    def create_rational(variables: List[str] = None, numerator_degree: int = 2, denominator_degree: int = 1) -> AdvancedSymbolicExpression:
        """
        إنشاء تعبير كسري.
        
        Args:
            variables: قائمة بأسماء المتغيرات
            numerator_degree: درجة البسط
            denominator_degree: درجة المقام
            
        Returns:
            التعبير الكسري
        """
        # إنشاء البسط
        numerator = SymbolicExpressionFactory.create_polynomial(variables, numerator_degree)
        
        # إنشاء المقام
        denominator = SymbolicExpressionFactory.create_polynomial(variables, denominator_degree)
        
        # التأكد من أن المقام لا يساوي صفر
        while str(denominator) == "0":
            denominator = SymbolicExpressionFactory.create_polynomial(variables, denominator_degree)
        
        # إنشاء التعبير الكسري
        expression = numerator.expression / denominator.expression
        
        return AdvancedSymbolicExpression(expression_obj=expression)


# اختبار الوحدة
if __name__ == "__main__":
    # إنشاء تعبير رمزي
    expr = AdvancedSymbolicExpression(expression_str="sin(x**2 + y**2) * exp(-x*y)")
    
    print(f"التعبير: {expr}")
    print(f"المتغيرات: {expr.variables}")
    print(f"العمليات: {expr.metadata.operations}")
    print(f"التعقيد: {expr.metadata.complexity}")
    
    # تقييم التعبير
    result = expr.evaluate({"x": 1.0, "y": 2.0})
    print(f"التقييم عند x=1.0, y=2.0: {result}")
    
    # تبسيط التعبير
    simplified = expr.simplify()
    print(f"التعبير المبسط: {simplified}")
    
    # اشتقاق التعبير
    derivative = expr.differentiate("x")
    print(f"المشتقة بالنسبة لـ x: {derivative}")
    
    # تكامل التعبير
    integral = expr.integrate("x")
    print(f"التكامل بالنسبة لـ x: {integral}")
    
    # طفرة التعبير
    mutated = expr.mutate()
    print(f"التعبير المطفر: {mutated}")
    
    # حساب التشابه
    similarity = expr.calculate_similarity(mutated)
    print(f"التشابه: {similarity}")
    
    # استخراج الأنماط
    patterns = expr.extract_patterns()
    print(f"الأنماط: {patterns}")
    
    # إنشاء تعبير عشوائي
    random_expr = SymbolicExpressionFactory.create_random_expression()
    print(f"تعبير عشوائي: {random_expr}")
    
    # إنشاء كثير حدود
    polynomial = SymbolicExpressionFactory.create_polynomial()
    print(f"كثير حدود: {polynomial}")
    
    # إنشاء تعبير مثلثي
    trigonometric = SymbolicExpressionFactory.create_trigonometric()
    print(f"تعبير مثلثي: {trigonometric}")
    
    # إنشاء تعبير أسي
    exponential = SymbolicExpressionFactory.create_exponential()
    print(f"تعبير أسي: {exponential}")
    
    # إنشاء تعبير لوغاريتمي
    logarithmic = SymbolicExpressionFactory.create_logarithmic()
    print(f"تعبير لوغاريتمي: {logarithmic}")
    
    # إنشاء تعبير كسري
    rational = SymbolicExpressionFactory.create_rational()
    print(f"تعبير كسري: {rational}")
