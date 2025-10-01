#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
التكامل الدلالي لنظام بصيرة

هذا الملف يحتوي على تنفيذ وحدة التكامل الدلالي، وهي مكون مسؤول عن ربط
المعادلات والأشكال بالمفاهيم الدلالية، وتمثيل المعرفة، وتسهيل التفاعل
بين النواة الرياضية والنواة الكونية.

المؤلف: فريق تطوير نظام بصيرة
الإصدار: 1.0.0
التاريخ: 2 يونيو 2025
"""

import os
import sys
import numpy as np
import sympy as sp
import torch
import torch.nn as nn
import torch.optim as optim
from typing import Dict, List, Tuple, Union, Optional, Any, Callable, Set
import random
import copy
import uuid
from datetime import datetime
import logging
from enum import Enum
from dataclasses import dataclass, field
import json
import re
from collections import defaultdict

# استيراد من الوحدات الأخرى
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.symbolic_engine import AdvancedSymbolicExpression, SymbolicMetadata
from core.adaptive_calculus import QuantumAdaptiveCalculus, CalculusContext
from core.equation_evolution import AdvancedEquationEvolution, EvolutionContext, EvolutionStrategy, EvolutionDirection, EvolutionResult
from core.advanced_shape_equation import AdvancedShapeEquation, ShapeDimension, ShapeComponent
from core.expert_system import AdvancedExpertSystem, KnowledgeItem, KnowledgeType, InferenceContext, InferenceMethod
from core.evolutionary_explorer import EvolutionaryExplorer, ExplorationMode, ExplorationConfig, ExplorationResult

# إعداد التسجيل
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("semantic_integration")


class SemanticDomain(str, Enum):
    """مجالات دلالية."""
    MATHEMATICS = "mathematics"  # الرياضيات
    PHYSICS = "physics"  # الفيزياء
    BIOLOGY = "biology"  # الأحياء
    CHEMISTRY = "chemistry"  # الكيمياء
    ASTRONOMY = "astronomy"  # الفلك
    GEOLOGY = "geology"  # الجيولوجيا
    PSYCHOLOGY = "psychology"  # علم النفس
    SOCIOLOGY = "sociology"  # علم الاجتماع
    ECONOMICS = "economics"  # الاقتصاد
    COMPUTER_SCIENCE = "computer_science"  # علوم الحاسوب
    PHILOSOPHY = "philosophy"  # الفلسفة
    ARTS = "arts"  # الفنون
    LINGUISTICS = "linguistics"  # اللغويات
    MEDICINE = "medicine"  # الطب
    ENGINEERING = "engineering"  # الهندسة
    QUANTUM_PHYSICS = "quantum_physics"  # الفيزياء الكمية
    COSMOLOGY = "cosmology"  # علم الكون
    METAPHYSICS = "metaphysics"  # الميتافيزيقا
    UNIVERSAL = "universal"  # عام


class SemanticRelationType(str, Enum):
    """أنواع العلاقات الدلالية."""
    IS_A = "is_a"  # هو
    PART_OF = "part_of"  # جزء من
    HAS_PROPERTY = "has_property"  # له خاصية
    CAUSES = "causes"  # يسبب
    AFFECTS = "affects"  # يؤثر على
    SIMILAR_TO = "similar_to"  # مشابه لـ
    OPPOSITE_OF = "opposite_of"  # عكس
    DERIVED_FROM = "derived_from"  # مشتق من
    TRANSFORMS_TO = "transforms_to"  # يتحول إلى
    REPRESENTS = "represents"  # يمثل
    SYMBOLIZES = "symbolizes"  # يرمز إلى
    EMERGES_FROM = "emerges_from"  # ينبثق من
    PERPENDICULAR_TO = "perpendicular_to"  # متعامد مع
    PARALLEL_TO = "parallel_to"  # موازي لـ
    INTERACTS_WITH = "interacts_with"  # يتفاعل مع
    QUANTUM_ENTANGLED = "quantum_entangled"  # متشابك كمياً
    REVOLUTIONARY_PAIR = "revolutionary_pair"  # زوج ثوري


@dataclass
class SemanticConcept:
    """مفهوم دلالي."""
    id: str = field(default_factory=lambda: f"concept_{uuid.uuid4()}")
    name: str  # اسم المفهوم
    description: str  # وصف المفهوم
    domains: List[SemanticDomain] = field(default_factory=list)  # المجالات الدلالية
    properties: Dict[str, Any] = field(default_factory=dict)  # خصائص المفهوم
    metadata: Dict[str, Any] = field(default_factory=dict)  # بيانات وصفية
    
    def to_dict(self) -> Dict[str, Any]:
        """تحويل المفهوم إلى قاموس."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "domains": [domain.value for domain in self.domains],
            "properties": self.properties,
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SemanticConcept':
        """إنشاء مفهوم من قاموس."""
        domains = [SemanticDomain(domain) for domain in data.get("domains", [])]
        return cls(
            id=data.get("id", f"concept_{uuid.uuid4()}"),
            name=data.get("name", ""),
            description=data.get("description", ""),
            domains=domains,
            properties=data.get("properties", {}),
            metadata=data.get("metadata", {})
        )


