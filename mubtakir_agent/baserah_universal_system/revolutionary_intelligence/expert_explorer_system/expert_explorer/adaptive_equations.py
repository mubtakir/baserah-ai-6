#!/usr/bin/env python3
# adaptive_equations.py - المعادلات المتكيفة Baserah النقية

import numpy as np
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Union, Optional, Any, Callable, Set
from dataclasses import dataclass, field
from enum import Enum

@dataclass
class BaserahAdaptiveContext:
    """سياق التكيف Baserah النقي."""
    adaptation_strength: float = 0.5  # قوة التكيف
    learning_rate: float = 0.01  # معدل التعلم
    quantum_factor: int = 4  # عامل التكميم
    max_iterations: int = 100  # أقصى تكرارات
    convergence_threshold: float = 1e-6  # عتبة التقارب
    baserah_weight: float = 1.0  # وزن Baserah
    metadata: Dict[str, Any] = field(default_factory=dict)

class AdaptationMode(Enum):
    """أوضاع التكيف."""
    SIGMOID_ADAPTATION = "sigmoid_adaptation"  # تكيف سيجمويدي
    LINEAR_ADAPTATION = "linear_adaptation"  # تكيف خطي
    QUANTUM_ADAPTATION = "quantum_adaptation"  # تكيف كمي
    HYBRID_ADAPTATION = "hybrid_adaptation"  # تكيف هجين
    REVOLUTIONARY_ADAPTATION = "revolutionary_adaptation"  # تكيف ثوري

class EvolutionDirection(Enum):
    """اتجاهات التطور."""
    OPTIMIZE = "optimize"  # تحسين
    SIMPLIFY = "simplify"  # تبسيط
    GENERALIZE = "generalize"  # تعميم
    SPECIALIZE = "specialize"  # تخصيص
    TRANSFORM = "transform"  # تحويل

