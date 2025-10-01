#!/usr/bin/env python3
# simple_demo.py - عرض تفاعلي بسيط للنظام الثوري Baserah

import sys
import time
from datetime import datetime

def print_header():
    """طباعة رأس البرنامج."""
    print("\n" + "=" * 60)
    print("🌟 النظام الثوري Baserah - عرض تفاعلي")
    print("=" * 60)
    print(f"📅 التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🎯 نظام ذكي ثوري بدون مكتبات ذكاء اصطناعي تقليدي")
    print("🔧 يستخدم فقط: السيجمويد + المعادلات الخطية")
    print("=" * 60)

def demo_basic_functions():
    """عرض الدوال الأساسية."""
    print("\n🔧 عرض الدوال الأساسية:")
    print("-" * 30)
    
    try:
        from artistic_intelligence.baserah_core import baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid
        
        print("📊 اختبار دالة السيجمويد:")
        for x in [-2, -1, 0, 1, 2]:
            result = baserah_sigmoid(x, n=2, k=1.5, x0=0.0, alpha=1.0)
            print(f"   sigmoid({x}) = {result:.4f}")
        
        print("\n📈 اختبار الدالة الخطية:")
        for x in [-2, -1, 0, 1, 2]:
            result = baserah_linear(x, beta=0.8, gamma=0.2)
            print(f"   linear({x}) = {result:.4f}")
        
        print("\n🔬 اختبار السيجمويد الكمي:")
        for x in [0, 1, 2]:
            result = baserah_quantum_sigmoid(x, quantum_factor=4)
            print(f"   quantum_sigmoid({x}) = {result:.4f}")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في الدوال الأساسية: {e}")
        return False

def demo_shapes_database():
    """عرض قاعدة بيانات الأشكال."""
    print("\n🗄️ عرض قاعدة بيانات الأشكال:")
    print("-" * 35)
    
    try:
        from knowledge_systems.shapes_database.shapes_database import BaserahShapesDatabase
        
        # إنشاء قاعدة البيانات
        db = BaserahShapesDatabase()
        print(f"✅ تم تحميل {len(db.shapes)} شكل أساسي")
        
        # عرض الأشكال حسب النوع
        from knowledge_systems.shapes_database.shapes_database import ShapeType
        for shape_type in ShapeType:
            shapes = db.get_shapes_by_type(shape_type)
            print(f"   📊 {shape_type.value}: {len(shapes)} شكل")
        
        # البحث عن أشكال
        print("\n🔍 البحث في الأشكال:")
        search_terms = ['قطة', 'دائرة', 'مربع', 'فني']
        for term in search_terms:
            results = db.search_shapes(term)
            print(f"   '{term}': {len(results)} نتيجة")
            for result in results[:2]:  # أول نتيجتين
                print(f"     - {result.metadata.name_ar}")
        
        # تحويل بين الأشكال
        print("\n🔄 تحويل بين الأشكال:")
        transformation = db.get_transformation_sequence('square_basic', 'circle_basic', 5)
        print(f"   مربع → دائرة: {len(transformation)} خطوة")
        for i, step in enumerate(transformation[:3]):  # أول 3 خطوات
            print(f"     خطوة {i+1}: تقدم {step['progress']:.2f}")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في قاعدة البيانات: {e}")
        return False

def demo_mother_system():
    """عرض النظام الأم."""
    print("\n🌟 عرض النظام الأم الثوري:")
    print("-" * 32)
    
    try:
        from revolutionary_intelligence.revolutionary_mother_system.revolutionary_mother_system import BaserahRevolutionaryMotherSystem
        
        # إنشاء النظام الأم
        mother = BaserahRevolutionaryMotherSystem()
        print(f"✅ تم إنشاء النظام الأم: {mother.system_id}")
        
        # عرض ملخص النظام
        summary = mother.get_system_summary()
        print(f"📊 نقاء Baserah: {summary['baserah_purity']:.1%}")
        print(f"📈 إجمالي الوراثات: {summary['total_inheritances']}")
        print(f"🔄 إجمالي التكيفات: {summary['total_adaptations']}")
        
        # معلومات قاعدة البيانات
        shapes_info = summary.get('shapes_database', {})
        if shapes_info:
            print(f"🗄️ قاعدة البيانات: {shapes_info.get('total_shapes', 0)} شكل")
            print(f"🎬 أشكال متحركة: {shapes_info.get('animated_shapes', 0)}")
        
        # اختبار الوصول للأشكال
        print("\n🔍 اختبار الوصول للأشكال:")
        square = mother.get_shape('square_basic')
        if square:
            print(f"   ✅ المربع: {square.metadata.name_ar}")
            print(f"      التعقيد: {square.complexity_level.value}")
            print(f"      المعادلات: {len(square.equations)}")
        
        circle = mother.get_shape('circle_basic')
        if circle:
            print(f"   ✅ الدائرة: {circle.metadata.name_ar}")
            print(f"      الجمال الرياضي: {circle.metadata.mathematical_beauty}")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في النظام الأم: {e}")
        return False

