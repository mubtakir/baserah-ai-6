#!/usr/bin/env python3
# api_interface.py - واجهة API REST للنظام الثوري Baserah

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
from datetime import datetime
import numpy as np
import uuid

# إضافة المسار للاستيراد
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from revolutionary_intelligence.revolutionary_mother_system.revolutionary_mother_system import BaserahRevolutionaryMotherSystem, InheritanceType
from revolutionary_intelligence.adaptive_equations_system.self_evolving_system import BaserahSelfEvolvingSystem, EvolutionDirection
from advanced_cognitive_objects import BaserahAdvancedCognitiveObject, AdvancedCognitiveType
from knowledge_systems.semantic_meaning.semantic_meaning_system import BaserahSemanticMeaningSystem
from artistic_unit.integrated_system import BaserahIntegratedSystem
from revolutionary_intelligence.quranic_analysis_engine import QuranicAnalysisEngine
from revolutionary_intelligence.arabic_lexicon_engine import ArabicLexiconEngine
from revolutionary_intelligent_agent.intelligent_agent import BaserahIntelligentAgent

class BaserahAPIInterface:
    """
    واجهة API REST للنظام الثوري Baserah
    
    توفر API كامل للوصول إلى جميع مكونات النظام:
    - النظام الأم الثوري
    - التطوير التلقائي
    - الكائنات المعرفية المتقدمة
    - نظام الدلالة المعنوية
    - الوحدة الفنية
    """
    
    def __init__(self):
        """تهيئة واجهة API."""
        
        self.app = Flask(__name__)
        CORS(self.app)  # تمكين CORS للوصول من المتصفحات
        
        # تهيئة النظام الثوري
        self.initialize_revolutionary_system()
        
        # إعداد المسارات
        self.setup_api_routes()
        
        # سجل العمليات
        self.operation_log = []
        
        print("🌐 تم تهيئة واجهة API للنظام الثوري")
    
    def initialize_revolutionary_system(self):
        """تهيئة النظام الثوري الكامل."""
        
        try:
            # النظام الأم
            self.mother_system = BaserahRevolutionaryMotherSystem()
            
            # نظام التطوير التلقائي
            self.self_evolving = BaserahSelfEvolvingSystem(self.mother_system)
            
            # نظام الدلالة المعنوية
            self.semantic_system = BaserahSemanticMeaningSystem(self.mother_system)
            
            # الوحدة الفنية
            self.artistic_unit = BaserahIntegratedSystem()
            
            # وراثة الوحدة الفنية من النظام الأم
            self.mother_system.inherit_to_unit(InheritanceType.ARTISTIC_UNIT, self.artistic_unit)
            
            # كائن معرفي متقدم
            self.consciousness = BaserahAdvancedCognitiveObject("الوعي API",
                                                              AdvancedCognitiveType.CONSCIOUSNESS_SIMULATOR)

            # محرك التحليل القرآني
            self.quranic_engine = QuranicAnalysisEngine("APIQuranicEngine")

            # محرك المعجم العربي
            self.lexicon_engine = ArabicLexiconEngine("APILexiconEngine")

            # الوكيل الذكي الثوري
            self.intelligent_agent = BaserahIntelligentAgent("APIIntelligentAgent")
            
            self.system_ready = True
            print("✅ تم تهيئة النظام الثوري للAPI بنجاح")
            
        except Exception as e:
            self.system_ready = False
            print(f"❌ فشل في تهيئة النظام الثوري: {e}")
    
    def log_operation(self, operation, details=None):
        """تسجيل عملية في السجل."""
        log_entry = {
            'id': str(uuid.uuid4()),
            'timestamp': datetime.now().isoformat(),
            'operation': operation,
            'details': details or {}
        }
        self.operation_log.append(log_entry)
        
        # الاحتفاظ بآخر 1000 عملية فقط
        if len(self.operation_log) > 1000:
            self.operation_log = self.operation_log[-1000:]
    
    def create_response(self, success=True, data=None, message=None, error=None):
        """إنشاء استجابة موحدة."""
        response = {
            'success': success,
            'timestamp': datetime.now().isoformat(),
            'system_ready': self.system_ready
        }
        
        if success:
            response['data'] = data or {}
            if message:
                response['message'] = message
        else:
            response['error'] = error or 'خطأ غير محدد'
            if message:
                response['message'] = message
        
        return jsonify(response)
    
    def setup_api_routes(self):
        """إعداد مسارات API."""
        
        # معلومات API
        @self.app.route('/api/info', methods=['GET'])
        def api_info():
            """معلومات API."""
            return self.create_response(data={
                'name': 'Baserah Revolutionary System API',
                'version': '1.0.0',
                'description': 'واجهة API للنظام الثوري Baserah',
                'endpoints': {
                    'system': '/api/system/*',
                    'evolution': '/api/evolution/*',
                    'semantic': '/api/semantic/*',
                    'cognitive': '/api/cognitive/*',
                    'artistic': '/api/artistic/*',
                    'quran': '/api/quran/*',
                    'lexicon': '/api/lexicon/*',
                    'agent': '/api/agent/*',
                    'logs': '/api/logs'
                }
            })
        
        # حالة النظام
        @self.app.route('/api/system/status', methods=['GET'])
        def system_status():
            """حالة النظام الكاملة."""
            if not self.system_ready:
                return self.create_response(False, error='النظام غير جاهز')
            
            try:
                summary = self.mother_system.get_system_summary()
                health_status = self.self_evolving.analyze_system_health()
                metrics = self.self_evolving.current_metrics
                semantic_summary = self.semantic_system.get_semantic_summary()
                cognitive_summary = self.consciousness.get_cognitive_summary()
                
                data = {
                    'mother_system': {
                        'system_id': summary['system_id'],
                        'total_inheritances': summary['total_inheritances'],
                        'total_adaptations': summary['total_adaptations'],
                        'evolution_count': summary['system_evolution_count'],
                        'inherited_units': summary['inherited_unit_types'],
                        'baserah_purity': summary['baserah_purity']
                    },
                    'evolution_system': {
                        'health_status': health_status.value,
                        'performance_score': metrics.performance_score,
                        'adaptation_efficiency': metrics.adaptation_efficiency,
                        'revolutionary_potential': metrics.revolutionary_potential,
                        'system_complexity': metrics.system_complexity,
                        'inheritance_success_rate': metrics.inheritance_success_rate
                    },
                    'semantic_system': {
                        'total_equations': semantic_summary['total_semantic_equations'],
                        'total_interpretations': semantic_summary['total_interpretations'],
                        'type_distribution': semantic_summary['type_distribution'],
                        'dimension_usage': semantic_summary['dimension_usage']
                    },
                    'cognitive_system': {
                        'consciousness_level': cognitive_summary['consciousness_level'],
                        'creativity_index': cognitive_summary['creativity_index'],
                        'learning_efficiency': cognitive_summary['learning_efficiency'],
                        'total_activities': cognitive_summary['total_activities']
                    }
                }
                
                self.log_operation('system_status_check')
                return self.create_response(data=data)
                
            except Exception as e:
                return self.create_response(False, error=str(e))
        
        # تحليل التطوير
        @self.app.route('/api/evolution/analyze', methods=['POST'])
        def evolution_analyze():
            """تحليل صحة النظام للتطوير."""
            if not self.system_ready:
                return self.create_response(False, error='النظام غير جاهز')
            
            try:
                health_status = self.self_evolving.analyze_system_health()
                decision = self.self_evolving.make_evolution_decision(health_status)
                
                data = {
                    'health_status': health_status.value,
                    'should_evolve': decision['should_evolve'],
                    'evolution_direction': decision.get('evolution_direction', {}).value if decision.get('evolution_direction') else None,
                    'safety_checks_passed': decision['safety_checks_passed'],
                    'reasoning': decision['reasoning']
                }
                
                self.log_operation('evolution_analyze', data)
                return self.create_response(data=data)
                
            except Exception as e:
                return self.create_response(False, error=str(e))
        
        # تنفيذ التطوير
        @self.app.route('/api/evolution/execute', methods=['POST'])
        def evolution_execute():
            """تنفيذ التطوير التلقائي."""
            if not self.system_ready:
                return self.create_response(False, error='النظام غير جاهز')
            
            try:
                health_status = self.self_evolving.analyze_system_health()
                decision = self.self_evolving.make_evolution_decision(health_status)
                
                if decision['should_evolve'] and decision['safety_checks_passed']:
                    evolution_result = self.self_evolving.execute_evolution(decision['evolution_direction'])
                    
                    data = {
                        'evolution_executed': True,
                        'success': evolution_result['success'],
                        'changes_count': len(evolution_result['changes_made']),
                        'new_capabilities_count': len(evolution_result['new_capabilities']),
                        'performance_improvement': evolution_result['performance_improvement'],
                        'changes_made': evolution_result['changes_made'][:10],  # أول 10 تغييرات
                        'new_capabilities': evolution_result['new_capabilities'][:5]  # أول 5 قدرات
                    }
                else:
                    data = {
                        'evolution_executed': False,
                        'reason': 'لم تتحقق شروط التطوير',
                        'should_evolve': decision['should_evolve'],
                        'safety_checks_passed': decision['safety_checks_passed']
                    }
                
                self.log_operation('evolution_execute', data)
                return self.create_response(data=data)
                
            except Exception as e:
                return self.create_response(False, error=str(e))
        
        # التطوير المستمر
        @self.app.route('/api/evolution/continuous', methods=['POST'])
        def evolution_continuous():
            """تشغيل التطوير المستمر."""
            if not self.system_ready:
                return self.create_response(False, error='النظام غير جاهز')
            
            try:
                request_data = request.get_json() or {}
                max_cycles = request_data.get('max_cycles', 5)
                
                continuous_result = self.self_evolving.run_continuous_evolution(max_cycles=max_cycles)
                
                data = {
                    'total_cycles': continuous_result['total_cycles'],
                    'successful_evolutions': continuous_result['successful_evolutions'],
                    'revolutionary_breakthroughs': continuous_result['revolutionary_breakthroughs'],
                    'success_rate': continuous_result['successful_evolutions'] / continuous_result['total_cycles'] * 100,
                    'final_performance': continuous_result['final_metrics'].performance_score
                }
                
                self.log_operation('evolution_continuous', data)
                return self.create_response(data=data)
                
            except Exception as e:
                return self.create_response(False, error=str(e))
        
        # تفسير دلالي
        @self.app.route('/api/semantic/interpret', methods=['POST'])
        def semantic_interpret():
            """تفسير جملة دلالية."""
            if not self.system_ready:
                return self.create_response(False, error='النظام غير جاهز')
            
            try:
                request_data = request.get_json()
                if not request_data or 'sentence' not in request_data:
                    return self.create_response(False, error='يرجى تحديد الجملة في حقل sentence')
                
                sentence = request_data['sentence'].strip()
                if not sentence:
                    return self.create_response(False, error='الجملة فارغة')
                
                interpretation = self.semantic_system.interpret_semantic_sentence(sentence)
                
                data = {
                    'sentence': sentence,
                    'confidence': interpretation['confidence'],
                    'recognized_words': interpretation['recognized_words'],
                    'execution_plan_steps': len(interpretation['execution_plan']),
                    'mathematical_components': len(interpretation.get('mathematical_representation', [])),
                    'semantic_components': len(interpretation.get('semantic_representation', [])),
                    'interpretation_id': interpretation['interpretation_id']
                }
                
                self.log_operation('semantic_interpret', {'sentence': sentence, 'confidence': interpretation['confidence']})
                return self.create_response(data=data)
                
            except Exception as e:
                return self.create_response(False, error=str(e))
        
        # تنفيذ دلالي
        @self.app.route('/api/semantic/execute', methods=['POST'])
        def semantic_execute():
            """تنفيذ أمر دلالي."""
            if not self.system_ready:
                return self.create_response(False, error='النظام غير جاهز')
            
            try:
                request_data = request.get_json()
                if not request_data or 'command' not in request_data:
                    return self.create_response(False, error='يرجى تحديد الأمر في حقل command')
                
                command = request_data['command'].strip()
                if not command:
                    return self.create_response(False, error='الأمر فارغ')
                
                execution_result = self.semantic_system.execute_semantic_command(command)
                
                data = {
                    'command': command,
                    'execution_success': execution_result['execution_success'],
                    'confidence': execution_result['interpretation']['confidence'],
                    'visual_objects_count': len(execution_result.get('visual_output', [])),
                    'mathematical_results_count': len(execution_result.get('mathematical_result', {})),
                    'fusion_score': execution_result.get('semantic_analysis', {}).get('fusion_score', 0)
                }
                
                self.log_operation('semantic_execute', {'command': command, 'success': execution_result['execution_success']})
                return self.create_response(data=data)
                
            except Exception as e:
                return self.create_response(False, error=str(e))
        
        # التحويل الدلالي
        @self.app.route('/api/semantic/transform', methods=['POST'])
        def semantic_transform():
            """تحويل دلالي بين كلمتين."""
            if not self.system_ready:
                return self.create_response(False, error='النظام غير جاهز')
            
            try:
                request_data = request.get_json()
                if not request_data or 'source' not in request_data or 'target' not in request_data:
                    return self.create_response(False, error='يرجى تحديد source و target')
                
                source = request_data['source'].strip()
                target = request_data['target'].strip()
                
                if not source or not target:
                    return self.create_response(False, error='كلمتا المصدر والهدف مطلوبتان')
                
                transformation = self.semantic_system.create_semantic_transformation(source, target)
                
                if 'error' in transformation:
                    return self.create_response(False, error=transformation['error'])
                
                data = {
                    'source': source,
                    'target': target,
                    'transformation_score': transformation['transformation_score'],
                    'mathematical_steps': len(transformation['mathematical_steps']),
                    'semantic_changes': len(transformation['semantic_changes']),
                    'transformation_id': transformation['transformation_id']
                }
                
                self.log_operation('semantic_transform', {'source': source, 'target': target, 'score': transformation['transformation_score']})
                return self.create_response(data=data)
                
            except Exception as e:
                return self.create_response(False, error=str(e))
        
        # قاعدة البيانات الدلالية
        @self.app.route('/api/semantic/database', methods=['GET'])
        def semantic_database():
            """عرض قاعدة البيانات الدلالية."""
            if not self.system_ready:
                return self.create_response(False, error='النظام غير جاهز')
            
            try:
                summary = self.semantic_system.get_semantic_summary()
                
                # قائمة الكلمات مع تفاصيلها
                words_details = []
                for word, equation in self.semantic_system.semantic_database.items():
                    words_details.append({
                        'word': word,
                        'type': equation.semantic_type.value,
                        'mathematical_components': len(equation.mathematical_components),
                        'semantic_components': len(equation.semantic_components),
                        'equation_id': equation.equation_id
                    })
                
                data = {
                    'total_equations': summary['total_semantic_equations'],
                    'type_distribution': summary['type_distribution'],
                    'dimension_usage': summary['dimension_usage'],
                    'words': words_details,
                    'symbol_registry': summary['symbol_registry']
                }
                
                self.log_operation('semantic_database_view')
                return self.create_response(data=data)
                
            except Exception as e:
                return self.create_response(False, error=str(e))
        
        # سجل العمليات
        @self.app.route('/api/logs', methods=['GET'])
        def get_logs():
            """الحصول على سجل العمليات."""
            try:
                # معاملات الاستعلام
                limit = request.args.get('limit', 50, type=int)
                operation_filter = request.args.get('operation', None)
                
                # تصفية السجل
                filtered_logs = self.operation_log
                if operation_filter:
                    filtered_logs = [log for log in self.operation_log if operation_filter in log['operation']]
                
                # تحديد العدد
                recent_logs = filtered_logs[-limit:] if limit > 0 else filtered_logs
                
                data = {
                    'total_logs': len(self.operation_log),
                    'filtered_logs': len(filtered_logs),
                    'returned_logs': len(recent_logs),
                    'logs': recent_logs
                }
                
                return self.create_response(data=data)
                
            except Exception as e:
                return self.create_response(False, error=str(e))
        
        # مسح السجل
        @self.app.route('/api/logs/clear', methods=['DELETE'])
        def clear_logs():
            """مسح سجل العمليات."""
            try:
                logs_count = len(self.operation_log)
                self.operation_log.clear()
                
                data = {
                    'cleared_logs': logs_count,
                    'message': f'تم مسح {logs_count} عملية من السجل'
                }
                
                return self.create_response(data=data)
                
            except Exception as e:
                return self.create_response(False, error=str(e))

        # تحليل آية قرآنية
        @self.app.route('/api/quran/analyze_verse', methods=['POST'])
        def quran_analyze_verse():
            """تحليل آية قرآنية."""
            if not self.system_ready:
                return self.create_response(False, error='النظام غير جاهز')

            try:
                request_data = request.get_json()
                if not request_data or 'surah_number' not in request_data or 'verse_number' not in request_data:
                    return self.create_response(False, error='يرجى تحديد surah_number و verse_number')

                surah_number = int(request_data['surah_number'])
                verse_number = int(request_data['verse_number'])
                deep_analysis = request_data.get('deep_analysis', True)

                analysis = self.quranic_engine.analyze_verse_revolutionary(
                    surah_number, verse_number, deep_analysis=deep_analysis
                )

                data = {
                    'verse_reference': f"{surah_number}:{verse_number}",
                    'verse_text': analysis.text,
                    'semantic_weight': analysis.semantic_weight,
                    'word_count': len(analysis.word_analysis),
                    'revolutionary_insights': analysis.revolutionary_insights,
                    'divine_patterns': analysis.divine_patterns,
                    'numerical_miracles_count': len(analysis.numerical_miracle),
                    'baserah_analysis': analysis.baserah_analysis,
                    'analysis_id': analysis.analysis_id
                }

                self.log_operation('quran_analyze_verse', {'reference': f"{surah_number}:{verse_number}", 'semantic_weight': analysis.semantic_weight})
                return self.create_response(data=data)

            except Exception as e:
                return self.create_response(False, error=str(e))

        # البحث في القرآن
        @self.app.route('/api/quran/search', methods=['POST'])
        def quran_search():
            """البحث في القرآن الكريم."""
            if not self.system_ready:
                return self.create_response(False, error='النظام غير جاهز')

            try:
                request_data = request.get_json()
                if not request_data or 'search_term' not in request_data:
                    return self.create_response(False, error='يرجى تحديد search_term')

                search_term = request_data['search_term'].strip()
                search_type = request_data.get('search_type', 'word')

                if not search_term:
                    return self.create_response(False, error='مصطلح البحث فارغ')

                search_result = self.quranic_engine.search_quranic_text(search_term, search_type)

                data = {
                    'search_term': search_term,
                    'search_type': search_type,
                    'total_matches': search_result['total_matches'],
                    'surahs_found': len(search_result['surahs_found']),
                    'matches': search_result['matches'][:20],  # أول 20 نتيجة
                    'search_statistics': search_result['search_statistics']
                }

                self.log_operation('quran_search', {'term': search_term, 'matches': search_result['total_matches']})
                return self.create_response(data=data)

            except Exception as e:
                return self.create_response(False, error=str(e))

        # تحليل كلمة عربية
        @self.app.route('/api/lexicon/analyze_word', methods=['POST'])
        def lexicon_analyze_word():
            """تحليل كلمة عربية."""
            if not self.system_ready:
                return self.create_response(False, error='النظام غير جاهز')

            try:
                request_data = request.get_json()
                if not request_data or 'word' not in request_data:
                    return self.create_response(False, error='يرجى تحديد word')

                word = request_data['word'].strip()
                deep_analysis = request_data.get('deep_analysis', True)

                if not word:
                    return self.create_response(False, error='الكلمة فارغة')

                analysis = self.lexicon_engine.analyze_word_revolutionary(word, deep_analysis=deep_analysis)

                data = {
                    'word': analysis.word,
                    'root': analysis.root,
                    'meaning': analysis.meaning,
                    'morphological_weight': analysis.morphological_weight,
                    'semantic_weight': analysis.semantic_weight,
                    'revolutionary_insights': analysis.revolutionary_insights,
                    'morphological_analysis': analysis.morphological_analysis,
                    'baserah_analysis': analysis.baserah_analysis,
                    'analysis_id': analysis.analysis_id
                }

                self.log_operation('lexicon_analyze_word', {'word': word, 'root': analysis.root})
                return self.create_response(data=data)

            except Exception as e:
                return self.create_response(False, error=str(e))

        # البحث بالجذر
        @self.app.route('/api/lexicon/search_root', methods=['POST'])
        def lexicon_search_root():
            """البحث عن جذر في المعجم."""
            if not self.system_ready:
                return self.create_response(False, error='النظام غير جاهز')

            try:
                request_data = request.get_json()
                if not request_data or 'root' not in request_data:
                    return self.create_response(False, error='يرجى تحديد root')

                root = request_data['root'].strip()

                if not root:
                    return self.create_response(False, error='الجذر فارغ')

                search_result = self.lexicon_engine.search_by_root(root)

                data = {
                    'root': root,
                    'words_found': len(search_result['words']),
                    'words': search_result['words'][:30],  # أول 30 كلمة
                    'root_meaning': search_result.get('root_meaning', ''),
                    'morphological_patterns': search_result.get('patterns', [])
                }

                self.log_operation('lexicon_search_root', {'root': root, 'words_found': len(search_result['words'])})
                return self.create_response(data=data)

            except Exception as e:
                return self.create_response(False, error=str(e))

    def run(self, host='localhost', port=8000, debug=False):
        """تشغيل خادم API."""
        
        if self.system_ready:
            print(f"🌐 تشغيل API على http://{host}:{port}")
            print("📚 وثائق API متاحة على:")
            print(f"   معلومات API: http://{host}:{port}/api/info")
            print(f"   حالة النظام: http://{host}:{port}/api/system/status")
            self.app.run(host=host, port=port, debug=debug)
        else:
            print("❌ النظام غير جاهز للتشغيل")

def main():
    """تشغيل واجهة API."""
    
    try:
        api_interface = BaserahAPIInterface()
        api_interface.run(host='0.0.0.0', port=8000, debug=True)
    except Exception as e:
        print(f"خطأ في تشغيل واجهة API: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
