import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from io import StringIO
import generate_openapi


class TestGenerateOpenAPICLI:
    
    def test_main_default_arguments(self, temp_docs_dir, temp_output_dir, capsys):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(temp_output_dir)
        ]
        
        mock_generator = Mock()
        mock_generator.save_spec.return_value = {
            "json": str(temp_output_dir / "canvas_api.openapi.json"),
            "yaml": str(temp_output_dir / "canvas_api.openapi.yaml")
        }
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', return_value=mock_generator):
            with patch.object(sys, 'argv', test_args):
                generate_openapi.main()
                
        mock_generator.save_spec.assert_called_once_with(
            output_dir=str(temp_output_dir),
            formats=["json", "yaml"]
        )
        
        captured = capsys.readouterr()
        assert "Starting Canvas API OpenAPI generation" in captured.out
        assert "Successfully generated OpenAPI specification" in captured.out
        
    def test_main_json_format_only(self, temp_docs_dir, temp_output_dir):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(temp_output_dir),
            "--format", "json"
        ]
        
        mock_generator = Mock()
        mock_generator.save_spec.return_value = {
            "json": str(temp_output_dir / "canvas_api.openapi.json")
        }
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', return_value=mock_generator):
            with patch.object(sys, 'argv', test_args):
                generate_openapi.main()
                
        mock_generator.save_spec.assert_called_once_with(
            output_dir=str(temp_output_dir),
            formats=["json"]
        )
        
    def test_main_yaml_format_only(self, temp_docs_dir, temp_output_dir):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(temp_output_dir),
            "--format", "yaml"
        ]
        
        mock_generator = Mock()
        mock_generator.save_spec.return_value = {
            "yaml": str(temp_output_dir / "canvas_api.openapi.yaml")
        }
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', return_value=mock_generator):
            with patch.object(sys, 'argv', test_args):
                generate_openapi.main()
                
        mock_generator.save_spec.assert_called_once_with(
            output_dir=str(temp_output_dir),
            formats=["yaml"]
        )
        
    def test_main_both_formats(self, temp_docs_dir, temp_output_dir):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(temp_output_dir),
            "--format", "both"
        ]
        
        mock_generator = Mock()
        mock_generator.save_spec.return_value = {
            "json": str(temp_output_dir / "canvas_api.openapi.json"),
            "yaml": str(temp_output_dir / "canvas_api.openapi.yaml")
        }
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', return_value=mock_generator):
            with patch.object(sys, 'argv', test_args):
                generate_openapi.main()
                
        mock_generator.save_spec.assert_called_once_with(
            output_dir=str(temp_output_dir),
            formats=["json", "yaml"]
        )
        
    def test_main_with_validation_success(self, temp_docs_dir, temp_output_dir, capsys):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(temp_output_dir),
            "--validate"
        ]
        
        mock_generator = Mock()
        mock_generator.save_spec.return_value = {
            "json": str(temp_output_dir / "canvas_api.openapi.json"),
            "yaml": str(temp_output_dir / "canvas_api.openapi.yaml")
        }
        mock_generator.validate_spec.return_value = True
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', return_value=mock_generator):
            with patch.object(sys, 'argv', test_args):
                generate_openapi.main()
                
        mock_generator.validate_spec.assert_called_once()
        
        captured = capsys.readouterr()
        assert "Validating OpenAPI specification" in captured.out
        
    def test_main_with_validation_failure(self, temp_docs_dir, temp_output_dir):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(temp_output_dir),
            "--validate"
        ]
        
        mock_generator = Mock()
        mock_generator.save_spec.return_value = {
            "json": str(temp_output_dir / "canvas_api.openapi.json")
        }
        mock_generator.validate_spec.return_value = False
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', return_value=mock_generator):
            with patch.object(sys, 'argv', test_args):
                with pytest.raises(SystemExit) as exc_info:
                    generate_openapi.main()
                    
        assert exc_info.value.code == 1
        
    def test_main_with_verbose_flag(self, temp_docs_dir, temp_output_dir):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(temp_output_dir),
            "--verbose"
        ]
        
        mock_generator = Mock()
        mock_generator.save_spec.return_value = {
            "json": str(temp_output_dir / "canvas_api.openapi.json")
        }
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', return_value=mock_generator):
            with patch.object(sys, 'argv', test_args):
                generate_openapi.main()
                
    def test_main_handles_generator_exception(self, temp_docs_dir, temp_output_dir, capsys):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(temp_output_dir)
        ]
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', side_effect=Exception("Test error")):
            with patch.object(sys, 'argv', test_args):
                with pytest.raises(SystemExit) as exc_info:
                    generate_openapi.main()
                    
        assert exc_info.value.code == 1
        
        captured = capsys.readouterr()
        assert "Error: Test error" in captured.out
        
    def test_main_handles_generator_exception_with_verbose(self, temp_docs_dir, temp_output_dir, capsys):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(temp_output_dir),
            "--verbose"
        ]
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', side_effect=Exception("Test error")):
            with patch.object(sys, 'argv', test_args):
                with patch('traceback.print_exc') as mock_traceback:
                    with pytest.raises(SystemExit) as exc_info:
                        generate_openapi.main()
                        
        assert exc_info.value.code == 1
        mock_traceback.assert_called_once()
        
    def test_main_handles_save_spec_exception(self, temp_docs_dir, temp_output_dir, capsys):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(temp_output_dir)
        ]
        
        mock_generator = Mock()
        mock_generator.save_spec.side_effect = Exception("Save error")
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', return_value=mock_generator):
            with patch.object(sys, 'argv', test_args):
                with pytest.raises(SystemExit) as exc_info:
                    generate_openapi.main()
                    
        assert exc_info.value.code == 1
        
        captured = capsys.readouterr()
        assert "Error: Save error" in captured.out
        
    def test_main_prints_next_steps(self, temp_docs_dir, temp_output_dir, capsys):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(temp_output_dir)
        ]
        
        mock_generator = Mock()
        mock_generator.save_spec.return_value = {
            "json": str(temp_output_dir / "canvas_api.openapi.json"),
            "yaml": str(temp_output_dir / "canvas_api.openapi.yaml")
        }
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', return_value=mock_generator):
            with patch.object(sys, 'argv', test_args):
                generate_openapi.main()
                
        captured = capsys.readouterr()
        assert "Next steps:" in captured.out
        assert "Generate Python SDK: python generate_sdk.py" in captured.out
        assert "View spec online: https://editor.swagger.io/" in captured.out
        assert "Generate other clients: https://openapi-generator.tech/" in captured.out
        
    def test_main_prints_file_paths(self, temp_docs_dir, temp_output_dir, capsys):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(temp_output_dir)
        ]
        
        json_path = str(temp_output_dir / "canvas_api.openapi.json")
        yaml_path = str(temp_output_dir / "canvas_api.openapi.yaml")
        
        mock_generator = Mock()
        mock_generator.save_spec.return_value = {
            "json": json_path,
            "yaml": yaml_path
        }
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', return_value=mock_generator):
            with patch.object(sys, 'argv', test_args):
                generate_openapi.main()
                
        captured = capsys.readouterr()
        assert f"JSON: {json_path}" in captured.out
        assert f"YAML: {yaml_path}" in captured.out
        
    def test_main_default_docs_dir(self, temp_output_dir):
        test_args = [
            "generate_openapi.py",
            "--output-dir", str(temp_output_dir)
        ]
        
        mock_generator = Mock()
        mock_generator.save_spec.return_value = {"json": "test.json"}
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', return_value=mock_generator) as mock_class:
            with patch.object(sys, 'argv', test_args):
                generate_openapi.main()
                
        mock_class.assert_called_once_with(docs_dir="data/canvas_api_resources")
        
    def test_main_default_output_dir(self, temp_docs_dir):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir)
        ]
        
        mock_generator = Mock()
        mock_generator.save_spec.return_value = {"json": "test.json"}
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', return_value=mock_generator):
            with patch.object(sys, 'argv', test_args):
                generate_openapi.main()
                
        mock_generator.save_spec.assert_called_once_with(
            output_dir="output",
            formats=["json", "yaml"]
        )
        
    def test_argument_parser_help(self, capsys):
        test_args = ["generate_openapi.py", "--help"]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                generate_openapi.main()
                
        assert exc_info.value.code == 0
        
        captured = capsys.readouterr()
        assert "Generate OpenAPI specification from Canvas API documentation" in captured.out
        assert "--docs-dir" in captured.out
        assert "--output-dir" in captured.out
        assert "--format" in captured.out
        assert "--validate" in captured.out
        assert "--verbose" in captured.out
        
    def test_invalid_format_argument(self, capsys):
        test_args = [
            "generate_openapi.py",
            "--format", "invalid"
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                generate_openapi.main()
                
        assert exc_info.value.code == 2
        
    def test_main_prints_source_and_output_info(self, temp_docs_dir, temp_output_dir, capsys):
        test_args = [
            "generate_openapi.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(temp_output_dir)
        ]
        
        mock_generator = Mock()
        mock_generator.save_spec.return_value = {"json": "test.json"}
        
        with patch('generate_openapi.CanvasOpenAPIGenerator', return_value=mock_generator):
            with patch.object(sys, 'argv', test_args):
                generate_openapi.main()
                
        captured = capsys.readouterr()
        assert f"Source: {temp_docs_dir}" in captured.out
        assert f"Output: {temp_output_dir}" in captured.out
        assert "Format: json, yaml" in captured.out
