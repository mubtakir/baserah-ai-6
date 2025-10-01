#!/usr/bin/env python3
# baserah_expert_core.py - النواة الخبيرة Baserah النقية

import math
import json
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Union, Optional, Any, Set
from dataclasses import dataclass, field
from enum import Enum

class KnowledgeType(str, Enum):
    """أنواع المعرفة في نظام Baserah."""
    FACT = "fact"  # حقيقة
    RULE = "rule"  # قاعدة
    HEURISTIC = "heuristic"  # استدلال إرشادي
    CONSTRAINT = "constraint"  # قيد
    GOAL = "goal"  # هدف
    CONCEPT = "concept"  # مفهوم
    RELATIONSHIP = "relationship"  # علاقة
    BASERAH_PATTERN = "baserah_pattern"  # نمط Baserah

class InferenceMethod(str, Enum):
    """طرق الاستدلال Baserah."""
    FORWARD_CHAINING = "forward_chaining"  # تسلسل أمامي
    BACKWARD_CHAINING = "backward_chaining"  # تسلسل خلفي
    HYBRID_CHAINING = "hybrid_chaining"  # تسلسل هجين
    SIGMOID_REASONING = "sigmoid_reasoning"  # استدلال سيجمويدي
    LINEAR_REASONING = "linear_reasoning"  # استدلال خطي
    QUANTUM_REASONING = "quantum_reasoning"  # استدلال كمي

@dataclass
class BaserahKnowledgeItem:
    """عنصر معرفة Baserah النقي."""
    type: KnowledgeType
    content: Any  # محتوى المعرفة
    id: str = field(default_factory=lambda: f"knowledge_{uuid.uuid4()}")
    activation_level: float = 1.0  # مستوى التنشيط
    relevance_score: float = 1.0  # درجة الصلة
    baserah_weight: float = 1.0  # وزن Baserah
    metadata: Dict[str, Any] = field(default_factory=dict)
    creation_date: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class BaserahInferenceContext:
    """سياق الاستدلال Baserah."""
    method: InferenceMethod = InferenceMethod.HYBRID_CHAINING
    current_facts: Set[str] = field(default_factory=set)
    goal: Optional[str] = None
    max_depth: int = 10
    confidence_threshold: float = 0.7
    sigmoid_params: Dict[str, float] = field(default_factory=lambda: {'n': 1, 'k': 1.0, 'x0': 0.0, 'alpha': 1.0})
    linear_params: Dict[str, float] = field(default_factory=lambda: {'beta': 1.0, 'gamma': 0.0})
    quantum_factor: int = 1
    custom_properties: Dict[str, Any] = field(default_factory=dict)

@dataclass
class BaserahInferenceResult:
    """نتيجة الاستدلال Baserah."""
    derived_facts: Set[str] = field(default_factory=set)
    explanation_path: List[str] = field(default_factory=list)
    confidence: float = 1.0
    success: bool = False
    message: str = ""
    baserah_score: float = 0.0  # نقاط Baserah
    reasoning_trace: List[Dict[str, Any]] = field(default_factory=list)

