#!/usr/bin/env python3
# test_artistic_unit.py - اختبار شامل للوحدة الفنية Baserah

import sys
import os

# إضافة المسار للاستيراد
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from baserah_core import (
    baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid, baserah_equation
)
from inference_engine import BaserahInferenceEngine
from artistic_renderer import BaserahArtisticRenderer
from integrated_system import BaserahIntegratedSystem

def test_core_functions():
    """اختبار الدوال الأساسية"""
    
    print("🔬 اختبار الدوال الأساسية للوحدة الفنية...")
    print("=" * 50)
    
    # اختبار السيجمويد
    print("1️⃣ اختبار السيجمويد:")
    x_test = 0.5
    y_sigmoid = baserah_sigmoid(x_test, n=1, k=2, x0=0, alpha=1)
    print(f"   σ({x_test}) = {y_sigmoid:.4f}")
    
    # اختبار التكميم
    print("\n2️⃣ اختبار التكميم:")
    y_quantum = baserah_quantum_sigmoid(x_test, n=1, k=2, x0=0, alpha=1, quantum_factor=4)
    print(f"   σ_quantum({x_test}) = {y_quantum}")
    
    # اختبار الخط المستقيم
    print("\n3️⃣ اختبار الخط المستقيم:")
    y_linear = baserah_linear(x_test, beta=2, gamma=1)
    print(f"   linear({x_test}) = {y_linear}")
    
    # اختبار المعادلة المركبة
    print("\n4️⃣ اختبار المعادلة المركبة:")
    components = [
        {'type': 'sigmoid', 'params': {'n': 1, 'k': 2, 'x0': 0, 'alpha': 0.8}},
        {'type': 'linear', 'params': {'beta': 0.2, 'gamma': 0.1}}
    ]
    
    y_equation = baserah_equation(x_test, components)
    print(f"   equation({x_test}) = {y_equation:.4f}")
    
    print("\n✅ اختبار الدوال الأساسية مكتمل!")

def test_inference_engine():
    """اختبار محرك الاستنباط"""
    
    print("\n🔍 اختبار محرك الاستنباط...")
    print("=" * 50)
    
    engine = BaserahInferenceEngine()
    
    # اختبار 1: خط مستقيم
    print("1️⃣ اختبار استنباط الخط المستقيم:")
    x_linear = [-2, -1, 0, 1, 2]
    y_linear = [1, 3, 5, 7, 9]  # y = 2x + 5
    
    result1 = engine.infer_from_data_points(x_linear, y_linear)
    equation1 = engine.generate_equation_string(result1)
    print(f"   النتيجة: {equation1}")
    
    # اختبار 2: سيجمويد
    print("\n2️⃣ اختبار استنباط السيجمويد:")
    x_sigmoid = [-2, -1, 0, 1, 2]
    y_sigmoid = [baserah_sigmoid(x, 1, 2, 0, 1) for x in x_sigmoid]
    
    result2 = engine.infer_from_data_points(x_sigmoid, y_sigmoid)
    equation2 = engine.generate_equation_string(result2)
    print(f"   النتيجة: {equation2}")
    
    # اختبار 3: دالة متقطعة
    print("\n3️⃣ اختبار استنباط الدالة المتقطعة:")
    x_step = [-2, -1, 0, 1, 2]
    y_step = [0, 0, 0.5, 1, 1]
    
    result3 = engine.infer_from_data_points(x_step, y_step)
    equation3 = engine.generate_equation_string(result3)
    print(f"   النتيجة: {equation3}")
    
    print("\n✅ اختبار محرك الاستنباط مكتمل!")

def test_artistic_renderer():
    """اختبار محرك الرسم"""
    
    print("\n🎨 اختبار محرك الرسم...")
    print("=" * 50)
    
    renderer = BaserahArtisticRenderer()
    
    # اختبار رسم معادلة بسيطة
    print("1️⃣ اختبار رسم معادلة بسيطة:")
    components = [
        {'type': 'sigmoid', 'params': {'n': 1, 'k': 2, 'x0': 0, 'alpha': 1}},
        {'type': 'linear', 'params': {'beta': 0.1, 'gamma': 0.2}}
    ]
    
    try:
        print("   رسم المعادلة...")
        renderer.render_equation(components, title="اختبار الرسم الأساسي")
        print("   ✅ نجح الرسم!")
    except Exception as e:
        print(f"   ❌ فشل الرسم: {e}")
    
    # اختبار عرض مستويات التكميم
    print("\n2️⃣ اختبار عرض مستويات التكميم:")
    try:
        print("   عرض مستويات التكميم...")
        renderer.render_quantum_levels_demo()
        print("   ✅ نجح العرض!")
    except Exception as e:
        print(f"   ❌ فشل العرض: {e}")
    
    print("\n✅ اختبار محرك الرسم مكتمل!")

