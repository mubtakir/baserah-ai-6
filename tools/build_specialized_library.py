#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧬 بناء مكتبة متخصصة - نظام بصيرة الثوري
===============================================

هذا السكريبت يساعد في بناء مكتبات معرفية متخصصة في مجالات محددة
باستخدام نظام بصيرة الثوري مع تكامل Ollama.

الاستخدام:
    python3 build_specialized_library.py

المطور: باسل يحيى عبدالله
"""

from revolutionary_knowledge_system import RevolutionaryKnowledgeSystem
import time
import sys
from datetime import datetime

class SpecializedLibraryBuilder:
    """بناء مكتبات معرفية متخصصة"""
    
    def __init__(self):
        """تهيئة البناء"""
        print("🧬 تهيئة بناء المكتبة المتخصصة...")
        self.system = RevolutionaryKnowledgeSystem()
        self.successful = 0
        self.failed = 0
        self.start_time = datetime.now()
    
    def build_ai_library(self):
        """بناء مكتبة متخصصة في الذكاء الاصطناعي"""
        ai_topics = [
            "تاريخ الذكاء الاصطناعي ومراحل تطوره",
            "أنواع خوارزميات التعلم الآلي والتطبيقات",
            "الشبكات العصبية العميقة والتطبيقات العملية", 
            "معالجة الصور والرؤية الحاسوبية",
            "الذكاء الاصطناعي في الطب والتشخيص",
            "أخلاقيات الذكاء الاصطناعي والمسؤولية",
            "مستقبل الذكاء الاصطناعي والتوقعات",
            "التعلم المعزز والألعاب الذكية",
            "معالجة اللغة العربية الطبيعية",
            "الرؤية الحاسوبية والتعرف على الأنماط",
            "الذكاء الاصطناعي في الروبوتات",
            "التعلم غير المراقب واكتشاف الأنماط",
            "الذكاء الاصطناعي في التجارة الإلكترونية",
            "أنظمة التوصية الذكية",
            "الذكاء الاصطناعي في الأمن السيبراني"
        ]
        
        return self._build_library("الذكاء الاصطناعي", ai_topics)
    
    def build_programming_library(self):
        """بناء مكتبة متخصصة في البرمجة"""
        programming_topics = [
            "أساسيات البرمجة والخوارزميات",
            "لغات البرمجة الحديثة ومقارنة بينها",
            "هياكل البيانات والخوارزميات المتقدمة",
            "البرمجة الكائنية والتصميم",
            "قواعد البيانات وإدارة المعلومات",
            "تطوير الويب والتقنيات الحديثة",
            "البرمجة المتوازية والمعالجة المتعددة",
            "أمن البرمجيات وأفضل الممارسات",
            "اختبار البرمجيات وضمان الجودة",
            "إدارة المشاريع البرمجية",
            "البرمجة الوظيفية والنماذج المختلفة",
            "تطوير التطبيقات المحمولة",
            "الحوسبة السحابية والخدمات",
            "DevOps والتطوير المستمر",
            "الذكاء الاصطناعي في البرمجة"
        ]
        
        return self._build_library("البرمجة", programming_topics)
    
    def build_science_library(self):
        """بناء مكتبة متخصصة في العلوم"""
        science_topics = [
            "الفيزياء الكمية والميكانيكا الكمية",
            "الكيمياء العضوية والتفاعلات",
            "علم الأحياء الجزيئي والخلايا",
            "الرياضيات التطبيقية والنظرية",
            "علم الفلك واستكشاف الفضاء",
            "الجيولوجيا وعلوم الأرض",
            "البيئة والتغير المناخي",
            "الطاقة المتجددة والاستدامة",
            "النانوتكنولوجي والمواد المتقدمة",
            "الهندسة الوراثية والتكنولوجيا الحيوية",
            "علم النفس المعرفي والسلوكي",
            "الإحصاء والتحليل الرياضي",
            "الفيزياء النظرية والنسبية",
            "الكيمياء التحليلية والقياسات",
            "علوم الحاسوب النظرية"
        ]
        
        return self._build_library("العلوم", science_topics)
    
    def build_arabic_language_library(self):
        """بناء مكتبة متخصصة في اللغة العربية"""
        arabic_topics = [
            "قواعد النحو العربي والإعراب",
            "علم الصرف والاشتقاق في العربية",
            "البلاغة العربية والأساليب البيانية",
            "الأدب العربي عبر العصور",
            "الشعر العربي والأوزان والقوافي",
            "فقه اللغة العربية والتطور التاريخي",
            "المعاجم العربية وعلم المعجم",
            "اللهجات العربية والتنوع اللغوي",
            "الترجمة من وإلى العربية",
            "تعليم العربية للناطقين بغيرها",
            "الخط العربي والكتابة",
            "الإعلام العربي واللغة",
            "التكنولوجيا واللغة العربية",
            "اللسانيات العربية الحديثة",
            "التراث العربي والمخطوطات"
        ]
        
        return self._build_library("اللغة العربية", arabic_topics)
    
    def _build_library(self, library_name: str, topics: list) -> dict:
        """بناء مكتبة معرفية متخصصة"""
        print(f"\n🎯 بناء مكتبة {library_name}")
        print(f"📚 عدد المواضيع: {len(topics)}")
        print("=" * 50)
        
        local_successful = 0
        local_failed = 0
        
        for i, topic in enumerate(topics, 1):
            print(f"📖 ({i:2d}/{len(topics)}) {topic}")
            
            try:
                result = self.system.extract_from_external_source('ollama', topic)
                if result and len(result.strip()) > 50:  # التأكد من جودة المحتوى
                    local_successful += 1
                    self.successful += 1
                    print(f"✅ تم بنجاح ({len(result)} حرف)")
                else:
                    local_failed += 1
                    self.failed += 1
                    print(f"❌ فشل أو محتوى ضعيف")
                
                # توقف قصير لتجنب إرهاق النظام
                time.sleep(3)
                
            except Exception as e:
                local_failed += 1
                self.failed += 1
                print(f"❌ خطأ: {str(e)[:50]}...")
                time.sleep(1)
        
        # إحصائيات المكتبة
        success_rate = (local_successful / len(topics)) * 100
        
        print(f"\n📊 نتائج مكتبة {library_name}:")
        print(f"✅ نجح: {local_successful}")
        print(f"❌ فشل: {local_failed}")
        print(f"📈 معدل النجاح: {success_rate:.1f}%")
        
        return {
            'name': library_name,
            'total': len(topics),
            'successful': local_successful,
            'failed': local_failed,
            'success_rate': success_rate
        }
    
    def build_all_libraries(self):
        """بناء جميع المكتبات المتخصصة"""
        print("🚀 بدء بناء جميع المكتبات المتخصصة...")
        print(f"⏰ وقت البدء: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        libraries = []
        
        try:
            # بناء المكتبات واحدة تلو الأخرى
            libraries.append(self.build_ai_library())
            libraries.append(self.build_programming_library())
            libraries.append(self.build_science_library())
            libraries.append(self.build_arabic_language_library())
            
        except KeyboardInterrupt:
            print("\n⚠️ تم إيقاف العملية بواسطة المستخدم")
        except Exception as e:
            print(f"\n❌ خطأ عام: {e}")
        
        # التقرير النهائي
        self._generate_final_report(libraries)
    
    def _generate_final_report(self, libraries: list):
        """إنتاج التقرير النهائي"""
        end_time = datetime.now()
        duration = end_time - self.start_time
        
        print("\n" + "="*60)
        print("📊 التقرير النهائي لبناء المكتبات المتخصصة")
        print("="*60)
        
        print(f"⏰ وقت البدء: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏰ وقت الانتهاء: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏱️ المدة الإجمالية: {duration}")
        
        print(f"\n📈 الإحصائيات الإجمالية:")
        print(f"✅ إجمالي النجاح: {self.successful}")
        print(f"❌ إجمالي الفشل: {self.failed}")
        
        if self.successful + self.failed > 0:
            overall_success = (self.successful / (self.successful + self.failed)) * 100
            print(f"📊 معدل النجاح الإجمالي: {overall_success:.1f}%")
        
        print(f"\n📚 تفاصيل المكتبات:")
        for lib in libraries:
            print(f"  📖 {lib['name']}:")
            print(f"    ✅ نجح: {lib['successful']}/{lib['total']} ({lib['success_rate']:.1f}%)")
        
        # تقييم الجودة
        if overall_success >= 80:
            print(f"\n🎉 ممتاز! تم بناء مكتبة معرفية عالية الجودة")
        elif overall_success >= 60:
            print(f"\n👍 جيد! مكتبة معرفية مقبولة مع إمكانية التحسين")
        else:
            print(f"\n⚠️ يحتاج تحسين! راجع إعدادات النظام والاتصال")
        
        print(f"\n🎯 الخطوات التالية:")
        print(f"  1. اختبار البحث في المعرفة الجديدة")
        print(f"  2. مراجعة جودة المحتوى المستخرج")
        print(f"  3. إضافة مواضيع إضافية حسب الحاجة")
        print(f"  4. تطوير نظام تقييم جودة المعرفة")

def main():
    """الدالة الرئيسية"""
    print("🧬 مرحباً بك في بناء المكتبات المتخصصة!")
    print("هذا السكريبت سيبني مكتبات معرفية متخصصة في:")
    print("  1. الذكاء الاصطناعي")
    print("  2. البرمجة")
    print("  3. العلوم")
    print("  4. اللغة العربية")
    print()
    
    response = input("هل تريد المتابعة؟ (y/n): ").lower().strip()
    if response not in ['y', 'yes', 'نعم', 'ن']:
        print("تم الإلغاء.")
        return
    
    builder = SpecializedLibraryBuilder()
    builder.build_all_libraries()

if __name__ == "__main__":
    main()
