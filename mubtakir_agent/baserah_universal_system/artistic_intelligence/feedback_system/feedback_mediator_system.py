#!/usr/bin/env python3
# feedback_mediator_system.py - النظام الوسيط للتغذية الراجعة

import sys
import os
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
import uuid
from datetime import datetime

# إضافة المسار للاستيراد
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@dataclass
class FeedbackCycle:
    """دورة تغذية راجعة واحدة."""
    cycle_id: str
    original_data: List[Tuple[float, float]]
    inferred_equations: Dict[str, Any]
    generated_data: List[Tuple[float, float]]
    quality_metrics: Any
    feedback: Dict[str, Any]
    timestamp: datetime
    improvement_achieved: float

class BaserahFeedbackMediatorSystem:
    """
    النظام الوسيط للتغذية الراجعة Baserah النقي
    يتوسط بين العين المستنبطة والراسم لتحسين الدقة
    """
    
    def __init__(self):
        """تهيئة النظام الوسيط."""
        
        # المكونات الأساسية
        self.quality_assessor = None
        self.expert_system = None
        self.inference_engine = None
        self.artistic_renderer = None
        
        # تاريخ دورات التغذية الراجعة
        self.feedback_cycles = []
        self.learning_rate = 0.05
        self.max_cycles = 10
        self.convergence_threshold = 0.95
        
        # إحصائيات الأداء
        self.total_improvements = 0
        self.successful_cycles = 0
        
        print("🤖 تم تهيئة النظام الوسيط للتغذية الراجعة Baserah النقي")
        
        # تهيئة المكونات
        self._initialize_components()
    
    def _initialize_components(self):
        """تهيئة المكونات المطلوبة."""
        
        try:
            # محرك تقييم الجودة
            from .quality_assessment_engine import BaserahQualityAssessmentEngine
            self.quality_assessor = BaserahQualityAssessmentEngine()
            print("   ✅ تم تهيئة محرك تقييم الجودة")
            
            # محرك الاستنباط
            from .inference_engine import BaserahInferenceEngine
            self.inference_engine = BaserahInferenceEngine()
            print("   ✅ تم تهيئة محرك الاستنباط")
            
            # الراسم الفني
            from .artistic_renderer import BaserahArtisticRenderer
            self.artistic_renderer = BaserahArtisticRenderer()
            print("   ✅ تم تهيئة الراسم الفني")
            
            # النظام الخبير (اختياري)
            try:
                from revolutionary_intelligence.expert_explorer_system.expert_explorer.integrated_expert_explorer import BaserahIntegratedExpertExplorer
                self.expert_system = BaserahIntegratedExpertExplorer()
                print("   ✅ تم تهيئة النظام الخبير/المستكشف")
            except ImportError:
                print("   ⚠️ النظام الخبير غير متاح - سيعمل النظام بدونه")
            
        except Exception as e:
            print(f"   ❌ خطأ في تهيئة المكونات: {e}")
    
    def run_feedback_cycle(self, original_data: List[Tuple[float, float]], 
                          initial_confidence: float = 0.5) -> Dict[str, Any]:
        """
        تشغيل دورة تغذية راجعة كاملة.
        
        Args:
            original_data: البيانات الأصلية
            initial_confidence: الثقة الأولية
            
        Returns:
            نتائج دورة التغذية الراجعة
        """
        
        cycle_id = f"feedback_cycle_{uuid.uuid4()}"
        print(f"\n🔄 بدء دورة التغذية الراجعة: {cycle_id}")
        print(f"📊 البيانات الأصلية: {len(original_data)} نقطة")
        
        best_result = None
        best_quality = 0.0
        cycle_count = 0
        
        # تحويل البيانات للاستنباط
        x_data = [p[0] for p in original_data]
        y_data = [p[1] for p in original_data]
        
        current_confidence = initial_confidence
        
        while cycle_count < self.max_cycles:
            cycle_count += 1
            print(f"\n🔄 الدورة {cycle_count}/{self.max_cycles}")
            
            # المرحلة 1: الاستنباط
            inferred_equations = self._perform_inference(x_data, y_data, current_confidence)
            
            # المرحلة 2: التوليد
            generated_data = self._generate_from_equations(inferred_equations, x_data)
            
            # المرحلة 3: التقييم
            quality_metrics = self._assess_quality(original_data, generated_data)
            
            # المرحلة 4: التحسين بالنظام الخبير
            if self.expert_system:
                enhanced_equations = self._enhance_with_expert_system(
                    inferred_equations, quality_metrics, original_data
                )
                
                # إعادة التوليد بالمعادلات المحسنة
                enhanced_generated = self._generate_from_equations(enhanced_equations, x_data)
                enhanced_quality = self._assess_quality(original_data, enhanced_generated)
                
                # اختيار الأفضل
                if enhanced_quality.overall_score > quality_metrics.overall_score:
                    inferred_equations = enhanced_equations
                    generated_data = enhanced_generated
                    quality_metrics = enhanced_quality
                    print("   🧠 تم تحسين النتائج بالنظام الخبير")
            
            # المرحلة 5: توليد التغذية الراجعة
            feedback = self.quality_assessor.generate_feedback(quality_metrics)
            
            # حفظ الدورة
            cycle = FeedbackCycle(
                cycle_id=f"{cycle_id}_iteration_{cycle_count}",
                original_data=original_data,
                inferred_equations=inferred_equations,
                generated_data=generated_data,
                quality_metrics=quality_metrics,
                feedback=feedback,
                timestamp=datetime.now(),
                improvement_achieved=quality_metrics.overall_score - best_quality
            )
            
            self.feedback_cycles.append(cycle)
            
            # تحديث أفضل نتيجة
            if quality_metrics.overall_score > best_quality:
                best_quality = quality_metrics.overall_score
                best_result = cycle
                print(f"   📈 تحسن الجودة: {quality_metrics.overall_score:.3f}")
            
            # تحديث الثقة
            current_confidence += feedback.get('confidence_adjustment', 0.0)
            current_confidence = max(0.1, min(0.99, current_confidence))
            
            # فحص التقارب
            if quality_metrics.overall_score >= self.convergence_threshold:
                print(f"   🎯 تم الوصول للتقارب المطلوب: {quality_metrics.overall_score:.3f}")
                self.successful_cycles += 1
                break
            
            # تطبيق التحسينات للدورة التالية
            if cycle_count < self.max_cycles:
                self._apply_feedback_improvements(feedback)
        
        # إحصائيات النهائية
        final_improvement = best_quality - initial_confidence
        self.total_improvements += final_improvement
        
        result = {
            'cycle_id': cycle_id,
            'total_iterations': cycle_count,
            'best_quality': best_quality,
            'final_confidence': current_confidence,
            'improvement_achieved': final_improvement,
            'converged': best_quality >= self.convergence_threshold,
            'best_equations': best_result.inferred_equations if best_result else None,
            'best_generated_data': best_result.generated_data if best_result else None,
            'feedback_summary': best_result.feedback if best_result else None
        }
        
        print(f"\n📊 نتائج دورة التغذية الراجعة:")
        print(f"   🎯 أفضل جودة: {best_quality:.3f}")
        print(f"   📈 التحسن: +{final_improvement:.3f}")
        print(f"   🔄 عدد التكرارات: {cycle_count}")
        print(f"   ✅ التقارب: {'نعم' if result['converged'] else 'لا'}")
        
        return result
    
    def _perform_inference(self, x_data: List[float], y_data: List[float], 
                          confidence: float) -> Dict[str, Any]:
        """تنفيذ الاستنباط مع الثقة المحدثة."""
        
        if not self.inference_engine:
            return {'error': 'محرك الاستنباط غير متاح'}
        
        # تنفيذ الاستنباط
        result = self.inference_engine.infer_from_data_points(x_data, y_data)
        
        # تحديث الثقة
        if 'confidence' in result:
            result['confidence'] = min(0.99, result['confidence'] + confidence * self.learning_rate)
        
        return result
    
    def _generate_from_equations(self, equations: Dict[str, Any], 
                               x_data: List[float]) -> List[Tuple[float, float]]:
        """توليد البيانات من المعادلات."""
        
        if not self.artistic_renderer or 'error' in equations:
            # توليد بسيط في حالة عدم توفر الراسم
            return [(x, 0.0) for x in x_data]
        
        try:
            # استخدام الراسم لتوليد البيانات
            generated_points = []
            
            for x in x_data:
                # تطبيق المعادلات المستنبطة
                if equations.get('type') == 'linear':
                    components = equations.get('components', [])
                    y = 0.0
                    
                    for comp in components:
                        if comp.get('type') == 'linear':
                            params = comp.get('parameters', {})
                            beta = params.get('beta', 1.0)
                            gamma = params.get('gamma', 0.0)
                            
                            from .baserah_core import baserah_linear
                            y += baserah_linear(x, beta=beta, gamma=gamma)
                
                elif equations.get('type') == 'sigmoid':
                    components = equations.get('components', [])
                    y = 0.0
                    
                    for comp in components:
                        if comp.get('type') == 'sigmoid':
                            params = comp.get('parameters', {})
                            n = params.get('n', 1)
                            k = params.get('k', 1.0)
                            x0 = params.get('x0', 0.0)
                            alpha = params.get('alpha', 1.0)
                            
                            from .baserah_core import baserah_sigmoid
                            y += baserah_sigmoid(x, n=n, k=k, x0=x0, alpha=alpha)
                
                else:
                    # افتراضي: خطي بسيط
                    y = x
                
                generated_points.append((x, y))
            
            return generated_points
            
        except Exception as e:
            print(f"   ❌ خطأ في التوليد: {e}")
            return [(x, 0.0) for x in x_data]
    
    def _assess_quality(self, original: List[Tuple[float, float]], 
                       generated: List[Tuple[float, float]]):
        """تقييم جودة البيانات المولدة."""
        
        if not self.quality_assessor:
            # تقييم بسيط في حالة عدم توفر المقيم
            class SimpleMetrics:
                def __init__(self):
                    self.overall_score = 0.5
                    self.structural_similarity = 0.5
                    self.mathematical_accuracy = 0.5
                    self.visual_fidelity = 0.5
            
            return SimpleMetrics()
        
        return self.quality_assessor.assess_quality(original, generated)
    
    def _enhance_with_expert_system(self, equations: Dict[str, Any], 
                                  quality_metrics: Any,
                                  original_data: List[Tuple[float, float]]) -> Dict[str, Any]:
        """تحسين المعادلات باستخدام النظام الخبير."""
        
        if not self.expert_system:
            return equations
        
        try:
            # استخراج البيانات للنظام الخبير
            x_data = [p[0] for p in original_data]
            y_data = [p[1] for p in original_data]
            
            # إنشاء معادلة متكيفة
            adaptive_eq = self.expert_system.create_adaptive_equation_from_data(x_data, y_data)
            
            if adaptive_eq:
                # دمج المعادلة المتكيفة مع المعادلات الأصلية
                enhanced_equations = equations.copy()
                enhanced_equations['adaptive_component'] = {
                    'type': 'adaptive',
                    'equation_id': adaptive_eq.id,
                    'components': [comp.__dict__ for comp in adaptive_eq.components]
                }
                
                return enhanced_equations
        
        except Exception as e:
            print(f"   ⚠️ خطأ في التحسين بالنظام الخبير: {e}")
        
        return equations
    
    def _apply_feedback_improvements(self, feedback: Dict[str, Any]):
        """تطبيق تحسينات التغذية الراجعة."""
        
        # تحديث معاملات التعلم
        if 'confidence_adjustment' in feedback:
            adjustment = feedback['confidence_adjustment']
            if adjustment > 0:
                self.learning_rate = min(0.1, self.learning_rate * 1.1)
            else:
                self.learning_rate = max(0.01, self.learning_rate * 0.9)
        
        # تطبيق تحسينات محددة
        specific_adjustments = feedback.get('specific_adjustments', {})
        for area, adjustment in specific_adjustments.items():
            print(f"   🔧 تطبيق تحسين {area}: {adjustment}")
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """ملخص أداء النظام الوسيط."""
        
        if not self.feedback_cycles:
            return {'message': 'لا توجد دورات تغذية راجعة بعد'}
        
        # حساب الإحصائيات
        total_cycles = len(self.feedback_cycles)
        quality_scores = [cycle.quality_metrics.overall_score for cycle in self.feedback_cycles]
        improvements = [cycle.improvement_achieved for cycle in self.feedback_cycles]
        
        summary = {
            'total_feedback_cycles': total_cycles,
            'successful_cycles': self.successful_cycles,
            'success_rate': self.successful_cycles / total_cycles if total_cycles > 0 else 0,
            'average_quality': sum(quality_scores) / len(quality_scores),
            'best_quality': max(quality_scores),
            'total_improvement': sum(improvements),
            'average_improvement': sum(improvements) / len(improvements),
            'current_learning_rate': self.learning_rate,
            'convergence_rate': self.successful_cycles / total_cycles if total_cycles > 0 else 0
        }
        
        return summary
