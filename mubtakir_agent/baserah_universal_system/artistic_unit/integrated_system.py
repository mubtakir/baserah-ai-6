#!/usr/bin/env python3
# integrated_system.py - النظام المتكامل للوحدة الفنية Baserah

import numpy as np
import matplotlib.pyplot as plt
try:
    from baserah_core import baserah_equation
    from inference_engine import BaserahInferenceEngine
    from artistic_renderer import BaserahArtisticRenderer
except ImportError:
    try:
        from .baserah_core import baserah_equation
        from .inference_engine import BaserahInferenceEngine
        from .artistic_renderer import BaserahArtisticRenderer
    except ImportError:
        # في حالة عدم توفر المكونات
        baserah_equation = None
        BaserahInferenceEngine = None
        BaserahArtisticRenderer = None
import sys
import os

# إضافة المسار للاستيراد من النظام الأم
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from knowledge_systems.shapes_database.shapes_database import BaserahShapesDatabase, ShapeDefinition, ShapeType, ComplexityLevel
    from revolutionary_intelligence.expert_explorer_system.expert_explorer.integrated_expert_explorer import BaserahIntegratedExpertExplorer
    from revolutionary_intelligence.expert_explorer_system.expert_explorer.adaptive_equations import BaserahAdaptiveEquation, AdaptationMode, EvolutionDirection
except ImportError:
    # في حالة عدم توفر قاعدة البيانات أو النظام الخبير
    BaserahShapesDatabase = None
    ShapeDefinition = None
    ShapeType = None
    ComplexityLevel = None
    BaserahIntegratedExpertExplorer = None
    BaserahAdaptiveEquation = None
    AdaptationMode = None
    EvolutionDirection = None

