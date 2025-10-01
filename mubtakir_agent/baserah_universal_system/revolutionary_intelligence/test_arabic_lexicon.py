#!/usr/bin/env python3
# test_arabic_lexicon.py - اختبار شامل لمحرك المعجم العربي الثوري

import sys
import os
import tempfile
import shutil
from datetime import datetime

# إضافة المسار للوصول للمكتبات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد المحرك والمكونات
from .arabic_lexicon_engine import (
    ArabicLexiconEngine, 
    analyze_arabic_word,
    explore_arabic_letter,
    analyze_arabic_text,
    create_arabic_lexicon_engine
)

from .lexicon_data_loader import (
    LexiconDataLoader,
    quick_load_lexicon_data,
    create_sample_lexicon_files
)


def test_engine_initialization():
    """اختبار تهيئة المحرك."""
    
    print("🧪 اختبار تهيئة المحرك")
    print("=" * 50)
    
    try:
        # إنشاء المحرك
        engine = ArabicLexiconEngine("TestEngine")
        
        # التحقق من التهيئة
        assert engine.engine_name == "TestEngine"
        assert hasattr(engine, 'letter_meanings')
        assert hasattr(engine, 'integrated_lexicons')
        assert hasattr(engine, 'engine_stats')
        
        print("✅ تم إنشاء المحرك بنجاح")
        
        # التحقق من دلالات الحروف
        assert len(engine.letter_meanings) > 20  # على الأقل 20 حرف
        assert 'ا' in engine.letter_meanings
        assert 'ع' in engine.letter_meanings
        assert 'م' in engine.letter_meanings
        
        print("✅ دلالات الحروف محملة بنجاح")
        
        # التحقق من قاعدة البيانات
        assert os.path.exists(engine.lexicon_db_path)
        
        print("✅ قاعدة البيانات منشأة بنجاح")
        
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار التهيئة: {e}")
        return False


def test_word_analysis():
    """اختبار تحليل الكلمات."""
    
    print("\n🔍 اختبار تحليل الكلمات")
    print("=" * 50)
    
    try:
        # إنشاء المحرك
        engine = ArabicLexiconEngine("WordTestEngine")
        
        # كلمات للاختبار
        test_words = ['الله', 'حياة', 'علم', 'حكمة', 'سلام']
        
        for word in test_words:
            print(f"\n🔤 تحليل كلمة: {word}")
            
            # تحليل الكلمة
            analysis = engine.analyze_word_revolutionary(word, deep_analysis=True)
            
            # التحقق من النتائج
            assert analysis.word == word
            assert analysis.meaning is not None
            assert analysis.semantic_weight >= 0.0
            assert analysis.semantic_weight <= 1.0
            assert len(analysis.letter_analysis) > 0
            assert 'total_value' in analysis.baserah_analysis
            assert 'zero_duality' in analysis.basil_theories_application
            
            print(f"   المعنى: {analysis.meaning}")
            print(f"   الجذر: {analysis.root}")
            print(f"   الوزن الدلالي: {analysis.semantic_weight:.3f}")
            print(f"   عدد الحروف المحللة: {len(analysis.letter_analysis)}")
            
            # التحقق من تحليل الحروف
            for letter, meaning in analysis.letter_analysis.items():
                assert letter in word
                assert len(meaning) > 0
            
            print(f"   ✅ تم تحليل الكلمة بنجاح")
        
        print(f"\n✅ نجح تحليل جميع الكلمات ({len(test_words)} كلمة)")
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار تحليل الكلمات: {e}")
        return False


def test_letter_analysis():
    """اختبار تحليل الحروف."""
    
    print("\n🔤 اختبار تحليل الحروف")
    print("=" * 50)
    
    try:
        # إنشاء المحرك
        engine = ArabicLexiconEngine("LetterTestEngine")
        
        # حروف للاختبار
        test_letters = ['ا', 'ب', 'ع', 'م', 'ن', 'ل', 'ه']
        
        for letter in test_letters:
            print(f"\n📝 تحليل حرف: {letter}")
            
            # تحليل الحرف
            analysis = engine.explore_letter_meanings(letter)
            
            # التحقق من النتائج
            assert analysis['letter'] == letter
            assert 'meaning' in analysis
            assert 'baserah_value' in analysis
            assert 'quantum_value' in analysis
            assert analysis['baserah_value'] >= 0.0
            assert analysis['baserah_value'] <= 1.0
            
            print(f"   المعنى: {analysis['meaning']}")
            print(f"   القيمة الثورية: {analysis['baserah_value']:.3f}")
            print(f"   القيمة الكمية: {analysis['quantum_value']:.3f}")
            print(f"   ✅ تم تحليل الحرف بنجاح")
        
        print(f"\n✅ نجح تحليل جميع الحروف ({len(test_letters)} حرف)")
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار تحليل الحروف: {e}")
        return False


