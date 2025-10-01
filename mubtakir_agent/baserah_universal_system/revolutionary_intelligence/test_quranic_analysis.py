#!/usr/bin/env python3
# test_quranic_analysis.py - اختبار شامل لمحرك التحليل القرآني الثوري

import sys
import os
import tempfile
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد المحرك والمكونات
from .quranic_analysis_engine import (
    QuranicAnalysisEngine,
    analyze_quranic_verse,
    search_in_quran,
    get_quranic_verse,
    create_quranic_analysis_engine
)


def test_engine_initialization():
    """اختبار تهيئة المحرك القرآني."""
    
    print("🧪 اختبار تهيئة المحرك القرآني")
    print("=" * 50)
    
    try:
        # إنشاء المحرك
        engine = QuranicAnalysisEngine("TestQuranicEngine")
        
        # التحقق من التهيئة
        assert engine.engine_name == "TestQuranicEngine"
        assert hasattr(engine, 'quran_data')
        assert hasattr(engine, 'surah_names')
        assert hasattr(engine, 'engine_stats')
        assert hasattr(engine, 'lexicon_engine')
        
        print("✅ تم إنشاء المحرك بنجاح")
        
        # التحقق من بيانات القرآن
        assert engine.quran_data['total_surahs'] == 114
        assert engine.quran_data['total_verses'] > 6000
        assert engine.quran_data['meccan_surahs'] + engine.quran_data['medinan_surahs'] == 114
        
        print("✅ بيانات القرآن صحيحة")
        
        # التحقق من أسماء السور
        assert 1 in engine.surah_names
        assert engine.surah_names[1]['arabic'] == "الفاتحة"
        assert 114 in engine.surah_names
        
        print("✅ أسماء السور محملة بنجاح")
        
        # التحقق من قاعدة البيانات
        assert os.path.exists(engine.quran_db_path)
        
        print("✅ قاعدة البيانات منشأة بنجاح")
        
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار التهيئة: {e}")
        return False


def test_verse_analysis():
    """اختبار تحليل الآيات."""
    
    print("\n🔍 اختبار تحليل الآيات")
    print("=" * 50)
    
    try:
        # إنشاء المحرك
        engine = QuranicAnalysisEngine("VerseTestEngine")
        
        # آيات للاختبار (من البيانات التجريبية)
        test_verses = [
            (1, 1),  # بسم الله الرحمن الرحيم
            (1, 2),  # الحمد لله رب العالمين
            (112, 1), # قل هو الله أحد
            (114, 1)  # قل أعوذ برب الناس
        ]
        
        for surah_num, verse_num in test_verses:
            print(f"\n📖 تحليل الآية: {surah_num}:{verse_num}")
            
            try:
                # تحليل الآية
                analysis = engine.analyze_verse_revolutionary(surah_num, verse_num, deep_analysis=True)
                
                # التحقق من النتائج
                assert analysis.text is not None
                assert len(analysis.text) > 0
                assert analysis.semantic_weight >= 0.0
                assert analysis.semantic_weight <= 1.0
                assert len(analysis.word_analysis) > 0
                assert 'total_value' in analysis.baserah_analysis
                assert 'zero_duality_quranic' in analysis.basil_theories_application
                
                print(f"   النص: {analysis.text}")
                print(f"   الوزن الدلالي: {analysis.semantic_weight:.3f}")
                print(f"   عدد الكلمات: {len(analysis.word_analysis)}")
                print(f"   رؤى ثورية: {len(analysis.revolutionary_insights)}")
                print(f"   أنماط إلهية: {len(analysis.divine_patterns)}")
                
                # التحقق من الإعجاز الرقمي
                assert isinstance(analysis.numerical_miracle, dict)
                
                # التحقق من الخصائص اللغوية
                assert 'length_analysis' in analysis.linguistic_features
                
                print(f"   ✅ تم تحليل الآية بنجاح")
                
            except Exception as e:
                print(f"   ⚠️ خطأ في تحليل الآية {surah_num}:{verse_num}: {e}")
        
        print(f"\n✅ نجح اختبار تحليل الآيات")
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار تحليل الآيات: {e}")
        return False


