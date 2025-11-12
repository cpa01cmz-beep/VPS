import unittest
import os
import yaml

class TestGeminiWorkflow(unittest.TestCase):
    def test_workflow_file_exists(self):
        """Test that the Gemini workflow file exists"""
        workflow_path = ".github/workflows/gemini-researcher.yml"
        self.assertTrue(os.path.exists(workflow_path), f"Workflow file {workflow_path} does not exist")
    
    def test_workflow_structure(self):
        """Test that the workflow file has the correct structure"""
        workflow_path = ".github/workflows/gemini-researcher.yml"
        with open(workflow_path, 'r') as file:
            workflow = yaml.safe_load(file)
        
        # Check if required keys exist
        self.assertIn('name', workflow)
        self.assertIn(True, workflow)  # 'on' is a reserved word in YAML and gets converted to True
        self.assertIn('jobs', workflow)
        
        # Check if research job exists
        self.assertIn('research', workflow['jobs'])
        
        # Check if research job has required steps
        steps = workflow['jobs']['research']['steps']
        step_names = [step['name'] for step in steps]
        
        self.assertIn('Checkout repository', step_names)
        self.assertIn('Run Gemini CLI', step_names)
        self.assertIn('Write output to file', step_names)
        self.assertIn('Commit and push if changed', step_names)

if __name__ == '__main__':
    unittest.main()