def test_text_analysis():
    """اختبار تحليل النصوص."""
    
    print("\n📝 اختبار تحليل النصوص")
    print("=" * 50)
    
    try:
        # إنشاء المحرك
        engine = ArabicLexiconEngine("TextTestEngine")
        
        # نصوص للاختبار
        test_texts = [
            "الله نور السماوات والأرض",
            "العلم نور والجهل ظلام",
            "الحياة جميلة والحكمة ضرورية"
        ]
        
        for text in test_texts:
            print(f"\n📄 تحليل نص: {text}")
            
            # تحليل النص
            analysis = engine.analyze_text_revolutionary(text)
            
            # التحقق من النتائج
            assert analysis['original_text'] == text
            assert 'text_statistics' in analysis
            assert 'word_analyses' in analysis
            assert 'letter_frequency' in analysis
            assert 'basil_theories_analysis' in analysis
            assert 'revolutionary_insights' in analysis
            
            stats = analysis['text_statistics']
            assert stats['total_words'] > 0
            assert stats['analyzed_words'] >= 0
            assert stats['total_letters'] > 0
            
            print(f"   إجمالي الكلمات: {stats['total_words']}")
            print(f"   كلمات محللة: {stats['analyzed_words']}")
            print(f"   إجمالي الحروف: {stats['total_letters']}")
            print(f"   متوسط الوزن الدلالي: {stats['average_semantic_weight']:.3f}")
            print(f"   رؤى ثورية: {len(analysis['revolutionary_insights'])}")
            print(f"   ✅ تم تحليل النص بنجاح")
        
        print(f"\n✅ نجح تحليل جميع النصوص ({len(test_texts)} نص)")
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار تحليل النصوص: {e}")
        return False


def test_basil_theories_application():
    """اختبار تطبيق نظريات باسل."""
    
    print("\n🧬 اختبار تطبيق نظريات باسل")
    print("=" * 50)
    
    try:
        # إنشاء المحرك
        engine = ArabicLexiconEngine("BasilTestEngine")
        
        # تحليل كلمة مع نظريات باسل
        word = "الله"
        analysis = engine.analyze_word_revolutionary(word, deep_analysis=True)
        
        # التحقق من تطبيق النظريات
        basil_theories = analysis.basil_theories_application
        
        # نظرية ثنائية الصفر
        assert 'zero_duality' in basil_theories
        zero_duality = basil_theories['zero_duality']
        assert 'positive_sum' in zero_duality
        assert 'negative_sum' in zero_duality
        assert 'balance' in zero_duality
        assert 'is_balanced' in zero_duality
        
        print(f"✅ نظرية ثنائية الصفر:")
        print(f"   مجموع إيجابي: {zero_duality['positive_sum']:.3f}")
        print(f"   مجموع سالب: {zero_duality['negative_sum']:.3f}")
        print(f"   التوازن: {zero_duality['balance']:.3f}")
        print(f"   متوازن: {zero_duality['is_balanced']}")
        
        # نظرية تعامد الأضداد
        if 'perpendicular_opposites' in basil_theories:
            perp_opposites = basil_theories['perpendicular_opposites']
            assert 'first_half_value' in perp_opposites
            assert 'second_half_value' in perp_opposites
            assert 'perpendicular_angle' in perp_opposites
            
            print(f"✅ نظرية تعامد الأضداد:")
            print(f"   النصف الأول: {perp_opposites['first_half_value']:.3f}")
            print(f"   النصف الثاني: {perp_opposites['second_half_value']:.3f}")
            print(f"   الزاوية: {perp_opposites['perpendicular_angle']:.1f}°")
        
        # نظرية الفتائل
        assert 'filament_theory' in basil_theories
        filament_theory = basil_theories['filament_theory']
        assert 'filaments' in filament_theory
        assert 'total_filaments' in filament_theory
        assert 'primary_filaments' in filament_theory
        
        print(f"✅ نظرية الفتائل:")
        print(f"   إجمالي الفتائل: {filament_theory['total_filaments']}")
        print(f"   فتائل أولية: {filament_theory['primary_filaments']}")
        
        print(f"\n✅ نجح تطبيق جميع نظريات باسل")
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار نظريات باسل: {e}")
        return False


