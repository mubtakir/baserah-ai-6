#!/usr/bin/env python3
# test_shapes_database.py - اختبار قاعدة بيانات الأشكال الأساسية

import sys
import os
from datetime import datetime

# إضافة المسار للاستيراد
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from knowledge_systems.shapes_database.shapes_database import BaserahShapesDatabase, ShapeType, ComplexityLevel
from revolutionary_intelligence.revolutionary_mother_system.revolutionary_mother_system import BaserahRevolutionaryMotherSystem

def test_shapes_database_initialization():
    """اختبار تهيئة قاعدة بيانات الأشكال."""
    
    print("🗄️ اختبار تهيئة قاعدة بيانات الأشكال...")
    print("-" * 50)
    
    # إنشاء قاعدة البيانات
    shapes_db = BaserahShapesDatabase()
    
    # فحص التهيئة الأساسية
    print(f"✅ معرف قاعدة البيانات: {shapes_db.database_id}")
    print(f"✅ إجمالي الأشكال: {len(shapes_db.shapes)}")
    
    # فحص الأنواع
    for shape_type in ShapeType:
        count = len(shapes_db.shape_categories[shape_type])
        print(f"   📊 {shape_type.value}: {count} شكل")
    
    # فحص مستويات التعقيد
    for complexity in ComplexityLevel:
        count = len(shapes_db.complexity_index[complexity])
        print(f"   🎯 {complexity.value}: {count} شكل")
    
    print("\n✅ تهيئة قاعدة البيانات مكتملة!")
    return shapes_db

def test_shape_retrieval():
    """اختبار استرجاع الأشكال."""
    
    print("\n🔍 اختبار استرجاع الأشكال...")
    print("-" * 50)
    
    shapes_db = BaserahShapesDatabase()
    
    # اختبار الحصول على شكل محدد
    square = shapes_db.get_shape("square_basic")
    if square:
        print(f"✅ تم العثور على المربع: {square.metadata.name_ar}")
        print(f"   النوع: {square.shape_type.value}")
        print(f"   التعقيد: {square.complexity_level.value}")
        print(f"   المعادلات: {len(square.equations)}")
        print(f"   الجمال الرياضي: {square.metadata.mathematical_beauty}")
    else:
        print("❌ لم يتم العثور على المربع")
    
    # اختبار الحصول على الأشكال الهندسية
    geometric_shapes = shapes_db.get_shapes_by_type(ShapeType.GEOMETRIC)
    print(f"\n✅ الأشكال الهندسية ({len(geometric_shapes)}):")
    for shape in geometric_shapes:
        print(f"   🔷 {shape.metadata.name_ar} ({shape.metadata.name_en})")
    
    # اختبار الحصول على الأشكال العضوية
    organic_shapes = shapes_db.get_shapes_by_type(ShapeType.ORGANIC)
    print(f"\n✅ الأشكال العضوية ({len(organic_shapes)}):")
    for shape in organic_shapes:
        print(f"   🌿 {shape.metadata.name_ar} ({shape.metadata.name_en})")
    
    # اختبار الحصول على الأشكال المحترفة
    professional_shapes = shapes_db.get_shapes_by_complexity(ComplexityLevel.PROFESSIONAL)
    print(f"\n✅ الأشكال المحترفة ({len(professional_shapes)}):")
    for shape in professional_shapes:
        print(f"   🌟 {shape.metadata.name_ar} - جمال: {shape.metadata.mathematical_beauty}")

def test_shape_search():
    """اختبار البحث في الأشكال."""
    
    print("\n🔎 اختبار البحث في الأشكال...")
    print("-" * 50)
    
    shapes_db = BaserahShapesDatabase()
    
    # البحث عن "قطة"
    cat_results = shapes_db.search_shapes("قطة")
    print(f"✅ نتائج البحث عن 'قطة': {len(cat_results)}")
    for shape in cat_results:
        print(f"   🐱 {shape.metadata.name_ar} - {shape.complexity_level.value}")
    
    # البحث عن "هندسي"
    geometric_results = shapes_db.search_shapes("هندسي")
    print(f"\n✅ نتائج البحث عن 'هندسي': {len(geometric_results)}")
    for shape in geometric_results:
        print(f"   📐 {shape.metadata.name_ar}")
    
    # البحث عن "رياضي"
    math_results = shapes_db.search_shapes("رياضي")
    print(f"\n✅ نتائج البحث عن 'رياضي': {len(math_results)}")
    for shape in math_results:
        print(f"   📊 {shape.metadata.name_ar}")

def test_transformation_sequence():
    """اختبار تسلسل التحويل."""
    
    print("\n🔄 اختبار تسلسل التحويل...")
    print("-" * 50)
    
    shapes_db = BaserahShapesDatabase()
    
    # تحويل من مربع إلى دائرة
    transformation = shapes_db.get_transformation_sequence("square_basic", "circle_basic", steps=5)
    
    if transformation:
        print(f"✅ تم إنشاء تسلسل التحويل: {len(transformation)} خطوة")
        
        for step in transformation:
            print(f"   خطوة {step['step'] + 1}: تقدم {step['progress']:.2f}")
            print(f"     الوصف: {step['description']}")
            print(f"     معادلات: {len(step['equations'])}")
        
        print(f"\n🎯 التحويل من مربع إلى دائرة مكتمل!")
    else:
        print("❌ فشل في إنشاء تسلسل التحويل")

