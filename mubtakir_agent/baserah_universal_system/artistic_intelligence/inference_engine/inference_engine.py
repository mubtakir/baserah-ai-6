#!/usr/bin/env python3
# inference_engine.py - محرك الاستنباط Baserah (عين النظام) - نسخة الوحدة الفنية

import math
from typing import List, Tuple, Dict, Optional, Union
from .baserah_core import (
    baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid, baserah_equation
)

class BaserahInferenceEngine:
    """
    محرك الاستنباط Baserah - عين النظام
    يستنتج معادلات الشكل العام من البيانات باستخدام منهج Baserah النقي فقط
    """
    
    def __init__(self):
        self.tolerance = 1e-6
        self.max_iterations = 1000
        self.learning_rate = 0.01
        
    def infer_from_data_points(self, x_data: List[float], y_data: List[float]) -> Dict:
        """
        استنتاج معادلة الشكل العام من نقاط البيانات
        """
        if len(x_data) != len(y_data) or len(x_data) < 3:
            return {'error': 'بيانات غير كافية'}
        
        print(f"🔍 بدء الاستنباط من {len(x_data)} نقطة بيانات...")
        
        # تحليل نوع البيانات
        data_analysis = self._analyze_data_pattern(x_data, y_data)
        print(f"   نوع النمط المكتشف: {data_analysis['pattern_type']}")
        
        # استنتاج المعاملات حسب النمط
        if data_analysis['pattern_type'] == 'linear':
            return self._infer_linear_parameters(x_data, y_data)
        elif data_analysis['pattern_type'] == 'sigmoid':
            return self._infer_sigmoid_parameters(x_data, y_data)
        elif data_analysis['pattern_type'] == 'step':
            return self._infer_quantum_parameters(x_data, y_data)
        elif data_analysis['pattern_type'] == 'mixed':
            return self._infer_mixed_parameters(x_data, y_data)
        else:
            return self._infer_general_parameters(x_data, y_data)
    
    def _analyze_data_pattern(self, x_data: List[float], y_data: List[float]) -> Dict:
        """تحليل نمط البيانات لتحديد نوع الدالة المناسبة"""
        
        # حساب الاختلافات
        y_range = max(y_data) - min(y_data)
        y_mean = sum(y_data) / len(y_data)
        
        # حساب التدرج
        gradients = []
        for i in range(1, len(x_data)):
            if x_data[i] != x_data[i-1]:
                grad = (y_data[i] - y_data[i-1]) / (x_data[i] - x_data[i-1])
                gradients.append(grad)
        
        if not gradients:
            return {'pattern_type': 'constant', 'confidence': 1.0}
        
        grad_variance = self._calculate_variance(gradients)
        grad_mean = sum(gradients) / len(gradients)
        
        # تحديد النمط
        if grad_variance < 0.01:  # تدرج ثابت تقريباً
            return {'pattern_type': 'linear', 'confidence': 0.9}
        elif self._is_step_function(y_data):
            return {'pattern_type': 'step', 'confidence': 0.8}
        elif self._is_sigmoid_like(x_data, y_data):
            return {'pattern_type': 'sigmoid', 'confidence': 0.7}
        else:
            return {'pattern_type': 'mixed', 'confidence': 0.5}
    
    def _is_step_function(self, y_data: List[float]) -> bool:
        """فحص إذا كانت البيانات تشبه دالة متقطعة"""
        unique_values = list(set(y_data))
        return len(unique_values) <= 5 and len(unique_values) < len(y_data) / 3
    
    def _is_sigmoid_like(self, x_data: List[float], y_data: List[float]) -> bool:
        """فحص إذا كانت البيانات تشبه السيجمويد"""
        y_min, y_max = min(y_data), max(y_data)
        y_range = y_max - y_min
        
        if y_range < 0.1:
            return False
        
        # فحص الشكل S
        sorted_pairs = sorted(zip(x_data, y_data))
        y_sorted = [pair[1] for pair in sorted_pairs]
        
        # فحص الزيادة التدريجية
        increasing_count = 0
        for i in range(1, len(y_sorted)):
            if y_sorted[i] >= y_sorted[i-1]:
                increasing_count += 1
        
        return increasing_count / len(y_sorted) > 0.7
    
    def _calculate_variance(self, data: List[float]) -> float:
        """حساب التباين"""
        if len(data) < 2:
            return 0.0
        
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return variance
    
    def _infer_linear_parameters(self, x_data: List[float], y_data: List[float]) -> Dict:
        """استنتاج معاملات الخط المستقيم"""
        print("   استنتاج معاملات خطية...")
        
        # حساب الميل والتقاطع بطريقة المربعات الصغرى
        n = len(x_data)
        sum_x = sum(x_data)
        sum_y = sum(y_data)
        sum_xy = sum(x_data[i] * y_data[i] for i in range(n))
        sum_x2 = sum(x * x for x in x_data)
        
        denominator = n * sum_x2 - sum_x * sum_x
        if abs(denominator) < self.tolerance:
            beta = 0.0
            gamma = sum_y / n
        else:
            beta = (n * sum_xy - sum_x * sum_y) / denominator
            gamma = (sum_y - beta * sum_x) / n
        
        # حساب الخطأ
        error = self._calculate_error(x_data, y_data, 
                                    lambda x: baserah_linear(x, beta, gamma))
        
        return {
            'type': 'linear',
            'components': [
                {
                    'type': 'linear',
                    'params': {'beta': beta, 'gamma': gamma}
                }
            ],
            'error': error,
            'confidence': 0.9 if error < 0.1 else 0.5
        }
    
    def _infer_sigmoid_parameters(self, x_data: List[float], y_data: List[float]) -> Dict:
        """استنتاج معاملات السيجمويد"""
        print("   استنتاج معاملات السيجمويد...")
        
        # تقدير أولي للمعاملات
        y_min, y_max = min(y_data), max(y_data)
        alpha = y_max - y_min
        x_mid = (max(x_data) + min(x_data)) / 2
        
        # البحث عن أفضل معاملات
        best_params = {'n': 1, 'k': 1.0, 'x0': x_mid, 'alpha': alpha}
        best_error = float('inf')
        
        # تجربة قيم مختلفة
        for n in [1, 2, 3]:
            for k in [0.5, 1.0, 2.0, 5.0]:
                for x0_offset in [-1.0, 0.0, 1.0]:
                    x0 = x_mid + x0_offset
                    
                    # تحسين alpha
                    alpha_opt = self._optimize_alpha(x_data, y_data, n, k, x0)
                    
                    error = self._calculate_error(x_data, y_data,
                                                lambda x: baserah_sigmoid(x, n, k, x0, alpha_opt))
                    
                    if error < best_error:
                        best_error = error
                        best_params = {'n': n, 'k': k, 'x0': x0, 'alpha': alpha_opt}
        
        return {
            'type': 'sigmoid',
            'components': [
                {
                    'type': 'sigmoid',
                    'params': best_params
                }
            ],
            'error': best_error,
            'confidence': 0.8 if best_error < 0.2 else 0.4
        }
    
    def _infer_quantum_parameters(self, x_data: List[float], y_data: List[float]) -> Dict:
        """استنتاج معاملات السيجمويد المكمم"""
        print("   استنتاج معاملات التكميم...")
        
        # تحديد عدد المستويات المنفصلة
        unique_values = sorted(list(set(y_data)))
        quantum_factor = len(unique_values)
        
        # تقدير معاملات السيجمويد الأساسي
        sigmoid_result = self._infer_sigmoid_parameters(x_data, y_data)
        
        if sigmoid_result['type'] == 'sigmoid':
            base_params = sigmoid_result['components'][0]['params']
            
            # إضافة عامل التكميم
            quantum_params = base_params.copy()
            quantum_params['quantum_factor'] = quantum_factor
            
            error = self._calculate_error(x_data, y_data,
                                        lambda x: baserah_quantum_sigmoid(x, **quantum_params))
            
            return {
                'type': 'quantum_sigmoid',
                'components': [
                    {
                        'type': 'quantum_sigmoid',
                        'params': quantum_params
                    }
                ],
                'error': error,
                'confidence': 0.7 if error < 0.3 else 0.3
            }
        
        return sigmoid_result
    
    def _infer_mixed_parameters(self, x_data: List[float], y_data: List[float]) -> Dict:
        """استنتاج معاملات مختلطة (سيجمويد + خطي)"""
        print("   استنتاج معاملات مختلطة...")
        
        # محاولة تركيب سيجمويد + خطي
        sigmoid_result = self._infer_sigmoid_parameters(x_data, y_data)
        
        if sigmoid_result['error'] > 0.5:
            # إضافة مكون خطي
            sigmoid_params = sigmoid_result['components'][0]['params']
            
            # حساب البقايا
            residuals = []
            for i, x in enumerate(x_data):
                predicted = baserah_sigmoid(x, **sigmoid_params)
                residual = y_data[i] - predicted
                residuals.append(residual)
            
            # تركيب خط مستقيم للبقايا
            linear_result = self._infer_linear_parameters(x_data, residuals)
            linear_params = linear_result['components'][0]['params']
            
            # دمج المكونات
            components = [
                {'type': 'sigmoid', 'params': sigmoid_params},
                {'type': 'linear', 'params': linear_params}
            ]
            
            error = self._calculate_error(x_data, y_data,
                                        lambda x: baserah_equation(x, components))
            
            return {
                'type': 'mixed',
                'components': components,
                'error': error,
                'confidence': 0.6 if error < 0.4 else 0.2
            }
        
        return sigmoid_result
    
    def _infer_general_parameters(self, x_data: List[float], y_data: List[float]) -> Dict:
        """استنتاج عام - محاولة جميع الأنواع"""
        print("   استنتاج عام...")
        
        results = []
        
        # تجربة جميع الأنواع
        linear_result = self._infer_linear_parameters(x_data, y_data)
        results.append(linear_result)
        
        sigmoid_result = self._infer_sigmoid_parameters(x_data, y_data)
        results.append(sigmoid_result)
        
        quantum_result = self._infer_quantum_parameters(x_data, y_data)
        results.append(quantum_result)
        
        # اختيار أفضل نتيجة
        best_result = min(results, key=lambda r: r['error'])
        
        return best_result
    
    def _optimize_alpha(self, x_data: List[float], y_data: List[float], 
                       n: int, k: float, x0: float) -> float:
        """تحسين معامل alpha"""
        
        # حساب alpha المثلى بطريقة المربعات الصغرى
        numerator = 0.0
        denominator = 0.0
        
        for i, x in enumerate(x_data):
            sigmoid_val = baserah_sigmoid(x, n, k, x0, 1.0)  # alpha = 1
            numerator += y_data[i] * sigmoid_val
            denominator += sigmoid_val * sigmoid_val
        
        if abs(denominator) < self.tolerance:
            return 1.0
        
        return numerator / denominator
    
    def _calculate_error(self, x_data: List[float], y_data: List[float], 
                        func) -> float:
        """حساب متوسط مربع الخطأ"""
        total_error = 0.0
        
        for i, x in enumerate(x_data):
            predicted = func(x)
            error = (y_data[i] - predicted) ** 2
            total_error += error
        
        return total_error / len(x_data)
    
    def generate_equation_string(self, inference_result: Dict) -> str:
        """توليد معادلة نصية من نتيجة الاستنباط"""
        
        if 'error' in inference_result:
            return f"خطأ: {inference_result['error']}"
        
        components = inference_result.get('components', [])
        if not components:
            return "لا توجد مكونات"
        
        equation_parts = []
        
        for comp in components:
            comp_type = comp['type']
            params = comp['params']
            
            if comp_type == 'linear':
                beta = params.get('beta', 0)
                gamma = params.get('gamma', 0)
                equation_parts.append(f"linear({beta:.3f}*x + {gamma:.3f})")
                
            elif comp_type == 'sigmoid':
                n = params.get('n', 1)
                k = params.get('k', 1)
                x0 = params.get('x0', 0)
                alpha = params.get('alpha', 1)
                equation_parts.append(f"sigmoid(n={n}, k={k:.3f}, x0={x0:.3f}, α={alpha:.3f})")
                
            elif comp_type == 'quantum_sigmoid':
                n = params.get('n', 1)
                k = params.get('k', 1)
                x0 = params.get('x0', 0)
                alpha = params.get('alpha', 1)
                qf = params.get('quantum_factor', 1)
                equation_parts.append(f"quantum_sigmoid(n={n}, k={k:.3f}, x0={x0:.3f}, α={alpha:.3f}, Q={qf})")
        
        equation = " + ".join(equation_parts)
        error = inference_result.get('error', 0)
        confidence = inference_result.get('confidence', 0)
        
        return f"f(x) = {equation} [خطأ: {error:.6f}, ثقة: {confidence:.2f}]"