@dataclass
class SemanticRelation:
    """علاقة دلالية."""
    id: str = field(default_factory=lambda: f"relation_{uuid.uuid4()}")
    source_id: str  # معرف المصدر
    target_id: str  # معرف الهدف
    relation_type: SemanticRelationType  # نوع العلاقة
    weight: float = 1.0  # وزن العلاقة
    properties: Dict[str, Any] = field(default_factory=dict)  # خصائص العلاقة
    metadata: Dict[str, Any] = field(default_factory=dict)  # بيانات وصفية
    
    def to_dict(self) -> Dict[str, Any]:
        """تحويل العلاقة إلى قاموس."""
        return {
            "id": self.id,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "relation_type": self.relation_type.value,
            "weight": self.weight,
            "properties": self.properties,
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SemanticRelation':
        """إنشاء علاقة من قاموس."""
        relation_type = SemanticRelationType(data.get("relation_type", "is_a"))
        return cls(
            id=data.get("id", f"relation_{uuid.uuid4()}"),
            source_id=data.get("source_id", ""),
            target_id=data.get("target_id", ""),
            relation_type=relation_type,
            weight=data.get("weight", 1.0),
            properties=data.get("properties", {}),
            metadata=data.get("metadata", {})
        )


@dataclass
class SemanticMapping:
    """تخطيط دلالي."""
    id: str = field(default_factory=lambda: f"mapping_{uuid.uuid4()}")
    equation_id: str  # معرف المعادلة
    concept_id: str  # معرف المفهوم
    mapping_type: str  # نوع التخطيط (مثل "direct", "symbolic", "metaphorical")
    confidence: float = 1.0  # درجة الثقة
    properties: Dict[str, Any] = field(default_factory=dict)  # خصائص التخطيط
    metadata: Dict[str, Any] = field(default_factory=dict)  # بيانات وصفية
    
    def to_dict(self) -> Dict[str, Any]:
        """تحويل التخطيط إلى قاموس."""
        return {
            "id": self.id,
            "equation_id": self.equation_id,
            "concept_id": self.concept_id,
            "mapping_type": self.mapping_type,
            "confidence": self.confidence,
            "properties": self.properties,
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SemanticMapping':
        """إنشاء تخطيط من قاموس."""
        return cls(
            id=data.get("id", f"mapping_{uuid.uuid4()}"),
            equation_id=data.get("equation_id", ""),
            concept_id=data.get("concept_id", ""),
            mapping_type=data.get("mapping_type", "direct"),
            confidence=data.get("confidence", 1.0),
            properties=data.get("properties", {}),
            metadata=data.get("metadata", {})
        )


@dataclass
class SemanticQuery:
    """استعلام دلالي."""
    query_type: str  # نوع الاستعلام (مثل "concept", "relation", "mapping")
    parameters: Dict[str, Any] = field(default_factory=dict)  # معلمات الاستعلام
    max_results: int = 10  # أقصى عدد للنتائج
    min_confidence: float = 0.5  # أدنى درجة ثقة
    custom_properties: Dict[str, Any] = field(default_factory=dict)  # خصائص مخصصة


@dataclass
class SemanticQueryResult:
    """نتيجة استعلام دلالي."""
    results: List[Dict[str, Any]] = field(default_factory=list)  # النتائج
    count: int = 0  # عدد النتائج
    success: bool = False  # نجاح الاستعلام
    message: str = ""  # رسالة الاستعلام


class SemanticIntegration:
    """
    التكامل الدلالي لنظام بصيرة.
    
    يربط المعادلات والأشكال بالمفاهيم الدلالية، ويمثل المعرفة،
    ويسهل التفاعل بين النواة الرياضية والنواة الكونية.
    """
    
    def __init__(self, knowledge_base_path: Optional[str] = None):
        """
        تهيئة التكامل الدلالي.
        
        Args:
            knowledge_base_path: مسار ملف قاعدة المعرفة الدلالية (JSON)
        """
        # قواميس المفاهيم والعلاقات والتخطيطات
        self.concepts: Dict[str, SemanticConcept] = {}
        self.relations: Dict[str, SemanticRelation] = {}
        self.mappings: Dict[str, SemanticMapping] = {}
        
        # قواميس مساعدة للبحث السريع
        self.concepts_by_name: Dict[str, List[str]] = defaultdict(list)  # اسم المفهوم -> قائمة معرفات المفاهيم
        self.concepts_by_domain: Dict[SemanticDomain, List[str]] = defaultdict(list)  # المجال -> قائمة معرفات المفاهيم
        self.relations_by_source: Dict[str, List[str]] = defaultdict(list)  # معرف المصدر -> قائمة معرفات العلاقات
        self.relations_by_target: Dict[str, List[str]] = defaultdict(list)  # معرف الهدف -> قائمة معرفات العلاقات
        self.relations_by_type: Dict[SemanticRelationType, List[str]] = defaultdict(list)  # نوع العلاقة -> قائمة معرفات العلاقات
        self.mappings_by_equation: Dict[str, List[str]] = defaultdict(list)  # معرف المعادلة -> قائمة معرفات التخطيطات
        self.mappings_by_concept: Dict[str, List[str]] = defaultdict(list)  # معرف المفهوم -> قائمة معرفات التخطيطات
        
        # تحميل قاعدة المعرفة الدلالية
        if knowledge_base_path:
            self.load_knowledge_base(knowledge_base_path)
        else:
            # تهيئة قاعدة المعرفة الدلالية بمفاهيم أساسية
            self._initialize_basic_concepts()
        
        logger.info("تم تهيئة التكامل الدلالي")
    
    def _initialize_basic_concepts(self):
        """تهيئة قاعدة المعرفة الدلالية بمفاهيم أساسية."""
        # مفاهيم رياضية أساسية
        self.add_concept(SemanticConcept(
            name="معادلة",
            description="تعبير رياضي يساوي بين كميتين",
            domains=[SemanticDomain.MATHEMATICS],
            properties={"abstract": True, "symbolic": True}
        ))
        
        self.add_concept(SemanticConcept(
            name="دالة",
            description="علاقة رياضية تربط عناصر مجموعة بعناصر مجموعة أخرى",
            domains=[SemanticDomain.MATHEMATICS],
            properties={"abstract": True, "symbolic": True}
        ))
        
        self.add_concept(SemanticConcept(
            name="متغير",
            description="رمز يمثل قيمة غير معروفة أو متغيرة",
            domains=[SemanticDomain.MATHEMATICS],
            properties={"abstract": True, "symbolic": True}
        ))
        
        self.add_concept(SemanticConcept(
            name="ثابت",
            description="قيمة لا تتغير في سياق معين",
            domains=[SemanticDomain.MATHEMATICS],
            properties={"abstract": True, "symbolic": True}
        ))
        
        self.add_concept(SemanticConcept(
            name="شكل",
            description="تمثيل هندسي لمجموعة من النقاط",
            domains=[SemanticDomain.MATHEMATICS],
            properties={"abstract": True, "geometric": True}
        ))
        
        # مفاهيم فيزيائية أساسية
        self.add_concept(SemanticConcept(
            name="كتلة",
            description="مقياس لمقدار المادة في جسم ما",
            domains=[SemanticDomain.PHYSICS],
            properties={"physical": True, "measurable": True}
        ))
        
        self.add_concept(SemanticConcept(
            name="قوة",
            description="تأثير يغير حالة حركة جسم ما",
            domains=[SemanticDomain.PHYSICS],
            properties={"physical": True, "measurable": True, "vector": True}
        ))
        
        self.add_concept(SemanticConcept(
            name="طاقة",
            description="القدرة على القيام بعمل",
            domains=[SemanticDomain.PHYSICS],
            properties={"physical": True, "measurable": True, "conserved": True}
        ))
        
        # مفاهيم كمية أساسية
        self.add_concept(SemanticConcept(
            name="تراكب كمي",
            description="حالة كمية تكون فيها الجسيمات في حالات متعددة في نفس الوقت",
            domains=[SemanticDomain.QUANTUM_PHYSICS],
            properties={"quantum": True, "non_classical": True}
        ))
        
        self.add_concept(SemanticConcept(
            name="تشابك كمي",
            description="ظاهرة كمية تربط جسيمات بحيث لا يمكن وصف حالة أحدها بشكل مستقل عن الآخر",
            domains=[SemanticDomain.QUANTUM_PHYSICS],
            properties={"quantum": True, "non_classical": True, "non_local": True}
        ))
        
        # مفاهيم ثورية أساسية
        self.add_concept(SemanticConcept(
            name="صفر",
            description="مفهوم العدم أو غياب الكمية",
            domains=[SemanticDomain.MATHEMATICS, SemanticDomain.PHILOSOPHY],
            properties={"abstract": True, "fundamental": True, "revolutionary": True}
        ))
        
        self.add_concept(SemanticConcept(
            name="تعامد الأضداد",
            description="مفهوم ثوري يشير إلى أن الأضداد تكون متعامدة وليست متقابلة",
            domains=[SemanticDomain.PHILOSOPHY, SemanticDomain.METAPHYSICS],
            properties={"abstract": True, "revolutionary": True}
        ))
        
        self.add_concept(SemanticConcept(
            name="خيط",
            description="مفهوم ثوري يشير إلى بنية أساسية تربط الكتلة والفضاء",
            domains=[SemanticDomain.PHILOSOPHY, SemanticDomain.PHYSICS, SemanticDomain.METAPHYSICS],
            properties={"abstract": True, "revolutionary": True, "fundamental": True}
        ))
        
        # إضافة علاقات أساسية
        # علاقة بين الدالة والمعادلة
        function_id = self.get_concept_by_name("دالة")[0].id
        equation_id = self.get_concept_by_name("معادلة")[0].id
        self.add_relation(SemanticRelation(
            source_id=function_id,
            target_id=equation_id,
            relation_type=SemanticRelationType.IS_A,
            weight=0.8
        ))
        
        # علاقة بين المتغير والثابت
        variable_id = self.get_concept_by_name("متغير")[0].id
        constant_id = self.get_concept_by_name("ثابت")[0].id
        self.add_relation(SemanticRelation(
            source_id=variable_id,
            target_id=constant_id,
            relation_type=SemanticRelationType.OPPOSITE_OF,
            weight=0.9
        ))
        
        # علاقة بين الكتلة والطاقة
        mass_id = self.get_concept_by_name("كتلة")[0].id
        energy_id = self.get_concept_by_name("طاقة")[0].id
        self.add_relation(SemanticRelation(
            source_id=mass_id,
            target_id=energy_id,
            relation_type=SemanticRelationType.TRANSFORMS_TO,
            weight=1.0,
            properties={"equation": "E=mc^2"}
        ))
        
        # علاقة بين التراكب الكمي والتشابك الكمي
        superposition_id = self.get_concept_by_name("تراكب كمي")[0].id
        entanglement_id = self.get_concept_by_name("تشابك كمي")[0].id
        self.add_relation(SemanticRelation(
            source_id=superposition_id,
            target_id=entanglement_id,
            relation_type=SemanticRelationType.INTERACTS_WITH,
            weight=0.9
        ))
        
        # علاقات ثورية
        zero_id = self.get_concept_by_name("صفر")[0].id
        perpendicular_id = self.get_concept_by_name("تعامد الأضداد")[0].id
        filament_id = self.get_concept_by_name("خيط")[0].id
        
        self.add_relation(SemanticRelation(
            source_id=zero_id,
            target_id=perpendicular_id,
            relation_type=SemanticRelationType.CAUSES,
            weight=1.0,
            properties={"revolutionary": True}
        ))
        
        self.add_relation(SemanticRelation(
            source_id=perpendicular_id,
            target_id=filament_id,
            relation_type=SemanticRelationType.EMERGES_FROM,
            weight=1.0,
            properties={"revolutionary": True}
        ))
        
        self.add_relation(SemanticRelation(
            source_id=mass_id,
            target_id=filament_id,
            relation_type=SemanticRelationType.PERPENDICULAR_TO,
            weight=0.9,
            properties={"revolutionary": True}
        ))
        
        logger.info("تم تهيئة قاعدة المعرفة الدلالية بمفاهيم أساسية")
    
    def add_concept(self, concept: SemanticConcept) -> str:
        """
        إضافة مفهوم دلالي.
        
        Args:
            concept: المفهوم الدلالي
            
        Returns:
            معرف المفهوم
        """
        self.concepts[concept.id] = concept
        self.concepts_by_name[concept.name].append(concept.id)
        
        for domain in concept.domains:
            self.concepts_by_domain[domain].append(concept.id)
        
        logger.debug(f"تمت إضافة المفهوم: {concept.name} ({concept.id})")
        
        return concept.id
    
    def add_relation(self, relation: SemanticRelation) -> str:
        """
        إضافة علاقة دلالية.
        
        Args:
            relation: العلاقة الدلالية
            
        Returns:
            معرف العلاقة
        """
        # التحقق من وجود المفاهيم
        if relation.source_id not in self.concepts:
            raise ValueError(f"المفهوم المصدر غير موجود: {relation.source_id}")
        
        if relation.target_id not in self.concepts:
            raise ValueError(f"المفهوم الهدف غير موجود: {relation.target_id}")
        
        self.relations[relation.id] = relation
        self.relations_by_source[relation.source_id].append(relation.id)
        self.relations_by_target[relation.target_id].append(relation.id)
        self.relations_by_type[relation.relation_type].append(relation.id)
        
        logger.debug(f"تمت إضافة العلاقة: {relation.relation_type} ({relation.id})")
        
        return relation.id
    
    def add_mapping(self, mapping: SemanticMapping) -> str:
        """
        إضافة تخطيط دلالي.
        
        Args:
            mapping: التخطيط الدلالي
            
        Returns:
            معرف التخطيط
        """
        # التحقق من وجود المفهوم
        if mapping.concept_id not in self.concepts:
            raise ValueError(f"المفهوم غير موجود: {mapping.concept_id}")
        
        self.mappings[mapping.id] = mapping
        self.mappings_by_equation[mapping.equation_id].append(mapping.id)
        self.mappings_by_concept[mapping.concept_id].append(mapping.id)
        
        logger.debug(f"تمت إضافة التخطيط: {mapping.mapping_type} ({mapping.id})")
        
        return mapping.id
    
    def get_concept(self, concept_id: str) -> Optional[SemanticConcept]:
        """
        الحصول على مفهوم دلالي بواسطة المعرف.
        
        Args:
            concept_id: معرف المفهوم
            
        Returns:
            المفهوم الدلالي أو None إذا لم يكن موجوداً
        """
        return self.concepts.get(concept_id)
    
    def get_concept_by_name(self, name: str) -> List[SemanticConcept]:
        """
        الحصول على مفاهيم دلالية بواسطة الاسم.
        
        Args:
            name: اسم المفهوم
            
        Returns:
            قائمة المفاهيم الدلالية
        """
        concept_ids = self.concepts_by_name.get(name, [])
        return [self.concepts[concept_id] for concept_id in concept_ids]
    
    def get_concepts_by_domain(self, domain: SemanticDomain) -> List[SemanticConcept]:
        """
        الحصول على مفاهيم دلالية بواسطة المجال.
        
        Args:
            domain: المجال الدلالي
            
        Returns:
            قائمة المفاهيم الدلالية
        """
        concept_ids = self.concepts_by_domain.get(domain, [])
        return [self.concepts[concept_id] for concept_id in concept_ids]
    
    def get_relation(self, relation_id: str) -> Optional[SemanticRelation]:
        """
        الحصول على علاقة دلالية بواسطة المعرف.
        
        Args:
            relation_id: معرف العلاقة
            
        Returns:
            العلاقة الدلالية أو None إذا لم تكن موجودة
        """
        return self.relations.get(relation_id)
    
    def get_relations_by_source(self, source_id: str) -> List[SemanticRelation]:
        """
        الحصول على علاقات دلالية بواسطة معرف المصدر.
        
        Args:
            source_id: معرف المصدر
            
        Returns:
            قائمة العلاقات الدلالية
        """
        relation_ids = self.relations_by_source.get(source_id, [])
        return [self.relations[relation_id] for relation_id in relation_ids]
    
    def get_relations_by_target(self, target_id: str) -> List[SemanticRelation]:
        """
        الحصول على علاقات دلالية بواسطة معرف الهدف.
        
        Args:
            target_id: معرف الهدف
            
        Returns:
            قائمة العلاقات الدلالية
        """
        relation_ids = self.relations_by_target.get(target_id, [])
        return [self.relations[relation_id] for relation_id in relation_ids]
    
    def get_relations_by_type(self, relation_type: SemanticRelationType) -> List[SemanticRelation]:
        """
        الحصول على علاقات دلالية بواسطة نوع العلاقة.
        
        Args:
            relation_type: نوع العلاقة
            
        Returns:
            قائمة العلاقات الدلالية
        """
        relation_ids = self.relations_by_type.get(relation_type, [])
        return [self.relations[relation_id] for relation_id in relation_ids]
    
    def get_mapping(self, mapping_id: str) -> Optional[SemanticMapping]:
        """
        الحصول على تخطيط دلالي بواسطة المعرف.
        
        Args:
            mapping_id: معرف التخطيط
            
        Returns:
            التخطيط الدلالي أو None إذا لم يكن موجوداً
        """
        return self.mappings.get(mapping_id)
    
    def get_mappings_by_equation(self, equation_id: str) -> List[SemanticMapping]:
        """
        الحصول على تخطيطات دلالية بواسطة معرف المعادلة.
        
        Args:
            equation_id: معرف المعادلة
            
        Returns:
            قائمة التخطيطات الدلالية
        """
        mapping_ids = self.mappings_by_equation.get(equation_id, [])
        return [self.mappings[mapping_id] for mapping_id in mapping_ids]
    
    def get_mappings_by_concept(self, concept_id: str) -> List[SemanticMapping]:
        """
        الحصول على تخطيطات دلالية بواسطة معرف المفهوم.
        
        Args:
            concept_id: معرف المفهوم
            
        Returns:
            قائمة التخطيطات الدلالية
        """
        mapping_ids = self.mappings_by_concept.get(concept_id, [])
        return [self.mappings[mapping_id] for mapping_id in mapping_ids]
    
    def remove_concept(self, concept_id: str):
        """
        إزالة مفهوم دلالي.
        
        Args:
            concept_id: معرف المفهوم
        """
        if concept_id not in self.concepts:
            logger.warning(f"المفهوم غير موجود: {concept_id}")
            return
        
        concept = self.concepts[concept_id]
        
        # إزالة المفهوم من القواميس المساعدة
        self.concepts_by_name[concept.name].remove(concept_id)
        if not self.concepts_by_name[concept.name]:
            del self.concepts_by_name[concept.name]
        
        for domain in concept.domains:
            self.concepts_by_domain[domain].remove(concept_id)
            if not self.concepts_by_domain[domain]:
                del self.concepts_by_domain[domain]
        
        # إزالة العلاقات المرتبطة بالمفهوم
        relation_ids_to_remove = []
        relation_ids_to_remove.extend(self.relations_by_source.get(concept_id, []))
        relation_ids_to_remove.extend(self.relations_by_target.get(concept_id, []))
        
        for relation_id in relation_ids_to_remove:
            self.remove_relation(relation_id)
        
        # إزالة التخطيطات المرتبطة بالمفهوم
        mapping_ids_to_remove = self.mappings_by_concept.get(concept_id, [])
        for mapping_id in mapping_ids_to_remove:
            self.remove_mapping(mapping_id)
        
        # إزالة المفهوم
        del self.concepts[concept_id]
        
        logger.debug(f"تمت إزالة المفهوم: {concept.name} ({concept_id})")
    
    def remove_relation(self, relation_id: str):
        """
        إزالة علاقة دلالية.
        
        Args:
            relation_id: معرف العلاقة
        """
        if relation_id not in self.relations:
            logger.warning(f"العلاقة غير موجودة: {relation_id}")
            return
        
        relation = self.relations[relation_id]
        
        # إزالة العلاقة من القواميس المساعدة
        self.relations_by_source[relation.source_id].remove(relation_id)
        if not self.relations_by_source[relation.source_id]:
            del self.relations_by_source[relation.source_id]
        
        self.relations_by_target[relation.target_id].remove(relation_id)
        if not self.relations_by_target[relation.target_id]:
            del self.relations_by_target[relation.target_id]
        
        self.relations_by_type[relation.relation_type].remove(relation_id)
        if not self.relations_by_type[relation.relation_type]:
            del self.relations_by_type[relation.relation_type]
        
        # إزالة العلاقة
        del self.relations[relation_id]
        
        logger.debug(f"تمت إزالة العلاقة: {relation.relation_type} ({relation_id})")
    
    def remove_mapping(self, mapping_id: str):
        """
        إزالة تخطيط دلالي.
        
        Args:
            mapping_id: معرف التخطيط
        """
        if mapping_id not in self.mappings:
            logger.warning(f"التخطيط غير موجود: {mapping_id}")
            return
        
        mapping = self.mappings[mapping_id]
        
        # إزالة التخطيط من القواميس المساعدة
        self.mappings_by_equation[mapping.equation_id].remove(mapping_id)
        if not self.mappings_by_equation[mapping.equation_id]:
            del self.mappings_by_equation[mapping.equation_id]
        
        self.mappings_by_concept[mapping.concept_id].remove(mapping_id)
        if not self.mappings_by_concept[mapping.concept_id]:
            del self.mappings_by_concept[mapping.concept_id]
        
        # إزالة التخطيط
        del self.mappings[mapping_id]
        
        logger.debug(f"تمت إزالة التخطيط: {mapping.mapping_type} ({mapping_id})")
    
    def save_knowledge_base(self, file_path: str):
        """
        حفظ قاعدة المعرفة الدلالية في ملف JSON.
        
        Args:
            file_path: مسار الملف
        """
        try:
            data = {
                "concepts": {concept_id: concept.to_dict() for concept_id, concept in self.concepts.items()},
                "relations": {relation_id: relation.to_dict() for relation_id, relation in self.relations.items()},
                "mappings": {mapping_id: mapping.to_dict() for mapping_id, mapping in self.mappings.items()}
            }
            
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            
            logger.info(f"تم حفظ قاعدة المعرفة الدلالية في: {file_path}")
        except Exception as e:
            logger.error(f"خطأ في حفظ قاعدة المعرفة الدلالية: {str(e)}")
    
    def load_knowledge_base(self, file_path: str):
        """
        تحميل قاعدة المعرفة الدلالية من ملف JSON.
        
        Args:
            file_path: مسار الملف
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # تحميل المفاهيم
            self.concepts = {}
            self.concepts_by_name = defaultdict(list)
            self.concepts_by_domain = defaultdict(list)
            
            for concept_id, concept_data in data.get("concepts", {}).items():
                concept = SemanticConcept.from_dict(concept_data)
                self.concepts[concept_id] = concept
                self.concepts_by_name[concept.name].append(concept_id)
                
                for domain in concept.domains:
                    self.concepts_by_domain[domain].append(concept_id)
            
            # تحميل العلاقات
            self.relations = {}
            self.relations_by_source = defaultdict(list)
            self.relations_by_target = defaultdict(list)
            self.relations_by_type = defaultdict(list)
            
            for relation_id, relation_data in data.get("relations", {}).items():
                relation = SemanticRelation.from_dict(relation_data)
                self.relations[relation_id] = relation
                self.relations_by_source[relation.source_id].append(relation_id)
                self.relations_by_target[relation.target_id].append(relation_id)
                self.relations_by_type[relation.relation_type].append(relation_id)
            
            # تحميل التخطيطات
            self.mappings = {}
            self.mappings_by_equation = defaultdict(list)
            self.mappings_by_concept = defaultdict(list)
            
            for mapping_id, mapping_data in data.get("mappings", {}).items():
                mapping = SemanticMapping.from_dict(mapping_data)
                self.mappings[mapping_id] = mapping
                self.mappings_by_equation[mapping.equation_id].append(mapping_id)
                self.mappings_by_concept[mapping.concept_id].append(mapping_id)
            
            logger.info(f"تم تحميل قاعدة المعرفة الدلالية من: {file_path}")
            logger.info(f"تم تحميل {len(self.concepts)} مفهوم، {len(self.relations)} علاقة، {len(self.mappings)} تخطيط")
        except FileNotFoundError:
            logger.warning(f"ملف قاعدة المعرفة الدلالية غير موجود: {file_path}")
            # تهيئة قاعدة المعرفة الدلالية بمفاهيم أساسية
            self._initialize_basic_concepts()
        except Exception as e:
            logger.error(f"خطأ في تحميل قاعدة المعرفة الدلالية: {str(e)}")
            # تهيئة قاعدة المعرفة الدلالية بمفاهيم أساسية
            self._initialize_basic_concepts()
    
    def query(self, query: SemanticQuery) -> SemanticQueryResult:
        """
        تنفيذ استعلام دلالي.
        
        Args:
            query: الاستعلام الدلالي
            
        Returns:
            نتيجة الاستعلام الدلالي
        """
        if query.query_type == "concept":
            return self._query_concepts(query)
        elif query.query_type == "relation":
            return self._query_relations(query)
        elif query.query_type == "mapping":
            return self._query_mappings(query)
        elif query.query_type == "path":
            return self._query_path(query)
        else:
            return SemanticQueryResult(
                success=False,
                message=f"نوع استعلام غير معروف: {query.query_type}"
            )
    
    def _query_concepts(self, query: SemanticQuery) -> SemanticQueryResult:
        """
        تنفيذ استعلام عن المفاهيم.
        
        Args:
            query: الاستعلام الدلالي
            
        Returns:
            نتيجة الاستعلام الدلالي
        """
        results = []
        
        # البحث حسب المعرف
        concept_id = query.parameters.get("id")
        if concept_id:
            concept = self.get_concept(concept_id)
            if concept:
                results.append(concept.to_dict())
        
        # البحث حسب الاسم
        name = query.parameters.get("name")
        if name:
            concepts = self.get_concept_by_name(name)
            for concept in concepts:
                results.append(concept.to_dict())
        
        # البحث حسب المجال
        domain_str = query.parameters.get("domain")
        if domain_str:
            try:
                domain = SemanticDomain(domain_str)
                concepts = self.get_concepts_by_domain(domain)
                for concept in concepts:
                    results.append(concept.to_dict())
            except ValueError:
                pass
        
        # البحث حسب الخصائص
        properties = query.parameters.get("properties", {})
        if properties:
            for concept_id, concept in self.concepts.items():
                match = True
                for key, value in properties.items():
                    if concept.properties.get(key) != value:
                        match = False
                        break
                
                if match:
                    results.append(concept.to_dict())
        
        # إذا لم يتم تحديد أي معلمات، إرجاع جميع المفاهيم
        if not concept_id and not name and not domain_str and not properties:
            for concept_id, concept in self.concepts.items():
                results.append(concept.to_dict())
        
        # تحديد النتائج حسب عدد النتائج المطلوب
        results = results[:query.max_results]
        
        return SemanticQueryResult(
            results=results,
            count=len(results),
            success=True,
            message=f"تم العثور على {len(results)} مفهوم"
        )
    
    def _query_relations(self, query: SemanticQuery) -> SemanticQueryResult:
        """
        تنفيذ استعلام عن العلاقات.
        
        Args:
            query: الاستعلام الدلالي
            
        Returns:
            نتيجة الاستعلام الدلالي
        """
        results = []
        
        # البحث حسب المعرف
        relation_id = query.parameters.get("id")
        if relation_id:
            relation = self.get_relation(relation_id)
            if relation:
                results.append(relation.to_dict())
        
        # البحث حسب معرف المصدر
        source_id = query.parameters.get("source_id")
        if source_id:
            relations = self.get_relations_by_source(source_id)
            for relation in relations:
                results.append(relation.to_dict())
        
        # البحث حسب معرف الهدف
        target_id = query.parameters.get("target_id")
        if target_id:
            relations = self.get_relations_by_target(target_id)
            for relation in relations:
                results.append(relation.to_dict())
        
        # البحث حسب نوع العلاقة
        relation_type_str = query.parameters.get("relation_type")
        if relation_type_str:
            try:
                relation_type = SemanticRelationType(relation_type_str)
                relations = self.get_relations_by_type(relation_type)
                for relation in relations:
                    results.append(relation.to_dict())
            except ValueError:
                pass
        
        # البحث حسب الوزن
        min_weight = query.parameters.get("min_weight")
        if min_weight is not None:
            min_weight = float(min_weight)
            for relation_id, relation in self.relations.items():
                if relation.weight >= min_weight:
                    results.append(relation.to_dict())
        
        # البحث حسب الخصائص
        properties = query.parameters.get("properties", {})
        if properties:
            for relation_id, relation in self.relations.items():
                match = True
                for key, value in properties.items():
                    if relation.properties.get(key) != value:
                        match = False
                        break
                
                if match:
                    results.append(relation.to_dict())
        
        # إذا لم يتم تحديد أي معلمات، إرجاع جميع العلاقات
        if not relation_id and not source_id and not target_id and not relation_type_str and min_weight is None and not properties:
            for relation_id, relation in self.relations.items():
                results.append(relation.to_dict())
        
        # تحديد النتائج حسب عدد النتائج المطلوب
        results = results[:query.max_results]
        
        return SemanticQueryResult(
            results=results,
            count=len(results),
            success=True,
            message=f"تم العثور على {len(results)} علاقة"
        )
    
    def _query_mappings(self, query: SemanticQuery) -> SemanticQueryResult:
        """
        تنفيذ استعلام عن التخطيطات.
        
        Args:
            query: الاستعلام الدلالي
            
        Returns:
            نتيجة الاستعلام الدلالي
        """
        results = []
        
        # البحث حسب المعرف
        mapping_id = query.parameters.get("id")
        if mapping_id:
            mapping = self.get_mapping(mapping_id)
            if mapping:
                results.append(mapping.to_dict())
        
        # البحث حسب معرف المعادلة
        equation_id = query.parameters.get("equation_id")
        if equation_id:
            mappings = self.get_mappings_by_equation(equation_id)
            for mapping in mappings:
                results.append(mapping.to_dict())
        
        # البحث حسب معرف المفهوم
        concept_id = query.parameters.get("concept_id")
        if concept_id:
            mappings = self.get_mappings_by_concept(concept_id)
            for mapping in mappings:
                results.append(mapping.to_dict())
        
        # البحث حسب نوع التخطيط
        mapping_type = query.parameters.get("mapping_type")
        if mapping_type:
            for mapping_id, mapping in self.mappings.items():
                if mapping.mapping_type == mapping_type:
                    results.append(mapping.to_dict())
        
        # البحث حسب درجة الثقة
        min_confidence = query.parameters.get("min_confidence")
        if min_confidence is not None:
            min_confidence = float(min_confidence)
            for mapping_id, mapping in self.mappings.items():
                if mapping.confidence >= min_confidence:
                    results.append(mapping.to_dict())
        
        # البحث حسب الخصائص
        properties = query.parameters.get("properties", {})
        if properties:
            for mapping_id, mapping in self.mappings.items():
                match = True
                for key, value in properties.items():
                    if mapping.properties.get(key) != value:
                        match = False
                        break
                
                if match:
                    results.append(mapping.to_dict())
        
        # إذا لم يتم تحديد أي معلمات، إرجاع جميع التخطيطات
        if not mapping_id and not equation_id and not concept_id and not mapping_type and min_confidence is None and not properties:
            for mapping_id, mapping in self.mappings.items():
                results.append(mapping.to_dict())
        
        # تحديد النتائج حسب عدد النتائج المطلوب
        results = results[:query.max_results]
        
        return SemanticQueryResult(
            results=results,
            count=len(results),
            success=True,
            message=f"تم العثور على {len(results)} تخطيط"
        )
    
    def _query_path(self, query: SemanticQuery) -> SemanticQueryResult:
        """
        تنفيذ استعلام عن المسار بين مفهومين.
        
        Args:
            query: الاستعلام الدلالي
            
        Returns:
            نتيجة الاستعلام الدلالي
        """
        source_id = query.parameters.get("source_id")
        target_id = query.parameters.get("target_id")
        
        if not source_id or not target_id:
            return SemanticQueryResult(
                success=False,
                message="يجب تحديد معرف المصدر ومعرف الهدف"
            )
        
        # التحقق من وجود المفاهيم
        if source_id not in self.concepts:
            return SemanticQueryResult(
                success=False,
                message=f"المفهوم المصدر غير موجود: {source_id}"
            )
        
        if target_id not in self.concepts:
            return SemanticQueryResult(
                success=False,
                message=f"المفهوم الهدف غير موجود: {target_id}"
            )
        
        # البحث عن المسار
        max_depth = query.parameters.get("max_depth", 5)
        paths = self._find_paths(source_id, target_id, max_depth)
        
        if not paths:
            return SemanticQueryResult(
                success=False,
                message=f"لم يتم العثور على مسار بين المفهومين"
            )
        
        # تحويل المسارات إلى نتائج
        results = []
        for path in paths[:query.max_results]:
            path_result = {
                "path": [],
                "length": len(path) // 2,
                "total_weight": 0.0
            }
            
            for i in range(0, len(path), 2):
                concept_id = path[i]
                concept = self.get_concept(concept_id)
                
                path_result["path"].append({
                    "type": "concept",
                    "id": concept_id,
                    "name": concept.name
                })
                
                if i + 1 < len(path):
                    relation_id = path[i + 1]
                    relation = self.get_relation(relation_id)
                    
                    path_result["path"].append({
                        "type": "relation",
                        "id": relation_id,
                        "relation_type": relation.relation_type.value,
                        "weight": relation.weight
                    })
                    
                    path_result["total_weight"] += relation.weight
            
            results.append(path_result)
        
        return SemanticQueryResult(
            results=results,
            count=len(results),
            success=True,
            message=f"تم العثور على {len(results)} مسار"
        )
    
    def _find_paths(self, source_id: str, target_id: str, max_depth: int) -> List[List[str]]:
        """
        البحث عن المسارات بين مفهومين.
        
        Args:
            source_id: معرف المصدر
            target_id: معرف الهدف
            max_depth: أقصى عمق للبحث
            
        Returns:
            قائمة المسارات (كل مسار هو قائمة من معرفات المفاهيم والعلاقات بالتناوب)
        """
        # استخدام خوارزمية البحث بالعرض أولاً
        visited = set()
        queue = [(source_id, [])]
        paths = []
        
        while queue:
            current_id, path = queue.pop(0)
            
            # إذا وصلنا إلى الهدف
            if current_id == target_id:
                paths.append(path + [current_id])
                continue
            
            # إذا تجاوزنا أقصى عمق
            if len(path) // 2 >= max_depth:
                continue
            
            # إذا زرنا هذا المفهوم من قبل
            if current_id in visited:
                continue
            
            visited.add(current_id)
            
            # البحث عن العلاقات الخارجة من المفهوم الحالي
            relations = self.get_relations_by_source(current_id)
            for relation in relations:
                next_id = relation.target_id
                if next_id not in visited:
                    queue.append((next_id, path + [current_id, relation.id]))
            
            # البحث عن العلاقات الداخلة إلى المفهوم الحالي
            relations = self.get_relations_by_target(current_id)
            for relation in relations:
                next_id = relation.source_id
                if next_id not in visited:
                    queue.append((next_id, path + [current_id, relation.id]))
        
        # ترتيب المسارات حسب الطول
        paths.sort(key=len)
        
        return paths
    
    def map_equation_to_concepts(self, equation: Union[AdvancedSymbolicExpression, AdvancedShapeEquation]) -> List[SemanticMapping]:
        """
        تخطيط معادلة إلى مفاهيم دلالية.
        
        Args:
            equation: المعادلة
            
        Returns:
            قائمة التخطيطات الدلالية
        """
        logger.info(f"تخطيط المعادلة {equation.metadata.equation_id} إلى مفاهيم دلالية")
        
        mappings = []
        
        # تحليل المعادلة
        if isinstance(equation, AdvancedSymbolicExpression):
            # تخطيط المعادلة الرمزية
            mappings.extend(self._map_symbolic_equation(equation))
        elif isinstance(equation, AdvancedShapeEquation):
            # تخطيط معادلة الشكل
            mappings.extend(self._map_shape_equation(equation))
        
        # إضافة التخطيطات إلى قاعدة المعرفة الدلالية
        for mapping in mappings:
            self.add_mapping(mapping)
        
        logger.info(f"تم تخطيط المعادلة {equation.metadata.equation_id} إلى {len(mappings)} مفهوم دلالي")
        
        return mappings
    
    def _map_symbolic_equation(self, equation: AdvancedSymbolicExpression) -> List[SemanticMapping]:
        """
        تخطيط معادلة رمزية إلى مفاهيم دلالية.
        
        Args:
            equation: المعادلة الرمزية
            
        Returns:
            قائمة التخطيطات الدلالية
        """
        mappings = []
        
        # تخطيط المعادلة إلى مفهوم "معادلة"
        equation_concepts = self.get_concept_by_name("معادلة")
        if equation_concepts:
            equation_concept = equation_concepts[0]
            mapping = SemanticMapping(
                equation_id=equation.metadata.equation_id,
                concept_id=equation_concept.id,
                mapping_type="direct",
                confidence=1.0
            )
            mappings.append(mapping)
        
        # تخطيط المعادلة إلى مفاهيم أخرى حسب العمليات
        operations = equation.metadata.operations
        
        if "sin" in operations or "cos" in operations or "tan" in operations:
            # البحث عن مفاهيم متعلقة بالدوال المثلثية
            trig_concepts = self._find_concepts_by_property("trigonometric", True)
            if trig_concepts:
                for concept in trig_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="operation_based",
                        confidence=0.8,
                        properties={"operation": "trigonometric"}
                    )
                    mappings.append(mapping)
        
        if "exp" in operations or "log" in operations:
            # البحث عن مفاهيم متعلقة بالدوال الأسية واللوغاريتمية
            exp_concepts = self._find_concepts_by_property("exponential", True)
            if exp_concepts:
                for concept in exp_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="operation_based",
                        confidence=0.8,
                        properties={"operation": "exponential"}
                    )
                    mappings.append(mapping)
        
        # تخطيط المعادلة إلى مفاهيم حسب المتغيرات
        variables = equation.variables
        
        if "x" in variables and "y" in variables:
            # البحث عن مفاهيم متعلقة بالأشكال ثنائية الأبعاد
            shape_concepts = self._find_concepts_by_property("geometric", True)
            if shape_concepts:
                for concept in shape_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="variable_based",
                        confidence=0.7,
                        properties={"variables": ["x", "y"]}
                    )
                    mappings.append(mapping)
        
        if "t" in variables:
            # البحث عن مفاهيم متعلقة بالزمن
            time_concepts = self._find_concepts_by_property("temporal", True)
            if time_concepts:
                for concept in time_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="variable_based",
                        confidence=0.7,
                        properties={"variables": ["t"]}
                    )
                    mappings.append(mapping)
        
        # تخطيط المعادلة إلى مفاهيم حسب العلامات الدلالية
        semantic_tags = equation.metadata.semantic_tags
        
        for tag in semantic_tags:
            # البحث عن مفاهيم متعلقة بالعلامة الدلالية
            tag_concepts = self._find_concepts_by_name(tag)
            if tag_concepts:
                for concept in tag_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="tag_based",
                        confidence=0.9,
                        properties={"tag": tag}
                    )
                    mappings.append(mapping)
        
        # تخطيط المعادلة إلى مفاهيم ثورية إذا كانت المعادلة ثورية
        if equation.metadata.is_revolutionary:
            revolutionary_concepts = self._find_concepts_by_property("revolutionary", True)
            if revolutionary_concepts:
                for concept in revolutionary_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="revolutionary",
                        confidence=0.9,
                        properties={"revolutionary": True}
                    )
                    mappings.append(mapping)
        
        return mappings
    
    def _map_shape_equation(self, equation: AdvancedShapeEquation) -> List[SemanticMapping]:
        """
        تخطيط معادلة شكل إلى مفاهيم دلالية.
        
        Args:
            equation: معادلة الشكل
            
        Returns:
            قائمة التخطيطات الدلالية
        """
        mappings = []
        
        # تخطيط المعادلة إلى مفهوم "شكل"
        shape_concepts = self.get_concept_by_name("شكل")
        if shape_concepts:
            shape_concept = shape_concepts[0]
            mapping = SemanticMapping(
                equation_id=equation.metadata.equation_id,
                concept_id=shape_concept.id,
                mapping_type="direct",
                confidence=1.0
            )
            mappings.append(mapping)
        
        # تخطيط المعادلة إلى مفاهيم حسب الأبعاد
        dimensions = equation.metadata.dimensions_represented
        
        if ShapeDimension.GEOMETRIC in dimensions:
            # البحث عن مفاهيم متعلقة بالأشكال الهندسية
            geometric_concepts = self._find_concepts_by_property("geometric", True)
            if geometric_concepts:
                for concept in geometric_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="dimension_based",
                        confidence=0.8,
                        properties={"dimension": "geometric"}
                    )
                    mappings.append(mapping)
        
        if ShapeDimension.TEMPORAL in dimensions:
            # البحث عن مفاهيم متعلقة بالزمن
            temporal_concepts = self._find_concepts_by_property("temporal", True)
            if temporal_concepts:
                for concept in temporal_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="dimension_based",
                        confidence=0.8,
                        properties={"dimension": "temporal"}
                    )
                    mappings.append(mapping)
        
        if ShapeDimension.SEMANTIC in dimensions:
            # البحث عن مفاهيم متعلقة بالدلالة
            semantic_concepts = self._find_concepts_by_property("semantic", True)
            if semantic_concepts:
                for concept in semantic_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="dimension_based",
                        confidence=0.8,
                        properties={"dimension": "semantic"}
                    )
                    mappings.append(mapping)
        
        if ShapeDimension.QUANTUM in dimensions:
            # البحث عن مفاهيم متعلقة بالكم
            quantum_concepts = self._find_concepts_by_property("quantum", True)
            if quantum_concepts:
                for concept in quantum_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="dimension_based",
                        confidence=0.8,
                        properties={"dimension": "quantum"}
                    )
                    mappings.append(mapping)
        
        if ShapeDimension.EMOTIONAL in dimensions:
            # البحث عن مفاهيم متعلقة بالعاطفة
            emotional_concepts = self._find_concepts_by_property("emotional", True)
            if emotional_concepts:
                for concept in emotional_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="dimension_based",
                        confidence=0.8,
                        properties={"dimension": "emotional"}
                    )
                    mappings.append(mapping)
        
        if ShapeDimension.SOCIAL in dimensions:
            # البحث عن مفاهيم متعلقة بالاجتماعية
            social_concepts = self._find_concepts_by_property("social", True)
            if social_concepts:
                for concept in social_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="dimension_based",
                        confidence=0.8,
                        properties={"dimension": "social"}
                    )
                    mappings.append(mapping)
        
        # تخطيط المعادلة إلى مفاهيم حسب نوع الشكل
        shape_type = equation.metadata.shape_type
        
        if shape_type:
            # البحث عن مفاهيم متعلقة بنوع الشكل
            type_concepts = self._find_concepts_by_name(shape_type)
            if type_concepts:
                for concept in type_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="type_based",
                        confidence=0.9,
                        properties={"shape_type": shape_type}
                    )
                    mappings.append(mapping)
        
        # تخطيط المعادلة إلى مفاهيم حسب العلامات الدلالية
        semantic_tags = equation.metadata.semantic_tags
        
        for tag in semantic_tags:
            # البحث عن مفاهيم متعلقة بالعلامة الدلالية
            tag_concepts = self._find_concepts_by_name(tag)
            if tag_concepts:
                for concept in tag_concepts:
                    mapping = SemanticMapping(
                        equation_id=equation.metadata.equation_id,
                        concept_id=concept.id,
                        mapping_type="tag_based",
                        confidence=0.9,
                        properties={"tag": tag}
                    )
                    mappings.append(mapping)
        
        return mappings
    
    def _find_concepts_by_property(self, property_name: str, property_value: Any) -> List[SemanticConcept]:
        """
        البحث عن مفاهيم حسب خاصية.
        
        Args:
            property_name: اسم الخاصية
            property_value: قيمة الخاصية
            
        Returns:
            قائمة المفاهيم
        """
        concepts = []
        
        for concept_id, concept in self.concepts.items():
            if concept.properties.get(property_name) == property_value:
                concepts.append(concept)
        
        return concepts
    
    def _find_concepts_by_name(self, name: str) -> List[SemanticConcept]:
        """
        البحث عن مفاهيم حسب الاسم (بحث جزئي).
        
        Args:
            name: اسم المفهوم
            
        Returns:
            قائمة المفاهيم
        """
        concepts = []
        
        for concept_id, concept in self.concepts.items():
            if name.lower() in concept.name.lower():
                concepts.append(concept)
        
        return concepts
    
    def enrich_equation_with_semantics(self, equation: Union[AdvancedSymbolicExpression, AdvancedShapeEquation]) -> Union[AdvancedSymbolicExpression, AdvancedShapeEquation]:
        """
        إثراء معادلة بالمعلومات الدلالية.
        
        Args:
            equation: المعادلة
            
        Returns:
            المعادلة المثراة
        """
        logger.info(f"إثراء المعادلة {equation.metadata.equation_id} بالمعلومات الدلالية")
        
        # البحث عن التخطيطات الدلالية للمعادلة
        mappings = self.get_mappings_by_equation(equation.metadata.equation_id)
        
        if not mappings:
            # إذا لم تكن هناك تخطيطات، إنشاء تخطيطات جديدة
            mappings = self.map_equation_to_concepts(equation)
        
        # إثراء المعادلة بالعلامات الدلالية
        for mapping in mappings:
            concept = self.get_concept(mapping.concept_id)
            if concept:
                # إضافة اسم المفهوم كعلامة دلالية
                if concept.name not in equation.metadata.semantic_tags:
                    equation.metadata.semantic_tags.append(concept.name)
                
                # إضافة المجالات الدلالية
                for domain in concept.domains:
                    domain_str = domain.value
                    if domain_str not in equation.metadata.domains:
                        equation.metadata.domains.append(domain_str)
                
                # إضافة خصائص المفهوم
                for key, value in concept.properties.items():
                    if key not in equation.metadata.properties:
                        equation.metadata.properties[key] = value
        
        logger.info(f"تم إثراء المعادلة {equation.metadata.equation_id} بـ {len(equation.metadata.semantic_tags)} علامة دلالية و {len(equation.metadata.domains)} مجال دلالي")
        
        return equation
    
    def find_related_equations(self, equation: Union[AdvancedSymbolicExpression, AdvancedShapeEquation], max_results: int = 10) -> List[Dict[str, Any]]:
        """
        البحث عن معادلات مرتبطة.
        
        Args:
            equation: المعادلة
            max_results: أقصى عدد للنتائج
            
        Returns:
            قائمة المعادلات المرتبطة
        """
        logger.info(f"البحث عن معادلات مرتبطة بالمعادلة {equation.metadata.equation_id}")
        
        related_equations = []
        
        # البحث عن التخطيطات الدلالية للمعادلة
        mappings = self.get_mappings_by_equation(equation.metadata.equation_id)
        
        if not mappings:
            # إذا لم تكن هناك تخطيطات، إنشاء تخطيطات جديدة
            mappings = self.map_equation_to_concepts(equation)
        
        # البحث عن معادلات مرتبطة بنفس المفاهيم
        for mapping in mappings:
            concept_id = mapping.concept_id
            
            # البحث عن تخطيطات أخرى لنفس المفهوم
            related_mappings = self.get_mappings_by_concept(concept_id)
            
            for related_mapping in related_mappings:
                if related_mapping.equation_id != equation.metadata.equation_id:
                    # إضافة المعادلة المرتبطة
                    related_equations.append({
                        "equation_id": related_mapping.equation_id,
                        "concept_id": concept_id,
                        "concept_name": self.get_concept(concept_id).name,
                        "mapping_type": related_mapping.mapping_type,
                        "confidence": related_mapping.confidence
                    })
        
        # ترتيب المعادلات المرتبطة حسب درجة الثقة
        related_equations.sort(key=lambda x: x["confidence"], reverse=True)
        
        # تحديد النتائج حسب عدد النتائج المطلوب
        related_equations = related_equations[:max_results]
        
        logger.info(f"تم العثور على {len(related_equations)} معادلة مرتبطة بالمعادلة {equation.metadata.equation_id}")
        
        return related_equations
    
    def bridge_to_cosmic_core(self, equation: Union[AdvancedSymbolicExpression, AdvancedShapeEquation]) -> Dict[str, Any]:
        """
        جسر إلى النواة الكونية.
        
        Args:
            equation: المعادلة
            
        Returns:
            بيانات الجسر
        """
        logger.info(f"إنشاء جسر إلى النواة الكونية للمعادلة {equation.metadata.equation_id}")
        
        # إثراء المعادلة بالمعلومات الدلالية
        equation = self.enrich_equation_with_semantics(equation)
        
        # إنشاء بيانات الجسر
        bridge_data = {
            "equation_id": equation.metadata.equation_id,
            "equation_type": "symbolic" if isinstance(equation, AdvancedSymbolicExpression) else "shape",
            "semantic_tags": equation.metadata.semantic_tags,
            "domains": equation.metadata.domains,
            "properties": equation.metadata.properties,
            "is_revolutionary": equation.metadata.is_revolutionary,
            "mappings": []
        }
        
        # إضافة التخطيطات الدلالية
        mappings = self.get_mappings_by_equation(equation.metadata.equation_id)
        
        for mapping in mappings:
            concept = self.get_concept(mapping.concept_id)
            
            bridge_data["mappings"].append({
                "concept_id": mapping.concept_id,
                "concept_name": concept.name,
                "mapping_type": mapping.mapping_type,
                "confidence": mapping.confidence
            })
        
        logger.info(f"تم إنشاء جسر إلى النواة الكونية للمعادلة {equation.metadata.equation_id} مع {len(bridge_data['mappings'])} تخطيط")
        
        return bridge_data


# اختبار الوحدة
if __name__ == "__main__":
    # إنشاء التكامل الدلالي
    semantic_integration = SemanticIntegration()
    
    # إنشاء معادلة رمزية للاختبار
    symbolic_expr = AdvancedSymbolicExpression(expression_str="sin(x**2 + y**2) * exp(-x*y)")
    symbolic_expr.metadata.equation_id = "test_symbolic_equation"
    symbolic_expr.metadata.semantic_tags = ["wave", "oscillation"]
    symbolic_expr.metadata.operations = ["sin", "exp", "power", "multiply", "add", "subtract"]
    
    # إنشاء معادلة شكل للاختبار
    shape_components = [
        ShapeComponent(
            dimension=ShapeDimension.GEOMETRIC,
            expression=AdvancedSymbolicExpression(expression_str="x**2 + y**2"),
            weight=1.0
        ),
        ShapeComponent(
            dimension=ShapeDimension.TEMPORAL,
            expression=AdvancedSymbolicExpression(expression_str="sin(t)"),
            weight=0.8
        )
    ]
    shape_eq = AdvancedShapeEquation(components=shape_components)
    shape_eq.metadata.equation_id = "test_shape_equation"
    shape_eq.metadata.shape_type = "dynamic_object"
    shape_eq.metadata.dimensions_represented = {ShapeDimension.GEOMETRIC, ShapeDimension.TEMPORAL}
    
    print("--- اختبار تخطيط المعادلة الرمزية ---")
    symbolic_mappings = semantic_integration.map_equation_to_concepts(symbolic_expr)
    print(f"تم إنشاء {len(symbolic_mappings)} تخطيط للمعادلة الرمزية")
    
    for i, mapping in enumerate(symbolic_mappings):
        concept = semantic_integration.get_concept(mapping.concept_id)
        print(f"{i+1}. {concept.name} ({mapping.mapping_type}, الثقة: {mapping.confidence:.2f})")
    
    print("\n--- اختبار تخطيط معادلة الشكل ---")
    shape_mappings = semantic_integration.map_equation_to_concepts(shape_eq)
    print(f"تم إنشاء {len(shape_mappings)} تخطيط لمعادلة الشكل")
    
    for i, mapping in enumerate(shape_mappings):
        concept = semantic_integration.get_concept(mapping.concept_id)
        print(f"{i+1}. {concept.name} ({mapping.mapping_type}, الثقة: {mapping.confidence:.2f})")
    
    print("\n--- اختبار إثراء المعادلة الرمزية ---")
    enriched_symbolic = semantic_integration.enrich_equation_with_semantics(symbolic_expr)
    print(f"العلامات الدلالية: {enriched_symbolic.metadata.semantic_tags}")
    print(f"المجالات الدلالية: {enriched_symbolic.metadata.domains}")
    
    print("\n--- اختبار إثراء معادلة الشكل ---")
    enriched_shape = semantic_integration.enrich_equation_with_semantics(shape_eq)
    print(f"العلامات الدلالية: {enriched_shape.metadata.semantic_tags}")
    print(f"المجالات الدلالية: {enriched_shape.metadata.domains}")
    
    print("\n--- اختبار البحث عن معادلات مرتبطة ---")
    related_equations = semantic_integration.find_related_equations(symbolic_expr)
    print(f"تم العثور على {len(related_equations)} معادلة مرتبطة")
    
    for i, related in enumerate(related_equations):
        print(f"{i+1}. {related['equation_id']} ({related['concept_name']}, الثقة: {related['confidence']:.2f})")
    
    print("\n--- اختبار الجسر إلى النواة الكونية ---")
    bridge_data = semantic_integration.bridge_to_cosmic_core(symbolic_expr)
    print(f"معرف المعادلة: {bridge_data['equation_id']}")
    print(f"نوع المعادلة: {bridge_data['equation_type']}")
    print(f"العلامات الدلالية: {bridge_data['semantic_tags']}")
    print(f"المجالات الدلالية: {bridge_data['domains']}")
    print(f"عدد التخطيطات: {len(bridge_data['mappings'])}")
    
    print("\n--- اختبار الاستعلام عن المفاهيم ---")
    concept_query = SemanticQuery(
        query_type="concept",
        parameters={"domain": "mathematics"},
        max_results=5
    )
    concept_result = semantic_integration.query(concept_query)
    print(f"تم العثور على {concept_result.count} مفهوم")
    
    for i, concept_data in enumerate(concept_result.results):
        print(f"{i+1}. {concept_data['name']} ({', '.join(concept_data['domains'])})")
    
    print("\n--- اختبار الاستعلام عن العلاقات ---")
    relation_query = SemanticQuery(
        query_type="relation",
        parameters={"relation_type": "is_a"},
        max_results=5
    )
    relation_result = semantic_integration.query(relation_query)
    print(f"تم العثور على {relation_result.count} علاقة")
    
    for i, relation_data in enumerate(relation_result.results):
        source_concept = semantic_integration.get_concept(relation_data['source_id'])
        target_concept = semantic_integration.get_concept(relation_data['target_id'])
        print(f"{i+1}. {source_concept.name} {relation_data['relation_type']} {target_concept.name}")
    
    print("\n--- اختبار الاستعلام عن المسار ---")
    # البحث عن مسار بين مفهومين
    mass_concepts = semantic_integration.get_concept_by_name("كتلة")
    filament_concepts = semantic_integration.get_concept_by_name("خيط")
    
    if mass_concepts and filament_concepts:
        path_query = SemanticQuery(
            query_type="path",
            parameters={
                "source_id": mass_concepts[0].id,
                "target_id": filament_concepts[0].id,
                "max_depth": 3
            },
            max_results=2
        )
        path_result = semantic_integration.query(path_query)
        print(f"تم العثور على {path_result.count} مسار")
        
        for i, path_data in enumerate(path_result.results):
            print(f"{i+1}. المسار (الطول: {path_data['length']}, الوزن الكلي: {path_data['total_weight']:.2f}):")
            
            for j, node in enumerate(path_data['path']):
                if node['type'] == "concept":
                    print(f"   - مفهوم: {node['name']}")
                else:
                    print(f"   - علاقة: {node['relation_type']} (الوزن: {node['weight']:.2f})")
    
    print("\n--- اختبار حفظ وتحميل قاعدة المعرفة الدلالية ---")
    kb_file = "/home/ubuntu/basira_system/mathematical_core/core/semantic_kb.json"
    semantic_integration.save_knowledge_base(kb_file)
    print(f"تم حفظ قاعدة المعرفة الدلالية في: {kb_file}")
    
    # إنشاء تكامل دلالي جديد وتحميل قاعدة المعرفة
    new_integration = SemanticIntegration(knowledge_base_path=kb_file)
    print(f"تم تحميل {len(new_integration.concepts)} مفهوم، {len(new_integration.relations)} علاقة، {len(new_integration.mappings)} تخطيط")
