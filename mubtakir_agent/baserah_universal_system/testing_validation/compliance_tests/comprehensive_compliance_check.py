#!/usr/bin/env python3
# comprehensive_compliance_check.py - فحص شامل لالتزام النظام بالتوصيات الثورية

import os
import re
import sys
from datetime import datetime
from typing import Dict, List, Tuple, Any

class BaserahComplianceChecker:
    """فاحص الالتزام بمنهج Baserah الثوري."""
    
    def __init__(self):
        """تهيئة الفاحص."""
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.compliance_report = {
            'total_files_checked': 0,
            'compliant_files': 0,
            'non_compliant_files': 0,
            'issues_found': [],
            'recommendations': [],
            'test_results': {},
            'purity_score': 0.0
        }
        
        # قائمة المكتبات المحظورة (الذكاء الاصطناعي التقليدي)
        self.forbidden_imports = [
            'tensorflow', 'torch', 'pytorch', 'sklearn', 'scikit-learn',
            'keras', 'theano', 'caffe', 'mxnet', 'paddle', 'jax',
            'transformers', 'huggingface', 'openai', 'anthropic',
            'neural', 'network', 'deep.*learning', 'machine.*learning',
            'gradient.*descent', 'backprop', 'cnn', 'rnn', 'lstm', 'gru'
        ]
        
        # الدوال المطلوبة (منهج Baserah)
        self.required_functions = [
            'baserah_sigmoid', 'baserah_linear', 'baserah_quantum',
            'baserah_equation'
        ]
        
        # مؤشرات النقاء المطلوبة
        self.purity_indicators = [
            'baserah_purity.*1\.0', 'نقي', 'بديل.*للشبكات.*العصبية',
            'لا.*مكتبات.*ذكاء.*اصطناعي', '100%.*نقي'
        ]
    
    def check_file_compliance(self, file_path: str) -> Dict[str, Any]:
        """فحص التزام ملف واحد."""
        
        compliance_result = {
            'file_path': file_path,
            'is_compliant': True,
            'issues': [],
            'baserah_functions_found': [],
            'purity_indicators_found': [],
            'forbidden_imports_found': [],
            'test_status': 'not_tested'
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # فحص الاستيرادات المحظورة
            for forbidden in self.forbidden_imports:
                pattern = rf'import.*{forbidden}|from.*{forbidden}'
                if re.search(pattern, content, re.IGNORECASE):
                    compliance_result['forbidden_imports_found'].append(forbidden)
                    compliance_result['issues'].append(f"استيراد محظور: {forbidden}")
                    compliance_result['is_compliant'] = False
            
            # فحص وجود دوال Baserah
            for func in self.required_functions:
                if re.search(rf'def.*{func}', content):
                    compliance_result['baserah_functions_found'].append(func)
            
            # فحص مؤشرات النقاء
            for indicator in self.purity_indicators:
                if re.search(indicator, content, re.IGNORECASE):
                    compliance_result['purity_indicators_found'].append(indicator)
            
            # فحص إضافي للملفات Python
            if file_path.endswith('.py'):
                # فحص استخدام numpy فقط للعمليات الأساسية
                numpy_usage = re.findall(r'np\.\w+', content)
                allowed_numpy = ['np.array', 'np.exp', 'np.sin', 'np.cos', 'np.random', 'np.linspace', 'np.mean']
                
                for usage in numpy_usage:
                    if not any(allowed in usage for allowed in allowed_numpy):
                        compliance_result['issues'].append(f"استخدام numpy غير مسموح: {usage}")
                
                # فحص التعليقات العربية
                arabic_comments = re.findall(r'#.*[\u0600-\u06FF]', content)
                if len(arabic_comments) < 3:  # يجب وجود تعليقات عربية كافية
                    compliance_result['issues'].append("قلة التعليقات العربية")
        
        except Exception as e:
            compliance_result['issues'].append(f"خطأ في قراءة الملف: {e}")
            compliance_result['is_compliant'] = False
        
        return compliance_result
    
    def check_directory_compliance(self, directory: str) -> List[Dict[str, Any]]:
        """فحص التزام مجلد كامل."""
        
        results = []
        
        for root, dirs, files in os.walk(directory):
            # تجاهل مجلدات معينة
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
            
            for file in files:
                if file.endswith(('.py', '.md')):
                    file_path = os.path.join(root, file)
                    result = self.check_file_compliance(file_path)
                    results.append(result)
        
        return results
    
    def test_core_functions(self) -> Dict[str, Any]:
        """اختبار الدوال الأساسية."""
        
        test_results = {
            'baserah_core_test': False,
            'sigmoid_test': False,
            'linear_test': False,
            'quantum_test': False,
            'error_messages': []
        }
        
        try:
            # اختبار نواة Baserah
            sys.path.append(os.path.join(self.base_path, 'artistic_unit'))
            from artistic_intelligence.baserah_core import baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid
            
            # اختبار السيجمويد
            result = baserah_sigmoid(0, n=1, k=1.0, x0=0.0, alpha=1.0)
            if 0.4 < result < 0.6:  # يجب أن يكون حوالي 0.5
                test_results['sigmoid_test'] = True
            
            # اختبار الخطي
            result = baserah_linear(2, beta=3.0, gamma=1.0)
            if result == 7.0:  # 3*2 + 1 = 7
                test_results['linear_test'] = True
            
            # اختبار الكمي
            result = baserah_quantum_sigmoid(0, quantum_factor=4)
            if isinstance(result, (int, float)):
                test_results['quantum_test'] = True
            
            test_results['baserah_core_test'] = all([
                test_results['sigmoid_test'],
                test_results['linear_test'],
                test_results['quantum_test']
            ])
            
        except Exception as e:
            test_results['error_messages'].append(f"خطأ في اختبار النواة: {e}")
        
        return test_results
    
    def test_system_integration(self) -> Dict[str, Any]:
        """اختبار تكامل النظام."""
        
        integration_results = {
            'mother_system_test': False,
            'shapes_database_test': False,
            'expert_explorer_test': False,
            'artistic_unit_test': False,
            'error_messages': []
        }
        
        try:
            # اختبار النظام الأم
            from revolutionary_intelligence.revolutionary_mother_system.revolutionary_mother_system import BaserahRevolutionaryMotherSystem
            mother_system = BaserahRevolutionaryMotherSystem()
            if hasattr(mother_system, 'system_id'):
                integration_results['mother_system_test'] = True
            
            # اختبار قاعدة بيانات الأشكال
            from knowledge_systems.shapes_database.shapes_database import BaserahShapesDatabase
            shapes_db = BaserahShapesDatabase()
            if len(shapes_db.shapes) > 0:
                integration_results['shapes_database_test'] = True
            
            # اختبار النظام الخبير
            try:
                from revolutionary_intelligence.expert_explorer_system.expert_explorer.integrated_expert_explorer import BaserahIntegratedExpertExplorer
                expert_system = BaserahIntegratedExpertExplorer()
                if hasattr(expert_system, 'adaptive_equations'):
                    integration_results['expert_explorer_test'] = True
            except ImportError:
                integration_results['error_messages'].append("النظام الخبير غير متاح")
            
            # اختبار الوحدة الفنية
            from artistic_unit.integrated_system import BaserahIntegratedSystem
            artistic_unit = BaserahIntegratedSystem()
            if hasattr(artistic_unit, 'inference_engine'):
                integration_results['artistic_unit_test'] = True
            
        except Exception as e:
            integration_results['error_messages'].append(f"خطأ في اختبار التكامل: {e}")
        
        return integration_results
    
    def generate_compliance_report(self) -> Dict[str, Any]:
        """إنشاء تقرير الالتزام الشامل."""
        
        print("🔍 بدء فحص الالتزام الشامل للنظام...")
        print("=" * 60)
        
        # فحص جميع الملفات
        file_results = self.check_directory_compliance(self.base_path)
        
        # تحديث الإحصائيات
        self.compliance_report['total_files_checked'] = len(file_results)
        self.compliance_report['compliant_files'] = sum(1 for r in file_results if r['is_compliant'])
        self.compliance_report['non_compliant_files'] = len(file_results) - self.compliance_report['compliant_files']
        
        # جمع المشاكل
        for result in file_results:
            if not result['is_compliant']:
                self.compliance_report['issues_found'].extend([
                    f"{result['file_path']}: {issue}" for issue in result['issues']
                ])
        
        # اختبار الدوال الأساسية
        core_test_results = self.test_core_functions()
        self.compliance_report['test_results']['core_functions'] = core_test_results
        
        # اختبار تكامل النظام
        integration_results = self.test_system_integration()
        self.compliance_report['test_results']['system_integration'] = integration_results
        
        # حساب نقاط النقاء
        total_tests = 7  # عدد الاختبارات الأساسية
        passed_tests = sum([
            core_test_results['baserah_core_test'],
            core_test_results['sigmoid_test'],
            core_test_results['linear_test'],
            core_test_results['quantum_test'],
            integration_results['mother_system_test'],
            integration_results['shapes_database_test'],
            integration_results['artistic_unit_test']
        ])
        
        self.compliance_report['purity_score'] = passed_tests / total_tests
        
        # توصيات
        if self.compliance_report['non_compliant_files'] > 0:
            self.compliance_report['recommendations'].append("إصلاح الملفات غير المتوافقة")
        
        if self.compliance_report['purity_score'] < 1.0:
            self.compliance_report['recommendations'].append("تحسين اختبارات النظام")
        
        return self.compliance_report
    
    def print_detailed_report(self):
        """طباعة تقرير مفصل."""
        
        report = self.generate_compliance_report()
        
        print("\n📊 تقرير الالتزام بمنهج Baserah الثوري")
        print("=" * 60)
        print(f"📅 تاريخ الفحص: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📁 المجلد المفحوص: {self.base_path}")
        
        print(f"\n📈 إحصائيات عامة:")
        print(f"   إجمالي الملفات: {report['total_files_checked']}")
        print(f"   ملفات متوافقة: {report['compliant_files']}")
        print(f"   ملفات غير متوافقة: {report['non_compliant_files']}")
        print(f"   نقاط النقاء: {report['purity_score']:.1%}")
        
        print(f"\n🧪 نتائج اختبار الدوال الأساسية:")
        core_results = report['test_results']['core_functions']
        print(f"   اختبار نواة Baserah: {'✅' if core_results['baserah_core_test'] else '❌'}")
        print(f"   اختبار السيجمويد: {'✅' if core_results['sigmoid_test'] else '❌'}")
        print(f"   اختبار الخطي: {'✅' if core_results['linear_test'] else '❌'}")
        print(f"   اختبار الكمي: {'✅' if core_results['quantum_test'] else '❌'}")
        
        print(f"\n🔗 نتائج اختبار تكامل النظام:")
        integration_results = report['test_results']['system_integration']
        print(f"   النظام الأم: {'✅' if integration_results['mother_system_test'] else '❌'}")
        print(f"   قاعدة بيانات الأشكال: {'✅' if integration_results['shapes_database_test'] else '❌'}")
        print(f"   النظام الخبير: {'✅' if integration_results['expert_explorer_test'] else '❌'}")
        print(f"   الوحدة الفنية: {'✅' if integration_results['artistic_unit_test'] else '❌'}")
        
        if report['issues_found']:
            print(f"\n⚠️ المشاكل المكتشفة ({len(report['issues_found'])}):")
            for issue in report['issues_found'][:10]:  # أول 10 مشاكل
                print(f"   • {issue}")
            if len(report['issues_found']) > 10:
                print(f"   ... و {len(report['issues_found']) - 10} مشكلة أخرى")
        
        if report['recommendations']:
            print(f"\n💡 التوصيات:")
            for rec in report['recommendations']:
                print(f"   • {rec}")
        
        # تقييم نهائي
        if report['purity_score'] >= 0.9:
            print(f"\n🎉 النظام يلتزم بمنهج Baserah الثوري بدرجة ممتازة!")
        elif report['purity_score'] >= 0.7:
            print(f"\n👍 النظام يلتزم بمنهج Baserah الثوري بدرجة جيدة")
        else:
            print(f"\n⚠️ النظام يحتاج تحسينات للالتزام بمنهج Baserah الثوري")
        
        return report

def main():
    """تشغيل فحص الالتزام الشامل."""
    
    checker = BaserahComplianceChecker()
    report = checker.print_detailed_report()
    
    # حفظ التقرير
    report_file = f"compliance_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(f"تقرير الالتزام بمنهج Baserah الثوري\n")
        f.write(f"تاريخ الفحص: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"نقاط النقاء: {report['purity_score']:.1%}\n")
        f.write(f"الملفات المتوافقة: {report['compliant_files']}/{report['total_files_checked']}\n")
    
    print(f"\n💾 تم حفظ التقرير في: {report_file}")
    
    return report['purity_score'] >= 0.8

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
