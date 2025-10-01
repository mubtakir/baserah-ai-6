#!/usr/bin/env python3
# run_quranic_analysis.py - تشغيل تفاعلي لمحرك التحليل القرآني الثوري

import sys
import os
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


def print_banner():
    """طباعة شعار المحرك القرآني."""

    banner = """
🕌════════════════════════════════════════════════════════════════════🕌
📖                   محرك التحليل القرآني الثوري                    📖
🧬              مدعوم بنظريات باسل ونظام Baserah النقي                🧬
🌟              تحليل القرآن الكريم بالمنهج الثوري                   🌟
🕌════════════════════════════════════════════════════════════════════🕌
"""

    print(banner)
    print(f"📅 التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔥 النسخة: 1.0.0 - Quranic Analysis Engine")
    print("🤲 بسم الله نبدأ هذا العمل المبارك")
    print()


def print_menu():
    """طباعة قائمة الخيارات."""

    menu = """
🎯 اختر العملية المطلوبة:

1️⃣  تحليل آية قرآنية
2️⃣  تحليل سورة كاملة
3️⃣  البحث في القرآن الكريم
4️⃣  اكتشاف الإعجاز الرقمي
5️⃣  عرض إحصائيات المحرك
6️⃣  اختبار المحرك
7️⃣  تصدير نتائج التحليل
8️⃣  عرض آية بالمرجع
9️⃣  عرض معلومات السور
0️⃣  خروج

"""
    print(menu)


def analyze_verse_interactive(engine):
    """تحليل آية تفاعلي."""

    print("📖 تحليل آية قرآنية")
    print("=" * 50)

    try:
        surah_num = int(input("📝 أدخل رقم السورة (1-114): ").strip())
        if surah_num < 1 or surah_num > 114:
            print("❌ رقم السورة يجب أن يكون بين 1 و 114!")
            return

        verse_num = int(input("📝 أدخل رقم الآية: ").strip())
        if verse_num < 1:
            print("❌ رقم الآية يجب أن يكون أكبر من 0!")
            return

    except ValueError:
        print("❌ يرجى إدخال أرقام صحيحة!")
        return

    deep_analysis = input("🧬 تحليل عميق مع نظريات باسل؟ (y/n): ").strip().lower() == 'y'

    print(f"\n🔄 جاري تحليل الآية: {surah_num}:{verse_num}")
    print("⏳ يرجى الانتظار...")

    try:
        # تحليل الآية
        analysis = engine.analyze_verse_revolutionary(surah_num, verse_num, deep_analysis=deep_analysis)

        # عرض النتائج
        print("\n📊 نتائج التحليل:")
        print("=" * 50)

        # معلومات السورة
        surah_name = engine.surah_names.get(surah_num, {}).get('arabic', f'السورة {surah_num}')
        surah_type = engine.surah_names.get(surah_num, {}).get('type', 'غير محدد')

        print(f"📖 السورة: {surah_name} ({surah_type})")
        print(f"📝 الآية: {verse_num}")
        print(f"🔤 النص: {analysis.text}")
        print(f"⚖️ الوزن الدلالي: {analysis.semantic_weight:.3f}")
        print(f"📊 عدد الكلمات: {len(analysis.word_analysis)}")

        # تحليل الكلمات
        print(f"\n🔤 تحليل الكلمات:")
        for i, word_analysis in enumerate(analysis.word_analysis[:5], 1):
            print(f"   {i}. {word_analysis['word']}: {word_analysis['meaning']} (وزن: {word_analysis['semantic_weight']:.3f})")

        if len(analysis.word_analysis) > 5:
            print(f"   ... و {len(analysis.word_analysis) - 5} كلمة أخرى")

        # تحليل Baserah
        print(f"\n🌟 تحليل Baserah:")
        baserah = analysis.baserah_analysis
        print(f"   القيمة الإجمالية: {baserah.get('total_value', 0):.3f}")
        print(f"   مؤشر التناغم: {baserah.get('harmony_index', 0):.3f}")
        print(f"   القيمة الإلهية: {baserah.get('divine_value', 0):.3f}")
        print(f"   التوقيع الثوري: {baserah.get('baserah_signature', 'غير محدد')}")

        # نظريات باسل (إذا كان التحليل عميقاً)
        if deep_analysis and analysis.basil_theories_application:
            print(f"\n🧬 نظريات باسل الثورية:")

            # ثنائية الصفر
            if 'zero_duality_quranic' in analysis.basil_theories_application:
                zero_duality = analysis.basil_theories_application['zero_duality_quranic']
                print(f"   🔄 ثنائية الصفر القرآنية:")
                print(f"      مجموع إيجابي: {zero_duality['positive_sum']:.3f}")
                print(f"      مجموع سالب: {zero_duality['negative_sum']:.3f}")
                print(f"      التوازن الإلهي: {zero_duality['divine_balance']:.3f}")
                print(f"      متوازن إلهياً: {'نعم' if zero_duality['is_divinely_balanced'] else 'لا'}")

            # تعامد الأضداد
            if 'perpendicular_opposites_quranic' in analysis.basil_theories_application:
                perp = analysis.basil_theories_application['perpendicular_opposites_quranic']
                print(f"   ⟂ تعامد الأضداد القرآنية:")
                print(f"      النصف الأول: {perp['first_half_value']:.3f}")
                print(f"      النصف الثاني: {perp['second_half_value']:.3f}")
                print(f"      الزاوية الإلهية: {perp['divine_angle']:.1f}°")

            # الفتائل
            if 'filament_theory_quranic' in analysis.basil_theories_application:
                filament = analysis.basil_theories_application['filament_theory_quranic']
                print(f"   🧵 نظرية الفتائل القرآنية:")
                print(f"      إجمالي الفتائل: {filament['total_filaments']}")
                print(f"      فتائل إلهية أولية: {filament['divine_primary_filaments']}")

        # الإعجاز الرقمي
        if analysis.numerical_miracle:
            print(f"\n🔢 الإعجاز الرقمي:")
            miracle_count = 0
            for miracle_type, miracle_data in analysis.numerical_miracle.items():
                if isinstance(miracle_data, dict):
                    print(f"   • {miracle_type}:")
                    if 'is_miraculous' in miracle_data and miracle_data['is_miraculous']:
                        print(f"     🌟 إعجاز مؤكد!")
                        miracle_count += 1
                    elif any(key.endswith('_miraculous') for key in miracle_data.keys()):
                        miraculous_keys = [k for k in miracle_data.keys() if k.endswith('_miraculous') and miracle_data[k]]
                        if miraculous_keys:
                            print(f"     🌟 إعجاز في: {', '.join(miraculous_keys)}")
                            miracle_count += 1

            if miracle_count == 0:
                print("   لم يتم اكتشاف إعجاز رقمي واضح في هذه الآية")

        # الأنماط الإلهية
        if analysis.divine_patterns:
            print(f"\n🌟 الأنماط الإلهية:")
            for pattern in analysis.divine_patterns:
                print(f"   • {pattern}")

        # الرؤى الثورية
        if analysis.revolutionary_insights:
            print(f"\n💡 الرؤى الثورية:")
            for insight in analysis.revolutionary_insights:
                print(f"   • {insight}")

    except Exception as e:
        print(f"❌ خطأ في تحليل الآية: {e}")


