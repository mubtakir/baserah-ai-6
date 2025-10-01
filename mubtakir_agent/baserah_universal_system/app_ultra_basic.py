import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
import tempfile

def generate_shape(shape_name):
    """Generate basic shapes"""
    try:
        # Create simple shapes
        t = np.linspace(0, 2*np.pi, 100)
        
        if shape_name == "Circle":
            x = np.cos(t)
            y = np.sin(t)
        elif shape_name == "Heart":
            x = 16 * np.sin(t)**3
            y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
            x = x / 16
            y = y / 16
        else:  # Star
            x = np.cos(t) * (1 + 0.3 * np.cos(5*t))
            y = np.sin(t) * (1 + 0.3 * np.cos(5*t))
        
        # Plot
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, 'b-', linewidth=2)
        plt.fill(x, y, alpha=0.3)
        plt.axis('equal')
        plt.grid(True, alpha=0.3)
        plt.title(f'Baserah System: {shape_name}\nCreator: Basil Yahya Abdullah')
        
        # Save
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        plt.savefig(temp_file.name, dpi=100, bbox_inches='tight')
        plt.close()
        
        return temp_file.name
        
    except Exception as e:
        # Error plot
        plt.figure(figsize=(4, 3))
        plt.text(0.5, 0.5, f'Error: {str(e)}', ha='center', va='center')
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        plt.savefig(temp_file.name, dpi=100, bbox_inches='tight')
        plt.close()
        
        return temp_file.name

# Interface
demo = gr.Interface(
    fn=generate_shape,
    inputs=gr.Radio(["Circle", "Heart", "Star"], value="Circle", label="Shape"),
    outputs=gr.Image(label="Result"),
    title="Baserah Universal System",
    description="""
**Revolutionary Mathematical Intelligence by Basil Yahya Abdullah**

Key Ideas:
• Pure Mathematical Intelligence - NO Neural Networks
• Adaptive Equations - Equations adapt when information changes  
• NO AI Libraries - No TensorFlow, PyTorch
• Complete Transparency - Every calculation explainable
• Revolutionary Physical Theories: Zero Duality, Perpendicular Opposites, Filament

System Status: Under Development

This is the future of explainable AI!
    """
)

if __name__ == "__main__":
    demo.launch()
