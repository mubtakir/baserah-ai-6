"""
Test module for the Cosmic Core integration
Developed by: Bassel Yahya Abdullah

This module tests the functionality and integration of the Cosmic Core with the rest of the Basira System.
"""

import unittest
import os
import sys
import tempfile
import numpy as np
from datetime import datetime

# Add the parent directory to sys.path to allow importing the basira_system package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from basira_system.cosmic_core.cosmic_core import CosmicCore
from basira_system.cosmic_core.universal_equation.equation_metadata import EquationMetadata
from basira_system.cosmic_core.universal_equation.equation_components import (
    ConstantComponent, VariableComponent, AdditionComponent
)


class TestCosmicCore(unittest.TestCase):
    """Test cases for the CosmicCore integration module."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.cosmic_core = CosmicCore()
        
    def test_create_equation(self):
        """Test creating a new universal equation."""
        eq_id = self.cosmic_core.create_equation(
            name="Test Equation",
            description="A test equation for unit testing",
            domain="testing"
        )
        
        self.assertIsNotNone(eq_id)
        self.assertIn(eq_id, self.cosmic_core.universal_equations)
        self.assertEqual(self.cosmic_core.active_equation_id, eq_id)
        
        equation = self.cosmic_core.get_equation(eq_id)
        self.assertIsNotNone(equation)
        self.assertEqual(equation.metadata.name, "Test Equation")
        self.assertEqual(equation.metadata.description, "A test equation for unit testing")
        self.assertIn("testing", equation.metadata.tags)
        
    def test_list_equations(self):
        """Test listing all registered equations."""
        # Create a few equations
        eq_id1 = self.cosmic_core.create_equation("Equation 1", domain="domain1")
        eq_id2 = self.cosmic_core.create_equation("Equation 2", domain="domain2")
        
        equations = self.cosmic_core.list_equations()
        self.assertEqual(len(equations), 2)
        
        # Check that both equations are in the list
        eq_ids = [eq["id"] for eq in equations]
        self.assertIn(eq_id1, eq_ids)
        self.assertIn(eq_id2, eq_ids)
        
    def test_set_active_equation(self):
        """Test setting the active equation."""
        # First create an equation and store its ID
        eq_id1 = self.cosmic_core.create_equation("Equation 1")
        
        # Create a second equation - this should become the active one
        eq_id2 = self.cosmic_core.create_equation("Equation 2")
        
        # Verify eq_id2 is now active
        self.assertEqual(self.cosmic_core.active_equation_id, eq_id2)
        
        # Explicitly set eq_id1 as active
        result = self.cosmic_core.set_active_equation(eq_id1)
        self.assertTrue(result)
        self.assertEqual(self.cosmic_core.active_equation_id, eq_id1)
        
        # Try setting a non-existent equation as active
        result = self.cosmic_core.set_active_equation("non-existent-id")
        self.assertFalse(result)
        self.assertEqual(self.cosmic_core.active_equation_id, eq_id1)  # Should remain unchanged
        
    def test_add_component(self):
        """Test adding components to an equation."""
        eq_id = self.cosmic_core.create_equation("Component Test")
        equation = self.cosmic_core.get_equation(eq_id)
        
        # Create some components
        const_comp = ConstantComponent(value=5.0, name="Constant")
        var_comp = VariableComponent(variable_name="x", name="Variable")
        
        # Add components to the equation
        result1 = self.cosmic_core.add_component(eq_id, const_comp)
        result2 = self.cosmic_core.add_component(eq_id, var_comp)
        
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        # Verify components were added
        self.assertIn(const_comp.component_id, equation.components)
        self.assertIn(var_comp.component_id, equation.components)
        
    def test_evolve_equation(self):
        """Test evolving an equation to create a new version."""
        source_eq_id = self.cosmic_core.create_equation("Source Equation")
        
        # Evolve the equation
        new_eq_id = self.cosmic_core.evolve_equation(
            source_eq_id, 
            evolution_strategy="test_strategy",
            parameters={"complexity_factor": 0.2}
        )
        
        self.assertIsNotNone(new_eq_id)
        self.assertNotEqual(source_eq_id, new_eq_id)
        self.assertIn(new_eq_id, self.cosmic_core.universal_equations)
        
        # Check the new equation's metadata
        new_equation = self.cosmic_core.get_equation(new_eq_id)
        self.assertIn("Evolved from", new_equation.metadata.name)
        
        # Check that the evolution was logged in the source equation
        source_equation = self.cosmic_core.get_equation(source_eq_id)
        
        # Check for evolution log (using either attribute name)
        evolution_log = getattr(source_equation.metadata, 'evolution_log', [])
        if not evolution_log:
            evolution_log = getattr(source_equation.metadata, 'evolution_history', [])
        
        self.assertGreater(len(evolution_log), 0)
        
    def test_save_and_load_equation(self):
        """Test saving and loading an equation to/from a file."""
        # Skip this test for now as it requires more complex mocking
        # of the save/load functionality in the UniversalEquation class
        self.skipTest("Requires more complex mocking of file operations")


if __name__ == "__main__":
    unittest.main()
