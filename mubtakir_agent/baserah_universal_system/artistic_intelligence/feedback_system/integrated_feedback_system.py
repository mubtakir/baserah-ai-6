#!/usr/bin/env python3
# integrated_feedback_system.py - النظام المتكامل للتغذية الراجعة

import sys
import os
import numpy as np
from typing import Dict, List, Tuple, Any, Optional
from datetime import datetime
import uuid

# إضافة المسار للاستيراد
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BaserahIntegratedFeedbackSystem:
    """
    النظام المتكامل للتغذية الراجعة Baserah النقي
    يجمع بين العين المستنبطة والراسم والنظام الخبير في دورة تحسين مستمرة
    """
    
    def __init__(self):
        """تهيئة النظام المتكامل."""
        
        # المكونات الأساسية
        self.enhanced_inference_engine = None
        self.feedback_mediator = None
        self.quality_assessor = None
        self.expert_system = None
        
        # إعدادات النظام
        self.max_feedback_cycles = 5
        self.target_quality = 0.95
        self.min_improvement = 0.02
        
        # إحصائيات الأداء
        self.total_sessions = 0
        self.successful_sessions = 0
        self.average_improvement = 0.0
        self.session_history = []
        
        print("🔗 تهيئة النظام المتكامل للتغذية الراجعة Baserah النقي")
        
        # تهيئة المكونات
        self._initialize_components()
    
    def _initialize_components(self):
        """تهيئة جميع المكونات."""
        
        try:
            # العين المستنبطة المحسنة
            from .enhanced_inference_engine import EnhancedBaserahInferenceEngine
            self.enhanced_inference_engine = EnhancedBaserahInferenceEngine()
            print("   ✅ تم تهيئة العين المستنبطة المحسنة")
            
            # النظام الوسيط
            from .feedback_mediator_system import BaserahFeedbackMediatorSystem
            self.feedback_mediator = BaserahFeedbackMediatorSystem()
            print("   ✅ تم تهيئة النظام الوسيط")
            
            # محرك تقييم الجودة
            from .quality_assessment_engine import BaserahQualityAssessmentEngine
            self.quality_assessor = BaserahQualityAssessmentEngine()
            print("   ✅ تم تهيئة محرك تقييم الجودة")
            
            # النظام الخبير (اختياري)
            try:
                from revolutionary_intelligence.expert_explorer_system.expert_explorer.integrated_expert_explorer import BaserahIntegratedExpertExplorer
                self.expert_system = BaserahIntegratedExpertExplorer()
                print("   ✅ تم تهيئة النظام الخبير/المستكشف")
            except ImportError:
                print("   ⚠️ النظام الخبير غير متاح - سيعمل النظام بدونه")
            
        except Exception as e:
            print(f"   ❌ خطأ في تهيئة المكونات: {e}")
    
    def run_intelligent_inference(self, input_data: List[Tuple[float, float]], 
                                 session_name: str = None) -> Dict[str, Any]:
        """
        تشغيل استنباط ذكي مع تغذية راجعة.
        
        Args:
            input_data: البيانات المدخلة [(x, y), ...]
            session_name: اسم الجلسة (اختياري)
            
        Returns:
            نتائج الاستنباط الذكي
        """
        
        session_id = f"intelligent_session_{uuid.uuid4()}"
        if session_name:
            session_id = f"{session_name}_{session_id}"
        
        self.total_sessions += 1
        
        print(f"\n🧠 بدء جلسة الاستنباط الذكي: {session_id}")
        print(f"📊 البيانات المدخلة: {len(input_data)} نقطة")
        print("=" * 60)
        
        # تحويل البيانات
        x_data = [p[0] for p in input_data]
        y_data = [p[1] for p in input_data]
        
        # المرحلة 1: الاستنباط الأولي
        print("🔍 المرحلة 1: الاستنباط الأولي")
        initial_result = self.enhanced_inference_engine.infer_from_data_points(x_data, y_data)
        initial_confidence = initial_result.get('confidence', 0.5)
        
        print(f"   📈 الثقة الأولية: {initial_confidence:.3f}")
        print(f"   📐 النوع المكتشف: {initial_result.get('type', 'غير محدد')}")
        
        # المرحلة 2: دورة التغذية الراجعة
        print("\n🔄 المرحلة 2: دورة التغذية الراجعة")
        feedback_result = self.feedback_mediator.run_feedback_cycle(
            input_data, initial_confidence
        )
        
        # المرحلة 3: الاستنباط المحسن النهائي
        print("\n🎯 المرحلة 3: الاستنباط المحسن النهائي")
        
        # استخدام أفضل تغذية راجعة
        best_feedback = feedback_result.get('feedback_summary', {})
        
        final_result = self.enhanced_inference_engine.infer_with_feedback(
            x_data, y_data, best_feedback
        )
        
        # المرحلة 4: التقييم النهائي
        print("\n📊 المرحلة 4: التقييم النهائي")
        final_quality = self._assess_final_quality(input_data, final_result)
        
        # إنشاء ملخص الجلسة
        session_summary = self._create_session_summary(
            session_id, input_data, initial_result, feedback_result, 
            final_result, final_quality
        )
        
        # حفظ في التاريخ
        self.session_history.append(session_summary)
        
        # تحديث الإحصائيات
        self._update_performance_stats(session_summary)
        
        print(f"\n✅ انتهت جلسة الاستنباط الذكي")
        print(f"📈 التحسن المحقق: +{session_summary['improvement_achieved']:.3f}")
        print(f"🎯 الجودة النهائية: {final_quality:.3f}")
        
        return session_summary
    
    def _assess_final_quality(self, original_data: List[Tuple[float, float]], 
                            inference_result: Dict[str, Any]) -> float:
        """تقييم الجودة النهائية."""
        
        try:
            # توليد البيانات من النتيجة
            x_data = [p[0] for p in original_data]
            generated_data = self._generate_data_from_result(inference_result, x_data)
            
            # تقييم الجودة
            if self.quality_assessor:
                quality_metrics = self.quality_assessor.assess_quality(original_data, generated_data)
                return quality_metrics.overall_score
            else:
                # تقييم بسيط
                return inference_result.get('confidence', 0.5)
                
        except Exception as e:
            print(f"   ⚠️ خطأ في تقييم الجودة: {e}")
            return inference_result.get('confidence', 0.5)
    
    def _generate_data_from_result(self, result: Dict[str, Any], 
                                 x_data: List[float]) -> List[Tuple[float, float]]:
        """توليد البيانات من نتيجة الاستنباط."""
        
        generated_points = []
        
        try:
            result_type = result.get('type', 'linear')
            components = result.get('components', [])
            
            for x in x_data:
                y = 0.0
                
                for component in components:
                    comp_type = component.get('type', 'linear')
                    params = component.get('parameters', {})
                    
                    if comp_type == 'linear':
                        from .baserah_core import baserah_linear
                        beta = params.get('beta', 1.0)
                        gamma = params.get('gamma', 0.0)
                        y += baserah_linear(x, beta=beta, gamma=gamma)
                    
                    elif comp_type == 'sigmoid':
                        from .baserah_core import baserah_sigmoid
                        n = params.get('n', 1)
                        k = params.get('k', 1.0)
                        x0 = params.get('x0', 0.0)
                        alpha = params.get('alpha', 1.0)
                        y += baserah_sigmoid(x, n=n, k=k, x0=x0, alpha=alpha)
                
                generated_points.append((x, y))
            
        except Exception as e:
            print(f"   ⚠️ خطأ في التوليد: {e}")
            # توليد افتراضي
            generated_points = [(x, x) for x in x_data]
        
        return generated_points
    
    def _create_session_summary(self, session_id: str, input_data: List[Tuple[float, float]],
                              initial_result: Dict[str, Any], feedback_result: Dict[str, Any],
                              final_result: Dict[str, Any], final_quality: float) -> Dict[str, Any]:
        """إنشاء ملخص الجلسة."""
        
        initial_confidence = initial_result.get('confidence', 0.5)
        final_confidence = final_result.get('confidence', 0.5)
        improvement = final_confidence - initial_confidence
        
        summary = {
            'session_id': session_id,
            'timestamp': datetime.now(),
            'input_data_points': len(input_data),
            
            # النتائج الأولية
            'initial_confidence': initial_confidence,
            'initial_type': initial_result.get('type', 'غير محدد'),
            
            # نتائج التغذية الراجعة
            'feedback_cycles': feedback_result.get('total_iterations', 0),
            'feedback_converged': feedback_result.get('converged', False),
            'feedback_quality': feedback_result.get('best_quality', 0.0),
            
            # النتائج النهائية
            'final_confidence': final_confidence,
            'final_quality': final_quality,
            'final_type': final_result.get('type', 'غير محدد'),
            
            # التحسن المحقق
            'improvement_achieved': improvement,
            'quality_improvement': final_quality - initial_confidence,
            
            # تفاصيل إضافية
            'enhancement_applied': final_result.get('enhancement_applied', False),
            'feedback_incorporated': final_result.get('feedback_incorporated', False),
            'expert_system_used': self.expert_system is not None,
            
            # تقييم النجاح
            'success': final_quality >= self.target_quality or improvement >= self.min_improvement,
            'target_achieved': final_quality >= self.target_quality
        }
        
        return summary
    
    def _update_performance_stats(self, session_summary: Dict[str, Any]):
        """تحديث إحصائيات الأداء."""
        
        if session_summary['success']:
            self.successful_sessions += 1
        
        # تحديث متوسط التحسن
        all_improvements = [s['improvement_achieved'] for s in self.session_history]
        self.average_improvement = sum(all_improvements) / len(all_improvements)
    
    def run_batch_inference(self, batch_data: List[List[Tuple[float, float]]], 
                          batch_name: str = None) -> Dict[str, Any]:
        """تشغيل استنباط مجموعي مع تغذية راجعة."""
        
        batch_id = f"batch_{uuid.uuid4()}"
        if batch_name:
            batch_id = f"{batch_name}_{batch_id}"
        
        print(f"\n📦 بدء الاستنباط المجموعي: {batch_id}")
        print(f"📊 عدد المجموعات: {len(batch_data)}")
        
        batch_results = []
        total_improvement = 0.0
        successful_count = 0
        
        for i, data_set in enumerate(batch_data):
            print(f"\n--- مجموعة {i+1}/{len(batch_data)} ---")
            
            session_result = self.run_intelligent_inference(
                data_set, f"{batch_id}_set_{i+1}"
            )
            
            batch_results.append(session_result)
            total_improvement += session_result['improvement_achieved']
            
            if session_result['success']:
                successful_count += 1
        
        # ملخص المجموعة
        batch_summary = {
            'batch_id': batch_id,
            'timestamp': datetime.now(),
            'total_sets': len(batch_data),
            'successful_sets': successful_count,
            'success_rate': successful_count / len(batch_data),
            'average_improvement': total_improvement / len(batch_data),
            'total_improvement': total_improvement,
            'individual_results': batch_results
        }
        
        print(f"\n📊 ملخص الاستنباط المجموعي:")
        print(f"   نجح: {successful_count}/{len(batch_data)} ({batch_summary['success_rate']:.1%})")
        print(f"   متوسط التحسن: {batch_summary['average_improvement']:.3f}")
        
        return batch_summary
    
    def get_system_performance(self) -> Dict[str, Any]:
        """الحصول على أداء النظام الشامل."""
        
        performance = {
            'total_sessions': self.total_sessions,
            'successful_sessions': self.successful_sessions,
            'success_rate': self.successful_sessions / self.total_sessions if self.total_sessions > 0 else 0,
            'average_improvement': self.average_improvement,
            'target_quality': self.target_quality,
            'min_improvement': self.min_improvement
        }
        
        # إحصائيات المكونات
        if self.enhanced_inference_engine:
            performance['inference_engine_stats'] = self.enhanced_inference_engine.get_learning_summary()
        
        if self.feedback_mediator:
            performance['mediator_stats'] = self.feedback_mediator.get_performance_summary()
        
        if self.quality_assessor:
            performance['quality_assessor_stats'] = self.quality_assessor.get_assessment_summary()
        
        # اتجاه الأداء
        if len(self.session_history) >= 5:
            recent_success = sum(1 for s in self.session_history[-5:] if s['success'])
            performance['recent_success_rate'] = recent_success / 5
            
            recent_improvements = [s['improvement_achieved'] for s in self.session_history[-5:]]
            performance['recent_average_improvement'] = sum(recent_improvements) / len(recent_improvements)
        
        return performance
    
    def demonstrate_system(self) -> Dict[str, Any]:
        """عرض توضيحي للنظام."""
        
        print("\n🎭 عرض توضيحي للنظام المتكامل للتغذية الراجعة")
        print("=" * 60)
        
        # إنشاء بيانات اختبار
        test_datasets = [
            # بيانات خطية
            [(i, 2*i + 1) for i in range(-3, 4)],
            # بيانات سيجمويد تقريبية
            [(i, 1/(1 + np.exp(-i))) for i in range(-3, 4)],
            # بيانات مع ضوضاء
            [(i, 2*i + 1 + 0.1*np.random.randn()) for i in range(-3, 4)]
        ]
        
        demo_results = self.run_batch_inference(test_datasets, "demo")
        
        print(f"\n🎯 نتائج العرض التوضيحي:")
        print(f"   معدل النجاح: {demo_results['success_rate']:.1%}")
        print(f"   متوسط التحسن: {demo_results['average_improvement']:.3f}")
        
        return demo_results
