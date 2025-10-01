#!/usr/bin/env python3
# baserah_explorer_core.py - النواة المستكشفة Baserah النقية

import math
import random
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Union, Optional, Any, Set
from dataclasses import dataclass, field
from enum import Enum

class ExplorationMode(str, Enum):
    """أوضاع الاستكشاف Baserah."""
    RANDOM = "random"  # استكشاف عشوائي
    GUIDED = "guided"  # استكشاف موجه
    FOCUSED = "focused"  # استكشاف مركز
    DIVERGENT = "divergent"  # استكشاف متباعد
    CONVERGENT = "convergent"  # استكشاف متقارب
    SIGMOID_EXPLORATION = "sigmoid_exploration"  # استكشاف سيجمويدي
    LINEAR_EXPLORATION = "linear_exploration"  # استكشاف خطي
    QUANTUM_EXPLORATION = "quantum_exploration"  # استكشاف كمي

@dataclass
class BaserahEquation:
    """معادلة Baserah النقية."""
    id: str = field(default_factory=lambda: f"eq_{uuid.uuid4()}")
    equation_type: str = "baserah"  # نوع المعادلة
    components: List[Dict[str, Any]] = field(default_factory=list)  # مكونات المعادلة
    complexity: float = 1.0  # درجة التعقيد
    fitness: float = 0.0  # درجة اللياقة
    variables: Set[str] = field(default_factory=set)  # المتغيرات
    metadata: Dict[str, Any] = field(default_factory=dict)
    creation_date: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class ExplorationConfig:
    """تكوين الاستكشاف Baserah."""
    mode: ExplorationMode = ExplorationMode.GUIDED
    budget: int = 100  # ميزانية الاستكشاف
    max_complexity: float = 10.0
    min_complexity: float = 1.0
    max_variables: int = 3
    min_variables: int = 1
    fitness_threshold: float = 0.7
    sigmoid_range: Tuple[float, float] = (-5.0, 5.0)
    linear_range: Tuple[float, float] = (-10.0, 10.0)
    quantum_factors: List[int] = field(default_factory=lambda: [1, 2, 4, 8])
    custom_properties: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ExplorationResult:
    """نتيجة الاستكشاف Baserah."""
    discovered_equations: List[BaserahEquation] = field(default_factory=list)
    fitness_scores: Dict[str, float] = field(default_factory=dict)
    exploration_path: List[str] = field(default_factory=list)
    patterns_discovered: List[Dict[str, Any]] = field(default_factory=list)
    statistics: Dict[str, Any] = field(default_factory=dict)
    success: bool = False
    message: str = ""
    baserah_score: float = 0.0

