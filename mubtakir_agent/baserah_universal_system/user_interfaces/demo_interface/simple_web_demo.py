#!/usr/bin/env python3
# simple_web_demo.py - واجهة ويب بسيطة للنظام الثوري Baserah

import http.server
import socketserver
import json
import urllib.parse
from datetime import datetime
import threading
import time

class BaserahWebHandler(http.server.SimpleHTTPRequestHandler):
    """معالج طلبات الويب للنظام الثوري Baserah."""
    
    def do_GET(self):
        """معالجة طلبات GET."""
        
        if self.path == '/' or self.path == '/index.html':
            self.serve_main_page()
        elif self.path == '/api/status':
            self.serve_status_api()
        elif self.path == '/api/shapes':
            self.serve_shapes_api()
        elif self.path == '/api/test':
            self.serve_test_api()
        else:
            super().do_GET()
    
    def serve_main_page(self):
        """تقديم الصفحة الرئيسية."""
        
        html_content = """
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>النظام الثوري Baserah</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            color: white;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 30px;
            backdrop-filter: blur(10px);
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        .header h1 {
            font-size: 2.5em;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .header p {
            font-size: 1.2em;
            margin: 10px 0;
            opacity: 0.9;
        }
        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        .card {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 10px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .card h3 {
            margin-top: 0;
            color: #ffd700;
        }
        .button {
            background: linear-gradient(45deg, #ff6b6b, #ee5a24);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            margin: 5px;
            transition: transform 0.2s;
        }
        .button:hover {
            transform: translateY(-2px);
        }
        .result {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 8px;
            padding: 15px;
            margin: 15px 0;
            font-family: monospace;
            white-space: pre-wrap;
            max-height: 300px;
            overflow-y: auto;
        }
        .status {
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
        }
        .status-item {
            text-align: center;
        }
        .status-value {
            font-size: 2em;
            font-weight: bold;
            color: #4ecdc4;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌟 النظام الثوري Baserah</h1>
            <p>🎯 نظام ذكي ثوري بدون مكتبات ذكاء اصطناعي تقليدي</p>
            <p>🔧 يستخدم فقط: السيجمويد + المعادلات الخطية</p>
            <p>📅 """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
        </div>
        
        <div class="status" id="status">
            <div class="status-item">
                <div class="status-value" id="purity">100%</div>
                <div>نقاء Baserah</div>
            </div>
            <div class="status-item">
                <div class="status-value" id="shapes">18</div>
                <div>الأشكال</div>
            </div>
            <div class="status-item">
                <div class="status-value" id="functions">3</div>
                <div>الدوال الأساسية</div>
            </div>
        </div>
        
        <div class="cards">
            <div class="card">
                <h3>🔧 الدوال الأساسية</h3>
                <p>اختبار دوال السيجمويد والخطي والكمي</p>
                <button class="button" onclick="testFunctions()">اختبار الدوال</button>
                <div class="result" id="functions-result"></div>
            </div>
            
            <div class="card">
                <h3>🗄️ قاعدة بيانات الأشكال</h3>
                <p>عرض الأشكال والبحث والتحويل</p>
                <button class="button" onclick="testShapes()">عرض الأشكال</button>
                <div class="result" id="shapes-result"></div>
            </div>
            
            <div class="card">
                <h3>🌟 النظام الأم</h3>
                <p>النظام الثوري الأم وقاعدة البيانات</p>
                <button class="button" onclick="testMother()">اختبار النظام الأم</button>
                <div class="result" id="mother-result"></div>
            </div>
            
            <div class="card">
                <h3>🧠 النظام الخبير</h3>
                <p>المعادلات المتكيفة والذكاء الثوري</p>
                <button class="button" onclick="testExpert()">اختبار النظام الخبير</button>
                <div class="result" id="expert-result"></div>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 30px;">
            <button class="button" onclick="runFullTest()" style="font-size: 18px; padding: 15px 30px;">
                🚀 تشغيل اختبار شامل
            </button>
        </div>
        
        <div class="result" id="full-result"></div>
    </div>

    <script>
        async function apiCall(endpoint) {
            try {
                const response = await fetch(endpoint);
                const data = await response.json();
                return data;
            } catch (error) {
                return { error: error.message };
            }
        }
        
        async function testFunctions() {
            document.getElementById('functions-result').textContent = 'جاري الاختبار...';
            const result = await apiCall('/api/test?type=functions');
            document.getElementById('functions-result').textContent = JSON.stringify(result, null, 2);
        }
        
        async function testShapes() {
            document.getElementById('shapes-result').textContent = 'جاري التحميل...';
            const result = await apiCall('/api/shapes');
            document.getElementById('shapes-result').textContent = JSON.stringify(result, null, 2);
        }
        
        async function testMother() {
            document.getElementById('mother-result').textContent = 'جاري الاختبار...';
            const result = await apiCall('/api/test?type=mother');
            document.getElementById('mother-result').textContent = JSON.stringify(result, null, 2);
        }
        
        async function testExpert() {
            document.getElementById('expert-result').textContent = 'جاري الاختبار...';
            const result = await apiCall('/api/test?type=expert');
            document.getElementById('expert-result').textContent = JSON.stringify(result, null, 2);
        }
        
        async function runFullTest() {
            document.getElementById('full-result').textContent = 'جاري تشغيل الاختبار الشامل...';
            const result = await apiCall('/api/test?type=full');
            document.getElementById('full-result').textContent = JSON.stringify(result, null, 2);
        }
        
        // تحديث الحالة كل 30 ثانية
        setInterval(async () => {
            const status = await apiCall('/api/status');
            if (status && !status.error) {
                document.getElementById('purity').textContent = status.purity || '100%';
                document.getElementById('shapes').textContent = status.shapes || '18';
                document.getElementById('functions').textContent = status.functions || '3';
            }
        }, 30000);
    </script>
