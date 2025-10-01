#!/usr/bin/env python3
# __init__.py - حزمة الوكيل المساعد الذكي الثوري
# يفهم الفكرة وينفذ المشروع كاملاً وينشئ المجلدات والملفات والهيكلية

"""
الوكيل المساعد الذكي الثوري
============================

وكيل مساعد ذكي يفهم الفكرة فينفذ المشروع كاملاً وينشئ المجلدات والملفات والهيكلية الكاملة الصحيحة ويكتب الكود.

الميزات الثورية:
- فهم عميق للأفكار باستخدام النظام المعرفي الباهر
- إنشاء مشاريع كاملة بهيكلية ثورية
- توليد كود ثوري مدعوم بنظام Baserah النقي
- تطبيق نظريات باسل الثورية الثلاث
- منهج التطوير الذاتي والتحسين المستمر
- عدم استخدام AI تقليدي (sigmoid + linear فقط)

المكونات الرئيسية:
- RevolutionaryIntelligentAgent: الوكيل الرئيسي
- RevolutionaryAgentCore: النواة الثورية
- BaserahContentGenerator: مولد المحتوى الثوري

الاستخدام السريع:
```python
from revolutionary_intelligent_agent import RevolutionaryIntelligentAgent
import asyncio

async def main():
    agent = RevolutionaryIntelligentAgent("MyAgent")
    result = await agent.understand_and_create_project("فكرة مشروعي الثوري")
    print(result)

asyncio.run(main())
```

أو استخدام الدوال السريعة:
```python
from revolutionary_intelligent_agent import create_revolutionary_project
import asyncio

async def main():
    result = await create_revolutionary_project("فكرة مشروعي")
    print(result)

asyncio.run(main())
```
"""

__version__ = "1.0.0"
__author__ = "Revolutionary Intelligent Agent System"
__description__ = "وكيل مساعد ذكي ثوري يفهم الأفكار وينفذ المشاريع كاملة"
__license__ = "MIT"

