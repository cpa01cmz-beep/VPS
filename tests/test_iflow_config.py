import unittest
from unittest.mock import patch, mock_open
import os
import yaml

class TestIflowConfig(unittest.TestCase):
    def setUp(self):
        self.config_file = '.github/iflow/config.yaml'
        self.expected_config = {
            'default_branch': 'main',
            'branch_prefix': 'iflow/',
            'label': 'orchestration',
            'maintenance_schedule': '0 2 * * 1-5',
            'intelijen_schedule': '0 3 * * 1',
            'research_schedule': '0 3 * * 1',
            'test_command': 'python -m pytest tests/',
            'lint_command': 'ruff check .',
            'format_command': 'ruff format .'
        }

    def test_config_file_exists(self):
        """Test that the config file exists"""
        self.assertTrue(os.path.exists(self.config_file))

    def test_config_file_is_valid_yaml(self):
        """Test that the config file is valid YAML"""
        with open(self.config_file, 'r') as f:
            config = yaml.safe_load(f)
        self.assertIsInstance(config, dict)

    def test_config_contains_expected_keys(self):
        """Test that the config contains all expected keys"""
        with open(self.config_file, 'r') as f:
            config = yaml.safe_load(f)
        
        for key in self.expected_config:
            self.assertIn(key, config)

    def test_config_values_are_correct(self):
        """Test that the config values are correct"""
        with open(self.config_file, 'r') as f:
            config = yaml.safe_load(f)
        
        for key, expected_value in self.expected_config.items():
            self.assertEqual(config[key], expected_value)

if __name__ == '__main__':
    unittest.main()