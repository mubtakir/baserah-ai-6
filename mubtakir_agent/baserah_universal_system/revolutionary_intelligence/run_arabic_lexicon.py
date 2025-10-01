#!/usr/bin/env python3
# run_arabic_lexicon.py - تشغيل تفاعلي لمحرك المعجم العربي الثوري

import sys
import os
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
    quick_load_lexicon_data
)


def print_banner():
    """طباعة شعار المحرك."""
    
    banner = """
📚════════════════════════════════════════════════════════════════════📚
🔤                   محرك المعجم العربي الثوري                      🔤
🧬              مدعوم بنظريات باسل ونظام Baserah النقي                🧬
📖              لاستكشاف دلالات الحروف والكلمات العربية              📖
📚════════════════════════════════════════════════════════════════════📚
"""
    
    print(banner)
    print(f"📅 التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔥 النسخة: 1.0.0 - Arabic Lexicon Engine")
    print()


def print_menu():
    """طباعة قائمة الخيارات."""
    
    menu = """
🎯 اختر العملية المطلوبة:

1️⃣  تحليل كلمة عربية
2️⃣  استكشاف دلالة حرف
3️⃣  تحليل نص عربي
4️⃣  تحميل معاجم إضافية
5️⃣  عرض إحصائيات المحرك
6️⃣  اختبار المحرك
7️⃣  عرض دلالات جميع الحروف
8️⃣  البحث في المعجم
0️⃣  خروج

"""
    print(menu)


def analyze_word_interactive(engine):
    """تحليل كلمة تفاعلي."""
    
    print("🔍 تحليل كلمة عربية")
    print("=" * 50)
    
    word = input("📝 أدخل الكلمة العربية: ").strip()
    
    if not word:
        print("❌ يجب إدخال كلمة!")
        return
    
    deep_analysis = input("🧬 تحليل عميق مع نظريات باسل؟ (y/n): ").strip().lower() == 'y'
    
    print(f"\n🔄 جاري تحليل الكلمة: {word}")
    print("⏳ يرجى الانتظار...")
    
    try:
        # تحليل الكلمة
        analysis = engine.analyze_word_revolutionary(word, deep_analysis=deep_analysis)
        
        # عرض النتائج
        print("\n📊 نتائج التحليل:")
        print("=" * 50)
        
        print(f"🔤 الكلمة: {analysis.word}")
        print(f"🌱 الجذر: {analysis.root}")
        print(f"💭 المعنى: {analysis.meaning}")
        print(f"📖 التفسير المفصل: {analysis.detailed_meaning}")
        print(f"⚖️ الوزن الدلالي: {analysis.semantic_weight:.3f}")
        
        # تحليل الحروف
        print(f"\n🔤 تحليل الحروف:")
        for letter, meaning in analysis.letter_analysis.items():
            print(f"   {letter}: {meaning}")
        
        # تحليل Baserah
        print(f"\n🌟 تحليل Baserah:")
        baserah = analysis.baserah_analysis
        print(f"   القيمة الإجمالية: {baserah.get('total_value', 0):.3f}")
        print(f"   القيمة المتوسطة: {baserah.get('average_value', 0):.3f}")
        print(f"   مؤشر التناغم: {baserah.get('harmony_index', 0):.3f}")
        print(f"   التوقيع الثوري: {baserah.get('baserah_signature', 'غير محدد')}")
        
        # نظريات باسل (إذا كان التحليل عميقاً)
        if deep_analysis and analysis.basil_theories_application:
            print(f"\n🧬 نظريات باسل الثورية:")
            
            # ثنائية الصفر
            if 'zero_duality' in analysis.basil_theories_application:
                zero_duality = analysis.basil_theories_application['zero_duality']
                print(f"   🔄 ثنائية الصفر:")
                print(f"      مجموع إيجابي: {zero_duality['positive_sum']:.3f}")
                print(f"      مجموع سالب: {zero_duality['negative_sum']:.3f}")
                print(f"      التوازن: {zero_duality['balance']:.3f}")
                print(f"      متوازن: {'نعم' if zero_duality['is_balanced'] else 'لا'}")
            
            # تعامد الأضداد
            if 'perpendicular_opposites' in analysis.basil_theories_application:
                perp = analysis.basil_theories_application['perpendicular_opposites']
                print(f"   ⟂ تعامد الأضداد:")
                print(f"      النصف الأول: {perp['first_half_value']:.3f}")
                print(f"      النصف الثاني: {perp['second_half_value']:.3f}")
                print(f"      الزاوية: {perp['perpendicular_angle']:.1f}°")
            
            # الفتائل
            if 'filament_theory' in analysis.basil_theories_application:
                filament = analysis.basil_theories_application['filament_theory']
                print(f"   🧵 نظرية الفتائل:")
                print(f"      إجمالي الفتائل: {filament['total_filaments']}")
                print(f"      فتائل أولية: {filament['primary_filaments']}")
        
        # الكلمات ذات الصلة
        if analysis.related_words:
            print(f"\n🔗 كلمات ذات صلة:")
            for related_word in analysis.related_words[:5]:
                print(f"   • {related_word}")
        
        # أمثلة الاستخدام
        if analysis.usage_examples:
            print(f"\n📝 أمثلة الاستخدام:")
            for example in analysis.usage_examples[:3]:
                print(f"   • {example}")
        
    except Exception as e:
        print(f"❌ خطأ في تحليل الكلمة: {e}")


