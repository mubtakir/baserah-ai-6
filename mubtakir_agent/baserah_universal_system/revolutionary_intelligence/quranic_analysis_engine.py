#!/usr/bin/env python3
# quranic_analysis_engine.py - محرك التحليل القرآني الثوري
#
# 👨‍💻 المطور: باسل يحيى عبدالله
# 🧠 الأفكار الابتكارية: جميع الأفكار والنظريات الثورية من إبداع باسل يحيى عبدالله
# 🤖 التطوير: أكواد بدائية تم تطويرها بمساعدة وكيل ذكاء اصطناعي
# 📅 تاريخ الإنشاء: 2025
# 🕌 المحرك: أول محرك في العالم لتحليل القرآن الكريم بنظريات باسل الثورية
# 🌟 النظام: Baserah Pure System - sigmoid + linear فقط، بدون AI تقليدي
# تحليل القرآن الكريم بنظريات باسل الثورية ونظام Baserah النقي

import os
import sys
import json
import sqlite3
import re
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import math

# إضافة المسار للوصول للنظام الثوري
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد النواة الفنية
from artistic_intelligence.baserah_core import (
    baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid
)

# استيراد النظام الأساسي
from .ai_oop_foundation import BaserahExpertExplorerFoundation
from .revolutionary_mother_equation import ConcreteRevolutionaryMotherEquation
from .arabic_lexicon_engine import ArabicLexiconEngine


class QuranicTextType(Enum):
    """أنواع النصوص القرآنية."""
    VERSE = "آية"
    SURAH = "سورة"
    JUZ = "جزء"
    HIZB = "حزب"
    QUARTER = "ربع"
    WORD = "كلمة"
    LETTER = "حرف"


class SurahType(Enum):
    """أنواع السور."""
    MECCAN = "مكية"
    MEDINAN = "مدنية"


@dataclass
class QuranicVerse:
    """آية قرآنية مع بياناتها."""
    surah_number: int
    verse_number: int
    arabic_text: str
    surah_name: str
    surah_type: SurahType
    revelation_order: int
    juz_number: int
    hizb_number: int
    quarter_number: int
    words_count: int
    letters_count: int
    metadata: Dict[str, Any]


@dataclass
class QuranicAnalysis:
    """تحليل ثوري لنص قرآني."""
    text: str
    text_type: QuranicTextType
    baserah_analysis: Dict[str, float]
    basil_theories_application: Dict[str, Any]
    letter_frequency: Dict[str, int]
    word_analysis: List[Dict[str, Any]]
    numerical_miracle: Dict[str, Any]
    semantic_weight: float
    revolutionary_insights: List[str]
    divine_patterns: List[str]
    linguistic_features: Dict[str, Any]
    timestamp: str


@dataclass
class NumericalMiracle:
    """إعجاز رقمي قرآني."""
    miracle_type: str
    description: str
    numbers_involved: List[int]
    baserah_calculation: float
    basil_theory_applied: str
    significance_level: float
    verification_method: str


