#!/usr/bin/env python3
# knowledge_manager.py - مدير المعرفة Baserah النقي

import json
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Union, Optional, Any, Set
from dataclasses import dataclass, field

from .baserah_expert_core import BaserahKnowledgeItem, KnowledgeType
from .baserah_explorer_core import BaserahEquation

@dataclass
class KnowledgeCluster:
    """مجموعة معرفة Baserah."""
    id: str = field(default_factory=lambda: f"cluster_{uuid.uuid4()}")
    name: str = "مجموعة معرفة"
    knowledge_items: List[str] = field(default_factory=list)  # معرفات العناصر
    equations: List[str] = field(default_factory=list)  # معرفات المعادلات
    cluster_type: str = "general"
    relevance_score: float = 1.0
    creation_date: str = field(default_factory=lambda: datetime.now().isoformat())
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class KnowledgeRelationship:
    """علاقة بين عناصر المعرفة."""
    id: str = field(default_factory=lambda: f"rel_{uuid.uuid4()}")
    source_id: str = ""
    target_id: str = ""
    relationship_type: str = "related"  # related, implies, contradicts, supports
    strength: float = 1.0  # قوة العلاقة
    confidence: float = 1.0  # ثقة في العلاقة
    metadata: Dict[str, Any] = field(default_factory=dict)
    creation_date: str = field(default_factory=lambda: datetime.now().isoformat())