def explore_letter_interactive(engine):
    """استكشاف حرف تفاعلي."""
    
    print("🔤 استكشاف دلالة حرف")
    print("=" * 50)
    
    letter = input("📝 أدخل الحرف العربي: ").strip()
    
    if not letter or len(letter) != 1:
        print("❌ يجب إدخال حرف واحد فقط!")
        return
    
    print(f"\n🔄 جاري استكشاف الحرف: {letter}")
    
    try:
        # استكشاف الحرف
        analysis = engine.explore_letter_meanings(letter)
        
        if 'error' in analysis:
            print(f"❌ {analysis['error']}")
            return
        
        # عرض النتائج
        print("\n📊 نتائج الاستكشاف:")
        print("=" * 50)
        
        print(f"🔤 الحرف: {analysis['letter']}")
        print(f"💭 المعنى: {analysis['meaning']}")
        print(f"🌟 القيمة الثورية: {analysis['baserah_value']:.3f}")
        print(f"⚛️ القيمة الكمية: {analysis['quantum_value']:.3f}")
        print(f"📊 تكرار في قاعدة البيانات: {analysis['frequency_in_database']}")
        
        # التحليل الثوري
        if 'revolutionary_analysis' in analysis:
            rev_analysis = analysis['revolutionary_analysis']
            print(f"\n🧬 التحليل الثوري:")
            print(f"   القوة الدلالية: {rev_analysis['semantic_power']:.3f}")
            print(f"   التوقيع الكمي: {rev_analysis['quantum_signature']:.3f}")
            if rev_analysis['letter_position_in_alphabet'] > 0:
                print(f"   الموضع في الأبجدية: {rev_analysis['letter_position_in_alphabet']}")
        
        # أمثلة الكلمات
        if analysis['example_words']:
            print(f"\n📝 أمثلة كلمات تحتوي على الحرف:")
            for word in analysis['example_words'][:10]:
                print(f"   • {word}")
        
    except Exception as e:
        print(f"❌ خطأ في استكشاف الحرف: {e}")