class BaserahAdaptiveMatrix:
    """
    مصفوفة تكيفية Baserah النقية
    تستخدم فقط السيجمويد والخط المستقيم
    """
    
    def __init__(self, input_dim: int, output_dim: int):
        """تهيئة المصفوفة التكيفية Baserah."""
        self.input_dim = input_dim
        self.output_dim = output_dim
        
        # معاملات السيجمويد لكل عقدة
        self.sigmoid_params = []
        for i in range(output_dim):
            self.sigmoid_params.append({
                'n': 1,
                'k': 1.0,
                'x0': 0.0,
                'alpha': 1.0
            })
        
        # معاملات خطية لكل عقدة
        self.linear_params = []
        for i in range(output_dim):
            self.linear_params.append({
                'beta': 1.0,
                'gamma': 0.0
            })
        
        # أوزان الدمج (سيجمويد vs خطي)
        self.mixing_weights = [0.5] * output_dim
        
        # معدل التعلم
        self.learning_rate = 0.01
    
    def baserah_sigmoid(self, x: float, n: int, k: float, x0: float, alpha: float) -> float:
        """دالة السيجمويد Baserah النقية."""
        try:
            exponent = -k * ((x - x0) ** n)
            if exponent > 700:  # تجنب overflow
                return 0.0
            elif exponent < -700:
                return alpha
            return alpha / (1 + math.exp(exponent))
        except (OverflowError, ZeroDivisionError):
            return alpha / 2
    
    def baserah_linear(self, x: float, beta: float, gamma: float) -> float:
        """دالة الخط المستقيم Baserah النقية."""
        return beta * x + gamma
    
    def forward(self, x: List[float]) -> List[float]:
        """التمرير الأمامي Baserah النقي."""
        if len(x) != self.input_dim:
            raise ValueError(f"Expected {self.input_dim} inputs, got {len(x)}")
        
        outputs = []
        
        for i in range(self.output_dim):
            # حساب مدخل العقدة (مجموع المدخلات)
            node_input = sum(x)
            
            # حساب السيجمويد
            sigmoid_output = self.baserah_sigmoid(
                node_input,
                self.sigmoid_params[i]['n'],
                self.sigmoid_params[i]['k'],
                self.sigmoid_params[i]['x0'],
                self.sigmoid_params[i]['alpha']
            )
            
            # حساب الخطي
            linear_output = self.baserah_linear(
                node_input,
                self.linear_params[i]['beta'],
                self.linear_params[i]['gamma']
            )
            
            # دمج السيجمويد والخطي
            mixed_output = (self.mixing_weights[i] * sigmoid_output + 
                          (1 - self.mixing_weights[i]) * linear_output)
            
            outputs.append(mixed_output)
        
        return outputs
    
    def update_parameters(self, error: List[float]):
        """تحديث المعاملات بناءً على الخطأ."""
        for i in range(self.output_dim):
            if i < len(error):
                # تحديث معاملات السيجمويد
                self.sigmoid_params[i]['k'] -= self.learning_rate * error[i] * 0.1
                self.sigmoid_params[i]['alpha'] -= self.learning_rate * error[i] * 0.1
                
                # تحديث معاملات الخط المستقيم
                self.linear_params[i]['beta'] -= self.learning_rate * error[i] * 0.1
                self.linear_params[i]['gamma'] -= self.learning_rate * error[i] * 0.1
                
                # تحديث أوزان الدمج
                self.mixing_weights[i] -= self.learning_rate * error[i] * 0.05
                self.mixing_weights[i] = max(0.0, min(1.0, self.mixing_weights[i]))

