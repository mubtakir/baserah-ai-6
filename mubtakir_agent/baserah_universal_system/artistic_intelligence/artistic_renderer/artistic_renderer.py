#!/usr/bin/env python3
# artistic_renderer.py - محرك الرسم والأنيميشن للوحدة الفنية Baserah

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from .baserah_core import (
    baserah_sigmoid, baserah_linear, baserah_quantum_sigmoid, baserah_equation
)

class BaserahArtisticRenderer:
    """
    محرك الرسم والأنيميشن Baserah
    يرسم الأشكال والأنيميشن باستخدام معادلات الشكل العام
    """
    
    def __init__(self):
        self.figure_size = (12, 8)
        self.dpi = 100
        self.animation_interval = 50  # milliseconds
        
    def render_equation(self, components, x_range=(-5, 5), num_points=1000, 
                       title="معادلة Baserah", show_components=True):
        """
        رسم معادلة الشكل العام
        
        Args:
            components: مكونات المعادلة
            x_range: نطاق x
            num_points: عدد النقاط
            title: عنوان الرسم
            show_components: إظهار المكونات منفصلة
        """
        x = np.linspace(x_range[0], x_range[1], num_points)
        
        # حساب المعادلة الكاملة
        y_total = np.array([baserah_equation(xi, components) for xi in x])
        
        plt.figure(figsize=self.figure_size, dpi=self.dpi)
        
        if show_components:
            # رسم كل مكون منفصل
            colors = ['red', 'blue', 'green', 'orange', 'purple']
            
            for i, component in enumerate(components):
                comp_type = component['type']
                params = component['params']
                color = colors[i % len(colors)]
                
                if comp_type == 'sigmoid':
                    y_comp = np.array([baserah_sigmoid(xi, **params) for xi in x])
                    plt.plot(x, y_comp, '--', color=color, alpha=0.6, 
                            label=f'سيجمويد {i+1}', linewidth=1)
                            
                elif comp_type == 'linear':
                    y_comp = np.array([baserah_linear(xi, **params) for xi in x])
                    plt.plot(x, y_comp, ':', color=color, alpha=0.6, 
                            label=f'خطي {i+1}', linewidth=1)
                            
                elif comp_type == 'quantum_sigmoid':
                    y_comp = np.array([baserah_quantum_sigmoid(xi, **params) for xi in x])
                    plt.plot(x, y_comp, '-.', color=color, alpha=0.6, 
                            label=f'مكمم {i+1}', linewidth=1)
        
        # رسم المعادلة الكاملة
        plt.plot(x, y_total, 'black', linewidth=3, label='المعادلة الكاملة')
        
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # إضافة معلومات المعادلة
        info_text = f"عدد المكونات: {len(components)}\n"
        for i, comp in enumerate(components):
            comp_type = comp['type']
            if comp_type == 'sigmoid':
                params = comp['params']
                info_text += f"σ{i+1}: n={params.get('n',1)}, k={params.get('k',1):.2f}\n"
            elif comp_type == 'quantum_sigmoid':
                params = comp['params']
                info_text += f"Q{i+1}: Q={params.get('quantum_factor',1)}\n"
        
        plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes, 
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))
        
        plt.tight_layout()
        plt.show()
    
    def create_animated_equation(self, base_components, parameter_animations, 
                               x_range=(-5, 5), num_points=500, duration=5.0):
        """
        إنشاء أنيميشن لمعادلة متحركة
        
        Args:
            base_components: المكونات الأساسية
            parameter_animations: قاموس التحريك للمعاملات
            duration: مدة الأنيميشن بالثواني
        """
        x = np.linspace(x_range[0], x_range[1], num_points)
        
        fig, ax = plt.subplots(figsize=self.figure_size, dpi=self.dpi)
        line, = ax.plot([], [], 'b-', linewidth=3)
        
        ax.set_xlim(x_range)
        ax.set_ylim(-2, 2)  # سيتم تعديلها تلقائياً
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('معادلة Baserah متحركة')
        ax.grid(True, alpha=0.3)
        
        # حساب عدد الإطارات
        frames = int(duration * 1000 / self.animation_interval)
        
        def animate(frame):
            t = frame / frames  # نسبة الوقت (0 إلى 1)
            
            # تحديث المعاملات حسب الأنيميشن
            current_components = []
            for i, component in enumerate(base_components):
                current_comp = component.copy()
                params = current_comp['params'].copy()
                
                # تطبيق التحريك
                if i in parameter_animations:
                    for param_name, (start_val, end_val) in parameter_animations[i].items():
                        # تحريك خطي
                        current_val = start_val + (end_val - start_val) * t
                        params[param_name] = current_val
                
                current_comp['params'] = params
                current_components.append(current_comp)
            
            # حساب القيم الجديدة
            y = np.array([baserah_equation(xi, current_components) for xi in x])
            
            # تحديث الرسم
            line.set_data(x, y)
            
            # تعديل نطاق y تلقائياً
            if len(y) > 0:
                y_min, y_max = np.min(y), np.max(y)
                margin = (y_max - y_min) * 0.1
                ax.set_ylim(y_min - margin, y_max + margin)
            
            return line,
        
        # إنشاء الأنيميشن
        anim = animation.FuncAnimation(fig, animate, frames=frames, 
                                     interval=self.animation_interval, 
                                     blit=True, repeat=True)
        
        plt.show()
        return anim
    
    def render_quantum_levels_demo(self, x_range=(-3, 3), num_points=300):
        """
        عرض مستويات التكميم المختلفة
        """
        x = np.linspace(x_range[0], x_range[1], num_points)
        quantum_levels = [1, 2, 4, 8, 16]
        
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.flatten()
        
        for i, q_level in enumerate(quantum_levels):
            ax = axes[i]
            
            # سيجمويد عادي
            y_normal = np.array([baserah_sigmoid(xi, 1, 2, 0, 1) for xi in x])
            
            # سيجمويد مكمم
            y_quantum = np.array([baserah_quantum_sigmoid(xi, 1, 2, 0, 1, q_level) for xi in x])
            
            ax.plot(x, y_normal, 'b--', alpha=0.5, label='عادي')
            ax.plot(x, y_quantum, 'r-', linewidth=2, label=f'مكمم Q={q_level}')
            
            ax.set_title(f'عامل التكميم = {q_level}')
            ax.set_xlabel('x')
            ax.set_ylabel('f(x)')
            ax.grid(True, alpha=0.3)
            ax.legend()
            
            # إضافة معلومات
            unique_vals = len(np.unique(np.round(y_quantum, 3)))
            ax.text(0.05, 0.95, f'{unique_vals} مستوى', 
                   transform=ax.transAxes, fontsize=10,
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
        
        # إخفاء المحور الأخير إذا كان فارغاً
        if len(quantum_levels) < len(axes):
            axes[-1].set_visible(False)
        
        plt.suptitle('عرض مستويات التكميم المختلفة', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    def create_artistic_pattern(self, pattern_type="heart", animate=True):
        """
        إنشاء أنماط فنية باستخدام معادلات Baserah
        """
        if pattern_type == "heart":
            return self._create_heart_pattern(animate)
        elif pattern_type == "wave":
            return self._create_wave_pattern(animate)
        elif pattern_type == "flower":
            return self._create_flower_pattern(animate)
        elif pattern_type == "spiral":
            return self._create_spiral_pattern(animate)
        else:
            print(f"نمط غير معروف: {pattern_type}")
    
    def _create_heart_pattern(self, animate=True):
        """إنشاء نمط قلب نابض"""
        t = np.linspace(0, 2*np.pi, 1000)
        
        if animate:
            fig, ax = plt.subplots(figsize=self.figure_size)
            
            def animate_heart(frame):
                ax.clear()
                
                # معاملات متحركة
                pulse = 1 + 0.3 * baserah_sigmoid(frame/10, 1, 1, 0, 1)
                
                # معادلة القلب باستخدام Baserah
                x_heart = []
                y_heart = []
                
                for ti in t:
                    # استخدام مكونات Baserah لرسم القلب
                    x_comp = pulse * (16 * baserah_sigmoid(ti, 3, 1, 0, 1) - 
                                    13 * baserah_sigmoid(ti, 1, 2, 0, 0.5))
                    y_comp = pulse * (13 * baserah_sigmoid(ti, 1, 1.5, 0, 1) - 
                                    6 * baserah_sigmoid(ti, 2, 1, 0, 0.3))
                    
                    x_heart.append(x_comp)
                    y_heart.append(y_comp)
                
                ax.plot(x_heart, y_heart, 'red', linewidth=3)
                ax.set_xlim(-20, 20)
                ax.set_ylim(-15, 15)
                ax.set_aspect('equal')
                ax.set_title('قلب نابض Baserah', fontsize=16)
                ax.grid(True, alpha=0.3)
            
            anim = animation.FuncAnimation(fig, animate_heart, frames=100, 
                                         interval=100, repeat=True)
            plt.show()
            return anim
        else:
            # رسم ثابت
            x_heart = []
            y_heart = []
            
            for ti in t:
                x_comp = 16 * baserah_sigmoid(ti, 3, 1, 0, 1) - 13 * baserah_sigmoid(ti, 1, 2, 0, 0.5)
                y_comp = 13 * baserah_sigmoid(ti, 1, 1.5, 0, 1) - 6 * baserah_sigmoid(ti, 2, 1, 0, 0.3)
                
                x_heart.append(x_comp)
                y_heart.append(y_comp)
            
            plt.figure(figsize=self.figure_size)
            plt.plot(x_heart, y_heart, 'red', linewidth=3)
            plt.title('قلب Baserah', fontsize=16)
            plt.axis('equal')
            plt.grid(True, alpha=0.3)
            plt.show()
    
    def _create_wave_pattern(self, animate=True):
        """إنشاء نمط موجي معقد"""
        x = np.linspace(-10, 10, 1000)
        
        # مكونات الموجة
        components = [
            {'type': 'sigmoid', 'params': {'n': 1, 'k': 0.5, 'x0': 0, 'alpha': 1}},
            {'type': 'quantum_sigmoid', 'params': {'n': 1, 'k': 1, 'x0': 2, 'alpha': 0.5, 'quantum_factor': 8}},
            {'type': 'linear', 'params': {'beta': 0.1, 'gamma': 0}}
        ]
        
        if animate:
            # أنيميشن الموجة
            parameter_animations = {
                0: {'k': (0.5, 2.0), 'x0': (0, 3)},
                1: {'quantum_factor': (4, 16)}
            }
            
            return self.create_animated_equation(components, parameter_animations, 
                                               x_range=(-10, 10), duration=6.0)
        else:
            # رسم ثابت
            self.render_equation(components, x_range=(-10, 10), 
                               title="موجة Baserah معقدة")
    
    def _create_flower_pattern(self, animate=True):
        """إنشاء نمط زهرة"""
        theta = np.linspace(0, 4*np.pi, 1000)
        
        if animate:
            fig, ax = plt.subplots(figsize=self.figure_size)
            
            def animate_flower(frame):
                ax.clear()
                
                # معاملات متحركة
                bloom = baserah_sigmoid(frame/20, 1, 0.5, 0, 1)
                
                r = []
                for t in theta:
                    # استخدام معادلات Baserah للزهرة
                    radius = bloom * (2 + baserah_sigmoid(t, 1, 3, 0, 1) + 
                                    0.5 * baserah_quantum_sigmoid(t, 1, 6, 0, 1, 8))
                    r.append(radius)
                
                x_flower = [r[i] * math.cos(theta[i]) for i in range(len(theta))]
                y_flower = [r[i] * math.sin(theta[i]) for i in range(len(theta))]
                
                ax.plot(x_flower, y_flower, 'magenta', linewidth=2)
                ax.set_xlim(-4, 4)
                ax.set_ylim(-4, 4)
                ax.set_aspect('equal')
                ax.set_title('زهرة متفتحة Baserah', fontsize=16)
                ax.grid(True, alpha=0.3)
            
            anim = animation.FuncAnimation(fig, animate_flower, frames=100, 
                                         interval=150, repeat=True)
            plt.show()
            return anim
        else:
            # رسم ثابت
            r = []
            for t in theta:
                radius = 2 + baserah_sigmoid(t, 1, 3, 0, 1) + 0.5 * baserah_quantum_sigmoid(t, 1, 6, 0, 1, 8)
                r.append(radius)
            
            x_flower = [r[i] * math.cos(theta[i]) for i in range(len(theta))]
            y_flower = [r[i] * math.sin(theta[i]) for i in range(len(theta))]
            
            plt.figure(figsize=self.figure_size)
            plt.plot(x_flower, y_flower, 'magenta', linewidth=2)
            plt.title('زهرة Baserah', fontsize=16)
            plt.axis('equal')
            plt.grid(True, alpha=0.3)
            plt.show()
    
    def _create_spiral_pattern(self, animate=True):
        """إنشاء نمط حلزوني"""
        t = np.linspace(0, 6*np.pi, 1000)
        
        # حلزون باستخدام معادلات Baserah
        components_r = [
            {'type': 'linear', 'params': {'beta': 0.5, 'gamma': 1}},
            {'type': 'sigmoid', 'params': {'n': 1, 'k': 0.2, 'x0': np.pi, 'alpha': 2}}
        ]
        
        r = [baserah_equation(ti, components_r) for ti in t]
        x_spiral = [r[i] * math.cos(t[i]) for i in range(len(t))]
        y_spiral = [r[i] * math.sin(t[i]) for i in range(len(t))]
        
        plt.figure(figsize=self.figure_size)
        plt.plot(x_spiral, y_spiral, 'blue', linewidth=2)
        plt.title('حلزون Baserah', fontsize=16)
        plt.axis('equal')
        plt.grid(True, alpha=0.3)
        plt.show()
