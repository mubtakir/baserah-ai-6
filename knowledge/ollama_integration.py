#!/usr/bin/env python3
"""
🦙 تكامل Ollama - نظام بصيرة الثوري
🔗 ربط مؤقت مع نماذج Ollama المفتوحة المصدر
🧬 استخراج المعرفة وتطبيق النظريات الثلاث

الهدف: بناء مكتبة معرفية ذاتية من النماذج المفتوحة
الاستراتيجية: استخراج → تحليل → حفظ → استقلالية

المطور: باسل يحيى عبدالله
"""

import requests
import json
import subprocess
import time
from typing import Dict, List, Any, Optional
from knowledge_harvester import KnowledgeHarvester
import os

class OllamaIntegration:
    """
    🦙 تكامل Ollama مع نظام بصيرة
    يربط مؤقتاً مع النماذج المفتوحة لاستخراج المعرفة
    """
    
    def __init__(self, ollama_url: str = "http://localhost:11434"):
        """تهيئة تكامل Ollama"""
        self.ollama_url = ollama_url
        self.harvester = KnowledgeHarvester()
        self.available_models = []
        
        print("🦙⚡ تم إنشاء تكامل Ollama")
        print("   🔗 محاولة الاتصال مع Ollama...")
        
        if self.check_ollama_status():
            self.load_available_models()
        else:
            print("   ⚠️ Ollama غير متاح - سيتم تشغيل النظام بدونه")
    
    def check_ollama_status(self) -> bool:
        """فحص حالة Ollama"""
        try:
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=5)
            if response.status_code == 200:
                print("   ✅ Ollama متصل ويعمل")
                return True
            else:
                print(f"   ❌ Ollama يرد بحالة: {response.status_code}")
                return False
        except requests.exceptions.ConnectionError:
            print("   ❌ Ollama غير متصل")
            return False
        except Exception as e:
            print(f"   ❌ خطأ في الاتصال: {e}")
            return False
    
    def install_ollama(self) -> bool:
        """تثبيت Ollama إذا لم يكن موجوداً"""
        try:
            print("📦 محاولة تثبيت Ollama...")
            
            # تحميل وتثبيت Ollama
            install_command = "curl -fsSL https://ollama.ai/install.sh | sh"
            result = subprocess.run(install_command, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ تم تثبيت Ollama بنجاح")
                
                # بدء خدمة Ollama
                print("🚀 بدء خدمة Ollama...")
                subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                time.sleep(5)  # انتظار بدء الخدمة
                
                return self.check_ollama_status()
            else:
                print(f"❌ فشل في تثبيت Ollama: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ خطأ في تثبيت Ollama: {e}")
            return False
    
    def load_available_models(self):
        """تحميل قائمة النماذج المتاحة"""
        try:
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.available_models = [model['name'] for model in data.get('models', [])]
                print(f"   📋 النماذج المتاحة: {self.available_models}")
            else:
                print("   ❌ فشل في تحميل قائمة النماذج")
        except Exception as e:
            print(f"   ❌ خطأ في تحميل النماذج: {e}")
    
    def pull_model(self, model_name: str) -> bool:
        """تحميل نموذج جديد"""
        try:
            print(f"📥 تحميل النموذج: {model_name}")
            
            payload = {"name": model_name}
            response = requests.post(
                f"{self.ollama_url}/api/pull",
                json=payload,
                stream=True,
                timeout=300
            )
            
            if response.status_code == 200:
                print(f"✅ تم تحميل النموذج: {model_name}")
                self.load_available_models()  # تحديث القائمة
                return True
            else:
                print(f"❌ فشل في تحميل النموذج: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ خطأ في تحميل النموذج: {e}")
            return False
    
    def generate_response(self, prompt: str, model: str = "llama3.2:1b") -> Optional[str]:
        """توليد استجابة من النموذج"""
        if not self.check_ollama_status():
            return None
        
        if model not in self.available_models:
            print(f"⚠️ النموذج {model} غير متاح، محاولة تحميله...")
            if not self.pull_model(model):
                return None
        
        try:
            payload = {
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9
                }
            }
            
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json=payload,
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                content = result.get('response', '')
                
                # حفظ الاستجابة في مكتبة المعرفة
                if content:
                    knowledge_item = self.harvester._create_knowledge_item(
                        content=content,
                        source=f"ollama_{model}",
                        category="llm_response",
                        language="ar"
                    )
                    self.harvester._save_knowledge_item(knowledge_item)
                    print(f"✅ تم حفظ الاستجابة في مكتبة المعرفة")
                
                return content
            else:
                print(f"❌ خطأ في توليد الاستجابة: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ خطأ في التوليد: {e}")
            return None
    
    def extract_knowledge_batch(self, topics: List[str], model: str = "llama3.2:1b") -> int:
        """استخراج معرفة مجمعة حول مواضيع متعددة"""
        extracted_count = 0
        
        for topic in topics:
            print(f"\n🔍 استخراج معرفة حول: {topic}")
            
            # إنشاء استعلام للموضوع
            prompt = f"اشرح لي بالتفصيل عن {topic} باللغة العربية. قدم معلومات شاملة ومفيدة."
            
            response = self.generate_response(prompt, model)
            if response:
                print(f"   ✅ تم استخراج {len(response)} حرف")
                extracted_count += 1
            else:
                print(f"   ❌ فشل في استخراج معرفة حول {topic}")
            
            time.sleep(2)  # تجنب الضغط على النموذج
        
        return extracted_count
    
    def create_knowledge_vectors(self, texts: List[str]) -> List[Dict[str, Any]]:
        """إنشاء متجهات للنصوص باستخدام النظريات الثورية"""
        vectors = []
        
        for text in texts:
            # حساب متجه ثوري للنص
            vector = {
                "text": text[:100] + "..." if len(text) > 100 else text,
                "length": len(text),
                "words": len(text.split()),
                "sentences": len([s for s in text.split('.') if s.strip()]),
                "zero_duality": self.harvester._calculate_zero_duality(text),
                "perpendicularity": self.harvester._calculate_perpendicularity(text),
                "filaments": self.harvester._calculate_filament_connections(text)
            }
            vectors.append(vector)
        
        return vectors
    
    def get_integration_stats(self) -> Dict[str, Any]:
        """إحصائيات التكامل"""
        knowledge_stats = self.harvester.get_knowledge_stats()
        
        return {
            "ollama_status": self.check_ollama_status(),
            "available_models": self.available_models,
            "knowledge_base": knowledge_stats,
            "integration_active": len(self.available_models) > 0
        }

