#!/usr/bin/env python3
# baserah_core.py - النواة النقية لفكرة Baserah Universal (نسخة الوحدة الفنية)
# الاعتماد فقط على: دوال السيجمويد + الخطوط المستقيمة + عامل التكميم

import math

# === النواة الرياضية النقية لفكرة Baserah ===

def baserah_sigmoid(x, n=1, k=1.0, x0=0.0, alpha=1.0):
    """
    دالة السيجمويد المعدلة - النواة الأساسية لفكرة Baserah
    σₙ(x; k, x₀, n, α) = α * (1 / (1 + e^(-k*(x - x₀)^n)))
    """
    try:
        term = x - x0
        
        # التعامل مع الأس
        if n % 2 == 0:
            powered_term = abs(term) ** n
        else:
            powered_term = (term ** n) if term >= 0 else -(abs(term) ** n)
        
        # حساب السيجمويد مع تجنب overflow
        exp_arg = -k * powered_term
        if exp_arg > 700:
            return 0.0
        elif exp_arg < -700:
            return alpha
        else:
            return alpha / (1 + math.exp(exp_arg))
    except:
        return alpha * 0.5

def baserah_linear(x, beta=1.0, gamma=0.0):
    """
    المكون الخطي النقي - الجزء الثاني من فكرة Baserah
    f(x) = β*x + γ
    """
    return beta * x + gamma

def baserah_quantum_sigmoid(x, n=1, k=1.0, x0=0.0, alpha=1.0, quantum_factor=1.0):
    """
    السيجمويد المكمم - عامل التكميم n = 1K, 2K, 3K...
    """
    # حساب السيجمويد الأساسي
    base_value = baserah_sigmoid(x, n, k, x0, alpha)
    
    # تطبيق التكميم
    if quantum_factor <= 1.0:
        return base_value
    
    # التكميم إلى مستويات منفصلة
    quantized = round(base_value * quantum_factor) / quantum_factor
    return quantized

def baserah_equation(x, components):
    """
    معادلة Baserah الأساسية النقية:
    f̂(x) = Σ(αᵢ · σₙᵢ(x; kᵢ, x₀ᵢ) + βᵢx + γᵢ)
    """
    result = 0.0
    
    for component in components:
        comp_type = component.get('type', 'sigmoid')
        params = component.get('params', {})
        
        if comp_type == 'sigmoid':
            result += baserah_sigmoid(x, **params)
        elif comp_type == 'linear':
            result += baserah_linear(x, **params)
        elif comp_type == 'quantum_sigmoid':
            result += baserah_quantum_sigmoid(x, **params)
    
    return result