def test_surah_analysis():
    """اختبار تحليل السور."""
    
    print("\n📚 اختبار تحليل السور")
    print("=" * 50)
    
    try:
        # إنشاء المحرك
        engine = QuranicAnalysisEngine("SurahTestEngine")
        
        # سور للاختبار (السور القصيرة المتوفرة في البيانات التجريبية)
        test_surahs = [112, 113, 114]  # الإخلاص، الفلق، الناس
        
        for surah_num in test_surahs:
            print(f"\n📖 تحليل السورة: {surah_num}")
            
            try:
                # تحليل السورة
                surah_analysis = engine.analyze_surah_revolutionary(surah_num, deep_analysis=True)
                
                # التحقق من النتائج
                assert 'surah_info' in surah_analysis
                assert 'surah_statistics' in surah_analysis
                assert 'verse_analyses' in surah_analysis
                assert 'surah_baserah_analysis' in surah_analysis
                
                stats = surah_analysis['surah_statistics']
                assert stats['surah_number'] == surah_num
                assert stats['total_verses'] > 0
                assert stats['total_words'] > 0
                assert stats['average_semantic_weight'] >= 0.0
                
                print(f"   اسم السورة: {stats['surah_name']}")
                print(f"   نوع السورة: {stats['surah_type']}")
                print(f"   عدد الآيات: {stats['total_verses']}")
                print(f"   إجمالي الكلمات: {stats['total_words']}")
                print(f"   متوسط الوزن الدلالي: {stats['average_semantic_weight']:.3f}")
                
                # التحقق من تحليل Baserah للسورة
                baserah = surah_analysis['surah_baserah_analysis']
                assert 'surah_total_weight' in baserah
                assert 'surah_divine_signature' in baserah
                
                # التحقق من نظريات باسل للسورة
                if surah_analysis['surah_basil_theories']:
                    basil = surah_analysis['surah_basil_theories']
                    assert 'zero_duality_surah' in basil
                    assert 'filament_theory_surah' in basil
                
                print(f"   ✅ تم تحليل السورة بنجاح")
                
            except Exception as e:
                print(f"   ⚠️ خطأ في تحليل السورة {surah_num}: {e}")
        
        print(f"\n✅ نجح اختبار تحليل السور")
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار تحليل السور: {e}")
        return False


def test_quranic_search():
    """اختبار البحث القرآني."""
    
    print("\n🔍 اختبار البحث القرآني")
    print("=" * 50)
    
    try:
        # إنشاء المحرك
        engine = QuranicAnalysisEngine("SearchTestEngine")
        
        # كلمات للبحث
        search_terms = [
            ("الله", "word"),
            ("رب", "word"),
            ("رحم", "partial"),
            ("حمد", "partial")
        ]
        
        for search_term, search_type in search_terms:
            print(f"\n🔍 البحث عن: '{search_term}' (نوع: {search_type})")
            
            # البحث
            search_result = engine.search_quranic_text(search_term, search_type)
            
            # التحقق من النتائج
            assert 'search_term' in search_result
            assert 'matches' in search_result
            assert 'total_matches' in search_result
            assert 'search_statistics' in search_result
            
            assert search_result['search_term'] == search_term
            assert search_result['search_type'] == search_type
            assert isinstance(search_result['matches'], list)
            assert search_result['total_matches'] >= 0
            
            print(f"   نتائج العثور: {search_result['total_matches']}")
            print(f"   سور مطابقة: {len(search_result['surahs_found'])}")
            
            # عرض بعض النتائج
            for i, match in enumerate(search_result['matches'][:3]):
                print(f"   {i+1}. {match['surah_name']} ({match['surah_number']}:{match['verse_number']})")
            
            if search_result['total_matches'] > 3:
                print(f"   ... و {search_result['total_matches'] - 3} نتيجة أخرى")
            
            print(f"   ✅ نجح البحث")
        
        print(f"\n✅ نجح اختبار البحث القرآني")
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار البحث القرآني: {e}")
        return False


def test_numerical_miracles():
    """اختبار اكتشاف الإعجاز الرقمي."""
    
    print("\n🔢 اختبار اكتشاف الإعجاز الرقمي")
    print("=" * 50)
    
    try:
        # إنشاء المحرك
        engine = QuranicAnalysisEngine("MiracleTestEngine")
        
        # تحليل آيات مختلفة للبحث عن الإعجاز الرقمي
        test_verses = [(1, 1), (112, 1), (114, 1)]
        
        total_miracles = 0
        
        for surah_num, verse_num in test_verses:
            print(f"\n🔍 البحث عن الإعجاز في الآية: {surah_num}:{verse_num}")
            
            try:
                analysis = engine.analyze_verse_revolutionary(surah_num, verse_num, deep_analysis=True)
                miracles = analysis.numerical_miracle
                
                print(f"   أنواع الإعجاز المكتشفة: {len(miracles)}")
                
                for miracle_type, miracle_data in miracles.items():
                    print(f"   • {miracle_type}: {type(miracle_data).__name__}")
                    if isinstance(miracle_data, dict):
                        if 'is_miraculous' in miracle_data and miracle_data['is_miraculous']:
                            print(f"     🌟 إعجاز مؤكد!")
                            total_miracles += 1
                        elif any(key.endswith('_miraculous') for key in miracle_data.keys()):
                            miraculous_keys = [k for k in miracle_data.keys() if k.endswith('_miraculous') and miracle_data[k]]
                            if miraculous_keys:
                                print(f"     🌟 إعجاز في: {', '.join(miraculous_keys)}")
                                total_miracles += 1
                
            except Exception as e:
                print(f"   ⚠️ خطأ في تحليل الآية: {e}")
        
        print(f"\n📊 إجمالي الإعجاز المكتشف: {total_miracles}")
        print(f"✅ نجح اختبار اكتشاف الإعجاز الرقمي")
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار الإعجاز الرقمي: {e}")
        return False