class BaserahKnowledgeManager:
    """
    مدير المعرفة Baserah النقي
    يدير قاعدة المعرفة والمعادلات والعلاقات بينها
    """
    
    def __init__(self):
        """تهيئة مدير المعرفة Baserah."""
        self.knowledge_items: Dict[str, BaserahKnowledgeItem] = {}
        self.equations: Dict[str, BaserahEquation] = {}
        self.clusters: Dict[str, KnowledgeCluster] = {}
        self.relationships: Dict[str, KnowledgeRelationship] = {}
        
        # فهارس للبحث السريع
        self.type_index: Dict[KnowledgeType, Set[str]] = {}
        self.variable_index: Dict[str, Set[str]] = {}  # فهرس المتغيرات للمعادلات
        self.complexity_index: Dict[int, Set[str]] = {}  # فهرس التعقيد
        
        # إحصائيات
        self.total_knowledge_items = 0
        self.total_equations = 0
        self.total_relationships = 0
        
        print("📚 تم تهيئة مدير المعرفة Baserah النقي")
    
    def add_knowledge_item(self, item: BaserahKnowledgeItem):
        """إضافة عنصر معرفة."""
        if not isinstance(item, BaserahKnowledgeItem):
            raise TypeError("يجب أن يكون العنصر من نوع BaserahKnowledgeItem")
        
        self.knowledge_items[item.id] = item
        self.total_knowledge_items += 1
        
        # تحديث فهرس النوع
        if item.type not in self.type_index:
            self.type_index[item.type] = set()
        self.type_index[item.type].add(item.id)
        
        print(f"✅ تمت إضافة معرفة ({item.type}): {item.id}")
    
    def add_equation(self, equation: BaserahEquation):
        """إضافة معادلة."""
        if not isinstance(equation, BaserahEquation):
            raise TypeError("يجب أن يكون العنصر من نوع BaserahEquation")
        
        self.equations[equation.id] = equation
        self.total_equations += 1
        
        # تحديث فهرس المتغيرات
        for variable in equation.variables:
            if variable not in self.variable_index:
                self.variable_index[variable] = set()
            self.variable_index[variable].add(equation.id)
        
        # تحديث فهرس التعقيد
        complexity_level = int(equation.complexity)
        if complexity_level not in self.complexity_index:
            self.complexity_index[complexity_level] = set()
        self.complexity_index[complexity_level].add(equation.id)
        
        print(f"✅ تمت إضافة معادلة ({equation.equation_type}): {equation.id}")
    
    def add_relationship(self, relationship: KnowledgeRelationship):
        """إضافة علاقة بين عناصر المعرفة."""
        if not isinstance(relationship, KnowledgeRelationship):
            raise TypeError("يجب أن يكون العنصر من نوع KnowledgeRelationship")
        
        self.relationships[relationship.id] = relationship
        self.total_relationships += 1
        
        print(f"🔗 تمت إضافة علاقة ({relationship.relationship_type}): {relationship.source_id} → {relationship.target_id}")
    
    def create_cluster(self, name: str, cluster_type: str = "general") -> KnowledgeCluster:
        """إنشاء مجموعة معرفة جديدة."""
        cluster = KnowledgeCluster(
            name=name,
            cluster_type=cluster_type
        )
        
        self.clusters[cluster.id] = cluster
        print(f"📁 تم إنشاء مجموعة معرفة: {name} ({cluster.id})")
        
        return cluster
    
    def add_to_cluster(self, cluster_id: str, item_id: str, item_type: str = "knowledge"):
        """إضافة عنصر إلى مجموعة معرفة."""
        if cluster_id not in self.clusters:
            print(f"❌ مجموعة المعرفة غير موجودة: {cluster_id}")
            return
        
        cluster = self.clusters[cluster_id]
        
        if item_type == "knowledge":
            if item_id in self.knowledge_items:
                cluster.knowledge_items.append(item_id)
                print(f"📚 تمت إضافة معرفة {item_id} إلى مجموعة {cluster.name}")
            else:
                print(f"❌ عنصر المعرفة غير موجود: {item_id}")
        elif item_type == "equation":
            if item_id in self.equations:
                cluster.equations.append(item_id)
                print(f"📐 تمت إضافة معادلة {item_id} إلى مجموعة {cluster.name}")
            else:
                print(f"❌ المعادلة غير موجودة: {item_id}")
    
    def search_knowledge_by_type(self, knowledge_type: KnowledgeType) -> List[BaserahKnowledgeItem]:
        """البحث عن المعرفة حسب النوع."""
        if knowledge_type not in self.type_index:
            return []
        
        items = []
        for item_id in self.type_index[knowledge_type]:
            if item_id in self.knowledge_items:
                items.append(self.knowledge_items[item_id])
        
        return items
    
    def search_equations_by_variable(self, variable: str) -> List[BaserahEquation]:
        """البحث عن المعادلات حسب المتغير."""
        if variable not in self.variable_index:
            return []
        
        equations = []
        for eq_id in self.variable_index[variable]:
            if eq_id in self.equations:
                equations.append(self.equations[eq_id])
        
        return equations
    
    def search_equations_by_complexity(self, min_complexity: float, max_complexity: float) -> List[BaserahEquation]:
        """البحث عن المعادلات حسب التعقيد."""
        equations = []
        
        for complexity_level in range(int(min_complexity), int(max_complexity) + 1):
            if complexity_level in self.complexity_index:
                for eq_id in self.complexity_index[complexity_level]:
                    if eq_id in self.equations:
                        eq = self.equations[eq_id]
                        if min_complexity <= eq.complexity <= max_complexity:
                            equations.append(eq)
        
        return equations
    
    def find_related_items(self, item_id: str) -> List[Tuple[str, KnowledgeRelationship]]:
        """العثور على العناصر المرتبطة بعنصر معين."""
        related_items = []
        
        for rel_id, relationship in self.relationships.items():
            if relationship.source_id == item_id:
                related_items.append((relationship.target_id, relationship))
            elif relationship.target_id == item_id:
                related_items.append((relationship.source_id, relationship))
        
        return related_items
    
    def get_cluster_summary(self, cluster_id: str) -> Dict[str, Any]:
        """الحصول على ملخص مجموعة معرفة."""
        if cluster_id not in self.clusters:
            return {}
        
        cluster = self.clusters[cluster_id]
        
        # إحصائيات المعرفة
        knowledge_types = {}
        for item_id in cluster.knowledge_items:
            if item_id in self.knowledge_items:
                item_type = self.knowledge_items[item_id].type
                knowledge_types[item_type] = knowledge_types.get(item_type, 0) + 1
        
        # إحصائيات المعادلات
        equation_types = {}
        total_complexity = 0.0
        for eq_id in cluster.equations:
            if eq_id in self.equations:
                eq = self.equations[eq_id]
                equation_types[eq.equation_type] = equation_types.get(eq.equation_type, 0) + 1
                total_complexity += eq.complexity
        
        avg_complexity = total_complexity / max(1, len(cluster.equations))
        
        return {
            'cluster_id': cluster_id,
            'cluster_name': cluster.name,
            'cluster_type': cluster.cluster_type,
            'total_knowledge_items': len(cluster.knowledge_items),
            'total_equations': len(cluster.equations),
            'knowledge_types_distribution': knowledge_types,
            'equation_types_distribution': equation_types,
            'average_equation_complexity': avg_complexity,
            'relevance_score': cluster.relevance_score,
            'creation_date': cluster.creation_date
        }
    
    def auto_cluster_by_similarity(self, similarity_threshold: float = 0.7):
        """تجميع تلقائي للمعرفة حسب التشابه."""
        print(f"🔄 بدء التجميع التلقائي (عتبة التشابه: {similarity_threshold})")
        
        # تجميع المعادلات حسب النوع
        equation_type_clusters = {}
        for eq_id, equation in self.equations.items():
            eq_type = equation.equation_type
            if eq_type not in equation_type_clusters:
                cluster = self.create_cluster(f"معادلات {eq_type}", "equation_type")
                equation_type_clusters[eq_type] = cluster.id
            
            self.add_to_cluster(equation_type_clusters[eq_type], eq_id, "equation")
        
        # تجميع المعرفة حسب النوع
        knowledge_type_clusters = {}
        for item_id, item in self.knowledge_items.items():
            item_type = item.type.value
            if item_type not in knowledge_type_clusters:
                cluster = self.create_cluster(f"معرفة {item_type}", "knowledge_type")
                knowledge_type_clusters[item_type] = cluster.id
            
            self.add_to_cluster(knowledge_type_clusters[item_type], item_id, "knowledge")
        
        print(f"✅ تم إنشاء {len(equation_type_clusters)} مجموعة معادلات و {len(knowledge_type_clusters)} مجموعة معرفة")
    
    def get_statistics(self) -> Dict[str, Any]:
        """الحصول على إحصائيات مدير المعرفة."""
        # إحصائيات أنواع المعرفة
        knowledge_type_counts = {}
        for item_type, item_ids in self.type_index.items():
            knowledge_type_counts[item_type.value] = len(item_ids)
        
        # إحصائيات أنواع المعادلات
        equation_type_counts = {}
        for equation in self.equations.values():
            eq_type = equation.equation_type
            equation_type_counts[eq_type] = equation_type_counts.get(eq_type, 0) + 1
        
        # إحصائيات التعقيد
        if self.equations:
            complexities = [eq.complexity for eq in self.equations.values()]
            avg_complexity = sum(complexities) / len(complexities)
            min_complexity = min(complexities)
            max_complexity = max(complexities)
        else:
            avg_complexity = min_complexity = max_complexity = 0.0
        
        # إحصائيات العلاقات
        relationship_type_counts = {}
        for relationship in self.relationships.values():
            rel_type = relationship.relationship_type
            relationship_type_counts[rel_type] = relationship_type_counts.get(rel_type, 0) + 1
        
        return {
            'total_knowledge_items': self.total_knowledge_items,
            'total_equations': self.total_equations,
            'total_relationships': self.total_relationships,
            'total_clusters': len(self.clusters),
            'knowledge_type_distribution': knowledge_type_counts,
            'equation_type_distribution': equation_type_counts,
            'relationship_type_distribution': relationship_type_counts,
            'complexity_statistics': {
                'average': avg_complexity,
                'minimum': min_complexity,
                'maximum': max_complexity
            },
            'index_sizes': {
                'type_index': len(self.type_index),
                'variable_index': len(self.variable_index),
                'complexity_index': len(self.complexity_index)
            }
        }
    
    def export_knowledge_base(self, file_path: str):
        """تصدير قاعدة المعرفة الكاملة."""
        try:
            export_data = {
                'knowledge_items': {},
                'equations': {},
                'clusters': {},
                'relationships': {},
                'metadata': {
                    'export_date': datetime.now().isoformat(),
                    'total_items': len(self.knowledge_items),
                    'total_equations': len(self.equations),
                    'total_clusters': len(self.clusters),
                    'total_relationships': len(self.relationships)
                }
            }
            
            # تصدير عناصر المعرفة
            for item_id, item in self.knowledge_items.items():
                export_data['knowledge_items'][item_id] = {
                    'type': item.type.value,
                    'content': item.content,
                    'activation_level': item.activation_level,
                    'relevance_score': item.relevance_score,
                    'baserah_weight': item.baserah_weight,
                    'metadata': item.metadata,
                    'creation_date': item.creation_date
                }
            
            # تصدير المعادلات
            for eq_id, equation in self.equations.items():
                export_data['equations'][eq_id] = {
                    'equation_type': equation.equation_type,
                    'components': equation.components,
                    'complexity': equation.complexity,
                    'fitness': equation.fitness,
                    'variables': list(equation.variables),
                    'metadata': equation.metadata,
                    'creation_date': equation.creation_date
                }
            
            # تصدير المجموعات
            for cluster_id, cluster in self.clusters.items():
                export_data['clusters'][cluster_id] = {
                    'name': cluster.name,
                    'knowledge_items': cluster.knowledge_items,
                    'equations': cluster.equations,
                    'cluster_type': cluster.cluster_type,
                    'relevance_score': cluster.relevance_score,
                    'creation_date': cluster.creation_date,
                    'metadata': cluster.metadata
                }
            
            # تصدير العلاقات
            for rel_id, relationship in self.relationships.items():
                export_data['relationships'][rel_id] = {
                    'source_id': relationship.source_id,
                    'target_id': relationship.target_id,
                    'relationship_type': relationship.relationship_type,
                    'strength': relationship.strength,
                    'confidence': relationship.confidence,
                    'metadata': relationship.metadata,
                    'creation_date': relationship.creation_date
                }
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)
            
            print(f"💾 تم تصدير قاعدة المعرفة الكاملة: {file_path}")
        except Exception as e:
            print(f"❌ خطأ في تصدير قاعدة المعرفة: {e}")
    
    def import_knowledge_base(self, file_path: str):
        """استيراد قاعدة المعرفة الكاملة."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                import_data = json.load(f)
            
            # استيراد عناصر المعرفة
            for item_id, item_data in import_data.get('knowledge_items', {}).items():
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
                self.add_knowledge_item(item)
            
            # استيراد المعادلات
            for eq_id, eq_data in import_data.get('equations', {}).items():
                from .baserah_explorer_core import BaserahEquation
                equation = BaserahEquation(
                    id=eq_id,
                    equation_type=eq_data['equation_type'],
                    components=eq_data['components'],
                    complexity=eq_data['complexity'],
                    fitness=eq_data['fitness'],
                    variables=set(eq_data['variables']),
                    metadata=eq_data['metadata'],
                    creation_date=eq_data['creation_date']
                )
                self.add_equation(equation)
            
            # استيراد المجموعات
            for cluster_id, cluster_data in import_data.get('clusters', {}).items():
                cluster = KnowledgeCluster(
                    id=cluster_id,
                    name=cluster_data['name'],
                    knowledge_items=cluster_data['knowledge_items'],
                    equations=cluster_data['equations'],
                    cluster_type=cluster_data['cluster_type'],
                    relevance_score=cluster_data['relevance_score'],
                    creation_date=cluster_data['creation_date'],
                    metadata=cluster_data['metadata']
                )
                self.clusters[cluster_id] = cluster
            
            # استيراد العلاقات
            for rel_id, rel_data in import_data.get('relationships', {}).items():
                relationship = KnowledgeRelationship(
                    id=rel_id,
                    source_id=rel_data['source_id'],
                    target_id=rel_data['target_id'],
                    relationship_type=rel_data['relationship_type'],
                    strength=rel_data['strength'],
                    confidence=rel_data['confidence'],
                    metadata=rel_data['metadata'],
                    creation_date=rel_data['creation_date']
                )
                self.add_relationship(relationship)
            
            print(f"📂 تم استيراد قاعدة المعرفة الكاملة من: {file_path}")
        except Exception as e:
            print(f"❌ خطأ في استيراد قاعدة المعرفة: {e}")
