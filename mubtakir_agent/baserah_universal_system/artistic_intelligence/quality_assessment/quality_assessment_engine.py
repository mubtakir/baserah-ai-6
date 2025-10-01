#!/usr/bin/env python3
# quality_assessment_engine.py - محرك تقييم الجودة للتغذية الراجعة

import numpy as np
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
import math

@dataclass
class QualityMetrics:
    """مقاييس الجودة."""
    structural_similarity: float
    mathematical_accuracy: float
    visual_fidelity: float
    overall_score: float
    error_analysis: Dict[str, Any]

class BaserahQualityAssessmentEngine:
    """
    محرك تقييم الجودة Baserah النقي
    يقارن بين الصورة الأصلية والمولدة لتوليد تغذية راجعة ذكية
    """
    
    def __init__(self):
        """تهيئة محرك تقييم الجودة."""
        
        # معاملات التقييم
        self.structural_weight = 0.4
        self.mathematical_weight = 0.3
        self.visual_weight = 0.3
        
        # عتبات الجودة
        self.excellent_threshold = 0.9
        self.good_threshold = 0.7
        self.acceptable_threshold = 0.5
        
        # تاريخ التقييمات
        self.assessment_history = []
        
        print("🔍 تم تهيئة محرك تقييم الجودة Baserah النقي")
    
    def assess_quality(self, original_data: List[Tuple[float, float]], 
                      generated_data: List[Tuple[float, float]]) -> QualityMetrics:
        """
        تقييم شامل للجودة بين البيانات الأصلية والمولدة.
        
        Args:
            original_data: البيانات الأصلية [(x, y), ...]
            generated_data: البيانات المولدة [(x, y), ...]
            
        Returns:
            QualityMetrics: مقاييس الجودة الشاملة
        """
        
        print(f"🔍 بدء تقييم الجودة: {len(original_data)} نقطة أصلية، {len(generated_data)} نقطة مولدة")
        
        # تقييم التشابه الهيكلي
        structural_sim = self._calculate_structural_similarity(original_data, generated_data)
        
        # تقييم الدقة الرياضية
        math_accuracy = self._calculate_mathematical_accuracy(original_data, generated_data)
        
        # تقييم الإخلاص البصري
        visual_fidelity = self._calculate_visual_fidelity(original_data, generated_data)
        
        # حساب النقاط الإجمالية
        overall_score = (
            self.structural_weight * structural_sim +
            self.mathematical_weight * math_accuracy +
            self.visual_weight * visual_fidelity
        )
        
        # تحليل الأخطاء
        error_analysis = self._analyze_errors(original_data, generated_data)
        
        # إنشاء مقاييس الجودة
        metrics = QualityMetrics(
            structural_similarity=structural_sim,
            mathematical_accuracy=math_accuracy,
            visual_fidelity=visual_fidelity,
            overall_score=overall_score,
            error_analysis=error_analysis
        )
        
        # حفظ في التاريخ
        self.assessment_history.append(metrics)
        
        print(f"📊 نتائج التقييم:")
        print(f"   التشابه الهيكلي: {structural_sim:.3f}")
        print(f"   الدقة الرياضية: {math_accuracy:.3f}")
        print(f"   الإخلاص البصري: {visual_fidelity:.3f}")
        print(f"   النقاط الإجمالية: {overall_score:.3f}")
        
        return metrics
    
    def _calculate_structural_similarity(self, original: List[Tuple[float, float]], 
                                       generated: List[Tuple[float, float]]) -> float:
        """حساب التشابه الهيكلي باستخدام دوال Baserah النقية."""
        
        if not original or not generated:
            return 0.0
        
        # تحويل إلى مصفوفات
        orig_x = [p[0] for p in original]
        orig_y = [p[1] for p in original]
        gen_x = [p[0] for p in generated]
        gen_y = [p[1] for p in generated]
        
        # حساب الإحصائيات الأساسية
        orig_mean_x = sum(orig_x) / len(orig_x)
        orig_mean_y = sum(orig_y) / len(orig_y)
        gen_mean_x = sum(gen_x) / len(gen_x)
        gen_mean_y = sum(gen_y) / len(gen_y)
        
        # حساب التباين
        orig_var_x = sum((x - orig_mean_x) ** 2 for x in orig_x) / len(orig_x)
        orig_var_y = sum((y - orig_mean_y) ** 2 for y in orig_y) / len(orig_y)
        gen_var_x = sum((x - gen_mean_x) ** 2 for x in gen_x) / len(gen_x)
        gen_var_y = sum((y - gen_mean_y) ** 2 for y in gen_y) / len(gen_y)
        
        # حساب التشابه باستخدام السيجمويد
        from .baserah_core import baserah_sigmoid
        
        mean_diff = abs(orig_mean_x - gen_mean_x) + abs(orig_mean_y - gen_mean_y)
        var_diff = abs(orig_var_x - gen_var_x) + abs(orig_var_y - gen_var_y)
        
        # تطبيق السيجمويد للحصول على نقاط تشابه
        mean_similarity = baserah_sigmoid(-mean_diff, n=1, k=2.0, x0=0.0, alpha=1.0)
        var_similarity = baserah_sigmoid(-var_diff, n=1, k=1.0, x0=0.0, alpha=1.0)
        
        structural_similarity = (mean_similarity + var_similarity) / 2
        
        return structural_similarity
    
    def _calculate_mathematical_accuracy(self, original: List[Tuple[float, float]], 
                                       generated: List[Tuple[float, float]]) -> float:
        """حساب الدقة الرياضية باستخدام معادلات Baserah."""
        
        if not original or not generated:
            return 0.0
        
        # حساب متوسط المسافة الإقليدية
        total_distance = 0.0
        min_len = min(len(original), len(generated))
        
        for i in range(min_len):
            orig_x, orig_y = original[i]
            gen_x, gen_y = generated[i]
            
            distance = math.sqrt((orig_x - gen_x) ** 2 + (orig_y - gen_y) ** 2)
            total_distance += distance
        
        avg_distance = total_distance / min_len if min_len > 0 else float('inf')
        
        # تحويل المسافة إلى نقاط دقة باستخدام السيجمويد
        from .baserah_core import baserah_sigmoid
        
        # كلما قلت المسافة، زادت الدقة
        accuracy = baserah_sigmoid(-avg_distance, n=1, k=3.0, x0=0.0, alpha=1.0)
        
        return accuracy
    
    def _calculate_visual_fidelity(self, original: List[Tuple[float, float]], 
                                 generated: List[Tuple[float, float]]) -> float:
        """حساب الإخلاص البصري باستخدام تحليل الشكل."""
        
        if not original or not generated:
            return 0.0
        
        # تحليل الشكل العام
        orig_shape_features = self._extract_shape_features(original)
        gen_shape_features = self._extract_shape_features(generated)
        
        # مقارنة الخصائص
        feature_similarity = 0.0
        feature_count = 0
        
        for feature_name in orig_shape_features:
            if feature_name in gen_shape_features:
                orig_val = orig_shape_features[feature_name]
                gen_val = gen_shape_features[feature_name]
                
                # حساب التشابه باستخدام دالة خطية
                from .baserah_core import baserah_linear
                
                diff = abs(orig_val - gen_val)
                similarity = max(0, baserah_linear(-diff, beta=1.0, gamma=1.0))
                feature_similarity += similarity
                feature_count += 1
        
        visual_fidelity = feature_similarity / feature_count if feature_count > 0 else 0.0
        
        return min(visual_fidelity, 1.0)
    
    def _extract_shape_features(self, data: List[Tuple[float, float]]) -> Dict[str, float]:
        """استخراج خصائص الشكل."""
        
        if len(data) < 3:
            return {}
        
        x_coords = [p[0] for p in data]
        y_coords = [p[1] for p in data]
        
        features = {
            'center_x': sum(x_coords) / len(x_coords),
            'center_y': sum(y_coords) / len(y_coords),
            'range_x': max(x_coords) - min(x_coords),
            'range_y': max(y_coords) - min(y_coords),
            'aspect_ratio': (max(x_coords) - min(x_coords)) / (max(y_coords) - min(y_coords) + 1e-6),
            'perimeter': self._calculate_perimeter(data),
            'compactness': self._calculate_compactness(data)
        }
        
        return features
    
    def _calculate_perimeter(self, data: List[Tuple[float, float]]) -> float:
        """حساب المحيط."""
        
        if len(data) < 2:
            return 0.0
        
        perimeter = 0.0
        for i in range(len(data)):
            x1, y1 = data[i]
            x2, y2 = data[(i + 1) % len(data)]
            perimeter += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        return perimeter
    
    def _calculate_compactness(self, data: List[Tuple[float, float]]) -> float:
        """حساب الانضغاط."""
        
        perimeter = self._calculate_perimeter(data)
        if perimeter == 0:
            return 0.0
        
        # تقدير المساحة باستخدام صيغة الحذاء
        area = 0.0
        for i in range(len(data)):
            x1, y1 = data[i]
            x2, y2 = data[(i + 1) % len(data)]
            area += x1 * y2 - x2 * y1
        area = abs(area) / 2.0
        
        # الانضغاط = 4π × المساحة / المحيط²
        compactness = (4 * math.pi * area) / (perimeter ** 2) if perimeter > 0 else 0.0
        
        return compactness
    
    def _analyze_errors(self, original: List[Tuple[float, float]], 
                       generated: List[Tuple[float, float]]) -> Dict[str, Any]:
        """تحليل مفصل للأخطاء."""
        
        error_analysis = {
            'total_points_original': len(original),
            'total_points_generated': len(generated),
            'point_count_difference': abs(len(original) - len(generated)),
            'error_types': [],
            'recommendations': []
        }
        
        if len(original) != len(generated):
            error_analysis['error_types'].append('point_count_mismatch')
            error_analysis['recommendations'].append('ضبط عدد النقاط المولدة')
        
        if original and generated:
            # حساب الأخطاء النقطية
            min_len = min(len(original), len(generated))
            point_errors = []
            
            for i in range(min_len):
                orig_x, orig_y = original[i]
                gen_x, gen_y = generated[i]
                
                error = math.sqrt((orig_x - gen_x) ** 2 + (orig_y - gen_y) ** 2)
                point_errors.append(error)
            
            if point_errors:
                error_analysis['mean_point_error'] = sum(point_errors) / len(point_errors)
                error_analysis['max_point_error'] = max(point_errors)
                error_analysis['min_point_error'] = min(point_errors)
                
                # تصنيف الأخطاء
                high_error_count = sum(1 for e in point_errors if e > 0.5)
                if high_error_count > len(point_errors) * 0.3:
                    error_analysis['error_types'].append('high_point_errors')
                    error_analysis['recommendations'].append('تحسين دقة المعادلات')
        
        return error_analysis
    
    def generate_feedback(self, metrics: QualityMetrics) -> Dict[str, Any]:
        """توليد تغذية راجعة ذكية من مقاييس الجودة."""
        
        feedback = {
            'overall_quality': self._classify_quality(metrics.overall_score),
            'improvement_areas': [],
            'specific_adjustments': {},
            'confidence_adjustment': 0.0,
            'priority_actions': []
        }
        
        # تحليل نقاط الضعف
        if metrics.structural_similarity < 0.7:
            feedback['improvement_areas'].append('structural_similarity')
            feedback['specific_adjustments']['structure'] = 'تحسين التشابه الهيكلي'
            feedback['priority_actions'].append('ضبط معاملات الشكل العام')
        
        if metrics.mathematical_accuracy < 0.7:
            feedback['improvement_areas'].append('mathematical_accuracy')
            feedback['specific_adjustments']['mathematics'] = 'تحسين الدقة الرياضية'
            feedback['priority_actions'].append('ضبط معاملات المعادلات')
        
        if metrics.visual_fidelity < 0.7:
            feedback['improvement_areas'].append('visual_fidelity')
            feedback['specific_adjustments']['visual'] = 'تحسين الإخلاص البصري'
            feedback['priority_actions'].append('ضبط خصائص الرسم')
        
        # تعديل الثقة
        if metrics.overall_score > 0.9:
            feedback['confidence_adjustment'] = 0.1
        elif metrics.overall_score > 0.7:
            feedback['confidence_adjustment'] = 0.05
        elif metrics.overall_score < 0.5:
            feedback['confidence_adjustment'] = -0.2
        else:
            feedback['confidence_adjustment'] = -0.1
        
        return feedback
    
    def _classify_quality(self, score: float) -> str:
        """تصنيف مستوى الجودة."""
        
        if score >= self.excellent_threshold:
            return 'ممتاز'
        elif score >= self.good_threshold:
            return 'جيد'
        elif score >= self.acceptable_threshold:
            return 'مقبول'
        else:
            return 'يحتاج تحسين'
    
    def get_assessment_summary(self) -> Dict[str, Any]:
        """ملخص تقييمات الجودة."""
        
        if not self.assessment_history:
            return {'message': 'لا توجد تقييمات بعد'}
        
        scores = [m.overall_score for m in self.assessment_history]
        
        summary = {
            'total_assessments': len(self.assessment_history),
            'average_score': sum(scores) / len(scores),
            'best_score': max(scores),
            'worst_score': min(scores),
            'improvement_trend': self._calculate_trend(scores),
            'recent_performance': scores[-5:] if len(scores) >= 5 else scores
        }
        
        return summary
    
    def _calculate_trend(self, scores: List[float]) -> str:
        """حساب اتجاه التحسن."""
        
        if len(scores) < 3:
            return 'غير كافي للتقييم'
        
        recent_avg = sum(scores[-3:]) / 3
        earlier_avg = sum(scores[:-3]) / len(scores[:-3]) if len(scores) > 3 else scores[0]
        
        if recent_avg > earlier_avg + 0.05:
            return 'تحسن'
        elif recent_avg < earlier_avg - 0.05:
            return 'تراجع'
        else:
            return 'مستقر'
