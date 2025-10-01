# 🎨 الوحدة الفنية Baserah - Artistic Unit

## 🎯 **نظرة عامة**

**الوحدة الفنية** تجمع بين **البرنامج الراسم والأنيميشن** مع **برنامج الاستنباط** في نظام متكامل واحد.

### **المكونات الأساسية:**
1. **النواة الرياضية** - `baserah_core.py`
2. **محرك الاستنباط** - `inference_engine.py` 
3. **محرك الرسم والأنيميشن** - `artistic_renderer.py`
4. **النظام المتكامل** - `integrated_system.py`

---

## 🔬 **المبادئ الأساسية**

### ✅ **منهج Baserah النقي:**
- **فقط دوال السيجمويد + الخط المستقيم + عامل التكميم**
- **لا مكتبات ذكاء اصطناعي**
- **لا شبكات عصبية**
- **لا تعلم عميق أو معزز**

### 🎯 **معادلة الشكل العام:**
```
f̂(x) = Σ(αᵢ · σₙᵢ(x; kᵢ, x₀ᵢ) + βᵢx + γᵢ)
```

---

## 📁 **هيكل الملفات**

```
artistic_unit/
├── __init__.py                 # تعريف الوحدة
├── baserah_core.py            # النواة الرياضية النقية
├── inference_engine.py        # محرك الاستنباط (عين النظام)
├── artistic_renderer.py       # محرك الرسم والأنيميشن
├── integrated_system.py       # النظام المتكامل
├── test_artistic_unit.py      # اختبارات شاملة
└── README.md                  # هذا الملف
```

---

## 🚀 **الاستخدام السريع**

### **1. اختبار الوحدة:**
```bash
cd artistic_unit
python test_artistic_unit.py
```

### **2. استخدام النواة الرياضية:**
```python
from artistic_unit.baserah_core import baserah_sigmoid, baserah_quantum_sigmoid

# سيجمويد عادي
y = baserah_sigmoid(0.5, n=1, k=2, x0=0, alpha=1)

# سيجمويد مكمم
y_quantum = baserah_quantum_sigmoid(0.5, n=1, k=2, x0=0, alpha=1, quantum_factor=4)
```

### **3. استخدام محرك الاستنباط:**
```python
from artistic_unit.inference_engine import BaserahInferenceEngine

engine = BaserahInferenceEngine()

# بيانات الاختبار
x_data = [-2, -1, 0, 1, 2]
y_data = [1, 3, 5, 7, 9]  # خط مستقيم

# الاستنباط
result = engine.infer_from_data_points(x_data, y_data)
equation = engine.generate_equation_string(result)
print(equation)
```

### **4. استخدام محرك الرسم:**
```python
from artistic_unit.artistic_renderer import BaserahArtisticRenderer

renderer = BaserahArtisticRenderer()

# تعريف معادلة
components = [
    {'type': 'sigmoid', 'params': {'n': 1, 'k': 2, 'x0': 0, 'alpha': 1}},
    {'type': 'linear', 'params': {'beta': 0.1, 'gamma': 0.2}}
]

# الرسم
renderer.render_equation(components, title="معادلة Baserah")
```

### **5. استخدام النظام المتكامل:**
```python
from artistic_unit.integrated_system import BaserahIntegratedSystem

system = BaserahIntegratedSystem()

# تحليل ورسم متكامل
x_data = [-3, -2, -1, 0, 1, 2, 3]
y_data = [0.05, 0.12, 0.27, 0.5, 0.73, 0.88, 0.95]

result = system.analyze_and_render(x_data, y_data, "تحليل متكامل")
```

---

## 🎨 **الإمكانيات الفنية**

### **1. الأنماط الفنية:**
- **قلب نابض** - `renderer.create_artistic_pattern("heart", animate=True)`
- **موجة صوتية** - `renderer.create_artistic_pattern("wave", animate=True)`
- **زهرة متفتحة** - `renderer.create_artistic_pattern("flower", animate=True)`
- **حلزون** - `renderer.create_artistic_pattern("spiral", animate=False)`

### **2. الأنيميشن المتقدم:**
```python
# تحريك المعاملات
parameter_animations = {
    0: {'k': (0.5, 2.0), 'x0': (0, 3)},
    1: {'quantum_factor': (4, 16)}
}

renderer.create_animated_equation(components, parameter_animations, duration=6.0)
```