# استيراد المكونات الرئيسية
try:
    from .revolutionary_intelligent_agent import (
        RevolutionaryIntelligentAgent,
        create_revolutionary_project,
        create_multiple_revolutionary_projects,
        get_revolutionary_agent_demo
    )
    
    from .revolutionary_agent_core import (
        RevolutionaryAgentCore,
        AgentTask,
        AgentResponse,
        AgentTaskType,
        AgentCapabilityLevel
    )
    
    from .content_generation_helpers import BaserahContentGenerator
    
    # قائمة الصادرات
    __all__ = [
        # الوكيل الرئيسي
        'RevolutionaryIntelligentAgent',
        
        # الدوال السريعة
        'create_revolutionary_project',
        'create_multiple_revolutionary_projects',
        'get_revolutionary_agent_demo',
        
        # النواة الثورية
        'RevolutionaryAgentCore',
        'AgentTask',
        'AgentResponse',
        'AgentTaskType',
        'AgentCapabilityLevel',
        
        # مولد المحتوى
        'BaserahContentGenerator',
        
        # معلومات الحزمة
        '__version__',
        '__author__',
        '__description__',
        '__license__'
    ]
    
    # رسالة ترحيب
    def print_welcome_message():
        """طباعة رسالة ترحيب ثورية."""
        print("🤖✨ مرحباً بك في الوكيل المساعد الذكي الثوري!")
        print("🧬 مدعوم بنظريات باسل الثورية ونظام Baserah النقي")
        print("🚀 يفهم الفكرة وينفذ المشروع كاملاً!")
        print(f"📦 الإصدار: {__version__}")
        print()
    
    # معلومات النظام
    def get_system_info():
        """الحصول على معلومات النظام."""
        return {
            'name': 'Revolutionary Intelligent Agent',
            'version': __version__,
            'author': __author__,
            'description': __description__,
            'license': __license__,
            'capabilities': [
                'project_understanding',
                'project_creation', 
                'code_generation',
                'structure_design',
                'file_management',
                'cognitive_intelligence',
                'revolutionary_thinking',
                'baserah_integration',
                'basil_theories_application'
            ],
            'revolutionary_features': {
                'baserah_pure_approach': True,
                'basil_theories_integration': True,
                'cognitive_deep_thinking': True,
                'self_development_capability': True,
                'intelligent_project_creation': True,
                'no_traditional_ai': True
            },
            'supported_project_types': [
                'web_application',
                'desktop_application',
                'api_service',
                'data_science',
                'machine_learning_alternative',
                'mathematical_tools',
                'educational_software',
                'revolutionary_systems'
            ]
        }
    
    # دوال مساعدة سريعة
    def quick_demo():
        """عرض سريع للوكيل."""
        print("🎭 عرض سريع للوكيل المساعد الثوري")
        print("=" * 50)
        
        # إنشاء وكيل تجريبي
        demo_agent = get_revolutionary_agent_demo()
        
        # عرض المعلومات
        status = demo_agent.get_agent_status()
        
        print(f"🤖 اسم الوكيل: {status['agent_info']['name']}")
        print(f"📦 الإصدار: {status['agent_info']['version']}")
        print(f"🏆 تقييم الأداء: {status['performance_assessment']}")
        
        print("\n🛠️ القدرات المتاحة:")
        for capability, enabled in status['capabilities'].items():
            if enabled:
                print(f"  ✅ {capability}")
        
        print("\n🌟 الميزات الثورية:")
        for feature, enabled in status['revolutionary_features'].items():
            if enabled:
                print(f"  🔥 {feature}")
        
        print("\n📊 الإحصائيات:")
        stats = status['statistics']
        print(f"  📁 مشاريع منشأة: {stats['projects_created']}")
        print(f"  📄 ملفات مولدة: {stats['total_files_generated']}")
        print(f"  💡 رؤى ثورية: {stats['revolutionary_insights_generated']}")
        
        return demo_agent
    
    # دالة للحصول على أمثلة الاستخدام
    def get_usage_examples():
        """الحصول على أمثلة الاستخدام."""
        
        examples = {
            'basic_usage': '''
# الاستخدام الأساسي
from revolutionary_intelligent_agent import RevolutionaryIntelligentAgent
import asyncio

async def main():
    agent = RevolutionaryIntelligentAgent("MyAgent")
    result = await agent.understand_and_create_project("تطبيق ويب ثوري")
    print(f"نجح المشروع: {result['overall_success']}")

asyncio.run(main())
''',
            
            'quick_function': '''
# استخدام الدالة السريعة
from revolutionary_intelligent_agent import create_revolutionary_project
import asyncio

async def main():
    result = await create_revolutionary_project(
        "حاسبة رياضية ثورية",
        {"type": "desktop", "features": ["baserah", "basil_theories"]}
    )
    print(result)

asyncio.run(main())
''',
            
            'multiple_projects': '''
# إنشاء عدة مشاريع
from revolutionary_intelligent_agent import create_multiple_revolutionary_projects
import asyncio

async def main():
    projects = [
        "تطبيق قائمة مهام ثوري",
        "محول وحدات رياضي",
        "نظام إدارة ملفات ذكي"
    ]
    
    result = await create_multiple_revolutionary_projects(projects)
    print(f"معدل النجاح: {result['batch_statistics']['success_rate']:.1%}")

asyncio.run(main())
''',
            
            'demo_agent': '''
# استخدام الوكيل التجريبي
from revolutionary_intelligent_agent import get_revolutionary_agent_demo

# إنشاء وكيل تجريبي
demo_agent = get_revolutionary_agent_demo()

# عرض حالة الوكيل
status = demo_agent.get_agent_status()
print(status)
''',
            
            'state_management': '''
# إدارة حالة الوكيل
from revolutionary_intelligent_agent import RevolutionaryIntelligentAgent

agent = RevolutionaryIntelligentAgent("PersistentAgent")

# حفظ الحالة
agent.save_agent_state("agent_state.json")

# تحميل الحالة لاحقاً
new_agent = RevolutionaryIntelligentAgent("RestoredAgent")
new_agent.load_agent_state("agent_state.json")
'''
        }
        
        return examples
    
    # دالة للحصول على التوثيق
    def get_documentation():
        """الحصول على التوثيق الكامل."""
        
        return {
            'overview': __doc__,
            'system_info': get_system_info(),
            'usage_examples': get_usage_examples(),
            'api_reference': {
                'RevolutionaryIntelligentAgent': {
                    'description': 'الوكيل المساعد الذكي الثوري الرئيسي',
                    'methods': [
                        'understand_and_create_project()',
                        'create_multiple_projects()',
                        'get_agent_status()',
                        'save_agent_state()',
                        'load_agent_state()'
                    ]
                },
                'create_revolutionary_project': {
                    'description': 'دالة سريعة لإنشاء مشروع ثوري',
                    'parameters': ['project_idea', 'project_requirements', 'agent_name']
                },
                'create_multiple_revolutionary_projects': {
                    'description': 'دالة سريعة لإنشاء عدة مشاريع',
                    'parameters': ['projects_list', 'agent_name']
                }
            },
            'revolutionary_features': {
                'baserah_system': 'نظام Baserah النقي (sigmoid + linear فقط)',
                'basil_theories': 'نظريات باسل الثورية الثلاث',
                'cognitive_intelligence': 'النظام المعرفي الباهر',
                'self_development': 'قدرة التطوير الذاتي',
                'no_traditional_ai': 'عدم استخدام AI تقليدي'
            }
        }

except ImportError as e:
    print(f"⚠️ تحذير: فشل في استيراد بعض المكونات: {e}")
    print("🔧 تأكد من وجود جميع الملفات المطلوبة")
    
    # تصدير محدود في حالة الخطأ
    __all__ = ['__version__', '__author__', '__description__', '__license__']


# رسالة تهيئة الحزمة
if __name__ != "__main__":
    try:
        # طباعة رسالة ترحيب موجزة عند الاستيراد
        import sys
        if hasattr(sys, 'ps1'):  # فقط في الوضع التفاعلي
            print(f"🤖 تم تحميل الوكيل المساعد الثوري v{__version__}")
    except:
        pass
