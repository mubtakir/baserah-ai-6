#!/usr/bin/env python3
# adaptive_evolution_engine.py - محرك التطور التكيفي Baserah النقي

import numpy as np
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Union, Optional, Any, Callable
from dataclasses import dataclass, field
from enum import Enum
import random

from .adaptive_equations import BaserahAdaptiveEquation, AdaptationMode, EvolutionDirection, BaserahAdaptiveContext

class EvolutionStrategy(Enum):
    """استراتيجيات التطور."""
    RANDOM_MUTATION = "random_mutation"  # طفرة عشوائية
    DIRECTED_EVOLUTION = "directed_evolution"  # تطور موجه
    GRADIENT_DESCENT = "gradient_descent"  # انحدار التدرج
    QUANTUM_EVOLUTION = "quantum_evolution"  # تطور كمي
    HYBRID_EVOLUTION = "hybrid_evolution"  # تطور هجين
    REVOLUTIONARY_LEAP = "revolutionary_leap"  # قفزة ثورية

class PopulationMode(Enum):
    """أوضاع المجموعة."""
    SINGLE_EQUATION = "single_equation"  # معادلة واحدة
    SMALL_POPULATION = "small_population"  # مجموعة صغيرة
    LARGE_POPULATION = "large_population"  # مجموعة كبيرة
    ECOSYSTEM = "ecosystem"  # نظام بيئي

@dataclass
class EvolutionConfig:
    """تكوين التطور."""
    strategy: EvolutionStrategy = EvolutionStrategy.HYBRID_EVOLUTION
    population_mode: PopulationMode = PopulationMode.SMALL_POPULATION
    population_size: int = 10
    max_generations: int = 50
    mutation_rate: float = 0.3
    crossover_rate: float = 0.7
    selection_pressure: float = 0.8
    fitness_threshold: float = 0.9
    quantum_factor_range: Tuple[int, int] = (2, 16)
    baserah_weight: float = 1.0

@dataclass
class EvolutionResult:
    """نتيجة التطور."""
    best_equation: Optional[BaserahAdaptiveEquation] = None
    population: List[BaserahAdaptiveEquation] = field(default_factory=list)
    generation_count: int = 0
    best_fitness: float = 0.0
    fitness_history: List[float] = field(default_factory=list)
    evolution_log: List[Dict[str, Any]] = field(default_factory=list)
    success: bool = False
    convergence_achieved: bool = False