@dataclass
class BaserahAdaptiveMatrix:
    """المصفوفة التكيفية Baserah النقية - بديل للشبكات العصبية."""
    
    def __init__(self, size: int = 10):
        """تهيئة المصفوفة التكيفية."""
        self.size = size
        self.sigmoid_weights = np.random.uniform(-1, 1, size)
        self.linear_weights = np.random.uniform(-1, 1, size)
        self.quantum_weights = np.random.uniform(-1, 1, size)
        self.adaptation_rate = 0.01
        self.baserah_score = 1.0
        
        # سجل التكيف
        self.adaptation_history = []
        self.performance_history = []
    
    def _baserah_sigmoid(self, x: float, n: int = 1, k: float = 1.0, x0: float = 0.0, alpha: float = 1.0) -> float:
        """دالة السيجمويد Baserah النقية."""
        try:
            return alpha / (1 + np.exp(-k * (x - x0)**n))
        except (OverflowError, ZeroDivisionError):
            return alpha if x > x0 else 0.0
    
    def _baserah_linear(self, x: float, beta: float = 1.0, gamma: float = 0.0) -> float:
        """دالة الخط المستقيم Baserah النقية."""
        return beta * x + gamma
    
    def _baserah_quantum_sigmoid(self, x: float, quantum_factor: int = 4, **kwargs) -> float:
        """دالة السيجمويد المكممة Baserah النقية."""
        sigmoid_value = self._baserah_sigmoid(x, **kwargs)
        if quantum_factor > 0:
            return round(sigmoid_value * quantum_factor) / quantum_factor
        return sigmoid_value
    
    def process(self, inputs: np.ndarray) -> float:
        """معالجة المدخلات بمنهج Baserah النقي."""
        if len(inputs) != self.size:
            # تكيف حجم المدخلات
            if len(inputs) > self.size:
                inputs = inputs[:self.size]
            else:
                inputs = np.pad(inputs, (0, self.size - len(inputs)), 'constant')
        
        # معالجة سيجمويدية
        sigmoid_output = np.sum([
            w * self._baserah_sigmoid(x, n=1, k=2.0, x0=0.0, alpha=1.0) 
            for w, x in zip(self.sigmoid_weights, inputs)
        ])
        
        # معالجة خطية
        linear_output = np.sum([
            w * self._baserah_linear(x, beta=1.0, gamma=0.0) 
            for w, x in zip(self.linear_weights, inputs)
        ])
        
        # معالجة كمية
        quantum_output = np.sum([
            w * self._baserah_quantum_sigmoid(x, quantum_factor=4, n=1, k=1.0, x0=0.0, alpha=1.0)
            for w, x in zip(self.quantum_weights, inputs)
        ])
        
        # دمج النتائج بمنهج Baserah
        total_output = sigmoid_output + linear_output + quantum_output * 0.5
        
        return total_output
    
    def adapt(self, error: float, inputs: np.ndarray):
        """تكيف المصفوفة بناءً على الخطأ."""
        # حساب التدرجات بمنهج Baserah النقي
        sigmoid_gradients = error * inputs * self.adaptation_rate
        linear_gradients = error * inputs * self.adaptation_rate * 0.5
        quantum_gradients = error * inputs * self.adaptation_rate * 0.3
        
        # تحديث الأوزان
        self.sigmoid_weights -= sigmoid_gradients[:len(self.sigmoid_weights)]
        self.linear_weights -= linear_gradients[:len(self.linear_weights)]
        self.quantum_weights -= quantum_gradients[:len(self.quantum_weights)]
        
        # تحديث نقاط Baserah
        self.baserah_score = max(0.1, self.baserah_score - abs(error) * 0.01)
        
        # تسجيل التكيف
        self.adaptation_history.append({
            'timestamp': datetime.now().isoformat(),
            'error': error,
            'baserah_score': self.baserah_score
        })
    
    def get_adaptation_summary(self) -> Dict[str, Any]:
        """الحصول على ملخص التكيف."""
        return {
            'total_adaptations': len(self.adaptation_history),
            'current_baserah_score': self.baserah_score,
            'average_error': np.mean([h['error'] for h in self.adaptation_history]) if self.adaptation_history else 0.0,
            'adaptation_trend': 'improving' if len(self.adaptation_history) > 1 and 
                              self.adaptation_history[-1]['baserah_score'] > self.adaptation_history[0]['baserah_score'] 
                              else 'stable'
        }

