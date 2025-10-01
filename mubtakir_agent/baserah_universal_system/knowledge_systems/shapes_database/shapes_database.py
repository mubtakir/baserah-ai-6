#!/usr/bin/env python3
# shapes_database.py - قاعدة بيانات الأشكال الأساسية للنظام الثوري Baserah

import numpy as np
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Union, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
import json

class ShapeType(Enum):
    """أنواع الأشكال الأساسية."""
    GEOMETRIC = "geometric"      # هندسي (مربع، دائرة، مثلث)
    ORGANIC = "organic"          # عضوي (قطة، شجرة، إنسان)
    ABSTRACT = "abstract"        # مجرد (موجة، نمط، تدرج)
    MATHEMATICAL = "mathematical" # رياضي (دالة، منحنى، معادلة)
    ARTISTIC = "artistic"        # فني (زخرفة، خط، تصميم)

class ComplexityLevel(Enum):
    """مستويات التعقيد."""
    PRIMITIVE = "primitive"      # بدائي
    BASIC = "basic"             # أساسي
    INTERMEDIATE = "intermediate" # متوسط
    ADVANCED = "advanced"        # متقدم
    PROFESSIONAL = "professional" # محترف

@dataclass
class ShapeEquation:
    """معادلة الشكل الرياضية."""
    equation_type: str  # sigmoid, linear, quantum_sigmoid, mixed
    parameters: Dict[str, float]  # المعاملات (n, k, x0, alpha, beta, gamma)
    domain: Tuple[float, float] = (-5.0, 5.0)  # المجال
    description: str = ""  # وصف المعادلة

@dataclass
class ShapeMetadata:
    """بيانات وصفية للشكل."""
    name_ar: str  # الاسم بالعربية
    name_en: str  # الاسم بالإنجليزية
    description: str  # الوصف
    tags: List[str] = field(default_factory=list)  # العلامات
    cultural_significance: str = ""  # الأهمية الثقافية
    mathematical_beauty: float = 0.0  # الجمال الرياضي (0-1)

@dataclass
class ShapeDefinition:
    """تعريف شامل للشكل."""
    shape_id: str
    shape_type: ShapeType
    complexity_level: ComplexityLevel
    metadata: ShapeMetadata
    equations: List[ShapeEquation]
    animation_frames: Optional[List[Dict]] = None
    visual_properties: Dict[str, Any] = field(default_factory=dict)
    creation_date: str = field(default_factory=lambda: datetime.now().isoformat())