class QuranicAnalysisEngine(BaserahExpertExplorerFoundation):
    """
    محرك التحليل القرآني الثوري.
    
    يدمج:
    1. النص القرآني الكامل مع التشكيل
    2. تحليل الآيات بنظريات باسل الثورية
    3. استكشاف الإعجاز الرقمي بنظام Baserah
    4. دراسة دلالات الحروف في السياق القرآني
    5. اكتشاف الأنماط الإلهية والمعجزات اللغوية
    """
    
    def __init__(self, engine_name: str = "QuranicAnalysisEngine",
                 mother_inheritance: ConcreteRevolutionaryMotherEquation = None):
        """تهيئة محرك التحليل القرآني الثوري."""
        
        # الوراثة من الأسس الثورية
        super().__init__(engine_name, mother_inheritance)
        
        # معلومات المحرك
        self.engine_name = engine_name
        self.creation_time = datetime.now()
        self.version = "1.0.0 - Quranic Analysis Engine"
        
        # قاعدة بيانات القرآن
        self.quran_db_path = "data/quran_analysis.db"
        self.quran_text_path = "data/quran/quran_text.json"
        
        # محرك المعجم العربي المدمج
        self.lexicon_engine = ArabicLexiconEngine("QuranicLexiconEngine")
        
        # إحصائيات المحرك
        self.engine_stats = {
            'verses_analyzed': 0,
            'surahs_analyzed': 0,
            'words_analyzed': 0,
            'letters_analyzed': 0,
            'numerical_miracles_discovered': 0,
            'divine_patterns_found': 0,
            'baserah_analyses_performed': 0,
            'basil_theories_applications': 0,
            'total_revolutionary_insights': 0,
            'average_semantic_weight': 0.0
        }
        
        # بيانات القرآن الأساسية
        self.quran_data = {
            'total_surahs': 114,
            'total_verses': 6236,  # عدد الآيات حسب العد الكوفي
            'total_words': 77439,  # تقريبي
            'total_letters': 323015,  # تقريبي
            'meccan_surahs': 86,
            'medinan_surahs': 28
        }
        
        # أسماء السور
        self.surah_names = self._load_surah_names()
        
        # تهيئة قاعدة البيانات
        self._initialize_quran_database()
        
        # تحميل النص القرآني
        self._load_quran_text()
        
        print(f"🕌 تم تهيئة محرك التحليل القرآني الثوري: {engine_name}")
        print(f"📖 سور القرآن: {self.quran_data['total_surahs']}")
        print(f"📝 آيات القرآن: {self.quran_data['total_verses']}")
        print(f"🧬 مدعوم بنظريات باسل الثورية")
        print(f"🌟 مدمج مع نظام Baserah النقي")
    
    def _load_surah_names(self) -> Dict[int, Dict[str, str]]:
        """تحميل أسماء السور."""
        
        surah_names = {
            1: {"arabic": "الفاتحة", "english": "Al-Fatiha", "type": "meccan"},
            2: {"arabic": "البقرة", "english": "Al-Baqarah", "type": "medinan"},
            3: {"arabic": "آل عمران", "english": "Aal-E-Imran", "type": "medinan"},
            4: {"arabic": "النساء", "english": "An-Nisa", "type": "medinan"},
            5: {"arabic": "المائدة", "english": "Al-Maidah", "type": "medinan"},
            6: {"arabic": "الأنعام", "english": "Al-An'am", "type": "meccan"},
            7: {"arabic": "الأعراف", "english": "Al-A'raf", "type": "meccan"},
            8: {"arabic": "الأنفال", "english": "Al-Anfal", "type": "medinan"},
            9: {"arabic": "التوبة", "english": "At-Tawbah", "type": "medinan"},
            10: {"arabic": "يونس", "english": "Yunus", "type": "meccan"},
            11: {"arabic": "هود", "english": "Hud", "type": "meccan"},
            12: {"arabic": "يوسف", "english": "Yusuf", "type": "meccan"},
            13: {"arabic": "الرعد", "english": "Ar-Ra'd", "type": "medinan"},
            14: {"arabic": "إبراهيم", "english": "Ibrahim", "type": "meccan"},
            15: {"arabic": "الحجر", "english": "Al-Hijr", "type": "meccan"},
            16: {"arabic": "النحل", "english": "An-Nahl", "type": "meccan"},
            17: {"arabic": "الإسراء", "english": "Al-Isra", "type": "meccan"},
            18: {"arabic": "الكهف", "english": "Al-Kahf", "type": "meccan"},
            19: {"arabic": "مريم", "english": "Maryam", "type": "meccan"},
            20: {"arabic": "طه", "english": "Taha", "type": "meccan"},
            # يمكن إضافة باقي السور...
        }
        
        # إضافة السور المتبقية بشكل مبسط
        remaining_surahs = {
            21: {"arabic": "الأنبياء", "english": "Al-Anbiya", "type": "meccan"},
            22: {"arabic": "الحج", "english": "Al-Hajj", "type": "medinan"},
            23: {"arabic": "المؤمنون", "english": "Al-Mu'minun", "type": "meccan"},
            24: {"arabic": "النور", "english": "An-Nur", "type": "medinan"},
            25: {"arabic": "الفرقان", "english": "Al-Furqan", "type": "meccan"},
            # ... يمكن إكمال القائمة
            112: {"arabic": "الإخلاص", "english": "Al-Ikhlas", "type": "meccan"},
            113: {"arabic": "الفلق", "english": "Al-Falaq", "type": "meccan"},
            114: {"arabic": "الناس", "english": "An-Nas", "type": "meccan"}
        }
        
        surah_names.update(remaining_surahs)
        return surah_names
    
    def _initialize_quran_database(self):
        """تهيئة قاعدة بيانات القرآن."""
        
        # إنشاء مجلد البيانات
        os.makedirs(os.path.dirname(self.quran_db_path), exist_ok=True)
        
        try:
            conn = sqlite3.connect(self.quran_db_path)
            cursor = conn.cursor()
            
            # جدول السور
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS surahs (
                    id INTEGER PRIMARY KEY,
                    number INTEGER UNIQUE NOT NULL,
                    arabic_name TEXT NOT NULL,
                    english_name TEXT,
                    type TEXT,
                    verses_count INTEGER,
                    revelation_order INTEGER,
                    baserah_analysis TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # جدول الآيات
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS verses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    surah_number INTEGER NOT NULL,
                    verse_number INTEGER NOT NULL,
                    arabic_text TEXT NOT NULL,
                    words_count INTEGER,
                    letters_count INTEGER,
                    juz_number INTEGER,
                    hizb_number INTEGER,
                    quarter_number INTEGER,
                    baserah_analysis TEXT,
                    basil_theories TEXT,
                    semantic_weight REAL,
                    numerical_miracles TEXT,
                    revolutionary_insights TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(surah_number, verse_number)
                )
            ''')
            
            # جدول الكلمات القرآنية
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS quranic_words (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    word TEXT NOT NULL,
                    root TEXT,
                    surah_number INTEGER,
                    verse_number INTEGER,
                    word_position INTEGER,
                    frequency_in_quran INTEGER,
                    baserah_value REAL,
                    semantic_weight REAL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # جدول الإعجاز الرقمي
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS numerical_miracles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    miracle_type TEXT NOT NULL,
                    description TEXT,
                    numbers_involved TEXT,
                    baserah_calculation REAL,
                    basil_theory TEXT,
                    significance_level REAL,
                    verification_method TEXT,
                    discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # جدول الأنماط الإلهية
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS divine_patterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pattern_type TEXT NOT NULL,
                    description TEXT,
                    occurrences TEXT,
                    baserah_analysis TEXT,
                    revolutionary_significance TEXT,
                    discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # فهارس للبحث السريع
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_verse_surah ON verses(surah_number)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_word_text ON quranic_words(word)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_miracle_type ON numerical_miracles(miracle_type)')
            
            conn.commit()
            conn.close()
            
            print(f"✅ تم تهيئة قاعدة بيانات القرآن: {self.quran_db_path}")
            
        except Exception as e:
            print(f"❌ خطأ في تهيئة قاعدة البيانات: {e}")
    
    def _load_quran_text(self):
        """تحميل النص القرآني."""
        
        # إنشاء مجلد النصوص القرآنية
        os.makedirs(os.path.dirname(self.quran_text_path), exist_ok=True)
        
        # إذا لم يكن الملف موجوداً، إنشاء نموذج أساسي
        if not os.path.exists(self.quran_text_path):
            self._create_sample_quran_data()
        
        try:
            with open(self.quran_text_path, 'r', encoding='utf-8') as f:
                self.quran_text_data = json.load(f)
            
            print(f"✅ تم تحميل النص القرآني من: {self.quran_text_path}")
            
        except Exception as e:
            print(f"⚠️ تحذير: لم يتم تحميل النص القرآني: {e}")
            self.quran_text_data = {}
    
    def _create_sample_quran_data(self):
        """إنشاء بيانات قرآنية تجريبية."""
        
        # بيانات تجريبية لبعض الآيات المشهورة
        sample_quran_data = {
            "metadata": {
                "source": "Quranic Analysis Engine",
                "version": "1.0.0",
                "created": datetime.now().isoformat(),
                "description": "بيانات قرآنية تجريبية للنظام الثوري"
            },
            "surahs": {
                "1": {
                    "name": "الفاتحة",
                    "english_name": "Al-Fatiha",
                    "type": "meccan",
                    "verses_count": 7,
                    "verses": {
                        "1": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
                        "2": "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
                        "3": "الرَّحْمَٰنِ الرَّحِيمِ",
                        "4": "مَالِكِ يَوْمِ الدِّينِ",
                        "5": "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ",
                        "6": "اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ",
                        "7": "صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ"
                    }
                },
                "112": {
                    "name": "الإخلاص",
                    "english_name": "Al-Ikhlas",
                    "type": "meccan",
                    "verses_count": 4,
                    "verses": {
                        "1": "قُلْ هُوَ اللَّهُ أَحَدٌ",
                        "2": "اللَّهُ الصَّمَدُ",
                        "3": "لَمْ يَلِدْ وَلَمْ يُولَدْ",
                        "4": "وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ"
                    }
                },
                "113": {
                    "name": "الفلق",
                    "english_name": "Al-Falaq",
                    "type": "meccan",
                    "verses_count": 5,
                    "verses": {
                        "1": "قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ",
                        "2": "مِن شَرِّ مَا خَلَقَ",
                        "3": "وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ",
                        "4": "وَمِن شَرِّ النَّفَّاثَاتِ فِي الْعُقَدِ",
                        "5": "وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ"
                    }
                },
                "114": {
                    "name": "الناس",
                    "english_name": "An-Nas",
                    "type": "meccan",
                    "verses_count": 6,
                    "verses": {
                        "1": "قُلْ أَعُوذُ بِرَبِّ النَّاسِ",
                        "2": "مَلِكِ النَّاسِ",
                        "3": "إِلَٰهِ النَّاسِ",
                        "4": "مِن شَرِّ الْوَسْوَاسِ الْخَنَّاسِ",
                        "5": "الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ",
                        "6": "مِنَ الْجِنَّةِ وَالنَّاسِ"
                    }
                }
            }
        }
        
        # حفظ البيانات
        with open(self.quran_text_path, 'w', encoding='utf-8') as f:
            json.dump(sample_quran_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ تم إنشاء بيانات قرآنية تجريبية: {self.quran_text_path}")
    
    def analyze_verse_revolutionary(self, surah_number: int, verse_number: int, 
                                  deep_analysis: bool = True) -> QuranicAnalysis:
        """
        تحليل ثوري شامل لآية قرآنية.
        
        Args:
            surah_number: رقم السورة
            verse_number: رقم الآية
            deep_analysis: تحليل عميق مع نظريات باسل
            
        Returns:
            QuranicAnalysis: تحليل شامل للآية
        """
        
        print(f"🕌 بدء التحليل الثوري للآية: {surah_number}:{verse_number}")
        
        # الحصول على نص الآية
        verse_text = self._get_verse_text(surah_number, verse_number)
        
        if not verse_text:
            raise ValueError(f"لم يتم العثور على الآية {surah_number}:{verse_number}")
        
        # تنظيف النص من التشكيل للتحليل
        clean_text = self._remove_diacritics(verse_text)
        
        # تحليل الكلمات
        words = clean_text.split()
        word_analyses = []
        
        for word in words:
            try:
                word_analysis = self.lexicon_engine.analyze_word_revolutionary(word, deep_analysis=False)
                word_analyses.append({
                    'word': word,
                    'root': word_analysis.root,
                    'meaning': word_analysis.meaning,
                    'semantic_weight': word_analysis.semantic_weight,
                    'baserah_analysis': word_analysis.baserah_analysis
                })
            except Exception as e:
                print(f"⚠️ تحذير: لم يتم تحليل الكلمة '{word}': {e}")
        
        # تحليل الحروف
        letter_frequency = self._analyze_letter_frequency(clean_text)
        
        # تطبيق تحليل Baserah
        baserah_analysis = self._apply_baserah_to_verse(verse_text, word_analyses)
        
        # تطبيق نظريات باسل
        basil_theories = self._apply_basil_theories_to_verse(verse_text, word_analyses) if deep_analysis else {}
        
        # اكتشاف الإعجاز الرقمي
        numerical_miracle = self._discover_numerical_miracles(surah_number, verse_number, verse_text)
        
        # حساب الوزن الدلالي
        semantic_weight = self._calculate_verse_semantic_weight(word_analyses, baserah_analysis)
        
        # توليد الرؤى الثورية
        revolutionary_insights = self._generate_verse_insights(surah_number, verse_number, verse_text, word_analyses)
        
        # اكتشاف الأنماط الإلهية
        divine_patterns = self._discover_divine_patterns(verse_text, baserah_analysis)
        
        # تحليل الخصائص اللغوية
        linguistic_features = self._analyze_linguistic_features(verse_text)
        
        # إنشاء التحليل الشامل
        analysis = QuranicAnalysis(
            text=verse_text,
            text_type=QuranicTextType.VERSE,
            baserah_analysis=baserah_analysis,
            basil_theories_application=basil_theories,
            letter_frequency=letter_frequency,
            word_analysis=word_analyses,
            numerical_miracle=numerical_miracle,
            semantic_weight=semantic_weight,
            revolutionary_insights=revolutionary_insights,
            divine_patterns=divine_patterns,
            linguistic_features=linguistic_features,
            timestamp=datetime.now().isoformat()
        )
        
        # حفظ التحليل في قاعدة البيانات
        self._save_verse_analysis(surah_number, verse_number, analysis)
        
        # تحديث الإحصائيات
        self._update_engine_statistics(analysis)
        
        print(f"✅ اكتمل التحليل الثوري للآية: {surah_number}:{verse_number}")
        
        return analysis

    def _get_verse_text(self, surah_number: int, verse_number: int) -> str:
        """الحصول على نص الآية."""

        try:
            if hasattr(self, 'quran_text_data') and 'surahs' in self.quran_text_data:
                surah_data = self.quran_text_data['surahs'].get(str(surah_number))
                if surah_data and 'verses' in surah_data:
                    return surah_data['verses'].get(str(verse_number), '')

            return ""

        except Exception as e:
            print(f"⚠️ خطأ في الحصول على نص الآية: {e}")
            return ""

    def _remove_diacritics(self, text: str) -> str:
        """إزالة التشكيل من النص."""

        # رموز التشكيل العربية
        diacritics = [
            '\u064B', '\u064C', '\u064D', '\u064E', '\u064F', '\u0650',  # تنوين وحركات
            '\u0651', '\u0652', '\u0653', '\u0654', '\u0655', '\u0656',  # شدة وسكون
            '\u0657', '\u0658', '\u0659', '\u065A', '\u065B', '\u065C',  # علامات أخرى
            '\u065D', '\u065E', '\u065F', '\u0670'  # علامات إضافية
        ]

        clean_text = text
        for diacritic in diacritics:
            clean_text = clean_text.replace(diacritic, '')

        return clean_text

    def _analyze_letter_frequency(self, text: str) -> Dict[str, int]:
        """تحليل تكرار الحروف."""

        frequency = {}

        for char in text:
            if char.isalpha() and 'ا' <= char <= 'ي':  # حروف عربية فقط
                frequency[char] = frequency.get(char, 0) + 1

        return frequency

    def _apply_baserah_to_verse(self, verse_text: str, word_analyses: List[Dict[str, Any]]) -> Dict[str, float]:
        """تطبيق تحليل Baserah على الآية."""

        # جمع القيم من تحليل الكلمات
        semantic_weights = [w['semantic_weight'] for w in word_analyses if 'semantic_weight' in w]

        if not semantic_weights:
            return {'total_value': 0.0, 'average_value': 0.0, 'harmony_index': 0.0}

        # حساب القيم الأساسية
        total_value = sum(semantic_weights)
        average_value = total_value / len(semantic_weights)

        # حساب مؤشر التناغم القرآني
        variance = sum((v - average_value) ** 2 for v in semantic_weights) / len(semantic_weights)
        harmony_index = baserah_sigmoid(1.0 - variance, n=1, k=3.0, x0=0.5, alpha=1.0)

        # تطبيق دوال Baserah المتقدمة
        quantum_value = baserah_quantum_sigmoid(average_value, n=1000, k=2.0, x0=0.5, alpha=1.2)
        linear_trend = baserah_linear(average_value, slope=1.5, intercept=0.1)

        # حساب القيمة الإلهية (Divine Value)
        divine_multiplier = len(verse_text) / 100.0  # عامل الطول
        divine_value = baserah_sigmoid(average_value * divine_multiplier, n=1, k=1.0, x0=0.7, alpha=1.5)

        return {
            'total_value': total_value,
            'average_value': average_value,
            'harmony_index': harmony_index,
            'quantum_value': quantum_value,
            'linear_trend': linear_trend,
            'divine_value': divine_value,
            'verse_length_factor': divine_multiplier,
            'baserah_signature': f"Q_{total_value:.3f}_{harmony_index:.3f}_{divine_value:.3f}"
        }

    def _apply_basil_theories_to_verse(self, verse_text: str, word_analyses: List[Dict[str, Any]]) -> Dict[str, Any]:
        """تطبيق نظريات باسل الثورية على الآية."""

        basil_theories = {}

        if not word_analyses:
            return basil_theories

        semantic_weights = [w['semantic_weight'] for w in word_analyses if 'semantic_weight' in w]

        # نظرية ثنائية الصفر القرآنية
        positive_words = [w for i, w in enumerate(word_analyses) if i % 2 == 0]
        negative_words = [w for i, w in enumerate(word_analyses) if i % 2 == 1]

        positive_sum = sum(w['semantic_weight'] for w in positive_words if 'semantic_weight' in w)
        negative_sum = sum(w['semantic_weight'] for w in negative_words if 'semantic_weight' in w)
        divine_balance = abs(positive_sum - negative_sum)

        basil_theories['zero_duality_quranic'] = {
            'positive_sum': positive_sum,
            'negative_sum': negative_sum,
            'divine_balance': divine_balance,
            'is_divinely_balanced': divine_balance < 0.05,  # توازن إلهي أدق
            'balance_percentage': (1 - divine_balance) * 100,
            'theory': 'Zero Duality Theory - Quranic Application'
        }

        # نظرية تعامد الأضداد القرآنية
        if len(word_analyses) >= 2:
            first_half = word_analyses[:len(word_analyses)//2]
            second_half = word_analyses[len(word_analyses)//2:]

            first_half_avg = sum(w['semantic_weight'] for w in first_half if 'semantic_weight' in w) / len(first_half) if first_half else 0
            second_half_avg = sum(w['semantic_weight'] for w in second_half if 'semantic_weight' in w) / len(second_half) if second_half else 0

            divine_angle = abs(first_half_avg - second_half_avg) * 90

            basil_theories['perpendicular_opposites_quranic'] = {
                'first_half_value': first_half_avg,
                'second_half_value': second_half_avg,
                'divine_angle': divine_angle,
                'is_divinely_perpendicular': abs(divine_angle - 90) < 5,  # دقة إلهية
                'theory': 'Perpendicular Opposites Theory - Quranic Application'
            }

        # نظرية الفتائل القرآنية
        quranic_filaments = []
        for i, word_analysis in enumerate(word_analyses):
            filament = {
                'filament_id': i,
                'word': word_analysis['word'],
                'semantic_weight': word_analysis.get('semantic_weight', 0),
                'meaning': word_analysis.get('meaning', ''),
                'is_divine_primary': word_analysis.get('semantic_weight', 0) > 0.7,  # فتيلة إلهية أولية
                'divine_significance': word_analysis.get('semantic_weight', 0) * len(word_analysis['word'])
            }
            quranic_filaments.append(filament)

        basil_theories['filament_theory_quranic'] = {
            'quranic_filaments': quranic_filaments,
            'total_filaments': len(quranic_filaments),
            'divine_primary_filaments': len([f for f in quranic_filaments if f['is_divine_primary']]),
            'divine_reconstruction_possible': len(quranic_filaments) > 0,
            'strongest_divine_filament': max(quranic_filaments, key=lambda x: x['divine_significance']) if quranic_filaments else None,
            'theory': 'Filament Theory - Quranic Application'
        }

        return basil_theories

    def _discover_numerical_miracles(self, surah_number: int, verse_number: int, verse_text: str) -> Dict[str, Any]:
        """اكتشاف الإعجاز الرقمي."""

        miracles = {}

        # إعجاز رقم السورة والآية
        surah_verse_sum = surah_number + verse_number
        surah_verse_product = surah_number * verse_number

        # تطبيق دوال Baserah على الأرقام
        sum_baserah = baserah_sigmoid(surah_verse_sum / 100.0, n=1, k=1.0, x0=0.5, alpha=1.0)
        product_baserah = baserah_sigmoid(surah_verse_product / 1000.0, n=1, k=1.5, x0=0.5, alpha=1.0)

        miracles['surah_verse_numerology'] = {
            'surah_number': surah_number,
            'verse_number': verse_number,
            'sum': surah_verse_sum,
            'product': surah_verse_product,
            'sum_baserah_value': sum_baserah,
            'product_baserah_value': product_baserah,
            'is_miraculous': sum_baserah > 0.7 or product_baserah > 0.7
        }

        # إعجاز طول الآية
        verse_length = len(verse_text)
        words_count = len(verse_text.split())
        letters_count = len([c for c in verse_text if c.isalpha()])

        # نسبة ذهبية قرآنية
        if words_count > 0:
            golden_ratio_quranic = letters_count / words_count
            golden_baserah = baserah_sigmoid(golden_ratio_quranic / 10.0, n=1, k=2.0, x0=0.5, alpha=1.0)

            miracles['golden_ratio_quranic'] = {
                'letters_count': letters_count,
                'words_count': words_count,
                'ratio': golden_ratio_quranic,
                'baserah_value': golden_baserah,
                'is_golden_miraculous': abs(golden_ratio_quranic - 1.618) < 0.5  # قريب من النسبة الذهبية
            }

        # إعجاز الرقم 19 (إعجاز مشهور في القرآن)
        if verse_length % 19 == 0 or letters_count % 19 == 0 or words_count % 19 == 0:
            miracles['nineteen_miracle'] = {
                'verse_length_divisible': verse_length % 19 == 0,
                'letters_divisible': letters_count % 19 == 0,
                'words_divisible': words_count % 19 == 0,
                'significance': 'إعجاز الرقم 19 في القرآن الكريم'
            }

        # إعجاز التماثل
        clean_text = self._remove_diacritics(verse_text).replace(' ', '')
        is_palindromic = clean_text == clean_text[::-1]

        if is_palindromic:
            miracles['palindromic_miracle'] = {
                'is_palindromic': True,
                'significance': 'آية متماثلة (تقرأ نفسها من الأمام والخلف)',
                'divine_symmetry': True
            }

        return miracles

    def _calculate_verse_semantic_weight(self, word_analyses: List[Dict[str, Any]],
                                       baserah_analysis: Dict[str, float]) -> float:
        """حساب الوزن الدلالي للآية."""

        if not word_analyses:
            return 0.0

        # عوامل الوزن الدلالي القرآني
        words_weight = sum(w.get('semantic_weight', 0) for w in word_analyses) / len(word_analyses)
        harmony_weight = baserah_analysis.get('harmony_index', 0.5)
        divine_weight = baserah_analysis.get('divine_value', 0.5)

        # الوزن النهائي مع التأكيد على القيمة الإلهية
        semantic_weight = (words_weight * 0.4 + harmony_weight * 0.3 + divine_weight * 0.3)

        # تطبيق التحويل الثوري القرآني
        return baserah_sigmoid(semantic_weight * 2.0, n=1, k=2.0, x0=0.6, alpha=1.2)

    def _generate_verse_insights(self, surah_number: int, verse_number: int,
                               verse_text: str, word_analyses: List[Dict[str, Any]]) -> List[str]:
        """توليد رؤى ثورية للآية."""

        insights = []

        # رؤى حول موقع الآية
        surah_name = self.surah_names.get(surah_number, {}).get('arabic', f'السورة {surah_number}')
        insights.append(f"هذه الآية من سورة {surah_name} المباركة")

        # رؤى حول التركيب اللغوي
        words_count = len(word_analyses)
        if words_count <= 3:
            insights.append("آية مختصرة ومركزة، كل كلمة فيها لها وزن عظيم")
        elif words_count <= 7:
            insights.append("آية متوسطة الطول، تحمل معاني متوازنة")
        else:
            insights.append("آية طويلة غنية بالمعاني والدلالات")

        # رؤى حول الكلمات المهمة
        high_weight_words = [w for w in word_analyses if w.get('semantic_weight', 0) > 0.7]
        if high_weight_words:
            key_words = [w['word'] for w in high_weight_words[:3]]
            insights.append(f"الكلمات المحورية في الآية: {', '.join(key_words)}")

        # رؤى حول الجذور
        roots = list(set(w['root'] for w in word_analyses if w.get('root')))
        if len(roots) > len(word_analyses) * 0.7:
            insights.append("تنوع لغوي عالي في الجذور، يدل على ثراء المعنى")

        # رؤى حول التوازن الإلهي
        if len(word_analyses) % 2 == 0:
            insights.append("عدد الكلمات زوجي، مما يشير إلى التوازن الإلهي")
        else:
            insights.append("عدد الكلمات فردي، مما يشير إلى الوحدانية الإلهية")

        # رؤى حول الحروف المقطعة (إذا وجدت)
        if any(len(word) == 1 and word in ['الم', 'الر', 'حم', 'طه', 'يس'] for word in [w['word'] for w in word_analyses]):
            insights.append("تحتوي على حروف مقطعة، من أسرار القرآن العظيمة")

        return insights

    def _discover_divine_patterns(self, verse_text: str, baserah_analysis: Dict[str, float]) -> List[str]:
        """اكتشاف الأنماط الإلهية."""

        patterns = []

        # نمط التوازن الإلهي
        harmony_index = baserah_analysis.get('harmony_index', 0)
        if harmony_index > 0.8:
            patterns.append("نمط التوازن الإلهي: تناغم عالي بين عناصر الآية")

        # نمط القيمة الإلهية
        divine_value = baserah_analysis.get('divine_value', 0)
        if divine_value > 0.7:
            patterns.append("نمط القيمة الإلهية: مستوى روحاني عالي في الآية")

        # نمط التكرار
        words = verse_text.split()
        word_counts = {}
        for word in words:
            clean_word = self._remove_diacritics(word)
            word_counts[clean_word] = word_counts.get(clean_word, 0) + 1

        repeated_words = [word for word, count in word_counts.items() if count > 1]
        if repeated_words:
            patterns.append(f"نمط التكرار الإلهي: تكرار الكلمات {', '.join(repeated_words)} للتأكيد")

        # نمط الطول الإلهي
        verse_length = len(verse_text)
        if verse_length in [19, 38, 57, 76, 95, 114]:  # مضاعفات 19
            patterns.append("نمط الطول الإلهي: طول الآية يتبع النظام الرقمي المعجز")

        return patterns

    def _analyze_linguistic_features(self, verse_text: str) -> Dict[str, Any]:
        """تحليل الخصائص اللغوية."""

        features = {}

        # تحليل الطول
        features['length_analysis'] = {
            'total_characters': len(verse_text),
            'letters_only': len([c for c in verse_text if c.isalpha()]),
            'words_count': len(verse_text.split()),
            'average_word_length': len([c for c in verse_text if c.isalpha()]) / len(verse_text.split()) if verse_text.split() else 0
        }

        # تحليل الحروف
        letter_analysis = self._analyze_letter_frequency(self._remove_diacritics(verse_text))
        features['letter_analysis'] = {
            'unique_letters': len(letter_analysis),
            'most_frequent_letter': max(letter_analysis.items(), key=lambda x: x[1]) if letter_analysis else ('', 0),
            'letter_diversity': len(letter_analysis) / len([c for c in verse_text if c.isalpha()]) if verse_text else 0
        }

        # تحليل الأنماط
        features['pattern_analysis'] = {
            'has_repetition': len(set(verse_text.split())) < len(verse_text.split()),
            'starts_with_praise': verse_text.strip().startswith(('الحمد', 'سبح', 'تبارك')),
            'ends_with_divine_name': verse_text.strip().endswith(('الله', 'العليم', 'الحكيم', 'الرحيم')),
            'contains_divine_names': any(name in verse_text for name in ['الله', 'الرحمن', 'الرحيم', 'رب'])
        }

        return features

    def _save_verse_analysis(self, surah_number: int, verse_number: int, analysis: QuranicAnalysis):
        """حفظ تحليل الآية في قاعدة البيانات."""

        try:
            conn = sqlite3.connect(self.quran_db_path)
            cursor = conn.cursor()

            # حفظ تحليل الآية
            cursor.execute('''
                INSERT OR REPLACE INTO verses
                (surah_number, verse_number, arabic_text, words_count, letters_count,
                 baserah_analysis, basil_theories, semantic_weight, numerical_miracles, revolutionary_insights)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                surah_number,
                verse_number,
                analysis.text,
                len(analysis.word_analysis),
                analysis.linguistic_features.get('length_analysis', {}).get('letters_only', 0),
                json.dumps(analysis.baserah_analysis, ensure_ascii=False),
                json.dumps(analysis.basil_theories_application, ensure_ascii=False),
                analysis.semantic_weight,
                json.dumps(analysis.numerical_miracle, ensure_ascii=False),
                json.dumps(analysis.revolutionary_insights, ensure_ascii=False)
            ))

            # حفظ الكلمات القرآنية
            for i, word_analysis in enumerate(analysis.word_analysis):
                cursor.execute('''
                    INSERT OR REPLACE INTO quranic_words
                    (word, root, surah_number, verse_number, word_position, semantic_weight)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    word_analysis['word'],
                    word_analysis.get('root', ''),
                    surah_number,
                    verse_number,
                    i + 1,
                    word_analysis.get('semantic_weight', 0)
                ))

            # حفظ الإعجاز الرقمي
            for miracle_type, miracle_data in analysis.numerical_miracle.items():
                if isinstance(miracle_data, dict):
                    cursor.execute('''
                        INSERT INTO numerical_miracles
                        (miracle_type, description, numbers_involved, significance_level)
                        VALUES (?, ?, ?, ?)
                    ''', (
                        miracle_type,
                        json.dumps(miracle_data, ensure_ascii=False),
                        json.dumps([surah_number, verse_number], ensure_ascii=False),
                        miracle_data.get('baserah_value', 0) if 'baserah_value' in miracle_data else 0.5
                    ))

            # حفظ الأنماط الإلهية
            for pattern in analysis.divine_patterns:
                cursor.execute('''
                    INSERT INTO divine_patterns
                    (pattern_type, description, occurrences)
                    VALUES (?, ?, ?)
                ''', (
                    'verse_pattern',
                    pattern,
                    json.dumps([f"{surah_number}:{verse_number}"], ensure_ascii=False)
                ))

            conn.commit()
            conn.close()

        except Exception as e:
            print(f"⚠️ خطأ في حفظ تحليل الآية: {e}")

    def _update_engine_statistics(self, analysis: QuranicAnalysis):
        """تحديث إحصائيات المحرك."""

        self.engine_stats['verses_analyzed'] += 1
        self.engine_stats['words_analyzed'] += len(analysis.word_analysis)
        self.engine_stats['letters_analyzed'] += analysis.linguistic_features.get('length_analysis', {}).get('letters_only', 0)
        self.engine_stats['baserah_analyses_performed'] += 1

        if analysis.basil_theories_application:
            self.engine_stats['basil_theories_applications'] += len(analysis.basil_theories_application)

        if analysis.numerical_miracle:
            self.engine_stats['numerical_miracles_discovered'] += len(analysis.numerical_miracle)

        if analysis.divine_patterns:
            self.engine_stats['divine_patterns_found'] += len(analysis.divine_patterns)

        self.engine_stats['total_revolutionary_insights'] += len(analysis.revolutionary_insights)

        # تحديث متوسط الوزن الدلالي
        current_avg = self.engine_stats['average_semantic_weight']
        verses_count = self.engine_stats['verses_analyzed']
        new_avg = ((current_avg * (verses_count - 1)) + analysis.semantic_weight) / verses_count
        self.engine_stats['average_semantic_weight'] = new_avg

    def analyze_surah_revolutionary(self, surah_number: int, deep_analysis: bool = True) -> Dict[str, Any]:
        """تحليل ثوري شامل لسورة كاملة."""

        print(f"🕌 بدء التحليل الثوري للسورة: {surah_number}")

        if surah_number not in self.surah_names:
            raise ValueError(f"رقم السورة غير صحيح: {surah_number}")

        surah_info = self.surah_names[surah_number]
        surah_name = surah_info['arabic']

        # الحصول على آيات السورة
        surah_data = self.quran_text_data.get('surahs', {}).get(str(surah_number), {})
        verses = surah_data.get('verses', {})

        if not verses:
            raise ValueError(f"لم يتم العثور على آيات السورة {surah_number}")

        # تحليل كل آية
        verse_analyses = []
        total_semantic_weight = 0.0
        all_words = []
        all_letters_freq = {}
        all_numerical_miracles = {}
        all_divine_patterns = []

        for verse_num in sorted(verses.keys(), key=int):
            try:
                verse_analysis = self.analyze_verse_revolutionary(surah_number, int(verse_num), deep_analysis)
                verse_analyses.append(verse_analysis)

                total_semantic_weight += verse_analysis.semantic_weight
                all_words.extend(verse_analysis.word_analysis)

                # جمع تكرار الحروف
                for letter, freq in verse_analysis.letter_frequency.items():
                    all_letters_freq[letter] = all_letters_freq.get(letter, 0) + freq

                # جمع الإعجاز الرقمي
                for miracle_type, miracle_data in verse_analysis.numerical_miracle.items():
                    if miracle_type not in all_numerical_miracles:
                        all_numerical_miracles[miracle_type] = []
                    all_numerical_miracles[miracle_type].append(miracle_data)

                # جمع الأنماط الإلهية
                all_divine_patterns.extend(verse_analysis.divine_patterns)

            except Exception as e:
                print(f"⚠️ خطأ في تحليل الآية {verse_num}: {e}")

        # تحليل السورة ككل
        surah_baserah_analysis = self._analyze_surah_baserah(verse_analyses)
        surah_basil_theories = self._apply_basil_theories_to_surah(verse_analyses) if deep_analysis else {}
        surah_numerical_miracles = self._discover_surah_numerical_miracles(surah_number, verse_analyses)
        surah_linguistic_features = self._analyze_surah_linguistic_features(verse_analyses)

        # حساب الإحصائيات
        surah_statistics = {
            'surah_number': surah_number,
            'surah_name': surah_name,
            'surah_type': surah_info['type'],
            'total_verses': len(verse_analyses),
            'total_words': len(all_words),
            'total_letters': sum(all_letters_freq.values()),
            'average_semantic_weight': total_semantic_weight / len(verse_analyses) if verse_analyses else 0,
            'unique_letters': len(all_letters_freq),
            'numerical_miracles_count': len(all_numerical_miracles),
            'divine_patterns_count': len(set(all_divine_patterns))
        }

        # الرؤى الثورية للسورة
        surah_insights = self._generate_surah_insights(surah_number, surah_statistics, verse_analyses)

        surah_analysis = {
            'surah_info': surah_info,
            'surah_statistics': surah_statistics,
            'verse_analyses': verse_analyses,
            'surah_baserah_analysis': surah_baserah_analysis,
            'surah_basil_theories': surah_basil_theories,
            'surah_numerical_miracles': surah_numerical_miracles,
            'surah_linguistic_features': surah_linguistic_features,
            'letter_frequency_surah': all_letters_freq,
            'divine_patterns_surah': list(set(all_divine_patterns)),
            'revolutionary_insights_surah': surah_insights,
            'analysis_timestamp': datetime.now().isoformat()
        }

        # تحديث الإحصائيات
        self.engine_stats['surahs_analyzed'] += 1

        print(f"✅ اكتمل التحليل الثوري للسورة: {surah_name}")

        return surah_analysis

    def _analyze_surah_baserah(self, verse_analyses: List[QuranicAnalysis]) -> Dict[str, float]:
        """تحليل Baserah للسورة كاملة."""

        if not verse_analyses:
            return {}

        # جمع القيم من جميع الآيات
        verse_weights = [analysis.semantic_weight for analysis in verse_analyses]
        verse_harmonies = [analysis.baserah_analysis.get('harmony_index', 0) for analysis in verse_analyses]
        verse_divine_values = [analysis.baserah_analysis.get('divine_value', 0) for analysis in verse_analyses]

        # حساب قيم السورة
        surah_total_weight = sum(verse_weights)
        surah_average_weight = surah_total_weight / len(verse_weights)
        surah_harmony = sum(verse_harmonies) / len(verse_harmonies)
        surah_divine_value = sum(verse_divine_values) / len(verse_divine_values)

        # حساب التناغم بين الآيات
        weight_variance = sum((w - surah_average_weight) ** 2 for w in verse_weights) / len(verse_weights)
        inter_verse_harmony = baserah_sigmoid(1.0 - weight_variance, n=1, k=2.0, x0=0.5, alpha=1.0)

        # القيمة الإلهية للسورة
        surah_length_factor = len(verse_analyses) / 100.0
        surah_divine_signature = baserah_sigmoid(surah_divine_value * surah_length_factor, n=1, k=1.5, x0=0.6, alpha=1.3)

        return {
            'surah_total_weight': surah_total_weight,
            'surah_average_weight': surah_average_weight,
            'surah_harmony': surah_harmony,
            'surah_divine_value': surah_divine_value,
            'inter_verse_harmony': inter_verse_harmony,
            'surah_divine_signature': surah_divine_signature,
            'surah_length_factor': surah_length_factor,
            'verses_count': len(verse_analyses)
        }

    def _apply_basil_theories_to_surah(self, verse_analyses: List[QuranicAnalysis]) -> Dict[str, Any]:
        """تطبيق نظريات باسل على السورة."""

        if not verse_analyses:
            return {}

        basil_theories = {}

        # نظرية ثنائية الصفر على مستوى السورة
        positive_verses = [v for i, v in enumerate(verse_analyses) if i % 2 == 0]
        negative_verses = [v for i, v in enumerate(verse_analyses) if i % 2 == 1]

        positive_sum = sum(v.semantic_weight for v in positive_verses)
        negative_sum = sum(v.semantic_weight for v in negative_verses)
        surah_balance = abs(positive_sum - negative_sum)

        basil_theories['zero_duality_surah'] = {
            'positive_verses_sum': positive_sum,
            'negative_verses_sum': negative_sum,
            'surah_balance': surah_balance,
            'is_surah_balanced': surah_balance < 0.1,
            'balance_percentage': (1 - surah_balance) * 100,
            'total_verses': len(verse_analyses)
        }

        # نظرية تعامد الأضداد على مستوى السورة
        if len(verse_analyses) >= 2:
            first_half = verse_analyses[:len(verse_analyses)//2]
            second_half = verse_analyses[len(verse_analyses)//2:]

            first_half_avg = sum(v.semantic_weight for v in first_half) / len(first_half)
            second_half_avg = sum(v.semantic_weight for v in second_half) / len(second_half)

            surah_perpendicular_angle = abs(first_half_avg - second_half_avg) * 90

            basil_theories['perpendicular_opposites_surah'] = {
                'first_half_avg': first_half_avg,
                'second_half_avg': second_half_avg,
                'surah_angle': surah_perpendicular_angle,
                'is_surah_perpendicular': abs(surah_perpendicular_angle - 90) < 10
            }

        # نظرية الفتائل على مستوى السورة
        surah_filaments = []
        for i, verse_analysis in enumerate(verse_analyses):
            filament = {
                'verse_number': i + 1,
                'semantic_weight': verse_analysis.semantic_weight,
                'words_count': len(verse_analysis.word_analysis),
                'is_primary_verse': verse_analysis.semantic_weight > 0.7,
                'divine_significance': verse_analysis.semantic_weight * len(verse_analysis.word_analysis)
            }
            surah_filaments.append(filament)

        basil_theories['filament_theory_surah'] = {
            'surah_filaments': surah_filaments,
            'total_verse_filaments': len(surah_filaments),
            'primary_verse_filaments': len([f for f in surah_filaments if f['is_primary_verse']]),
            'strongest_verse_filament': max(surah_filaments, key=lambda x: x['divine_significance']) if surah_filaments else None
        }

        return basil_theories

    def _discover_surah_numerical_miracles(self, surah_number: int, verse_analyses: List[QuranicAnalysis]) -> Dict[str, Any]:
        """اكتشاف الإعجاز الرقمي للسورة."""

        miracles = {}

        # إعجاز رقم السورة
        surah_baserah = baserah_sigmoid(surah_number / 114.0, n=1, k=1.0, x0=0.5, alpha=1.0)

        miracles['surah_number_miracle'] = {
            'surah_number': surah_number,
            'position_in_quran': surah_number / 114.0,
            'baserah_value': surah_baserah,
            'is_miraculous_position': surah_baserah > 0.7
        }

        # إعجاز عدد الآيات
        verses_count = len(verse_analyses)
        verses_baserah = baserah_sigmoid(verses_count / 100.0, n=1, k=1.5, x0=0.5, alpha=1.0)

        miracles['verses_count_miracle'] = {
            'verses_count': verses_count,
            'baserah_value': verses_baserah,
            'is_miraculous_count': verses_baserah > 0.6
        }

        # إعجاز التوازن في السورة
        total_words = sum(len(v.word_analysis) for v in verse_analyses)
        total_letters = sum(v.linguistic_features.get('length_analysis', {}).get('letters_only', 0) for v in verse_analyses)

        if total_words > 0:
            letters_words_ratio = total_letters / total_words
            ratio_baserah = baserah_sigmoid(letters_words_ratio / 10.0, n=1, k=2.0, x0=0.5, alpha=1.0)

            miracles['surah_balance_miracle'] = {
                'total_words': total_words,
                'total_letters': total_letters,
                'ratio': letters_words_ratio,
                'baserah_value': ratio_baserah,
                'is_balanced_miracle': ratio_baserah > 0.5
            }

        # إعجاز الرقم 19 على مستوى السورة
        if (verses_count % 19 == 0 or total_words % 19 == 0 or
            total_letters % 19 == 0 or surah_number % 19 == 0):

            miracles['nineteen_miracle_surah'] = {
                'verses_divisible': verses_count % 19 == 0,
                'words_divisible': total_words % 19 == 0,
                'letters_divisible': total_letters % 19 == 0,
                'surah_number_divisible': surah_number % 19 == 0,
                'significance': 'إعجاز الرقم 19 على مستوى السورة'
            }

        return miracles

    def _analyze_surah_linguistic_features(self, verse_analyses: List[QuranicAnalysis]) -> Dict[str, Any]:
        """تحليل الخصائص اللغوية للسورة."""

        features = {}

        # إحصائيات عامة
        total_verses = len(verse_analyses)
        total_words = sum(len(v.word_analysis) for v in verse_analyses)
        total_letters = sum(v.linguistic_features.get('length_analysis', {}).get('letters_only', 0) for v in verse_analyses)

        features['general_statistics'] = {
            'total_verses': total_verses,
            'total_words': total_words,
            'total_letters': total_letters,
            'average_words_per_verse': total_words / total_verses if total_verses > 0 else 0,
            'average_letters_per_verse': total_letters / total_verses if total_verses > 0 else 0,
            'average_letters_per_word': total_letters / total_words if total_words > 0 else 0
        }

        # تحليل التنوع
        all_words = []
        for verse_analysis in verse_analyses:
            all_words.extend([w['word'] for w in verse_analysis.word_analysis])

        unique_words = len(set(all_words))
        word_diversity = unique_words / total_words if total_words > 0 else 0

        features['diversity_analysis'] = {
            'unique_words': unique_words,
            'total_words': total_words,
            'word_diversity_ratio': word_diversity,
            'repetition_level': 1 - word_diversity
        }

        # تحليل الأنماط
        verse_lengths = [len(v.word_analysis) for v in verse_analyses]
        features['pattern_analysis'] = {
            'shortest_verse_length': min(verse_lengths) if verse_lengths else 0,
            'longest_verse_length': max(verse_lengths) if verse_lengths else 0,
            'verse_length_variance': sum((l - sum(verse_lengths)/len(verse_lengths))**2 for l in verse_lengths) / len(verse_lengths) if verse_lengths else 0,
            'has_consistent_pattern': max(verse_lengths) - min(verse_lengths) <= 3 if verse_lengths else False
        }

        return features

    def _generate_surah_insights(self, surah_number: int, surah_statistics: Dict[str, Any],
                               verse_analyses: List[QuranicAnalysis]) -> List[str]:
        """توليد رؤى ثورية للسورة."""

        insights = []

        # رؤى حول السورة
        surah_name = surah_statistics['surah_name']
        surah_type = surah_statistics['surah_type']
        insights.append(f"سورة {surah_name} من السور ال{surah_type}ة المباركة")

        # رؤى حول الطول
        verses_count = surah_statistics['total_verses']
        if verses_count <= 10:
            insights.append("سورة قصيرة مركزة، كل آية فيها لها وقع خاص")
        elif verses_count <= 50:
            insights.append("سورة متوسطة الطول، تحمل معاني متوازنة ومتدرجة")
        else:
            insights.append("سورة طويلة غنية بالمعاني والأحكام والقصص")

        # رؤى حول التوازن
        avg_semantic_weight = surah_statistics['average_semantic_weight']
        if avg_semantic_weight > 0.7:
            insights.append("سورة ذات وزن دلالي عالي، تحمل معاني عميقة وقوية")
        elif avg_semantic_weight > 0.5:
            insights.append("سورة متوازنة دلالياً، تجمع بين المعاني المختلفة")
        else:
            insights.append("سورة خفيفة الوزن الدلالي، مناسبة للتأمل والتدبر")

        # رؤى حول الإعجاز الرقمي
        miracles_count = surah_statistics['numerical_miracles_count']
        if miracles_count > 3:
            insights.append("سورة غنية بالإعجاز الرقمي، تحمل أسراراً عددية عظيمة")
        elif miracles_count > 0:
            insights.append("سورة تحتوي على إعجاز رقمي، يدل على النظام الإلهي المحكم")

        # رؤى حول الأنماط الإلهية
        patterns_count = surah_statistics['divine_patterns_count']
        if patterns_count > 5:
            insights.append("سورة غنية بالأنماط الإلهية، تظهر الإبداع الرباني")

        # رؤى حول موقع السورة
        if surah_number == 1:
            insights.append("فاتحة الكتاب، أم القرآن، تحتوي على جوهر الدين")
        elif surah_number <= 10:
            insights.append("من السور الأولى في المصحف، لها مكانة خاصة")
        elif surah_number >= 110:
            insights.append("من السور الأخيرة في المصحف، غالباً ما تكون قصيرة ومؤثرة")

        return insights

    def search_quranic_text(self, search_term: str, search_type: str = 'word') -> Dict[str, Any]:
        """البحث في النص القرآني."""

        print(f"🔍 البحث في القرآن عن: {search_term}")

        results = {
            'search_term': search_term,
            'search_type': search_type,
            'matches': [],
            'total_matches': 0,
            'surahs_found': set(),
            'search_statistics': {}
        }

        # البحث في جميع السور
        for surah_num, surah_data in self.quran_text_data.get('surahs', {}).items():
            surah_number = int(surah_num)
            surah_name = surah_data.get('name', f'السورة {surah_number}')
            verses = surah_data.get('verses', {})

            for verse_num, verse_text in verses.items():
                verse_number = int(verse_num)

                # البحث حسب النوع
                if search_type == 'word':
                    # البحث عن الكلمة
                    clean_verse = self._remove_diacritics(verse_text)
                    clean_search = self._remove_diacritics(search_term)

                    if clean_search in clean_verse.split():
                        match = {
                            'surah_number': surah_number,
                            'surah_name': surah_name,
                            'verse_number': verse_number,
                            'verse_text': verse_text,
                            'match_type': 'exact_word'
                        }
                        results['matches'].append(match)
                        results['surahs_found'].add(surah_number)

                elif search_type == 'partial':
                    # البحث الجزئي
                    clean_verse = self._remove_diacritics(verse_text)
                    clean_search = self._remove_diacritics(search_term)

                    if clean_search in clean_verse:
                        match = {
                            'surah_number': surah_number,
                            'surah_name': surah_name,
                            'verse_number': verse_number,
                            'verse_text': verse_text,
                            'match_type': 'partial_match'
                        }
                        results['matches'].append(match)
                        results['surahs_found'].add(surah_number)

                elif search_type == 'root':
                    # البحث في الجذور
                    words = self._remove_diacritics(verse_text).split()
                    for word in words:
                        try:
                            word_analysis = self.lexicon_engine.analyze_word_revolutionary(word, deep_analysis=False)
                            if word_analysis.root == search_term:
                                match = {
                                    'surah_number': surah_number,
                                    'surah_name': surah_name,
                                    'verse_number': verse_number,
                                    'verse_text': verse_text,
                                    'matched_word': word,
                                    'root': word_analysis.root,
                                    'match_type': 'root_match'
                                }
                                results['matches'].append(match)
                                results['surahs_found'].add(surah_number)
                                break
                        except:
                            continue

        # إحصائيات البحث
        results['total_matches'] = len(results['matches'])
        results['surahs_found'] = list(results['surahs_found'])
        results['search_statistics'] = {
            'total_verses_found': len(results['matches']),
            'total_surahs_found': len(results['surahs_found']),
            'search_coverage': len(results['surahs_found']) / 114 * 100,  # نسبة السور المطابقة
            'most_frequent_surah': max(results['surahs_found'], key=lambda s: len([m for m in results['matches'] if m['surah_number'] == s])) if results['surahs_found'] else None
        }

        print(f"✅ تم العثور على {results['total_matches']} نتيجة في {len(results['surahs_found'])} سورة")

        return results

    def get_engine_status(self) -> Dict[str, Any]:
        """الحصول على حالة محرك التحليل القرآني."""

        return {
            'engine_info': {
                'name': self.engine_name,
                'version': self.version,
                'creation_time': self.creation_time.isoformat(),
                'type': 'quranic_analysis_engine'
            },
            'quran_data': self.quran_data,
            'statistics': self.engine_stats,
            'capabilities': {
                'verse_analysis': True,
                'surah_analysis': True,
                'numerical_miracles_discovery': True,
                'divine_patterns_recognition': True,
                'baserah_integration': True,
                'basil_theories_application': True,
                'quranic_search': True,
                'linguistic_analysis': True,
                'revolutionary_insights': True
            },
            'database_info': {
                'quran_db_path': self.quran_db_path,
                'quran_text_path': self.quran_text_path,
                'database_exists': os.path.exists(self.quran_db_path),
                'text_data_loaded': hasattr(self, 'quran_text_data')
            },
            'lexicon_engine_status': self.lexicon_engine.get_engine_status() if hasattr(self.lexicon_engine, 'get_engine_status') else {},
            'revolutionary_features': {
                'baserah_pure_approach': True,
                'basil_theories_integration': True,
                'divine_patterns_discovery': True,
                'numerical_miracles_analysis': True,
                'quranic_linguistic_analysis': True,
                'revolutionary_insights_generation': True,
                'no_traditional_ai': True
            }
        }

    def export_analysis_results(self, output_file: str, format_type: str = 'json') -> bool:
        """تصدير نتائج التحليل القرآني."""

        try:
            # جمع البيانات للتصدير
            export_data = {
                'engine_info': {
                    'name': self.engine_name,
                    'version': self.version,
                    'export_time': datetime.now().isoformat(),
                    'export_type': 'quranic_analysis_results'
                },
                'quran_metadata': self.quran_data,
                'engine_statistics': self.engine_stats,
                'analysis_results': {
                    'verses': [],
                    'numerical_miracles': [],
                    'divine_patterns': []
                }
            }

            # استخراج نتائج التحليل من قاعدة البيانات
            conn = sqlite3.connect(self.quran_db_path)
            cursor = conn.cursor()

            # استخراج تحليل الآيات
            cursor.execute('SELECT * FROM verses ORDER BY surah_number, verse_number LIMIT 100')
            verses_results = cursor.fetchall()

            for verse_result in verses_results:
                verse_data = {
                    'surah_number': verse_result[1],
                    'verse_number': verse_result[2],
                    'arabic_text': verse_result[3],
                    'semantic_weight': verse_result[7],
                    'analysis_date': verse_result[10]
                }
                export_data['analysis_results']['verses'].append(verse_data)

            # استخراج الإعجاز الرقمي
            cursor.execute('SELECT * FROM numerical_miracles ORDER BY discovered_at DESC LIMIT 50')
            miracles_results = cursor.fetchall()

            for miracle_result in miracles_results:
                miracle_data = {
                    'miracle_type': miracle_result[1],
                    'description': miracle_result[2],
                    'significance_level': miracle_result[5],
                    'discovered_at': miracle_result[7]
                }
                export_data['analysis_results']['numerical_miracles'].append(miracle_data)

            # استخراج الأنماط الإلهية
            cursor.execute('SELECT * FROM divine_patterns ORDER BY discovered_at DESC LIMIT 50')
            patterns_results = cursor.fetchall()

            for pattern_result in patterns_results:
                pattern_data = {
                    'pattern_type': pattern_result[1],
                    'description': pattern_result[2],
                    'discovered_at': pattern_result[6]
                }
                export_data['analysis_results']['divine_patterns'].append(pattern_data)

            conn.close()

            # حفظ البيانات
            if format_type.lower() == 'json':
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(export_data, f, ensure_ascii=False, indent=2)
            else:
                return False

            print(f"✅ تم تصدير نتائج التحليل القرآني إلى: {output_file}")
            return True

        except Exception as e:
            print(f"❌ خطأ في التصدير: {e}")
            return False

    def get_verse_by_reference(self, surah_number: int, verse_number: int) -> Dict[str, Any]:
        """الحصول على آية بالمرجع مع تحليلها."""

        try:
            # الحصول على نص الآية
            verse_text = self._get_verse_text(surah_number, verse_number)

            if not verse_text:
                return {
                    'error': f'لم يتم العثور على الآية {surah_number}:{verse_number}',
                    'success': False
                }

            # معلومات السورة
            surah_info = self.surah_names.get(surah_number, {})

            # تحليل الآية إذا لم تكن محللة من قبل
            try:
                analysis = self.analyze_verse_revolutionary(surah_number, verse_number, deep_analysis=True)

                return {
                    'success': True,
                    'surah_number': surah_number,
                    'verse_number': verse_number,
                    'surah_name': surah_info.get('arabic', f'السورة {surah_number}'),
                    'surah_type': surah_info.get('type', 'غير محدد'),
                    'verse_text': verse_text,
                    'analysis': {
                        'semantic_weight': analysis.semantic_weight,
                        'word_count': len(analysis.word_analysis),
                        'letter_frequency': analysis.letter_frequency,
                        'baserah_analysis': analysis.baserah_analysis,
                        'numerical_miracles': analysis.numerical_miracle,
                        'divine_patterns': analysis.divine_patterns,
                        'revolutionary_insights': analysis.revolutionary_insights,
                        'linguistic_features': analysis.linguistic_features
                    },
                    'reference': f"{surah_number}:{verse_number}",
                    'analysis_timestamp': analysis.timestamp
                }

            except Exception as e:
                return {
                    'success': True,
                    'surah_number': surah_number,
                    'verse_number': verse_number,
                    'surah_name': surah_info.get('arabic', f'السورة {surah_number}'),
                    'verse_text': verse_text,
                    'analysis_error': str(e),
                    'reference': f"{surah_number}:{verse_number}"
                }

        except Exception as e:
            return {
                'error': f'خطأ في الحصول على الآية: {e}',
                'success': False
            }


# === دوال مساعدة للاستخدام السريع ===

def create_quranic_analysis_engine(engine_name: str = "QuickQuranicEngine") -> QuranicAnalysisEngine:
    """إنشاء محرك تحليل قرآني سريع."""

    engine = QuranicAnalysisEngine(engine_name)
    print(f"🕌 تم إنشاء محرك التحليل القرآني: {engine_name}")
    return engine


def analyze_quranic_verse(surah_number: int, verse_number: int,
                         engine_name: str = "QuickVerseAnalyzer") -> Dict[str, Any]:
    """تحليل سريع لآية قرآنية."""

    engine = QuranicAnalysisEngine(engine_name)
    try:
        analysis = engine.analyze_verse_revolutionary(surah_number, verse_number, deep_analysis=True)
        return {
            'success': True,
            'verse_reference': f"{surah_number}:{verse_number}",
            'verse_text': analysis.text,
            'semantic_weight': analysis.semantic_weight,
            'revolutionary_insights': analysis.revolutionary_insights,
            'numerical_miracles': analysis.numerical_miracle,
            'divine_patterns': analysis.divine_patterns
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'verse_reference': f"{surah_number}:{verse_number}"
        }


def search_in_quran(search_term: str, search_type: str = 'word',
                   engine_name: str = "QuickQuranicSearch") -> Dict[str, Any]:
    """بحث سريع في القرآن الكريم."""

    engine = QuranicAnalysisEngine(engine_name)
    result = engine.search_quranic_text(search_term, search_type)
    return result


def get_quranic_verse(surah_number: int, verse_number: int,
                     engine_name: str = "QuickVerseGetter") -> Dict[str, Any]:
    """الحصول السريع على آية قرآنية."""

    engine = QuranicAnalysisEngine(engine_name)
    result = engine.get_verse_by_reference(surah_number, verse_number)
    return result


# === نقطة الدخول الرئيسية ===

def main():
    """الدالة الرئيسية لمحرك التحليل القرآني."""

    print("🕌✨ مرحباً بك في محرك التحليل القرآني الثوري!")
    print("📖 تحليل القرآن الكريم بنظريات باسل ونظام Baserah النقي")
    print()

    # إنشاء المحرك
    engine = QuranicAnalysisEngine("MainQuranicAnalysisEngine")

    # أمثلة على الاستخدام
    print("🔍 أمثلة على التحليل الثوري:")

    # تحليل آية الكرسي (مثال)
    try:
        verse_analysis = engine.get_verse_by_reference(1, 1)  # الفاتحة الآية الأولى
        if verse_analysis['success']:
            print(f"\n📝 تحليل الآية: {verse_analysis['reference']}")
            print(f"   النص: {verse_analysis['verse_text']}")
            print(f"   الوزن الدلالي: {verse_analysis['analysis']['semantic_weight']:.3f}")
            print(f"   عدد الكلمات: {verse_analysis['analysis']['word_count']}")
    except Exception as e:
        print(f"⚠️ خطأ في المثال: {e}")

    # بحث في القرآن
    search_result = engine.search_quranic_text("الله", "word")
    print(f"\n🔍 البحث عن كلمة 'الله':")
    print(f"   نتائج العثور: {search_result['total_matches']}")
    print(f"   سور مطابقة: {len(search_result['surahs_found'])}")

    # عرض حالة المحرك
    status = engine.get_engine_status()
    print(f"\n📊 حالة المحرك:")
    print(f"   آيات محللة: {status['statistics']['verses_analyzed']}")
    print(f"   كلمات محللة: {status['statistics']['words_analyzed']}")
    print(f"   إعجاز رقمي مكتشف: {status['statistics']['numerical_miracles_discovered']}")
    print(f"   أنماط إلهية: {status['statistics']['divine_patterns_found']}")


if __name__ == "__main__":
    main()