def main():
    """الدالة الرئيسية."""

    print_banner()

    # إنشاء المحرك
    print("🔄 تهيئة محرك التحليل القرآني الثوري...")
    try:
        engine = QuranicAnalysisEngine("InteractiveQuranicEngine")
        print("✅ تم تهيئة المحرك بنجاح!")
    except Exception as e:
        print(f"❌ فشل في تهيئة المحرك: {e}")
        return

    while True:
        print_menu()

        try:
            choice = input("🎯 اختر رقم العملية: ").strip()

            if choice == '1':
                analyze_verse_interactive(engine)
            elif choice == '2':
                print("🚧 تحليل السورة الكاملة - قيد التطوير")
            elif choice == '3':
                print("🚧 البحث في القرآن - قيد التطوير")
            elif choice == '4':
                print("🚧 اكتشاف الإعجاز الرقمي - قيد التطوير")
            elif choice == '5':
                print("🚧 إحصائيات المحرك - قيد التطوير")
            elif choice == '6':
                print("🚧 اختبار المحرك - قيد التطوير")
            elif choice == '7':
                print("🚧 تصدير النتائج - قيد التطوير")
            elif choice == '8':
                print("🚧 عرض آية بالمرجع - قيد التطوير")
            elif choice == '9':
                print("🚧 معلومات السور - قيد التطوير")
            elif choice == '0':
                print("\n🤲 الحمد لله رب العالمين")
                print("📖 شكراً لاستخدام محرك التحليل القرآني الثوري!")
                print("🕌 بارك الله في هذا العمل المبارك!")
                break
            else:
                print("❌ خيار غير صحيح! يرجى اختيار رقم من القائمة.")

            input("\n⏸️ اضغط Enter للمتابعة...")
            print("\n" + "="*70 + "\n")

        except KeyboardInterrupt:
            print("\n\n🤲 تم إيقاف البرنامج - الحمد لله رب العالمين")
            break
        except Exception as e:
            print(f"\n💥 خطأ غير متوقع: {e}")
            input("⏸️ اضغط Enter للمتابعة...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🤲 الحمد لله رب العالمين!")
    except Exception as e:
        print(f"💥 خطأ في تشغيل البرنامج: {e}")