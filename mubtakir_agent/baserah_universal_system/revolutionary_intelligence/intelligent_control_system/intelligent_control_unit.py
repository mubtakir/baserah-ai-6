#!/usr/bin/env python3
# intelligent_control_unit.py - وحدة التحكم الذكي Baserah النقية

import numpy as np
import math
from typing import Dict, List, Tuple, Any, Optional
from datetime import datetime
import uuid

# استيراد نواة Baserah النقية
from artistic_intelligence.baserah_core import baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid

class BaserahTauBalanceUnit:
    """
    وحدة توازن Tau Baserah النقية
    مستوحاة من TauRLayer ولكن باستخدام السيجمويد والخطي فقط
    """
    
    def __init__(self, alpha: float = 0.1, beta: float = 0.1):
        """تهيئة وحدة التوازن."""
        
        self.alpha = alpha
        self.beta = beta
        self.epsilon = 1e-6
        
        # معاملات التكيف
        self.progress_weight = 1.0
        self.risk_weight = 1.0
        self.adaptation_rate = 0.01
        
        print("⚖️ تم تهيئة وحدة توازن Tau Baserah النقية")
    
    def calculate_tau_balance(self, progress: float, risk: float) -> float:
        """
        حساب توازن Tau باستخدام معادلات Baserah النقية.
        
        Args:
            progress: مقدار التقدم
            risk: مقدار المخاطر
            
        Returns:
            قيمة التوازن Tau
        """
        
        # تحويل التقدم باستخدام الخطي
        progress_transformed = baserah_linear(
            progress, 
            beta=self.progress_weight, 
            gamma=self.alpha
        )
        
        # تحويل المخاطر باستخدام الخطي
        risk_transformed = baserah_linear(
            risk, 
            beta=self.risk_weight, 
            gamma=self.beta
        )
        
        # حساب النسبة
        denominator = risk_transformed + self.epsilon
        ratio = progress_transformed / denominator
        
        # تطبيق السيجمويد للحصول على قيمة متوازنة
        tau_balance = baserah_sigmoid(
            ratio, 
            n=1, 
            k=2.0, 
            x0=0.0, 
            alpha=1.0
        )
        
        return tau_balance
    
    def adapt_weights(self, feedback: float):
        """تكييف الأوزان بناءً على التغذية الراجعة."""
        
        if feedback > 0:  # تحسن
            self.progress_weight += self.adaptation_rate
            self.risk_weight *= 0.99
        else:  # تراجع
            self.progress_weight *= 0.99
            self.risk_weight += self.adaptation_rate
        
        # تحديد الحدود
        self.progress_weight = max(0.1, min(2.0, self.progress_weight))
        self.risk_weight = max(0.1, min(2.0, self.risk_weight))

class BaserahDynamicMathUnit:
    """
    وحدة رياضية ديناميكية Baserah النقية
    مستوحاة من DynamicMathUnit ولكن باستخدام السيجمويد والخطي فقط
    """
    
    def __init__(self, complexity: int = 5):
        """تهيئة الوحدة الرياضية الديناميكية."""
        
        self.complexity = complexity
        
        # معاملات السيجمويد
        self.sigmoid_coeffs = np.random.randn(complexity) * 0.1
        self.sigmoid_k_values = np.random.rand(complexity) * 2.0 + 0.5
        self.sigmoid_x0_values = np.random.randn(complexity) * 0.5
        
        # معاملات الخطي
        self.linear_betas = np.random.randn(complexity) * 0.1
        self.linear_gammas = np.random.randn(complexity) * 0.1
        
        # أوزان التركيب
        self.composition_weights = np.random.rand(complexity)
        self.composition_weights /= np.sum(self.composition_weights)
        
        print(f"🧮 تم تهيئة الوحدة الرياضية الديناميكية Baserah (تعقيد: {complexity})")
    
    def compute_dynamic_output(self, x: float) -> float:
        """
        حساب المخرج الديناميكي باستخدام معادلات Baserah النقية.
        
        Args:
            x: المدخل
            
        Returns:
            المخرج الديناميكي
        """
        
        total_output = 0.0
        
        for i in range(self.complexity):
            # مكون السيجمويد
            sigmoid_component = baserah_sigmoid(
                x,
                n=1,
                k=self.sigmoid_k_values[i],
                x0=self.sigmoid_x0_values[i],
                alpha=1.0
            )
            
            # مكون الخطي
            linear_component = baserah_linear(
                x,
                beta=self.linear_betas[i],
                gamma=self.linear_gammas[i]
            )
            
            # تركيب المكونات
            combined_component = (
                self.sigmoid_coeffs[i] * sigmoid_component +
                (1 - self.sigmoid_coeffs[i]) * linear_component
            )
            
            # إضافة للمخرج الإجمالي
            total_output += self.composition_weights[i] * combined_component
        
        return total_output
    
    def evolve_parameters(self, feedback: float):
        """تطوير المعاملات بناءً على التغذية الراجعة."""
        
        evolution_rate = 0.01
        
        if feedback > 0:  # تحسن
            # تحسين المعاملات الحالية
            self.sigmoid_k_values *= (1 + evolution_rate)
            self.linear_betas *= (1 + evolution_rate)
        else:  # تراجع
            # إضافة تنويع
            noise_sigmoid = np.random.randn(self.complexity) * evolution_rate
            noise_linear = np.random.randn(self.complexity) * evolution_rate
            
            self.sigmoid_k_values += noise_sigmoid
            self.linear_betas += noise_linear
        
        # تحديد الحدود
        self.sigmoid_k_values = np.clip(self.sigmoid_k_values, 0.1, 5.0)
        self.linear_betas = np.clip(self.linear_betas, -2.0, 2.0)

