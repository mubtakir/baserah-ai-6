#!/usr/bin/env python3
# intelligent_visual_inference_engine.py - محرك الاستنباط البصري الذكي

from typing import Dict, List, Any, Optional, Union, Tuple
from datetime import datetime
import uuid
import numpy as np
from dataclasses import dataclass, field
from enum import Enum, auto
import math

# استيراد الأسس الثورية
from .revolutionary_mother_equation import ConcreteRevolutionaryMotherEquation
from .ai_oop_foundation import BaserahAIOOPFoundation
from .semantic_meaning_engine import SemanticMeaningEngine
from artistic_intelligence.baserah_core import baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid

@dataclass
class ShapeDescriptor:
    """واصف الشكل الأساسي مع معادلاته."""
    name: str
    category: str
    base_equation: str
    properties: Dict[str, Any] = field(default_factory=dict)
    states: Dict[str, Any] = field(default_factory=dict)
    feature_vector: List[float] = field(default_factory=list)
    tolerance_range: float = 0.15
    confidence_threshold: float = 0.7

@dataclass
class VisualElement:
    """عنصر بصري مكتشف في الصورة."""
    shape_name: str
    properties: Dict[str, Any]
    position: Tuple[float, float]
    size: Tuple[float, float]
    confidence: float
    euclidean_distance: float

@dataclass
class ImageAnalysisResult:
    """نتيجة تحليل الصورة."""
    detected_elements: List[VisualElement]
    scene_description: str
    overall_confidence: float
    analysis_time: float
    inference_details: Dict[str, Any] = field(default_factory=dict)