class BaserahShapesDatabase:
    """
    قاعدة بيانات الأشكال الأساسية للنظام الثوري Baserah
    
    تحتوي على جميع الأشكال والأمثلة التي ترث منها الوحدات:
    - الأشكال الهندسية الأساسية
    - الكائنات العضوية
    - الأنماط الرياضية
    - الأمثلة الفنية
    - معادلات التحويل والتكيف
    """
    
    def __init__(self):
        """تهيئة قاعدة بيانات الأشكال."""
        
        self.database_id = f"shapes_db_{uuid.uuid4()}"
        self.shapes: Dict[str, ShapeDefinition] = {}
        self.shape_categories: Dict[ShapeType, List[str]] = {
            shape_type: [] for shape_type in ShapeType
        }
        self.complexity_index: Dict[ComplexityLevel, List[str]] = {
            level: [] for level in ComplexityLevel
        }
        
        # تهيئة قاعدة البيانات الأساسية
        self._initialize_basic_shapes()
        self._initialize_organic_shapes()
        self._initialize_mathematical_shapes()
        self._initialize_artistic_shapes()
        self._initialize_transformation_examples()
        
        print("🗄️ تم تهيئة قاعدة بيانات الأشكال الأساسية")
        print(f"   📊 إجمالي الأشكال: {len(self.shapes)}")
    
    def _initialize_basic_shapes(self):
        """تهيئة الأشكال الهندسية الأساسية."""
        
        print("📐 تهيئة الأشكال الهندسية الأساسية...")
        
        # مربع
        square_shape = ShapeDefinition(
            shape_id="square_basic",
            shape_type=ShapeType.GEOMETRIC,
            complexity_level=ComplexityLevel.BASIC,
            metadata=ShapeMetadata(
                name_ar="مربع",
                name_en="Square",
                description="شكل هندسي أساسي بأربعة أضلاع متساوية",
                tags=["هندسي", "أساسي", "متساوي الأضلاع"],
                cultural_significance="رمز الاستقرار والتوازن",
                mathematical_beauty=0.8
            ),
            equations=[
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": 1.0, "gamma": 0.0},
                    description="الضلع العلوي"
                ),
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": 0.0, "gamma": 1.0},
                    description="الضلع الأيمن"
                ),
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": -1.0, "gamma": 1.0},
                    description="الضلع السفلي"
                ),
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": 0.0, "gamma": 0.0},
                    description="الضلع الأيسر"
                )
            ],
            visual_properties={
                "color": "#3498db",
                "line_width": 2,
                "fill": False,
                "symmetry": "4-fold"
            }
        )
        self._add_shape(square_shape)
        
        # دائرة
        circle_shape = ShapeDefinition(
            shape_id="circle_basic",
            shape_type=ShapeType.GEOMETRIC,
            complexity_level=ComplexityLevel.BASIC,
            metadata=ShapeMetadata(
                name_ar="دائرة",
                name_en="Circle",
                description="شكل هندسي مثالي بجميع النقاط متساوية البعد عن المركز",
                tags=["هندسي", "مثالي", "دائري"],
                cultural_significance="رمز الكمال والوحدة",
                mathematical_beauty=1.0
            ),
            equations=[
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 2, "k": 10.0, "x0": 0.0, "alpha": 1.0},
                    description="الدائرة الكاملة"
                )
            ],
            visual_properties={
                "color": "#e74c3c",
                "line_width": 2,
                "fill": False,
                "symmetry": "infinite"
            }
        )
        self._add_shape(circle_shape)
        
        # مثلث
        triangle_shape = ShapeDefinition(
            shape_id="triangle_basic",
            shape_type=ShapeType.GEOMETRIC,
            complexity_level=ComplexityLevel.BASIC,
            metadata=ShapeMetadata(
                name_ar="مثلث",
                name_en="Triangle",
                description="شكل هندسي بثلاثة أضلاع وثلاث زوايا",
                tags=["هندسي", "ثلاثي", "زاوي"],
                cultural_significance="رمز القوة والاتجاه",
                mathematical_beauty=0.7
            ),
            equations=[
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": 0.5, "gamma": 0.0},
                    description="القاعدة"
                ),
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": -1.0, "gamma": 1.0},
                    description="الضلع الأيسر"
                ),
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": 1.0, "gamma": 1.0},
                    description="الضلع الأيمن"
                )
            ],
            visual_properties={
                "color": "#f39c12",
                "line_width": 2,
                "fill": False,
                "symmetry": "3-fold"
            }
        )
        self._add_shape(triangle_shape)
        
        # مستطيل
        rectangle_shape = ShapeDefinition(
            shape_id="rectangle_basic",
            shape_type=ShapeType.GEOMETRIC,
            complexity_level=ComplexityLevel.BASIC,
            metadata=ShapeMetadata(
                name_ar="مستطيل",
                name_en="Rectangle",
                description="شكل هندسي بأربعة أضلاع وأربع زوايا قائمة",
                tags=["هندسي", "مستطيل", "زوايا قائمة"],
                cultural_significance="رمز النظام والترتيب",
                mathematical_beauty=0.6
            ),
            equations=[
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": 1.5, "gamma": 0.0},
                    description="الضلع العلوي"
                ),
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": 0.0, "gamma": 1.0},
                    description="الضلع الأيمن"
                ),
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": -1.5, "gamma": 1.0},
                    description="الضلع السفلي"
                ),
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": 0.0, "gamma": 0.0},
                    description="الضلع الأيسر"
                )
            ],
            visual_properties={
                "color": "#9b59b6",
                "line_width": 2,
                "fill": False,
                "symmetry": "2-fold"
            }
        )
        self._add_shape(rectangle_shape)
        
        print(f"   ✅ تم إضافة {len([s for s in self.shapes.values() if s.shape_type == ShapeType.GEOMETRIC])} أشكال هندسية")
    
    def _initialize_organic_shapes(self):
        """تهيئة الأشكال العضوية."""
        
        print("🌿 تهيئة الأشكال العضوية...")
        
        # قطة بدائية
        primitive_cat = ShapeDefinition(
            shape_id="cat_primitive",
            shape_type=ShapeType.ORGANIC,
            complexity_level=ComplexityLevel.PRIMITIVE,
            metadata=ShapeMetadata(
                name_ar="قطة بدائية",
                name_en="Primitive Cat",
                description="تمثيل بسيط لقطة باستخدام أشكال أساسية",
                tags=["عضوي", "حيوان", "بدائي"],
                cultural_significance="رمز الرشاقة والاستقلالية",
                mathematical_beauty=0.4
            ),
            equations=[
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 1, "k": 2.0, "x0": 0.0, "alpha": 0.8},
                    description="الجسم"
                ),
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 1, "k": 3.0, "x0": 0.5, "alpha": 0.4},
                    description="الرأس"
                ),
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": 0.2, "gamma": 0.1},
                    description="الذيل"
                )
            ],
            visual_properties={
                "color": "#34495e",
                "line_width": 2,
                "fill": True,
                "texture": "fur"
            }
        )
        self._add_shape(primitive_cat)
        
        # قطة محترفة
        professional_cat = ShapeDefinition(
            shape_id="cat_professional",
            shape_type=ShapeType.ORGANIC,
            complexity_level=ComplexityLevel.PROFESSIONAL,
            metadata=ShapeMetadata(
                name_ar="قطة محترفة",
                name_en="Professional Cat",
                description="تمثيل متقدم ومفصل لقطة بتفاصيل واقعية",
                tags=["عضوي", "حيوان", "محترف", "مفصل"],
                cultural_significance="تطور الفن من البساطة إلى التعقيد",
                mathematical_beauty=0.9
            ),
            equations=[
                ShapeEquation(
                    equation_type="quantum_sigmoid",
                    parameters={"n": 3, "k": 1.5, "x0": 0.0, "alpha": 1.2},
                    description="الجسم المفصل"
                ),
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 2, "k": 4.0, "x0": 0.6, "alpha": 0.6},
                    description="الرأس المفصل"
                ),
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 1, "k": 1.8, "x0": -0.3, "alpha": 0.3},
                    description="الذيل المنحني"
                ),
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": 0.1, "gamma": 0.05},
                    description="الأرجل"
                ),
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 1, "k": 8.0, "x0": 0.7, "alpha": 0.1},
                    description="الأذنان"
                )
            ],
            visual_properties={
                "color": "#2c3e50",
                "line_width": 1,
                "fill": True,
                "texture": "detailed_fur",
                "shading": True,
                "whiskers": True
            }
        )
        self._add_shape(professional_cat)
        
        # شجرة
        tree_shape = ShapeDefinition(
            shape_id="tree_basic",
            shape_type=ShapeType.ORGANIC,
            complexity_level=ComplexityLevel.INTERMEDIATE,
            metadata=ShapeMetadata(
                name_ar="شجرة",
                name_en="Tree",
                description="شجرة طبيعية بجذع وأوراق",
                tags=["عضوي", "نبات", "طبيعة"],
                cultural_significance="رمز النمو والحياة",
                mathematical_beauty=0.7
            ),
            equations=[
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": 2.0, "gamma": 0.0},
                    description="الجذع"
                ),
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 3, "k": 1.0, "x0": 0.0, "alpha": 1.5},
                    description="الأوراق"
                ),
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 2, "k": 0.8, "x0": 0.2, "alpha": 0.8},
                    description="الفروع"
                )
            ],
            visual_properties={
                "trunk_color": "#8b4513",
                "leaves_color": "#228b22",
                "line_width": 3,
                "seasonal": True
            }
        )
        self._add_shape(tree_shape)
        
        # إنسان بسيط
        human_simple = ShapeDefinition(
            shape_id="human_simple",
            shape_type=ShapeType.ORGANIC,
            complexity_level=ComplexityLevel.BASIC,
            metadata=ShapeMetadata(
                name_ar="إنسان بسيط",
                name_en="Simple Human",
                description="تمثيل بسيط للشكل الإنساني",
                tags=["عضوي", "إنسان", "بسيط"],
                cultural_significance="جوهر الإنسانية",
                mathematical_beauty=0.6
            ),
            equations=[
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 2, "k": 1.5, "x0": 0.0, "alpha": 1.8},
                    description="الجسم"
                ),
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 1, "k": 2.0, "x0": 0.5, "alpha": 0.8},
                    description="الرأس"
                ),
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": 0.3, "gamma": 0.1},
                    description="الأطراف"
                )
            ],
            visual_properties={
                "color": "#d4a574",
                "line_width": 2,
                "proportions": "human",
                "posture": "standing"
            }
        )
        self._add_shape(human_simple)
        
        print(f"   ✅ تم إضافة {len([s for s in self.shapes.values() if s.shape_type == ShapeType.ORGANIC])} أشكال عضوية")
    
    def _initialize_mathematical_shapes(self):
        """تهيئة الأشكال الرياضية."""
        
        print("📊 تهيئة الأشكال الرياضية...")
        
        # موجة جيبية
        sine_wave = ShapeDefinition(
            shape_id="sine_wave",
            shape_type=ShapeType.MATHEMATICAL,
            complexity_level=ComplexityLevel.INTERMEDIATE,
            metadata=ShapeMetadata(
                name_ar="موجة جيبية",
                name_en="Sine Wave",
                description="موجة رياضية جيبية كلاسيكية",
                tags=["رياضي", "موجة", "دوري"],
                cultural_significance="أساس الذبذبات والموسيقى",
                mathematical_beauty=0.9
            ),
            equations=[
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 1, "k": 1.0, "x0": 0.0, "alpha": 1.0},
                    description="الموجة الجيبية"
                )
            ],
            visual_properties={
                "color": "#1abc9c",
                "line_width": 2,
                "frequency": 1.0,
                "amplitude": 1.0,
                "animated": True
            }
        )
        self._add_shape(sine_wave)
        
        # حلزون
        spiral_shape = ShapeDefinition(
            shape_id="spiral_fibonacci",
            shape_type=ShapeType.MATHEMATICAL,
            complexity_level=ComplexityLevel.ADVANCED,
            metadata=ShapeMetadata(
                name_ar="حلزون فيبوناتشي",
                name_en="Fibonacci Spiral",
                description="حلزون رياضي يتبع متتالية فيبوناتشي",
                tags=["رياضي", "حلزون", "فيبوناتشي", "ذهبي"],
                cultural_significance="النسبة الذهبية في الطبيعة",
                mathematical_beauty=1.0
            ),
            equations=[
                ShapeEquation(
                    equation_type="quantum_sigmoid",
                    parameters={"n": 2, "k": 0.618, "x0": 0.0, "alpha": 1.618},
                    description="الحلزون الذهبي"
                )
            ],
            visual_properties={
                "color": "#f1c40f",
                "line_width": 2,
                "golden_ratio": True,
                "growth_factor": 1.618
            }
        )
        self._add_shape(spiral_shape)
        
        # منحنى بيزيه
        bezier_curve = ShapeDefinition(
            shape_id="bezier_curve",
            shape_type=ShapeType.MATHEMATICAL,
            complexity_level=ComplexityLevel.ADVANCED,
            metadata=ShapeMetadata(
                name_ar="منحنى بيزيه",
                name_en="Bezier Curve",
                description="منحنى رياضي ناعم يستخدم في التصميم",
                tags=["رياضي", "منحنى", "ناعم", "تصميم"],
                cultural_significance="أساس التصميم الرقمي الحديث",
                mathematical_beauty=0.8
            ),
            equations=[
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 3, "k": 2.0, "x0": 0.0, "alpha": 1.0},
                    description="منحنى بيزيه التكعيبي"
                )
            ],
            visual_properties={
                "color": "#e67e22",
                "line_width": 2,
                "control_points": 4,
                "smoothness": "high"
            }
        )
        self._add_shape(bezier_curve)
        
        print(f"   ✅ تم إضافة {len([s for s in self.shapes.values() if s.shape_type == ShapeType.MATHEMATICAL])} أشكال رياضية")
    
    def _initialize_artistic_shapes(self):
        """تهيئة الأشكال الفنية."""
        
        print("🎨 تهيئة الأشكال الفنية...")
        
        # زخرفة إسلامية
        islamic_pattern = ShapeDefinition(
            shape_id="islamic_geometric",
            shape_type=ShapeType.ARTISTIC,
            complexity_level=ComplexityLevel.PROFESSIONAL,
            metadata=ShapeMetadata(
                name_ar="زخرفة إسلامية",
                name_en="Islamic Geometric Pattern",
                description="نمط زخرفي إسلامي هندسي تقليدي",
                tags=["فني", "إسلامي", "زخرفة", "هندسي"],
                cultural_significance="التراث الإسلامي والفن الهندسي",
                mathematical_beauty=0.95
            ),
            equations=[
                ShapeEquation(
                    equation_type="quantum_sigmoid",
                    parameters={"n": 8, "k": 1.0, "x0": 0.0, "alpha": 1.0},
                    description="النمط الثماني"
                ),
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 4, "k": 1.414, "x0": 0.0, "alpha": 0.707},
                    description="النمط المربع"
                )
            ],
            visual_properties={
                "color": "#8e44ad",
                "line_width": 1,
                "symmetry": "8-fold",
                "repetitive": True,
                "traditional": True
            }
        )
        self._add_shape(islamic_pattern)
        
        # خط عربي
        arabic_calligraphy = ShapeDefinition(
            shape_id="arabic_calligraphy",
            shape_type=ShapeType.ARTISTIC,
            complexity_level=ComplexityLevel.PROFESSIONAL,
            metadata=ShapeMetadata(
                name_ar="خط عربي",
                name_en="Arabic Calligraphy",
                description="فن الخط العربي الجميل",
                tags=["فني", "خط", "عربي", "جمال"],
                cultural_significance="فن الكتابة العربية الأصيل",
                mathematical_beauty=0.9
            ),
            equations=[
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 2, "k": 3.0, "x0": 0.0, "alpha": 1.5},
                    description="انسيابية الخط"
                ),
                ShapeEquation(
                    equation_type="linear",
                    parameters={"beta": 0.5, "gamma": 0.2},
                    description="استقامة الحروف"
                )
            ],
            visual_properties={
                "color": "#2c3e50",
                "line_width": 3,
                "style": "naskh",
                "flowing": True,
                "artistic": True
            }
        )
        self._add_shape(arabic_calligraphy)
        
        # ماندالا
        mandala_pattern = ShapeDefinition(
            shape_id="mandala_pattern",
            shape_type=ShapeType.ARTISTIC,
            complexity_level=ComplexityLevel.ADVANCED,
            metadata=ShapeMetadata(
                name_ar="ماندالا",
                name_en="Mandala Pattern",
                description="نمط دائري متماثل للتأمل والفن",
                tags=["فني", "دائري", "متماثل", "تأمل"],
                cultural_significance="رمز الكون والتوازن الروحي",
                mathematical_beauty=0.85
            ),
            equations=[
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 6, "k": 2.0, "x0": 0.0, "alpha": 1.0},
                    description="النمط السداسي"
                ),
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 12, "k": 1.5, "x0": 0.0, "alpha": 0.8},
                    description="النمط الاثني عشري"
                )
            ],
            visual_properties={
                "color": "#e74c3c",
                "line_width": 1,
                "symmetry": "radial",
                "meditative": True,
                "colorful": True
            }
        )
        self._add_shape(mandala_pattern)
        
        print(f"   ✅ تم إضافة {len([s for s in self.shapes.values() if s.shape_type == ShapeType.ARTISTIC])} أشكال فنية")
    
    def _add_shape(self, shape: ShapeDefinition):
        """إضافة شكل إلى قاعدة البيانات."""
        
        self.shapes[shape.shape_id] = shape
        self.shape_categories[shape.shape_type].append(shape.shape_id)
        self.complexity_index[shape.complexity_level].append(shape.shape_id)
    
    def get_shape(self, shape_id: str) -> Optional[ShapeDefinition]:
        """الحصول على شكل بالمعرف."""
        return self.shapes.get(shape_id)
    
    def get_shapes_by_type(self, shape_type: ShapeType) -> List[ShapeDefinition]:
        """الحصول على الأشكال حسب النوع."""
        shape_ids = self.shape_categories.get(shape_type, [])
        return [self.shapes[shape_id] for shape_id in shape_ids]
    
    def get_shapes_by_complexity(self, complexity: ComplexityLevel) -> List[ShapeDefinition]:
        """الحصول على الأشكال حسب مستوى التعقيد."""
        shape_ids = self.complexity_index.get(complexity, [])
        return [self.shapes[shape_id] for shape_id in shape_ids]
    
    def search_shapes(self, query: str) -> List[ShapeDefinition]:
        """البحث في الأشكال."""
        results = []
        query_lower = query.lower()
        
        for shape in self.shapes.values():
            if (query_lower in shape.metadata.name_ar.lower() or
                query_lower in shape.metadata.name_en.lower() or
                query_lower in shape.metadata.description.lower() or
                any(query_lower in tag.lower() for tag in shape.metadata.tags)):
                results.append(shape)
        
        return results

    def _initialize_transformation_examples(self):
        """تهيئة أمثلة التحويل والتكيف."""

        print("🔄 تهيئة أمثلة التحويل والتكيف...")

        # تحويل مربع إلى دائرة
        square_to_circle = ShapeDefinition(
            shape_id="transform_square_to_circle",
            shape_type=ShapeType.ABSTRACT,
            complexity_level=ComplexityLevel.INTERMEDIATE,
            metadata=ShapeMetadata(
                name_ar="تحويل مربع إلى دائرة",
                name_en="Square to Circle Transformation",
                description="تحويل تدريجي من مربع إلى دائرة",
                tags=["تحويل", "تكيف", "هندسي"],
                cultural_significance="تطور الشكل من الزاوية إلى الانسيابية",
                mathematical_beauty=0.8
            ),
            equations=[
                ShapeEquation(
                    equation_type="mixed",
                    parameters={"n": 2, "k": 5.0, "x0": 0.0, "alpha": 1.0, "transition": 0.5},
                    description="معادلة التحويل التدريجي"
                )
            ],
            animation_frames=[
                {"frame": i, "transition_factor": i/20, "shape_blend": f"square_{100-i*5}_circle_{i*5}"}
                for i in range(21)
            ],
            visual_properties={
                "color_start": "#3498db",
                "color_end": "#e74c3c",
                "morphing": True,
                "duration": 2.0
            }
        )
        self._add_shape(square_to_circle)

        # تطوير القطة من بدائية إلى محترفة
        cat_evolution = ShapeDefinition(
            shape_id="cat_evolution_sequence",
            shape_type=ShapeType.ABSTRACT,
            complexity_level=ComplexityLevel.ADVANCED,
            metadata=ShapeMetadata(
                name_ar="تطوير القطة",
                name_en="Cat Evolution Sequence",
                description="تطوير تدريجي للقطة من بدائية إلى محترفة",
                tags=["تطوير", "عضوي", "تحسن"],
                cultural_significance="تطور الفن والمهارة",
                mathematical_beauty=0.9
            ),
            equations=[
                ShapeEquation(
                    equation_type="quantum_sigmoid",
                    parameters={"n": 3, "k": 2.0, "x0": 0.0, "alpha": 1.5, "evolution_factor": 1.0},
                    description="معادلة التطوير التدريجي"
                )
            ],
            animation_frames=[
                {
                    "frame": i,
                    "detail_level": i/10,
                    "complexity": "primitive" if i < 3 else "basic" if i < 6 else "intermediate" if i < 8 else "professional",
                    "features_added": ["body", "head", "tail", "legs", "ears", "whiskers", "fur_texture", "shading", "expression", "pose"][:(i+1)]
                }
                for i in range(10)
            ],
            visual_properties={
                "progressive_detail": True,
                "skill_demonstration": True,
                "artistic_growth": True
            }
        )
        self._add_shape(cat_evolution)

        # موجة متحركة
        animated_wave = ShapeDefinition(
            shape_id="animated_wave",
            shape_type=ShapeType.ABSTRACT,
            complexity_level=ComplexityLevel.INTERMEDIATE,
            metadata=ShapeMetadata(
                name_ar="موجة متحركة",
                name_en="Animated Wave",
                description="موجة رياضية متحركة تظهر الحركة الدورية",
                tags=["متحرك", "موجة", "دوري"],
                cultural_significance="إيقاع الطبيعة والزمن",
                mathematical_beauty=0.85
            ),
            equations=[
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 1, "k": 1.0, "x0": 0.0, "alpha": 1.0, "phase": 0.0},
                    description="الموجة الأساسية"
                )
            ],
            animation_frames=[
                {
                    "frame": i,
                    "phase": i * 0.314,  # π/10
                    "amplitude": 1.0 + 0.2 * np.sin(i * 0.1),
                    "frequency": 1.0
                }
                for i in range(20)
            ],
            visual_properties={
                "color": "#1abc9c",
                "animated": True,
                "wave_motion": True,
                "continuous": True
            }
        )
        self._add_shape(animated_wave)

        # نمط متطور
        evolving_pattern = ShapeDefinition(
            shape_id="evolving_geometric_pattern",
            shape_type=ShapeType.ABSTRACT,
            complexity_level=ComplexityLevel.ADVANCED,
            metadata=ShapeMetadata(
                name_ar="نمط متطور",
                name_en="Evolving Geometric Pattern",
                description="نمط هندسي يتطور ويزداد تعقيداً",
                tags=["نمط", "تطوير", "هندسي", "معقد"],
                cultural_significance="نمو التعقيد في الطبيعة والفن",
                mathematical_beauty=0.9
            ),
            equations=[
                ShapeEquation(
                    equation_type="quantum_sigmoid",
                    parameters={"n": 4, "k": 1.5, "x0": 0.0, "alpha": 1.0, "complexity_factor": 1.0},
                    description="النمط الأساسي"
                ),
                ShapeEquation(
                    equation_type="sigmoid",
                    parameters={"n": 8, "k": 1.0, "x0": 0.0, "alpha": 0.8, "detail_factor": 1.0},
                    description="التفاصيل المضافة"
                )
            ],
            animation_frames=[
                {
                    "frame": i,
                    "complexity_level": i + 1,
                    "detail_density": i * 0.1,
                    "symmetry_order": 4 + i,
                    "fractal_depth": min(i, 5)
                }
                for i in range(8)
            ],
            visual_properties={
                "fractal": True,
                "self_similar": True,
                "increasing_complexity": True,
                "mathematical": True
            }
        )
        self._add_shape(evolving_pattern)

        print(f"   ✅ تم إضافة {len([s for s in self.shapes.values() if s.shape_type == ShapeType.ABSTRACT])} مثال تحويل وتكيف")

    def get_transformation_sequence(self, source_shape_id: str, target_shape_id: str, steps: int = 10) -> List[Dict]:
        """إنشاء تسلسل تحويل بين شكلين."""

        source_shape = self.get_shape(source_shape_id)
        target_shape = self.get_shape(target_shape_id)

        if not source_shape or not target_shape:
            return []

        transformation_sequence = []

        for i in range(steps + 1):
            t = i / steps  # معامل التحويل من 0 إلى 1

            # حساب المعادلات المتوسطة
            blended_equations = []

            # دمج معادلات المصدر والهدف
            max_equations = max(len(source_shape.equations), len(target_shape.equations))

            for j in range(max_equations):
                source_eq = source_shape.equations[j] if j < len(source_shape.equations) else source_shape.equations[-1]
                target_eq = target_shape.equations[j] if j < len(target_shape.equations) else target_shape.equations[-1]

                # دمج المعاملات
                blended_params = {}
                all_params = set(source_eq.parameters.keys()) | set(target_eq.parameters.keys())

                for param in all_params:
                    source_val = source_eq.parameters.get(param, 0.0)
                    target_val = target_eq.parameters.get(param, 0.0)
                    blended_params[param] = source_val * (1 - t) + target_val * t

                blended_equations.append(ShapeEquation(
                    equation_type="mixed",
                    parameters=blended_params,
                    description=f"تحويل خطوة {i+1}"
                ))

            # دمج الخصائص البصرية
            blended_properties = {}
            if hasattr(source_shape.visual_properties, 'get') and hasattr(target_shape.visual_properties, 'get'):
                # دمج الألوان إذا كانت موجودة
                if 'color' in source_shape.visual_properties and 'color' in target_shape.visual_properties:
                    # هنا يمكن إضافة دمج الألوان
                    blended_properties['color'] = target_shape.visual_properties['color'] if t > 0.5 else source_shape.visual_properties['color']

            transformation_sequence.append({
                'step': i,
                'progress': t,
                'equations': blended_equations,
                'visual_properties': blended_properties,
                'description': f"تحويل من {source_shape.metadata.name_ar} إلى {target_shape.metadata.name_ar} - خطوة {i+1}/{steps+1}"
            })

        return transformation_sequence

    def get_database_summary(self) -> Dict[str, Any]:
        """الحصول على ملخص قاعدة البيانات."""

        summary = {
            'database_id': self.database_id,
            'total_shapes': len(self.shapes),
            'shapes_by_type': {
                shape_type.value: len(shape_ids)
                for shape_type, shape_ids in self.shape_categories.items()
            },
            'shapes_by_complexity': {
                complexity.value: len(shape_ids)
                for complexity, shape_ids in self.complexity_index.items()
            },
            'animated_shapes': len([
                shape for shape in self.shapes.values()
                if shape.animation_frames is not None
            ]),
            'mathematical_beauty_average': np.mean([
                shape.metadata.mathematical_beauty
                for shape in self.shapes.values()
            ]),
            'creation_date': min([
                shape.creation_date for shape in self.shapes.values()
            ]) if self.shapes else datetime.now().isoformat(),
            'shape_list': [
                {
                    'id': shape.shape_id,
                    'name_ar': shape.metadata.name_ar,
                    'name_en': shape.metadata.name_en,
                    'type': shape.shape_type.value,
                    'complexity': shape.complexity_level.value,
                    'beauty_score': shape.metadata.mathematical_beauty
                }
                for shape in self.shapes.values()
            ]
        }

        return summary

    def export_database(self, filename: str = None) -> str:
        """تصدير قاعدة البيانات إلى ملف JSON."""

        if filename is None:
            filename = f"shapes_database_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        export_data = {
            'database_info': {
                'id': self.database_id,
                'export_date': datetime.now().isoformat(),
                'total_shapes': len(self.shapes)
            },
            'shapes': {}
        }

        # تحويل الأشكال إلى تنسيق قابل للتسلسل
        for shape_id, shape in self.shapes.items():
            export_data['shapes'][shape_id] = {
                'shape_id': shape.shape_id,
                'shape_type': shape.shape_type.value,
                'complexity_level': shape.complexity_level.value,
                'metadata': {
                    'name_ar': shape.metadata.name_ar,
                    'name_en': shape.metadata.name_en,
                    'description': shape.metadata.description,
                    'tags': shape.metadata.tags,
                    'cultural_significance': shape.metadata.cultural_significance,
                    'mathematical_beauty': shape.metadata.mathematical_beauty
                },
                'equations': [
                    {
                        'equation_type': eq.equation_type,
                        'parameters': eq.parameters,
                        'domain': eq.domain,
                        'description': eq.description
                    }
                    for eq in shape.equations
                ],
                'animation_frames': shape.animation_frames,
                'visual_properties': shape.visual_properties,
                'creation_date': shape.creation_date
            }

        # حفظ الملف
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)

        return filename
