import json
from pathlib import Path
from unittest.mock import patch, mock_open, Mock
import pytest
from test_collection import test_collection


class TestTestCollection:
    
    def test_collection_file_not_found(self, tmp_path):
        with patch('test_collection.Path') as mock_path:
            mock_path.return_value.exists.return_value = False
            
            with patch('builtins.print') as mock_print:
                test_collection()
                
            mock_print.assert_called_with("❌ Collection file not found!")
    
    def test_collection_valid_file(self, tmp_path):
        # Create a mock collection
        mock_collection = {
            "info": {
                "name": "Test Canvas API Collection"
            },
            "item": [
                {
                    "name": "Courses",
                    "item": [
                        {
                            "name": "List Courses",
                            "request": {
                                "method": "GET",
                                "url": {
                                    "raw": "{{base_url}}/api/v1/courses"
                                }
                            }
                        },
                        {
                            "name": "Create Course",
                            "request": {
                                "method": "POST",
                                "url": {
                                    "raw": "{{base_url}}/api/v1/courses"
                                }
                            }
                        }
                    ]
                },
                {
                    "name": "Users", 
                    "item": [
                        {
                            "name": "List Users",
                            "request": {
                                "method": "GET",
                                "url": {
                                    "raw": "{{base_url}}/api/v1/users"
                                }
                            }
                        }
                    ]
                }
            ]
        }
        
        # Create actual test file
        collection_file = tmp_path / "canvas_api.postman_collection.json"
        collection_file.write_text(json.dumps(mock_collection))
        
        with patch('test_collection.Path') as mock_path_class:
            mock_path_instance = Mock()
            mock_path_instance.exists.return_value = True
            mock_path_class.return_value = mock_path_instance
            
            with patch('builtins.open', mock_open(read_data=json.dumps(mock_collection))):
                with patch('builtins.print') as mock_print:
                    test_collection()
                    
                # Verify the expected print statements
                print_calls = [call.args[0] for call in mock_print.call_args_list]
                
                assert "✅ Collection loaded successfully!" in print_calls
                assert "📊 Collection name: Test Canvas API Collection" in print_calls
                assert "📊 Total resource folders: 2" in print_calls
                assert "📊 Total endpoints: 3" in print_calls
                assert "\n✅ Collection validation complete!" in print_calls
    
    def test_collection_with_courses_folder(self, tmp_path):
        mock_collection = {
            "info": {"name": "Test Collection"},
            "item": [
                {
                    "name": "Courses",
                    "item": [
                        {
                            "name": "List Courses",
                            "request": {
                                "method": "GET",
                                "url": {
                                    "raw": "{{base_url}}/api/v1/courses"
                                }
                            }
                        }
                    ]
                }
            ]
        }
        
        with patch('test_collection.Path') as mock_path_class:
            mock_path_instance = Mock()
            mock_path_instance.exists.return_value = True
            mock_path_class.return_value = mock_path_instance
            
            with patch('builtins.open', mock_open(read_data=json.dumps(mock_collection))):
                with patch('builtins.print') as mock_print:
                    test_collection()
                    
                print_calls = [call.args[0] for call in mock_print.call_args_list]
                
                # Should show sample endpoint details
                assert any("🔍 Sample endpoint: List Courses" in call for call in print_calls)
                assert any("Method: GET" in call for call in print_calls)
                assert any("URL: {{base_url}}/api/v1/courses" in call for call in print_calls)
    
    def test_collection_no_courses_folder(self, tmp_path):
        mock_collection = {
            "info": {"name": "Test Collection"},
            "item": [
                {
                    "name": "Users",
                    "item": [{"name": "List Users"}]
                }
            ]
        }
        
        with patch('test_collection.Path') as mock_path_class:
            mock_path_instance = Mock()
            mock_path_instance.exists.return_value = True
            mock_path_class.return_value = mock_path_instance
            
            with patch('builtins.open', mock_open(read_data=json.dumps(mock_collection))):
                with patch('builtins.print') as mock_print:
                    test_collection()
                    
                print_calls = [call.args[0] for call in mock_print.call_args_list]
                
                # Should not show sample endpoint details since no Courses folder
                assert not any("🔍 Sample endpoint:" in call for call in print_calls)
    
    def test_collection_empty_folders(self, tmp_path):
        mock_collection = {
            "info": {"name": "Test Collection"},
            "item": [
                {
                    "name": "Empty Folder",
                    "item": []
                }
            ]
        }
        
        with patch('test_collection.Path') as mock_path_class:
            mock_path_instance = Mock()
            mock_path_instance.exists.return_value = True
            mock_path_class.return_value = mock_path_instance
            
            with patch('builtins.open', mock_open(read_data=json.dumps(mock_collection))):
                with patch('builtins.print') as mock_print:
                    test_collection()
                    
                print_calls = [call.args[0] for call in mock_print.call_args_list]
                
                assert "📊 Total endpoints: 0" in print_calls
    
    def test_collection_invalid_json(self, tmp_path):
        with patch('test_collection.Path') as mock_path_class:
            mock_path_instance = Mock()
            mock_path_instance.exists.return_value = True
            mock_path_class.return_value = mock_path_instance
            
            with patch('builtins.open', mock_open(read_data="invalid json content")):
                with pytest.raises(json.JSONDecodeError):
                    test_collection()
    
    def test_collection_missing_keys(self, tmp_path):
        # Collection with missing expected keys
        mock_collection = {
            "info": {"name": "Test Collection"}
            # Missing 'item' key
        }
        
        with patch('test_collection.Path') as mock_path_class:
            mock_path_instance = Mock()
            mock_path_instance.exists.return_value = True
            mock_path_class.return_value = mock_path_instance
            
            with patch('builtins.open', mock_open(read_data=json.dumps(mock_collection))):
                with pytest.raises(KeyError):
                    test_collection()
    
    def test_sample_folders_display(self, tmp_path):
        # Test with more than 5 folders to verify only first 5 are shown
        mock_collection = {
            "info": {"name": "Test Collection"},
            "item": [
                {"name": f"Folder {i}", "item": [{"name": f"Endpoint {i}"}]} 
                for i in range(1, 8)  # 7 folders
            ]
        }
        
        with patch('test_collection.Path') as mock_path_class:
            mock_path_instance = Mock()
            mock_path_instance.exists.return_value = True
            mock_path_class.return_value = mock_path_instance
            
            with patch('builtins.open', mock_open(read_data=json.dumps(mock_collection))):
                with patch('builtins.print') as mock_print:
                    test_collection()
                    
                print_calls = [call.args[0] for call in mock_print.call_args_list]
                
                # Should show first 5 folders in sample
                folder_displays = [call for call in print_calls if "Folder" in call and ":" in call]
                assert len(folder_displays) == 5  # Only first 5 should be displayed


class TestMainExecution:
    
    @patch('test_collection.test_collection')
    def test_main_execution(self, mock_test_collection):
        # Test that the main execution calls test_collection
        import test_collection
        
        # Simulate running the script
        if __name__ == "__main__":
            test_collection.test_collection()
            
        # In actual execution, we can't easily test this without running the script
        # But we can verify the function exists and is callable
        assert callable(test_collection.test_collection)