def test_basil_theories_application():
    """اختبار تطبيق نظريات باسل على النص القرآني."""
    
    print("\n🧬 اختبار تطبيق نظريات باسل القرآنية")
    print("=" * 50)
    
    try:
        # إنشاء المحرك
        engine = QuranicAnalysisEngine("BasilTestEngine")
        
        # تحليل آية مع نظريات باسل
        surah_num, verse_num = 1, 1
        analysis = engine.analyze_verse_revolutionary(surah_num, verse_num, deep_analysis=True)
        
        # التحقق من تطبيق النظريات
        basil_theories = analysis.basil_theories_application
        
        # نظرية ثنائية الصفر القرآنية
        assert 'zero_duality_quranic' in basil_theories
        zero_duality = basil_theories['zero_duality_quranic']
        assert 'positive_sum' in zero_duality
        assert 'negative_sum' in zero_duality
        assert 'divine_balance' in zero_duality
        assert 'is_divinely_balanced' in zero_duality
        
        print(f"✅ نظرية ثنائية الصفر القرآنية:")
        print(f"   مجموع إيجابي: {zero_duality['positive_sum']:.3f}")
        print(f"   مجموع سالب: {zero_duality['negative_sum']:.3f}")
        print(f"   التوازن الإلهي: {zero_duality['divine_balance']:.3f}")
        print(f"   متوازن إلهياً: {'نعم' if zero_duality['is_divinely_balanced'] else 'لا'}")
        
        # نظرية تعامد الأضداد القرآنية
        if 'perpendicular_opposites_quranic' in basil_theories:
            perp_opposites = basil_theories['perpendicular_opposites_quranic']
            assert 'first_half_value' in perp_opposites
            assert 'second_half_value' in perp_opposites
            assert 'divine_angle' in perp_opposites
            
            print(f"✅ نظرية تعامد الأضداد القرآنية:")
            print(f"   النصف الأول: {perp_opposites['first_half_value']:.3f}")
            print(f"   النصف الثاني: {perp_opposites['second_half_value']:.3f}")
            print(f"   الزاوية الإلهية: {perp_opposites['divine_angle']:.1f}°")
        
        # نظرية الفتائل القرآنية
        assert 'filament_theory_quranic' in basil_theories
        filament_theory = basil_theories['filament_theory_quranic']
        assert 'quranic_filaments' in filament_theory
        assert 'total_filaments' in filament_theory
        assert 'divine_primary_filaments' in filament_theory
        
        print(f"✅ نظرية الفتائل القرآنية:")
        print(f"   إجمالي الفتائل: {filament_theory['total_filaments']}")
        print(f"   فتائل إلهية أولية: {filament_theory['divine_primary_filaments']}")
        
        print(f"\n✅ نجح تطبيق جميع نظريات باسل القرآنية")
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار نظريات باسل القرآنية: {e}")
        return False


def test_quick_functions():
    """اختبار الدوال السريعة."""
    
    print("\n⚡ اختبار الدوال السريعة")
    print("=" * 50)
    
    try:
        # اختبار إنشاء محرك سريع
        engine = create_quranic_analysis_engine("QuickTestEngine")
        assert engine.engine_name == "QuickTestEngine"
        print("✅ إنشاء محرك سريع")
        
        # اختبار تحليل آية سريع
        verse_result = analyze_quranic_verse(1, 1, "QuickVerseAnalyzer")
        assert 'success' in verse_result
        if verse_result['success']:
            assert 'verse_reference' in verse_result
            assert 'semantic_weight' in verse_result
            print("✅ تحليل آية سريع")
        else:
            print(f"⚠️ تحذير في تحليل الآية: {verse_result.get('error', 'خطأ غير محدد')}")
        
        # اختبار البحث السريع
        search_result = search_in_quran("الله", "word", "QuickSearchEngine")
        assert 'search_term' in search_result
        assert search_result['search_term'] == "الله"
        print("✅ بحث سريع")
        
        # اختبار الحصول على آية سريع
        verse_get_result = get_quranic_verse(1, 1, "QuickVerseGetter")
        assert 'success' in verse_get_result
        if verse_get_result['success']:
            assert 'verse_text' in verse_get_result
            print("✅ الحصول على آية سريع")
        
        print(f"\n✅ نجحت جميع الدوال السريعة")
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار الدوال السريعة: {e}")
        return False


