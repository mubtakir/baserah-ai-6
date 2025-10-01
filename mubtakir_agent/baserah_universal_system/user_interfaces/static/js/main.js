// main.js - JavaScript للواجهة التفاعلية للنظام الثوري Baserah

// تحديث حالة النظام عند تحميل الصفحة
document.addEventListener('DOMContentLoaded', function() {
    updateSystemStatus();
    
    // تحديث تلقائي كل 30 ثانية
    setInterval(updateSystemStatus, 30000);
});

// تحديث حالة النظام
async function updateSystemStatus() {
    try {
        const response = await fetch('/api/system/status');
        const data = await response.json();
        
        if (data.status === 'success') {
            document.getElementById('system-status').textContent = data.health.status;
            document.getElementById('performance-score').textContent = data.health.performance_score.toFixed(3);
            document.getElementById('inheritances-count').textContent = data.mother_system.total_inheritances;
            document.getElementById('adaptations-count').textContent = data.mother_system.total_adaptations;
            
            // تغيير لون حالة النظام حسب الأداء
            const statusElement = document.getElementById('system-status');
            if (data.health.performance_score > 0.8) {
                statusElement.style.background = 'linear-gradient(45deg, #28a745, #20c997)';
            } else if (data.health.performance_score > 0.5) {
                statusElement.style.background = 'linear-gradient(45deg, #ffc107, #fd7e14)';
            } else {
                statusElement.style.background = 'linear-gradient(45deg, #dc3545, #e83e8c)';
            }
        } else {
            showError('فشل في تحديث حالة النظام: ' + data.message);
        }
    } catch (error) {
        showError('خطأ في الاتصال بالخادم: ' + error.message);
    }
}

