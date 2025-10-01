#!/usr/bin/env python3
# revolutionary_mother_system.py - النظام الثوري الأم وفقاً للسياسة الثورية

import numpy as np
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Union, Optional, Any, Callable
from dataclasses import dataclass, field
from enum import Enum
from abc import ABC, abstractmethod

# استيراد قاعدة بيانات الأشكال
try:
    from knowledge_systems.shapes_database.shapes_database import BaserahShapesDatabase, ShapeDefinition, ShapeType, ComplexityLevel
except ImportError:
    try:
        from .shapes_database import BaserahShapesDatabase, ShapeDefinition, ShapeType, ComplexityLevel
    except ImportError:
        # في حالة عدم توفر قاعدة البيانات
        BaserahShapesDatabase = None
        ShapeDefinition = None
        ShapeType = None
        ComplexityLevel = None

@dataclass
class BaserahMotherDatabase:
    """قاعدة بيانات المعادلة الأم الثورية."""
    basic_equations: Dict[str, Any] = field(default_factory=dict)
    basic_shapes: Dict[str, Any] = field(default_factory=dict)
    adaptation_patterns: Dict[str, Any] = field(default_factory=dict)
    evolution_history: List[Dict[str, Any]] = field(default_factory=list)
    inheritance_tree: Dict[str, List[str]] = field(default_factory=dict)

class InheritanceType(Enum):
    """أنواع الوراثة من المعادلة الأم."""
    ARTISTIC_UNIT = "artistic_unit"  # الوحدة الفنية
    ADAPTIVE_EQUATIONS = "adaptive_equations"  # المعادلات المتكيفة
    EXPERT_EXPLORER = "expert_explorer"  # الخبير والمستكشف
    INFERENCE_ENGINE = "inference_engine"  # العين المستنبطة
    ANIMATION_RENDERER = "animation_renderer"  # الراسم والأنيميشن
    GENERAL_SHAPE = "general_shape"  # معادلة الشكل العام

class AdaptationType(Enum):
    """أنواع التكيف في النظام الثوري."""
    VISUAL_ADAPTATION = "visual_adaptation"  # التكيف البصري (الأولوية)
    DATA_ADAPTATION = "data_adaptation"  # التكيف مع البيانات (ثانوي)
    PATTERN_ADAPTATION = "pattern_adaptation"  # التكيف مع الأنماط (ثانوي)
    BEHAVIORAL_ADAPTATION = "behavioral_adaptation"  # التكيف السلوكي (ثانوي)