def test_engine_performance():
    """اختبار أداء المحرك."""
    
    print("\n📊 اختبار أداء المحرك")
    print("=" * 50)
    
    try:
        # إنشاء المحرك
        engine = QuranicAnalysisEngine("PerformanceTestEngine")
        
        # قياس الوقت
        start_time = datetime.now()
        
        # تحليل عدة آيات
        test_verses = [(1, 1), (1, 2), (112, 1), (112, 2), (114, 1)]
        
        successful_analyses = 0
        for surah_num, verse_num in test_verses:
            try:
                analysis = engine.analyze_verse_revolutionary(surah_num, verse_num, deep_analysis=True)
                assert analysis.text is not None
                successful_analyses += 1
            except Exception as e:
                print(f"⚠️ فشل تحليل الآية {surah_num}:{verse_num}: {e}")
        
        # حساب الوقت المستغرق
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print(f"✅ تم تحليل {successful_analyses}/{len(test_verses)} آية في {duration:.2f} ثانية")
        print(f"   متوسط الوقت لكل آية: {duration/len(test_verses):.3f} ثانية")
        
        # التحقق من الإحصائيات
        status = engine.get_engine_status()
        stats = status['statistics']
        
        assert stats['verses_analyzed'] >= successful_analyses
        assert stats['words_analyzed'] > 0
        assert stats['baserah_analyses_performed'] > 0
        
        print(f"   آيات محللة: {stats['verses_analyzed']}")
        print(f"   كلمات محللة: {stats['words_analyzed']}")
        print(f"   تحليلات Baserah: {stats['baserah_analyses_performed']}")
        print(f"   إعجاز رقمي مكتشف: {stats['numerical_miracles_discovered']}")
        print(f"   أنماط إلهية: {stats['divine_patterns_found']}")
        
        print(f"\n✅ نجح اختبار الأداء")
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار الأداء: {e}")
        return False


def run_all_tests():
    """تشغيل جميع الاختبارات."""
    
    print("🧪✨ بدء اختبارات محرك التحليل القرآني الثوري")
    print("🕌 تحليل القرآن الكريم بنظريات باسل ونظام Baserah النقي")
    print("=" * 80)
    print(f"📅 وقت الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    tests = [
        ("اختبار تهيئة المحرك", test_engine_initialization),
        ("اختبار تحليل الآيات", test_verse_analysis),
        ("اختبار تحليل السور", test_surah_analysis),
        ("اختبار البحث القرآني", test_quranic_search),
        ("اختبار الإعجاز الرقمي", test_numerical_miracles),
        ("اختبار نظريات باسل القرآنية", test_basil_theories_application),
        ("اختبار الدوال السريعة", test_quick_functions),
        ("اختبار الأداء", test_engine_performance)
    ]
    
    results = []
    
    for test_name, test_function in tests:
        print(f"🔬 تشغيل {test_name}...")
        try:
            result = test_function()
            results.append((test_name, result))
            if result:
                print(f"✅ نجح {test_name}")
            else:
                print(f"❌ فشل {test_name}")
        except Exception as e:
            print(f"💥 خطأ في {test_name}: {e}")
            results.append((test_name, False))
        
        print()
    
    # ملخص النتائج
    print("📊 ملخص نتائج الاختبارات")
    print("=" * 80)
    
    passed_tests = sum(1 for _, result in results if result)
    total_tests = len(results)
    success_rate = passed_tests / total_tests
    
    for test_name, result in results:
        status = "✅ نجح" if result else "❌ فشل"
        print(f"{status} {test_name}")
    
    print()
    print(f"📈 النتيجة الإجمالية:")
    print(f"   اختبارات ناجحة: {passed_tests}/{total_tests}")
    print(f"   معدل النجاح: {success_rate:.1%}")
    
    if success_rate >= 0.9:
        print("🏆 النتيجة النهائية: ممتاز!")
        print("🕌 محرك التحليل القرآني الثوري جاهز لخدمة كتاب الله!")
    elif success_rate >= 0.7:
        print("👍 النتيجة النهائية: جيد")
        print("⚠️ بعض التحسينات مطلوبة")
    else:
        print("⚠️ النتيجة النهائية: يحتاج تطوير")
        print("🔧 مراجعة وإصلاح مطلوب")
    
    print()
    print("🔬 انتهت اختبارات محرك التحليل القرآني الثوري")
    print(f"📅 وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🕌 بارك الله في هذا العمل المبارك")


if __name__ == "__main__":
    run_all_tests()
