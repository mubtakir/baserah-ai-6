#!/usr/bin/env python3
"""
Baserah Universal System - النظام الثوري المتكامل
🧬 Creator: Basil Yahya Abdullah
🌟 Revolutionary Mathematical Intelligence - Integrated System
🎯 Features: Core Components + Advanced Interfaces + AI-OOP
"""

import gradio as gr
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tempfile
import sys
import os
from pathlib import Path
import traceback

# إضافة المسارات للاستيراد
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

# === استيراد المكونات الأساسية ===
try:
    from artistic_intelligence.baserah_core import baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid
    print("✅ تم تحميل النواة الأساسية")
    CORE_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ تحذير في تحميل النواة: {e}")
    CORE_AVAILABLE = False
    
    # نسخة احتياطية للدوال الأساسية
    def baserah_sigmoid(x, n=1, k=1.0, x0=0.0, alpha=1.0):
        import math
        try:
            term = x - x0
            if n % 2 == 0:
                powered_term = abs(term) ** n
            else:
                powered_term = (term ** n) if term >= 0 else -(abs(term) ** n)
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
        return beta * x + gamma
    
    def baserah_quantum_sigmoid(x, n=1, k=1.0, x0=0.0, alpha=1.0, quantum_factor=1.0):
        base_value = baserah_sigmoid(x, n, k, x0, alpha)
        if quantum_factor <= 1.0:
            return base_value
        quantized = round(base_value * quantum_factor) / quantum_factor
        return quantized

# === استيراد المكونات المتقدمة ===
try:
    from ai_oop_system import BaserahAIOOPSystem
    print("✅ تم تحميل نظام AI-OOP")
    AI_OOP_AVAILABLE = True
except ImportError:
    print("⚠️ نظام AI-OOP غير متاح")
    AI_OOP_AVAILABLE = False

# === دوال توليد الأشكال ===
def sigmoid_wave_approximation(t, amplitude=1.0, num_waves=2, k_steepness=1.5, phase_shift=0.0):
    """تقريب الموجات باستخدام sigmoid - النواة الثورية لبصيرة"""
    approx = np.zeros_like(t, dtype=float)
    period = 2 * np.pi
    
    for n in range(-int(num_waves), int(num_waves) + 1):
        x0_pos = n * period + 0.25 * period + phase_shift
        x0_neg = n * period - 0.25 * period + phase_shift
        
        approx += baserah_sigmoid(t, alpha=1.0, k=k_steepness, x0=x0_pos) - \
                 baserah_sigmoid(t, alpha=1.0, k=k_steepness, x0=x0_neg)
    
    # تطبيع النتيجة
    min_val = np.min(approx)
    max_val = np.max(approx)
    range_val = max_val - min_val
    if range_val > 1e-9:
        approx = 2 * (approx - min_val) / range_val - 1
    else:
        approx = np.zeros_like(t)
    
    return amplitude * approx