// تحليل التطوير
async function analyzeEvolution() {
    showLoading('evolution-loading');
    
    try {
        const response = await fetch('/api/evolution/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            const resultHtml = `
                <div class="alert alert-info">
                    <h5><i class="fas fa-search"></i> نتائج تحليل صحة النظام</h5>
                    <p><strong>حالة الصحة:</strong> ${data.health_status}</p>
                    <p><strong>هل يجب التطوير:</strong> ${data.decision.should_evolve ? 'نعم' : 'لا'}</p>
                    <p><strong>اتجاه التطوير:</strong> ${data.decision.evolution_direction || 'غير محدد'}</p>
                    <p><strong>فحص الأمان:</strong> ${data.decision.safety_checks_passed ? 'نجح' : 'فشل'}</p>
                    <div class="mt-3">
                        <strong>الأسباب:</strong>
                        <ul>
                            ${data.decision.reasoning.map(reason => `<li>${reason}</li>`).join('')}
                        </ul>
                    </div>
                </div>
            `;
            
            document.getElementById('evolution-results').innerHTML = resultHtml;
        } else {
            showError('فشل في تحليل التطوير: ' + data.message);
        }
    } catch (error) {
        showError('خطأ في تحليل التطوير: ' + error.message);
    } finally {
        hideLoading('evolution-loading');
    }
}

// تنفيذ التطوير
async function executeEvolution() {
    showLoading('evolution-loading');
    
    try {
        const response = await fetch('/api/evolution/execute', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            let resultHtml = `
                <div class="alert ${data.evolution_executed ? 'alert-success' : 'alert-warning'}">
                    <h5><i class="fas fa-dna"></i> نتائج التطوير التلقائي</h5>
                    <p><strong>تم التطوير:</strong> ${data.evolution_executed ? 'نعم' : 'لا'}</p>
            `;
            
            if (data.evolution_executed) {
                resultHtml += `
                    <p><strong>نجح التطوير:</strong> ${data.result.success ? 'نعم' : 'لا'}</p>
                    <p><strong>عدد التغييرات:</strong> ${data.result.changes_count}</p>
                    <p><strong>قدرات جديدة:</strong> ${data.result.new_capabilities_count}</p>
                    <p><strong>تحسن الأداء:</strong> ${data.result.performance_improvement.toFixed(3)}</p>
                    
                    <div class="mt-3">
                        <strong>التغييرات المطبقة:</strong>
                        <ul>
                            ${data.result.changes_made.map(change => `<li>${change}</li>`).join('')}
                        </ul>
                    </div>
                    
                    ${data.result.new_capabilities.length > 0 ? `
                        <div class="mt-3">
                            <strong>قدرات جديدة:</strong>
                            <ul>
                                ${data.result.new_capabilities.map(capability => `<li>${capability}</li>`).join('')}
                            </ul>
                        </div>
                    ` : ''}
                `;
            } else {
                resultHtml += `<p><strong>السبب:</strong> ${data.reason}</p>`;
            }
            
            resultHtml += '</div>';
            document.getElementById('evolution-results').innerHTML = resultHtml;
            
            // تحديث حالة النظام
            updateSystemStatus();
        } else {
            showError('فشل في تنفيذ التطوير: ' + data.message);
        }
    } catch (error) {
        showError('خطأ في تنفيذ التطوير: ' + error.message);
    } finally {
        hideLoading('evolution-loading');
    }
}

// تفسير الجملة الدلالية
async function interpretSemantic() {
    const sentence = document.getElementById('semantic-input').value.trim();
    
    if (!sentence) {
        showError('يرجى إدخال جملة للتفسير');
        return;
    }
    
    showLoading('semantic-loading');
    
    try {
        const response = await fetch('/api/semantic/interpret', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ sentence: sentence })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            const interpretation = data.interpretation;
            
            const resultHtml = `
                <div class="alert alert-info">
                    <h5><i class="fas fa-brain"></i> تفسير الجملة: "${interpretation.sentence}"</h5>
                    <p><strong>الثقة:</strong> ${(interpretation.confidence * 100).toFixed(1)}%</p>
                    <p><strong>كلمات معروفة:</strong> ${interpretation.recognized_words.length}</p>
                    <p><strong>خطوات التنفيذ:</strong> ${interpretation.execution_plan_steps}</p>
                    <p><strong>مكونات رياضية:</strong> ${interpretation.mathematical_components}</p>
                    <p><strong>مكونات دلالية:</strong> ${interpretation.semantic_components}</p>
                    
                    <div class="mt-3">
                        <strong>الكلمات المعروفة:</strong>
                        <div class="mt-2">
                            ${interpretation.recognized_words.map(word => 
                                `<span class="badge bg-primary me-2">${word.symbol} ${word.word} (${word.type})</span>`
                            ).join('')}
                        </div>
                    </div>
                </div>
            `;
            
            document.getElementById('semantic-results').innerHTML = resultHtml;
        } else {
            showError('فشل في تفسير الجملة: ' + data.message);
        }
    } catch (error) {
        showError('خطأ في تفسير الجملة: ' + error.message);
    } finally {
        hideLoading('semantic-loading');
    }
}

// تنفيذ الأمر الدلالي
async function executeSemantic() {
    const sentence = document.getElementById('semantic-input').value.trim();
    
    if (!sentence) {
        showError('يرجى إدخال أمر للتنفيذ');
        return;
    }
    
    showLoading('semantic-loading');
    
    try {
        const response = await fetch('/api/semantic/execute', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ sentence: sentence })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            const execution = data.execution;
            
            const resultHtml = `
                <div class="alert ${execution.success ? 'alert-success' : 'alert-warning'}">
                    <h5><i class="fas fa-play"></i> تنفيذ الأمر: "${execution.sentence}"</h5>
                    <p><strong>نجح التنفيذ:</strong> ${execution.success ? 'نعم' : 'لا'}</p>
                    <p><strong>ثقة التفسير:</strong> ${(execution.confidence * 100).toFixed(1)}%</p>
                    <p><strong>كائنات بصرية:</strong> ${execution.visual_objects_count}</p>
                    <p><strong>نتائج رياضية:</strong> ${execution.mathematical_results_count}</p>
                    <p><strong>نقاط الدمج الدلالي:</strong> ${execution.fusion_score.toFixed(3)}</p>
                </div>
            `;
            
            document.getElementById('semantic-results').innerHTML = resultHtml;
        } else {
            showError('فشل في تنفيذ الأمر: ' + data.message);
        }
    } catch (error) {
        showError('خطأ في تنفيذ الأمر: ' + error.message);
    } finally {
        hideLoading('semantic-loading');
    }
}

// التحويل الدلالي
async function semanticTransform() {
    const source = document.getElementById('transform-from').value.trim();
    const target = document.getElementById('transform-to').value.trim();
    
    if (!source || !target) {
        showError('يرجى إدخال كلمتي المصدر والهدف');
        return;
    }
    
    showLoading('semantic-loading');
    
    try {
        const response = await fetch('/api/semantic/transform', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ source: source, target: target })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            const transformation = data.transformation;
            
            const resultHtml = `
                <div class="alert alert-success">
                    <h5><i class="fas fa-exchange-alt"></i> التحويل الدلالي: ${transformation.source} → ${transformation.target}</h5>
                    <p><strong>نقاط التحويل:</strong> ${transformation.score.toFixed(3)}</p>
                    <p><strong>خطوات رياضية:</strong> ${transformation.mathematical_steps}</p>
                    <p><strong>تغييرات دلالية:</strong> ${transformation.semantic_changes}</p>
                </div>
            `;
            
            document.getElementById('semantic-results').innerHTML = resultHtml;
        } else {
            showError('فشل في التحويل الدلالي: ' + data.message);
        }
    } catch (error) {
        showError('خطأ في التحويل الدلالي: ' + error.message);
    } finally {
        hideLoading('semantic-loading');
    }
}

// التأمل الذاتي للكائن المعرفي
async function cognitiveReflect() {
    showLoading('cognitive-loading');
    
    try {
        const response = await fetch('/api/cognitive/reflect', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            const reflection = data.reflection;
            
            const resultHtml = `
                <div class="alert alert-info">
                    <h5><i class="fas fa-mirror"></i> التأمل الذاتي</h5>
                    <p><strong>مستوى الوعي:</strong> ${reflection.consciousness_level.toFixed(3)}</p>
                    <p><strong>نقاط الوعي الذاتي:</strong> ${reflection.self_awareness_score.toFixed(3)}</p>
                    <p><strong>استنتاجات:</strong> ${reflection.insights_count}</p>
                    <p><strong>مجالات تحسين:</strong> ${reflection.improvement_areas_count}</p>
                    
                    <div class="mt-3">
                        <strong>الاستنتاجات:</strong>
                        <ul>
                            ${reflection.insights.map(insight => `<li>${insight}</li>`).join('')}
                        </ul>
                    </div>
                    
                    ${reflection.improvement_areas.length > 0 ? `
                        <div class="mt-3">
                            <strong>مجالات التحسين:</strong>
                            <ul>
                                ${reflection.improvement_areas.map(area => `<li>${area}</li>`).join('')}
                            </ul>
                        </div>
                    ` : ''}
                </div>
            `;
            
            document.getElementById('cognitive-results').innerHTML = resultHtml;
        } else {
            showError('فشل في التأمل الذاتي: ' + data.message);
        }
    } catch (error) {
        showError('خطأ في التأمل الذاتي: ' + error.message);
    } finally {
        hideLoading('cognitive-loading');
    }
}

// التوليد الإبداعي
async function cognitiveCreate() {
    showLoading('cognitive-loading');
    
    try {
        const response = await fetch('/api/cognitive/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ inspiration: Math.random() * 10 })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            const creation = data.creation;
            
            const resultHtml = `
                <div class="alert alert-success">
                    <h5><i class="fas fa-palette"></i> التوليد الإبداعي</h5>
                    <p><strong>نوع الإبداع:</strong> ${creation.type}</p>
                    <p><strong>نقاط الإبداع:</strong> ${creation.creativity_score.toFixed(3)}</p>
                    <p><strong>مستوى الجدة:</strong> ${creation.novelty_level.toFixed(3)}</p>
                    <p><strong>مصدر الإلهام:</strong> ${creation.inspiration_source}</p>
                    
                    <div class="mt-3">
                        <strong>ملخص الناتج:</strong>
                        <p class="bg-light p-3 rounded">${creation.output_summary}</p>
                    </div>
                </div>
            `;
            
            document.getElementById('cognitive-results').innerHTML = resultHtml;
        } else {
            showError('فشل في التوليد الإبداعي: ' + data.message);
        }
    } catch (error) {
        showError('خطأ في التوليد الإبداعي: ' + error.message);
    } finally {
        hideLoading('cognitive-loading');
    }
}

// تطوير الوعي
async function cognitiveConsciousness() {
    showLoading('cognitive-loading');
    
    try {
        const response = await fetch('/api/cognitive/consciousness', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            const consciousness = data.consciousness;
            
            const resultHtml = `
                <div class="alert alert-warning">
                    <h5><i class="fas fa-star"></i> تطوير الوعي</h5>
                    <p><strong>المستوى السابق:</strong> ${consciousness.previous_level.toFixed(3)}</p>
                    <p><strong>المستوى الجديد:</strong> ${consciousness.new_level.toFixed(3)}</p>
                    <p><strong>التحسن:</strong> +${consciousness.improvement.toFixed(3)}</p>
                    <p><strong>استنتاجات الوعي:</strong> ${consciousness.insights_count}</p>
                    <p><strong>أسئلة وجودية:</strong> ${consciousness.questions_count}</p>
                    
                    ${consciousness.insights.length > 0 ? `
                        <div class="mt-3">
                            <strong>استنتاجات الوعي:</strong>
                            <ul>
                                ${consciousness.insights.map(insight => `<li>${insight}</li>`).join('')}
                            </ul>
                        </div>
                    ` : ''}
                    
                    ${consciousness.questions.length > 0 ? `
                        <div class="mt-3">
                            <strong>أسئلة وجودية:</strong>
                            <ul>
                                ${consciousness.questions.map(question => `<li>${question}</li>`).join('')}
                            </ul>
                        </div>
                    ` : ''}
                </div>
            `;
            
            document.getElementById('cognitive-results').innerHTML = resultHtml;
        } else {
            showError('فشل في تطوير الوعي: ' + data.message);
        }
    } catch (error) {
        showError('خطأ في تطوير الوعي: ' + error.message);
    } finally {
        hideLoading('cognitive-loading');
    }
}

// إظهار نافذة التعلم
function showLearningModal() {
    const modal = new bootstrap.Modal(document.getElementById('learningModal'));
    modal.show();
}

// التعلم المستقل
async function cognitiveLearn() {
    const learningData = document.getElementById('learning-data').value.trim();
    
    if (!learningData) {
        showError('يرجى إدخال بيانات للتعلم');
        return;
    }
    
    // إغلاق النافذة
    const modal = bootstrap.Modal.getInstance(document.getElementById('learningModal'));
    modal.hide();
    
    showLoading('cognitive-loading');
    
    try {
        const response = await fetch('/api/cognitive/learn', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data: learningData })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            const learning = data.learning;
            
            const resultHtml = `
                <div class="alert alert-primary">
                    <h5><i class="fas fa-graduation-cap"></i> التعلم المستقل</h5>
                    <p><strong>نوع البيانات:</strong> ${learning.data_type}</p>
                    <p><strong>معرفة مكتسبة:</strong> ${learning.knowledge_gained_count}</p>
                    <p><strong>أنماط مكتشفة:</strong> ${learning.patterns_found_count}</p>
                    <p><strong>تحسن الكفاءة:</strong> +${learning.efficiency_improvement.toFixed(4)}</p>
                    
                    ${learning.knowledge_gained.length > 0 ? `
                        <div class="mt-3">
                            <strong>المعرفة المكتسبة:</strong>
                            <ul>
                                ${learning.knowledge_gained.map(knowledge => `<li>${knowledge}</li>`).join('')}
                            </ul>
                        </div>
                    ` : ''}
                    
                    ${learning.patterns_found.length > 0 ? `
                        <div class="mt-3">
                            <strong>الأنماط المكتشفة:</strong>
                            <ul>
                                ${learning.patterns_found.map(pattern => `<li>${pattern.type}: ${pattern.description}</li>`).join('')}
                            </ul>
                        </div>
                    ` : ''}
                </div>
            `;
            
            document.getElementById('cognitive-results').innerHTML = resultHtml;
        } else {
            showError('فشل في التعلم المستقل: ' + data.message);
        }
    } catch (error) {
        showError('خطأ في التعلم المستقل: ' + error.message);
    } finally {
        hideLoading('cognitive-loading');
    }
}

// رسم أداء النظام
async function plotSystemPerformance() {
    showLoading('visualization-loading');
    
    try {
        const response = await fetch('/api/plot/system_performance');
        const data = await response.json();
        
        if (data.status === 'success') {
            document.getElementById('performance-chart').src = data.image;
            document.getElementById('chart-container').style.display = 'block';
        } else {
            showError('فشل في رسم أداء النظام: ' + data.message);
        }
    } catch (error) {
        showError('خطأ في رسم أداء النظام: ' + error.message);
    } finally {
        hideLoading('visualization-loading');
    }
}

// تصدير النتائج
function exportResults() {
    const results = {
        timestamp: new Date().toISOString(),
        system_status: document.getElementById('system-status').textContent,
        performance_score: document.getElementById('performance-score').textContent,
        inheritances_count: document.getElementById('inheritances-count').textContent,
        adaptations_count: document.getElementById('adaptations-count').textContent,
        evolution_results: document.getElementById('evolution-results').innerHTML,
        semantic_results: document.getElementById('semantic-results').innerHTML,
        cognitive_results: document.getElementById('cognitive-results').innerHTML
    };
    
    const dataStr = JSON.stringify(results, null, 2);
    const dataBlob = new Blob([dataStr], {type: 'application/json'});
    
    const link = document.createElement('a');
    link.href = URL.createObjectURL(dataBlob);
    link.download = `baserah_results_${new Date().toISOString().slice(0, 19).replace(/:/g, '-')}.json`;
    link.click();
}

// دوال مساعدة
function showLoading(elementId) {
    document.getElementById(elementId).style.display = 'block';
}

function hideLoading(elementId) {
    document.getElementById(elementId).style.display = 'none';
}

function showError(message) {
    alert('خطأ: ' + message);
}

function showSuccess(message) {
    alert('نجح: ' + message);
}