def setup_recommended_models():
    """إعداد النماذج الموصى بها"""
    
    print("🦙 إعداد النماذج الموصى بها لنظام بصيرة")
    print("=" * 60)
    
    integration = OllamaIntegration()
    
    # النماذج الموصى بها (صغيرة ومناسبة)
    recommended_models = [
        "llama2:7b",      # نموذج عام جيد
        "mistral:7b",     # نموذج سريع وفعال
        "codellama:7b"    # للبرمجة والتقنية
    ]
    
    if integration.check_ollama_status():
        print("\n📥 تحميل النماذج الموصى بها:")
        for model in recommended_models:
            print(f"\n🔄 محاولة تحميل: {model}")
            success = integration.pull_model(model)
            if success:
                print(f"✅ تم تحميل {model} بنجاح")
            else:
                print(f"❌ فشل في تحميل {model}")
    else:
        print("\n⚠️ Ollama غير متاح - تخطي تحميل النماذج")
    
    return integration

def demo_knowledge_extraction():
    """عرض توضيحي لاستخراج المعرفة"""
    
    print("\n🌾 عرض توضيحي لاستخراج المعرفة")
    print("=" * 60)
    
    integration = OllamaIntegration()
    
    # مواضيع للاستخراج
    topics = [
        "الذكاء الاصطناعي",
        "معالجة اللغة الطبيعية",
        "التعلم الآلي",
        "الرياضيات التطبيقية"
    ]
    
    if integration.check_ollama_status() and integration.available_models:
        print(f"\n🔍 استخراج معرفة حول {len(topics)} مواضيع:")
        model = integration.available_models[0]  # استخدام أول نموذج متاح
        
        extracted = integration.extract_knowledge_batch(topics, model)
        print(f"\n✅ تم استخراج معرفة حول {extracted} موضوع")
    else:
        print("\n⚠️ لا توجد نماذج متاحة - استخدام المعرفة المحلية فقط")
    
    # عرض الإحصائيات
    print("\n📊 إحصائيات التكامل:")
    stats = integration.get_integration_stats()
    print(f"   🦙 حالة Ollama: {'متصل' if stats['ollama_status'] else 'غير متصل'}")
    print(f"   📋 النماذج المتاحة: {len(stats['available_models'])}")
    print(f"   📚 قاعدة المعرفة: {stats['knowledge_base'].get('total_knowledge', 0)} عنصر")
    
    return integration

if __name__ == "__main__":
    # تشغيل العرض التوضيحي
    integration = demo_knowledge_extraction()
    
    print("\n🎉 انتهى العرض التوضيحي!")
    print("🧬 نظام التكامل مع Ollama جاهز للاستخدام!")