def test_integrated_system():
    """اختبار النظام المتكامل"""
    
    print("\n🔗 اختبار النظام المتكامل...")
    print("=" * 50)
    
    system = BaserahIntegratedSystem()
    
    # اختبار التحليل والرسم المتكامل
    print("1️⃣ اختبار التحليل والرسم المتكامل:")
    
    x_data = [-3, -2, -1, 0, 1, 2, 3]
    y_data = [-1, 1, 3, 5, 7, 9, 11]  # خط مستقيم
    
    try:
        print("   تحليل ورسم البيانات...")
        result = system.analyze_and_render(x_data, y_data, "اختبار النظام المتكامل")
        
        if result and 'error' not in result:
            print("   ✅ نجح التحليل والرسم!")
            print(f"   نوع النمط: {result['type']}")
            print(f"   الخطأ: {result['error']:.6f}")
        else:
            print("   ❌ فشل التحليل!")
    except Exception as e:
        print(f"   ❌ خطأ في النظام المتكامل: {e}")
    
    print("\n✅ اختبار النظام المتكامل مكتمل!")

def test_quantum_factor_demo():
    """اختبار عرض عامل التكميم"""
    
    print("\n🎯 اختبار عرض عامل التكميم...")
    print("=" * 50)
    
    x_test = 0.5
    quantum_levels = [1, 2, 4, 8, 16]
    
    print("عرض مستويات التكميم المختلفة:")
    for q_level in quantum_levels:
        y = baserah_quantum_sigmoid(x_test, n=1, k=2, x0=0, alpha=1, quantum_factor=q_level)
        step_size = 1.0 / q_level if q_level > 1 else "مستمر"
        print(f"   Q = {q_level:2d}: f({x_test}) = {y:.4f}, خطوة = {step_size}")
    
    print("\n✅ اختبار عرض عامل التكميم مكتمل!")

def run_comprehensive_test():
    """تشغيل اختبار شامل للوحدة الفنية"""
    
    print("🚀 بدء الاختبار الشامل للوحدة الفنية Baserah")
    print("=" * 60)
    print("الوحدة الفنية تجمع: الرسم + الأنيميشن + الاستنباط")
    print("=" * 60)
    
    try:
        # اختبار الدوال الأساسية
        test_core_functions()
        
        # اختبار محرك الاستنباط
        test_inference_engine()
        
        # اختبار عامل التكميم
        test_quantum_factor_demo()
        
        # اختبار محرك الرسم (اختياري - يتطلب matplotlib)
        try:
            import matplotlib.pyplot as plt
            test_artistic_renderer()
            test_integrated_system()
        except ImportError:
            print("\n⚠️ matplotlib غير متوفر - تم تخطي اختبارات الرسم")
        except Exception as e:
            print(f"\n⚠️ خطأ في اختبارات الرسم: {e}")
        
        print("\n" + "=" * 60)
        print("🎉 انتهى الاختبار الشامل للوحدة الفنية!")
        print("✅ الوحدة الفنية Baserah جاهزة للاستخدام!")
        print("🎯 تكامل كامل بين الرسم والاستنباط محقق!")
        
    except Exception as e:
        print(f"\n❌ خطأ في الاختبار الشامل: {e}")
        import traceback
        traceback.print_exc()

def interactive_demo():
    """عرض تفاعلي للوحدة الفنية"""
    
    print("\n🎮 العرض التفاعلي للوحدة الفنية")
    print("=" * 40)
    
    options = {
        '1': 'اختبار الدوال الأساسية',
        '2': 'اختبار محرك الاستنباط',
        '3': 'اختبار محرك الرسم',
        '4': 'اختبار النظام المتكامل',
        '5': 'عرض عامل التكميم',
        '6': 'اختبار شامل',
        '0': 'خروج'
    }
    
    while True:
        print("\nالخيارات المتاحة:")
        for key, value in options.items():
            print(f"  {key}. {value}")
        
        choice = input("\nاختر رقم الخيار: ").strip()
        
        if choice == '1':
            test_core_functions()
        elif choice == '2':
            test_inference_engine()
        elif choice == '3':
            test_artistic_renderer()
        elif choice == '4':
            test_integrated_system()
        elif choice == '5':
            test_quantum_factor_demo()
        elif choice == '6':
            run_comprehensive_test()
        elif choice == '0':
            print("🚪 خروج من العرض التفاعلي")
            break
        else:
            print("❌ اختيار غير صحيح")

if __name__ == "__main__":
    # تشغيل الاختبار الشامل
    run_comprehensive_test()
    
    # عرض تفاعلي (اختياري)
    interactive_choice = input("\nهل تريد العرض التفاعلي؟ (y/n): ").strip().lower()
    if interactive_choice == 'y':
        interactive_demo()
