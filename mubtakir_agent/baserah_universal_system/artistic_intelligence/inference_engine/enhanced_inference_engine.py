#!/usr/bin/env python3
# enhanced_inference_engine.py - العين المستنبطة المحسنة بالتغذية الراجعة

import math
from typing import List, Tuple, Dict, Optional, Union, Any
from datetime import datetime
import uuid

# استيراد المحرك الأصلي
from .inference_engine import BaserahInferenceEngine
from .baserah_core import baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid

class EnhancedBaserahInferenceEngine(BaserahInferenceEngine):
    """
    العين المستنبطة المحسنة بالتغذية الراجعة
    تتعلم من التغذية الراجعة وتحسن دقتها تدريجياً
    """
    
    def __init__(self):
        """تهيئة العين المستنبطة المحسنة."""
        
        # تهيئة المحرك الأساسي
        super().__init__()
        
        # نظام التغذية الراجعة
        self.feedback_history = []
        self.confidence_adjustments = []
        self.learning_enabled = True
        self.base_confidence = 0.5
        self.adaptive_learning_rate = 0.05
        
        # إحصائيات التحسن
        self.total_inferences = 0
        self.successful_improvements = 0
        self.average_confidence_improvement = 0.0
        
        # معاملات التكيف
        self.pattern_recognition_weights = {
            'linear': 1.0,
            'sigmoid': 1.0,
            'quantum': 0.8,
            'mixed': 0.9
        }
        
        print("🧠 تم تهيئة العين المستنبطة المحسنة بالتغذية الراجعة")
    
    def infer_with_feedback(self, x_data: List[float], y_data: List[float], 
                           feedback: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        استنباط محسن بالتغذية الراجعة.
        
        Args:
            x_data: بيانات المحور السيني
            y_data: بيانات المحور الصادي
            feedback: تغذية راجعة من الدورة السابقة
            
        Returns:
            نتيجة الاستنباط المحسنة
        """
        
        self.total_inferences += 1
        inference_id = f"enhanced_inference_{uuid.uuid4()}"
        
        print(f"🧠 بدء الاستنباط المحسن: {inference_id}")
        
        # تطبيق التغذية الراجعة إذا كانت متاحة
        if feedback:
            self._apply_feedback(feedback)
        
        # الاستنباط الأساسي
        base_result = self.infer_from_data_points(x_data, y_data)
        
        # تحسين النتيجة
        enhanced_result = self._enhance_inference_result(base_result, x_data, y_data)
        
        # إضافة معلومات التحسين
        enhanced_result['inference_id'] = inference_id
        enhanced_result['enhancement_applied'] = True
        enhanced_result['feedback_incorporated'] = feedback is not None
        enhanced_result['total_inferences'] = self.total_inferences
        
        return enhanced_result
    
    def _apply_feedback(self, feedback: Dict[str, Any]):
        """تطبيق التغذية الراجعة لتحسين الأداء."""
        
        print("🔄 تطبيق التغذية الراجعة...")
        
        # حفظ التغذية الراجعة
        self.feedback_history.append({
            'feedback': feedback,
            'timestamp': datetime.now(),
            'applied': True
        })
        
        # تحديث الثقة
        confidence_adj = feedback.get('confidence_adjustment', 0.0)
        if confidence_adj != 0:
            self.confidence_adjustments.append(confidence_adj)
            self.base_confidence += confidence_adj * self.adaptive_learning_rate
            self.base_confidence = max(0.1, min(0.99, self.base_confidence))
            print(f"   📈 تحديث الثقة الأساسية: {self.base_confidence:.3f}")
        
        # تحديث أوزان التعرف على الأنماط
        improvement_areas = feedback.get('improvement_areas', [])
        for area in improvement_areas:
            if area in self.pattern_recognition_weights:
                # تقليل الوزن للأنماط التي تحتاج تحسين
                self.pattern_recognition_weights[area] *= 0.95
                print(f"   🔧 تقليل وزن {area}: {self.pattern_recognition_weights[area]:.3f}")
        
        # تحديث معدل التعلم
        overall_quality = feedback.get('overall_quality', 'مقبول')
        if overall_quality == 'ممتاز':
            self.adaptive_learning_rate *= 1.05  # زيادة طفيفة
        elif overall_quality == 'يحتاج تحسين':
            self.adaptive_learning_rate *= 1.1   # زيادة أكبر
        
        self.adaptive_learning_rate = min(0.2, self.adaptive_learning_rate)
        
        # تطبيق تحسينات محددة
        specific_adjustments = feedback.get('specific_adjustments', {})
        for adjustment_type, description in specific_adjustments.items():
            self._apply_specific_adjustment(adjustment_type, description)
    
    def _apply_specific_adjustment(self, adjustment_type: str, description: str):
        """تطبيق تحسين محدد."""
        
        if adjustment_type == 'structure':
            # تحسين التشابه الهيكلي
            self.tolerance *= 0.9  # زيادة الدقة
            print(f"   🔧 تحسين الهيكل: تقليل التسامح إلى {self.tolerance:.2e}")
        
        elif adjustment_type == 'mathematics':
            # تحسين الدقة الرياضية
            self.max_iterations = min(2000, int(self.max_iterations * 1.1))
            print(f"   🔧 تحسين الرياضيات: زيادة التكرارات إلى {self.max_iterations}")
        
        elif adjustment_type == 'visual':
            # تحسين الإخلاص البصري
            self.learning_rate *= 1.05
            print(f"   🔧 تحسين البصريات: زيادة معدل التعلم إلى {self.learning_rate:.4f}")
    
    def _enhance_inference_result(self, base_result: Dict[str, Any], 
                                x_data: List[float], y_data: List[float]) -> Dict[str, Any]:
        """تحسين نتيجة الاستنباط."""
        
        if 'error' in base_result:
            return base_result
        
        enhanced_result = base_result.copy()
        
        # تحسين الثقة بناءً على التاريخ
        original_confidence = enhanced_result.get('confidence', 0.5)
        confidence_boost = self._calculate_confidence_boost(base_result, x_data, y_data)
        
        enhanced_confidence = min(0.99, original_confidence + confidence_boost)
        enhanced_result['confidence'] = enhanced_confidence
        enhanced_result['confidence_boost'] = confidence_boost
        enhanced_result['original_confidence'] = original_confidence
        
        # تحسين المعاملات بناءً على التعلم
        if 'components' in enhanced_result:
            enhanced_result['components'] = self._enhance_components(
                enhanced_result['components'], x_data, y_data
            )
        
        # إضافة معلومات التحسين
        enhanced_result['enhancement_details'] = {
            'feedback_history_count': len(self.feedback_history),
            'confidence_adjustments_applied': len(self.confidence_adjustments),
            'pattern_weights': self.pattern_recognition_weights.copy(),
            'adaptive_learning_rate': self.adaptive_learning_rate
        }
        
        print(f"   📈 تحسين الثقة: {original_confidence:.3f} → {enhanced_confidence:.3f}")
        
        return enhanced_result
    
    def _calculate_confidence_boost(self, result: Dict[str, Any], 
                                  x_data: List[float], y_data: List[float]) -> float:
        """حساب تعزيز الثقة بناءً على التعلم."""
        
        # تعزيز أساسي من التاريخ
        base_boost = sum(self.confidence_adjustments) * 0.1 if self.confidence_adjustments else 0.0
        
        # تعزيز من نوع النمط
        pattern_type = result.get('type', 'unknown')
        pattern_weight = self.pattern_recognition_weights.get(pattern_type, 1.0)
        pattern_boost = (pattern_weight - 1.0) * 0.1
        
        # تعزيز من جودة البيانات
        data_quality = self._assess_data_quality(x_data, y_data)
        quality_boost = (data_quality - 0.5) * 0.2
        
        total_boost = base_boost + pattern_boost + quality_boost
        
        # تحديد الحد الأقصى للتعزيز
        max_boost = 0.3
        return max(-0.2, min(max_boost, total_boost))
    
    def _assess_data_quality(self, x_data: List[float], y_data: List[float]) -> float:
        """تقييم جودة البيانات."""
        
        if len(x_data) < 3 or len(y_data) < 3:
            return 0.3
        
        # تقييم التوزيع
        x_range = max(x_data) - min(x_data)
        y_range = max(y_data) - min(y_data)
        
        # تقييم الانتظام
        x_sorted = sorted(x_data)
        x_intervals = [x_sorted[i+1] - x_sorted[i] for i in range(len(x_sorted)-1)]
        interval_consistency = 1.0 - (max(x_intervals) - min(x_intervals)) / (max(x_intervals) + 1e-6)
        
        # تقييم عدم وجود قيم شاذة
        y_mean = sum(y_data) / len(y_data)
        y_std = math.sqrt(sum((y - y_mean) ** 2 for y in y_data) / len(y_data))
        outlier_count = sum(1 for y in y_data if abs(y - y_mean) > 2 * y_std)
        outlier_ratio = outlier_count / len(y_data)
        
        # حساب الجودة الإجمالية
        range_quality = min(1.0, (x_range + y_range) / 10.0)
        consistency_quality = interval_consistency
        outlier_quality = 1.0 - outlier_ratio
        
        overall_quality = (range_quality + consistency_quality + outlier_quality) / 3.0
        
        return max(0.1, min(1.0, overall_quality))
    
    def _enhance_components(self, components: List[Dict[str, Any]], 
                          x_data: List[float], y_data: List[float]) -> List[Dict[str, Any]]:
        """تحسين مكونات المعادلة."""
        
        enhanced_components = []
        
        for component in components:
            enhanced_comp = component.copy()
            comp_type = component.get('type', 'unknown')
            
            # تطبيق تحسينات خاصة بالنوع
            if comp_type == 'linear':
                enhanced_comp = self._enhance_linear_component(enhanced_comp, x_data, y_data)
            elif comp_type == 'sigmoid':
                enhanced_comp = self._enhance_sigmoid_component(enhanced_comp, x_data, y_data)
            
            # تطبيق تحسين عام
            enhanced_comp['enhancement_applied'] = True
            enhanced_comp['enhancement_timestamp'] = datetime.now().isoformat()
            
            enhanced_components.append(enhanced_comp)
        
        return enhanced_components
    
    def _enhance_linear_component(self, component: Dict[str, Any], 
                                x_data: List[float], y_data: List[float]) -> Dict[str, Any]:
        """تحسين مكون خطي."""
        
        enhanced = component.copy()
        params = enhanced.get('parameters', {})
        
        # تحسين طفيف للمعاملات بناءً على التعلم
        if 'beta' in params:
            adjustment = sum(self.confidence_adjustments) * 0.01 if self.confidence_adjustments else 0.0
            params['beta'] += adjustment
        
        enhanced['parameters'] = params
        return enhanced
    
    def _enhance_sigmoid_component(self, component: Dict[str, Any], 
                                 x_data: List[float], y_data: List[float]) -> Dict[str, Any]:
        """تحسين مكون سيجمويد."""
        
        enhanced = component.copy()
        params = enhanced.get('parameters', {})
        
        # تحسين طفيف للمعاملات
        if 'k' in params:
            adjustment = sum(self.confidence_adjustments) * 0.02 if self.confidence_adjustments else 0.0
            params['k'] = max(0.1, params['k'] + adjustment)
        
        enhanced['parameters'] = params
        return enhanced
    
    def get_learning_summary(self) -> Dict[str, Any]:
        """ملخص التعلم والتحسن."""
        
        if self.total_inferences == 0:
            return {'message': 'لم يتم تنفيذ أي استنباط بعد'}
        
        # حساب الإحصائيات
        avg_confidence_adj = sum(self.confidence_adjustments) / len(self.confidence_adjustments) if self.confidence_adjustments else 0.0
        
        summary = {
            'total_inferences': self.total_inferences,
            'feedback_cycles': len(self.feedback_history),
            'confidence_adjustments': len(self.confidence_adjustments),
            'average_confidence_adjustment': avg_confidence_adj,
            'current_base_confidence': self.base_confidence,
            'adaptive_learning_rate': self.adaptive_learning_rate,
            'pattern_recognition_weights': self.pattern_recognition_weights.copy(),
            'learning_enabled': self.learning_enabled,
            'improvement_trend': self._calculate_improvement_trend()
        }
        
        return summary
    
    def _calculate_improvement_trend(self) -> str:
        """حساب اتجاه التحسن."""
        
        if len(self.confidence_adjustments) < 3:
            return 'غير كافي للتقييم'
        
        recent_adjustments = self.confidence_adjustments[-3:]
        earlier_adjustments = self.confidence_adjustments[:-3]
        
        recent_avg = sum(recent_adjustments) / len(recent_adjustments)
        earlier_avg = sum(earlier_adjustments) / len(earlier_adjustments) if earlier_adjustments else 0.0
        
        if recent_avg > earlier_avg + 0.02:
            return 'تحسن مستمر'
        elif recent_avg < earlier_avg - 0.02:
            return 'تراجع'
        else:
            return 'مستقر'
    
    def reset_learning(self):
        """إعادة تعيين نظام التعلم."""
        
        self.feedback_history.clear()
        self.confidence_adjustments.clear()
        self.base_confidence = 0.5
        self.adaptive_learning_rate = 0.05
        self.pattern_recognition_weights = {
            'linear': 1.0,
            'sigmoid': 1.0,
            'quantum': 0.8,
            'mixed': 0.9
        }
        
        print("🔄 تم إعادة تعيين نظام التعلم")
