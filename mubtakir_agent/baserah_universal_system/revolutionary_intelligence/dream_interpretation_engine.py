#!/usr/bin/env python3
# dream_interpretation_engine.py - محرك تفسير الأحلام الثوري

from typing import Dict, List, Any, Optional, Union, Tuple
from datetime import datetime
import uuid
import re

# استيراد الأسس الثورية
from .revolutionary_mother_equation import ConcreteRevolutionaryMotherEquation
from .ai_oop_foundation import BaserahAIOOPFoundation
from .semantic_meaning_engine import SemanticMeaningEngine
from artistic_intelligence.baserah_core import baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid

class DreamInterpretationEngine(BaserahAIOOPFoundation):
    """
    محرك تفسير الأحلام الثوري
    
    يدمج الطرق المعروفة والمبتكرة:
    - التحليل الرمزي والدلالي المتقدم
    - المعادلات الرياضية التكيفية (بدلاً من الشبكات العصبية)
    - تكامل الخبير/المستكشف التطوري
    - الشبكة الدلالية المتكاملة
    - اكتشاف الأنماط الجديدة
    """
    
    def __init__(self, engine_name: str = "DreamInterpretationEngine",
                 mother_equation_inheritance: Dict[str, Any] = None):
        """تهيئة محرك تفسير الأحلام الثوري."""
        
        super().__init__(engine_name, "dream_interpretation_engine", mother_equation_inheritance)
        
        # قاعدة بيانات الرموز الشاملة
        self.symbol_database = {
            'animals': {
                'قط': {'meaning': 'الاستقلالية والغموض', 'emotional_impact': 'هدوء', 'associations': ['ليل', 'صمت', 'حكمة']},
                'كلب': {'meaning': 'الوفاء والحماية', 'emotional_impact': 'أمان', 'associations': ['صداقة', 'حراسة', 'إخلاص']},
                'طائر': {'meaning': 'الحرية والروحانية', 'emotional_impact': 'تحرر', 'associations': ['سماء', 'طيران', 'علو']},
                'أسد': {'meaning': 'القوة والشجاعة', 'emotional_impact': 'قوة', 'associations': ['ملك', 'هيبة', 'سيطرة']}
            },
            'nature': {
                'بحر': {'meaning': 'اللاوعي والعمق', 'emotional_impact': 'غموض', 'associations': ['عمق', 'موج', 'لانهاية']},
                'جبل': {'meaning': 'التحدي والثبات', 'emotional_impact': 'قوة', 'associations': ['علو', 'صعوبة', 'استقرار']},
                'شجرة': {'meaning': 'النمو والحياة', 'emotional_impact': 'نمو', 'associations': ['جذور', 'أوراق', 'ظل']},
                'نهر': {'meaning': 'التدفق والتغيير', 'emotional_impact': 'حركة', 'associations': ['جريان', 'تجديد', 'حياة']}
            },
            'objects': {
                'بيت': {'meaning': 'الأمان والذات', 'emotional_impact': 'أمان', 'associations': ['عائلة', 'دفء', 'حماية']},
                'سيارة': {'meaning': 'التقدم والسيطرة', 'emotional_impact': 'حركة', 'associations': ['سفر', 'سرعة', 'اتجاه']},
                'مفتاح': {'meaning': 'الحلول والفرص', 'emotional_impact': 'أمل', 'associations': ['فتح', 'سر', 'إمكانية']},
                'مرآة': {'meaning': 'التأمل والحقيقة', 'emotional_impact': 'تأمل', 'associations': ['انعكاس', 'ذات', 'وضوح']}
            }
        }
        
        # الأنماط السردية المعروفة والمبتكرة
        self.narrative_patterns = {
            'classic_patterns': [
                {'name': 'المطاردة', 'keywords': ['مطاردة', 'هروب', 'ملاحقة', 'يلاحق', 'يطارد', 'يهرب']},
                {'name': 'السقوط', 'keywords': ['سقوط', 'يسقط', 'سقط', 'يقع', 'وقع']},
                {'name': 'الطيران', 'keywords': ['طيران', 'يطير', 'طار', 'تحليق', 'يحلق', 'حلق']},
                {'name': 'الاختباء', 'keywords': ['اختباء', 'يختبئ', 'اختبأ', 'مخبأ', 'يختفي', 'اختفى']},
                {'name': 'البحث', 'keywords': ['بحث', 'يبحث', 'بحث عن', 'يفتش', 'فتش']}
            ],
            'innovative_patterns': [
                {'name': 'التحول الرقمي', 'keywords': ['كمبيوتر', 'هاتف', 'إنترنت', 'شاشة', 'رقمي']},
                {'name': 'الانصهار الزمني', 'keywords': ['ماضي', 'مستقبل', 'زمن', 'تاريخ', 'عصر']},
                {'name': 'التفاعل الكوني', 'keywords': ['نجوم', 'كواكب', 'فضاء', 'كون', 'مجرة']},
                {'name': 'الذكاء الاصطناعي', 'keywords': ['روبوت', 'ذكي', 'آلة', 'تقنية', 'مستقبل']}
            ]
        }
        
        # محرك الدلالة المعنوية المتكامل
        self.semantic_engine = SemanticMeaningEngine("DreamSemanticEngine", mother_equation_inheritance)
        
        # شبكة الأحلام الدلالية
        self.dream_semantic_network = {
            'dream_nodes': {},      # عقد الأحلام
            'symbol_connections': {},  # روابط الرموز
            'pattern_clusters': {},    # مجموعات الأنماط
            'interpretation_history': []  # تاريخ التفسيرات
        }
        
        # نظام التعلم التطوري للأحلام
        self.evolutionary_learning = {
            'discovered_patterns': {},
            'adaptation_rules': {},
            'interpretation_evolution': {},
            'feedback_integration': {}
        }
        
        # إحصائيات المحرك
        self.engine_stats = {
            'dreams_interpreted': 0,
            'symbols_analyzed': 0,
            'patterns_discovered': 0,
            'accuracy_score': 0.0
        }
        
        print(f"🌙 تم تهيئة محرك تفسير الأحلام الثوري: {engine_name}")
        print("✨ يدمج الطرق المعروفة والمبتكرة لتفسير الأحلام")
    
    def interpret_dream_comprehensive(self, dream_text: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        تفسير شامل للحلم يدمج جميع الطرق المتقدمة.
        
        Args:
            dream_text: نص الحلم
            context: سياق الحلم (العمر، الجنس، الحالة النفسية، ...)
            
        Returns:
            التفسير الشامل للحلم
        """
        
        print(f"🌙 بدء التفسير الشامل للحلم...")
        
        comprehensive_interpretation = {
            'dream_text': dream_text,
            'context': context or {},
            'symbolic_analysis': {},
            'semantic_analysis': {},
            'pattern_analysis': {},
            'evolutionary_insights': {},
            'integrated_interpretation': {},
            'recommendations': [],
            'confidence_score': 0.0
        }
        
        # المرحلة 1: التحليل الرمزي المتقدم
        print("   🔍 المرحلة 1: التحليل الرمزي المتقدم...")
        symbolic_analysis = self._analyze_symbols_advanced(dream_text, context)
        comprehensive_interpretation['symbolic_analysis'] = symbolic_analysis
        
        # المرحلة 2: التحليل الدلالي المعنوي
        print("   🧠 المرحلة 2: التحليل الدلالي المعنوي...")
        semantic_analysis = self._analyze_semantics_meaningful(dream_text, symbolic_analysis, context)
        comprehensive_interpretation['semantic_analysis'] = semantic_analysis
        
        # المرحلة 3: تحليل الأنماط المبتكر
        print("   🔄 المرحلة 3: تحليل الأنماط المبتكر...")
        pattern_analysis = self._analyze_patterns_innovative(dream_text, symbolic_analysis, semantic_analysis)
        comprehensive_interpretation['pattern_analysis'] = pattern_analysis
        
        # المرحلة 4: الاستكشاف التطوري
        print("   🚀 المرحلة 4: الاستكشاف التطوري...")
        evolutionary_insights = self._explore_evolutionary_insights(
            dream_text, symbolic_analysis, semantic_analysis, pattern_analysis, context
        )
        comprehensive_interpretation['evolutionary_insights'] = evolutionary_insights
        
        # المرحلة 5: التكامل الثوري
        print("   🌟 المرحلة 5: التكامل الثوري...")
        integrated_interpretation = self._integrate_revolutionary_interpretation(
            comprehensive_interpretation
        )
        comprehensive_interpretation['integrated_interpretation'] = integrated_interpretation
        
        # المرحلة 6: توليد التوصيات
        print("   💡 المرحلة 6: توليد التوصيات...")
        recommendations = self._generate_dream_recommendations(comprehensive_interpretation)
        comprehensive_interpretation['recommendations'] = recommendations
        
        # حساب درجة الثقة
        confidence_score = self._calculate_interpretation_confidence(comprehensive_interpretation)
        comprehensive_interpretation['confidence_score'] = confidence_score
        
        # تحديث الإحصائيات
        self._update_interpretation_statistics(comprehensive_interpretation)
        
        # إضافة إلى الشبكة الدلالية
        self._add_to_dream_network(comprehensive_interpretation)
        
        print(f"   ✅ اكتمل التفسير - درجة الثقة: {confidence_score:.3f}")
        
        return comprehensive_interpretation
    
    def _analyze_symbols_advanced(self, dream_text: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """تحليل رمزي متقدم للحلم."""
        
        # استخراج الرموز من النص
        extracted_symbols = self._extract_symbols_from_text(dream_text)
        
        # تحليل كل رمز
        symbol_analyses = []
        for symbol in extracted_symbols:
            symbol_analysis = self._analyze_single_symbol(symbol, context)
            symbol_analyses.append(symbol_analysis)
        
        # حساب التفاعل بين الرموز
        symbol_interactions = self._calculate_symbol_interactions(symbol_analyses)
        
        # تطبيق المعادلات الرمزية التكيفية
        symbolic_equations = self._apply_adaptive_symbolic_equations(symbol_analyses, symbol_interactions)
        
        return {
            'extracted_symbols': extracted_symbols,
            'symbol_analyses': symbol_analyses,
            'symbol_interactions': symbol_interactions,
            'symbolic_equations': symbolic_equations,
            'symbolic_weight': self._calculate_symbolic_weight(symbol_analyses)
        }
    
    def _analyze_semantics_meaningful(self, dream_text: str, symbolic_analysis: Dict[str, Any], 
                                    context: Dict[str, Any] = None) -> Dict[str, Any]:
        """تحليل دلالي معنوي متقدم."""
        
        # استخدام محرك الدلالة المعنوية
        semantic_sentence_analysis = self.semantic_engine.parse_semantic_sentence(dream_text)
        
        # تحليل العلاقات الدلالية مع الرموز
        semantic_symbol_relations = self._analyze_semantic_symbol_relations(
            semantic_sentence_analysis, symbolic_analysis
        )
        
        # بناء الشبكة الدلالية للحلم
        dream_semantic_network = self._build_dream_semantic_network(
            semantic_sentence_analysis, semantic_symbol_relations
        )
        
        # تحليل السياق العاطفي
        emotional_context = self._analyze_emotional_context(dream_text, symbolic_analysis, context)
        
        return {
            'semantic_sentence_analysis': semantic_sentence_analysis,
            'semantic_symbol_relations': semantic_symbol_relations,
            'dream_semantic_network': dream_semantic_network,
            'emotional_context': emotional_context,
            'semantic_completeness': semantic_sentence_analysis.get('meaning_completeness', 0.0)
        }
    
    def _analyze_patterns_innovative(self, dream_text: str, symbolic_analysis: Dict[str, Any], 
                                   semantic_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """تحليل الأنماط المبتكر."""
        
        # تحليل الأنماط الكلاسيكية
        classic_patterns = self._recognize_classic_patterns(dream_text)
        
        # تحليل الأنماط المبتكرة
        innovative_patterns = self._recognize_innovative_patterns(dream_text)
        
        # اكتشاف أنماط جديدة بالذكاء التطوري
        evolutionary_patterns = self._discover_evolutionary_patterns(
            dream_text, symbolic_analysis, semantic_analysis
        )
        
        # تحليل الأنماط الزمنية والمكانية
        temporal_spatial_patterns = self._analyze_temporal_spatial_patterns(dream_text)
        
        # حساب قوة الأنماط
        pattern_strengths = self._calculate_pattern_strengths(
            classic_patterns, innovative_patterns, evolutionary_patterns
        )
        
        return {
            'classic_patterns': classic_patterns,
            'innovative_patterns': innovative_patterns,
            'evolutionary_patterns': evolutionary_patterns,
            'temporal_spatial_patterns': temporal_spatial_patterns,
            'pattern_strengths': pattern_strengths,
            'dominant_pattern': self._identify_dominant_pattern(pattern_strengths)
        }
    
    def process_revolutionary_input(self, input_data: Any) -> Any:
        """تنفيذ المعالجة الثورية لمحرك تفسير الأحلام."""
        
        if isinstance(input_data, str):
            return self.interpret_dream_comprehensive(input_data)
        elif isinstance(input_data, dict) and 'dream_text' in input_data:
            return self.interpret_dream_comprehensive(
                input_data['dream_text'], 
                input_data.get('context', {})
            )
        else:
            return self.interpret_dream_comprehensive(str(input_data))
    
    def adapt_parameters(self, feedback: Dict[str, Any]) -> bool:
        """تكييف معاملات محرك تفسير الأحلام."""
        
        try:
            # تكييف دقة التفسير
            if 'interpretation_accuracy' in feedback:
                accuracy = feedback['interpretation_accuracy']
                if accuracy > 0.8:
                    # زيادة تعقيد التحليل
                    self.engine_stats['accuracy_score'] = min(1.0, self.engine_stats['accuracy_score'] + 0.1)
                elif accuracy < 0.5:
                    # تبسيط التحليل
                    self.engine_stats['accuracy_score'] = max(0.0, self.engine_stats['accuracy_score'] - 0.05)
            
            # تكييف قاعدة بيانات الرموز
            if 'new_symbols' in feedback:
                for symbol, meaning in feedback['new_symbols'].items():
                    self._add_symbol_to_database(symbol, meaning)
            
            return True
            
        except Exception as e:
            print(f"❌ خطأ في تكييف معاملات محرك تفسير الأحلام: {e}")
            return False

    def _extract_symbols_from_text(self, dream_text: str) -> List[str]:
        """استخراج الرموز من نص الحلم."""

        symbols = []
        words = re.findall(r'[\u0600-\u06FF\w]+', dream_text.lower())

        # البحث في قاعدة بيانات الرموز
        for word in words:
            for category, symbols_dict in self.symbol_database.items():
                if word in symbols_dict:
                    symbols.append(word)

        return list(set(symbols))  # إزالة التكرار

    def _analyze_single_symbol(self, symbol: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """تحليل رمز واحد."""

        symbol_info = None
        symbol_category = None

        # البحث عن الرمز في قاعدة البيانات
        for category, symbols_dict in self.symbol_database.items():
            if symbol in symbols_dict:
                symbol_info = symbols_dict[symbol]
                symbol_category = category
                break

        if not symbol_info:
            return {'symbol': symbol, 'found': False}

        # تطبيق التحويل الثوري على قوة الرمز
        symbol_strength = baserah_sigmoid(
            len(symbol_info.get('associations', [])) / 5.0,
            n=1, k=1.5, x0=0.0, alpha=1.0
        )

        return {
            'symbol': symbol,
            'found': True,
            'category': symbol_category,
            'meaning': symbol_info.get('meaning', ''),
            'emotional_impact': symbol_info.get('emotional_impact', ''),
            'associations': symbol_info.get('associations', []),
            'symbol_strength': symbol_strength,
            'context_relevance': self._calculate_context_relevance(symbol, context)
        }

    def _calculate_symbol_interactions(self, symbol_analyses: List[Dict[str, Any]]) -> Dict[str, Any]:
        """حساب التفاعل بين الرموز."""

        interactions = []

        for i, symbol1 in enumerate(symbol_analyses):
            for j, symbol2 in enumerate(symbol_analyses[i+1:], i+1):
                if symbol1.get('found') and symbol2.get('found'):
                    # حساب قوة التفاعل
                    interaction_strength = self._calculate_interaction_strength(symbol1, symbol2)

                    if interaction_strength > 0.3:  # عتبة التفاعل المعنوي
                        interactions.append({
                            'symbol1': symbol1['symbol'],
                            'symbol2': symbol2['symbol'],
                            'interaction_type': self._determine_interaction_type(symbol1, symbol2),
                            'interaction_strength': interaction_strength,
                            'combined_meaning': self._generate_combined_meaning(symbol1, symbol2)
                        })

        return {
            'interactions': interactions,
            'interaction_count': len(interactions),
            'overall_interaction_strength': sum(inter['interaction_strength'] for inter in interactions) / max(1, len(interactions))
        }

    def _apply_adaptive_symbolic_equations(self, symbol_analyses: List[Dict[str, Any]],
                                         symbol_interactions: Dict[str, Any]) -> Dict[str, Any]:
        """تطبيق المعادلات الرمزية التكيفية."""

        # معادلة القوة الرمزية الإجمالية
        total_symbol_strength = sum(
            symbol.get('symbol_strength', 0.0) for symbol in symbol_analyses if symbol.get('found')
        )

        # معادلة التفاعل الرمزي
        interaction_factor = symbol_interactions.get('overall_interaction_strength', 0.0)

        # المعادلة التكيفية الرئيسية
        adaptive_equation = baserah_sigmoid(
            (total_symbol_strength + interaction_factor) / 2,
            n=1, k=2.0, x0=0.0, alpha=1.2
        )

        # معادلة التوازن الرمزي
        balance_equation = baserah_linear(
            abs(total_symbol_strength - interaction_factor),
            beta=0.8, gamma=0.1
        )

        return {
            'total_symbol_strength': total_symbol_strength,
            'interaction_factor': interaction_factor,
            'adaptive_equation': adaptive_equation,
            'balance_equation': balance_equation,
            'symbolic_harmony': 1.0 - balance_equation  # كلما قل عدم التوازن، زاد التناغم
        }

    def _calculate_symbolic_weight(self, symbol_analyses: List[Dict[str, Any]]) -> float:
        """حساب الوزن الرمزي الإجمالي."""

        if not symbol_analyses:
            return 0.0

        found_symbols = [s for s in symbol_analyses if s.get('found')]
        if not found_symbols:
            return 0.0

        total_weight = sum(s.get('symbol_strength', 0.0) for s in found_symbols)
        return total_weight / len(found_symbols)

    def _analyze_semantic_symbol_relations(self, semantic_analysis: Dict[str, Any],
                                         symbolic_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """تحليل العلاقات الدلالية مع الرموز."""

        relations = []

        # ربط الكائنات الدلالية بالرموز
        entities = semantic_analysis.get('entities', [])
        symbols = symbolic_analysis.get('symbol_analyses', [])

        for entity in entities:
            entity_word = entity.get('word', '').lower()
            for symbol in symbols:
                if symbol.get('found') and symbol['symbol'] == entity_word:
                    relations.append({
                        'type': 'entity_symbol_match',
                        'entity': entity_word,
                        'symbol': symbol['symbol'],
                        'semantic_meaning': entity.get('meaning', ''),
                        'symbolic_meaning': symbol.get('meaning', ''),
                        'relation_strength': 0.9
                    })

        # ربط الأفعال بالرموز
        actions = semantic_analysis.get('actions', [])
        for action in actions:
            action_word = action.get('word', '').lower()
            for symbol in symbols:
                if symbol.get('found'):
                    # حساب التشابه الدلالي
                    semantic_similarity = self._calculate_semantic_similarity(action_word, symbol['symbol'])
                    if semantic_similarity > 0.5:
                        relations.append({
                            'type': 'action_symbol_relation',
                            'action': action_word,
                            'symbol': symbol['symbol'],
                            'similarity': semantic_similarity,
                            'relation_strength': semantic_similarity
                        })

        return {
            'relations': relations,
            'relations_count': len(relations),
            'average_relation_strength': sum(r['relation_strength'] for r in relations) / max(1, len(relations))
        }

    def _build_dream_semantic_network(self, semantic_analysis: Dict[str, Any],
                                    semantic_symbol_relations: Dict[str, Any]) -> Dict[str, Any]:
        """بناء الشبكة الدلالية للحلم."""

        network = {
            'nodes': [],
            'edges': [],
            'clusters': {},
            'centrality_scores': {}
        }

        # إضافة العقد (الكائنات والرموز)
        entities = semantic_analysis.get('entities', [])
        for entity in entities:
            network['nodes'].append({
                'id': entity.get('word', ''),
                'type': 'entity',
                'properties': entity
            })

        # إضافة الروابط من العلاقات الدلالية الرمزية
        relations = semantic_symbol_relations.get('relations', [])
        for relation in relations:
            network['edges'].append({
                'source': relation.get('entity', relation.get('action', '')),
                'target': relation.get('symbol', ''),
                'weight': relation.get('relation_strength', 0.0),
                'type': relation.get('type', '')
            })

        # حساب درجات المركزية
        for node in network['nodes']:
            node_id = node['id']
            connections = len([edge for edge in network['edges']
                             if edge['source'] == node_id or edge['target'] == node_id])
            network['centrality_scores'][node_id] = connections

        return network

    def _analyze_emotional_context(self, dream_text: str, symbolic_analysis: Dict[str, Any],
                                 context: Dict[str, Any] = None) -> Dict[str, Any]:
        """تحليل السياق العاطفي."""

        # استخراج المشاعر من الرموز
        symbol_emotions = []
        for symbol in symbolic_analysis.get('symbol_analyses', []):
            if symbol.get('found'):
                emotion = symbol.get('emotional_impact', '')
                if emotion:
                    symbol_emotions.append(emotion)

        # تحليل الكلمات العاطفية في النص
        emotional_words = {
            'إيجابي': ['سعيد', 'فرح', 'حب', 'أمل', 'نور', 'جميل', 'رائع'],
            'سلبي': ['خوف', 'حزن', 'قلق', 'ألم', 'ظلام', 'مخيف', 'سيء'],
            'محايد': ['عادي', 'طبيعي', 'هادئ', 'ساكن', 'بسيط']
        }

        emotion_scores = {'إيجابي': 0, 'سلبي': 0, 'محايد': 0}

        for emotion_type, words in emotional_words.items():
            for word in words:
                if word in dream_text:
                    emotion_scores[emotion_type] += 1

        # تحديد النبرة العاطفية السائدة
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # حساب الشدة العاطفية
        total_emotions = sum(emotion_scores.values())
        emotional_intensity = baserah_sigmoid(
            total_emotions / 10.0, n=1, k=1.8, x0=0.0, alpha=1.0
        )

        return {
            'symbol_emotions': symbol_emotions,
            'emotion_scores': emotion_scores,
            'dominant_emotion': dominant_emotion,
            'emotional_intensity': emotional_intensity,
            'emotional_balance': self._calculate_emotional_balance(emotion_scores)
        }

    def _recognize_classic_patterns(self, dream_text: str) -> List[Dict[str, Any]]:
        """التعرف على الأنماط الكلاسيكية."""

        patterns = []

        for pattern in self.narrative_patterns['classic_patterns']:
            for keyword in pattern['keywords']:
                if keyword in dream_text.lower():
                    patterns.append({
                        'type': 'classic',
                        'name': pattern['name'],
                        'keyword': keyword,
                        'position': dream_text.lower().find(keyword),
                        'pattern_strength': 0.8
                    })
                    break

        return patterns

    def _recognize_innovative_patterns(self, dream_text: str) -> List[Dict[str, Any]]:
        """التعرف على الأنماط المبتكرة."""

        patterns = []

        for pattern in self.narrative_patterns['innovative_patterns']:
            for keyword in pattern['keywords']:
                if keyword in dream_text.lower():
                    patterns.append({
                        'type': 'innovative',
                        'name': pattern['name'],
                        'keyword': keyword,
                        'position': dream_text.lower().find(keyword),
                        'pattern_strength': 0.9  # الأنماط المبتكرة لها قوة أعلى
                    })
                    break

        return patterns

    def _discover_evolutionary_patterns(self, dream_text: str, symbolic_analysis: Dict[str, Any],
                                      semantic_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """اكتشاف أنماط جديدة بالذكاء التطوري."""

        evolutionary_patterns = []

        # تحليل تسلسل الأحداث
        sentences = dream_text.split('.')
        if len(sentences) > 2:
            # نمط التطور السردي
            evolutionary_patterns.append({
                'type': 'evolutionary',
                'name': 'التطور السردي',
                'description': f'تطور الحلم عبر {len(sentences)} مراحل',
                'pattern_strength': len(sentences) / 10.0,
                'discovery_method': 'sequence_analysis'
            })

        # تحليل كثافة الرموز
        symbols_count = len(symbolic_analysis.get('symbol_analyses', []))
        if symbols_count > 3:
            evolutionary_patterns.append({
                'type': 'evolutionary',
                'name': 'الكثافة الرمزية',
                'description': f'حلم غني بالرموز ({symbols_count} رموز)',
                'pattern_strength': min(1.0, symbols_count / 5.0),
                'discovery_method': 'symbol_density_analysis'
            })

        # تحليل التعقيد الدلالي
        semantic_completeness = semantic_analysis.get('semantic_completeness', 0.0)
        if semantic_completeness > 0.7:
            evolutionary_patterns.append({
                'type': 'evolutionary',
                'name': 'التعقيد الدلالي',
                'description': 'حلم معقد دلالياً',
                'pattern_strength': semantic_completeness,
                'discovery_method': 'semantic_complexity_analysis'
            })

        return evolutionary_patterns

    def _calculate_context_relevance(self, symbol: str, context: Dict[str, Any] = None) -> float:
        """حساب صلة الرمز بالسياق."""

        if not context:
            return 0.5  # قيمة افتراضية

        relevance_factors = []

        # عامل العمر
        age = context.get('age', 0)
        if age > 0:
            # رموز مختلفة لأعمار مختلفة
            if symbol in ['مدرسة', 'كتاب'] and 5 <= age <= 25:
                relevance_factors.append(0.9)
            elif symbol in ['عمل', 'سيارة'] and 20 <= age <= 65:
                relevance_factors.append(0.8)
            elif symbol in ['بيت', 'عائلة'] and age >= 25:
                relevance_factors.append(0.7)
            else:
                relevance_factors.append(0.5)

        # عامل الحالة النفسية
        mood = context.get('mood', '')
        if mood:
            if mood == 'قلق' and symbol in ['مطاردة', 'هروب']:
                relevance_factors.append(0.9)
            elif mood == 'سعيد' and symbol in ['طيران', 'نور']:
                relevance_factors.append(0.8)
            else:
                relevance_factors.append(0.6)

        return sum(relevance_factors) / max(1, len(relevance_factors))

    def get_engine_statistics(self) -> Dict[str, Any]:
        """الحصول على إحصائيات المحرك."""

        return {
            'engine_info': {
                'name': self.system_name,
                'type': 'dream_interpretation_engine',
                'creation_time': getattr(self, 'creation_time', datetime.now())
            },
            'interpretation_stats': {
                'dreams_interpreted': self.engine_stats['dreams_interpreted'],
                'symbols_analyzed': self.engine_stats['symbols_analyzed'],
                'patterns_discovered': self.engine_stats['patterns_discovered'],
                'accuracy_score': self.engine_stats['accuracy_score']
            },
            'database_stats': {
                'total_symbols': sum(len(category) for category in self.symbol_database.values()),
                'symbol_categories': len(self.symbol_database),
                'classic_patterns': len(self.narrative_patterns['classic_patterns']),
                'innovative_patterns': len(self.narrative_patterns['innovative_patterns'])
            },
            'network_stats': {
                'dream_nodes': len(self.dream_semantic_network['dream_nodes']),
                'symbol_connections': len(self.dream_semantic_network['symbol_connections']),
                'pattern_clusters': len(self.dream_semantic_network['pattern_clusters'])
            },
            'performance_assessment': 'excellent' if self.engine_stats['accuracy_score'] > 0.8 else 'good' if self.engine_stats['accuracy_score'] > 0.6 else 'developing'
        }

    def _calculate_interaction_strength(self, symbol1: Dict[str, Any], symbol2: Dict[str, Any]) -> float:
        """حساب قوة التفاعل بين رمزين."""

        # التفاعل بناءً على الفئة
        if symbol1.get('category') == symbol2.get('category'):
            category_bonus = 0.3
        else:
            category_bonus = 0.0

        # التفاعل بناءً على الارتباطات
        associations1 = set(symbol1.get('associations', []))
        associations2 = set(symbol2.get('associations', []))
        common_associations = len(associations1.intersection(associations2))
        association_factor = common_associations / max(1, len(associations1.union(associations2)))

        # التفاعل بناءً على التأثير العاطفي
        emotion1 = symbol1.get('emotional_impact', '')
        emotion2 = symbol2.get('emotional_impact', '')
        emotion_factor = 0.2 if emotion1 == emotion2 else 0.0

        total_strength = category_bonus + association_factor + emotion_factor
        return min(1.0, total_strength)

    def _determine_interaction_type(self, symbol1: Dict[str, Any], symbol2: Dict[str, Any]) -> str:
        """تحديد نوع التفاعل بين رمزين."""

        category1 = symbol1.get('category', '')
        category2 = symbol2.get('category', '')

        if category1 == category2:
            return 'same_category_interaction'
        elif category1 == 'animals' and category2 == 'nature':
            return 'animal_nature_interaction'
        elif category1 == 'objects' and category2 == 'nature':
            return 'object_nature_interaction'
        else:
            return 'cross_category_interaction'

    def _generate_combined_meaning(self, symbol1: Dict[str, Any], symbol2: Dict[str, Any]) -> str:
        """توليد معنى مركب من رمزين."""

        meaning1 = symbol1.get('meaning', '')
        meaning2 = symbol2.get('meaning', '')

        if meaning1 and meaning2:
            return f"تفاعل {meaning1} مع {meaning2}"
        else:
            return "تفاعل رمزي معقد"

    def _calculate_semantic_similarity(self, word1: str, word2: str) -> float:
        """حساب التشابه الدلالي بين كلمتين."""

        # تشابه بسيط بناءً على الحروف المشتركة
        set1 = set(word1)
        set2 = set(word2)
        common_chars = len(set1.intersection(set2))
        total_chars = len(set1.union(set2))

        if total_chars == 0:
            return 0.0

        char_similarity = common_chars / total_chars

        # تطبيق التحويل الثوري
        return baserah_sigmoid(char_similarity * 2, n=1, k=1.5, x0=0.0, alpha=1.0)

    def _calculate_emotional_balance(self, emotion_scores: Dict[str, int]) -> float:
        """حساب التوازن العاطفي."""

        total = sum(emotion_scores.values())
        if total == 0:
            return 0.5  # توازن محايد

        # حساب الانحراف عن التوازن المثالي
        ideal_balance = total / 3  # توزيع متساوي
        deviations = [abs(score - ideal_balance) for score in emotion_scores.values()]
        average_deviation = sum(deviations) / len(deviations)

        # تحويل إلى درجة توازن (كلما قل الانحراف، زاد التوازن)
        balance_score = 1.0 - (average_deviation / total)
        return max(0.0, min(1.0, balance_score))

    def _analyze_temporal_spatial_patterns(self, dream_text: str) -> Dict[str, Any]:
        """تحليل الأنماط الزمنية والمكانية."""

        # كلمات زمنية
        temporal_words = ['صباح', 'مساء', 'ليل', 'نهار', 'أمس', 'غداً', 'الآن', 'قديماً', 'حديثاً']
        # كلمات مكانية
        spatial_words = ['فوق', 'تحت', 'يمين', 'يسار', 'أمام', 'خلف', 'داخل', 'خارج', 'بعيد', 'قريب']

        temporal_patterns = []
        spatial_patterns = []

        for word in temporal_words:
            if word in dream_text:
                temporal_patterns.append({
                    'word': word,
                    'position': dream_text.find(word),
                    'type': 'temporal'
                })

        for word in spatial_words:
            if word in dream_text:
                spatial_patterns.append({
                    'word': word,
                    'position': dream_text.find(word),
                    'type': 'spatial'
                })

        return {
            'temporal_patterns': temporal_patterns,
            'spatial_patterns': spatial_patterns,
            'temporal_density': len(temporal_patterns),
            'spatial_density': len(spatial_patterns)
        }

    def _calculate_pattern_strengths(self, classic_patterns: List[Dict[str, Any]],
                                   innovative_patterns: List[Dict[str, Any]],
                                   evolutionary_patterns: List[Dict[str, Any]]) -> Dict[str, float]:
        """حساب قوة الأنماط."""

        classic_strength = sum(p.get('pattern_strength', 0.0) for p in classic_patterns)
        innovative_strength = sum(p.get('pattern_strength', 0.0) for p in innovative_patterns)
        evolutionary_strength = sum(p.get('pattern_strength', 0.0) for p in evolutionary_patterns)

        total_strength = classic_strength + innovative_strength + evolutionary_strength

        if total_strength == 0:
            return {'classic': 0.0, 'innovative': 0.0, 'evolutionary': 0.0}

        return {
            'classic': classic_strength / total_strength,
            'innovative': innovative_strength / total_strength,
            'evolutionary': evolutionary_strength / total_strength
        }

    def _identify_dominant_pattern(self, pattern_strengths: Dict[str, float]) -> str:
        """تحديد النمط المهيمن."""

        if not pattern_strengths:
            return 'none'

        return max(pattern_strengths, key=pattern_strengths.get)

    def _explore_evolutionary_insights(self, dream_text: str, symbolic_analysis: Dict[str, Any],
                                     semantic_analysis: Dict[str, Any], pattern_analysis: Dict[str, Any],
                                     context: Dict[str, Any] = None) -> Dict[str, Any]:
        """استكشاف الرؤى التطورية."""

        insights = []

        # رؤية التطور الرمزي
        symbol_evolution = self._analyze_symbol_evolution(symbolic_analysis)
        if symbol_evolution['evolution_detected']:
            insights.append({
                'type': 'symbol_evolution',
                'insight': symbol_evolution['insight'],
                'confidence': symbol_evolution['confidence']
            })

        # رؤية التطور الدلالي
        semantic_evolution = self._analyze_semantic_evolution(semantic_analysis)
        if semantic_evolution['evolution_detected']:
            insights.append({
                'type': 'semantic_evolution',
                'insight': semantic_evolution['insight'],
                'confidence': semantic_evolution['confidence']
            })

        # رؤية التطور النمطي
        pattern_evolution = self._analyze_pattern_evolution(pattern_analysis)
        if pattern_evolution['evolution_detected']:
            insights.append({
                'type': 'pattern_evolution',
                'insight': pattern_evolution['insight'],
                'confidence': pattern_evolution['confidence']
            })

        return {
            'insights': insights,
            'insights_count': len(insights),
            'evolutionary_score': sum(insight['confidence'] for insight in insights) / max(1, len(insights))
        }

    def _integrate_revolutionary_interpretation(self, comprehensive_interpretation: Dict[str, Any]) -> Dict[str, Any]:
        """التكامل الثوري للتفسير."""

        # استخراج العناصر الرئيسية
        symbolic_weight = comprehensive_interpretation['symbolic_analysis'].get('symbolic_weight', 0.0)
        semantic_completeness = comprehensive_interpretation['semantic_analysis'].get('semantic_completeness', 0.0)
        dominant_pattern = comprehensive_interpretation['pattern_analysis'].get('dominant_pattern', 'none')
        evolutionary_score = comprehensive_interpretation['evolutionary_insights'].get('evolutionary_score', 0.0)

        # حساب التكامل الثوري
        integration_factors = [symbolic_weight, semantic_completeness, evolutionary_score]
        integration_score = sum(integration_factors) / len(integration_factors)

        # تطبيق التحويل الثوري النهائي
        revolutionary_integration = baserah_sigmoid(
            integration_score * 1.5, n=1, k=2.5, x0=0.0, alpha=1.3
        )

        # توليد التفسير المتكامل
        integrated_meaning = self._generate_integrated_meaning(comprehensive_interpretation)

        return {
            'integration_score': integration_score,
            'revolutionary_integration': revolutionary_integration,
            'integrated_meaning': integrated_meaning,
            'dominant_pattern': dominant_pattern,
            'interpretation_quality': 'excellent' if revolutionary_integration > 0.8 else 'good' if revolutionary_integration > 0.6 else 'developing'
        }

    def _generate_dream_recommendations(self, comprehensive_interpretation: Dict[str, Any]) -> List[Dict[str, str]]:
        """توليد توصيات للحلم."""

        recommendations = []

        # توصيات بناءً على الرموز
        symbolic_analysis = comprehensive_interpretation.get('symbolic_analysis', {})
        for symbol in symbolic_analysis.get('symbol_analyses', []):
            if symbol.get('found') and symbol.get('symbol_strength', 0.0) > 0.7:
                recommendations.append({
                    'type': 'symbol',
                    'recommendation': f"تأمل في معنى رمز '{symbol['symbol']}' وعلاقته بحياتك الحالية"
                })

        # توصيات بناءً على الأنماط
        pattern_analysis = comprehensive_interpretation.get('pattern_analysis', {})
        dominant_pattern = pattern_analysis.get('dominant_pattern', '')
        if dominant_pattern != 'none':
            recommendations.append({
                'type': 'pattern',
                'recommendation': f"انتبه لنمط '{dominant_pattern}' في حياتك وكيف يؤثر على قراراتك"
            })

        # توصيات بناءً على السياق العاطفي
        emotional_context = comprehensive_interpretation.get('semantic_analysis', {}).get('emotional_context', {})
        dominant_emotion = emotional_context.get('dominant_emotion', '')
        if dominant_emotion:
            recommendations.append({
                'type': 'emotion',
                'recommendation': f"اهتم بحالتك العاطفية '{dominant_emotion}' وتأثيرها على أحلامك"
            })

        return recommendations[:5]  # أهم 5 توصيات

    def _calculate_interpretation_confidence(self, comprehensive_interpretation: Dict[str, Any]) -> float:
        """حساب درجة الثقة في التفسير."""

        confidence_factors = []

        # ثقة التحليل الرمزي
        symbolic_weight = comprehensive_interpretation.get('symbolic_analysis', {}).get('symbolic_weight', 0.0)
        confidence_factors.append(symbolic_weight)

        # ثقة التحليل الدلالي
        semantic_completeness = comprehensive_interpretation.get('semantic_analysis', {}).get('semantic_completeness', 0.0)
        confidence_factors.append(semantic_completeness)

        # ثقة تحليل الأنماط
        pattern_strengths = comprehensive_interpretation.get('pattern_analysis', {}).get('pattern_strengths', {})
        if pattern_strengths:
            max_pattern_strength = max(pattern_strengths.values())
            confidence_factors.append(max_pattern_strength)

        # ثقة الرؤى التطورية
        evolutionary_score = comprehensive_interpretation.get('evolutionary_insights', {}).get('evolutionary_score', 0.0)
        confidence_factors.append(evolutionary_score)

        # حساب الثقة الإجمالية
        overall_confidence = sum(confidence_factors) / max(1, len(confidence_factors))

        # تطبيق التحويل الثوري
        return baserah_sigmoid(overall_confidence * 1.2, n=1, k=2.0, x0=0.0, alpha=1.1)

    def _update_interpretation_statistics(self, comprehensive_interpretation: Dict[str, Any]):
        """تحديث إحصائيات التفسير."""

        self.engine_stats['dreams_interpreted'] += 1

        # عدد الرموز المحللة
        symbols_count = len(comprehensive_interpretation.get('symbolic_analysis', {}).get('symbol_analyses', []))
        self.engine_stats['symbols_analyzed'] += symbols_count

        # عدد الأنماط المكتشفة
        patterns_count = (
            len(comprehensive_interpretation.get('pattern_analysis', {}).get('classic_patterns', [])) +
            len(comprehensive_interpretation.get('pattern_analysis', {}).get('innovative_patterns', [])) +
            len(comprehensive_interpretation.get('pattern_analysis', {}).get('evolutionary_patterns', []))
        )
        self.engine_stats['patterns_discovered'] += patterns_count

        # تحديث درجة الدقة
        confidence = comprehensive_interpretation.get('confidence_score', 0.0)
        current_accuracy = self.engine_stats['accuracy_score']
        dreams_count = self.engine_stats['dreams_interpreted']

        # متوسط متحرك للدقة
        self.engine_stats['accuracy_score'] = (current_accuracy * (dreams_count - 1) + confidence) / dreams_count

    def _add_to_dream_network(self, comprehensive_interpretation: Dict[str, Any]):
        """إضافة التفسير إلى شبكة الأحلام."""

        dream_id = f"dream_{uuid.uuid4()}"

        # إضافة عقدة الحلم
        self.dream_semantic_network['dream_nodes'][dream_id] = {
            'dream_text': comprehensive_interpretation['dream_text'],
            'interpretation_summary': comprehensive_interpretation.get('integrated_interpretation', {}).get('integrated_meaning', ''),
            'confidence_score': comprehensive_interpretation.get('confidence_score', 0.0),
            'timestamp': datetime.now()
        }

        # إضافة روابط الرموز
        symbols = comprehensive_interpretation.get('symbolic_analysis', {}).get('symbol_analyses', [])
        for symbol in symbols:
            if symbol.get('found'):
                symbol_name = symbol['symbol']
                if symbol_name not in self.dream_semantic_network['symbol_connections']:
                    self.dream_semantic_network['symbol_connections'][symbol_name] = []

                self.dream_semantic_network['symbol_connections'][symbol_name].append({
                    'dream_id': dream_id,
                    'symbol_strength': symbol.get('symbol_strength', 0.0)
                })

        # إضافة إلى تاريخ التفسيرات
        self.dream_semantic_network['interpretation_history'].append({
            'dream_id': dream_id,
            'timestamp': datetime.now(),
            'confidence': comprehensive_interpretation.get('confidence_score', 0.0)
        })