class BaserahExpertCore:
    """
    النواة الخبيرة Baserah النقية
    نظام خبير يعمل بمنهج Baserah فقط (سيجمويد + خطي + تكميم)
    """
    
    def __init__(self):
        """تهيئة النواة الخبيرة Baserah."""
        self.knowledge_base: Dict[str, BaserahKnowledgeItem] = {}
        self.learning_model: Optional[BaserahAdaptiveMatrix] = None
        self.learning_history: List[Dict[str, Any]] = []
        
        # إحصائيات النظام
        self.inference_count = 0
        self.success_count = 0
        self.total_confidence = 0.0
        
        print("🧠 تم تهيئة النواة الخبيرة Baserah النقية")
    
    def add_knowledge(self, item: BaserahKnowledgeItem):
        """إضافة عنصر معرفة إلى قاعدة المعرفة."""
        if not isinstance(item, BaserahKnowledgeItem):
            raise TypeError("يجب أن يكون العنصر من نوع BaserahKnowledgeItem")
        
        self.knowledge_base[item.id] = item
        print(f"✅ تمت إضافة معرفة ({item.type}): {item.id}")
    
    def get_knowledge(self, item_id: str) -> Optional[BaserahKnowledgeItem]:
        """الحصول على عنصر معرفة."""
        return self.knowledge_base.get(item_id)
    
    def remove_knowledge(self, item_id: str):
        """إزالة عنصر معرفة."""
        if item_id in self.knowledge_base:
            del self.knowledge_base[item_id]
            print(f"🗑️ تمت إزالة المعرفة: {item_id}")
        else:
            print(f"⚠️ لم يتم العثور على المعرفة: {item_id}")
    
    def infer(self, context: BaserahInferenceContext) -> BaserahInferenceResult:
        """تنفيذ عملية الاستدلال Baserah."""
        self.inference_count += 1
        
        print(f"🔍 بدء الاستدلال Baserah #{self.inference_count} بطريقة {context.method}")
        
        if context.method == InferenceMethod.FORWARD_CHAINING:
            result = self._forward_chaining(context)
        elif context.method == InferenceMethod.BACKWARD_CHAINING:
            result = self._backward_chaining(context)
        elif context.method == InferenceMethod.HYBRID_CHAINING:
            result = self._hybrid_chaining(context)
        elif context.method == InferenceMethod.SIGMOID_REASONING:
            result = self._sigmoid_reasoning(context)
        elif context.method == InferenceMethod.LINEAR_REASONING:
            result = self._linear_reasoning(context)
        elif context.method == InferenceMethod.QUANTUM_REASONING:
            result = self._quantum_reasoning(context)
        else:
            result = BaserahInferenceResult(
                success=False,
                message=f"طريقة استدلال غير معروفة: {context.method}"
            )
        
        # تحديث الإحصائيات
        if result.success:
            self.success_count += 1
            self.total_confidence += result.confidence
        
        # تسجيل النتيجة
        self.learning_history.append({
            'timestamp': datetime.now().isoformat(),
            'method': context.method,
            'success': result.success,
            'confidence': result.confidence,
            'derived_facts_count': len(result.derived_facts)
        })
        
        print(f"✅ اكتمل الاستدلال. النجاح: {result.success}, الثقة: {result.confidence:.3f}")
        return result
    
    def _forward_chaining(self, context: BaserahInferenceContext) -> BaserahInferenceResult:
        """الاستدلال بالتسلسل الأمامي Baserah."""
        derived_facts = set(context.current_facts)
        explanation_path = []
        newly_derived = True
        iterations = 0
        
        while newly_derived and iterations < context.max_depth:
            newly_derived = False
            iterations += 1
            
            for item_id, item in self.knowledge_base.items():
                if item.type == KnowledgeType.RULE and item_id not in explanation_path:
                    rule_content = item.content
                    if isinstance(rule_content, dict) and "if" in rule_content and "then" in rule_content:
                        conditions = rule_content["if"]
                        conclusions = rule_content["then"]
                        
                        # تطبيق وزن Baserah
                        baserah_weight = item.baserah_weight
                        
                        if all(cond_id in derived_facts for cond_id in conditions):
                            for conc_id in conclusions:
                                if conc_id not in derived_facts:
                                    derived_facts.add(conc_id)
                                    explanation_path.append(item_id)
                                    explanation_path.append(conc_id)
                                    newly_derived = True
        
        final_derived = derived_facts - context.current_facts
        success = bool(final_derived)
        confidence = min(1.0, len(final_derived) / max(1, len(context.current_facts)))
        
        return BaserahInferenceResult(
            derived_facts=final_derived,
            explanation_path=explanation_path,
            confidence=confidence,
            success=success,
            message=f"تسلسل أمامي: {len(final_derived)} حقائق جديدة",
            baserah_score=confidence * len(final_derived)
        )

    def _backward_chaining(self, context: BaserahInferenceContext) -> BaserahInferenceResult:
        """الاستدلال بالتسلسل الخلفي Baserah."""
        if context.goal is None:
            return BaserahInferenceResult(
                success=False,
                message="يجب تحديد هدف للتسلسل الخلفي"
            )

        memo = {}
        explanation_path = []

        def prove_goal(goal_id, depth):
            if goal_id in memo:
                return memo[goal_id]
            if depth > context.max_depth:
                return False

            if goal_id in context.current_facts:
                memo[goal_id] = True
                return True

            # البحث عن قواعد Baserah
            for item_id, item in self.knowledge_base.items():
                if item.type == KnowledgeType.RULE:
                    rule_content = item.content
                    if isinstance(rule_content, dict) and "then" in rule_content:
                        if goal_id in rule_content["then"]:
                            conditions = rule_content["if"]

                            all_conditions_proven = True
                            for cond_id in conditions:
                                if not prove_goal(cond_id, depth + 1):
                                    all_conditions_proven = False
                                    break

                            if all_conditions_proven:
                                explanation_path.append(item_id)
                                explanation_path.append(goal_id)
                                memo[goal_id] = True
                                return True

            memo[goal_id] = False
            return False

        goal_proven = prove_goal(context.goal, 0)

        return BaserahInferenceResult(
            derived_facts={context.goal} if goal_proven else set(),
            explanation_path=explanation_path,
            confidence=1.0 if goal_proven else 0.0,
            success=goal_proven,
            message=f"تسلسل خلفي: {'نجح' if goal_proven else 'فشل'} في إثبات {context.goal}",
            baserah_score=1.0 if goal_proven else 0.0
        )

    def _hybrid_chaining(self, context: BaserahInferenceContext) -> BaserahInferenceResult:
        """الاستدلال الهجين Baserah."""
        # محاولة التسلسل الخلفي أولاً إذا كان هناك هدف
        if context.goal:
            backward_result = self._backward_chaining(context)
            if backward_result.success:
                return backward_result

        # التسلسل الأمامي
        forward_result = self._forward_chaining(context)

        # دمج النتائج
        return BaserahInferenceResult(
            derived_facts=forward_result.derived_facts,
            explanation_path=forward_result.explanation_path,
            confidence=forward_result.confidence,
            success=forward_result.success,
            message=f"هجين: {forward_result.message}",
            baserah_score=forward_result.baserah_score
        )

    def _sigmoid_reasoning(self, context: BaserahInferenceContext) -> BaserahInferenceResult:
        """الاستدلال السيجمويدي Baserah."""
        # استخدام السيجمويد لحساب درجات الثقة
        derived_facts = set()
        explanation_path = []

        sigmoid_params = context.sigmoid_params

        for item_id, item in self.knowledge_base.items():
            if item.type == KnowledgeType.FACT:
                # حساب درجة الثقة باستخدام السيجمويد
                x = item.activation_level
                confidence = self._calculate_sigmoid_confidence(x, sigmoid_params)

                if confidence >= context.confidence_threshold:
                    derived_facts.add(item_id)
                    explanation_path.append(item_id)

        success = bool(derived_facts)
        avg_confidence = sum(self._calculate_sigmoid_confidence(
            self.knowledge_base[fact_id].activation_level, sigmoid_params
        ) for fact_id in derived_facts) / max(1, len(derived_facts))

        return BaserahInferenceResult(
            derived_facts=derived_facts,
            explanation_path=explanation_path,
            confidence=avg_confidence,
            success=success,
            message=f"استدلال سيجمويدي: {len(derived_facts)} حقائق",
            baserah_score=avg_confidence * len(derived_facts)
        )

    def _linear_reasoning(self, context: BaserahInferenceContext) -> BaserahInferenceResult:
        """الاستدلال الخطي Baserah."""
        derived_facts = set()
        explanation_path = []

        linear_params = context.linear_params

        for item_id, item in self.knowledge_base.items():
            if item.type == KnowledgeType.FACT:
                # حساب درجة الثقة باستخدام الخط المستقيم
                x = item.activation_level
                confidence = self._calculate_linear_confidence(x, linear_params)

                if confidence >= context.confidence_threshold:
                    derived_facts.add(item_id)
                    explanation_path.append(item_id)

        success = bool(derived_facts)
        avg_confidence = sum(self._calculate_linear_confidence(
            self.knowledge_base[fact_id].activation_level, linear_params
        ) for fact_id in derived_facts) / max(1, len(derived_facts))

        return BaserahInferenceResult(
            derived_facts=derived_facts,
            explanation_path=explanation_path,
            confidence=avg_confidence,
            success=success,
            message=f"استدلال خطي: {len(derived_facts)} حقائق",
            baserah_score=avg_confidence * len(derived_facts)
        )

    def _quantum_reasoning(self, context: BaserahInferenceContext) -> BaserahInferenceResult:
        """الاستدلال الكمي Baserah."""
        derived_facts = set()
        explanation_path = []

        quantum_factor = context.quantum_factor

        for item_id, item in self.knowledge_base.items():
            if item.type == KnowledgeType.FACT:
                # تطبيق التكميم على مستوى التنشيط
                x = item.activation_level
                quantized_activation = self._apply_quantum_factor(x, quantum_factor)

                if quantized_activation >= context.confidence_threshold:
                    derived_facts.add(item_id)
                    explanation_path.append(item_id)

        success = bool(derived_facts)
        avg_confidence = sum(self._apply_quantum_factor(
            self.knowledge_base[fact_id].activation_level, quantum_factor
        ) for fact_id in derived_facts) / max(1, len(derived_facts))

        return BaserahInferenceResult(
            derived_facts=derived_facts,
            explanation_path=explanation_path,
            confidence=avg_confidence,
            success=success,
            message=f"استدلال كمي (Q={quantum_factor}): {len(derived_facts)} حقائق",
            baserah_score=avg_confidence * len(derived_facts)
        )

    def _calculate_sigmoid_confidence(self, x: float, params: Dict[str, float]) -> float:
        """حساب الثقة باستخدام السيجمويد."""
        try:
            n = params.get('n', 1)
            k = params.get('k', 1.0)
            x0 = params.get('x0', 0.0)
            alpha = params.get('alpha', 1.0)

            exponent = -k * ((x - x0) ** n)
            if exponent > 700:
                return 0.0
            elif exponent < -700:
                return alpha
            return alpha / (1 + math.exp(exponent))
        except (OverflowError, ZeroDivisionError):
            return 0.5

    def _calculate_linear_confidence(self, x: float, params: Dict[str, float]) -> float:
        """حساب الثقة باستخدام الخط المستقيم."""
        beta = params.get('beta', 1.0)
        gamma = params.get('gamma', 0.0)
        result = beta * x + gamma
        return max(0.0, min(1.0, result))  # تقييد بين 0 و 1

    def _apply_quantum_factor(self, x: float, quantum_factor: int) -> float:
        """تطبيق عامل التكميم."""
        if quantum_factor <= 1:
            return x

        # تكميم القيمة
        step_size = 1.0 / quantum_factor
        quantized = round(x / step_size) * step_size
        return max(0.0, min(1.0, quantized))

    def initialize_learning_model(self, input_dim: int, output_dim: int):
        """تهيئة نموذج التعلم Baserah."""
        self.learning_model = BaserahAdaptiveMatrix(input_dim, output_dim)
        print(f"🧠 تم تهيئة نموذج التعلم Baserah: {input_dim}→{output_dim}")

    def learn_from_inference(self, context: BaserahInferenceContext, result: BaserahInferenceResult):
        """التعلم من نتائج الاستدلال."""
        if not result.success:
            return

        # تحديث مستويات التنشيط للعناصر المستخدمة
        for item_id in result.explanation_path:
            if item_id in self.knowledge_base:
                item = self.knowledge_base[item_id]
                item.activation_level += 0.1 * result.confidence
                item.activation_level = min(item.activation_level, 2.0)
                item.baserah_weight += 0.05 * result.baserah_score

        print(f"📚 تم التعلم من الاستدلال: {len(result.derived_facts)} حقائق جديدة")

    def get_statistics(self) -> Dict[str, Any]:
        """الحصول على إحصائيات النظام."""
        success_rate = self.success_count / max(1, self.inference_count)
        avg_confidence = self.total_confidence / max(1, self.success_count)

        return {
            'total_inferences': self.inference_count,
            'successful_inferences': self.success_count,
            'success_rate': success_rate,
            'average_confidence': avg_confidence,
            'knowledge_base_size': len(self.knowledge_base),
            'learning_history_size': len(self.learning_history)
        }

    def save_knowledge_base(self, file_path: str):
        """حفظ قاعدة المعرفة."""
        try:
            kb_data = {}
            for item_id, item in self.knowledge_base.items():
                kb_data[item_id] = {
                    'type': item.type.value,
                    'content': item.content,
                    'activation_level': item.activation_level,
                    'relevance_score': item.relevance_score,
                    'baserah_weight': item.baserah_weight,
                    'metadata': item.metadata,
                    'creation_date': item.creation_date
                }

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(kb_data, f, ensure_ascii=False, indent=2)

            print(f"💾 تم حفظ قاعدة المعرفة: {file_path}")
        except Exception as e:
            print(f"❌ خطأ في حفظ قاعدة المعرفة: {e}")

    def load_knowledge_base(self, file_path: str):
        """تحميل قاعدة المعرفة."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                kb_data = json.load(f)

            self.knowledge_base = {}
            for item_id, item_data in kb_data.items():
                item = BaserahKnowledgeItem(
                    id=item_id,
                    type=KnowledgeType(item_data['type']),
                    content=item_data['content'],
                    activation_level=item_data.get('activation_level', 1.0),
                    relevance_score=item_data.get('relevance_score', 1.0),
                    baserah_weight=item_data.get('baserah_weight', 1.0),
                    metadata=item_data.get('metadata', {}),
                    creation_date=item_data.get('creation_date', datetime.now().isoformat())
                )
                self.knowledge_base[item_id] = item

            print(f"📂 تم تحميل قاعدة المعرفة: {len(self.knowledge_base)} عنصر")
        except Exception as e:
            print(f"❌ خطأ في تحميل قاعدة المعرفة: {e}")
