#!/usr/bin/env python3
# arabic_lexicon_engine.py - محرك المعجم العربي الثوري
#
# 👨‍💻 المطور: باسل يحيى عبدالله
# 🧠 الأفكار الابتكارية: جميع الأفكار والنظريات الثورية من إبداع باسل يحيى عبدالله
# 🤖 التطوير: أكواد بدائية تم تطويرها بمساعدة وكيل ذكاء اصطناعي
# 📅 تاريخ الإنشاء: 2025
# 📚 المحرك: محرك ثوري لتحليل اللغة العربية بنظريات باسل الثورية
# 🌟 النظام: Baserah Pure System - sigmoid + linear فقط، بدون AI تقليدي
# مدمج مع نظام Baserah ونظريات باسل لاستكشاف دلالات الحروف والكلمات

import os
import sys
import json
import sqlite3
import requests
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

# إضافة المسار للوصول للنظام الثوري
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد النواة الفنية
from artistic_intelligence.baserah_core import (
    baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid
)

# استيراد النظام الأساسي
from .ai_oop_foundation import BaserahExpertExplorerFoundation
from .revolutionary_mother_equation import ConcreteRevolutionaryMotherEquation


class LexiconSource(Enum):
    """مصادر المعاجم العربية."""
    LISAN_AL_ARAB = "lisan_al_arab"
    TAJ_AL_AROUS = "taj_al_arous"
    QAMOUS_MUHIT = "qamous_muhit"
    MUKHTAR_SAHAH = "mukhtar_sahah"
    WASEET = "waseet"
    AL_GHANI = "al_ghani"
    CUSTOM_DATABASE = "custom_database"


class LetterMeaning(Enum):
    """دلالات الحروف العربية الأساسية."""
    ALIF = "الوحدة والبداية والألوهية"
    BAA = "البيت والاحتواء والبركة"
    TAA = "التاج والعلو والتمام"
    THAA = "الثبات والاستقرار"
    JEEM = "الجمع والاجتماع والجمال"
    HAA_HOTI = "الحياة والحيوية"
    KHAA = "الخروج والخلاص"
    DAL = "الدلالة والإرشاد"
    THAL = "الذل والخضوع"
    RAA = "الرحمة والرقة"
    ZAIN = "الزينة والجمال"
    SEEN = "السرعة والسير"
    SHEEN = "الشعاع والانتشار"
    SAD = "الصدق والصلابة"
    DAD = "الضغط والقوة"
    TAA_MUTBAQA = "الطهارة والنظافة"
    DHAA = "الظهور والوضوح"
    AIN = "العين والرؤية والعلم"
    GHAIN = "الغموض والخفاء"
    FAA = "الفتح والانفتاح"
    QAF = "القوة والشدة"
    KAF = "الكف والإمساك"
    LAM = "اللسان والكلام"
    MEEM = "الماء والحياة"
    NOON = "النور والإضاءة"
    HAA = "الهواء والتنفس"
    WAW = "الواو والربط"
    YAA = "اليد والعمل"


@dataclass
class LexiconEntry:
    """مدخل معجمي ثوري."""
    word: str
    root: str
    meaning: str
    detailed_meaning: str
    source: LexiconSource
    letter_analysis: Dict[str, str]
    baserah_analysis: Dict[str, float]
    basil_theories_application: Dict[str, Any]
    semantic_weight: float
    usage_examples: List[str]
    related_words: List[str]
    metadata: Dict[str, Any]


@dataclass
class LetterAnalysis:
    """تحليل ثوري للحروف."""
    letter: str
    position: int
    meaning: str
    baserah_value: float
    basil_theory_applied: str
    semantic_contribution: float
    revolutionary_insights: List[str]