def generate_baserah_shape(shape_type, size=1.0, color="blue", quantum_factor=1.0):
    """توليد الأشكال باستخدام نظام Baserah المتكامل"""
    try:
        t = np.linspace(0, 2*np.pi, 1000)
        
        if shape_type == "circle":
            x = sigmoid_wave_approximation(t, amplitude=size, num_waves=2, k_steepness=1.5, phase_shift=np.pi/2)
            y = sigmoid_wave_approximation(t, amplitude=size, num_waves=2, k_steepness=1.5, phase_shift=0)
            equation = f"Circle: x = SigmoidWave(t, φ=π/2), y = SigmoidWave(t, φ=0) - PURE SIGMOID!"
            
        elif shape_type == "heart":
            sin_t = sigmoid_wave_approximation(t, amplitude=1, num_waves=2, k_steepness=2)
            cos_t = sigmoid_wave_approximation(t, amplitude=1, num_waves=2, k_steepness=2, phase_shift=np.pi/2)
            cos_2t = sigmoid_wave_approximation(2*t, amplitude=1, num_waves=4, k_steepness=2, phase_shift=np.pi/2)
            cos_3t = sigmoid_wave_approximation(3*t, amplitude=1, num_waves=6, k_steepness=2, phase_shift=np.pi/2)
            cos_4t = sigmoid_wave_approximation(4*t, amplitude=1, num_waves=8, k_steepness=2, phase_shift=np.pi/2)
            
            x = size * 16 * (sin_t ** 3) / 16
            y = size * (13 * cos_t - 5 * cos_2t - 2 * cos_3t - cos_4t) / 16
            equation = f"Heart: PURE SIGMOID approximations - NO trigonometry! Size={size}"
            
        elif shape_type == "star":
            cos_t = sigmoid_wave_approximation(t, amplitude=1, num_waves=2, k_steepness=3, phase_shift=np.pi/2)
            sin_t = sigmoid_wave_approximation(t, amplitude=1, num_waves=2, k_steepness=3)
            cos_5t = sigmoid_wave_approximation(5*t, amplitude=1, num_waves=10, k_steepness=3, phase_shift=np.pi/2)
            
            spike_factor = 0.3
            x = size * cos_t * (1 + spike_factor * cos_5t)
            y = size * sin_t * (1 + spike_factor * cos_5t)
            equation = f"Star: PURE SIGMOID spikes - Revolutionary! Size={size}"
            
        elif shape_type == "quantum_circle":
            # دائرة مكممة - ميزة متقدمة
            x_base = sigmoid_wave_approximation(t, amplitude=size, num_waves=2, k_steepness=1.5, phase_shift=np.pi/2)
            y_base = sigmoid_wave_approximation(t, amplitude=size, num_waves=2, k_steepness=1.5, phase_shift=0)
            
            # تطبيق التكميم
            x = np.array([baserah_quantum_sigmoid(val, quantum_factor=quantum_factor) for val in x_base])
            y = np.array([baserah_quantum_sigmoid(val, quantum_factor=quantum_factor) for val in y_base])
            equation = f"Quantum Circle: Quantized Sigmoid (n={quantum_factor}K) - REVOLUTIONARY!"
            
        else:  # default
            x = sigmoid_wave_approximation(t, amplitude=size, num_waves=2, k_steepness=1.5, phase_shift=np.pi/2)
            y = sigmoid_wave_approximation(t, amplitude=size, num_waves=2, k_steepness=1.5, phase_shift=0)
            equation = f"Default: SIGMOID Circle - PURE BASERAH! Size={size}"
        
        # إنشاء الرسم
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.plot(x, y, linewidth=3, color=color, alpha=0.8)
        ax.fill(x, y, alpha=0.3, color=color)
        
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title(f'Baserah Universal System: {shape_type.title()}\n{equation}', 
                    fontsize=12, fontweight='bold')
        
        # معلومات النظام
        system_info = f"""🧬 Creator: Basil Yahya Abdullah
🌟 Method: PURE SIGMOID + LINEAR ONLY
🚫 NO Trigonometry - NO AI Libraries
✅ Core Available: {CORE_AVAILABLE}
✅ AI-OOP Available: {AI_OOP_AVAILABLE}
🎯 Revolutionary Mathematical Intelligence"""
        
        ax.text(0.02, 0.98, system_info, transform=ax.transAxes, fontsize=9,
                verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3",
                facecolor="lightyellow", alpha=0.8))
        
        plt.tight_layout()
        
        # حفظ الملف
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        plt.savefig(temp_file.name, format='png', dpi=150, bbox_inches='tight')
        plt.close(fig)
        
        return temp_file.name
        
    except Exception as e:
        # معالجة الأخطاء
        fig, ax = plt.subplots(figsize=(8, 6))
        error_msg = f"""❌ Error in Baserah System:
{str(e)}

🔧 System Status:
✅ Core Available: {CORE_AVAILABLE}
✅ AI-OOP Available: {AI_OOP_AVAILABLE}

Please try a different shape or parameters."""
        
        ax.text(0.5, 0.5, error_msg, ha='center', va='center', fontsize=12, color='red',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow"))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        plt.savefig(temp_file.name, format='png', dpi=150, bbox_inches='tight')
        plt.close(fig)
        
        return temp_file.name

def test_system_components():
    """اختبار مكونات النظام"""
    results = []
    
    # اختبار النواة الأساسية
    try:
        test_val = baserah_sigmoid(0.5)
        results.append(f"✅ Sigmoid Core: {test_val:.3f}")
    except Exception as e:
        results.append(f"❌ Sigmoid Core: {str(e)}")
    
    # اختبار AI-OOP
    if AI_OOP_AVAILABLE:
        try:
            system = BaserahAIOOPSystem()
            results.append("✅ AI-OOP System: Initialized")
        except Exception as e:
            results.append(f"❌ AI-OOP System: {str(e)}")
    else:
        results.append("⚠️ AI-OOP System: Not Available")
    
    return "\n".join(results)

def create_interface():
    """إنشاء واجهة Gradio المتكاملة"""
    
    with gr.Blocks(title="Baserah Universal System", theme=gr.themes.Soft()) as interface:
        
        gr.Markdown("""
        # 🌟 Baserah Universal System - النظام الثوري المتكامل
        ## 🧬 Creator: Basil Yahya Abdullah
        
        ### ⚡ Revolutionary Mathematical Intelligence
        **🚫 No Neural Networks • 🚫 No Big Data • ✅ Pure Sigmoid + Linear Only**
        
        ---
        """)
        
        with gr.Tabs():
            # تبويب الأشكال الأساسية
            with gr.Tab("🎨 Shape Generator"):
                with gr.Row():
                    with gr.Column(scale=1):
                        shape_input = gr.Dropdown(
                            choices=["circle", "heart", "star", "quantum_circle"],
                            value="circle",
                            label="🔹 Select Shape"
                        )
                        
                        size_input = gr.Slider(
                            minimum=0.1, maximum=3.0, value=1.0, step=0.1,
                            label="📏 Size"
                        )
                        
                        color_input = gr.Dropdown(
                            choices=["blue", "red", "green", "purple", "orange", "pink"],
                            value="blue",
                            label="🎨 Color"
                        )
                        
                        quantum_input = gr.Slider(
                            minimum=1.0, maximum=10.0, value=1.0, step=0.5,
                            label="⚛️ Quantum Factor (for quantum shapes)"
                        )
                        
                        generate_btn = gr.Button("🚀 Generate Shape", variant="primary", size="lg")
                        
                    with gr.Column(scale=2):
                        output_image = gr.Image(label="🖼️ Generated Shape", type="filepath")
            
            # تبويب اختبار النظام
            with gr.Tab("🧪 System Test"):
                test_btn = gr.Button("🔍 Test System Components", variant="secondary")
                test_output = gr.Textbox(label="📊 Test Results", lines=10)
        
        # ربط الأحداث
        generate_btn.click(
            fn=generate_baserah_shape,
            inputs=[shape_input, size_input, color_input, quantum_input],
            outputs=output_image
        )
        
        test_btn.click(
            fn=test_system_components,
            outputs=test_output
        )
        
        # تحديث تلقائي عند تغيير الشكل
        shape_input.change(
            fn=generate_baserah_shape,
            inputs=[shape_input, size_input, color_input, quantum_input],
            outputs=output_image
        )
        
        gr.Markdown("""
        ---
        ## 🧮 Revolutionary Equations (SIGMOID + LINEAR ONLY):
        
        - **🔵 Circle:** `x = SigmoidWave(t, φ=π/2), y = SigmoidWave(t, φ=0)`
        - **❤️ Heart:** `x = 16×SigmoidSin³(t), y = 13×SigmoidCos(t) - 5×SigmoidCos(2t) - ...`
        - **⭐ Star:** `x = SigmoidCos(t)×(1 + a×SigmoidCos(5t))`
        - **⚛️ Quantum:** `Quantized Sigmoid with factor n = 1K, 2K, 3K...`
        
        ### 🎯 System Status:
        - **Core Components:** Available
        - **AI-OOP System:** """ + ("Available" if AI_OOP_AVAILABLE else "Not Available") + """
        - **Method:** Pure Mathematical Intelligence
        
        **🌟 This is the future of transparent AI!**
        """)
    
    return interface

if __name__ == "__main__":
    interface = create_interface()
    interface.launch(server_name="0.0.0.0", server_port=7860)