class BaserahEquationGenerator:
    """مولد المعادلات Baserah النقي."""
    
    def __init__(self):
        """تهيئة مولد المعادلات."""
        self.variable_names = ['x', 'y', 'z', 't', 'u', 'v']
        self.generation_count = 0
    
    def baserah_sigmoid(self, x: float, n: int, k: float, x0: float, alpha: float) -> float:
        """دالة السيجمويد Baserah النقية."""
        try:
            exponent = -k * ((x - x0) ** n)
            if exponent > 700:
                return 0.0
            elif exponent < -700:
                return alpha
            return alpha / (1 + math.exp(exponent))
        except (OverflowError, ZeroDivisionError):
            return alpha / 2
    
    def baserah_linear(self, x: float, beta: float, gamma: float) -> float:
        """دالة الخط المستقيم Baserah النقية."""
        return beta * x + gamma
    
    def baserah_quantum_sigmoid(self, x: float, n: int, k: float, x0: float, alpha: float, quantum_factor: int) -> float:
        """دالة السيجمويد المكممة Baserah النقية."""
        if quantum_factor <= 1:
            return self.baserah_sigmoid(x, n, k, x0, alpha)
        
        # حساب السيجمويد العادي
        sigmoid_val = self.baserah_sigmoid(x, n, k, x0, alpha)
        
        # تطبيق التكميم
        step_size = alpha / quantum_factor
        quantized = round(sigmoid_val / step_size) * step_size
        return max(0.0, min(alpha, quantized))
    
    def generate_random_equation(self, config: ExplorationConfig) -> BaserahEquation:
        """توليد معادلة عشوائية."""
        self.generation_count += 1
        
        # اختيار عدد المتغيرات
        num_vars = random.randint(config.min_variables, config.max_variables)
        variables = set(random.sample(self.variable_names, num_vars))
        
        # اختيار عدد المكونات
        num_components = random.randint(1, 3)
        components = []
        
        for _ in range(num_components):
            component_type = random.choice(['sigmoid', 'linear', 'quantum_sigmoid'])
            
            if component_type == 'sigmoid':
                component = {
                    'type': 'sigmoid',
                    'params': {
                        'n': random.randint(1, 3),
                        'k': random.uniform(0.1, 5.0),
                        'x0': random.uniform(*config.sigmoid_range),
                        'alpha': random.uniform(0.1, 2.0)
                    },
                    'variable': random.choice(list(variables))
                }
            elif component_type == 'linear':
                component = {
                    'type': 'linear',
                    'params': {
                        'beta': random.uniform(*config.linear_range),
                        'gamma': random.uniform(*config.linear_range)
                    },
                    'variable': random.choice(list(variables))
                }
            else:  # quantum_sigmoid
                component = {
                    'type': 'quantum_sigmoid',
                    'params': {
                        'n': random.randint(1, 2),
                        'k': random.uniform(0.5, 3.0),
                        'x0': random.uniform(*config.sigmoid_range),
                        'alpha': random.uniform(0.5, 1.5),
                        'quantum_factor': random.choice(config.quantum_factors)
                    },
                    'variable': random.choice(list(variables))
                }
            
            components.append(component)
        
        # حساب التعقيد
        complexity = self._calculate_complexity(components)
        
        equation = BaserahEquation(
            equation_type="baserah_generated",
            components=components,
            complexity=complexity,
            variables=variables,
            metadata={
                'generation_method': 'random',
                'generation_count': self.generation_count,
                'config_mode': config.mode
            }
        )
        
        return equation
    
    def generate_guided_equation(self, config: ExplorationConfig, guide_equation: Optional[BaserahEquation] = None) -> BaserahEquation:
        """توليد معادلة موجهة."""
        if guide_equation is None:
            return self.generate_random_equation(config)
        
        # نسخ المعادلة الموجهة وتعديلها
        new_components = []
        
        for component in guide_equation.components:
            new_component = component.copy()
            
            # تعديل المعاملات قليلاً
            if component['type'] == 'sigmoid':
                params = new_component['params']
                params['k'] *= random.uniform(0.8, 1.2)
                params['x0'] += random.uniform(-0.5, 0.5)
                params['alpha'] *= random.uniform(0.9, 1.1)
            elif component['type'] == 'linear':
                params = new_component['params']
                params['beta'] *= random.uniform(0.8, 1.2)
                params['gamma'] += random.uniform(-0.5, 0.5)
            elif component['type'] == 'quantum_sigmoid':
                params = new_component['params']
                params['k'] *= random.uniform(0.8, 1.2)
                params['x0'] += random.uniform(-0.5, 0.5)
                # أحياناً تغيير عامل التكميم
                if random.random() < 0.3:
                    params['quantum_factor'] = random.choice(config.quantum_factors)
            
            new_components.append(new_component)
        
        # أحياناً إضافة مكون جديد
        if random.random() < 0.3 and len(new_components) < 3:
            new_component = self._generate_random_component(config, guide_equation.variables)
            new_components.append(new_component)
        
        complexity = self._calculate_complexity(new_components)
        
        equation = BaserahEquation(
            equation_type="baserah_guided",
            components=new_components,
            complexity=complexity,
            variables=guide_equation.variables.copy(),
            metadata={
                'generation_method': 'guided',
                'guide_equation_id': guide_equation.id,
                'generation_count': self.generation_count
            }
        )
        
        return equation
    
    def _generate_random_component(self, config: ExplorationConfig, variables: Set[str]) -> Dict[str, Any]:
        """توليد مكون عشوائي."""
        component_type = random.choice(['sigmoid', 'linear', 'quantum_sigmoid'])
        
        if component_type == 'sigmoid':
            return {
                'type': 'sigmoid',
                'params': {
                    'n': random.randint(1, 3),
                    'k': random.uniform(0.1, 5.0),
                    'x0': random.uniform(*config.sigmoid_range),
                    'alpha': random.uniform(0.1, 2.0)
                },
                'variable': random.choice(list(variables))
            }
        elif component_type == 'linear':
            return {
                'type': 'linear',
                'params': {
                    'beta': random.uniform(*config.linear_range),
                    'gamma': random.uniform(*config.linear_range)
                },
                'variable': random.choice(list(variables))
            }
        else:  # quantum_sigmoid
            return {
                'type': 'quantum_sigmoid',
                'params': {
                    'n': random.randint(1, 2),
                    'k': random.uniform(0.5, 3.0),
                    'x0': random.uniform(*config.sigmoid_range),
                    'alpha': random.uniform(0.5, 1.5),
                    'quantum_factor': random.choice(config.quantum_factors)
                },
                'variable': random.choice(list(variables))
            }
    
    def _calculate_complexity(self, components: List[Dict[str, Any]]) -> float:
        """حساب تعقيد المعادلة."""
        complexity = 0.0
        
        for component in components:
            if component['type'] == 'sigmoid':
                complexity += 2.0  # السيجمويد معقد نسبياً
                if component['params']['n'] > 1:
                    complexity += 0.5 * component['params']['n']
            elif component['type'] == 'linear':
                complexity += 1.0  # الخط المستقيم بسيط
            elif component['type'] == 'quantum_sigmoid':
                complexity += 3.0  # السيجمويد المكمم أكثر تعقيداً
                complexity += 0.1 * component['params']['quantum_factor']
        
        return complexity
    
    def evaluate_equation(self, equation: BaserahEquation, test_points: List[float]) -> float:
        """تقييم المعادلة على نقاط اختبار."""
        if not test_points:
            return 0.0
        
        total_score = 0.0
        valid_points = 0
        
        for x in test_points:
            try:
                result = self._evaluate_at_point(equation, x)
                if not math.isnan(result) and not math.isinf(result):
                    # تقييم بناءً على خصائص مرغوبة
                    score = self._calculate_point_score(result, x)
                    total_score += score
                    valid_points += 1
            except:
                continue
        
        if valid_points == 0:
            return 0.0
        
        return total_score / valid_points
    
    def _evaluate_at_point(self, equation: BaserahEquation, x: float) -> float:
        """تقييم المعادلة عند نقطة معينة."""
        result = 0.0
        
        for component in equation.components:
            if component['type'] == 'sigmoid':
                params = component['params']
                value = self.baserah_sigmoid(x, **params)
            elif component['type'] == 'linear':
                params = component['params']
                value = self.baserah_linear(x, **params)
            elif component['type'] == 'quantum_sigmoid':
                params = component['params']
                value = self.baserah_quantum_sigmoid(x, **params)
            else:
                value = 0.0
            
            result += value
        
        return result
    
    def _calculate_point_score(self, result: float, x: float) -> float:
        """حساب نقاط النقطة."""
        # تفضيل النتائج المحدودة والمعقولة
        if abs(result) > 100:
            return 0.1
        
        # تفضيل التنوع في النتائج
        score = 1.0
        
        # مكافأة للنتائج في نطاق معقول
        if 0 <= abs(result) <= 10:
            score += 0.5
        
        # مكافأة للسلوك السلس
        if abs(result) < 1:
            score += 0.3
        
        return min(score, 2.0)

