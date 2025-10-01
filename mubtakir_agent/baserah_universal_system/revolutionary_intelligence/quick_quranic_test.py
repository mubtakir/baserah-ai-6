#!/usr/bin/env python3
# quick_quranic_test.py - اختبار سريع لمحرك التحليل القرآني الثوري

import sys
import os
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    # استيراد المحرك
    from .quranic_analysis_engine import (
        QuranicAnalysisEngine,
        analyze_quranic_verse,
        create_quranic_analysis_engine
    )
    
    print("🕌✨ اختبار سريع لمحرك التحليل القرآني الثوري")
    print("=" * 60)
    print(f"📅 الوقت: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # إنشاء المحرك
    print("🔄 إنشاء محرك التحليل القرآني...")
    engine = QuranicAnalysisEngine("QuickTestEngine")
    print("✅ تم إنشاء المحرك بنجاح!")
    print()
    
    # اختبار تحليل آية (الفاتحة الآية الأولى)
    print("📖 اختبار تحليل آية (الفاتحة 1:1)...")
    try:
        verse_result = engine.get_verse_by_reference(1, 1)
        
        if verse_result['success']:
            print(f"✅ نجح الحصول على الآية:")
            print(f"   📚 السورة: {verse_result['surah_name']}")
            print(f"   📝 النص: {verse_result['verse_text']}")
            
            if 'analysis' in verse_result:
                analysis = verse_result['analysis']
                print(f"   ⚖️ الوزن الدلالي: {analysis['semantic_weight']:.3f}")
                print(f"   🔤 عدد الكلمات: {analysis['word_count']}")
        else:
            print(f"❌ فشل: {verse_result['error']}")
    
    except Exception as e:
        print(f"❌ خطأ في تحليل الآية: {e}")
    
    print()
    
    # اختبار البحث
    print("🔍 اختبار البحث عن كلمة 'الله'...")
    try:
        search_result = engine.search_quranic_text("الله", "word")
        print(f"✅ نتائج البحث:")
        print(f"   📊 إجمالي النتائج: {search_result['total_matches']}")
        print(f"   📚 سور مطابقة: {len(search_result['surahs_found'])}")
        
        # عرض أول نتيجة
        if search_result['matches']:
            first_match = search_result['matches'][0]
            print(f"   📖 أول نتيجة: {first_match['surah_name']} ({first_match['surah_number']}:{first_match['verse_number']})")
    
    except Exception as e:
        print(f"❌ خطأ في البحث: {e}")
    
    print()
    
    # عرض إحصائيات المحرك
    print("📊 إحصائيات المحرك:")
    try:
        status = engine.get_engine_status()
        stats = status['statistics']
        
        print(f"   آيات محللة: {stats['verses_analyzed']}")
        print(f"   كلمات محللة: {stats['words_analyzed']}")
        print(f"   إعجاز رقمي: {stats['numerical_miracles_discovered']}")
        print(f"   أنماط إلهية: {stats['divine_patterns_found']}")
        print(f"   رؤى ثورية: {stats['total_revolutionary_insights']}")
    
    except Exception as e:
        print(f"❌ خطأ في الإحصائيات: {e}")
    
    print()
    
    # اختبار الدوال السريعة
    print("⚡ اختبار الدوال السريعة...")
    try:
        # تحليل آية سريع
        quick_result = analyze_quranic_verse(1, 1, "QuickAnalyzer")
        
        if quick_result['success']:
            print(f"✅ تحليل سريع نجح:")
            print(f"   📍 المرجع: {quick_result['verse_reference']}")
            print(f"   ⚖️ الوزن الدلالي: {quick_result['semantic_weight']:.3f}")
            print(f"   💡 رؤى ثورية: {len(quick_result['revolutionary_insights'])}")
        else:
            print(f"❌ فشل التحليل السريع: {quick_result['error']}")
    
    except Exception as e:
        print(f"❌ خطأ في الدوال السريعة: {e}")
    
    print()
    print("🎉 انتهى الاختبار السريع!")
    print("🕌 الحمد لله رب العالمين")

except ImportError as e:
    print(f"❌ خطأ في استيراد المكتبات: {e}")
    print("💡 تأكد من وجود ملفات المحرك في المسار الصحيح")

except Exception as e:
    print(f"💥 خطأ عام: {e}")

print("\n" + "="*60)
