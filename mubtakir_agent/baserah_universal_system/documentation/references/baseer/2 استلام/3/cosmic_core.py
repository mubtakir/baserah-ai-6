"""
Cosmic Core Integration Module for the Basira System
Developed by: Bassel Yahya Abdullah

This module integrates the Universal Equation components with the rest of the Basira System,
providing a unified interface for accessing and manipulating the mathematical foundation.
"""

import numpy as np
from typing import Dict, Any, List, Tuple, Optional, Union, Callable

from basira_system.cosmic_core.universal_equation.equation_metadata import EquationMetadata
from basira_system.cosmic_core.universal_equation.equation_components import (
    EquationComponent, ConstantComponent, VariableComponent, 
    OperationComponent, AdditionComponent, MultiplicationComponent
)
from basira_system.cosmic_core.universal_equation.universal_equation import UniversalEquation

class CosmicCore:
    """
    The CosmicCore class serves as the central integration point for the Universal Equation
    and its components, providing a unified interface for the rest of the Basira System.
    
    This class implements the innovative approach of using adaptive mathematical equations
    rather than traditional neural networks, as envisioned by Bassel Yahya Abdullah.
    """
    
    def __init__(self):
        """Initialize the CosmicCore with default settings."""
        self.universal_equations = {}
        self.active_equation_id = None
        self.equation_registry = {}
        
    def create_equation(self, name: str, description: str = "", 
                       domain: str = "general") -> str:
        """
        Create a new Universal Equation instance.
        
        Args:
            name: A descriptive name for the equation
            description: A detailed description of the equation's purpose
            domain: The domain this equation is designed for
            
        Returns:
            The unique ID of the created equation
        """
        metadata = EquationMetadata(
            name=name,
            description=description,
            tags=[domain]
        )
        
        equation = UniversalEquation(metadata=metadata)
        equation_id = metadata.equation_id  # Using equation_id attribute from the metadata
        
        self.universal_equations[equation_id] = equation
        self.equation_registry[equation_id] = {
            "name": name,
            "description": description,
            "domain": domain,
            "creation_timestamp": metadata.creation_timestamp
        }
        
        # Set as active equation if none is currently active
        if self.active_equation_id is None:
            self.active_equation_id = equation_id
            
        return equation_id
    
    def get_equation(self, equation_id: str) -> Optional[UniversalEquation]:
        """
        Retrieve a Universal Equation by its ID.
        
        Args:
            equation_id: The unique ID of the equation
            
        Returns:
            The UniversalEquation instance or None if not found
        """
        return self.universal_equations.get(equation_id)
    
    def set_active_equation(self, equation_id: str) -> bool:
        """
        Set the active equation for operations that don't specify an equation ID.
        
        Args:
            equation_id: The unique ID of the equation to set as active
            
        Returns:
            True if successful, False if the equation ID doesn't exist
        """
        if equation_id in self.universal_equations:
            self.active_equation_id = equation_id
            return True
        return False
    
    def get_active_equation(self) -> Optional[UniversalEquation]:
        """
        Get the currently active Universal Equation.
        
        Returns:
            The active UniversalEquation instance or None if none is active
        """
        if self.active_equation_id:
            return self.universal_equations.get(self.active_equation_id)
        return None
    
    def list_equations(self) -> List[Dict[str, Any]]:
        """
        List all registered equations with their metadata.
        
        Returns:
            A list of dictionaries containing equation metadata
        """
        return [
            {
                "id": eq_id,
                "name": info["name"],
                "description": info["description"],
                "domain": info["domain"],
                "creation_timestamp": info["creation_timestamp"]
            }
            for eq_id, info in self.equation_registry.items()
        ]
    
    def add_component(self, equation_id: str, component: EquationComponent) -> bool:
        """
        Add a component to a Universal Equation.
        
        Args:
            equation_id: The unique ID of the equation
            component: The EquationComponent to add
            
        Returns:
            True if successful, False otherwise
        """
        equation = self.get_equation(equation_id)
        if equation is None:
            return False
        
        # In a real implementation, this would integrate with the UniversalEquation's
        # component management system
        # For now, we'll just simulate this
        component_id = component.component_id
        equation.components[component_id] = component
        return True
    
    def evaluate_equation(self, equation_id: str, inputs: Dict[str, Any], 
                         context: Dict[str, Any] = None) -> Any:
        """
        Evaluate a Universal Equation with the given inputs.
        
        Args:
            equation_id: The unique ID of the equation
            inputs: Dictionary of input values
            context: Optional context for evaluation
            
        Returns:
            The result of the equation evaluation
        """
        equation = self.get_equation(equation_id)
        if equation is None:
            raise ValueError(f"Equation with ID {equation_id} not found")
        
        # In a real implementation, this would use the UniversalEquation's evaluate method
        # For now, we'll just simulate this
        return equation.evaluate(inputs, context=context)
    
    def adapt_equation(self, equation_id: str, training_data: List[Dict[str, Any]], 
                      learning_rate: float = 0.01, iterations: int = 100) -> Dict[str, Any]:
        """
        Adapt a Universal Equation to better fit the provided training data.
        
        Args:
            equation_id: The unique ID of the equation
            training_data: List of input-output pairs for training
            learning_rate: Learning rate for adaptation
            iterations: Number of adaptation iterations
            
        Returns:
            Dictionary containing adaptation results
        """
        equation = self.get_equation(equation_id)
        if equation is None:
            raise ValueError(f"Equation with ID {equation_id} not found")
        
        # In a real implementation, this would use the UniversalEquation's adapt method
        # For now, we'll just simulate this
        result = equation.adapt(training_data, learning_rate=learning_rate, iterations=iterations)
        
        # Update metadata to reflect adaptation
        if hasattr(equation.metadata, 'log_adaptation'):
            equation.metadata.log_adaptation({
                "training_data_size": len(training_data),
                "learning_rate": learning_rate,
                "iterations": iterations,
                "result": result
            })
        else:
            # Fallback for the universal_equation.py implementation
            equation.metadata.add_evolution_record(
                f"Adapted with {len(training_data)} training samples",
                {"learning_rate": learning_rate, "iterations": iterations}
            )
        
        return result
    
    def evolve_equation(self, equation_id: str, evolution_strategy: str, 
                       parameters: Dict[str, Any] = None) -> str:
        """
        Evolve a Universal Equation to create a new, improved version.
        
        Args:
            equation_id: The unique ID of the equation to evolve
            evolution_strategy: The strategy to use for evolution
            parameters: Additional parameters for the evolution process
            
        Returns:
            The unique ID of the newly evolved equation
        """
        source_equation = self.get_equation(equation_id)
        if source_equation is None:
            raise ValueError(f"Equation with ID {equation_id} not found")
        
        parameters = parameters or {}
        
        # Create a new equation based on the source
        source_metadata = source_equation.metadata
        
        # Create new metadata for evolved equation
        new_metadata = EquationMetadata(
            name=f"Evolved from {source_metadata.name}",
            description=f"Evolved using {evolution_strategy} strategy from equation {equation_id}",
            parent_id=equation_id,
            tags=source_metadata.tags.copy() if hasattr(source_metadata, 'tags') else []
        )
        
        # In a real implementation, this would clone and modify the equation structure
        # For now, we'll just create a new equation with updated metadata
        new_equation = UniversalEquation(metadata=new_metadata)
        new_equation_id = new_metadata.equation_id  # Using equation_id attribute
        
        # Register the new equation
        self.universal_equations[new_equation_id] = new_equation
        self.equation_registry[new_equation_id] = {
            "name": new_metadata.name,
            "description": new_metadata.description,
            "domain": source_metadata.tags[0] if hasattr(source_metadata, 'tags') else "general",
            "creation_timestamp": new_metadata.creation_timestamp
        }
        
        # Log the evolution in the source equation
        if hasattr(source_metadata, 'log_evolution'):
            source_metadata.log_evolution({
                "strategy": evolution_strategy,
                "parameters": parameters,
                "new_equation_id": new_equation_id
            })
        else:
            # Fallback for the universal_equation.py implementation
            source_metadata.add_evolution_record(
                f"Evolved using {evolution_strategy} strategy",
                {"parameters": parameters, "new_equation_id": new_equation_id}
            )
        
        return new_equation_id
    
    def save_equation(self, equation_id: str, filepath: str) -> bool:
        """
        Save a Universal Equation to a file.
        
        Args:
            equation_id: The unique ID of the equation
            filepath: Path to save the equation
            
        Returns:
            True if successful, False otherwise
        """
        equation = self.get_equation(equation_id)
        if equation is None:
            return False
        
        try:
            equation.save(filepath)
            return True
        except Exception as e:
            print(f"Error saving equation: {e}")
            return False
    
    def load_equation(self, filepath: str) -> Optional[str]:
        """
        Load a Universal Equation from a file.
        
        Args:
            filepath: Path to the equation file
            
        Returns:
            The unique ID of the loaded equation, or None if loading failed
        """
        try:
            equation = UniversalEquation()
            success = equation.load(filepath)
            
            if not success:
                return None
                
            # Use the equation_id attribute from metadata
            equation_id = equation.metadata.equation_id
            
            # Register the loaded equation
            self.universal_equations[equation_id] = equation
            self.equation_registry[equation_id] = {
                "name": equation.metadata.name,
                "description": equation.metadata.description,
                "domain": equation.metadata.tags[0] if hasattr(equation.metadata, 'tags') else "general",
                "creation_timestamp": equation.metadata.creation_timestamp
            }
            
            return equation_id
        except Exception as e:
            print(f"Error loading equation: {e}")
            return None