class BaserahIntegratedSystem:
    """
    النظام المتكامل للوحدة الفنية Baserah
    يجمع بين الرسم والاستنباط في نظام واحد متكامل
    """
    
    def __init__(self):
        # المكونات الأساسية مع فحص التوفر
        if BaserahInferenceEngine:
            self.inference_engine = BaserahInferenceEngine()
        else:
            self.inference_engine = None
            print("⚠️ محرك الاستنباط غير متاح")

        if BaserahArtisticRenderer:
            self.artistic_renderer = BaserahArtisticRenderer()
        else:
            self.artistic_renderer = None
            print("⚠️ المرسم الفني غير متاح")

        # الوراثة من النظام الأم وفقاً للسياسة الثورية
        self.mother_inheritance = None
        self.inherited_shapes = {}
        self.inherited_equations = {}
        self.inherited_coefficients = {}
        self.visual_adaptation_enabled = False

        # قاعدة بيانات الأشكال (ستورث من النظام الأم)
        self.shapes_database = None
        self.mother_shapes_database = None

        # النظام الخبير/المستكشف (سيورث من النظام الأم)
        self.expert_explorer_system = None
        self.inherited_adaptive_equations = []
        self.adaptive_intelligence_enabled = False

        print("🎨 تم تهيئة النظام المتكامل - جاهز للوراثة من النظام الأم")

    def inherit_shapes_database(self, shapes_database):
        """وراثة قاعدة بيانات الأشكال من النظام الأم."""

        if BaserahShapesDatabase and isinstance(shapes_database, BaserahShapesDatabase):
            self.shapes_database = shapes_database
            self.mother_shapes_database = shapes_database

            print(f"🗄️ تم وراثة قاعدة بيانات الأشكال: {len(shapes_database.shapes)} شكل")
            print(f"   📊 الأشكال الهندسية: {len(shapes_database.get_shapes_by_type(ShapeType.GEOMETRIC))}")
            print(f"   🌿 الأشكال العضوية: {len(shapes_database.get_shapes_by_type(ShapeType.ORGANIC))}")
            print(f"   📈 الأشكال الرياضية: {len(shapes_database.get_shapes_by_type(ShapeType.MATHEMATICAL))}")
            print(f"   🎨 الأشكال الفنية: {len(shapes_database.get_shapes_by_type(ShapeType.ARTISTIC))}")

            return True
        else:
            print("⚠️ قاعدة بيانات الأشكال غير متاحة")
            return False

    def inherit_expert_explorer_system(self, expert_explorer_system):
        """وراثة النظام الخبير/المستكشف من النظام الأم للتكيف الذكي."""

        if expert_explorer_system and hasattr(expert_explorer_system, 'adaptive_equations'):
            self.expert_explorer_system = expert_explorer_system
            self.inherited_adaptive_equations = expert_explorer_system.adaptive_equations.copy()
            self.adaptive_intelligence_enabled = True

            print(f"🧠🔍 تم وراثة النظام الخبير/المستكشف:")
            print(f"   📊 معادلات متكيفة: {len(self.inherited_adaptive_equations)}")
            print(f"   🎯 ذكاء التكيف: مفعل")
            print(f"   🧬 التطوير التكيفي: متاح")

            return True
        else:
            print("⚠️ النظام الخبير/المستكشف غير متاح للوراثة")
            return False

    def get_shape_from_database(self, shape_id: str):
        """الحصول على شكل من قاعدة البيانات."""

        if self.shapes_database:
            return self.shapes_database.get_shape(shape_id)
        elif self.mother_shapes_database:
            return self.mother_shapes_database.get_shape(shape_id)
        else:
            print("⚠️ قاعدة بيانات الأشكال غير متاحة")
            return None

    def search_shapes_in_database(self, query: str):
        """البحث في قاعدة بيانات الأشكال."""

        if self.shapes_database:
            return self.shapes_database.search_shapes(query)
        elif self.mother_shapes_database:
            return self.mother_shapes_database.search_shapes(query)
        else:
            print("⚠️ قاعدة بيانات الأشكال غير متاحة")
            return []

    def get_transformation_from_database(self, source_id: str, target_id: str, steps: int = 10):
        """الحصول على تحويل من قاعدة البيانات."""

        if self.shapes_database:
            return self.shapes_database.get_transformation_sequence(source_id, target_id, steps)
        elif self.mother_shapes_database:
            return self.mother_shapes_database.get_transformation_sequence(source_id, target_id, steps)
        else:
            print("⚠️ قاعدة بيانات الأشكال غير متاحة")
            return []

    def inherit_from_mother(self, inheritance_package: dict):
        """وراثة من النظام الثوري الأم وفقاً للسياسة الثورية."""

        print("🧬 بدء وراثة الوحدة الفنية من النظام الأم...")

        self.mother_inheritance = inheritance_package

        # وراثة الأشكال الأساسية
        if 'shapes' in inheritance_package:
            self.inherited_shapes = inheritance_package['shapes']
            print(f"   ✅ تم وراثة {len(self.inherited_shapes)} شكل أساسي")

        # وراثة المعادلات الأساسية
        if 'equations' in inheritance_package:
            self.inherited_equations = inheritance_package['equations']
            print(f"   ✅ تم وراثة {len(self.inherited_equations)} معادلة أساسية")

        # وراثة المعاملات
        if 'coefficients' in inheritance_package:
            self.inherited_coefficients = inheritance_package['coefficients']
            print("   ✅ تم وراثة معاملات المعادلة الأم")

        # تفعيل التكيف البصري (الأولوية العليا)
        self.visual_adaptation_enabled = True

        # تحديث محرك الاستنباط بالمعرفة الموروثة
        if hasattr(self.inference_engine, 'update_with_inherited_knowledge'):
            self.inference_engine.update_with_inherited_knowledge(inheritance_package)

        # تحديث محرك الرسم بالأشكال الموروثة
        if hasattr(self.artistic_renderer, 'update_with_inherited_shapes'):
            self.artistic_renderer.update_with_inherited_shapes(self.inherited_shapes)

        print("🎨 تمت وراثة الوحدة الفنية بنجاح من النظام الأم!")

    def create_visual_adaptation(self, source_shape: str, target_shape: str, steps: int = 50):
        """إنشاء تكيف بصري سلس - الأولوية العليا وفقاً للسياسة الثورية."""

        if not self.visual_adaptation_enabled:
            print("❌ التكيف البصري غير مفعل - يجب الوراثة من النظام الأم أولاً")
            return None

        # محاولة الحصول على الأشكال من قاعدة البيانات أولاً
        source_shape_def = self.get_shape_from_database(source_shape)
        target_shape_def = self.get_shape_from_database(target_shape)

        if source_shape_def and target_shape_def:
            print(f"🗄️ تم العثور على الأشكال في قاعدة البيانات:")
            print(f"   المصدر: {source_shape_def.metadata.name_ar}")
            print(f"   الهدف: {target_shape_def.metadata.name_ar}")

            # استخدام تسلسل التحويل من قاعدة البيانات
            transformation_sequence = self.get_transformation_from_database(source_shape, target_shape, steps)

            if transformation_sequence:
                print(f"🔄 تم إنشاء تسلسل التحويل من قاعدة البيانات: {len(transformation_sequence)} خطوة")

                # تحسين التحويل باستخدام النظام الخبير/المستكشف الموروث
                if self.adaptive_intelligence_enabled and self.expert_explorer_system:
                    print("🧠 تحسين التحويل باستخدام المعادلات المتكيفة الذكية...")
                    enhanced_transformation = self._enhance_transformation_with_adaptive_intelligence(
                        transformation_sequence, source_shape_def, target_shape_def
                    )
                    return enhanced_transformation

                return transformation_sequence

        if source_shape not in self.inherited_shapes or target_shape not in self.inherited_shapes:
            print(f"❌ أحد الأشكال غير موجود في الأشكال الموروثة")
            return None

        print(f"🎨 إنشاء تكيف بصري سلس من {source_shape} إلى {target_shape}")

        source_components = self.inherited_shapes[source_shape]['components']
        target_components = self.inherited_shapes[target_shape]['components']

        adaptation_frames = []

        for step in range(steps + 1):
            progress = step / steps

            # تكيف المكونات
            adapted_components = []
            max_components = max(len(source_components), len(target_components))

            for i in range(max_components):
                if i < len(source_components) and i < len(target_components):
                    # تكيف بين مكونين
                    source_comp = source_components[i]
                    target_comp = target_components[i]
                    adapted_comp = self._interpolate_visual_component(source_comp, target_comp, progress)
                    adapted_components.append(adapted_comp)
                elif i < len(source_components):
                    # تلاشي المكون المصدر
                    source_comp = source_components[i].copy()
                    fade_factor = 1.0 - progress
                    if source_comp['type'] == 'sigmoid':
                        source_comp['params']['alpha'] *= fade_factor
                    elif source_comp['type'] == 'linear':
                        source_comp['params']['beta'] *= fade_factor
                    adapted_components.append(source_comp)
                elif i < len(target_components):
                    # ظهور المكون الهدف
                    target_comp = target_components[i].copy()
                    appear_factor = progress
                    if target_comp['type'] == 'sigmoid':
                        target_comp['params']['alpha'] *= appear_factor
                    elif target_comp['type'] == 'linear':
                        target_comp['params']['beta'] *= appear_factor
                    adapted_components.append(target_comp)

            adaptation_frames.append({
                'step': step,
                'progress': progress,
                'components': adapted_components,
                'title': f"تكيف بصري: {progress:.1%}"
            })

        print(f"✅ تم إنشاء {len(adaptation_frames)} إطار تكيف بصري")

        return adaptation_frames

    def _interpolate_visual_component(self, source_comp: dict, target_comp: dict, progress: float) -> dict:
        """تكيف بصري سلس بين مكونين."""

        adapted_comp = source_comp.copy()

        if source_comp['type'] == target_comp['type']:
            # نفس النوع - تكيف المعاملات
            if source_comp['type'] == 'sigmoid':
                for param in ['n', 'k', 'x0', 'alpha']:
                    if param in source_comp['params'] and param in target_comp['params']:
                        source_val = source_comp['params'][param]
                        target_val = target_comp['params'][param]
                        adapted_comp['params'][param] = source_val + (target_val - source_val) * progress
            elif source_comp['type'] == 'linear':
                for param in ['beta', 'gamma']:
                    if param in source_comp['params'] and param in target_comp['params']:
                        source_val = source_comp['params'][param]
                        target_val = target_comp['params'][param]
                        adapted_comp['params'][param] = source_val + (target_val - source_val) * progress
        else:
            # أنواع مختلفة - تحويل تدريجي
            if progress < 0.5:
                fade_factor = 1.0 - (progress * 2)
                if adapted_comp['type'] == 'sigmoid':
                    adapted_comp['params']['alpha'] *= fade_factor
                elif adapted_comp['type'] == 'linear':
                    adapted_comp['params']['beta'] *= fade_factor
            else:
                adapted_comp = target_comp.copy()
                appear_factor = (progress - 0.5) * 2
                if adapted_comp['type'] == 'sigmoid':
                    adapted_comp['params']['alpha'] *= appear_factor
                elif adapted_comp['type'] == 'linear':
                    adapted_comp['params']['beta'] *= appear_factor

        return adapted_comp

    def _enhance_transformation_with_adaptive_intelligence(self, transformation_sequence, source_shape_def, target_shape_def):
        """تحسين التحويل باستخدام النظام الخبير/المستكشف والمعادلات المتكيفة الذكية."""

        print("🧠🔍 تطبيق الذكاء التكيفي على التحويل...")

        if not self.expert_explorer_system or not self.inherited_adaptive_equations:
            print("⚠️ النظام الخبير/المستكشف أو المعادلات المتكيفة غير متاحة")
            return transformation_sequence

        enhanced_sequence = []

        # استخراج بيانات التحويل للتحليل
        x_data = [step['progress'] for step in transformation_sequence]

        # تحليل معادلات الشكل المصدر
        source_equations = source_shape_def.equations
        source_complexity = len(source_equations)

        # تحليل معادلات الشكل الهدف
        target_equations = target_shape_def.equations
        target_complexity = len(target_equations)

        print(f"   📊 تعقيد المصدر: {source_complexity}, تعقيد الهدف: {target_complexity}")

        # إنشاء بيانات تدريب للمعادلات المتكيفة
        training_data = []
        for i, step in enumerate(transformation_sequence):
            progress = step['progress']

            # حساب مؤشر التعقيد المتوقع في هذه النقطة
            expected_complexity = source_complexity + (target_complexity - source_complexity) * progress
            training_data.append((progress, expected_complexity))

        x_train = [point[0] for point in training_data]
        y_train = [point[1] for point in training_data]

        # استخدام النظام الخبير/المستكشف لإنشاء معادلة تكيفية ذكية
        try:
            print("   🧬 إنشاء معادلة تكيفية ذكية للتحويل...")
            adaptive_eq = self.expert_explorer_system.create_adaptive_equation_from_data(x_train, y_train)

            # تطوير المعادلة لتحسين الأداء
            print("   🔧 تطوير المعادلة التكيفية...")
            evolution_result = self.expert_explorer_system.evolve_adaptive_equations(x_train, y_train, population_size=5)

            if evolution_result['evolution_success']:
                best_adaptive_eq = evolution_result['best_equation']
                print(f"   ✅ تم تطوير معادلة تكيفية: لياقة={evolution_result['best_fitness']:.4f}")

                # تطبيق المعادلة المتكيفة على التحويل
                for step in transformation_sequence:
                    progress = step['progress']

                    # حساب عامل التحسين من المعادلة المتكيفة
                    if hasattr(best_adaptive_eq, 'evaluate'):
                        enhancement_factor = best_adaptive_eq.evaluate(progress)
                    else:
                        enhancement_factor = 1.0

                    # تطبيق التحسين على معادلات الخطوة
                    enhanced_equations = []
                    for eq in step['equations']:
                        enhanced_eq = eq.__dict__.copy() if hasattr(eq, '__dict__') else eq.copy()

                        # تحسين المعاملات باستخدام عامل التحسين
                        if 'parameters' in enhanced_eq:
                            for param, value in enhanced_eq['parameters'].items():
                                if isinstance(value, (int, float)):
                                    # تطبيق تحسين ذكي مع حدود آمنة
                                    enhanced_value = value * (1.0 + (enhancement_factor - 1.0) * 0.1)
                                    enhanced_eq['parameters'][param] = enhanced_value

                        enhanced_equations.append(enhanced_eq)

                    # إنشاء خطوة محسنة
                    enhanced_step = step.copy()
                    enhanced_step['equations'] = enhanced_equations
                    enhanced_step['enhancement_factor'] = enhancement_factor
                    enhanced_step['description'] += f" (محسن ذكياً: {enhancement_factor:.3f})"

                    enhanced_sequence.append(enhanced_step)

                print(f"   🌟 تم تحسين {len(enhanced_sequence)} خطوة باستخدام الذكاء التكيفي")
                return enhanced_sequence

        except Exception as e:
            print(f"   ⚠️ خطأ في التحسين الذكي: {e}")

        # في حالة فشل التحسين، إرجاع التسلسل الأصلي
        print("   📋 استخدام التسلسل الأصلي")
        return transformation_sequence

    def create_intelligent_visual_adaptation(self, source_shape: str, target_shape: str, steps: int = 50):
        """إنشاء تكيف بصري ذكي يقوده النظام الخبير/المستكشف."""

        print(f"🧠🎨 إنشاء تكيف بصري ذكي من {source_shape} إلى {target_shape}")

        if not self.adaptive_intelligence_enabled:
            print("❌ الذكاء التكيفي غير مفعل - استخدام التكيف العادي")
            return self.create_visual_adaptation(source_shape, target_shape, steps)

        if not self.expert_explorer_system:
            print("❌ النظام الخبير/المستكشف غير متاح")
            return None

        # الحصول على الأشكال
        source_shape_def = self.get_shape_from_database(source_shape)
        target_shape_def = self.get_shape_from_database(target_shape)

        if not source_shape_def or not target_shape_def:
            print("❌ لم يتم العثور على الأشكال في قاعدة البيانات")
            return None

        print(f"🗄️ الأشكال المحددة:")
        print(f"   المصدر: {source_shape_def.metadata.name_ar} (تعقيد: {source_shape_def.complexity_level.value})")
        print(f"   الهدف: {target_shape_def.metadata.name_ar} (تعقيد: {target_shape_def.complexity_level.value})")

        # تحليل الأشكال باستخدام النظام الخبير
        print("🧠 تحليل الأشكال باستخدام النظام الخبير...")

        # إنشاء بيانات تدريب من معادلات الأشكال
        source_equations = source_shape_def.equations
        target_equations = target_shape_def.equations

        # إنشاء نقاط تدريب للمعادلات المتكيفة
        x_train = []
        y_train = []

        # تحليل معاملات المعادلات
        for i, eq in enumerate(source_equations):
            for param, value in eq.parameters.items():
                if isinstance(value, (int, float)):
                    x_train.append(i + param.__hash__() % 100 / 100.0)  # نقطة فريدة
                    y_train.append(value)

        for i, eq in enumerate(target_equations):
            for param, value in eq.parameters.items():
                if isinstance(value, (int, float)):
                    x_train.append(i + param.__hash__() % 100 / 100.0 + 10)  # نقاط الهدف
                    y_train.append(value)

        if len(x_train) < 2:
            print("⚠️ بيانات تدريب غير كافية - استخدام التكيف العادي")
            return self.create_visual_adaptation(source_shape, target_shape, steps)

        # تشغيل دورة التعلم التكيفية
        print("🔄 تشغيل دورة التعلم التكيفية...")
        learning_result = self.expert_explorer_system.adaptive_learning_cycle(x_train, y_train)

        if learning_result['success']:
            print(f"✅ نجح التعلم التكيفي:")
            print(f"   معادلات متكيفة: {learning_result.get('adaptive_equation_created', False)}")
            print(f"   تطوير: {learning_result.get('evolution_performed', False)}")
            print(f"   أنماط مكتشفة: {learning_result.get('patterns_discovered', 0)}")

            # إنشاء التحويل الذكي
            base_transformation = self.get_transformation_from_database(source_shape, target_shape, steps)

            if base_transformation:
                enhanced_transformation = self._enhance_transformation_with_adaptive_intelligence(
                    base_transformation, source_shape_def, target_shape_def
                )

                print(f"🌟 تم إنشاء تكيف بصري ذكي: {len(enhanced_transformation)} خطوة محسنة")
                return enhanced_transformation

        print("⚠️ فشل التعلم التكيفي - استخدام التكيف العادي")
        return self.create_visual_adaptation(source_shape, target_shape, steps)

    def render_visual_adaptation(self, adaptation_frames: list, animate: bool = True):
        """رسم التكيف البصري."""

        if not adaptation_frames:
            print("❌ لا توجد إطارات تكيف للرسم")
            return

        if animate:
            print("🎬 إنشاء أنيميشن التكيف البصري...")

            # إنشاء أنيميشن للتكيف
            fig, ax = plt.subplots(figsize=(12, 8))

            x_range = (-3, 3)
            x_plot = np.linspace(x_range[0], x_range[1], 500)

            def animate_frame(frame_idx):
                ax.clear()

                frame = adaptation_frames[frame_idx]
                components = frame['components']
                progress = frame['progress']

                # حساب القيم
                y_plot = np.array([baserah_equation(xi, components) for xi in x_plot])

                # رسم المعادلة
                ax.plot(x_plot, y_plot, 'blue', linewidth=3, alpha=0.8)

                # رسم المكونات
                colors = ['green', 'orange', 'purple', 'brown']
                for i, component in enumerate(components):
                    comp_type = component['type']
                    params = component['params']
                    color = colors[i % len(colors)]

                    if comp_type == 'sigmoid':
                        y_comp = np.array([baserah_sigmoid(xi, **params) for xi in x_plot])
                        ax.plot(x_plot, y_comp, '--', color=color, alpha=0.6, linewidth=1)
                    elif comp_type == 'linear':
                        y_comp = np.array([baserah_linear(xi, **params) for xi in x_plot])
                        ax.plot(x_plot, y_comp, ':', color=color, alpha=0.6, linewidth=1)

                ax.set_title(f'{frame["title"]} - التقدم: {progress:.1%}', fontsize=14)
                ax.set_xlabel('x')
                ax.set_ylabel('f(x)')
                ax.grid(True, alpha=0.3)
                ax.set_xlim(x_range)

            from matplotlib.animation import FuncAnimation
            anim = FuncAnimation(fig, animate_frame, frames=len(adaptation_frames),
                               interval=100, repeat=True)

            plt.show()

        else:
            # رسم إطارات مختارة
            selected_frames = [0, len(adaptation_frames)//4, len(adaptation_frames)//2,
                             3*len(adaptation_frames)//4, len(adaptation_frames)-1]

            fig, axes = plt.subplots(1, len(selected_frames), figsize=(20, 4))

            x_range = (-3, 3)
            x_plot = np.linspace(x_range[0], x_range[1], 200)

            for i, frame_idx in enumerate(selected_frames):
                frame = adaptation_frames[frame_idx]
                components = frame['components']

                y_plot = np.array([baserah_equation(xi, components) for xi in x_plot])

                axes[i].plot(x_plot, y_plot, 'blue', linewidth=2)
                axes[i].set_title(f'التقدم: {frame["progress"]:.1%}')
                axes[i].grid(True, alpha=0.3)
                axes[i].set_xlim(x_range)

            plt.tight_layout()
            plt.show()

        print("✅ تم رسم التكيف البصري!")

    def analyze_and_render(self, x_data, y_data, title="تحليل ورسم Baserah"):
        """
        تحليل البيانات واستنتاج المعادلة ثم رسمها
        
        Args:
            x_data: نقاط x
            y_data: نقاط y
            title: عنوان الرسم
        """
        print("🎨 بدء التحليل والرسم المتكامل...")
        
        # الاستنباط
        inference_result = self.inference_engine.infer_from_data_points(x_data, y_data)
        
        if 'error' in inference_result:
            print(f"❌ خطأ في الاستنباط: {inference_result['error']}")
            return None
        
        # توليد المعادلة النصية
        equation_string = self.inference_engine.generate_equation_string(inference_result)
        print(f"📐 المعادلة المستنتجة: {equation_string}")
        
        # الرسم
        components = inference_result['components']
        
        # رسم البيانات الأصلية والمعادلة المستنتجة
        x_range = (min(x_data) - 1, max(x_data) + 1)
        x_plot = np.linspace(x_range[0], x_range[1], 500)
        y_plot = np.array([baserah_equation(xi, components) for xi in x_plot])
        
        plt.figure(figsize=(12, 8))
        
        # رسم البيانات الأصلية
        plt.scatter(x_data, y_data, color='red', s=50, zorder=5, 
                   label='البيانات الأصلية', alpha=0.8)
        
        # رسم المعادلة المستنتجة
        plt.plot(x_plot, y_plot, 'blue', linewidth=3, 
                label='المعادلة المستنتجة', alpha=0.8)
        
        # رسم المكونات منفصلة
        colors = ['green', 'orange', 'purple', 'brown']
        for i, component in enumerate(components):
            comp_type = component['type']
            params = component['params']
            color = colors[i % len(colors)]
            
            if comp_type == 'sigmoid':
                from .baserah_core import baserah_sigmoid
                y_comp = np.array([baserah_sigmoid(xi, **params) for xi in x_plot])
                plt.plot(x_plot, y_comp, '--', color=color, alpha=0.6, 
                        label=f'مكون سيجمويد {i+1}', linewidth=1)
                        
            elif comp_type == 'linear':
                from .baserah_core import baserah_linear
                y_comp = np.array([baserah_linear(xi, **params) for xi in x_plot])
                plt.plot(x_plot, y_comp, ':', color=color, alpha=0.6, 
                        label=f'مكون خطي {i+1}', linewidth=1)
                        
            elif comp_type == 'quantum_sigmoid':
                from .baserah_core import baserah_quantum_sigmoid
                y_comp = np.array([baserah_quantum_sigmoid(xi, **params) for xi in x_plot])
                plt.plot(x_plot, y_comp, '-.', color=color, alpha=0.6, 
                        label=f'مكون مكمم {i+1}', linewidth=1)
        
        plt.title(f'{title}\n{equation_string}', fontsize=14, fontweight='bold')
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # إضافة معلومات الدقة
        error = inference_result.get('error', 0)
        confidence = inference_result.get('confidence', 0)
        info_text = f"خطأ: {error:.6f}\nثقة: {confidence:.2f}\nنوع: {inference_result['type']}"
        
        plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes, 
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.7))
        
        plt.tight_layout()
        plt.show()
        
        return inference_result
    
    def interactive_shape_creator(self):
        """
        أداة تفاعلية لإنشاء الأشكال
        """
        print("🎨 أداة إنشاء الأشكال التفاعلية")
        print("=" * 40)
        
        # قائمة الأشكال المتاحة
        shapes = {
            '1': 'خط مستقيم',
            '2': 'منحنى سيجمويد',
            '3': 'دالة متقطعة',
            '4': 'موجة معقدة',
            '5': 'نمط فني'
        }
        
        print("الأشكال المتاحة:")
        for key, value in shapes.items():
            print(f"  {key}. {value}")
        
        choice = input("\nاختر رقم الشكل: ").strip()
        
        if choice == '1':
            self._create_linear_shape()
        elif choice == '2':
            self._create_sigmoid_shape()
        elif choice == '3':
            self._create_quantum_shape()
        elif choice == '4':
            self._create_complex_wave()
        elif choice == '5':
            self._create_artistic_pattern()
        else:
            print("اختيار غير صحيح")
    
    def _create_linear_shape(self):
        """إنشاء خط مستقيم"""
        print("\n📏 إنشاء خط مستقيم...")
        
        try:
            beta = float(input("أدخل الميل (beta): ") or "1.0")
            gamma = float(input("أدخل التقاطع (gamma): ") or "0.0")
        except ValueError:
            beta, gamma = 1.0, 0.0
            print("استخدام القيم الافتراضية")
        
        components = [
            {'type': 'linear', 'params': {'beta': beta, 'gamma': gamma}}
        ]
        
        self.artistic_renderer.render_equation(components, 
                                             title=f"خط مستقيم: y = {beta}x + {gamma}")
    
    def _create_sigmoid_shape(self):
        """إنشاء منحنى سيجمويد"""
        print("\n📈 إنشاء منحنى سيجمويد...")
        
        try:
            n = int(input("أدخل عامل التقطيع (n): ") or "1")
            k = float(input("أدخل معامل الحدة (k): ") or "1.0")
            x0 = float(input("أدخل نقطة المنتصف (x0): ") or "0.0")
            alpha = float(input("أدخل معامل الوزن (alpha): ") or "1.0")
        except ValueError:
            n, k, x0, alpha = 1, 1.0, 0.0, 1.0
            print("استخدام القيم الافتراضية")
        
        components = [
            {'type': 'sigmoid', 'params': {'n': n, 'k': k, 'x0': x0, 'alpha': alpha}}
        ]
        
        self.artistic_renderer.render_equation(components, 
                                             title=f"سيجمويد: n={n}, k={k}, x0={x0}, α={alpha}")
    
    def _create_quantum_shape(self):
        """إنشاء دالة متقطعة"""
        print("\n🎯 إنشاء دالة متقطعة...")
        
        try:
            quantum_factor = int(input("أدخل عامل التكميم (Q): ") or "4")
            k = float(input("أدخل معامل الحدة (k): ") or "5.0")
        except ValueError:
            quantum_factor, k = 4, 5.0
            print("استخدام القيم الافتراضية")
        
        components = [
            {'type': 'quantum_sigmoid', 
             'params': {'n': 1, 'k': k, 'x0': 0, 'alpha': 1, 'quantum_factor': quantum_factor}}
        ]
        
        self.artistic_renderer.render_equation(components, 
                                             title=f"دالة متقطعة: Q={quantum_factor}")
    
    def _create_complex_wave(self):
        """إنشاء موجة معقدة"""
        print("\n🌊 إنشاء موجة معقدة...")
        
        components = [
            {'type': 'sigmoid', 'params': {'n': 1, 'k': 1, 'x0': 0, 'alpha': 0.8}},
            {'type': 'sigmoid', 'params': {'n': 1, 'k': 2, 'x0': 2, 'alpha': 0.4}},
            {'type': 'linear', 'params': {'beta': 0.1, 'gamma': 0.2}},
            {'type': 'quantum_sigmoid', 'params': {'n': 1, 'k': 3, 'x0': -1, 'alpha': 0.3, 'quantum_factor': 6}}
        ]
        
        animate = input("هل تريد أنيميشن؟ (y/n): ").strip().lower() == 'y'
        
        if animate:
            parameter_animations = {
                0: {'k': (0.5, 2.0)},
                1: {'x0': (1, 3)},
                3: {'quantum_factor': (4, 12)}
            }
            
            self.artistic_renderer.create_animated_equation(components, parameter_animations, 
                                                          x_range=(-5, 5), duration=8.0)
        else:
            self.artistic_renderer.render_equation(components, title="موجة معقدة")
    
    def _create_artistic_pattern(self):
        """إنشاء نمط فني"""
        print("\n🎨 إنشاء نمط فني...")
        
        patterns = {
            '1': 'heart',
            '2': 'wave', 
            '3': 'flower',
            '4': 'spiral'
        }
        
        print("الأنماط المتاحة:")
        for key, value in patterns.items():
            print(f"  {key}. {value}")
        
        choice = input("اختر رقم النمط: ").strip()
        animate = input("هل تريد أنيميشن؟ (y/n): ").strip().lower() == 'y'
        
        if choice in patterns:
            pattern_type = patterns[choice]
            self.artistic_renderer.create_artistic_pattern(pattern_type, animate)
        else:
            print("اختيار غير صحيح")
    
    def batch_analysis(self, data_sets):
        """
        تحليل مجموعة من البيانات دفعة واحدة
        
        Args:
            data_sets: قائمة من أزواج (x_data, y_data, title)
        """
        print(f"📊 بدء التحليل المجمع لـ {len(data_sets)} مجموعة بيانات...")
        
        results = []
        
        for i, (x_data, y_data, title) in enumerate(data_sets):
            print(f"\n--- تحليل المجموعة {i+1}: {title} ---")
            
            result = self.analyze_and_render(x_data, y_data, title)
            results.append(result)
        
        # ملخص النتائج
        print("\n📋 ملخص النتائج:")
        print("=" * 50)
        
        for i, result in enumerate(results):
            if result and 'error' not in result:
                error = result.get('error', 0)
                confidence = result.get('confidence', 0)
                pattern_type = result.get('type', 'غير محدد')
                
                print(f"{i+1}. {data_sets[i][2]}:")
                print(f"   النمط: {pattern_type}")
                print(f"   الخطأ: {error:.6f}")
                print(f"   الثقة: {confidence:.2f}")
            else:
                print(f"{i+1}. {data_sets[i][2]}: فشل التحليل")
        
        return results
    
    def demo_integrated_system(self):
        """عرض شامل للنظام المتكامل"""
        
        print("🚀 عرض شامل للنظام المتكامل Baserah")
        print("=" * 50)
        
        # بيانات اختبار متنوعة
        test_data_sets = [
            # خط مستقيم
            ([-3, -2, -1, 0, 1, 2, 3], 
             [-1, 1, 3, 5, 7, 9, 11], 
             "خط مستقيم"),
            
            # سيجمويد
            ([-3, -2, -1, 0, 1, 2, 3], 
             [0.05, 0.12, 0.27, 0.5, 0.73, 0.88, 0.95], 
             "منحنى سيجمويد"),
            
            # دالة متقطعة
            ([-2, -1, 0, 1, 2], 
             [0, 0, 0.5, 1, 1], 
             "دالة متقطعة"),
            
            # موجة معقدة
            ([-4, -3, -2, -1, 0, 1, 2, 3, 4], 
             [0.1, 0.3, 0.7, 1.2, 1.5, 1.8, 2.1, 2.3, 2.4], 
             "موجة معقدة")
        ]
        
        # تحليل مجمع
        results = self.batch_analysis(test_data_sets)
        
        # عرض مستويات التكميم
        print("\n🎯 عرض مستويات التكميم...")
        self.artistic_renderer.render_quantum_levels_demo()
        
        print("\n✅ انتهى العرض الشامل للنظام المتكامل!")

if __name__ == "__main__":
    system = BaserahIntegratedSystem()
    system.demo_integrated_system()