### **3. عرض مستويات التكميم:**
```python
renderer.render_quantum_levels_demo()
```

---

## 🔍 **محرك الاستنباط (عين النظام)**

### **القدرات:**
- **كشف الأنماط**: خطي، سيجمويد، متقطع، مختلط
- **استنتاج المعاملات**: `n, k, x₀, α, β, γ, quantum_factor`
- **توليد المعادلات**: نصوص قابلة للقراءة
- **حساب الدقة**: خطأ + مستوى ثقة

### **مثال على الاستنباط:**
```
مدخل: x=[-2,-1,0,1,2], y=[0,0,0.5,1,1]
تحليل: "نمط متقطع مكتشف"
استنتاج: quantum_factor=2, k=10.0
مخرج: f(x) = quantum_sigmoid(n=1, k=10.000, x0=0.000, α=1.000, Q=2)
```

---

## 🎯 **عامل التكميم**

### **المستويات المدعومة:**
- **K=1**: سيجمويد عادي (مستمر)
- **K=2**: قفزات بمضاعفات 0.5
- **K=4**: قفزات بمضاعفات 0.25  
- **K=8**: قفزات بمضاعفات 0.125
- **K=16**: قفزات بمضاعفات 0.0625

### **الاستخدام:**
```python
# دالة متقطعة بـ 4 مستويات
y = baserah_quantum_sigmoid(x, quantum_factor=4)
# النتيجة: [0.0, 0.25, 0.5, 0.75, 1.0]
```

---

## 🔗 **التكامل بين الرسم والاستنباط**

### **الدورة الكاملة:**
```
بيانات → [الاستنباط] → معادلة → [الرسم] → شكل بصري
   ↑                                           ↓
   ← [التحليل البصري] ← [معالجة الصورة] ←
```

### **مثال التكامل:**
```python
# 1. بيانات أولية
x_data = [-2, -1, 0, 1, 2]
y_data = [0.1, 0.3, 0.5, 0.7, 0.9]

# 2. الاستنباط
result = engine.infer_from_data_points(x_data, y_data)

# 3. الرسم التلقائي
system.analyze_and_render(x_data, y_data, "تكامل كامل")

# 4. النتيجة: رسم بياني + معادلة نصية + تحليل دقة
```

---

## 🧪 **الاختبارات**

### **تشغيل جميع الاختبارات:**
```bash
python test_artistic_unit.py
```

### **الاختبارات المتاحة:**
1. **اختبار الدوال الأساسية** - التحقق من النواة الرياضية
2. **اختبار محرك الاستنباط** - التحقق من دقة الاستنتاج
3. **اختبار محرك الرسم** - التحقق من الرسم والأنيميشن
4. **اختبار النظام المتكامل** - التحقق من التكامل الكامل
5. **اختبار عامل التكميم** - التحقق من المستويات المنفصلة

---

## 📊 **أمثلة النتائج**

### **استنباط خط مستقيم:**
```
f(x) = linear(2.000*x + 5.000) [خطأ: 0.000000, ثقة: 0.90]
```

### **استنباط سيجمويد:**
```
f(x) = sigmoid(n=1, k=2.000, x0=0.000, α=1.000) [خطأ: 0.000123, ثقة: 0.80]
```

### **استنباط دالة مكممة:**
```
f(x) = quantum_sigmoid(n=1, k=10.000, x0=0.000, α=1.000, Q=4) [خطأ: 0.000456, ثقة: 0.70]
```

---

## 🎉 **الخلاصة**

**الوحدة الفنية Baserah** تحقق تكامل<|im_start|> كامل بين:

- ✅ **الرسم والأنيميشن** - إنشاء أشكال بصرية متحركة
- ✅ **الاستنباط والتحليل** - استنتاج المعادلات من البيانات  
- ✅ **عامل التكميم** - دعم الدوال المتقطعة
- ✅ **منهج Baserah النقي** - بدون مكتبات ذكاء اصطناعي

**هذه وحدة فنية متكاملة جاهزة للاستخدام في المشاريع المتقدمة!** 🚀