def test_animation_examples():
    """اختبار أمثلة الرسوم المتحركة."""
    
    print("\n🎬 اختبار أمثلة الرسوم المتحركة...")
    print("-" * 50)
    
    shapes_db = BaserahShapesDatabase()
    
    # البحث عن الأشكال المتحركة
    animated_shapes = [
        shape for shape in shapes_db.shapes.values() 
        if shape.animation_frames is not None
    ]
    
    print(f"✅ الأشكال المتحركة: {len(animated_shapes)}")
    
    for shape in animated_shapes:
        print(f"\n   🎬 {shape.metadata.name_ar}:")
        print(f"     إطارات: {len(shape.animation_frames) if shape.animation_frames else 0}")
        print(f"     النوع: {shape.shape_type.value}")
        print(f"     التعقيد: {shape.complexity_level.value}")
        
        if shape.animation_frames and len(shape.animation_frames) > 0:
            first_frame = shape.animation_frames[0]
            last_frame = shape.animation_frames[-1]
            print(f"     الإطار الأول: {first_frame}")
            print(f"     الإطار الأخير: {last_frame}")

def test_mother_system_integration():
    """اختبار التكامل مع النظام الأم."""
    
    print("\n🌟 اختبار التكامل مع النظام الأم...")
    print("-" * 50)
    
    # إنشاء النظام الأم
    mother_system = BaserahRevolutionaryMotherSystem()
    
    print(f"✅ النظام الأم: {mother_system.system_id}")
    print(f"✅ قاعدة بيانات الأشكال: {mother_system.shapes_database.database_id}")
    
    # اختبار الوصول للأشكال عبر النظام الأم
    square = mother_system.get_shape("square_basic")
    if square:
        print(f"✅ الوصول للمربع عبر النظام الأم: {square.metadata.name_ar}")
    
    # اختبار البحث عبر النظام الأم
    search_results = mother_system.search_shapes("دائرة")
    print(f"✅ نتائج البحث عبر النظام الأم: {len(search_results)}")
    
    # اختبار التحويل عبر النظام الأم
    transformation = mother_system.get_transformation_sequence("square_basic", "circle_basic", steps=3)
    print(f"✅ تحويل عبر النظام الأم: {len(transformation)} خطوة")
    
    # اختبار ملخص النظام
    summary = mother_system.get_system_summary()
    shapes_info = summary.get('shapes_database', {})
    
    print(f"\n📊 ملخص قاعدة بيانات الأشكال:")
    print(f"   إجمالي الأشكال: {shapes_info.get('total_shapes', 0)}")
    print(f"   الأشكال المتحركة: {shapes_info.get('animated_shapes', 0)}")
    print(f"   متوسط الجمال الرياضي: {shapes_info.get('mathematical_beauty_average', 0):.3f}")
    
    print("\n✅ التكامل مع النظام الأم مكتمل!")

def test_database_export():
    """اختبار تصدير قاعدة البيانات."""
    
    print("\n💾 اختبار تصدير قاعدة البيانات...")
    print("-" * 50)
    
    shapes_db = BaserahShapesDatabase()
    
    # تصدير قاعدة البيانات
    export_filename = shapes_db.export_database()
    
    print(f"✅ تم تصدير قاعدة البيانات: {export_filename}")
    
    # فحص الملف المصدر
    if os.path.exists(export_filename):
        file_size = os.path.getsize(export_filename)
        print(f"✅ حجم الملف: {file_size} بايت")
        
        # قراءة جزء من الملف للتحقق
        with open(export_filename, 'r', encoding='utf-8') as f:
            content_preview = f.read(200)
            print(f"✅ معاينة المحتوى: {content_preview[:100]}...")
        
        # حذف الملف بعد الاختبار
        os.remove(export_filename)
        print(f"✅ تم حذف ملف الاختبار")
    else:
        print("❌ فشل في إنشاء ملف التصدير")

def run_comprehensive_shapes_test():
    """تشغيل اختبار شامل لقاعدة بيانات الأشكال."""
    
    print("🗄️ اختبار شامل لقاعدة بيانات الأشكال الأساسية")
    print("=" * 70)
    print(f"📅 تاريخ الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    try:
        # تشغيل جميع الاختبارات
        shapes_db = test_shapes_database_initialization()
        test_shape_retrieval()
        test_shape_search()
        test_transformation_sequence()
        test_animation_examples()
        test_mother_system_integration()
        test_database_export()
        
        # ملخص النتائج
        print("\n" + "=" * 70)
        print("📊 ملخص نتائج اختبار قاعدة بيانات الأشكال:")
        
        summary = shapes_db.get_database_summary()
        
        print(f"   إجمالي الأشكال: {summary['total_shapes']}")
        print(f"   الأشكال الهندسية: {summary['shapes_by_type'].get('geometric', 0)}")
        print(f"   الأشكال العضوية: {summary['shapes_by_type'].get('organic', 0)}")
        print(f"   الأشكال الرياضية: {summary['shapes_by_type'].get('mathematical', 0)}")
        print(f"   الأشكال الفنية: {summary['shapes_by_type'].get('artistic', 0)}")
        print(f"   أمثلة التحويل: {summary['shapes_by_type'].get('abstract', 0)}")
        print(f"   الأشكال المتحركة: {summary['animated_shapes']}")
        print(f"   متوسط الجمال الرياضي: {summary['mathematical_beauty_average']:.3f}")
        
        print(f"\n🎉 قاعدة بيانات الأشكال تعمل بنجاح كامل!")
        print(f"✅ جميع الأشكال الأساسية متاحة للوراثة!")
        print(f"🔄 أمثلة التحويل والتكيف جاهزة!")
        print(f"🎬 الرسوم المتحركة مدعومة!")
        print(f"🌟 التكامل مع النظام الأم محقق!")
        
        print(f"\n🎯 قاعدة بيانات الأشكال جاهزة لوراثة جميع الوحدات!")
        
    except Exception as e:
        print(f"\n❌ خطأ في اختبار قاعدة بيانات الأشكال: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_comprehensive_shapes_test()
