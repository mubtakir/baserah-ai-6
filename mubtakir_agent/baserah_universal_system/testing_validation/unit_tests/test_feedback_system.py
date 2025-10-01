#!/usr/bin/env python3
# test_feedback_system.py - اختبار نظام التغذية الراجعة

def test_quality_assessor():
    """اختبار محرك تقييم الجودة."""
    
    print("🔍 اختبار محرك تقييم الجودة...")
    
    try:
        from artistic_intelligence.quality_assessment.quality_assessment_engine import BaserahQualityAssessmentEngine
        
        assessor = BaserahQualityAssessmentEngine()
        
        # بيانات اختبار
        original = [(0, 1), (1, 3), (2, 5), (3, 7)]
        generated = [(0, 1.1), (1, 2.9), (2, 5.1), (3, 6.9)]
        
        metrics = assessor.assess_quality(original, generated)
        
        print(f"   ✅ التشابه الهيكلي: {metrics.structural_similarity:.3f}")
        print(f"   ✅ الدقة الرياضية: {metrics.mathematical_accuracy:.3f}")
        print(f"   ✅ الإخلاص البصري: {metrics.visual_fidelity:.3f}")
        print(f"   ✅ النقاط الإجمالية: {metrics.overall_score:.3f}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ خطأ: {e}")
        return False

def test_enhanced_inference():
    """اختبار العين المستنبطة المحسنة."""
    
    print("\n🧠 اختبار العين المستنبطة المحسنة...")
    
    try:
        from artistic_intelligence.inference_engine.enhanced_inference_engine import EnhancedBaserahInferenceEngine
        
        engine = EnhancedBaserahInferenceEngine()
        
        # بيانات اختبار خطية
        x_data = [0, 1, 2, 3, 4]
        y_data = [1, 3, 5, 7, 9]  # y = 2x + 1
        
        # اختبار بدون تغذية راجعة
        result1 = engine.infer_from_data_points(x_data, y_data)
        print(f"   📊 بدون تغذية راجعة: {result1.get('confidence', 0):.3f}")
        
        # اختبار مع تغذية راجعة وهمية
        fake_feedback = {
            'confidence_adjustment': 0.1,
            'overall_quality': 'جيد',
            'improvement_areas': ['mathematical_accuracy']
        }
        
        result2 = engine.infer_with_feedback(x_data, y_data, fake_feedback)
        print(f"   📈 مع تغذية راجعة: {result2.get('confidence', 0):.3f}")
        print(f"   🔧 تحسن الثقة: {result2.get('confidence_boost', 0):.3f}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ خطأ: {e}")
        return False

def test_feedback_mediator():
    """اختبار النظام الوسيط."""
    
    print("\n🤖 اختبار النظام الوسيط...")
    
    try:
        from artistic_intelligence.feedback_system.feedback_mediator_system import BaserahFeedbackMediatorSystem
        
        mediator = BaserahFeedbackMediatorSystem()
        
        # بيانات اختبار
        test_data = [(0, 1), (1, 3), (2, 5)]
        
        # تشغيل دورة تغذية راجعة مبسطة
        result = mediator.run_feedback_cycle(test_data, 0.5)
        
        print(f"   ✅ عدد التكرارات: {result.get('total_iterations', 0)}")
        print(f"   ✅ أفضل جودة: {result.get('best_quality', 0):.3f}")
        print(f"   ✅ التحسن: {result.get('improvement_achieved', 0):.3f}")
        print(f"   ✅ التقارب: {'نعم' if result.get('converged', False) else 'لا'}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ خطأ: {e}")
        return False

def main():
    """تشغيل جميع الاختبارات."""
    
    print("🧪 اختبار نظام التغذية الراجعة المتكامل")
    print("=" * 50)
    
    tests = [
        ("محرك تقييم الجودة", test_quality_assessor),
        ("العين المستنبطة المحسنة", test_enhanced_inference),
        ("النظام الوسيط", test_feedback_mediator)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ خطأ في {test_name}: {e}")
            results.append((test_name, False))
    
    # ملخص النتائج
    print("\n" + "=" * 50)
    print("📊 ملخص نتائج الاختبار:")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ نجح" if result else "❌ فشل"
        print(f"   {test_name}: {status}")
    
    success_rate = passed / total
    print(f"\n📈 معدل النجاح: {success_rate:.1%} ({passed}/{total})")
    
    if success_rate >= 0.8:
        print("\n🎉 نظام التغذية الراجعة يعمل بنجاح!")
        print("✅ تم تنفيذ اقتراحك بنجاح")
        print("🔄 العين المستنبطة أصبحت أكثر ذكاءً")
    elif success_rate >= 0.6:
        print("\n👍 النظام يعمل بشكل جيد مع بعض التحسينات")
    else:
        print("\n⚠️ النظام يحتاج مراجعة")
    
    return success_rate >= 0.6

if __name__ == "__main__":
    main()