class BaserahAdaptiveEquation:
    """معادلة متكيفة Baserah النقية."""
    
    def __init__(self, equation_id: str = None):
        """تهيئة المعادلة المتكيفة."""
        self.id = equation_id or f"adaptive_eq_{uuid.uuid4()}"
        self.components = []  # مكونات المعادلة
        self.adaptive_matrix = BaserahAdaptiveMatrix()
        self.adaptation_context = BaserahAdaptiveContext()
        
        # معاملات التكيف
        self.sigmoid_params = {'n': 1, 'k': 1.0, 'x0': 0.0, 'alpha': 1.0}
        self.linear_params = {'beta': 1.0, 'gamma': 0.0}
        self.quantum_params = {'quantum_factor': 4}
        
        # سجل التطور
        self.evolution_history = []
        self.fitness_history = []
        self.current_fitness = 0.0
        
        # بيانات وصفية
        self.metadata = {
            'creation_date': datetime.now().isoformat(),
            'adaptation_mode': AdaptationMode.HYBRID_ADAPTATION.value,
            'evolution_direction': EvolutionDirection.OPTIMIZE.value,
            'baserah_purity': 1.0
        }
        
        print(f"✅ تم إنشاء معادلة متكيفة Baserah: {self.id}")
    
    def add_sigmoid_component(self, variable: str = 'x', **params):
        """إضافة مكون سيجمويد."""
        component = {
            'type': 'sigmoid',
            'variable': variable,
            'params': {**self.sigmoid_params, **params},
            'weight': 1.0,
            'adaptive': True
        }
        self.components.append(component)
        print(f"➕ تم إضافة مكون سيجمويد للمتغير {variable}")
    
    def add_linear_component(self, variable: str = 'x', **params):
        """إضافة مكون خطي."""
        component = {
            'type': 'linear',
            'variable': variable,
            'params': {**self.linear_params, **params},
            'weight': 1.0,
            'adaptive': True
        }
        self.components.append(component)
        print(f"➕ تم إضافة مكون خطي للمتغير {variable}")
    
    def add_quantum_component(self, variable: str = 'x', **params):
        """إضافة مكون كمي."""
        component = {
            'type': 'quantum_sigmoid',
            'variable': variable,
            'params': {**self.sigmoid_params, **self.quantum_params, **params},
            'weight': 1.0,
            'adaptive': True
        }
        self.components.append(component)
        print(f"➕ تم إضافة مكون كمي للمتغير {variable}")
    
    def evaluate(self, x: float) -> float:
        """تقييم المعادلة عند نقطة معينة."""
        total_value = 0.0
        
        for component in self.components:
            if component['type'] == 'sigmoid':
                params = component['params']
                value = params['alpha'] / (1 + np.exp(-params['k'] * (x - params['x0'])**params['n']))
                total_value += component['weight'] * value
                
            elif component['type'] == 'linear':
                params = component['params']
                value = params['beta'] * x + params['gamma']
                total_value += component['weight'] * value
                
            elif component['type'] == 'quantum_sigmoid':
                params = component['params']
                sigmoid_value = params['alpha'] / (1 + np.exp(-params['k'] * (x - params['x0'])**params['n']))
                quantum_factor = params['quantum_factor']
                if quantum_factor > 0:
                    value = round(sigmoid_value * quantum_factor) / quantum_factor
                else:
                    value = sigmoid_value
                total_value += component['weight'] * value
        
        return total_value
    
    def adapt_to_data(self, x_data: List[float], y_data: List[float]) -> Dict[str, Any]:
        """تكيف المعادلة مع البيانات."""
        if len(x_data) != len(y_data):
            raise ValueError("أطوال البيانات غير متطابقة")
        
        print(f"🔄 بدء تكيف المعادلة {self.id} مع {len(x_data)} نقطة بيانات")
        
        adaptation_results = {
            'initial_error': 0.0,
            'final_error': 0.0,
            'iterations': 0,
            'success': False,
            'adaptations_made': []
        }
        
        # حساب الخطأ الأولي
        initial_errors = []
        for x, y_target in zip(x_data, y_data):
            y_pred = self.evaluate(x)
            error = abs(y_target - y_pred)
            initial_errors.append(error)
        
        adaptation_results['initial_error'] = np.mean(initial_errors)
        
        # عملية التكيف
        for iteration in range(self.adaptation_context.max_iterations):
            total_error = 0.0
            adaptations_this_iteration = []
            
            for x, y_target in zip(x_data, y_data):
                y_pred = self.evaluate(x)
                error = y_target - y_pred
                total_error += abs(error)
                
                # تكيف المكونات
                if abs(error) > self.adaptation_context.convergence_threshold:
                    adaptation = self._adapt_components(x, error)
                    adaptations_this_iteration.extend(adaptation)
            
            avg_error = total_error / len(x_data)
            self.fitness_history.append(1.0 / (1.0 + avg_error))  # لياقة عكسية للخطأ
            
            # تحديث المصفوفة التكيفية
            inputs = np.array(x_data[:self.adaptive_matrix.size])
            self.adaptive_matrix.adapt(avg_error, inputs)
            
            # فحص التقارب
            if avg_error < self.adaptation_context.convergence_threshold:
                adaptation_results['success'] = True
                break
            
            adaptation_results['adaptations_made'].extend(adaptations_this_iteration)
            adaptation_results['iterations'] = iteration + 1
        
        # حساب الخطأ النهائي
        final_errors = []
        for x, y_target in zip(x_data, y_data):
            y_pred = self.evaluate(x)
            error = abs(y_target - y_pred)
            final_errors.append(error)
        
        adaptation_results['final_error'] = np.mean(final_errors)
        self.current_fitness = 1.0 / (1.0 + adaptation_results['final_error'])
        
        # تسجيل التطور
        self.evolution_history.append({
            'timestamp': datetime.now().isoformat(),
            'adaptation_results': adaptation_results,
            'fitness': self.current_fitness
        })
        
        print(f"✅ انتهى التكيف: خطأ أولي={adaptation_results['initial_error']:.6f}, "
              f"خطأ نهائي={adaptation_results['final_error']:.6f}, "
              f"تكرارات={adaptation_results['iterations']}")
        
        return adaptation_results
    
    def _adapt_components(self, x: float, error: float) -> List[Dict[str, Any]]:
        """تكيف مكونات المعادلة."""
        adaptations = []
        
        for i, component in enumerate(self.components):
            if not component['adaptive']:
                continue
            
            adaptation_info = {
                'component_index': i,
                'component_type': component['type'],
                'old_params': component['params'].copy(),
                'adaptations_applied': []
            }
            
            if component['type'] == 'sigmoid':
                # تكيف معاملات السيجمويد
                if abs(error) > 0.1:
                    # تعديل k (الانحدار)
                    component['params']['k'] += error * self.adaptation_context.learning_rate
                    component['params']['k'] = max(0.1, min(10.0, component['params']['k']))
                    adaptation_info['adaptations_applied'].append('k_adjustment')
                    
                    # تعديل x0 (الإزاحة)
                    component['params']['x0'] += error * self.adaptation_context.learning_rate * 0.5
                    adaptation_info['adaptations_applied'].append('x0_adjustment')
                    
                    # تعديل alpha (المقياس)
                    component['params']['alpha'] += error * self.adaptation_context.learning_rate * 0.3
                    component['params']['alpha'] = max(0.1, component['params']['alpha'])
                    adaptation_info['adaptations_applied'].append('alpha_adjustment')
            
            elif component['type'] == 'linear':
                # تكيف معاملات الخط المستقيم
                component['params']['beta'] += error * self.adaptation_context.learning_rate
                component['params']['gamma'] += error * self.adaptation_context.learning_rate * 0.5
                adaptation_info['adaptations_applied'].extend(['beta_adjustment', 'gamma_adjustment'])
            
            elif component['type'] == 'quantum_sigmoid':
                # تكيف معاملات السيجمويد الكمي
                component['params']['k'] += error * self.adaptation_context.learning_rate
                component['params']['k'] = max(0.1, min(10.0, component['params']['k']))
                
                # تكيف عامل التكميم
                if abs(error) > 0.2:
                    if error > 0:
                        component['params']['quantum_factor'] = min(16, component['params']['quantum_factor'] + 1)
                    else:
                        component['params']['quantum_factor'] = max(2, component['params']['quantum_factor'] - 1)
                    adaptation_info['adaptations_applied'].append('quantum_factor_adjustment')
            
            # تكيف الوزن
            component['weight'] += error * self.adaptation_context.learning_rate * 0.1
            component['weight'] = max(0.1, min(2.0, component['weight']))
            adaptation_info['adaptations_applied'].append('weight_adjustment')
            
            adaptation_info['new_params'] = component['params'].copy()
            adaptations.append(adaptation_info)
        
        return adaptations
    
    def evolve(self, direction: EvolutionDirection = EvolutionDirection.OPTIMIZE) -> Dict[str, Any]:
        """تطوير المعادلة في اتجاه معين."""
        print(f"🧬 بدء تطوير المعادلة {self.id} في اتجاه {direction.value}")
        
        evolution_result = {
            'direction': direction.value,
            'changes_made': [],
            'fitness_before': self.current_fitness,
            'fitness_after': 0.0,
            'success': False
        }
        
        if direction == EvolutionDirection.OPTIMIZE:
            # تحسين المعاملات
            for component in self.components:
                if component['type'] == 'sigmoid':
                    # تحسين k للحصول على انحدار أفضل
                    old_k = component['params']['k']
                    component['params']['k'] = min(5.0, max(0.5, old_k * 1.1))
                    evolution_result['changes_made'].append(f"optimized sigmoid k: {old_k:.3f} → {component['params']['k']:.3f}")
                
                elif component['type'] == 'quantum_sigmoid':
                    # تحسين عامل التكميم
                    old_qf = component['params']['quantum_factor']
                    component['params']['quantum_factor'] = min(8, max(2, old_qf))
                    evolution_result['changes_made'].append(f"optimized quantum factor: {old_qf} → {component['params']['quantum_factor']}")
        
        elif direction == EvolutionDirection.SIMPLIFY:
            # تبسيط المعادلة
            simplified_components = []
            for component in self.components:
                if component['weight'] > 0.1:  # الاحتفاظ بالمكونات المهمة فقط
                    simplified_components.append(component)
                else:
                    evolution_result['changes_made'].append(f"removed low-weight {component['type']} component")
            
            self.components = simplified_components
        
        elif direction == EvolutionDirection.GENERALIZE:
            # تعميم المعادلة
            for component in self.components:
                if component['type'] == 'sigmoid':
                    # زيادة مرونة السيجمويد
                    component['params']['n'] = min(3, component['params']['n'] + 0.5)
                    evolution_result['changes_made'].append(f"generalized sigmoid n to {component['params']['n']}")
        
        # تحديث اللياقة
        evolution_result['fitness_after'] = self.current_fitness
        evolution_result['success'] = len(evolution_result['changes_made']) > 0
        
        # تسجيل التطور
        self.evolution_history.append({
            'timestamp': datetime.now().isoformat(),
            'evolution_type': 'directed_evolution',
            'direction': direction.value,
            'result': evolution_result
        })
        
        print(f"✅ انتهى التطوير: {len(evolution_result['changes_made'])} تغيير")
        
        return evolution_result
    
    def get_equation_string(self) -> str:
        """الحصول على تمثيل نصي للمعادلة."""
        if not self.components:
            return "f(x) = 0"
        
        terms = []
        for component in self.components:
            if component['type'] == 'sigmoid':
                params = component['params']
                term = f"sigmoid(n={params['n']}, k={params['k']:.3f}, x0={params['x0']:.3f}, α={params['alpha']:.3f})"
                if component['weight'] != 1.0:
                    term = f"{component['weight']:.3f}*{term}"
                terms.append(term)
                
            elif component['type'] == 'linear':
                params = component['params']
                term = f"linear({params['beta']:.3f}*x + {params['gamma']:.3f})"
                if component['weight'] != 1.0:
                    term = f"{component['weight']:.3f}*{term}"
                terms.append(term)
                
            elif component['type'] == 'quantum_sigmoid':
                params = component['params']
                term = f"quantum_sigmoid(Q={params['quantum_factor']}, k={params['k']:.3f}, α={params['alpha']:.3f})"
                if component['weight'] != 1.0:
                    term = f"{component['weight']:.3f}*{term}"
                terms.append(term)
        
        return f"f(x) = {' + '.join(terms)}"
    
    def get_adaptation_summary(self) -> Dict[str, Any]:
        """الحصول على ملخص التكيف."""
        matrix_summary = self.adaptive_matrix.get_adaptation_summary()
        
        return {
            'equation_id': self.id,
            'total_components': len(self.components),
            'component_types': [c['type'] for c in self.components],
            'current_fitness': self.current_fitness,
            'total_evolutions': len(self.evolution_history),
            'adaptation_mode': self.metadata['adaptation_mode'],
            'baserah_purity': self.metadata['baserah_purity'],
            'adaptive_matrix_summary': matrix_summary,
            'equation_string': self.get_equation_string()
        }