class BaserahRevolutionaryMotherSystem:
    """
    النظام الثوري الأم Baserah النقي
    
    هذا هو النظام الأساسي الذي يحتوي على المعادلة الأم الثورية
    وقاعدة البيانات التي ترث منها جميع الوحدات الأخرى.
    
    السياسة الثورية:
    1. المعادلة الأم هي أساس النظام - كل شيء يرث منها
    2. نظام AI-OOP - كل الوحدات ترث بدلاً من التكرار
    3. المعادلات المتكيفة ترث معادلة الشكل العام
    4. الأنظمة الثورية تدعم كل الوحدات
    5. التكيف البصري له الأولوية
    """
    
    def __init__(self):
        """تهيئة النظام الثوري الأم."""
        self.system_id = f"revolutionary_mother_{uuid.uuid4()}"
        self.mother_database = BaserahMotherDatabase()

        # قاعدة بيانات الأشكال الأساسية - ترث منها جميع الوحدات
        if BaserahShapesDatabase:
            self.shapes_database = BaserahShapesDatabase()
        else:
            self.shapes_database = None
            print("⚠️ قاعدة بيانات الأشكال غير متاحة")

        # النظام الخبير/المستكشف للمعادلات المتكيفة الذكية
        try:
            from revolutionary_intelligence.expert_explorer_system.expert_explorer.integrated_expert_explorer import BaserahIntegratedExpertExplorer
            self.expert_explorer_system = BaserahIntegratedExpertExplorer()
            print("🧠🔍 تم تهيئة النظام الخبير/المستكشف في النظام الأم")
        except ImportError:
            self.expert_explorer_system = None
            print("⚠️ النظام الخبير/المستكشف غير متاح")
        
        # المعادلة الأم الثورية الأساسية
        self.mother_equation_coefficients = {
            # معاملات السيجمويد الأساسية
            'sigmoid_base': {'n': 1, 'k': 1.0, 'x0': 0.0, 'alpha': 1.0},
            'sigmoid_shape': {'n': 2, 'k': 2.0, 'x0': 0.0, 'alpha': 1.618},  # النسبة الذهبية
            'sigmoid_adaptive': {'n': 1, 'k': 1.5, 'x0': 0.0, 'alpha': 1.0},
            
            # معاملات الخط المستقيم الأساسية
            'linear_base': {'beta': 1.0, 'gamma': 0.0},
            'linear_shape': {'beta': 1.618, 'gamma': 0.0},  # النسبة الذهبية
            'linear_adaptive': {'beta': 1.0, 'gamma': 0.0},
            
            # معاملات التكميم الأساسية
            'quantum_factors': [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        }
        
        # سجل الوحدات الوارثة
        self.inherited_units: Dict[InheritanceType, Any] = {}
        
        # إحصائيات النظام
        self.total_inheritances = 0
        self.total_adaptations = 0
        self.system_evolution_count = 0
        
        # تهيئة قاعدة البيانات الأساسية
        self._initialize_mother_database()
        
        print("🌟 تم تهيئة النظام الثوري الأم وفقاً للسياسة الثورية")
        print("✅ المعادلة الأم جاهزة للوراثة من جميع الوحدات")
    
    def _initialize_mother_database(self):
        """تهيئة قاعدة بيانات المعادلة الأم."""
        
        # المعادلات الأساسية
        self.mother_database.basic_equations = {
            'sigmoid_pure': lambda x, n=1, k=1.0, x0=0.0, alpha=1.0: alpha / (1 + np.exp(-k * (x - x0)**n)),
            'linear_pure': lambda x, beta=1.0, gamma=0.0: beta * x + gamma,
            'quantum_sigmoid': lambda x, qf=4, **kwargs: round(self._sigmoid_pure(x, **kwargs) * qf) / qf,
            'general_shape': self._create_general_shape_equation,
            'adaptive_base': self._create_adaptive_base_equation
        }
        
        # الأشكال الأساسية
        self.mother_database.basic_shapes = {
            'primitive_cat': {
                'description': 'شكل القطة البدائي - مستطيل مع ذيل',
                'components': [
                    {'type': 'linear', 'params': {'beta': 1.0, 'gamma': 0.0}},  # الجسم
                    {'type': 'linear', 'params': {'beta': 0.2, 'gamma': 0.8}}   # الذيل
                ],
                'adaptation_target': 'professional_cat'
            },
            'professional_cat': {
                'description': 'شكل القطة المحترف - منحنيات متقدمة',
                'components': [
                    {'type': 'sigmoid', 'params': {'n': 2, 'k': 2.0, 'x0': 0.0, 'alpha': 1.0}},  # الجسم
                    {'type': 'sigmoid', 'params': {'n': 1, 'k': 1.5, 'x0': 0.5, 'alpha': 0.8}},  # الرأس
                    {'type': 'sigmoid', 'params': {'n': 1, 'k': 3.0, 'x0': -0.5, 'alpha': 0.3}}  # الذيل
                ]
            },
            'basic_triangle': {
                'description': 'مثلث أساسي',
                'components': [
                    {'type': 'linear', 'params': {'beta': 1.0, 'gamma': 0.0}},
                    {'type': 'linear', 'params': {'beta': -1.0, 'gamma': 1.0}},
                    {'type': 'linear', 'params': {'beta': 0.0, 'gamma': 0.0}}
                ]
            },
            'basic_circle': {
                'description': 'دائرة أساسية',
                'components': [
                    {'type': 'sigmoid', 'params': {'n': 2, 'k': 10.0, 'x0': 0.0, 'alpha': 1.0}}
                ]
            }
        }
        
        # أنماط التكيف
        self.mother_database.adaptation_patterns = {
            'visual_smooth_adaptation': {
                'priority': 1,  # الأولوية العليا
                'method': 'smooth_visual_transition',
                'learning_rate': 0.01,
                'adaptation_steps': 100
            },
            'data_pattern_adaptation': {
                'priority': 2,  # ثانوي
                'method': 'data_fitting',
                'learning_rate': 0.05,
                'adaptation_steps': 50
            },
            'behavioral_adaptation': {
                'priority': 3,  # ثانوي
                'method': 'behavior_learning',
                'learning_rate': 0.02,
                'adaptation_steps': 75
            }
        }
        
        print("📊 تم تهيئة قاعدة بيانات المعادلة الأم")
    
    def _sigmoid_pure(self, x: float, n: int = 1, k: float = 1.0, x0: float = 0.0, alpha: float = 1.0) -> float:
        """دالة السيجمويد النقية Baserah."""
        try:
            return alpha / (1 + np.exp(-k * (x - x0)**n))
        except (OverflowError, ZeroDivisionError):
            return alpha if x > x0 else 0.0
    
    def _linear_pure(self, x: float, beta: float = 1.0, gamma: float = 0.0) -> float:
        """دالة الخط المستقيم النقية Baserah."""
        return beta * x + gamma
    
    def _create_general_shape_equation(self) -> Dict[str, Any]:
        """إنشاء معادلة الشكل العام التي ترث منها المعادلات المتكيفة."""
        return {
            'equation_type': 'general_shape',
            'components': [
                {
                    'type': 'sigmoid',
                    'params': self.mother_equation_coefficients['sigmoid_shape'],
                    'weight': 1.0,
                    'inheritable': True
                },
                {
                    'type': 'linear', 
                    'params': self.mother_equation_coefficients['linear_shape'],
                    'weight': 0.8,
                    'inheritable': True
                },
                {
                    'type': 'quantum_sigmoid',
                    'params': {**self.mother_equation_coefficients['sigmoid_base'], 'quantum_factor': 4},
                    'weight': 0.6,
                    'inheritable': True
                }
            ],
            'inheritance_ready': True,
            'adaptation_enabled': True
        }
    
    def _create_adaptive_base_equation(self) -> Dict[str, Any]:
        """إنشاء المعادلة الأساسية للتكيف."""
        return {
            'equation_type': 'adaptive_base',
            'components': [
                {
                    'type': 'sigmoid',
                    'params': self.mother_equation_coefficients['sigmoid_adaptive'],
                    'weight': 1.2,
                    'adaptive': True
                },
                {
                    'type': 'linear',
                    'params': self.mother_equation_coefficients['linear_adaptive'], 
                    'weight': 1.0,
                    'adaptive': True
                }
            ],
            'adaptation_priority': AdaptationType.VISUAL_ADAPTATION,
            'inheritance_ready': True
        }
    
    def inherit_to_unit(self, unit_type: InheritanceType, unit_instance: Any) -> Dict[str, Any]:
        """وراثة المعادلة الأم إلى وحدة معينة."""
        
        self.total_inheritances += 1
        
        print(f"🧬 بدء وراثة المعادلة الأم إلى {unit_type.value}")
        
        inheritance_result = {
            'unit_type': unit_type.value,
            'inheritance_id': f"inherit_{uuid.uuid4()}",
            'timestamp': datetime.now().isoformat(),
            'inherited_components': [],
            'success': False
        }
        
        try:
            if unit_type == InheritanceType.ADAPTIVE_EQUATIONS:
                # وراثة معادلة الشكل العام للمعادلات المتكيفة
                general_shape = self.mother_database.basic_equations['general_shape']()
                inheritance_result['inherited_components'] = general_shape['components']
                
                # تطبيق الوراثة على الوحدة
                if hasattr(unit_instance, 'inherit_from_mother'):
                    unit_instance.inherit_from_mother(general_shape)
                
            elif unit_type == InheritanceType.ARTISTIC_UNIT:
                # وراثة الأشكال الأساسية والمعادلات للوحدة الفنية
                basic_shapes = self.mother_database.basic_shapes
                basic_equations = self.mother_database.basic_equations
                
                inheritance_package = {
                    'shapes': basic_shapes,
                    'equations': basic_equations,
                    'coefficients': self.mother_equation_coefficients
                }
                
                if hasattr(unit_instance, 'inherit_from_mother'):
                    unit_instance.inherit_from_mother(inheritance_package)
                
                inheritance_result['inherited_components'] = list(basic_shapes.keys())
                
            elif unit_type == InheritanceType.EXPERT_EXPLORER:
                # وراثة قواعد الاستدلال والاستكشاف
                expert_knowledge = {
                    'basic_equations': self.mother_database.basic_equations,
                    'adaptation_patterns': self.mother_database.adaptation_patterns,
                    'evolution_history': self.mother_database.evolution_history
                }
                
                if hasattr(unit_instance, 'inherit_from_mother'):
                    unit_instance.inherit_from_mother(expert_knowledge)
                
                inheritance_result['inherited_components'] = ['expert_knowledge', 'adaptation_patterns']
                
            elif unit_type == InheritanceType.INFERENCE_ENGINE:
                # وراثة قدرات الاستنباط للعين المستنبطة
                inference_capabilities = {
                    'shape_recognition': self.mother_database.basic_shapes,
                    'adaptation_patterns': self.mother_database.adaptation_patterns,
                    'visual_adaptation_priority': AdaptationType.VISUAL_ADAPTATION
                }
                
                if hasattr(unit_instance, 'inherit_from_mother'):
                    unit_instance.inherit_from_mother(inference_capabilities)
                
                inheritance_result['inherited_components'] = ['shape_recognition', 'visual_adaptation']
                
            elif unit_type == InheritanceType.ANIMATION_RENDERER:
                # وراثة قدرات الرسم والأنيميشن
                rendering_capabilities = {
                    'basic_shapes': self.mother_database.basic_shapes,
                    'animation_equations': self.mother_database.basic_equations,
                    'quantum_factors': self.mother_equation_coefficients['quantum_factors']
                }
                
                if hasattr(unit_instance, 'inherit_from_mother'):
                    unit_instance.inherit_from_mother(rendering_capabilities)
                
                inheritance_result['inherited_components'] = ['basic_shapes', 'animation_equations']
            
            # تسجيل الوراثة
            self.inherited_units[unit_type] = unit_instance
            
            # تحديث شجرة الوراثة
            if unit_type.value not in self.mother_database.inheritance_tree:
                self.mother_database.inheritance_tree[unit_type.value] = []
            
            self.mother_database.inheritance_tree[unit_type.value].append(inheritance_result['inheritance_id'])
            
            inheritance_result['success'] = True
            
            print(f"✅ تمت وراثة {len(inheritance_result['inherited_components'])} مكون إلى {unit_type.value}")
            
        except Exception as e:
            print(f"❌ خطأ في الوراثة: {e}")
            inheritance_result['error'] = str(e)
        
        return inheritance_result
    
    def adapt_visual_smooth(self, source_shape: str, target_shape: str, steps: int = 100) -> List[Dict[str, Any]]:
        """التكيف البصري السلس - الأولوية العليا."""
        
        print(f"🎨 بدء التكيف البصري السلس من {source_shape} إلى {target_shape}")
        
        if source_shape not in self.mother_database.basic_shapes:
            print(f"❌ الشكل المصدر {source_shape} غير موجود")
            return []
        
        if target_shape not in self.mother_database.basic_shapes:
            print(f"❌ الشكل الهدف {target_shape} غير موجود")
            return []
        
        source_components = self.mother_database.basic_shapes[source_shape]['components']
        target_components = self.mother_database.basic_shapes[target_shape]['components']
        
        adaptation_steps = []
        
        # إنشاء خطوات التكيف السلس
        for step in range(steps + 1):
            progress = step / steps  # من 0 إلى 1
            
            step_components = []
            
            # تكيف كل مكون
            max_components = max(len(source_components), len(target_components))
            
            for i in range(max_components):
                if i < len(source_components) and i < len(target_components):
                    # تكيف بين مكونين موجودين
                    source_comp = source_components[i]
                    target_comp = target_components[i]
                    
                    adapted_comp = self._interpolate_component(source_comp, target_comp, progress)
                    step_components.append(adapted_comp)
                    
                elif i < len(source_components):
                    # تلاشي المكون المصدر
                    source_comp = source_components[i].copy()
                    fade_factor = 1.0 - progress
                    
                    if source_comp['type'] == 'sigmoid':
                        source_comp['params']['alpha'] *= fade_factor
                    elif source_comp['type'] == 'linear':
                        source_comp['params']['beta'] *= fade_factor
                    
                    step_components.append(source_comp)
                    
                elif i < len(target_components):
                    # ظهور المكون الهدف
                    target_comp = target_components[i].copy()
                    appear_factor = progress
                    
                    if target_comp['type'] == 'sigmoid':
                        target_comp['params']['alpha'] *= appear_factor
                    elif target_comp['type'] == 'linear':
                        target_comp['params']['beta'] *= appear_factor
                    
                    step_components.append(target_comp)
            
            adaptation_step = {
                'step': step,
                'progress': progress,
                'components': step_components,
                'timestamp': datetime.now().isoformat()
            }
            
            adaptation_steps.append(adaptation_step)
        
        # تسجيل التكيف
        self.total_adaptations += 1
        
        adaptation_record = {
            'adaptation_id': f"visual_adapt_{uuid.uuid4()}",
            'type': AdaptationType.VISUAL_ADAPTATION,
            'source_shape': source_shape,
            'target_shape': target_shape,
            'steps_count': len(adaptation_steps),
            'timestamp': datetime.now().isoformat()
        }
        
        self.mother_database.evolution_history.append(adaptation_record)
        
        print(f"✅ تم إنشاء {len(adaptation_steps)} خطوة تكيف بصري سلس")
        
        return adaptation_steps
    
    def _interpolate_component(self, source_comp: Dict[str, Any], target_comp: Dict[str, Any], progress: float) -> Dict[str, Any]:
        """تكيف سلس بين مكونين."""
        
        adapted_comp = source_comp.copy()
        
        if source_comp['type'] == target_comp['type']:
            # نفس النوع - تكيف المعاملات
            if source_comp['type'] == 'sigmoid':
                for param in ['n', 'k', 'x0', 'alpha']:
                    if param in source_comp['params'] and param in target_comp['params']:
                        source_val = source_comp['params'][param]
                        target_val = target_comp['params'][param]
                        adapted_comp['params'][param] = source_val + (target_val - source_val) * progress
                        
            elif source_comp['type'] == 'linear':
                for param in ['beta', 'gamma']:
                    if param in source_comp['params'] and param in target_comp['params']:
                        source_val = source_comp['params'][param]
                        target_val = target_comp['params'][param]
                        adapted_comp['params'][param] = source_val + (target_val - source_val) * progress
        else:
            # أنواع مختلفة - تحويل تدريجي
            if progress < 0.5:
                # النصف الأول - تلاشي المصدر
                fade_factor = 1.0 - (progress * 2)
                if adapted_comp['type'] == 'sigmoid':
                    adapted_comp['params']['alpha'] *= fade_factor
                elif adapted_comp['type'] == 'linear':
                    adapted_comp['params']['beta'] *= fade_factor
            else:
                # النصف الثاني - ظهور الهدف
                adapted_comp = target_comp.copy()
                appear_factor = (progress - 0.5) * 2
                if adapted_comp['type'] == 'sigmoid':
                    adapted_comp['params']['alpha'] *= appear_factor
                elif adapted_comp['type'] == 'linear':
                    adapted_comp['params']['beta'] *= appear_factor
        
        return adapted_comp
    
    def evolve_system(self) -> Dict[str, Any]:
        """تطوير النظام لنفسه بنفسه."""
        
        self.system_evolution_count += 1
        
        print(f"🧬 بدء تطوير النظام التلقائي #{self.system_evolution_count}")
        
        evolution_result = {
            'evolution_id': f"system_evolution_{uuid.uuid4()}",
            'evolution_count': self.system_evolution_count,
            'changes_made': [],
            'new_capabilities': [],
            'success': False
        }
        
        try:
            # تحليل أداء الوحدات الوارثة
            performance_analysis = self._analyze_inherited_units_performance()
            
            # تحسين المعاملات بناءً على الأداء
            if performance_analysis['needs_optimization']:
                optimization_changes = self._optimize_mother_coefficients()
                evolution_result['changes_made'].extend(optimization_changes)
            
            # إضافة قدرات جديدة إذا لزم الأمر
            if performance_analysis['needs_new_capabilities']:
                new_capabilities = self._add_new_capabilities()
                evolution_result['new_capabilities'].extend(new_capabilities)
            
            # تحديث قاعدة البيانات
            self._update_mother_database()
            
            evolution_result['success'] = True
            
            print(f"✅ تم تطوير النظام: {len(evolution_result['changes_made'])} تغيير")
            
        except Exception as e:
            print(f"❌ خطأ في تطوير النظام: {e}")
            evolution_result['error'] = str(e)
        
        return evolution_result
    
    def _analyze_inherited_units_performance(self) -> Dict[str, Any]:
        """تحليل أداء الوحدات الوارثة."""
        return {
            'total_units': len(self.inherited_units),
            'needs_optimization': self.total_adaptations > 10,
            'needs_new_capabilities': self.total_inheritances > 5,
            'performance_score': min(1.0, self.total_inheritances / 10.0)
        }
    
    def _optimize_mother_coefficients(self) -> List[str]:
        """تحسين معاملات المعادلة الأم."""
        changes = []
        
        # تحسين معاملات السيجمويد
        self.mother_equation_coefficients['sigmoid_shape']['k'] *= 1.05
        changes.append("optimized sigmoid k coefficient")
        
        # تحسين معاملات الخط المستقيم
        self.mother_equation_coefficients['linear_shape']['beta'] *= 1.02
        changes.append("optimized linear beta coefficient")
        
        return changes
    
    def _add_new_capabilities(self) -> List[str]:
        """إضافة قدرات جديدة للنظام."""
        new_capabilities = []
        
        # إضافة عوامل تكميم جديدة
        max_quantum = max(self.mother_equation_coefficients['quantum_factors'])
        if max_quantum < 2048:
            self.mother_equation_coefficients['quantum_factors'].append(max_quantum * 2)
            new_capabilities.append(f"added quantum factor {max_quantum * 2}")
        
        return new_capabilities
    
    def _update_mother_database(self):
        """تحديث قاعدة بيانات المعادلة الأم."""
        # تسجيل التحديث
        update_record = {
            'update_id': f"db_update_{uuid.uuid4()}",
            'timestamp': datetime.now().isoformat(),
            'evolution_count': self.system_evolution_count
        }
        
        self.mother_database.evolution_history.append(update_record)
    
    def get_system_summary(self) -> Dict[str, Any]:
        """الحصول على ملخص النظام الثوري الأم."""

        # ملخص قاعدة بيانات الأشكال
        if self.shapes_database:
            shapes_summary = self.shapes_database.get_database_summary()
        else:
            shapes_summary = {
                'total_shapes': 0,
                'shapes_by_type': {},
                'shapes_by_complexity': {},
                'animated_shapes': 0,
                'mathematical_beauty_average': 0.0,
                'database_id': 'not_available'
            }

        return {
            'system_id': self.system_id,
            'total_inheritances': self.total_inheritances,
            'total_adaptations': self.total_adaptations,
            'system_evolution_count': self.system_evolution_count,
            'inherited_units_count': len(self.inherited_units),
            'inherited_unit_types': [unit_type.value for unit_type in self.inherited_units.keys()],
            'basic_equations_count': len(self.mother_database.basic_equations),
            'basic_shapes_count': len(self.mother_database.basic_shapes),
            'adaptation_patterns_count': len(self.mother_database.adaptation_patterns),
            'inheritance_tree': self.mother_database.inheritance_tree,
            'mother_equation_coefficients': self.mother_equation_coefficients,
            'system_status': 'active_and_evolving',
            'baserah_purity': 1.0,
            # معلومات قاعدة بيانات الأشكال الأساسية
            'shapes_database': {
                'total_shapes': shapes_summary['total_shapes'],
                'shapes_by_type': shapes_summary['shapes_by_type'],
                'shapes_by_complexity': shapes_summary['shapes_by_complexity'],
                'animated_shapes': shapes_summary['animated_shapes'],
                'mathematical_beauty_average': shapes_summary['mathematical_beauty_average'],
                'database_id': shapes_summary['database_id']
            }
        }

    # دوال الوصول إلى قاعدة بيانات الأشكال
    def get_shape(self, shape_id: str):
        """الحصول على شكل من قاعدة البيانات."""
        if self.shapes_database:
            return self.shapes_database.get_shape(shape_id)
        return None

    def get_shapes_by_type(self, shape_type: ShapeType) -> List[ShapeDefinition]:
        """الحصول على الأشكال حسب النوع."""
        return self.shapes_database.get_shapes_by_type(shape_type)

    def get_shapes_by_complexity(self, complexity: ComplexityLevel) -> List[ShapeDefinition]:
        """الحصول على الأشكال حسب مستوى التعقيد."""
        return self.shapes_database.get_shapes_by_complexity(complexity)

    def search_shapes(self, query: str) -> List[ShapeDefinition]:
        """البحث في قاعدة بيانات الأشكال."""
        return self.shapes_database.search_shapes(query)

    def get_transformation_sequence(self, source_shape_id: str, target_shape_id: str, steps: int = 10) -> List[Dict]:
        """إنشاء تسلسل تحويل بين شكلين."""
        return self.shapes_database.get_transformation_sequence(source_shape_id, target_shape_id, steps)

    def export_shapes_database(self, filename: str = None) -> str:
        """تصدير قاعدة بيانات الأشكال."""
        return self.shapes_database.export_database(filename)

    def inherit_shapes_to_unit(self, unit, inheritance_type: InheritanceType) -> Dict[str, Any]:
        """وراثة قاعدة بيانات الأشكال إلى وحدة."""

        inheritance_id = f"shapes_inheritance_{uuid.uuid4()}"

        try:
            # نقل قاعدة بيانات الأشكال إلى الوحدة
            if hasattr(unit, 'inherit_shapes_database'):
                unit.inherit_shapes_database(self.shapes_database)
            elif hasattr(unit, 'shapes_database'):
                unit.shapes_database = self.shapes_database
            else:
                # إنشاء مرجع لقاعدة البيانات
                unit.mother_shapes_database = self.shapes_database

            # تسجيل الوراثة
            inheritance_record = InheritanceRecord(
                inheritance_id=inheritance_id,
                inheritance_type=inheritance_type,
                target_unit_id=getattr(unit, 'unit_id', str(id(unit))),
                inherited_data={
                    'shapes_database_id': self.shapes_database.database_id,
                    'total_shapes': len(self.shapes_database.shapes),
                    'inheritance_timestamp': datetime.now().isoformat()
                },
                success=True,
                timestamp=datetime.now().isoformat()
            )

            self.inheritance_registry[inheritance_id] = inheritance_record
            self.total_inheritances += 1

            return {
                'success': True,
                'inheritance_id': inheritance_id,
                'shapes_inherited': len(self.shapes_database.shapes),
                'message': f'تم وراثة قاعدة بيانات الأشكال ({len(self.shapes_database.shapes)} شكل) إلى الوحدة'
            }

        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': 'فشل في وراثة قاعدة بيانات الأشكال'
            }

    def inherit_expert_explorer_to_unit(self, unit, inheritance_type: InheritanceType) -> Dict[str, Any]:
        """وراثة النظام الخبير/المستكشف إلى وحدة للتكيف الذكي."""

        inheritance_id = f"expert_explorer_inheritance_{uuid.uuid4()}"

        try:
            if not self.expert_explorer_system:
                return {
                    'success': False,
                    'error': 'النظام الخبير/المستكشف غير متاح',
                    'message': 'لا يمكن وراثة النظام الخبير/المستكشف'
                }

            # نقل النظام الخبير/المستكشف إلى الوحدة
            if hasattr(unit, 'inherit_expert_explorer_system'):
                success = unit.inherit_expert_explorer_system(self.expert_explorer_system)
            else:
                # إنشاء مرجع للنظام
                unit.expert_explorer_system = self.expert_explorer_system
                unit.adaptive_intelligence_enabled = True
                success = True

            if success:
                # تسجيل الوراثة
                inheritance_record = InheritanceRecord(
                    inheritance_id=inheritance_id,
                    inheritance_type=inheritance_type,
                    target_unit_id=getattr(unit, 'unit_id', str(id(unit))),
                    inherited_data={
                        'expert_explorer_system_id': getattr(self.expert_explorer_system, 'system_id', 'unknown'),
                        'adaptive_equations_count': len(getattr(self.expert_explorer_system, 'adaptive_equations', [])),
                        'inheritance_timestamp': datetime.now().isoformat()
                    },
                    success=True,
                    timestamp=datetime.now().isoformat()
                )

                self.inheritance_registry[inheritance_id] = inheritance_record
                self.total_inheritances += 1

                return {
                    'success': True,
                    'inheritance_id': inheritance_id,
                    'adaptive_equations_inherited': len(getattr(self.expert_explorer_system, 'adaptive_equations', [])),
                    'message': f'تم وراثة النظام الخبير/المستكشف للتكيف الذكي'
                }
            else:
                return {
                    'success': False,
                    'error': 'فشل في وراثة النظام الخبير/المستكشف',
                    'message': 'الوحدة لا تدعم وراثة النظام الخبير/المستكشف'
                }

        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': 'فشل في وراثة النظام الخبير/المستكشف'
            }