def test_data_loader():
    """اختبار محمل البيانات."""
    
    print("\n📥 اختبار محمل البيانات")
    print("=" * 50)
    
    try:
        # إنشاء المحرك
        engine = ArabicLexiconEngine("LoaderTestEngine")
        
        # إنشاء محمل البيانات
        loader = LexiconDataLoader(engine)
        
        # التحقق من التهيئة
        assert hasattr(loader, 'data_sources')
        assert hasattr(loader, 'loading_stats')
        assert len(loader.data_sources) > 0
        
        print("✅ تم إنشاء محمل البيانات بنجاح")
        
        # اختبار تحميل من API (محاكاة)
        api_result = loader.load_from_api('almaany_api', ['الله', 'حياة'])
        assert api_result['success']
        assert api_result['entries_loaded'] > 0
        
        print(f"✅ تحميل API: {api_result['entries_loaded']} مدخل")
        
        # اختبار إنشاء ملفات تجريبية
        with tempfile.TemporaryDirectory() as temp_dir:
            # تغيير مسار البيانات للمجلد المؤقت
            original_sources = loader.data_sources.copy()
            
            for source_name, source in loader.data_sources.items():
                if source.file_path:
                    source.file_path = os.path.join(temp_dir, os.path.basename(source.file_path))
            
            try:
                # اختبار تحميل JSON
                json_result = loader.load_from_json('custom_json')
                assert json_result['success']
                print(f"✅ تحميل JSON: {json_result['entries_loaded']} مدخل")
                
                # اختبار تحميل XML
                xml_result = loader.load_from_xml('lisan_xml')
                assert xml_result['success']
                print(f"✅ تحميل XML: {xml_result['entries_loaded']} مدخل")
                
            finally:
                # استعادة المسارات الأصلية
                loader.data_sources = original_sources
        
        print(f"\n✅ نجح اختبار محمل البيانات")
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار محمل البيانات: {e}")
        return False


def test_quick_functions():
    """اختبار الدوال السريعة."""
    
    print("\n⚡ اختبار الدوال السريعة")
    print("=" * 50)
    
    try:
        # اختبار إنشاء محرك سريع
        engine = create_arabic_lexicon_engine("QuickTestEngine")
        assert engine.engine_name == "QuickTestEngine"
        print("✅ إنشاء محرك سريع")
        
        # اختبار تحليل كلمة سريع
        word_result = analyze_arabic_word("علم", "QuickWordAnalyzer")
        assert word_result['word'] == "علم"
        assert 'main_meaning' in word_result
        print("✅ تحليل كلمة سريع")
        
        # اختبار استكشاف حرف سريع
        letter_result = explore_arabic_letter("ع", "QuickLetterExplorer")
        assert letter_result['letter'] == "ع"
        assert 'meaning' in letter_result
        print("✅ استكشاف حرف سريع")
        
        # اختبار تحليل نص سريع
        text_result = analyze_arabic_text("العلم نور", "QuickTextAnalyzer")
        assert text_result['original_text'] == "العلم نور"
        assert 'text_statistics' in text_result
        print("✅ تحليل نص سريع")
        
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
        engine = ArabicLexiconEngine("PerformanceTestEngine")
        
        # قياس الوقت
        start_time = datetime.now()
        
        # تحليل عدة كلمات
        test_words = ['الله', 'حياة', 'علم', 'حكمة', 'سلام', 'نور', 'كتاب', 'قلم', 'بيت', 'ماء']
        
        for word in test_words:
            analysis = engine.analyze_word_revolutionary(word, deep_analysis=True)
            assert analysis.word == word
        
        # حساب الوقت المستغرق
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print(f"✅ تم تحليل {len(test_words)} كلمة في {duration:.2f} ثانية")
        print(f"   متوسط الوقت لكل كلمة: {duration/len(test_words):.3f} ثانية")
        
        # التحقق من الإحصائيات
        status = engine.get_engine_status()
        stats = status['statistics']
        
        assert stats['words_analyzed'] >= len(test_words)
        assert stats['letters_analyzed'] > 0
        assert stats['baserah_analyses_performed'] > 0
        
        print(f"   كلمات محللة: {stats['words_analyzed']}")
        print(f"   حروف محللة: {stats['letters_analyzed']}")
        print(f"   تحليلات Baserah: {stats['baserah_analyses_performed']}")
        print(f"   رؤى ثورية: {stats['total_revolutionary_insights']}")
        
        print(f"\n✅ نجح اختبار الأداء")
        return True
        
    except Exception as e:
        print(f"❌ فشل اختبار الأداء: {e}")
        return False


def run_all_tests():
    """تشغيل جميع الاختبارات."""
    
    print("🧪✨ بدء اختبارات محرك المعجم العربي الثوري")
    print("📚 مدعوم بنظريات باسل ونظام Baserah لاستكشاف دلالات الحروف")
    print("=" * 80)
    print(f"📅 وقت الاختبار: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    tests = [
        ("اختبار تهيئة المحرك", test_engine_initialization),
        ("اختبار تحليل الكلمات", test_word_analysis),
        ("اختبار تحليل الحروف", test_letter_analysis),
        ("اختبار تحليل النصوص", test_text_analysis),
        ("اختبار نظريات باسل", test_basil_theories_application),
        ("اختبار محمل البيانات", test_data_loader),
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
        print("🌟 محرك المعجم العربي الثوري جاهز للاستخدام!")
    elif success_rate >= 0.7:
        print("👍 النتيجة النهائية: جيد")
        print("⚠️ بعض التحسينات مطلوبة")
    else:
        print("⚠️ النتيجة النهائية: يحتاج تطوير")
        print("🔧 مراجعة وإصلاح مطلوب")
    
    print()
    print("🔬 انتهت اختبارات محرك المعجم العربي الثوري")
    print(f"📅 وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    run_all_tests()