def analyze_text_interactive(engine):
    """تحليل نص تفاعلي."""
    
    print("📝 تحليل نص عربي")
    print("=" * 50)
    
    text = input("📝 أدخل النص العربي: ").strip()
    
    if not text:
        print("❌ يجب إدخال نص!")
        return
    
    print(f"\n🔄 جاري تحليل النص...")
    print("⏳ يرجى الانتظار...")
    
    try:
        # تحليل النص
        analysis = engine.analyze_text_revolutionary(text)
        
        # عرض النتائج
        print("\n📊 نتائج التحليل:")
        print("=" * 50)
        
        print(f"📝 النص الأصلي: {analysis['original_text']}")
        
        # الإحصائيات
        stats = analysis['text_statistics']
        print(f"\n📊 الإحصائيات:")
        print(f"   إجمالي الكلمات: {stats['total_words']}")
        print(f"   كلمات محللة: {stats['analyzed_words']}")
        print(f"   إجمالي الحروف: {stats['total_letters']}")
        print(f"   حروف فريدة: {stats['unique_letters']}")
        print(f"   جذور فريدة: {stats['unique_roots']}")
        print(f"   متوسط الوزن الدلالي: {stats['average_semantic_weight']:.3f}")
        
        # تحليل الكلمات
        print(f"\n🔤 تحليل الكلمات:")
        for word_analysis in analysis['word_analyses'][:5]:  # أول 5 كلمات
            print(f"   • {word_analysis['word']}: {word_analysis['meaning']} (وزن: {word_analysis['semantic_weight']:.3f})")
        
        if len(analysis['word_analyses']) > 5:
            print(f"   ... و {len(analysis['word_analyses']) - 5} كلمة أخرى")
        
        # الحروف الأكثر تكراراً
        print(f"\n🔤 الحروف الأكثر تكراراً:")
        for letter_info in analysis['most_frequent_letters_meanings'][:5]:
            print(f"   • {letter_info['letter']}: {letter_info['frequency']} مرة - {letter_info['meaning']}")
        
        # الجذور المكتشفة
        if analysis['unique_roots']:
            print(f"\n🌱 الجذور المكتشفة:")
            for root in analysis['unique_roots'][:10]:
                print(f"   • {root}")
        
        # نظريات باسل على النص
        if 'basil_theories_analysis' in analysis:
            basil = analysis['basil_theories_analysis']
            print(f"\n🧬 تطبيق نظريات باسل على النص:")
            
            if 'zero_duality_text' in basil:
                zero_text = basil['zero_duality_text']
                print(f"   🔄 ثنائية الصفر: توازن {zero_text['balance_percentage']:.1f}%")
            
            if 'filament_theory_text' in basil:
                filament_text = basil['filament_theory_text']
                print(f"   🧵 الفتائل: {filament_text['total_filaments']} فتيلة ({filament_text['primary_filaments']} أولية)")
        
        # الرؤى الثورية
        if analysis['revolutionary_insights']:
            print(f"\n💡 الرؤى الثورية:")
            for insight in analysis['revolutionary_insights']:
                print(f"   • {insight}")
        
    except Exception as e:
        print(f"❌ خطأ في تحليل النص: {e}")


def load_lexicons_interactive(engine):
    """تحميل معاجم تفاعلي."""
    
    print("📥 تحميل معاجم إضافية")
    print("=" * 50)
    
    try:
        # إنشاء محمل البيانات
        loader = LexiconDataLoader(engine)
        
        # عرض المصادر المتاحة
        print("🔗 المصادر المتاحة:")
        for source_name, source in loader.data_sources.items():
            status = "✅ نشط" if source.is_active else "❌ غير نشط"
            print(f"   {source_name}: {source.name} ({source.source_type}) - {status}")
        
        print("\nخيارات التحميل:")
        print("1. تحميل جميع المصادر")
        print("2. تحميل مصدر محدد")
        print("3. إنشاء ملفات تجريبية")
        
        choice = input("\nاختر رقم الخيار: ").strip()
        
        if choice == '1':
            print("\n🔄 تحميل جميع المصادر...")
            results = loader.load_all_available_sources()
            
            print("\n📊 نتائج التحميل:")
            for source_name, result in results.items():
                if result['success']:
                    print(f"   ✅ {source_name}: {result['entries_loaded']} مدخل")
                else:
                    print(f"   ❌ {source_name}: {result['error']}")
        
        elif choice == '2':
            source_name = input("أدخل اسم المصدر: ").strip()
            if source_name in loader.data_sources:
                source = loader.data_sources[source_name]
                
                if source.source_type == 'api':
                    words = input("أدخل كلمات للبحث (مفصولة بفواصل): ").strip().split(',')
                    words = [w.strip() for w in words if w.strip()]
                    result = loader.load_from_api(source_name, words)
                elif source.source_type == 'xml':
                    result = loader.load_from_xml(source_name)
                elif source.source_type == 'json':
                    result = loader.load_from_json(source_name)
                else:
                    result = {'success': False, 'error': 'نوع مصدر غير مدعوم'}
                
                if result['success']:
                    print(f"✅ تم تحميل {result['entries_loaded']} مدخل من {source_name}")
                else:
                    print(f"❌ فشل التحميل: {result['error']}")
            else:
                print("❌ مصدر غير معروف!")
        
        elif choice == '3':
            print("\n🔄 إنشاء ملفات تجريبية...")
            from .lexicon_data_loader import create_sample_lexicon_files
            results = create_sample_lexicon_files()
            
            for format_type, result in results.items():
                if result['success']:
                    print(f"✅ تم إنشاء ملف {format_type.upper()}: {result['entries_loaded']} مدخل")
                else:
                    print(f"❌ فشل إنشاء ملف {format_type.upper()}: {result['error']}")
        
        else:
            print("❌ خيار غير صحيح!")
    
    except Exception as e:
        print(f"❌ خطأ في تحميل المعاجم: {e}")