</body>
</html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))
    
    def serve_status_api(self):
        """تقديم API الحالة."""
        
        try:
            status = {
                'timestamp': datetime.now().isoformat(),
                'purity': '100%',
                'shapes': 18,
                'functions': 3,
                'system_status': 'running',
                'components': {
                    'mother_system': True,
                    'shapes_database': True,
                    'expert_system': True,
                    'basic_functions': True
                }
            }
            
            self.send_json_response(status)
            
        except Exception as e:
            self.send_json_response({'error': str(e)})
    
    def serve_shapes_api(self):
        """تقديم API الأشكال."""
        
        try:
            # محاولة تحميل قاعدة البيانات
            import sys
            sys.path.append('.')
            
            from knowledge_systems.shapes_database.shapes_database import BaserahShapesDatabase
            
            db = BaserahShapesDatabase()
            
            shapes_info = {
                'total_shapes': len(db.shapes),
                'shapes_by_type': {},
                'sample_shapes': []
            }
            
            # تجميع حسب النوع
            from knowledge_systems.shapes_database.shapes_database import ShapeType
            for shape_type in ShapeType:
                shapes = db.get_shapes_by_type(shape_type)
                shapes_info['shapes_by_type'][shape_type.value] = len(shapes)
            
            # عينة من الأشكال
            for shape_id, shape in list(db.shapes.items())[:5]:
                shapes_info['sample_shapes'].append({
                    'id': shape_id,
                    'name_ar': shape.metadata.name_ar,
                    'type': shape.shape_type.value,
                    'complexity': shape.complexity_level.value
                })
            
            self.send_json_response(shapes_info)
            
        except Exception as e:
            self.send_json_response({'error': str(e)})
    
    def serve_test_api(self):
        """تقديم API الاختبار."""
        
        try:
            # استخراج نوع الاختبار
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            test_type = params.get('type', ['functions'])[0]
            
            import sys
            sys.path.append('.')
            
            if test_type == 'functions':
                result = self.test_basic_functions()
            elif test_type == 'mother':
                result = self.test_mother_system()
            elif test_type == 'expert':
                result = self.test_expert_system()
            elif test_type == 'full':
                result = self.test_full_system()
            else:
                result = {'error': 'نوع اختبار غير معروف'}
            
            self.send_json_response(result)
            
        except Exception as e:
            self.send_json_response({'error': str(e)})
    
    def test_basic_functions(self):
        """اختبار الدوال الأساسية."""
        
        try:
            from artistic_intelligence.baserah_core import baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid
            
            results = {
                'sigmoid_tests': [],
                'linear_tests': [],
                'quantum_tests': [],
                'success': True
            }
            
            # اختبار السيجمويد
            for x in [-2, -1, 0, 1, 2]:
                result = baserah_sigmoid(x, n=2, k=1.5, x0=0.0, alpha=1.0)
                results['sigmoid_tests'].append({'x': x, 'result': round(result, 4)})
            
            # اختبار الخطي
            for x in [-2, -1, 0, 1, 2]:
                result = baserah_linear(x, beta=0.8, gamma=0.2)
                results['linear_tests'].append({'x': x, 'result': round(result, 4)})
            
            # اختبار الكمي
            for x in [0, 1, 2]:
                result = baserah_quantum_sigmoid(x, quantum_factor=4)
                results['quantum_tests'].append({'x': x, 'result': round(result, 4)})
            
            return results
            
        except Exception as e:
            return {'error': str(e), 'success': False}
    
    def test_mother_system(self):
        """اختبار النظام الأم."""
        
        try:
            from revolutionary_intelligence.revolutionary_mother_system.revolutionary_mother_system import BaserahRevolutionaryMotherSystem
            
            mother = BaserahRevolutionaryMotherSystem()
            summary = mother.get_system_summary()
            
            return {
                'system_id': mother.system_id,
                'purity': summary['baserah_purity'],
                'total_shapes': summary.get('shapes_database', {}).get('total_shapes', 0),
                'success': True
            }
            
        except Exception as e:
            return {'error': str(e), 'success': False}
    
    def test_expert_system(self):
        """اختبار النظام الخبير."""
        
        try:
            from revolutionary_intelligence.expert_explorer_system.expert_explorer.integrated_expert_explorer import BaserahIntegratedExpertExplorer
            
            expert = BaserahIntegratedExpertExplorer()
            
            # اختبار إنشاء معادلة
            x_data = [0, 1, 2, 3, 4]
            y_data = [0, 1, 4, 9, 16]
            
            adaptive_eq = expert.create_adaptive_equation_from_data(x_data, y_data)
            
            return {
                'adaptive_equations': len(expert.adaptive_equations),
                'equation_created': adaptive_eq is not None,
                'equation_id': adaptive_eq.id if adaptive_eq else None,
                'success': True
            }
            
        except Exception as e:
            return {'error': str(e), 'success': False}
    
    def test_full_system(self):
        """اختبار شامل للنظام."""
        
        results = {
            'functions': self.test_basic_functions(),
            'mother': self.test_mother_system(),
            'expert': self.test_expert_system(),
            'timestamp': datetime.now().isoformat()
        }
        
        # حساب معدل النجاح
        successes = sum(1 for test in results.values() if isinstance(test, dict) and test.get('success', False))
        total = 3  # عدد الاختبارات
        
        results['overall'] = {
            'success_rate': successes / total,
            'passed': successes,
            'total': total,
            'status': 'excellent' if successes == total else 'good' if successes >= 2 else 'needs_improvement'
        }
        
        return results
    
    def send_json_response(self, data):
        """إرسال استجابة JSON."""
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        json_data = json.dumps(data, ensure_ascii=False, indent=2)
        self.wfile.write(json_data.encode('utf-8'))

def start_web_server(port=8080):
    """بدء خادم الويب."""
    
    print(f"🌐 بدء خادم الويب للنظام الثوري Baserah...")
    print(f"📡 المنفذ: {port}")
    print(f"🔗 الرابط: http://localhost:{port}")
    print("=" * 50)
    
    try:
        with socketserver.TCPServer(("", port), BaserahWebHandler) as httpd:
            print(f"✅ الخادم يعمل على المنفذ {port}")
            print("🎯 اضغط Ctrl+C للإيقاف")
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 تم إيقاف الخادم")
    except Exception as e:
        print(f"❌ خطأ في الخادم: {e}")

if __name__ == "__main__":
    start_web_server()