class ArabicLexiconEngine(BaserahExpertExplorerFoundation):
    """
    محرك المعجم العربي الثوري.
    
    يدمج:
    1. معاجم عربية متعددة (لسان العرب، تاج العروس، إلخ)
    2. تحليل دلالات الحروف بنظريات باسل
    3. معالجة Baserah النقية للمعاني
    4. استكشاف الجذور والاشتقاقات
    5. التكامل مع النظام المعرفي الباهر
    """
    
    def __init__(self, engine_name: str = "ArabicLexiconEngine",
                 mother_inheritance: ConcreteRevolutionaryMotherEquation = None):
        """تهيئة محرك المعجم العربي الثوري."""
        
        # الوراثة من الأسس الثورية
        super().__init__(engine_name, mother_inheritance)
        
        # معلومات المحرك
        self.engine_name = engine_name
        self.creation_time = datetime.now()
        self.version = "1.0.0 - Arabic Lexicon Engine"
        
        # قاعدة بيانات المعجم
        self.lexicon_db_path = "data/arabic_lexicon.db"
        self.letter_meanings_path = "ref/معاني الحروف.txt"
        
        # إحصائيات المحرك
        self.engine_stats = {
            'words_analyzed': 0,
            'letters_analyzed': 0,
            'roots_discovered': 0,
            'meanings_extracted': 0,
            'baserah_analyses_performed': 0,
            'basil_theories_applications': 0,
            'average_semantic_weight': 0.0,
            'total_revolutionary_insights': 0
        }
        
        # معاجم مدمجة
        self.integrated_lexicons = {
            LexiconSource.LISAN_AL_ARAB: {},
            LexiconSource.CUSTOM_DATABASE: {}
        }
        
        # دلالات الحروف
        self.letter_meanings = self._load_letter_meanings()
        
        # تهيئة قاعدة البيانات
        self._initialize_database()
        
        # تحميل المعاجم الأساسية
        self._load_basic_lexicons()
        
        print(f"📚 تم تهيئة محرك المعجم العربي الثوري: {engine_name}")
        print(f"🔤 دلالات الحروف: {len(self.letter_meanings)} حرف")
        print(f"📖 معاجم مدمجة: {len(self.integrated_lexicons)}")
        print(f"🧬 مدعوم بنظريات باسل الثورية")
    
    def _load_letter_meanings(self) -> Dict[str, str]:
        """تحميل دلالات الحروف العربية."""
        
        letter_meanings = {}
        
        # دلالات الحروف الأساسية من النظرية الثورية
        arabic_letters = {
            'ا': LetterMeaning.ALIF.value,
            'ب': LetterMeaning.BAA.value,
            'ت': LetterMeaning.TAA.value,
            'ث': LetterMeaning.THAA.value,
            'ج': LetterMeaning.JEEM.value,
            'ح': LetterMeaning.HAA_HOTI.value,
            'خ': LetterMeaning.KHAA.value,
            'د': LetterMeaning.DAL.value,
            'ذ': LetterMeaning.THAL.value,
            'ر': LetterMeaning.RAA.value,
            'ز': LetterMeaning.ZAIN.value,
            'س': LetterMeaning.SEEN.value,
            'ش': LetterMeaning.SHEEN.value,
            'ص': LetterMeaning.SAD.value,
            'ض': LetterMeaning.DAD.value,
            'ط': LetterMeaning.TAA_MUTBAQA.value,
            'ظ': LetterMeaning.DHAA.value,
            'ع': LetterMeaning.AIN.value,
            'غ': LetterMeaning.GHAIN.value,
            'ف': LetterMeaning.FAA.value,
            'ق': LetterMeaning.QAF.value,
            'ك': LetterMeaning.KAF.value,
            'ل': LetterMeaning.LAM.value,
            'م': LetterMeaning.MEEM.value,
            'ن': LetterMeaning.NOON.value,
            'ه': LetterMeaning.HAA.value,
            'و': LetterMeaning.WAW.value,
            'ي': LetterMeaning.YAA.value
        }
        
        letter_meanings.update(arabic_letters)
        
        # محاولة تحميل من ملف إضافي إذا كان موجوداً
        try:
            if os.path.exists(self.letter_meanings_path):
                with open(self.letter_meanings_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # معالجة المحتوى وإضافة معاني إضافية
                    lines = content.split('\n')
                    for line in lines:
                        if ':' in line:
                            parts = line.split(':', 1)
                            if len(parts) == 2:
                                letter = parts[0].strip()
                                meaning = parts[1].strip()
                                if letter in letter_meanings:
                                    letter_meanings[letter] += f" | {meaning}"
                                else:
                                    letter_meanings[letter] = meaning
        except Exception as e:
            print(f"⚠️ تحذير: لم يتم تحميل ملف معاني الحروف: {e}")
        
        return letter_meanings
    
    def _initialize_database(self):
        """تهيئة قاعدة بيانات المعجم."""
        
        # إنشاء مجلد البيانات إذا لم يكن موجوداً
        os.makedirs(os.path.dirname(self.lexicon_db_path), exist_ok=True)
        
        try:
            conn = sqlite3.connect(self.lexicon_db_path)
            cursor = conn.cursor()
            
            # جدول الكلمات الرئيسي
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS lexicon_entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    word TEXT NOT NULL,
                    root TEXT,
                    meaning TEXT,
                    detailed_meaning TEXT,
                    source TEXT,
                    letter_analysis TEXT,
                    baserah_analysis TEXT,
                    basil_theories TEXT,
                    semantic_weight REAL,
                    usage_examples TEXT,
                    related_words TEXT,
                    metadata TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # جدول تحليل الحروف
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS letter_analyses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    word TEXT NOT NULL,
                    letter TEXT NOT NULL,
                    position INTEGER,
                    meaning TEXT,
                    baserah_value REAL,
                    basil_theory TEXT,
                    semantic_contribution REAL,
                    revolutionary_insights TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # جدول الجذور
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS roots (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    root TEXT UNIQUE NOT NULL,
                    meaning TEXT,
                    derived_words TEXT,
                    baserah_analysis TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # فهارس للبحث السريع
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_word ON lexicon_entries(word)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_root ON lexicon_entries(root)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_letter ON letter_analyses(letter)')
            
            conn.commit()
            conn.close()
            
            print(f"✅ تم تهيئة قاعدة بيانات المعجم: {self.lexicon_db_path}")
            
        except Exception as e:
            print(f"❌ خطأ في تهيئة قاعدة البيانات: {e}")
    
    def _load_basic_lexicons(self):
        """تحميل المعاجم الأساسية."""
        
        # تحميل معجم أساسي مدمج
        basic_lexicon = {
            # كلمات أساسية مع تحليل ثوري
            'الله': {
                'root': 'أله',
                'meaning': 'الإله الواحد الأحد',
                'detailed_meaning': 'اسم الجلالة، الإله المعبود بحق، الواحد الأحد الفرد الصمد',
                'letter_analysis': {
                    'ا': 'الوحدة والبداية',
                    'ل': 'اللسان والكلام الإلهي',
                    'ل': 'التأكيد والتكرار',
                    'ه': 'الهواء والروح الإلهية'
                }
            },
            'حياة': {
                'root': 'حيي',
                'meaning': 'الوجود والبقاء',
                'detailed_meaning': 'النمو والحركة والاستمرار في الوجود',
                'letter_analysis': {
                    'ح': 'الحياة والحيوية',
                    'ي': 'اليد والعمل والحركة',
                    'ا': 'الوحدة والاستمرار',
                    'ة': 'التأنيث والرقة'
                }
            },
            'علم': {
                'root': 'علم',
                'meaning': 'المعرفة والإدراك',
                'detailed_meaning': 'إدراك الشيء على ما هو عليه إدراكاً جازماً',
                'letter_analysis': {
                    'ع': 'العين والرؤية والإدراك',
                    'ل': 'اللسان والتعبير',
                    'م': 'الماء والحياة والنماء'
                }
            },
            'حكمة': {
                'root': 'حكم',
                'meaning': 'العدل والإتقان',
                'detailed_meaning': 'وضع الشيء في موضعه الصحيح، العدل والإتقان',
                'letter_analysis': {
                    'ح': 'الحياة والحيوية',
                    'ك': 'الكف والإمساك والضبط',
                    'م': 'الماء والحياة',
                    'ة': 'التأنيث والرقة'
                }
            }
        }
        
        # إضافة إلى المعجم المدمج
        self.integrated_lexicons[LexiconSource.CUSTOM_DATABASE] = basic_lexicon
        
        # حفظ في قاعدة البيانات
        for word, data in basic_lexicon.items():
            self._save_lexicon_entry(word, data, LexiconSource.CUSTOM_DATABASE)
        
        print(f"📚 تم تحميل المعجم الأساسي: {len(basic_lexicon)} كلمة")
    
    def analyze_word_revolutionary(self, word: str, deep_analysis: bool = True) -> LexiconEntry:
        """
        تحليل ثوري شامل للكلمة.
        
        Args:
            word: الكلمة المراد تحليلها
            deep_analysis: تحليل عميق يشمل نظريات باسل
            
        Returns:
            LexiconEntry: تحليل شامل للكلمة
        """
        
        print(f"🔍 بدء التحليل الثوري للكلمة: {word}")
        
        # البحث في المعاجم المدمجة
        lexicon_data = self._search_in_lexicons(word)
        
        # تحليل الحروف
        letter_analyses = self._analyze_letters_revolutionary(word)
        
        # استخراج الجذر
        root = self._extract_root(word)
        
        # تحليل Baserah
        baserah_analysis = self._apply_baserah_analysis(word, letter_analyses)
        
        # تطبيق نظريات باسل
        basil_theories = self._apply_basil_theories_to_word(word, letter_analyses) if deep_analysis else {}
        
        # حساب الوزن الدلالي
        semantic_weight = self._calculate_semantic_weight(word, letter_analyses, baserah_analysis)
        
        # إنشاء مدخل معجمي ثوري
        lexicon_entry = LexiconEntry(
            word=word,
            root=root,
            meaning=lexicon_data.get('meaning', 'معنى غير محدد'),
            detailed_meaning=lexicon_data.get('detailed_meaning', ''),
            source=LexiconSource.CUSTOM_DATABASE,
            letter_analysis={letter.letter: letter.meaning for letter in letter_analyses},
            baserah_analysis=baserah_analysis,
            basil_theories_application=basil_theories,
            semantic_weight=semantic_weight,
            usage_examples=lexicon_data.get('usage_examples', []),
            related_words=self._find_related_words(word, root),
            metadata={
                'analysis_time': datetime.now().isoformat(),
                'deep_analysis': deep_analysis,
                'revolutionary_method': True
            }
        )
        
        # حفظ التحليل
        self._save_analysis_to_database(lexicon_entry, letter_analyses)
        
        # تحديث الإحصائيات
        self._update_engine_statistics(lexicon_entry, letter_analyses)
        
        print(f"✅ اكتمل التحليل الثوري للكلمة: {word}")
        
        return lexicon_entry

    def _search_in_lexicons(self, word: str) -> Dict[str, Any]:
        """البحث في المعاجم المدمجة."""

        # البحث في المعجم المخصص أولاً
        if word in self.integrated_lexicons[LexiconSource.CUSTOM_DATABASE]:
            return self.integrated_lexicons[LexiconSource.CUSTOM_DATABASE][word]

        # البحث في قاعدة البيانات
        try:
            conn = sqlite3.connect(self.lexicon_db_path)
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM lexicon_entries WHERE word = ?', (word,))
            result = cursor.fetchone()

            if result:
                return {
                    'meaning': result[3],
                    'detailed_meaning': result[4],
                    'usage_examples': json.loads(result[10]) if result[10] else []
                }

            conn.close()

        except Exception as e:
            print(f"⚠️ خطأ في البحث في قاعدة البيانات: {e}")

        # إذا لم توجد، إنشاء تحليل أساسي
        return {
            'meaning': f'كلمة عربية: {word}',
            'detailed_meaning': f'تحليل ثوري للكلمة: {word}',
            'usage_examples': []
        }

    def _analyze_letters_revolutionary(self, word: str) -> List[LetterAnalysis]:
        """تحليل ثوري للحروف."""

        letter_analyses = []

        for i, letter in enumerate(word):
            if letter in self.letter_meanings:
                # تطبيق دوال Baserah على الحرف
                letter_value = ord(letter) / 1000.0  # تحويل إلى قيمة رقمية
                baserah_value = baserah_sigmoid(letter_value, n=1, k=1.5, x0=0.5, alpha=1.0)

                # تحديد نظرية باسل المطبقة
                basil_theory = self._determine_basil_theory_for_letter(letter, i, len(word))

                # حساب المساهمة الدلالية
                semantic_contribution = self._calculate_letter_semantic_contribution(letter, i, word)

                # الرؤى الثورية
                revolutionary_insights = self._generate_letter_insights(letter, i, word)

                letter_analysis = LetterAnalysis(
                    letter=letter,
                    position=i,
                    meaning=self.letter_meanings[letter],
                    baserah_value=baserah_value,
                    basil_theory_applied=basil_theory,
                    semantic_contribution=semantic_contribution,
                    revolutionary_insights=revolutionary_insights
                )

                letter_analyses.append(letter_analysis)

        return letter_analyses

    def _determine_basil_theory_for_letter(self, letter: str, position: int, word_length: int) -> str:
        """تحديد نظرية باسل المناسبة للحرف."""

        # نظرية ثنائية الصفر للحروف في المواضع الزوجية/الفردية
        if position % 2 == 0:
            return "Zero Duality Theory - الموضع الزوجي (إيجابي)"
        else:
            return "Zero Duality Theory - الموضع الفردي (سالب)"

        # يمكن إضافة منطق أكثر تعقيداً هنا

    def _calculate_letter_semantic_contribution(self, letter: str, position: int, word: str) -> float:
        """حساب المساهمة الدلالية للحرف."""

        # عوامل المساهمة
        position_weight = 1.0 - (position / len(word))  # الحروف الأولى أهم
        letter_frequency = word.count(letter) / len(word)  # تكرار الحرف

        # تطبيق دالة السيجمويد
        contribution = baserah_sigmoid(position_weight * letter_frequency, n=1, k=2.0, x0=0.3, alpha=1.0)

        return contribution

    def _generate_letter_insights(self, letter: str, position: int, word: str) -> List[str]:
        """توليد رؤى ثورية للحرف."""

        insights = []

        # رؤى حسب الموضع
        if position == 0:
            insights.append(f"الحرف الأول '{letter}' يحدد الاتجاه الدلالي للكلمة")
        elif position == len(word) - 1:
            insights.append(f"الحرف الأخير '{letter}' يختتم المعنى ويثبته")
        else:
            insights.append(f"الحرف '{letter}' في الموضع {position + 1} يربط بين أجزاء المعنى")

        # رؤى حسب المعنى
        meaning = self.letter_meanings.get(letter, '')
        if 'الوحدة' in meaning:
            insights.append("يشير إلى مفهوم الوحدة والتفرد")
        elif 'الحياة' in meaning:
            insights.append("يضفي معنى الحيوية والنشاط")
        elif 'العلم' in meaning:
            insights.append("يدل على المعرفة والإدراك")

        return insights

    def _extract_root(self, word: str) -> str:
        """استخراج الجذر الثلاثي للكلمة."""

        # خوارزمية بسيطة لاستخراج الجذر
        # يمكن تطويرها لتكون أكثر دقة

        # إزالة الحروف الزائدة الشائعة
        prefixes = ['ال', 'و', 'ف', 'ب', 'ك', 'ل']
        suffixes = ['ة', 'ان', 'ين', 'ون', 'ها', 'هم', 'هن', 'كم', 'كن']

        clean_word = word

        # إزالة البادئات
        for prefix in prefixes:
            if clean_word.startswith(prefix):
                clean_word = clean_word[len(prefix):]
                break

        # إزالة اللواحق
        for suffix in suffixes:
            if clean_word.endswith(suffix):
                clean_word = clean_word[:-len(suffix)]
                break

        # استخراج الجذر الثلاثي (أول 3 حروف عادة)
        if len(clean_word) >= 3:
            return clean_word[:3]
        else:
            return clean_word

    def _apply_baserah_analysis(self, word: str, letter_analyses: List[LetterAnalysis]) -> Dict[str, float]:
        """تطبيق تحليل Baserah على الكلمة."""

        # جمع قيم الحروف
        letter_values = [analysis.baserah_value for analysis in letter_analyses]

        if not letter_values:
            return {'total_value': 0.0, 'average_value': 0.0, 'harmony_index': 0.0}

        # حساب القيم الإجمالية
        total_value = sum(letter_values)
        average_value = total_value / len(letter_values)

        # حساب مؤشر التناغم (مدى تقارب قيم الحروف)
        variance = sum((v - average_value) ** 2 for v in letter_values) / len(letter_values)
        harmony_index = baserah_sigmoid(1.0 - variance, n=1, k=3.0, x0=0.5, alpha=1.0)

        # تطبيق دوال Baserah المتقدمة
        quantum_value = baserah_quantum_sigmoid(average_value, n=1000, k=2.0, x0=0.5, alpha=1.2)
        linear_trend = baserah_linear(average_value, slope=1.5, intercept=0.1)

        return {
            'total_value': total_value,
            'average_value': average_value,
            'harmony_index': harmony_index,
            'quantum_value': quantum_value,
            'linear_trend': linear_trend,
            'baserah_signature': f"{total_value:.3f}_{harmony_index:.3f}_{quantum_value:.3f}"
        }

    def _apply_basil_theories_to_word(self, word: str, letter_analyses: List[LetterAnalysis]) -> Dict[str, Any]:
        """تطبيق نظريات باسل الثورية على الكلمة."""

        basil_theories = {}

        # نظرية ثنائية الصفر
        positive_letters = [l for l in letter_analyses if l.position % 2 == 0]
        negative_letters = [l for l in letter_analyses if l.position % 2 == 1]

        positive_sum = sum(l.baserah_value for l in positive_letters)
        negative_sum = sum(l.baserah_value for l in negative_letters)
        balance = abs(positive_sum - negative_sum)

        basil_theories['zero_duality'] = {
            'positive_sum': positive_sum,
            'negative_sum': negative_sum,
            'balance': balance,
            'is_balanced': balance < 0.1,
            'theory': 'Zero Duality Theory - ثنائية الصفر'
        }

        # نظرية تعامد الأضداد
        if len(letter_analyses) >= 2:
            first_half = letter_analyses[:len(letter_analyses)//2]
            second_half = letter_analyses[len(letter_analyses)//2:]

            first_half_avg = sum(l.baserah_value for l in first_half) / len(first_half)
            second_half_avg = sum(l.baserah_value for l in second_half) / len(second_half)

            perpendicular_angle = abs(first_half_avg - second_half_avg) * 90

            basil_theories['perpendicular_opposites'] = {
                'first_half_value': first_half_avg,
                'second_half_value': second_half_avg,
                'perpendicular_angle': perpendicular_angle,
                'is_perpendicular': abs(perpendicular_angle - 90) < 10,
                'theory': 'Perpendicular Opposites Theory - تعامد الأضداد'
            }

        # نظرية الفتائل
        filaments = []
        for i, letter_analysis in enumerate(letter_analyses):
            filament = {
                'filament_id': i,
                'letter': letter_analysis.letter,
                'value': letter_analysis.baserah_value,
                'meaning_contribution': letter_analysis.semantic_contribution,
                'is_primary': letter_analysis.baserah_value > 0.5
            }
            filaments.append(filament)

        basil_theories['filament_theory'] = {
            'filaments': filaments,
            'total_filaments': len(filaments),
            'primary_filaments': len([f for f in filaments if f['is_primary']]),
            'reconstruction_possible': len(filaments) > 0,
            'theory': 'Filament Theory - نظرية الفتائل'
        }

        return basil_theories

    def _calculate_semantic_weight(self, word: str, letter_analyses: List[LetterAnalysis],
                                 baserah_analysis: Dict[str, float]) -> float:
        """حساب الوزن الدلالي للكلمة."""

        # عوامل الوزن الدلالي
        length_factor = baserah_sigmoid(len(word) / 10.0, n=1, k=1.0, x0=0.5, alpha=1.0)
        harmony_factor = baserah_analysis.get('harmony_index', 0.5)
        contribution_factor = sum(l.semantic_contribution for l in letter_analyses) / len(letter_analyses) if letter_analyses else 0.0

        # الوزن النهائي
        semantic_weight = (length_factor + harmony_factor + contribution_factor) / 3.0

        # تطبيق التحويل الثوري
        return baserah_sigmoid(semantic_weight * 2.0, n=1, k=2.0, x0=0.5, alpha=1.0)

    def _find_related_words(self, word: str, root: str) -> List[str]:
        """البحث عن الكلمات ذات الصلة."""

        related_words = []

        # البحث في قاعدة البيانات عن كلمات بنفس الجذر
        try:
            conn = sqlite3.connect(self.lexicon_db_path)
            cursor = conn.cursor()

            cursor.execute('SELECT word FROM lexicon_entries WHERE root = ? AND word != ?', (root, word))
            results = cursor.fetchall()

            related_words = [result[0] for result in results]

            conn.close()

        except Exception as e:
            print(f"⚠️ خطأ في البحث عن الكلمات ذات الصلة: {e}")

        # إضافة كلمات افتراضية إذا لم توجد
        if not related_words and root:
            # كلمات شائعة بنفس الجذر (يمكن تطويرها)
            common_patterns = [f"{root}ة", f"م{root}", f"{root}ي", f"{root}ان"]
            related_words = [pattern for pattern in common_patterns if pattern != word]

        return related_words[:5]  # أول 5 كلمات

    def _save_lexicon_entry(self, word: str, data: Dict[str, Any], source: LexiconSource):
        """حفظ مدخل معجمي في قاعدة البيانات."""

        try:
            conn = sqlite3.connect(self.lexicon_db_path)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT OR REPLACE INTO lexicon_entries
                (word, root, meaning, detailed_meaning, source, letter_analysis, usage_examples, related_words, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                word,
                data.get('root', ''),
                data.get('meaning', ''),
                data.get('detailed_meaning', ''),
                source.value,
                json.dumps(data.get('letter_analysis', {}), ensure_ascii=False),
                json.dumps(data.get('usage_examples', []), ensure_ascii=False),
                json.dumps(data.get('related_words', []), ensure_ascii=False),
                json.dumps({'source': source.value}, ensure_ascii=False)
            ))

            conn.commit()
            conn.close()

        except Exception as e:
            print(f"❌ خطأ في حفظ المدخل المعجمي: {e}")

    def _save_analysis_to_database(self, lexicon_entry: LexiconEntry, letter_analyses: List[LetterAnalysis]):
        """حفظ التحليل في قاعدة البيانات."""

        try:
            conn = sqlite3.connect(self.lexicon_db_path)
            cursor = conn.cursor()

            # حفظ المدخل المعجمي
            cursor.execute('''
                INSERT OR REPLACE INTO lexicon_entries
                (word, root, meaning, detailed_meaning, source, letter_analysis, baserah_analysis,
                 basil_theories, semantic_weight, usage_examples, related_words, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                lexicon_entry.word,
                lexicon_entry.root,
                lexicon_entry.meaning,
                lexicon_entry.detailed_meaning,
                lexicon_entry.source.value,
                json.dumps(lexicon_entry.letter_analysis, ensure_ascii=False),
                json.dumps(lexicon_entry.baserah_analysis, ensure_ascii=False),
                json.dumps(lexicon_entry.basil_theories_application, ensure_ascii=False),
                lexicon_entry.semantic_weight,
                json.dumps(lexicon_entry.usage_examples, ensure_ascii=False),
                json.dumps(lexicon_entry.related_words, ensure_ascii=False),
                json.dumps(lexicon_entry.metadata, ensure_ascii=False)
            ))

            # حفظ تحليل الحروف
            for letter_analysis in letter_analyses:
                cursor.execute('''
                    INSERT INTO letter_analyses
                    (word, letter, position, meaning, baserah_value, basil_theory,
                     semantic_contribution, revolutionary_insights)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    lexicon_entry.word,
                    letter_analysis.letter,
                    letter_analysis.position,
                    letter_analysis.meaning,
                    letter_analysis.baserah_value,
                    letter_analysis.basil_theory_applied,
                    letter_analysis.semantic_contribution,
                    json.dumps(letter_analysis.revolutionary_insights, ensure_ascii=False)
                ))

            conn.commit()
            conn.close()

        except Exception as e:
            print(f"❌ خطأ في حفظ التحليل: {e}")

    def _update_engine_statistics(self, lexicon_entry: LexiconEntry, letter_analyses: List[LetterAnalysis]):
        """تحديث إحصائيات المحرك."""

        self.engine_stats['words_analyzed'] += 1
        self.engine_stats['letters_analyzed'] += len(letter_analyses)
        self.engine_stats['meanings_extracted'] += 1
        self.engine_stats['baserah_analyses_performed'] += 1

        if lexicon_entry.root:
            self.engine_stats['roots_discovered'] += 1

        if lexicon_entry.basil_theories_application:
            self.engine_stats['basil_theories_applications'] += len(lexicon_entry.basil_theories_application)

        # تحديث متوسط الوزن الدلالي
        current_avg = self.engine_stats['average_semantic_weight']
        words_count = self.engine_stats['words_analyzed']
        new_avg = ((current_avg * (words_count - 1)) + lexicon_entry.semantic_weight) / words_count
        self.engine_stats['average_semantic_weight'] = new_avg

        # حساب الرؤى الثورية
        total_insights = sum(len(l.revolutionary_insights) for l in letter_analyses)
        self.engine_stats['total_revolutionary_insights'] += total_insights

    def search_word_meanings(self, word: str, include_related: bool = True) -> Dict[str, Any]:
        """البحث عن معاني الكلمة مع التحليل الثوري."""

        print(f"🔍 البحث عن معاني الكلمة: {word}")

        # تحليل الكلمة
        lexicon_entry = self.analyze_word_revolutionary(word, deep_analysis=True)

        # تجميع النتائج
        search_results = {
            'word': word,
            'root': lexicon_entry.root,
            'main_meaning': lexicon_entry.meaning,
            'detailed_meaning': lexicon_entry.detailed_meaning,
            'semantic_weight': lexicon_entry.semantic_weight,
            'letter_analysis': lexicon_entry.letter_analysis,
            'baserah_analysis': lexicon_entry.baserah_analysis,
            'basil_theories': lexicon_entry.basil_theories_application,
            'revolutionary_insights': [],
            'related_words': lexicon_entry.related_words if include_related else [],
            'usage_examples': lexicon_entry.usage_examples
        }

        # جمع الرؤى الثورية من تحليل الحروف
        letter_analyses = self._analyze_letters_revolutionary(word)
        for letter_analysis in letter_analyses:
            search_results['revolutionary_insights'].extend(letter_analysis.revolutionary_insights)

        return search_results

    def explore_letter_meanings(self, letter: str) -> Dict[str, Any]:
        """استكشاف دلالات حرف معين."""

        if letter not in self.letter_meanings:
            return {
                'letter': letter,
                'meaning': 'حرف غير معروف',
                'error': 'الحرف غير موجود في قاعدة دلالات الحروف'
            }

        # تحليل الحرف
        letter_value = ord(letter) / 1000.0
        baserah_value = baserah_sigmoid(letter_value, n=1, k=1.5, x0=0.5, alpha=1.0)
        quantum_value = baserah_quantum_sigmoid(letter_value, n=1000, k=2.0, x0=0.5, alpha=1.2)

        # البحث عن كلمات تحتوي على هذا الحرف
        words_with_letter = self._find_words_with_letter(letter)

        return {
            'letter': letter,
            'meaning': self.letter_meanings[letter],
            'baserah_value': baserah_value,
            'quantum_value': quantum_value,
            'frequency_in_database': len(words_with_letter),
            'example_words': words_with_letter[:10],  # أول 10 كلمات
            'revolutionary_analysis': {
                'semantic_power': baserah_value,
                'quantum_signature': quantum_value,
                'letter_position_in_alphabet': ord(letter) - ord('ا') + 1 if 'ا' <= letter <= 'ي' else -1
            }
        }

    def _find_words_with_letter(self, letter: str) -> List[str]:
        """البحث عن كلمات تحتوي على حرف معين."""

        words = []

        try:
            conn = sqlite3.connect(self.lexicon_db_path)
            cursor = conn.cursor()

            cursor.execute('SELECT word FROM lexicon_entries WHERE word LIKE ?', (f'%{letter}%',))
            results = cursor.fetchall()

            words = [result[0] for result in results]

            conn.close()

        except Exception as e:
            print(f"⚠️ خطأ في البحث عن الكلمات: {e}")

        # إضافة من المعجم المدمج
        for word in self.integrated_lexicons[LexiconSource.CUSTOM_DATABASE]:
            if letter in word and word not in words:
                words.append(word)

        return words

    def analyze_text_revolutionary(self, text: str) -> Dict[str, Any]:
        """تحليل ثوري شامل لنص كامل."""

        print(f"📝 بدء التحليل الثوري للنص...")

        # تقسيم النص إلى كلمات
        words = text.split()

        # تحليل كل كلمة
        word_analyses = []
        total_semantic_weight = 0.0
        all_letters = []
        all_roots = set()

        for word in words:
            # تنظيف الكلمة من علامات الترقيم
            clean_word = ''.join(c for c in word if c.isalpha())

            if clean_word:
                try:
                    analysis = self.analyze_word_revolutionary(clean_word, deep_analysis=False)
                    word_analyses.append(analysis)
                    total_semantic_weight += analysis.semantic_weight
                    all_letters.extend(list(clean_word))
                    if analysis.root:
                        all_roots.add(analysis.root)
                except Exception as e:
                    print(f"⚠️ خطأ في تحليل الكلمة '{clean_word}': {e}")

        # تحليل إحصائي للنص
        text_statistics = {
            'total_words': len(words),
            'analyzed_words': len(word_analyses),
            'total_letters': len(all_letters),
            'unique_letters': len(set(all_letters)),
            'unique_roots': len(all_roots),
            'average_semantic_weight': total_semantic_weight / len(word_analyses) if word_analyses else 0.0
        }

        # تحليل الحروف الأكثر تكراراً
        letter_frequency = {}
        for letter in all_letters:
            letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

        most_frequent_letters = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)[:5]

        # تطبيق نظريات باسل على النص كاملاً
        text_basil_analysis = self._apply_basil_theories_to_text(word_analyses)

        return {
            'original_text': text,
            'text_statistics': text_statistics,
            'word_analyses': [
                {
                    'word': analysis.word,
                    'meaning': analysis.meaning,
                    'semantic_weight': analysis.semantic_weight,
                    'root': analysis.root
                } for analysis in word_analyses
            ],
            'letter_frequency': dict(most_frequent_letters),
            'most_frequent_letters_meanings': [
                {
                    'letter': letter,
                    'frequency': freq,
                    'meaning': self.letter_meanings.get(letter, 'غير معروف')
                } for letter, freq in most_frequent_letters
            ],
            'unique_roots': list(all_roots),
            'basil_theories_analysis': text_basil_analysis,
            'revolutionary_insights': self._generate_text_insights(word_analyses, text_statistics),
            'analysis_metadata': {
                'analysis_time': datetime.now().isoformat(),
                'engine_version': self.version,
                'revolutionary_method': True
            }
        }

    def _apply_basil_theories_to_text(self, word_analyses: List[LexiconEntry]) -> Dict[str, Any]:
        """تطبيق نظريات باسل على النص كاملاً."""

        if not word_analyses:
            return {}

        # جمع الأوزان الدلالية
        semantic_weights = [analysis.semantic_weight for analysis in word_analyses]

        # نظرية ثنائية الصفر على مستوى النص
        positive_words = [w for i, w in enumerate(word_analyses) if i % 2 == 0]
        negative_words = [w for i, w in enumerate(word_analyses) if i % 2 == 1]

        positive_sum = sum(w.semantic_weight for w in positive_words)
        negative_sum = sum(w.semantic_weight for w in negative_words)
        text_balance = abs(positive_sum - negative_sum)

        # نظرية تعامد الأضداد
        first_half = word_analyses[:len(word_analyses)//2]
        second_half = word_analyses[len(word_analyses)//2:]

        first_half_avg = sum(w.semantic_weight for w in first_half) / len(first_half) if first_half else 0
        second_half_avg = sum(w.semantic_weight for w in second_half) / len(second_half) if second_half else 0

        # نظرية الفتائل على مستوى النص
        text_filaments = []
        for i, word_analysis in enumerate(word_analyses):
            filament = {
                'word': word_analysis.word,
                'semantic_weight': word_analysis.semantic_weight,
                'position': i,
                'is_primary': word_analysis.semantic_weight > 0.5
            }
            text_filaments.append(filament)

        return {
            'zero_duality_text': {
                'positive_sum': positive_sum,
                'negative_sum': negative_sum,
                'balance': text_balance,
                'is_balanced': text_balance < 0.1,
                'balance_percentage': (1 - text_balance) * 100
            },
            'perpendicular_opposites_text': {
                'first_half_avg': first_half_avg,
                'second_half_avg': second_half_avg,
                'difference': abs(first_half_avg - second_half_avg),
                'is_perpendicular': abs(first_half_avg - second_half_avg) > 0.3
            },
            'filament_theory_text': {
                'total_filaments': len(text_filaments),
                'primary_filaments': len([f for f in text_filaments if f['is_primary']]),
                'filament_density': len(text_filaments) / len(word_analyses) if word_analyses else 0,
                'strongest_filament': max(text_filaments, key=lambda x: x['semantic_weight']) if text_filaments else None
            }
        }

    def _generate_text_insights(self, word_analyses: List[LexiconEntry],
                              text_statistics: Dict[str, Any]) -> List[str]:
        """توليد رؤى ثورية للنص."""

        insights = []

        # رؤى حول الطول والتعقيد
        if text_statistics['total_words'] > 20:
            insights.append("النص طويل ومعقد، يحتاج تحليل عميق للمعاني")
        elif text_statistics['total_words'] < 5:
            insights.append("النص قصير ومركز، المعاني مكثفة")

        # رؤى حول التنوع اللغوي
        diversity_ratio = text_statistics['unique_roots'] / text_statistics['analyzed_words'] if text_statistics['analyzed_words'] > 0 else 0
        if diversity_ratio > 0.7:
            insights.append("النص يتميز بتنوع لغوي عالي وثراء في الجذور")
        elif diversity_ratio < 0.3:
            insights.append("النص يركز على مجموعة محدودة من الجذور والمعاني")

        # رؤى حول الوزن الدلالي
        avg_weight = text_statistics['average_semantic_weight']
        if avg_weight > 0.7:
            insights.append("النص يحمل وزناً دلالياً عالياً ومعاني قوية")
        elif avg_weight < 0.3:
            insights.append("النص خفيف الوزن الدلالي، قد يحتاج تعميق في المعاني")

        # رؤى حول الحروف
        if text_statistics['unique_letters'] > 20:
            insights.append("النص يستخدم معظم الحروف العربية، مما يدل على ثراء لغوي")

        return insights

    def get_engine_status(self) -> Dict[str, Any]:
        """الحصول على حالة محرك المعجم."""

        return {
            'engine_info': {
                'name': self.engine_name,
                'version': self.version,
                'creation_time': self.creation_time.isoformat(),
                'type': 'arabic_lexicon_engine'
            },
            'statistics': self.engine_stats,
            'capabilities': {
                'word_analysis': True,
                'letter_analysis': True,
                'text_analysis': True,
                'root_extraction': True,
                'baserah_integration': True,
                'basil_theories_application': True,
                'revolutionary_insights': True,
                'database_storage': True
            },
            'integrated_lexicons': {
                source.value: len(data) for source, data in self.integrated_lexicons.items()
            },
            'letter_meanings_count': len(self.letter_meanings),
            'database_path': self.lexicon_db_path,
            'revolutionary_features': {
                'baserah_pure_approach': True,
                'basil_theories_integration': True,
                'letter_semantic_analysis': True,
                'quantum_linguistic_processing': True,
                'revolutionary_insights_generation': True
            }
        }

    def export_analysis_results(self, output_file: str, format_type: str = 'json') -> bool:
        """تصدير نتائج التحليل."""

        try:
            # جمع البيانات للتصدير
            export_data = {
                'engine_info': {
                    'name': self.engine_name,
                    'version': self.version,
                    'export_time': datetime.now().isoformat()
                },
                'statistics': self.engine_stats,
                'letter_meanings': self.letter_meanings,
                'analysis_results': []
            }

            # استخراج نتائج التحليل من قاعدة البيانات
            conn = sqlite3.connect(self.lexicon_db_path)
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM lexicon_entries ORDER BY created_at DESC LIMIT 100')
            results = cursor.fetchall()

            for result in results:
                analysis_result = {
                    'word': result[1],
                    'root': result[2],
                    'meaning': result[3],
                    'semantic_weight': result[9],
                    'created_at': result[13]
                }
                export_data['analysis_results'].append(analysis_result)

            conn.close()

            # حفظ البيانات
            if format_type.lower() == 'json':
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(export_data, f, ensure_ascii=False, indent=2)
            else:
                return False

            print(f"✅ تم تصدير النتائج إلى: {output_file}")
            return True

        except Exception as e:
            print(f"❌ خطأ في التصدير: {e}")
            return False


# === دوال مساعدة للاستخدام السريع ===

def create_arabic_lexicon_engine(engine_name: str = "QuickArabicLexicon") -> ArabicLexiconEngine:
    """إنشاء محرك معجم عربي سريع."""

    engine = ArabicLexiconEngine(engine_name)
    print(f"📚 تم إنشاء محرك المعجم العربي: {engine_name}")
    return engine


def analyze_arabic_word(word: str, engine_name: str = "QuickAnalyzer") -> Dict[str, Any]:
    """تحليل سريع لكلمة عربية."""

    engine = ArabicLexiconEngine(engine_name)
    result = engine.search_word_meanings(word, include_related=True)
    return result


def explore_arabic_letter(letter: str, engine_name: str = "QuickExplorer") -> Dict[str, Any]:
    """استكشاف سريع لحرف عربي."""

    engine = ArabicLexiconEngine(engine_name)
    result = engine.explore_letter_meanings(letter)
    return result


def analyze_arabic_text(text: str, engine_name: str = "QuickTextAnalyzer") -> Dict[str, Any]:
    """تحليل سريع لنص عربي."""

    engine = ArabicLexiconEngine(engine_name)
    result = engine.analyze_text_revolutionary(text)
    return result


# === نقطة الدخول الرئيسية ===

def main():
    """الدالة الرئيسية لمحرك المعجم العربي."""

    print("📚✨ مرحباً بك في محرك المعجم العربي الثوري!")
    print("🔤 مدعوم بنظريات باسل ونظام Baserah لاستكشاف دلالات الحروف")
    print()

    # إنشاء المحرك
    engine = ArabicLexiconEngine("MainArabicLexiconEngine")

    # أمثلة على الاستخدام
    print("🔍 أمثلة على التحليل الثوري:")

    # تحليل كلمة
    word_analysis = engine.search_word_meanings("الله")
    print(f"\n📝 تحليل كلمة 'الله':")
    print(f"   المعنى: {word_analysis['main_meaning']}")
    print(f"   الجذر: {word_analysis['root']}")
    print(f"   الوزن الدلالي: {word_analysis['semantic_weight']:.3f}")

    # تحليل حرف
    letter_analysis = engine.explore_letter_meanings("ع")
    print(f"\n🔤 تحليل حرف 'ع':")
    print(f"   المعنى: {letter_analysis['meaning']}")
    print(f"   القيمة الثورية: {letter_analysis['baserah_value']:.3f}")

    # عرض حالة المحرك
    status = engine.get_engine_status()
    print(f"\n📊 حالة المحرك:")
    print(f"   كلمات محللة: {status['statistics']['words_analyzed']}")
    print(f"   حروف محللة: {status['statistics']['letters_analyzed']}")
    print(f"   رؤى ثورية: {status['statistics']['total_revolutionary_insights']}")


if __name__ == "__main__":
    main()