class BaserahExplorerCore:
    """
    النواة المستكشفة Baserah النقية
    نظام استكشاف يعمل بمنهج Baserah فقط (سيجمويد + خطي + تكميم)
    """

    def __init__(self):
        """تهيئة النواة المستكشفة Baserah."""
        self.equation_generator = BaserahEquationGenerator()
        self.discovered_equations: List[BaserahEquation] = []
        self.exploration_history: List[Dict[str, Any]] = []
        self.pattern_database: List[Dict[str, Any]] = []

        # إحصائيات الاستكشاف
        self.exploration_count = 0
        self.successful_explorations = 0
        self.total_equations_discovered = 0

        print("🔍 تم تهيئة النواة المستكشفة Baserah النقية")

    def explore(self, config: ExplorationConfig) -> ExplorationResult:
        """تنفيذ عملية الاستكشاف Baserah."""
        self.exploration_count += 1

        print(f"🚀 بدء الاستكشاف Baserah #{self.exploration_count} بوضع {config.mode}")

        if config.mode == ExplorationMode.RANDOM:
            result = self._random_exploration(config)
        elif config.mode == ExplorationMode.GUIDED:
            result = self._guided_exploration(config)
        elif config.mode == ExplorationMode.FOCUSED:
            result = self._focused_exploration(config)
        elif config.mode == ExplorationMode.DIVERGENT:
            result = self._divergent_exploration(config)
        elif config.mode == ExplorationMode.CONVERGENT:
            result = self._convergent_exploration(config)
        elif config.mode == ExplorationMode.SIGMOID_EXPLORATION:
            result = self._sigmoid_exploration(config)
        elif config.mode == ExplorationMode.LINEAR_EXPLORATION:
            result = self._linear_exploration(config)
        elif config.mode == ExplorationMode.QUANTUM_EXPLORATION:
            result = self._quantum_exploration(config)
        else:
            result = ExplorationResult(
                success=False,
                message=f"وضع استكشاف غير معروف: {config.mode}"
            )

        # تحديث الإحصائيات
        if result.success:
            self.successful_explorations += 1
            self.total_equations_discovered += len(result.discovered_equations)
            self.discovered_equations.extend(result.discovered_equations)

        # تسجيل الاستكشاف
        self.exploration_history.append({
            'timestamp': datetime.now().isoformat(),
            'mode': config.mode,
            'success': result.success,
            'equations_discovered': len(result.discovered_equations),
            'baserah_score': result.baserah_score
        })

        print(f"✅ اكتمل الاستكشاف. النجاح: {result.success}, المعادلات: {len(result.discovered_equations)}")
        return result

    def _random_exploration(self, config: ExplorationConfig) -> ExplorationResult:
        """الاستكشاف العشوائي Baserah."""
        discovered_equations = []
        fitness_scores = {}
        exploration_path = []

        test_points = [x * 0.1 for x in range(-50, 51)]  # نقاط اختبار من -5 إلى 5

        for i in range(config.budget):
            equation = self.equation_generator.generate_random_equation(config)
            fitness = self.equation_generator.evaluate_equation(equation, test_points)

            equation.fitness = fitness
            fitness_scores[equation.id] = fitness
            exploration_path.append(equation.id)

            if fitness >= config.fitness_threshold:
                discovered_equations.append(equation)

        success = bool(discovered_equations)
        avg_fitness = sum(fitness_scores.values()) / max(1, len(fitness_scores))

        return ExplorationResult(
            discovered_equations=discovered_equations,
            fitness_scores=fitness_scores,
            exploration_path=exploration_path,
            success=success,
            message=f"استكشاف عشوائي: {len(discovered_equations)} معادلات مكتشفة",
            baserah_score=avg_fitness * len(discovered_equations),
            statistics={
                'total_generated': config.budget,
                'successful_equations': len(discovered_equations),
                'average_fitness': avg_fitness
            }
        )

    def _guided_exploration(self, config: ExplorationConfig) -> ExplorationResult:
        """الاستكشاف الموجه Baserah."""
        discovered_equations = []
        fitness_scores = {}
        exploration_path = []

        test_points = [x * 0.1 for x in range(-50, 51)]

        # البدء بمعادلة عشوائية
        guide_equation = self.equation_generator.generate_random_equation(config)
        guide_fitness = self.equation_generator.evaluate_equation(guide_equation, test_points)

        best_equation = guide_equation
        best_fitness = guide_fitness

        for i in range(config.budget):
            if i % 10 == 0 and self.discovered_equations:
                # أحياناً استخدام معادلة مكتشفة سابقاً كدليل
                guide_equation = random.choice(self.discovered_equations)

            equation = self.equation_generator.generate_guided_equation(config, guide_equation)
            fitness = self.equation_generator.evaluate_equation(equation, test_points)

            equation.fitness = fitness
            fitness_scores[equation.id] = fitness
            exploration_path.append(equation.id)

            if fitness >= config.fitness_threshold:
                discovered_equations.append(equation)

            # تحديث الدليل إذا وجدنا معادلة أفضل
            if fitness > best_fitness:
                best_equation = equation
                best_fitness = fitness
                guide_equation = equation

        success = bool(discovered_equations)
        avg_fitness = sum(fitness_scores.values()) / max(1, len(fitness_scores))

        return ExplorationResult(
            discovered_equations=discovered_equations,
            fitness_scores=fitness_scores,
            exploration_path=exploration_path,
            success=success,
            message=f"استكشاف موجه: {len(discovered_equations)} معادلات مكتشفة",
            baserah_score=avg_fitness * len(discovered_equations),
            statistics={
                'total_generated': config.budget,
                'successful_equations': len(discovered_equations),
                'average_fitness': avg_fitness,
                'best_fitness': best_fitness
            }
        )

    def _focused_exploration(self, config: ExplorationConfig) -> ExplorationResult:
        """الاستكشاف المركز Baserah."""
        # التركيز على نوع واحد من المكونات
        component_types = ['sigmoid', 'linear', 'quantum_sigmoid']
        focus_type = random.choice(component_types)

        discovered_equations = []
        fitness_scores = {}
        exploration_path = []

        test_points = [x * 0.1 for x in range(-50, 51)]

        for i in range(config.budget):
            equation = self._generate_focused_equation(config, focus_type)
            fitness = self.equation_generator.evaluate_equation(equation, test_points)

            equation.fitness = fitness
            fitness_scores[equation.id] = fitness
            exploration_path.append(equation.id)

            if fitness >= config.fitness_threshold:
                discovered_equations.append(equation)

        success = bool(discovered_equations)
        avg_fitness = sum(fitness_scores.values()) / max(1, len(fitness_scores))

        return ExplorationResult(
            discovered_equations=discovered_equations,
            fitness_scores=fitness_scores,
            exploration_path=exploration_path,
            success=success,
            message=f"استكشاف مركز ({focus_type}): {len(discovered_equations)} معادلات",
            baserah_score=avg_fitness * len(discovered_equations),
            statistics={
                'focus_type': focus_type,
                'total_generated': config.budget,
                'successful_equations': len(discovered_equations),
                'average_fitness': avg_fitness
            }
        )

    def _divergent_exploration(self, config: ExplorationConfig) -> ExplorationResult:
        """الاستكشاف المتباعد Baserah."""
        # استكشاف متنوع بمعاملات متباعدة
        discovered_equations = []
        fitness_scores = {}
        exploration_path = []

        test_points = [x * 0.1 for x in range(-50, 51)]

        # توسيع نطاقات المعاملات
        expanded_config = ExplorationConfig(
            mode=config.mode,
            budget=config.budget,
            sigmoid_range=(-10.0, 10.0),  # نطاق أوسع
            linear_range=(-20.0, 20.0),   # نطاق أوسع
            quantum_factors=[1, 2, 4, 8, 16, 32],  # عوامل تكميم أكثر
            max_complexity=config.max_complexity * 2
        )

        for i in range(config.budget):
            equation = self.equation_generator.generate_random_equation(expanded_config)
            fitness = self.equation_generator.evaluate_equation(equation, test_points)

            equation.fitness = fitness
            fitness_scores[equation.id] = fitness
            exploration_path.append(equation.id)

            if fitness >= config.fitness_threshold:
                discovered_equations.append(equation)

        success = bool(discovered_equations)
        avg_fitness = sum(fitness_scores.values()) / max(1, len(fitness_scores))

        return ExplorationResult(
            discovered_equations=discovered_equations,
            fitness_scores=fitness_scores,
            exploration_path=exploration_path,
            success=success,
            message=f"استكشاف متباعد: {len(discovered_equations)} معادلات مكتشفة",
            baserah_score=avg_fitness * len(discovered_equations),
            statistics={
                'exploration_type': 'divergent',
                'expanded_ranges': True,
                'total_generated': config.budget,
                'successful_equations': len(discovered_equations),
                'average_fitness': avg_fitness
            }
        )

    def _convergent_exploration(self, config: ExplorationConfig) -> ExplorationResult:
        """الاستكشاف المتقارب Baserah."""
        # التقارب نحو معادلات بسيطة وفعالة
        discovered_equations = []
        fitness_scores = {}
        exploration_path = []

        test_points = [x * 0.1 for x in range(-50, 51)]

        # تضييق نطاقات المعاملات
        focused_config = ExplorationConfig(
            mode=config.mode,
            budget=config.budget,
            sigmoid_range=(-2.0, 2.0),  # نطاق أضيق
            linear_range=(-5.0, 5.0),   # نطاق أضيق
            quantum_factors=[1, 2, 4],  # عوامل تكميم أقل
            max_complexity=config.max_complexity * 0.5,
            max_variables=2  # متغيرات أقل
        )

        for i in range(config.budget):
            equation = self.equation_generator.generate_random_equation(focused_config)
            fitness = self.equation_generator.evaluate_equation(equation, test_points)

            # مكافأة إضافية للبساطة
            simplicity_bonus = 1.0 / (equation.complexity + 1)
            adjusted_fitness = fitness + simplicity_bonus * 0.2

            equation.fitness = adjusted_fitness
            fitness_scores[equation.id] = adjusted_fitness
            exploration_path.append(equation.id)

            if adjusted_fitness >= config.fitness_threshold:
                discovered_equations.append(equation)

        success = bool(discovered_equations)
        avg_fitness = sum(fitness_scores.values()) / max(1, len(fitness_scores))

        return ExplorationResult(
            discovered_equations=discovered_equations,
            fitness_scores=fitness_scores,
            exploration_path=exploration_path,
            success=success,
            message=f"استكشاف متقارب: {len(discovered_equations)} معادلات بسيطة",
            baserah_score=avg_fitness * len(discovered_equations),
            statistics={
                'exploration_type': 'convergent',
                'focused_ranges': True,
                'simplicity_bonus': True,
                'total_generated': config.budget,
                'successful_equations': len(discovered_equations),
                'average_fitness': avg_fitness
            }
        )

    def _sigmoid_exploration(self, config: ExplorationConfig) -> ExplorationResult:
        """الاستكشاف السيجمويدي Baserah."""
        # التركيز على معادلات السيجمويد فقط
        discovered_equations = []
        fitness_scores = {}
        exploration_path = []

        test_points = [x * 0.1 for x in range(-50, 51)]

        for i in range(config.budget):
            equation = self._generate_sigmoid_only_equation(config)
            fitness = self.equation_generator.evaluate_equation(equation, test_points)

            equation.fitness = fitness
            fitness_scores[equation.id] = fitness
            exploration_path.append(equation.id)

            if fitness >= config.fitness_threshold:
                discovered_equations.append(equation)

        success = bool(discovered_equations)
        avg_fitness = sum(fitness_scores.values()) / max(1, len(fitness_scores))

        return ExplorationResult(
            discovered_equations=discovered_equations,
            fitness_scores=fitness_scores,
            exploration_path=exploration_path,
            success=success,
            message=f"استكشاف سيجمويدي: {len(discovered_equations)} معادلات سيجمويد",
            baserah_score=avg_fitness * len(discovered_equations),
            statistics={
                'exploration_type': 'sigmoid_only',
                'total_generated': config.budget,
                'successful_equations': len(discovered_equations),
                'average_fitness': avg_fitness
            }
        )

    def _linear_exploration(self, config: ExplorationConfig) -> ExplorationResult:
        """الاستكشاف الخطي Baserah."""
        # التركيز على المعادلات الخطية فقط
        discovered_equations = []
        fitness_scores = {}
        exploration_path = []

        test_points = [x * 0.1 for x in range(-50, 51)]

        for i in range(config.budget):
            equation = self._generate_linear_only_equation(config)
            fitness = self.equation_generator.evaluate_equation(equation, test_points)

            equation.fitness = fitness
            fitness_scores[equation.id] = fitness
            exploration_path.append(equation.id)

            if fitness >= config.fitness_threshold:
                discovered_equations.append(equation)

        success = bool(discovered_equations)
        avg_fitness = sum(fitness_scores.values()) / max(1, len(fitness_scores))

        return ExplorationResult(
            discovered_equations=discovered_equations,
            fitness_scores=fitness_scores,
            exploration_path=exploration_path,
            success=success,
            message=f"استكشاف خطي: {len(discovered_equations)} معادلات خطية",
            baserah_score=avg_fitness * len(discovered_equations),
            statistics={
                'exploration_type': 'linear_only',
                'total_generated': config.budget,
                'successful_equations': len(discovered_equations),
                'average_fitness': avg_fitness
            }
        )

    def _quantum_exploration(self, config: ExplorationConfig) -> ExplorationResult:
        """الاستكشاف الكمي Baserah."""
        # التركيز على المعادلات المكممة فقط
        discovered_equations = []
        fitness_scores = {}
        exploration_path = []

        test_points = [x * 0.1 for x in range(-50, 51)]

        for i in range(config.budget):
            equation = self._generate_quantum_only_equation(config)
            fitness = self.equation_generator.evaluate_equation(equation, test_points)

            equation.fitness = fitness
            fitness_scores[equation.id] = fitness
            exploration_path.append(equation.id)

            if fitness >= config.fitness_threshold:
                discovered_equations.append(equation)

        success = bool(discovered_equations)
        avg_fitness = sum(fitness_scores.values()) / max(1, len(fitness_scores))

        return ExplorationResult(
            discovered_equations=discovered_equations,
            fitness_scores=fitness_scores,
            exploration_path=exploration_path,
            success=success,
            message=f"استكشاف كمي: {len(discovered_equations)} معادلات مكممة",
            baserah_score=avg_fitness * len(discovered_equations),
            statistics={
                'exploration_type': 'quantum_only',
                'total_generated': config.budget,
                'successful_equations': len(discovered_equations),
                'average_fitness': avg_fitness
            }
        )

    def _generate_focused_equation(self, config: ExplorationConfig, focus_type: str) -> BaserahEquation:
        """توليد معادلة مركزة على نوع معين."""
        variables = {'x'}  # متغير واحد للتركيز

        if focus_type == 'sigmoid':
            components = [{
                'type': 'sigmoid',
                'params': {
                    'n': random.randint(1, 3),
                    'k': random.uniform(0.1, 5.0),
                    'x0': random.uniform(*config.sigmoid_range),
                    'alpha': random.uniform(0.1, 2.0)
                },
                'variable': 'x'
            }]
        elif focus_type == 'linear':
            components = [{
                'type': 'linear',
                'params': {
                    'beta': random.uniform(*config.linear_range),
                    'gamma': random.uniform(*config.linear_range)
                },
                'variable': 'x'
            }]
        else:  # quantum_sigmoid
            components = [{
                'type': 'quantum_sigmoid',
                'params': {
                    'n': random.randint(1, 2),
                    'k': random.uniform(0.5, 3.0),
                    'x0': random.uniform(*config.sigmoid_range),
                    'alpha': random.uniform(0.5, 1.5),
                    'quantum_factor': random.choice(config.quantum_factors)
                },
                'variable': 'x'
            }]

        complexity = self.equation_generator._calculate_complexity(components)

        return BaserahEquation(
            equation_type=f"baserah_{focus_type}_focused",
            components=components,
            complexity=complexity,
            variables=variables,
            metadata={'focus_type': focus_type}
        )

    def _generate_sigmoid_only_equation(self, config: ExplorationConfig) -> BaserahEquation:
        """توليد معادلة سيجمويد فقط."""
        num_components = random.randint(1, 3)
        variables = {'x'}
        components = []

        for _ in range(num_components):
            components.append({
                'type': 'sigmoid',
                'params': {
                    'n': random.randint(1, 3),
                    'k': random.uniform(0.1, 5.0),
                    'x0': random.uniform(*config.sigmoid_range),
                    'alpha': random.uniform(0.1, 2.0)
                },
                'variable': 'x'
            })

        complexity = self.equation_generator._calculate_complexity(components)

        return BaserahEquation(
            equation_type="baserah_sigmoid_only",
            components=components,
            complexity=complexity,
            variables=variables,
            metadata={'type_restriction': 'sigmoid_only'}
        )

    def _generate_linear_only_equation(self, config: ExplorationConfig) -> BaserahEquation:
        """توليد معادلة خطية فقط."""
        num_components = random.randint(1, 3)
        variables = {'x'}
        components = []

        for _ in range(num_components):
            components.append({
                'type': 'linear',
                'params': {
                    'beta': random.uniform(*config.linear_range),
                    'gamma': random.uniform(*config.linear_range)
                },
                'variable': 'x'
            })

        complexity = self.equation_generator._calculate_complexity(components)

        return BaserahEquation(
            equation_type="baserah_linear_only",
            components=components,
            complexity=complexity,
            variables=variables,
            metadata={'type_restriction': 'linear_only'}
        )

    def _generate_quantum_only_equation(self, config: ExplorationConfig) -> BaserahEquation:
        """توليد معادلة مكممة فقط."""
        num_components = random.randint(1, 2)
        variables = {'x'}
        components = []

        for _ in range(num_components):
            components.append({
                'type': 'quantum_sigmoid',
                'params': {
                    'n': random.randint(1, 2),
                    'k': random.uniform(0.5, 3.0),
                    'x0': random.uniform(*config.sigmoid_range),
                    'alpha': random.uniform(0.5, 1.5),
                    'quantum_factor': random.choice(config.quantum_factors)
                },
                'variable': 'x'
            })

        complexity = self.equation_generator._calculate_complexity(components)

        return BaserahEquation(
            equation_type="baserah_quantum_only",
            components=components,
            complexity=complexity,
            variables=variables,
            metadata={'type_restriction': 'quantum_only'}
        )

    def discover_patterns(self, equations: List[BaserahEquation]) -> List[Dict[str, Any]]:
        """اكتشاف الأنماط في المعادلات."""
        if not equations:
            return []

        patterns = []

        # نمط التعقيد
        complexities = [eq.complexity for eq in equations]
        avg_complexity = sum(complexities) / len(complexities)

        patterns.append({
            'type': 'complexity_pattern',
            'description': f'متوسط التعقيد: {avg_complexity:.2f}',
            'data': {
                'average_complexity': avg_complexity,
                'min_complexity': min(complexities),
                'max_complexity': max(complexities),
                'complexity_range': max(complexities) - min(complexities)
            }
        })

        # نمط أنواع المكونات
        component_types = {}
        for eq in equations:
            for comp in eq.components:
                comp_type = comp['type']
                component_types[comp_type] = component_types.get(comp_type, 0) + 1

        patterns.append({
            'type': 'component_type_pattern',
            'description': f'توزيع أنواع المكونات: {component_types}',
            'data': component_types
        })

        # نمط اللياقة
        fitness_scores = [eq.fitness for eq in equations if eq.fitness > 0]
        if fitness_scores:
            avg_fitness = sum(fitness_scores) / len(fitness_scores)
            patterns.append({
                'type': 'fitness_pattern',
                'description': f'متوسط اللياقة: {avg_fitness:.3f}',
                'data': {
                    'average_fitness': avg_fitness,
                    'min_fitness': min(fitness_scores),
                    'max_fitness': max(fitness_scores),
                    'high_fitness_count': len([f for f in fitness_scores if f > 0.8])
                }
            })

        # نمط عوامل التكميم
        quantum_factors = []
        for eq in equations:
            for comp in eq.components:
                if comp['type'] == 'quantum_sigmoid':
                    quantum_factors.append(comp['params']['quantum_factor'])

        if quantum_factors:
            from collections import Counter
            qf_distribution = Counter(quantum_factors)
            patterns.append({
                'type': 'quantum_factor_pattern',
                'description': f'توزيع عوامل التكميم: {dict(qf_distribution)}',
                'data': dict(qf_distribution)
            })

        return patterns

    def get_best_equations(self, top_n: int = 10) -> List[BaserahEquation]:
        """الحصول على أفضل المعادلات المكتشفة."""
        sorted_equations = sorted(self.discovered_equations,
                                key=lambda eq: eq.fitness, reverse=True)
        return sorted_equations[:top_n]

    def get_statistics(self) -> Dict[str, Any]:
        """الحصول على إحصائيات الاستكشاف."""
        success_rate = self.successful_explorations / max(1, self.exploration_count)

        if self.discovered_equations:
            avg_fitness = sum(eq.fitness for eq in self.discovered_equations) / len(self.discovered_equations)
            avg_complexity = sum(eq.complexity for eq in self.discovered_equations) / len(self.discovered_equations)
        else:
            avg_fitness = 0.0
            avg_complexity = 0.0

        return {
            'total_explorations': self.exploration_count,
            'successful_explorations': self.successful_explorations,
            'success_rate': success_rate,
            'total_equations_discovered': self.total_equations_discovered,
            'average_fitness': avg_fitness,
            'average_complexity': avg_complexity,
            'exploration_history_size': len(self.exploration_history),
            'pattern_database_size': len(self.pattern_database)
        }

    def save_discovered_equations(self, file_path: str):
        """حفظ المعادلات المكتشفة."""
        try:
            equations_data = []
            for eq in self.discovered_equations:
                eq_data = {
                    'id': eq.id,
                    'equation_type': eq.equation_type,
                    'components': eq.components,
                    'complexity': eq.complexity,
                    'fitness': eq.fitness,
                    'variables': list(eq.variables),
                    'metadata': eq.metadata,
                    'creation_date': eq.creation_date
                }
                equations_data.append(eq_data)

            import json
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(equations_data, f, ensure_ascii=False, indent=2)

            print(f"💾 تم حفظ {len(equations_data)} معادلة: {file_path}")
        except Exception as e:
            print(f"❌ خطأ في حفظ المعادلات: {e}")

    def load_discovered_equations(self, file_path: str):
        """تحميل المعادلات المكتشفة."""
        try:
            import json
            with open(file_path, 'r', encoding='utf-8') as f:
                equations_data = json.load(f)

            loaded_equations = []
            for eq_data in equations_data:
                eq = BaserahEquation(
                    id=eq_data['id'],
                    equation_type=eq_data['equation_type'],
                    components=eq_data['components'],
                    complexity=eq_data['complexity'],
                    fitness=eq_data['fitness'],
                    variables=set(eq_data['variables']),
                    metadata=eq_data['metadata'],
                    creation_date=eq_data['creation_date']
                )
                loaded_equations.append(eq)

            self.discovered_equations.extend(loaded_equations)
            print(f"📂 تم تحميل {len(loaded_equations)} معادلة")
        except Exception as e:
            print(f"❌ خطأ في تحميل المعادلات: {e}")