class BaserahIntelligentControlUnit:
    """
    وحدة التحكم الذكي Baserah النقية
    مستوحاة من IMRLS ولكن باستخدام منهجنا الثوري فقط
    """
    
    def __init__(self, input_dim: int = 3, output_dim: int = 3, complexity: int = 5):
        """تهيئة وحدة التحكم الذكي."""
        
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.complexity = complexity
        
        # المكونات الأساسية
        self.tau_balance_unit = BaserahTauBalanceUnit()
        self.dynamic_math_units = [
            BaserahDynamicMathUnit(complexity) for _ in range(output_dim)
        ]
        
        # ذاكرة التجارب
        self.experience_memory = []
        self.max_memory_size = 1000
        
        # إحصائيات الأداء
        self.performance_history = []
        self.adaptation_count = 0
        
        print(f"🧠 تم تهيئة وحدة التحكم الذكي Baserah النقية")
        print(f"   📊 أبعاد: {input_dim} → {output_dim}")
        print(f"   🔧 تعقيد: {complexity}")
    
    def process_input(self, inputs: List[float], target: List[float] = None) -> List[float]:
        """
        معالجة المدخلات وإنتاج مخرجات التحكم.
        
        Args:
            inputs: المدخلات
            target: الهدف المطلوب (اختياري)
            
        Returns:
            مخرجات التحكم
        """
        
        if len(inputs) != self.input_dim:
            raise ValueError(f"Expected {self.input_dim} inputs, got {len(inputs)}")
        
        outputs = []
        
        for i in range(self.output_dim):
            # حساب المخرج لكل بعد
            output_value = 0.0
            
            for j, input_val in enumerate(inputs):
                # معالجة كل مدخل بالوحدة الرياضية الديناميكية
                processed_input = self.dynamic_math_units[i].compute_dynamic_output(input_val)
                
                # تطبيق وزن بناءً على الموقع
                weight = baserah_sigmoid(
                    j - i, 
                    n=1, 
                    k=1.0, 
                    x0=0.0, 
                    alpha=1.0
                )
                
                output_value += weight * processed_input
            
            # تطبيق توازن Tau إذا كان الهدف متاحاً
            if target and i < len(target):
                error = abs(target[i] - output_value)
                progress = max(0, 1.0 - error)
                risk = error
                
                tau_balance = self.tau_balance_unit.calculate_tau_balance(progress, risk)
                output_value *= tau_balance
            
            outputs.append(output_value)
        
        return outputs
    
    def learn_from_experience(self, inputs: List[float], outputs: List[float], 
                            reward: float, target: List[float] = None):
        """
        التعلم من التجربة وتحديث المعاملات.
        
        Args:
            inputs: المدخلات
            outputs: المخرجات
            reward: المكافأة
            target: الهدف (اختياري)
        """
        
        # حفظ التجربة
        experience = {
            'inputs': inputs.copy(),
            'outputs': outputs.copy(),
            'reward': reward,
            'target': target.copy() if target else None,
            'timestamp': datetime.now()
        }
        
        self.experience_memory.append(experience)
        
        # تحديد حجم الذاكرة
        if len(self.experience_memory) > self.max_memory_size:
            self.experience_memory.pop(0)
        
        # تحديث الأداء
        self.performance_history.append(reward)
        
        # التكيف بناءً على المكافأة
        self._adapt_parameters(reward)
        
        self.adaptation_count += 1
    
    def _adapt_parameters(self, reward: float):
        """تكييف المعاملات بناءً على المكافأة."""
        
        # تحديد ما إذا كانت المكافأة تحسن أم لا
        improvement = 0.0
        if len(self.performance_history) > 1:
            improvement = reward - self.performance_history[-2]
        
        # تكييف وحدة التوازن
        self.tau_balance_unit.adapt_weights(improvement)
        
        # تطوير الوحدات الرياضية الديناميكية
        for unit in self.dynamic_math_units:
            unit.evolve_parameters(improvement)
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """الحصول على ملخص الأداء."""
        
        if not self.performance_history:
            return {'message': 'لا توجد بيانات أداء'}
        
        recent_performance = self.performance_history[-10:] if len(self.performance_history) >= 10 else self.performance_history
        
        summary = {
            'total_experiences': len(self.experience_memory),
            'adaptation_count': self.adaptation_count,
            'average_reward': np.mean(self.performance_history),
            'recent_average_reward': np.mean(recent_performance),
            'best_reward': max(self.performance_history),
            'worst_reward': min(self.performance_history),
            'improvement_trend': self._calculate_trend(),
            'tau_balance_weights': {
                'progress_weight': self.tau_balance_unit.progress_weight,
                'risk_weight': self.tau_balance_unit.risk_weight
            }
        }
        
        return summary
    
    def _calculate_trend(self) -> str:
        """حساب اتجاه التحسن."""
        
        if len(self.performance_history) < 5:
            return 'غير كافي للتقييم'
        
        recent = self.performance_history[-5:]
        earlier = self.performance_history[-10:-5] if len(self.performance_history) >= 10 else self.performance_history[:-5]
        
        if not earlier:
            return 'غير كافي للمقارنة'
        
        recent_avg = np.mean(recent)
        earlier_avg = np.mean(earlier)
        
        if recent_avg > earlier_avg + 0.1:
            return 'تحسن مستمر'
        elif recent_avg < earlier_avg - 0.1:
            return 'تراجع'
        else:
            return 'مستقر'
    
    def demonstrate_control(self) -> Dict[str, Any]:
        """عرض توضيحي لوحدة التحكم."""
        
        print("\n🎭 عرض توضيحي لوحدة التحكم الذكي Baserah")
        print("=" * 50)
        
        # بيانات اختبار
        test_scenarios = [
            {
                'name': 'تحكم خطي بسيط',
                'inputs': [1.0, 0.5, -0.2],
                'target': [2.0, 1.0, 0.0]
            },
            {
                'name': 'تحكم معقد',
                'inputs': [-1.5, 2.0, 0.8],
                'target': [0.0, 0.0, 1.0]
            },
            {
                'name': 'تحكم ديناميكي',
                'inputs': [0.3, -0.7, 1.2],
                'target': [-1.0, 2.0, -0.5]
            }
        ]
        
        results = []
        
        for scenario in test_scenarios:
            print(f"\n🔧 اختبار: {scenario['name']}")
            
            # معالجة المدخلات
            outputs = self.process_input(scenario['inputs'], scenario['target'])
            
            # حساب الخطأ
            if scenario['target']:
                errors = [abs(t - o) for t, o in zip(scenario['target'], outputs)]
                total_error = sum(errors)
                reward = max(0, 1.0 - total_error)
            else:
                reward = 0.5
            
            # التعلم من التجربة
            self.learn_from_experience(
                scenario['inputs'], 
                outputs, 
                reward, 
                scenario['target']
            )
            
            result = {
                'scenario': scenario['name'],
                'inputs': scenario['inputs'],
                'outputs': outputs,
                'target': scenario['target'],
                'reward': reward,
                'errors': errors if scenario['target'] else None
            }
            
            results.append(result)
            
            print(f"   📊 المدخلات: {scenario['inputs']}")
            print(f"   📈 المخرجات: {[f'{o:.3f}' for o in outputs]}")
            print(f"   🎯 الهدف: {scenario['target']}")
            print(f"   🏆 المكافأة: {reward:.3f}")
        
        # ملخص الأداء
        performance = self.get_performance_summary()
        print(f"\n📊 ملخص الأداء:")
        print(f"   التجارب: {performance['total_experiences']}")
        print(f"   التكيفات: {performance['adaptation_count']}")
        print(f"   متوسط المكافأة: {performance['average_reward']:.3f}")
        print(f"   اتجاه التحسن: {performance['improvement_trend']}")
        
        return {
            'test_results': results,
            'performance_summary': performance
        }
