# gse_math_components.py
import numpy as np

# --- 1. المكونات الرياضية الأساسية ---
def generalized_sigmoid(x, n=1, k=1.0, x0=0.0, alpha=1.0):
    """
    دالة السيجمويد المعدلة بعامل التقطيع n ومعامل الوزن alpha.
    sigma_n(x; k, x0, n, alpha) = alpha * (1 / (1 + e^(-k*(x - x0)^n)))
    """
    term_val = x - x0
    k_float = float(k) # تأكد أن k هو float

    # التعامل مع k قريب جدًا من الصفر بشكل منفصل لتجنب مشاكل حسابية لاحقة
    if abs(k_float) < 1e-9: 
        return alpha * 0.5 * np.ones_like(x if isinstance(x, np.ndarray) else 1.0)

    # التعامل مع powered_term بحذر أكثر للأسس الزوجية والأعداد السالبة
    if n % 2 == 0:
        powered_term = np.abs(term_val) ** n # لـ n زوجي، النتيجة دائمًا موجبة أو صفر
    else:
        # لـ n فردي، term_val ** n يجب أن يعمل بشكل صحيح مع الإشارات
        # ولكن استخدام sign و abs قد يكون أكثر أمانًا للقيم المتطرفة أو n غير صحيح (نادر)
        powered_term = np.sign(term_val) * (np.abs(term_val) ** n) if k_float != 0 else np.zeros_like(term_val)
    
    with np.errstate(over='ignore', under='ignore', invalid='ignore'): # invalid لتجاهل 0**0 إذا حدث
        exp_argument = -k_float * powered_term
        exp_argument_clipped = np.clip(exp_argument, -700, 700) # تجنب القيم المتطرفة في np.exp
        sigmoid_base = 1 / (1 + np.exp(exp_argument_clipped))
        
        # إذا كان الناتج لا يزال nan (نادر جدًا بعد clip إلا إذا كان الإدخال x هو nan)
        # استخدم 0.5 كقيمة افتراضية آمنة
        final_sigmoid_val = np.nan_to_num(sigmoid_base, nan=0.5) 
    return alpha * final_sigmoid_val

def linear_component(t, beta=1.0, gamma=0.0):
    """
    المكون الخطي: beta * t + gamma
    """
    return beta * t + gamma

def quantized_sigmoid(x, n=1, k=1.0, x0=0.0, alpha=1.0, quantum_factor=1.0):
    """
    دالة السيجمويد المكممة - تطوير مهم لعامل التكميم
    
    عامل التكميم يسمح بإنشاء انقطاعات وقفزات كمية:
    - quantum_factor = 1.0: سيجمويد عادي
    - quantum_factor = 2.0: قفزات بمضاعفات 0.5
    - quantum_factor = 3.0: قفزات بمضاعفات 0.33
    - quantum_factor = K: قفزات بمضاعفات 1/K
    
    Args:
        x: المتغير المستقل
        n: عامل التقطيع (1 للناعم، أكبر للحاد)
        k: معامل الحدة
        x0: نقطة المنتصف
        alpha: معامل الوزن
        quantum_factor: عامل التكميم (K في n=1K, 2K, 3K...)
    
    Returns:
        القيمة المكممة للسيجمويد
    """
    # حساب السيجمويد العادي أولاً
    base_sigmoid = generalized_sigmoid(x, n, k, x0, alpha)
    
    # تطبيق التكميم
    if quantum_factor <= 1.0:
        return base_sigmoid
    
    # تكميم القيمة إلى مستويات منفصلة
    quantized_levels = np.round(base_sigmoid * quantum_factor) / quantum_factor
    
    return quantized_levels

def stepped_sigmoid(x, n=1, k=1.0, x0=0.0, alpha=1.0, step_count=5):
    """
    دالة السيجمويد المدرجة - للدوال والأشكال المتقطعة
    
    تنشئ سلسلة من الدرجات (steps) بدلاً من الانتقال الناعم
    مفيدة جداً للدوال المتقطعة والأشكال الرقمية
    
    Args:
        step_count: عدد الدرجات المطلوبة
    """
    base_sigmoid = generalized_sigmoid(x, n, k, x0, alpha)
    
    # تحويل إلى درجات منفصلة
    step_size = 1.0 / step_count
    stepped_value = np.floor(base_sigmoid / step_size) * step_size
    
    return stepped_value

def fractal_sigmoid(x, n=1, k=1.0, x0=0.0, alpha=1.0, fractal_depth=3, scale_factor=0.5):
    """
    دالة السيجمويد الكسرية - للأشكال المعقدة والتفاصيل الدقيقة
    
    تضيف تفاصيل كسرية على مستويات مختلفة من الدقة
    """
    result = generalized_sigmoid(x, n, k, x0, alpha)
    
    # إضافة طبقات كسرية
    for depth in range(1, fractal_depth + 1):
        scale = scale_factor ** depth
        freq_multiplier = 2 ** depth
        
        fractal_component = generalized_sigmoid(
            x * freq_multiplier, n, k * freq_multiplier, x0, alpha * scale
        )
        
        result += fractal_component
    
    return result

def adaptive_sigmoid(x, n=1, k=1.0, x0=0.0, alpha=1.0, adaptation_rate=0.1):
    """
    دالة السيجمويد التكيفية - تتكيف مع خصائص الإدخال
    
    تغير معاملاتها بناءً على خصائص البيانات المحلية
    مفيدة للذكاء الاصطناعي التكيفي
    """
    # حساب التكيف المحلي
    local_variance = np.var(x) if isinstance(x, np.ndarray) else 0
    adapted_k = k * (1 + adaptation_rate * local_variance)
    adapted_alpha = alpha * (1 + adaptation_rate * np.abs(np.mean(x)) if isinstance(x, np.ndarray) else alpha)
    
    return generalized_sigmoid(x, n, adapted_k, x0, adapted_alpha)