def demo_expert_system():
    """عرض النظام الخبير."""
    print("\n🧠 عرض النظام الخبير/المستكشف:")
    print("-" * 38)
    
    try:
        from revolutionary_intelligence.expert_explorer_system.expert_explorer.integrated_expert_explorer import BaserahIntegratedExpertExplorer
        
        # إنشاء النظام الخبير
        expert = BaserahIntegratedExpertExplorer()
        print(f"✅ تم إنشاء النظام الخبير")
        print(f"🧬 معادلات متكيفة: {len(expert.adaptive_equations)}")
        
        # إنشاء معادلة متكيفة من بيانات
        print("\n🔬 إنشاء معادلة متكيفة:")
        x_data = [0, 1, 2, 3, 4]
        y_data = [0, 1, 4, 9, 16]  # دالة تربيعية
        
        print(f"   البيانات: x = {x_data}")
        print(f"   البيانات: y = {y_data}")
        
        adaptive_eq = expert.create_adaptive_equation_from_data(x_data, y_data)
        if adaptive_eq:
            print(f"   ✅ تم إنشاء معادلة: {adaptive_eq.id}")
            print(f"   📊 المكونات: {len(adaptive_eq.components)}")
            print(f"   🎯 اللياقة: {adaptive_eq.current_fitness:.4f}")
        
        # اختبار التطوير
        print("\n🔧 اختبار التطوير:")
        evolution = expert.evolve_adaptive_equations(x_data, y_data, population_size=3)
        if evolution['evolution_success']:
            print(f"   ✅ نجح التطوير")
            print(f"   🏆 أفضل لياقة: {evolution['best_fitness']:.4f}")
            print(f"   🔄 أجيال: {evolution['generations']}")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في النظام الخبير: {e}")
        return False

def interactive_menu():
    """قائمة تفاعلية للمستخدم."""
    print("\n🎮 القائمة التفاعلية:")
    print("-" * 25)
    print("1. عرض الدوال الأساسية")
    print("2. عرض قاعدة بيانات الأشكال")
    print("3. عرض النظام الأم")
    print("4. عرض النظام الخبير")
    print("5. عرض شامل لجميع المكونات")
    print("6. خروج")
    
    while True:
        try:
            choice = input("\n🎯 اختر رقم (1-6): ").strip()
            
            if choice == '1':
                demo_basic_functions()
            elif choice == '2':
                demo_shapes_database()
            elif choice == '3':
                demo_mother_system()
            elif choice == '4':
                demo_expert_system()
            elif choice == '5':
                print("\n🚀 عرض شامل لجميع المكونات:")
                print("=" * 45)
                demo_basic_functions()
                demo_shapes_database()
                demo_mother_system()
                demo_expert_system()
                print("\n🎉 انتهى العرض الشامل!")
            elif choice == '6':
                print("\n👋 شكراً لاستخدام النظام الثوري Baserah!")
                break
            else:
                print("❌ اختيار غير صحيح، حاول مرة أخرى")
                
        except KeyboardInterrupt:
            print("\n\n👋 تم إنهاء البرنامج")
            break
        except Exception as e:
            print(f"❌ خطأ: {e}")

def auto_demo():
    """عرض تلقائي لجميع المكونات."""
    print("\n🤖 العرض التلقائي:")
    print("-" * 20)
    
    demos = [
        ("الدوال الأساسية", demo_basic_functions),
        ("قاعدة بيانات الأشكال", demo_shapes_database),
        ("النظام الأم", demo_mother_system),
        ("النظام الخبير", demo_expert_system)
    ]
    
    results = []
    
    for name, demo_func in demos:
        print(f"\n⏳ تشغيل {name}...")
        time.sleep(1)  # توقف قصير للتأثير
        
        try:
            result = demo_func()
            results.append((name, result))
            if result:
                print(f"✅ {name}: نجح")
            else:
                print(f"❌ {name}: فشل")
        except Exception as e:
            print(f"❌ {name}: خطأ - {e}")
            results.append((name, False))
        
        time.sleep(0.5)
    
    # ملخص النتائج
    print("\n" + "=" * 50)
    print("📊 ملخص نتائج العرض التلقائي:")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ نجح" if result else "❌ فشل"
        print(f"   {name}: {status}")
    
    success_rate = passed / total
    print(f"\n📈 معدل النجاح: {success_rate:.1%} ({passed}/{total})")
    
    if success_rate >= 0.8:
        print("\n🎉 النظام الثوري Baserah يعمل بنجاح!")
        print("✨ جميع المكونات الأساسية تعمل بشكل ممتاز")
    else:
        print("\n⚠️ بعض المكونات تحتاج مراجعة")

def main():
    """الدالة الرئيسية."""
    print_header()
    
    print("\n🎯 اختر نوع العرض:")
    print("1. عرض تلقائي شامل")
    print("2. قائمة تفاعلية")
    
    try:
        choice = input("\nاختر (1 أو 2): ").strip()
        
        if choice == '1':
            auto_demo()
        elif choice == '2':
            interactive_menu()
        else:
            print("🤖 سيتم تشغيل العرض التلقائي...")
            auto_demo()
            
    except KeyboardInterrupt:
        print("\n\n👋 تم إنهاء البرنامج")
    except Exception as e:
        print(f"\n❌ خطأ: {e}")

if __name__ == "__main__":
    main()
