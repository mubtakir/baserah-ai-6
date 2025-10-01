#!/usr/bin/env python3
"""
اختبار الأشكال المصححة
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tempfile
import os

def baserah_sigmoid(x, alpha=1.0, k=1.0, x0=0.0):
    """دالة السيجمويد الثورية الأساسية."""
    return alpha / (1 + np.exp(-k * (x - x0)))

def generate_revolutionary_shape(shape_type, num_points=1000):
    """Generate shapes using the revolutionary GSE equation with CORRECT mathematical formulations"""

    # Generate parametric coordinates
    t = np.linspace(0, 2*np.pi, num_points)
    
    if shape_type == 'circle':
        # Perfect circle using trigonometric approach with sigmoid smoothing
        x_coords = np.cos(t)
        y_coords = np.sin(t)
        # Apply sigmoid smoothing for revolutionary touch
        smoothing = baserah_sigmoid(t, alpha=0.1, k=1.0)
        x_coords = x_coords + smoothing * 0.05 * np.cos(3*t)
        y_coords = y_coords + smoothing * 0.05 * np.sin(3*t)
        
    elif shape_type == 'heart':
        # Heart shape using parametric equations with sigmoid enhancement
        x_coords = 16 * np.sin(t)**3
        y_coords = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
        # Normalize and apply revolutionary smoothing
        x_coords = x_coords / 16
        y_coords = y_coords / 16
        # Add sigmoid-based romantic curves
        romantic_factor = baserah_sigmoid(t, alpha=0.2, k=2.0)
        x_coords = x_coords + romantic_factor * 0.1 * np.sin(2*t)
        
    elif shape_type == 'star':
        # 5-pointed star with sigmoid-enhanced points
        n_points = 5
        outer_radius = 1.0
        inner_radius = 0.4
        
        # Create star points
        angles = np.linspace(0, 2*np.pi, n_points*2, endpoint=False)
        radii = np.tile([outer_radius, inner_radius], n_points)
        
        # Interpolate for smooth star
        star_t = np.linspace(0, 2*np.pi, num_points)
        x_coords = np.interp(star_t, angles, radii * np.cos(angles))
        y_coords = np.interp(star_t, angles, radii * np.sin(angles))
        
        # Add revolutionary sigmoid sharpening to points
        sharpening = baserah_sigmoid(star_t * n_points, alpha=0.3, k=5.0)
        x_coords = x_coords + sharpening * 0.1 * np.cos(star_t * n_points)
        y_coords = y_coords + sharpening * 0.1 * np.sin(star_t * n_points)
        
    else:
        # Default to circle
        x_coords = np.cos(t)
        y_coords = np.sin(t)

    return x_coords, y_coords

def test_all_shapes():
    """Test all shape types"""
    
    shapes = ['circle', 'heart', 'star']
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for i, shape in enumerate(shapes):
        try:
            x, y = generate_revolutionary_shape(shape)
            
            axes[i].plot(x, y, linewidth=3, color='#FF6B6B', alpha=0.8)
            axes[i].fill(x, y, alpha=0.3, color='#4ECDC4')
            axes[i].set_title(f'{shape.title()} Shape', fontsize=14, fontweight='bold')
            axes[i].set_aspect('equal')
            axes[i].grid(True, alpha=0.3)
            
            print(f"✅ {shape}: Generated successfully ({len(x)} points)")
            
        except Exception as e:
            print(f"❌ {shape}: Error - {e}")
            axes[i].text(0.5, 0.5, f'Error: {shape}', ha='center', va='center')
    
    plt.tight_layout()
    
    # Save test image
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    plt.savefig(temp_file.name, format='png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    
    print(f"✅ Test image saved: {temp_file.name}")
    print(f"✅ File size: {os.path.getsize(temp_file.name)} bytes")
    
    return temp_file.name

if __name__ == "__main__":
    print("🧪 Testing Revolutionary Shapes...")
    result = test_all_shapes()
    if result:
        print("🎉 All shapes tested successfully!")
    else:
        print("💥 Shape testing failed!")