def show_engine_statistics(engine):
    """عرض إحصائيات المحرك."""
    
    print("📊 إحصائيات المحرك")
    print("=" * 50)
    
    try:
        status = engine.get_engine_status()
        
        # معلومات المحرك
        info = status['engine_info']
        print(f"🤖 اسم المحرك: {info['name']}")
        print(f"📦 الإصدار: {info['version']}")
        print(f"📅 وقت الإنشاء: {info['creation_time']}")
        
        # الإحصائيات
        stats = status['statistics']
        print(f"\n📊 الإحصائيات:")
        print(f"   كلمات محللة: {stats['words_analyzed']}")
        print(f"   حروف محللة: {stats['letters_analyzed']}")
        print(f"   جذور مكتشفة: {stats['roots_discovered']}")
        print(f"   معاني مستخرجة: {stats['meanings_extracted']}")
        print(f"   تحليلات Baserah: {stats['baserah_analyses_performed']}")
        print(f"   تطبيقات نظريات باسل: {stats['basil_theories_applications']}")
        print(f"   متوسط الوزن الدلالي: {stats['average_semantic_weight']:.3f}")
        print(f"   رؤى ثورية: {stats['total_revolutionary_insights']}")
        
        # القدرات
        capabilities = status['capabilities']
        print(f"\n🛠️ القدرات:")
        for capability, enabled in capabilities.items():
            status_icon = "✅" if enabled else "❌"
            print(f"   {status_icon} {capability}")
        
        # المعاجم المدمجة
        lexicons = status['integrated_lexicons']
        print(f"\n📚 المعاجم المدمجة:")
        for lexicon, count in lexicons.items():
            print(f"   📖 {lexicon}: {count} مدخل")
        
        # الميزات الثورية
        revolutionary = status['revolutionary_features']
        print(f"\n🌟 الميزات الثورية:")
        for feature, enabled in revolutionary.items():
            if enabled:
                print(f"   🔥 {feature}")
        
        print(f"\n📁 مسار قاعدة البيانات: {status['database_path']}")
        print(f"🔤 عدد دلالات الحروف: {status['letter_meanings_count']}")
        
    except Exception as e:
        print(f"❌ خطأ في عرض الإحصائيات: {e}")


def run_engine_tests():
    """تشغيل اختبارات المحرك."""
    
    print("🧪 تشغيل اختبارات المحرك")
    print("=" * 50)
    
    try:
        from .test_arabic_lexicon import run_all_tests
        run_all_tests()
    except Exception as e:
        print(f"❌ خطأ في تشغيل الاختبارات: {e}")