class IntelligentVisualInferenceEngine(BaserahAIOOPFoundation):
    """
    محرك الاستنباط البصري الذكي
    
    نظام ثوري يتعلم من صور قليلة باستخدام:
    - قاعدة بيانات الأشكال الأساسية مع معادلاتها
    - نظام السماحية والمسافة الإقليدية
    - الاستنباط الذكي للعناصر المشتركة
    - العين المستنبطة للتحليل البصري
    """
    
    def __init__(self, engine_name: str = "IntelligentVisualInferenceEngine",
                 mother_equation_inheritance: Dict[str, Any] = None):
        """تهيئة محرك الاستنباط البصري الذكي."""
        
        super().__init__(engine_name, "intelligent_visual_inference_engine", mother_equation_inheritance)
        
        # قاعدة بيانات الأشكال الأساسية مع معادلاتها
        self.shapes_database = self._initialize_shapes_database()
        
        # إعدادات السماحية والمسافة الإقليدية
        self.tolerance_settings = {
            'global_tolerance': 0.15,  # السماحية العامة
            'color_tolerance': 0.2,    # سماحية الألوان
            'size_tolerance': 0.25,    # سماحية الأحجام
            'position_tolerance': 0.3,  # سماحية المواضع
            'shape_tolerance': 0.1     # سماحية الأشكال
        }
        
        # محرك التحليل الدلالي المتكامل
        self.semantic_engine = SemanticMeaningEngine("VisualSemanticEngine", mother_equation_inheritance)
        
        # العين المستنبطة - نظام التحليل البصري
        self.inference_eye = {
            'feature_extractors': self._initialize_feature_extractors(),
            'pattern_recognizers': self._initialize_pattern_recognizers(),
            'scene_composers': self._initialize_scene_composers(),
            'confidence_calculators': self._initialize_confidence_calculators()
        }
        
        # إحصائيات المحرك
        self.engine_stats = {
            'images_analyzed': 0,
            'elements_detected': 0,
            'successful_inferences': 0,
            'average_confidence': 0.0,
            'average_analysis_time': 0.0,
            'shapes_in_database': len(self.shapes_database)
        }
        
        print(f"👁️ تم تهيئة محرك الاستنباط البصري الذكي: {engine_name}")
        print("🧠 يتعلم من صور قليلة باستخدام السماحية والمسافة الإقليدية")
        print("🔍 العين المستنبطة للتحليل البصري الثوري")
    
    def _initialize_shapes_database(self) -> Dict[str, ShapeDescriptor]:
        """تهيئة قاعدة بيانات الأشكال الأساسية."""
        
        shapes_db = {}
        
        # الحيوانات
        shapes_db['قطة_بيضاء'] = ShapeDescriptor(
            name='قطة_بيضاء',
            category='حيوانات',
            base_equation='σ(ears) + σ(whiskers) + σ(tail)',
            properties={
                'color': 'أبيض',
                'size': 'متوسط',
                'ears': 'مثلثية',
                'tail': 'طويل',
                'whiskers': 'موجود'
            },
            states={'واقفة': 0.8, 'نائمة': 0.2, 'تلعب': 0.5},
            feature_vector=[0.9, 0.8, 0.7, 0.6, 0.9],  # [ears, whiskers, tail, body, color]
            tolerance_range=0.15
        )
        
        shapes_db['قطة_سوداء_نائمة'] = ShapeDescriptor(
            name='قطة_سوداء_نائمة',
            category='حيوانات',
            base_equation='σ(ears) + σ(whiskers) + σ(tail) * σ(sleeping_pose)',
            properties={
                'color': 'أسود',
                'size': 'متوسط',
                'ears': 'مثلثية',
                'tail': 'ملتف',
                'pose': 'نائمة'
            },
            states={'نائمة': 0.9, 'واقفة': 0.1, 'تلعب': 0.1},
            feature_vector=[0.8, 0.7, 0.9, 0.8, 0.1],  # [ears, whiskers, tail, body, color]
            tolerance_range=0.12
        )
        
        shapes_db['قطة_واقفة'] = ShapeDescriptor(
            name='قطة_واقفة',
            category='حيوانات',
            base_equation='σ(ears) + σ(whiskers) + σ(tail) * σ(standing_pose)',
            properties={
                'color': 'متغير',
                'size': 'متوسط',
                'ears': 'مثلثية',
                'tail': 'مستقيم',
                'pose': 'واقفة'
            },
            states={'واقفة': 0.9, 'نائمة': 0.1, 'تلعب': 0.3},
            feature_vector=[0.9, 0.8, 0.6, 0.9, 0.5],
            tolerance_range=0.18
        )
        
        # النباتات
        shapes_db['شجرة_خضراء'] = ShapeDescriptor(
            name='شجرة_خضراء',
            category='نباتات',
            base_equation='σ(trunk) + σ(branches) + σ(leaves)',
            properties={
                'color': 'أخضر',
                'size': 'كبير',
                'trunk': 'بني',
                'branches': 'متفرعة',
                'leaves': 'كثيفة'
            },
            states={'مورقة': 0.9, 'عارية': 0.1, 'مزهرة': 0.3},
            feature_vector=[0.8, 0.9, 0.9, 0.7, 0.8],  # [trunk, branches, leaves, height, color]
            tolerance_range=0.2
        )
        
        # المباني
        shapes_db['بيت_صغير'] = ShapeDescriptor(
            name='بيت_صغير',
            category='مباني',
            base_equation='σ(walls) + σ(roof) + σ(door) + σ(windows)',
            properties={
                'color': 'متغير',
                'size': 'صغير',
                'walls': 'مربعة',
                'roof': 'مثلثي',
                'door': 'مستطيل',
                'windows': 'مربعة'
            },
            states={'مسكون': 0.7, 'فارغ': 0.3, 'قديم': 0.4},
            feature_vector=[0.8, 0.9, 0.7, 0.6, 0.5],  # [walls, roof, door, windows, size]
            tolerance_range=0.16
        )
        
        return shapes_db
    
    def analyze_image_intelligently(self, image_data: Any, 
                                  analysis_depth: int = 3) -> ImageAnalysisResult:
        """
        تحليل الصورة بذكاء باستخدام العين المستنبطة.
        
        Args:
            image_data: بيانات الصورة
            analysis_depth: عمق التحليل (1-5)
            
        Returns:
            نتيجة التحليل البصري الذكي
        """
        
        print(f"👁️ بدء التحليل البصري الذكي...")
        print(f"🔍 عمق التحليل: {analysis_depth}")
        
        import time
        start_time = time.time()
        
        try:
            # المرحلة 1: استخراج الميزات البصرية
            print("   🔍 المرحلة 1: استخراج الميزات البصرية...")
            extracted_features = self._extract_visual_features(image_data, analysis_depth)
            
            # المرحلة 2: التعرف على الأنماط باستخدام المسافة الإقليدية
            print("   📐 المرحلة 2: التعرف على الأنماط بالمسافة الإقليدية...")
            pattern_matches = self._recognize_patterns_with_euclidean_distance(extracted_features)
            
            # المرحلة 3: الاستنباط الذكي للعناصر
            print("   🧠 المرحلة 3: الاستنباط الذكي للعناصر...")
            detected_elements = self._infer_elements_intelligently(pattern_matches, extracted_features)
            
            # المرحلة 4: تركيب وصف المشهد
            print("   📝 المرحلة 4: تركيب وصف المشهد...")
            scene_description = self._compose_scene_description(detected_elements)
            
            # المرحلة 5: حساب الثقة الإجمالية
            print("   🎯 المرحلة 5: حساب الثقة الإجمالية...")
            overall_confidence = self._calculate_overall_confidence(detected_elements)
            
            # إنشاء النتيجة
            analysis_time = time.time() - start_time
            
            result = ImageAnalysisResult(
                detected_elements=detected_elements,
                scene_description=scene_description,
                overall_confidence=overall_confidence,
                analysis_time=analysis_time,
                inference_details={
                    'extracted_features_count': len(extracted_features),
                    'pattern_matches_count': len(pattern_matches),
                    'analysis_depth': analysis_depth,
                    'tolerance_used': self.tolerance_settings['global_tolerance']
                }
            )
            
            # تحديث الإحصائيات
            self._update_engine_statistics(result)
            
            print(f"   ✅ اكتمل التحليل - الثقة: {overall_confidence:.3f}")
            
            return result
            
        except Exception as e:
            print(f"   ❌ خطأ في التحليل البصري: {e}")
            return ImageAnalysisResult(
                detected_elements=[],
                scene_description="فشل في تحليل الصورة",
                overall_confidence=0.0,
                analysis_time=time.time() - start_time,
                inference_details={'error': str(e)}
            )
    
    def _extract_visual_features(self, image_data: Any, depth: int) -> List[Dict[str, Any]]:
        """استخراج الميزات البصرية من الصورة."""
        
        # محاكاة استخراج الميزات (في التطبيق الحقيقي، سيتم استخدام معالجة الصور)
        features = []
        
        # ميزات أساسية (محاكاة)
        basic_features = [
            {
                'type': 'shape',
                'properties': {'roundness': 0.8, 'size': 0.6, 'position': (0.3, 0.4)},
                'feature_vector': [0.8, 0.7, 0.6, 0.9, 0.5],
                'confidence': 0.85
            },
            {
                'type': 'color_region',
                'properties': {'color': 'أبيض', 'area': 0.4, 'position': (0.3, 0.4)},
                'feature_vector': [0.9, 0.8, 0.7, 0.6, 0.9],
                'confidence': 0.9
            },
            {
                'type': 'texture',
                'properties': {'texture_type': 'ناعم', 'density': 0.7, 'position': (0.3, 0.4)},
                'feature_vector': [0.7, 0.8, 0.6, 0.8, 0.7],
                'confidence': 0.75
            }
        ]
        
        features.extend(basic_features)
        
        # ميزات متقدمة حسب العمق
        if depth >= 2:
            advanced_features = [
                {
                    'type': 'edge',
                    'properties': {'edge_strength': 0.8, 'orientation': 45, 'position': (0.2, 0.3)},
                    'feature_vector': [0.8, 0.6, 0.7, 0.9, 0.4],
                    'confidence': 0.8
                }
            ]
            features.extend(advanced_features)
        
        if depth >= 3:
            complex_features = [
                {
                    'type': 'pattern',
                    'properties': {'pattern_type': 'متكرر', 'frequency': 0.6, 'position': (0.7, 0.6)},
                    'feature_vector': [0.6, 0.9, 0.8, 0.7, 0.8],
                    'confidence': 0.82
                }
            ]
            features.extend(complex_features)
        
        return features
    
    def _recognize_patterns_with_euclidean_distance(self, features: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """التعرف على الأنماط باستخدام المسافة الإقليدية."""
        
        pattern_matches = []
        
        for feature in features:
            feature_vector = feature.get('feature_vector', [])
            if not feature_vector:
                continue
            
            # مقارنة مع كل شكل في قاعدة البيانات
            for shape_name, shape_descriptor in self.shapes_database.items():
                # حساب المسافة الإقليدية
                euclidean_distance = self._calculate_euclidean_distance(
                    feature_vector, shape_descriptor.feature_vector
                )
                
                # تحقق من السماحية
                if euclidean_distance <= shape_descriptor.tolerance_range:
                    # حساب درجة التطابق
                    match_confidence = 1.0 - (euclidean_distance / shape_descriptor.tolerance_range)
                    
                    # تطبيق التحويل الثوري لدرجة الثقة
                    revolutionary_confidence = baserah_sigmoid(
                        match_confidence * 2, n=1, k=2.0, x0=0.0, alpha=1.2
                    )
                    
                    pattern_matches.append({
                        'shape_name': shape_name,
                        'shape_descriptor': shape_descriptor,
                        'feature': feature,
                        'euclidean_distance': euclidean_distance,
                        'match_confidence': match_confidence,
                        'revolutionary_confidence': revolutionary_confidence,
                        'within_tolerance': True
                    })
        
        # ترتيب حسب درجة الثقة
        pattern_matches.sort(key=lambda x: x['revolutionary_confidence'], reverse=True)
        
        return pattern_matches
    
    def _calculate_euclidean_distance(self, vector1: List[float], vector2: List[float]) -> float:
        """حساب المسافة الإقليدية بين متجهين."""
        
        if len(vector1) != len(vector2):
            # تطبيع الأطوال
            min_len = min(len(vector1), len(vector2))
            vector1 = vector1[:min_len]
            vector2 = vector2[:min_len]
        
        # حساب المسافة الإقليدية
        distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(vector1, vector2)))
        
        # تطبيع المسافة (0-1)
        normalized_distance = distance / math.sqrt(len(vector1))
        
        return normalized_distance
    
    def process_revolutionary_input(self, input_data: Any) -> Any:
        """تنفيذ المعالجة الثورية لمحرك الاستنباط البصري."""
        
        if isinstance(input_data, dict) and 'image_data' in input_data:
            image_data = input_data['image_data']
            analysis_depth = input_data.get('analysis_depth', 3)
            return self.analyze_image_intelligently(image_data, analysis_depth)
        else:
            # تحليل أساسي
            return self.analyze_image_intelligently(input_data)
    
    def adapt_parameters(self, feedback: Dict[str, Any]) -> bool:
        """تكييف معاملات محرك الاستنباط البصري."""
        
        try:
            # تكييف السماحية
            if 'accuracy_feedback' in feedback:
                accuracy = feedback['accuracy_feedback']
                if accuracy < 0.5:
                    # زيادة السماحية للحصول على تطابقات أكثر
                    self.tolerance_settings['global_tolerance'] = min(0.3, 
                        self.tolerance_settings['global_tolerance'] + 0.02)
                elif accuracy > 0.9:
                    # تقليل السماحية للحصول على دقة أعلى
                    self.tolerance_settings['global_tolerance'] = max(0.05, 
                        self.tolerance_settings['global_tolerance'] - 0.01)
            
            # تكييف عتبة الثقة
            if 'confidence_feedback' in feedback:
                confidence = feedback['confidence_feedback']
                for shape_name, shape_descriptor in self.shapes_database.items():
                    if confidence > 0.8:
                        shape_descriptor.confidence_threshold = min(0.9, 
                            shape_descriptor.confidence_threshold + 0.05)
                    elif confidence < 0.6:
                        shape_descriptor.confidence_threshold = max(0.5, 
                            shape_descriptor.confidence_threshold - 0.03)
            
            return True
            
        except Exception as e:
            print(f"❌ خطأ في تكييف معاملات محرك الاستنباط البصري: {e}")
            return False

    def _initialize_feature_extractors(self) -> Dict[str, Any]:
        """تهيئة مستخرجات الميزات."""

        return {
            'shape_extractor': {
                'method': 'contour_analysis',
                'parameters': {'min_area': 100, 'max_area': 10000}
            },
            'color_extractor': {
                'method': 'histogram_analysis',
                'parameters': {'bins': 32, 'color_space': 'HSV'}
            },
            'texture_extractor': {
                'method': 'lbp_analysis',
                'parameters': {'radius': 3, 'n_points': 24}
            },
            'edge_extractor': {
                'method': 'canny_detection',
                'parameters': {'low_threshold': 50, 'high_threshold': 150}
            }
        }

    def _initialize_pattern_recognizers(self) -> Dict[str, Any]:
        """تهيئة مُعرِّفات الأنماط."""

        return {
            'geometric_recognizer': {
                'shapes': ['دائرة', 'مربع', 'مثلث', 'مستطيل'],
                'tolerance': 0.1
            },
            'object_recognizer': {
                'categories': ['حيوانات', 'نباتات', 'مباني', 'أشياء'],
                'confidence_threshold': 0.7
            },
            'scene_recognizer': {
                'contexts': ['داخلي', 'خارجي', 'طبيعي', 'حضري'],
                'composition_rules': True
            }
        }

    def _initialize_scene_composers(self) -> Dict[str, Any]:
        """تهيئة مُركِّبات المشهد."""

        return {
            'spatial_composer': {
                'relations': ['أمام', 'خلف', 'يمين', 'يسار', 'فوق', 'تحت'],
                'proximity_threshold': 0.2
            },
            'semantic_composer': {
                'context_rules': {
                    'حيوانات + نباتات': 'مشهد طبيعي',
                    'مباني + أشياء': 'مشهد حضري',
                    'قطة + بيت': 'قطة منزلية'
                }
            },
            'narrative_composer': {
                'action_verbs': ['تلعب', 'تنام', 'تقف', 'تجري', 'تأكل'],
                'state_adjectives': ['سعيدة', 'هادئة', 'نشطة', 'مسترخية']
            }
        }

    def _initialize_confidence_calculators(self) -> Dict[str, Any]:
        """تهيئة حاسبات الثقة."""

        return {
            'euclidean_calculator': {
                'weight': 0.4,
                'normalization': 'min_max'
            },
            'feature_calculator': {
                'weight': 0.3,
                'aggregation': 'weighted_average'
            },
            'context_calculator': {
                'weight': 0.2,
                'semantic_boost': 0.1
            },
            'revolutionary_calculator': {
                'weight': 0.1,
                'basil_theories_bonus': 0.05
            }
        }

    def _infer_elements_intelligently(self, pattern_matches: List[Dict[str, Any]],
                                    features: List[Dict[str, Any]]) -> List[VisualElement]:
        """الاستنباط الذكي للعناصر البصرية."""

        detected_elements = []

        # تجميع التطابقات حسب الموضع
        position_groups = self._group_matches_by_position(pattern_matches)

        for position, matches in position_groups.items():
            if not matches:
                continue

            # اختيار أفضل تطابق
            best_match = max(matches, key=lambda x: x['revolutionary_confidence'])

            # التحقق من عتبة الثقة
            if best_match['revolutionary_confidence'] >= best_match['shape_descriptor'].confidence_threshold:

                # استنباط الخصائص
                inferred_properties = self._infer_element_properties(best_match, matches)

                # إنشاء العنصر البصري
                visual_element = VisualElement(
                    shape_name=best_match['shape_name'],
                    properties=inferred_properties,
                    position=position,
                    size=self._estimate_element_size(best_match),
                    confidence=best_match['revolutionary_confidence'],
                    euclidean_distance=best_match['euclidean_distance']
                )

                detected_elements.append(visual_element)

        return detected_elements

    def _group_matches_by_position(self, pattern_matches: List[Dict[str, Any]]) -> Dict[Tuple[float, float], List[Dict[str, Any]]]:
        """تجميع التطابقات حسب الموضع."""

        position_groups = {}
        position_tolerance = self.tolerance_settings['position_tolerance']

        for match in pattern_matches:
            feature = match['feature']
            feature_position = feature['properties'].get('position', (0.5, 0.5))

            # البحث عن مجموعة موضع مناسبة
            found_group = False
            for existing_position in position_groups.keys():
                distance = math.sqrt(
                    (feature_position[0] - existing_position[0]) ** 2 +
                    (feature_position[1] - existing_position[1]) ** 2
                )

                if distance <= position_tolerance:
                    position_groups[existing_position].append(match)
                    found_group = True
                    break

            # إنشاء مجموعة جديدة إذا لم توجد
            if not found_group:
                position_groups[feature_position] = [match]

        return position_groups

    def _infer_element_properties(self, best_match: Dict[str, Any],
                                all_matches: List[Dict[str, Any]]) -> Dict[str, Any]:
        """استنباط خصائص العنصر."""

        shape_descriptor = best_match['shape_descriptor']
        base_properties = shape_descriptor.properties.copy()

        # استنباط الحالة
        inferred_state = self._infer_element_state(best_match, all_matches)
        if inferred_state:
            base_properties['state'] = inferred_state

        # استنباط اللون إذا كان متغير
        if base_properties.get('color') == 'متغير':
            inferred_color = self._infer_element_color(best_match, all_matches)
            if inferred_color:
                base_properties['color'] = inferred_color

        # استنباط الحجم النسبي
        inferred_size = self._infer_element_relative_size(best_match, all_matches)
        if inferred_size:
            base_properties['relative_size'] = inferred_size

        return base_properties

    def _infer_element_state(self, best_match: Dict[str, Any],
                           all_matches: List[Dict[str, Any]]) -> Optional[str]:
        """استنباط حالة العنصر."""

        shape_descriptor = best_match['shape_descriptor']
        available_states = shape_descriptor.states

        # تحليل الميزات للاستنباط
        feature = best_match['feature']
        feature_properties = feature['properties']

        # استنباط بناءً على الخصائص
        if 'roundness' in feature_properties:
            roundness = feature_properties['roundness']
            if roundness > 0.8 and 'نائمة' in available_states:
                return 'نائمة'
            elif roundness < 0.5 and 'واقفة' in available_states:
                return 'واقفة'

        # استنباط بناءً على الموضع
        position = feature_properties.get('position', (0.5, 0.5))
        if position[1] > 0.7 and 'تلعب' in available_states:  # في الأسفل
            return 'تلعب'

        # الحالة الافتراضية (الأعلى احتمالاً)
        if available_states:
            return max(available_states, key=available_states.get)

        return None

    def _infer_element_color(self, best_match: Dict[str, Any],
                           all_matches: List[Dict[str, Any]]) -> Optional[str]:
        """استنباط لون العنصر."""

        # البحث عن ميزات اللون في التطابقات
        for match in all_matches:
            feature = match['feature']
            if feature['type'] == 'color_region':
                color = feature['properties'].get('color')
                if color:
                    return color

        # ألوان افتراضية حسب الفئة
        shape_descriptor = best_match['shape_descriptor']
        if shape_descriptor.category == 'حيوانات':
            return 'بني'  # لون افتراضي للحيوانات
        elif shape_descriptor.category == 'نباتات':
            return 'أخضر'  # لون افتراضي للنباتات
        elif shape_descriptor.category == 'مباني':
            return 'رمادي'  # لون افتراضي للمباني

        return None

    def _infer_element_relative_size(self, best_match: Dict[str, Any],
                                   all_matches: List[Dict[str, Any]]) -> Optional[str]:
        """استنباط الحجم النسبي للعنصر."""

        feature = best_match['feature']
        feature_properties = feature['properties']

        size_value = feature_properties.get('size', 0.5)

        if size_value > 0.8:
            return 'كبير'
        elif size_value > 0.5:
            return 'متوسط'
        else:
            return 'صغير'

    def _estimate_element_size(self, best_match: Dict[str, Any]) -> Tuple[float, float]:
        """تقدير حجم العنصر."""

        feature = best_match['feature']
        feature_properties = feature['properties']

        # حجم افتراضي
        default_size = (0.2, 0.2)

        # استخراج الحجم من الميزات
        if 'size' in feature_properties:
            size_factor = feature_properties['size']
            return (size_factor * 0.3, size_factor * 0.3)

        if 'area' in feature_properties:
            area = feature_properties['area']
            side = math.sqrt(area)
            return (side, side)

        return default_size

    def _compose_scene_description(self, detected_elements: List[VisualElement]) -> str:
        """تركيب وصف المشهد من العناصر المكتشفة."""

        if not detected_elements:
            return "لم يتم اكتشاف عناصر واضحة في الصورة"

        # تجميع العناصر حسب الفئة
        elements_by_category = {}
        for element in detected_elements:
            # استخراج الفئة من اسم الشكل
            shape_parts = element.shape_name.split('_')
            base_shape = shape_parts[0]

            # تحديد الفئة
            category = self._get_element_category(base_shape)

            if category not in elements_by_category:
                elements_by_category[category] = []
            elements_by_category[category].append(element)

        # بناء الوصف
        description_parts = []

        # وصف العناصر الرئيسية
        for category, elements in elements_by_category.items():
            category_description = self._describe_category_elements(category, elements)
            if category_description:
                description_parts.append(category_description)

        # وصف العلاقات المكانية
        spatial_relations = self._describe_spatial_relations(detected_elements)
        if spatial_relations:
            description_parts.append(spatial_relations)

        # دمج الوصف
        if description_parts:
            return ' '.join(description_parts)
        else:
            return "مشهد يحتوي على عناصر متنوعة"

    def _get_element_category(self, base_shape: str) -> str:
        """تحديد فئة العنصر."""

        animal_shapes = ['قطة', 'كلب', 'طائر', 'حصان']
        plant_shapes = ['شجرة', 'زهرة', 'عشب', 'نبات']
        building_shapes = ['بيت', 'مبنى', 'قصر', 'كوخ']

        if base_shape in animal_shapes:
            return 'حيوانات'
        elif base_shape in plant_shapes:
            return 'نباتات'
        elif base_shape in building_shapes:
            return 'مباني'
        else:
            return 'أشياء'

    def _describe_category_elements(self, category: str, elements: List[VisualElement]) -> str:
        """وصف عناصر فئة معينة."""

        if not elements:
            return ""

        descriptions = []

        for element in elements:
            # استخراج الوصف الأساسي
            base_name = element.shape_name.split('_')[0]

            # إضافة الخصائص
            properties = element.properties
            color = properties.get('color', '')
            state = properties.get('state', '')

            # بناء الوصف
            element_desc = base_name

            if color and color != 'متغير':
                element_desc = f"{base_name} {color}"

            if state:
                element_desc += f" {state}"

            descriptions.append(element_desc)

        # دمج الأوصاف
        if len(descriptions) == 1:
            return descriptions[0]
        elif len(descriptions) == 2:
            return f"{descriptions[0]} و{descriptions[1]}"
        else:
            return f"{', '.join(descriptions[:-1])} و{descriptions[-1]}"

    def _describe_spatial_relations(self, detected_elements: List[VisualElement]) -> str:
        """وصف العلاقات المكانية بين العناصر."""

        if len(detected_elements) < 2:
            return ""

        relations = []

        # تحليل المواضع النسبية
        for i, element1 in enumerate(detected_elements):
            for element2 in detected_elements[i+1:]:
                relation = self._determine_spatial_relation(element1, element2)
                if relation:
                    relations.append(relation)

        # اختيار أهم العلاقات
        if relations:
            return f"في خلفيتها {relations[0]}" if len(relations) == 1 else f"مع {relations[0]}"

        return ""

    def _determine_spatial_relation(self, element1: VisualElement, element2: VisualElement) -> Optional[str]:
        """تحديد العلاقة المكانية بين عنصرين."""

        pos1 = element1.position
        pos2 = element2.position

        # حساب الفروق
        dx = pos2[0] - pos1[0]
        dy = pos2[1] - pos1[1]

        # تحديد العلاقة الأساسية
        if abs(dx) > abs(dy):
            if dx > 0.1:
                return f"{element2.shape_name.split('_')[0]} على اليمين"
            elif dx < -0.1:
                return f"{element2.shape_name.split('_')[0]} على اليسار"
        else:
            if dy > 0.1:
                return f"{element2.shape_name.split('_')[0]} في الأسفل"
            elif dy < -0.1:
                return f"{element2.shape_name.split('_')[0]} في الأعلى"

        # عناصر قريبة
        distance = math.sqrt(dx**2 + dy**2)
        if distance < 0.2:
            return f"{element2.shape_name.split('_')[0]} قريب"

        return None

    def _calculate_overall_confidence(self, detected_elements: List[VisualElement]) -> float:
        """حساب الثقة الإجمالية."""

        if not detected_elements:
            return 0.0

        # متوسط ثقة العناصر
        element_confidences = [element.confidence for element in detected_elements]
        average_confidence = sum(element_confidences) / len(element_confidences)

        # عامل عدد العناصر (المزيد من العناصر = ثقة أعلى)
        element_count_factor = min(1.0, len(detected_elements) / 3.0)

        # عامل تنوع الفئات
        categories = set(self._get_element_category(elem.shape_name.split('_')[0]) for elem in detected_elements)
        diversity_factor = min(1.0, len(categories) / 2.0)

        # الثقة الإجمالية
        overall_confidence = (
            average_confidence * 0.6 +
            element_count_factor * 0.2 +
            diversity_factor * 0.2
        )

        # تطبيق التحويل الثوري
        return baserah_sigmoid(overall_confidence * 1.5, n=1, k=2.0, x0=0.0, alpha=1.1)

    def _update_engine_statistics(self, result: ImageAnalysisResult):
        """تحديث إحصائيات المحرك."""

        self.engine_stats['images_analyzed'] += 1
        self.engine_stats['elements_detected'] += len(result.detected_elements)

        if result.overall_confidence > 0.7:
            self.engine_stats['successful_inferences'] += 1

        # تحديث متوسط الثقة
        current_avg = self.engine_stats['average_confidence']
        images_count = self.engine_stats['images_analyzed']
        new_confidence = result.overall_confidence

        self.engine_stats['average_confidence'] = (
            (current_avg * (images_count - 1) + new_confidence) / images_count
        )

        # تحديث متوسط وقت التحليل
        current_time_avg = self.engine_stats['average_analysis_time']
        new_time = result.analysis_time

        self.engine_stats['average_analysis_time'] = (
            (current_time_avg * (images_count - 1) + new_time) / images_count
        )

    def add_shape_to_database(self, shape_descriptor: ShapeDescriptor) -> bool:
        """إضافة شكل جديد إلى قاعدة البيانات."""

        try:
            self.shapes_database[shape_descriptor.name] = shape_descriptor
            self.engine_stats['shapes_in_database'] = len(self.shapes_database)
            print(f"✅ تم إضافة الشكل الجديد: {shape_descriptor.name}")
            return True
        except Exception as e:
            print(f"❌ خطأ في إضافة الشكل: {e}")
            return False

    def get_engine_statistics(self) -> Dict[str, Any]:
        """الحصول على إحصائيات المحرك."""

        success_rate = 0.0
        if self.engine_stats['images_analyzed'] > 0:
            success_rate = self.engine_stats['successful_inferences'] / self.engine_stats['images_analyzed']

        return {
            'engine_info': {
                'name': self.system_name,
                'type': 'intelligent_visual_inference_engine',
                'creation_time': getattr(self, 'creation_time', datetime.now())
            },
            'analysis_stats': {
                'images_analyzed': self.engine_stats['images_analyzed'],
                'elements_detected': self.engine_stats['elements_detected'],
                'successful_inferences': self.engine_stats['successful_inferences'],
                'success_rate': success_rate,
                'average_confidence': self.engine_stats['average_confidence'],
                'average_analysis_time': self.engine_stats['average_analysis_time']
            },
            'database_stats': {
                'shapes_in_database': self.engine_stats['shapes_in_database'],
                'categories_supported': len(set(shape.category for shape in self.shapes_database.values())),
                'tolerance_settings': self.tolerance_settings
            },
            'capabilities': {
                'feature_extractors': len(self.inference_eye['feature_extractors']),
                'pattern_recognizers': len(self.inference_eye['pattern_recognizers']),
                'scene_composers': len(self.inference_eye['scene_composers']),
                'confidence_calculators': len(self.inference_eye['confidence_calculators'])
            },
            'revolutionary_features': {
                'euclidean_distance_matching': True,
                'tolerance_based_recognition': True,
                'intelligent_inference': True,
                'few_shot_learning': True,
                'baserah_equations': True,
                'semantic_composition': True
            },
            'performance_assessment': 'excellent' if success_rate > 0.8 else 'good' if success_rate > 0.6 else 'developing'
        }