class BaserahAdaptiveEvolutionEngine:
    """
    محرك التطور التكيفي Baserah النقي
    يطور المعادلات باستخدام منهج Baserah فقط
    """
    
    def __init__(self, config: EvolutionConfig = None):
        """تهيئة محرك التطور."""
        self.config = config or EvolutionConfig()
        self.population: List[BaserahAdaptiveEquation] = []
        self.generation_count = 0
        self.evolution_history = []
        
        # إحصائيات
        self.total_evolutions = 0
        self.successful_evolutions = 0
        self.best_fitness_achieved = 0.0
        
        print("🧬 تم تهيئة محرك التطور التكيفي Baserah النقي")
    
    def initialize_population(self, size: int = None) -> List[BaserahAdaptiveEquation]:
        """تهيئة مجموعة المعادلات."""
        size = size or self.config.population_size
        
        print(f"🌱 تهيئة مجموعة من {size} معادلة")
        
        self.population = []
        
        for i in range(size):
            equation = BaserahAdaptiveEquation(f"evolved_eq_{i}_{uuid.uuid4()}")
            
            # إضافة مكونات عشوائية
            num_components = random.randint(1, 3)
            
            for _ in range(num_components):
                component_type = random.choice(['sigmoid', 'linear', 'quantum_sigmoid'])
                
                if component_type == 'sigmoid':
                    equation.add_sigmoid_component(
                        n=random.randint(1, 3),
                        k=random.uniform(0.5, 3.0),
                        x0=random.uniform(-1.0, 1.0),
                        alpha=random.uniform(0.5, 2.0)
                    )
                elif component_type == 'linear':
                    equation.add_linear_component(
                        beta=random.uniform(-2.0, 2.0),
                        gamma=random.uniform(-1.0, 1.0)
                    )
                elif component_type == 'quantum_sigmoid':
                    equation.add_quantum_component(
                        quantum_factor=random.randint(*self.config.quantum_factor_range),
                        k=random.uniform(0.5, 3.0),
                        alpha=random.uniform(0.5, 2.0)
                    )
            
            self.population.append(equation)
        
        print(f"✅ تم إنشاء {len(self.population)} معادلة في المجموعة")
        return self.population
    
    def evaluate_fitness(self, equation: BaserahAdaptiveEquation, 
                        x_data: List[float], y_data: List[float]) -> float:
        """تقييم لياقة المعادلة."""
        if len(x_data) != len(y_data):
            return 0.0
        
        total_error = 0.0
        for x, y_target in zip(x_data, y_data):
            try:
                y_pred = equation.evaluate(x)
                error = abs(y_target - y_pred)
                total_error += error
            except (OverflowError, ZeroDivisionError):
                total_error += 1000.0  # عقوبة للمعادلات غير المستقرة
        
        avg_error = total_error / len(x_data)
        fitness = 1.0 / (1.0 + avg_error)  # لياقة عكسية للخطأ
        
        # مكافأة للمعادلات البسيطة (منهج Baserah)
        simplicity_bonus = 1.0 / (1.0 + len(equation.components) * 0.1)
        
        # مكافأة للمعادلات الكمية
        quantum_bonus = 1.0
        for component in equation.components:
            if component['type'] == 'quantum_sigmoid':
                quantum_bonus += 0.1
        
        final_fitness = fitness * simplicity_bonus * quantum_bonus
        equation.current_fitness = final_fitness
        
        return final_fitness
    
    def select_parents(self, fitness_scores: List[float]) -> Tuple[int, int]:
        """اختيار الوالدين للتكاثر."""
        # اختيار بناءً على اللياقة مع عشوائية
        weights = np.array(fitness_scores)
        weights = weights / np.sum(weights) if np.sum(weights) > 0 else np.ones_like(weights)
        
        parent1_idx = np.random.choice(len(self.population), p=weights)
        parent2_idx = np.random.choice(len(self.population), p=weights)
        
        # تجنب اختيار نفس الوالد
        while parent2_idx == parent1_idx and len(self.population) > 1:
            parent2_idx = np.random.choice(len(self.population), p=weights)
        
        return parent1_idx, parent2_idx
    
    def crossover(self, parent1: BaserahAdaptiveEquation, 
                  parent2: BaserahAdaptiveEquation) -> BaserahAdaptiveEquation:
        """تقاطع بين معادلتين لإنتاج معادلة جديدة."""
        child = BaserahAdaptiveEquation(f"crossover_{uuid.uuid4()}")
        
        # دمج مكونات الوالدين
        all_components = parent1.components + parent2.components
        
        # اختيار مكونات عشوائية
        num_components = min(len(all_components), random.randint(1, 4))
        selected_components = random.sample(all_components, num_components)
        
        for component in selected_components:
            # نسخ المكون مع تعديل طفيف
            new_component = component.copy()
            
            if component['type'] == 'sigmoid':
                # تعديل طفيف في المعاملات
                new_component['params']['k'] *= random.uniform(0.8, 1.2)
                new_component['params']['alpha'] *= random.uniform(0.9, 1.1)
                child.components.append(new_component)
                
            elif component['type'] == 'linear':
                new_component['params']['beta'] *= random.uniform(0.8, 1.2)
                new_component['params']['gamma'] += random.uniform(-0.1, 0.1)
                child.components.append(new_component)
                
            elif component['type'] == 'quantum_sigmoid':
                # تعديل عامل التكميم
                old_qf = new_component['params']['quantum_factor']
                new_qf = max(2, min(16, old_qf + random.randint(-2, 2)))
                new_component['params']['quantum_factor'] = new_qf
                child.components.append(new_component)
        
        return child
    
    def mutate(self, equation: BaserahAdaptiveEquation) -> BaserahAdaptiveEquation:
        """طفرة في المعادلة."""
        mutated = BaserahAdaptiveEquation(f"mutated_{uuid.uuid4()}")
        
        # نسخ المكونات مع طفرات
        for component in equation.components:
            new_component = component.copy()
            
            if random.random() < self.config.mutation_rate:
                if component['type'] == 'sigmoid':
                    # طفرة في معاملات السيجمويد
                    new_component['params']['k'] *= random.uniform(0.5, 2.0)
                    new_component['params']['x0'] += random.uniform(-0.5, 0.5)
                    new_component['params']['alpha'] *= random.uniform(0.7, 1.3)
                    
                elif component['type'] == 'linear':
                    # طفرة في معاملات الخط المستقيم
                    new_component['params']['beta'] *= random.uniform(0.5, 2.0)
                    new_component['params']['gamma'] += random.uniform(-0.5, 0.5)
                    
                elif component['type'] == 'quantum_sigmoid':
                    # طفرة في عامل التكميم
                    new_component['params']['quantum_factor'] = random.randint(*self.config.quantum_factor_range)
                    new_component['params']['k'] *= random.uniform(0.7, 1.3)
            
            mutated.components.append(new_component)
        
        # إضافة مكون جديد أحياناً
        if random.random() < 0.2 and len(mutated.components) < 4:
            component_type = random.choice(['sigmoid', 'linear', 'quantum_sigmoid'])
            
            if component_type == 'sigmoid':
                mutated.add_sigmoid_component(
                    k=random.uniform(0.5, 3.0),
                    alpha=random.uniform(0.5, 2.0)
                )
            elif component_type == 'linear':
                mutated.add_linear_component(
                    beta=random.uniform(-1.0, 1.0),
                    gamma=random.uniform(-0.5, 0.5)
                )
            elif component_type == 'quantum_sigmoid':
                mutated.add_quantum_component(
                    quantum_factor=random.randint(*self.config.quantum_factor_range)
                )
        
        return mutated
    
    def evolve_population(self, x_data: List[float], y_data: List[float]) -> EvolutionResult:
        """تطوير مجموعة المعادلات."""
        self.total_evolutions += 1
        
        print(f"🧬 بدء تطوير المجموعة (التطوير #{self.total_evolutions})")
        
        if not self.population:
            self.initialize_population()
        
        result = EvolutionResult()
        result.population = self.population.copy()
        
        best_fitness = 0.0
        best_equation = None
        
        for generation in range(self.config.max_generations):
            # تقييم اللياقة
            fitness_scores = []
            for equation in self.population:
                fitness = self.evaluate_fitness(equation, x_data, y_data)
                fitness_scores.append(fitness)
            
            # العثور على أفضل معادلة
            max_fitness_idx = np.argmax(fitness_scores)
            current_best_fitness = fitness_scores[max_fitness_idx]
            
            if current_best_fitness > best_fitness:
                best_fitness = current_best_fitness
                best_equation = self.population[max_fitness_idx]
            
            result.fitness_history.append(best_fitness)
            
            # فحص التقارب
            if best_fitness >= self.config.fitness_threshold:
                result.convergence_achieved = True
                break
            
            # إنشاء الجيل الجديد
            new_population = []
            
            # الاحتفاظ بأفضل معادلة (النخبوية)
            new_population.append(self.population[max_fitness_idx])
            
            # إنشاء باقي المجموعة
            while len(new_population) < self.config.population_size:
                if random.random() < self.config.crossover_rate:
                    # تقاطع
                    parent1_idx, parent2_idx = self.select_parents(fitness_scores)
                    child = self.crossover(self.population[parent1_idx], self.population[parent2_idx])
                    new_population.append(child)
                else:
                    # طفرة
                    parent_idx = self.select_parents(fitness_scores)[0]
                    mutated = self.mutate(self.population[parent_idx])
                    new_population.append(mutated)
            
            self.population = new_population
            result.generation_count = generation + 1
            
            # تسجيل التطور
            result.evolution_log.append({
                'generation': generation,
                'best_fitness': best_fitness,
                'avg_fitness': np.mean(fitness_scores),
                'population_size': len(self.population)
            })
        
        result.best_equation = best_equation
        result.best_fitness = best_fitness
        result.success = best_fitness > 0.5
        
        if result.success:
            self.successful_evolutions += 1
        
        self.best_fitness_achieved = max(self.best_fitness_achieved, best_fitness)
        
        # تسجيل في التاريخ
        self.evolution_history.append({
            'timestamp': datetime.now().isoformat(),
            'result': result,
            'config': self.config
        })
        
        print(f"✅ انتهى التطوير: أفضل لياقة={best_fitness:.6f}, "
              f"أجيال={result.generation_count}, تقارب={result.convergence_achieved}")
        
        return result
    
    def get_statistics(self) -> Dict[str, Any]:
        """الحصول على إحصائيات المحرك."""
        success_rate = self.successful_evolutions / max(1, self.total_evolutions)
        
        return {
            'total_evolutions': self.total_evolutions,
            'successful_evolutions': self.successful_evolutions,
            'success_rate': success_rate,
            'best_fitness_achieved': self.best_fitness_achieved,
            'current_population_size': len(self.population),
            'evolution_strategy': self.config.strategy.value,
            'population_mode': self.config.population_mode.value
        }
    
    def get_best_equations(self, top_k: int = 5) -> List[BaserahAdaptiveEquation]:
        """الحصول على أفضل المعادلات."""
        if not self.population:
            return []
        
        # ترتيب حسب اللياقة
        sorted_population = sorted(self.population, key=lambda eq: eq.current_fitness, reverse=True)
        
        return sorted_population[:top_k]