def show_all_letters_meanings(engine):
    """عرض دلالات جميع الحروف."""
    
    print("🔤 دلالات جميع الحروف العربية")
    print("=" * 50)
    
    try:
        arabic_letters = ['ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']
        
        for letter in arabic_letters:
            if letter in engine.letter_meanings:
                meaning = engine.letter_meanings[letter]
                print(f"   {letter}: {meaning}")
            else:
                print(f"   {letter}: غير محدد")
        
        print(f"\nإجمالي الحروف: {len(arabic_letters)}")
        print(f"حروف محددة المعنى: {len([l for l in arabic_letters if l in engine.letter_meanings])}")
        
    except Exception as e:
        print(f"❌ خطأ في عرض دلالات الحروف: {e}")


def search_in_lexicon(engine):
    """البحث في المعجم."""
    
    print("🔍 البحث في المعجم")
    print("=" * 50)
    
    search_term = input("📝 أدخل كلمة أو جزء من كلمة للبحث: ").strip()
    
    if not search_term:
        print("❌ يجب إدخال كلمة للبحث!")
        return
    
    try:
        # البحث باستخدام دالة البحث السريع
        result = engine.search_word_meanings(search_term, include_related=True)
        
        print(f"\n📊 نتائج البحث عن: {search_term}")
        print("=" * 50)
        
        print(f"🔤 الكلمة: {result['word']}")
        print(f"🌱 الجذر: {result['root']}")
        print(f"💭 المعنى الرئيسي: {result['main_meaning']}")
        print(f"📖 المعنى المفصل: {result['detailed_meaning']}")
        print(f"⚖️ الوزن الدلالي: {result['semantic_weight']:.3f}")
        
        # الكلمات ذات الصلة
        if result['related_words']:
            print(f"\n🔗 كلمات ذات صلة:")
            for related_word in result['related_words']:
                print(f"   • {related_word}")
        
        # أمثلة الاستخدام
        if result['usage_examples']:
            print(f"\n📝 أمثلة الاستخدام:")
            for example in result['usage_examples']:
                print(f"   • {example}")
        
        # الرؤى الثورية
        if result['revolutionary_insights']:
            print(f"\n💡 الرؤى الثورية:")
            for insight in result['revolutionary_insights'][:5]:
                print(f"   • {insight}")
        
    except Exception as e:
        print(f"❌ خطأ في البحث: {e}")


def main():
    """الدالة الرئيسية."""
    
    print_banner()
    
    # إنشاء المحرك
    print("🔄 تهيئة محرك المعجم العربي الثوري...")
    try:
        engine = ArabicLexiconEngine("InteractiveLexiconEngine")
        print("✅ تم تهيئة المحرك بنجاح!")
    except Exception as e:
        print(f"❌ فشل في تهيئة المحرك: {e}")
        return
    
    while True:
        print_menu()
        
        try:
            choice = input("🎯 اختر رقم العملية: ").strip()
            
            if choice == '1':
                analyze_word_interactive(engine)
            elif choice == '2':
                explore_letter_interactive(engine)
            elif choice == '3':
                analyze_text_interactive(engine)
            elif choice == '4':
                load_lexicons_interactive(engine)
            elif choice == '5':
                show_engine_statistics(engine)
            elif choice == '6':
                run_engine_tests()
            elif choice == '7':
                show_all_letters_meanings(engine)
            elif choice == '8':
                search_in_lexicon(engine)
            elif choice == '0':
                print("\n👋 شكراً لاستخدام محرك المعجم العربي الثوري!")
                print("📚 نراكم في رحلة أخرى لاستكشاف دلالات الحروف!")
                break
            else:
                print("❌ خيار غير صحيح! يرجى اختيار رقم من القائمة.")
            
            input("\n⏸️ اضغط Enter للمتابعة...")
            print("\n" + "="*70 + "\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 تم إيقاف البرنامج بواسطة المستخدم")
            break
        except Exception as e:
            print(f"\n💥 خطأ غير متوقع: {e}")
            input("⏸️ اضغط Enter للمتابعة...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 وداعاً!")
    except Exception as e:
        print(f"💥 خطأ في تشغيل البرنامج: {e}")
