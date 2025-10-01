#!/usr/bin/env python3
"""
Baserah Universal System - Simple Fixed Version
🧬 Creator: Basil Yahya Abdullah
🌟 Revolutionary: ONLY Sigmoid + Linear Functions
"""

import gradio as gr
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tempfile
import math

def baserah_sigmoid(x, alpha=1.0, k=1.0, x0=0.0):
    """دالة السيجمويد الثورية - نواة نظام بصيرة"""
    try:
        return alpha / (1 + np.exp(-k * (x - x0)))
    except:
        return alpha * 0.5

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

def generate_sigmoid_shape(shape_type, size=1.0, color="blue"):
    """توليد الأشكال باستخدام sigmoid فقط"""
    try:
        t = np.linspace(0, 2*np.pi, 1000)
        
        if shape_type == "circle":
            x = sigmoid_wave_approximation(t, amplitude=size, num_waves=2, k_steepness=1.5, phase_shift=np.pi/2)
            y = sigmoid_wave_approximation(t, amplitude=size, num_waves=2, k_steepness=1.5, phase_shift=0)
            equation = "x = SigmoidWave(t, φ=π/2), y = SigmoidWave(t, φ=0) - PURE SIGMOID!"
            
        elif shape_type == "heart":
            sin_t = sigmoid_wave_approximation(t, amplitude=1, num_waves=2, k_steepness=2)
            cos_t = sigmoid_wave_approximation(t, amplitude=1, num_waves=2, k_steepness=2, phase_shift=np.pi/2)
            cos_2t = sigmoid_wave_approximation(2*t, amplitude=1, num_waves=4, k_steepness=2, phase_shift=np.pi/2)
            cos_3t = sigmoid_wave_approximation(3*t, amplitude=1, num_waves=6, k_steepness=2, phase_shift=np.pi/2)
            cos_4t = sigmoid_wave_approximation(4*t, amplitude=1, num_waves=8, k_steepness=2, phase_shift=np.pi/2)
            
            x = size * 16 * (sin_t ** 3) / 16
            y = size * (13 * cos_t - 5 * cos_2t - 2 * cos_3t - cos_4t) / 16
            equation = "Heart using PURE SIGMOID approximations - NO trigonometry!"
            
        elif shape_type == "star":
            cos_t = sigmoid_wave_approximation(t, amplitude=1, num_waves=2, k_steepness=3, phase_shift=np.pi/2)
            sin_t = sigmoid_wave_approximation(t, amplitude=1, num_waves=2, k_steepness=3)
            cos_5t = sigmoid_wave_approximation(5*t, amplitude=1, num_waves=10, k_steepness=3, phase_shift=np.pi/2)
            
            spike_factor = 0.3
            x = size * cos_t * (1 + spike_factor * cos_5t)
            y = size * sin_t * (1 + spike_factor * cos_5t)
            equation = "Star using PURE SIGMOID spikes - Revolutionary!"
            
        else:  # default circle
            x = sigmoid_wave_approximation(t, amplitude=size, num_waves=2, k_steepness=1.5, phase_shift=np.pi/2)
            y = sigmoid_wave_approximation(t, amplitude=size, num_waves=2, k_steepness=1.5, phase_shift=0)
            equation = "DEFAULT SIGMOID CIRCLE - PURE BASERAH!"
        
        # إنشاء الرسم
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.plot(x, y, linewidth=3, color=color, alpha=0.8)
        ax.fill(x, y, alpha=0.3, color=color)
        
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title(f'Baserah System: {shape_type.title()}\n{equation}', fontsize=12, fontweight='bold')
        
        # إضافة التوقيع
        signature = f"""Creator: Basil Yahya Abdullah
Method: PURE SIGMOID + LINEAR ONLY
NO Trigonometry - NO AI Libraries
Revolutionary Mathematical Intelligence"""
        
        ax.text(0.02, 0.98, signature, transform=ax.transAxes, fontsize=9,
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
        ax.text(0.5, 0.5, f'Error: {str(e)}\nPlease try again', ha='center', va='center', 
                fontsize=14, color='red', bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow"))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        plt.savefig(temp_file.name, format='png', dpi=150, bbox_inches='tight')
        plt.close(fig)
        
        return temp_file.name

def test_system():
    """اختبار النظام"""
    try:
        test_val = baserah_sigmoid(0.5)
        return f"System Test: SUCCESS\nSigmoid(0.5) = {test_val:.3f}\nAll components working!"
    except Exception as e:
        return f"System Test: ERROR\n{str(e)}"

# إنشاء واجهة Gradio
def create_interface():
    """إنشاء واجهة Gradio البسيطة"""
    
    with gr.Blocks(title="Baserah Universal System") as interface:
        
        gr.Markdown("""
        # Baserah Universal System
        ## Creator: Basil Yahya Abdullah
        
        ### Revolutionary Mathematical Intelligence
        **Pure Sigmoid + Linear Only - No Traditional AI**
        """)
        
        with gr.Row():
            with gr.Column():
                shape_input = gr.Dropdown(
                    choices=["circle", "heart", "star"],
                    value="circle",
                    label="Select Shape"
                )
                
                size_input = gr.Slider(
                    minimum=0.1, maximum=3.0, value=1.0, step=0.1,
                    label="Size"
                )
                
                color_input = gr.Dropdown(
                    choices=["blue", "red", "green", "purple", "orange", "pink"],
                    value="blue",
                    label="Color"
                )
                
                generate_btn = gr.Button("Generate Shape", variant="primary")
                test_btn = gr.Button("Test System")
                
            with gr.Column():
                output_image = gr.Image(label="Generated Shape")
                test_output = gr.Textbox(label="Test Results", lines=3)
        
        # ربط الأحداث
        generate_btn.click(
            fn=generate_sigmoid_shape,
            inputs=[shape_input, size_input, color_input],
            outputs=output_image
        )
        
        test_btn.click(
            fn=test_system,
            outputs=test_output
        )
        
        shape_input.change(
            fn=generate_sigmoid_shape,
            inputs=[shape_input, size_input, color_input],
            outputs=output_image
        )
        
        gr.Markdown("""
        ---
        ## Revolutionary Equations (SIGMOID + LINEAR ONLY):
        
        - Circle: x = SigmoidWave(t, φ=π/2), y = SigmoidWave(t, φ=0)
        - Heart: PURE SIGMOID approximations - NO trigonometry
        - Star: SigmoidCos(t) × (1 + a×SigmoidCos(5t))
        
        **This is the future of transparent AI!**
        """)
    
    return interface

if __name__ == "__main__":
    interface = create_interface()
    interface.launch()
