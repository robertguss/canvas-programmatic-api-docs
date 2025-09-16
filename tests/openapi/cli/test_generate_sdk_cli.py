import pytest
import sys
import subprocess
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import generate_sdk


class TestGenerateSDKCLI:
    
    def test_run_command_success(self, capsys):
        mock_result = Mock()
        mock_result.stdout = "Command output"
        mock_result.stderr = ""
        
        with patch('generate_sdk.subprocess.run', return_value=mock_result) as mock_run:
            result = generate_sdk.run_command(["echo", "test"])
            
        assert result is True
        mock_run.assert_called_once_with(
            ["echo", "test"],
            cwd=None,
            capture_output=True,
            text=True,
            check=True
        )
        
        captured = capsys.readouterr()
        assert "Running: echo test" in captured.out
        assert "Command output" in captured.out
        
    def test_run_command_with_cwd(self, tmp_path):
        mock_result = Mock()
        mock_result.stdout = ""
        
        with patch('generate_sdk.subprocess.run', return_value=mock_result) as mock_run:
            generate_sdk.run_command(["ls"], cwd=tmp_path)
            
        mock_run.assert_called_once_with(
            ["ls"],
            cwd=tmp_path,
            capture_output=True,
            text=True,
            check=True
        )
        
    def test_run_command_failure(self, capsys):
        error = subprocess.CalledProcessError(1, ["false"], stderr="Error message")
        
        with patch('generate_sdk.subprocess.run', side_effect=error):
            result = generate_sdk.run_command(["false"])
            
        assert result is False
        
        captured = capsys.readouterr()
        assert "Command failed" in captured.out
        assert "Error message" in captured.out
        
    def test_main_default_arguments(self, temp_docs_dir, tmp_path, capsys):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk")
        ]
        
        spec_file = tmp_path / "output" / "canvas_api.openapi.json"
        spec_file.parent.mkdir(parents=True)
        spec_file.write_text('{"openapi": "3.1.0"}')
        
        with patch('generate_sdk.shutil.which', return_value="/usr/bin/openapi-python-client"):
            with patch('generate_sdk.run_command', return_value=True) as mock_run:
                with patch.object(sys, 'argv', test_args):
                    with patch('generate_sdk.Path.cwd', return_value=tmp_path):
                        generate_sdk.main()
                        
        captured = capsys.readouterr()
        assert "Generating Python SDK from OpenAPI spec" in captured.out
        assert "Successfully generated Canvas LMS Python SDK" in captured.out
        
    def test_main_with_regenerate_spec(self, temp_docs_dir, tmp_path):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk"),
            "--regenerate-spec"
        ]
        
        spec_file_path = tmp_path / "output" / "canvas_api.openapi.json"
        spec_file_path.parent.mkdir(parents=True, exist_ok=True)
        spec_file_path.write_text('{"openapi": "3.1.0"}')
        
        mock_generator = Mock()
        mock_generator.save_spec.return_value = {
            "json": str(spec_file_path)
        }
        
        with patch('generate_sdk.CanvasOpenAPIGenerator', return_value=mock_generator):
            with patch('generate_sdk.shutil.which', return_value="/usr/bin/openapi-python-client"):
                with patch('generate_sdk.run_command', return_value=True):
                    with patch.object(sys, 'argv', test_args):
                        generate_sdk.main()
                        
        mock_generator.save_spec.assert_called_once_with(formats=["json"])
        
    def test_main_with_clean_flag(self, temp_docs_dir, tmp_path):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk"),
            "--clean"
        ]
        
        output_dir = tmp_path / "sdk"
        output_dir.mkdir()
        (output_dir / "existing_file.txt").write_text("test")
        
        spec_file = tmp_path / "output" / "canvas_api.openapi.json"
        spec_file.parent.mkdir(parents=True)
        spec_file.write_text('{"openapi": "3.1.0"}')
        
        with patch('generate_sdk.shutil.which', return_value="/usr/bin/openapi-python-client"):
            with patch('generate_sdk.run_command', return_value=True):
                with patch.object(sys, 'argv', test_args):
                    with patch('generate_sdk.Path.cwd', return_value=tmp_path):
                        generate_sdk.main()
                        
        assert not (output_dir / "existing_file.txt").exists()
        
    def test_main_spec_file_not_found(self, temp_docs_dir, tmp_path, capsys):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk")
        ]
        
        # Mock Path.exists to return False for the spec file check
        with patch.object(sys, 'argv', test_args):
            with patch('generate_sdk.Path') as mock_path_class:
                # Create mock instances for different Path calls
                def path_side_effect(path_str):
                    mock_path = Mock()
                    if "canvas_api.openapi.json" in str(path_str):
                        mock_path.exists.return_value = False
                    else:
                        mock_path.exists.return_value = True
                        mock_path.mkdir = Mock()
                    return mock_path
                
                mock_path_class.side_effect = path_side_effect
                
                with pytest.raises(SystemExit) as exc_info:
                    generate_sdk.main()
                    
        assert exc_info.value.code == 1
        
        captured = capsys.readouterr()
        assert "OpenAPI spec file not found" in captured.out
        assert "Run with --regenerate-spec" in captured.out
        
    def test_main_installs_openapi_python_client(self, temp_docs_dir, tmp_path, capsys):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk")
        ]
        
        spec_file = tmp_path / "output" / "canvas_api.openapi.json"
        spec_file.parent.mkdir(parents=True)
        spec_file.write_text('{"openapi": "3.1.0"}')
        
        with patch('generate_sdk.shutil.which', return_value=None):
            with patch('generate_sdk.run_command', return_value=True) as mock_run:
                with patch.object(sys, 'argv', test_args):
                    with patch('generate_sdk.Path.cwd', return_value=tmp_path):
                        generate_sdk.main()
                        
        install_call = mock_run.call_args_list[0]
        assert sys.executable in install_call[0][0]
        assert "pip" in install_call[0][0]
        assert "install" in install_call[0][0]
        assert "openapi-python-client" in install_call[0][0]
        
        captured = capsys.readouterr()
        assert "Installing openapi-python-client" in captured.out
        
    def test_main_install_fails(self, temp_docs_dir, tmp_path):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk")
        ]
        
        spec_file = tmp_path / "output" / "canvas_api.openapi.json"
        spec_file.parent.mkdir(parents=True)
        spec_file.write_text('{"openapi": "3.1.0"}')
        
        with patch('generate_sdk.shutil.which', return_value=None):
            with patch('generate_sdk.run_command', return_value=False):
                with patch.object(sys, 'argv', test_args):
                    with patch('generate_sdk.Path.cwd', return_value=tmp_path):
                        with pytest.raises(SystemExit) as exc_info:
                            generate_sdk.main()
                            
        assert exc_info.value.code == 1
        
    def test_main_sdk_generation_fails(self, temp_docs_dir, tmp_path):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk")
        ]
        
        spec_file = tmp_path / "output" / "canvas_api.openapi.json"
        spec_file.parent.mkdir(parents=True)
        spec_file.write_text('{"openapi": "3.1.0"}')
        
        def mock_run_command(cmd):
            if "openapi-python-client" in cmd and "generate" in cmd:
                return False
            return True
            
        with patch('generate_sdk.shutil.which', return_value="/usr/bin/openapi-python-client"):
            with patch('generate_sdk.run_command', side_effect=mock_run_command):
                with patch.object(sys, 'argv', test_args):
                    with patch('generate_sdk.Path.cwd', return_value=tmp_path):
                        with pytest.raises(SystemExit) as exc_info:
                            generate_sdk.main()
                            
        assert exc_info.value.code == 1
        
    def test_main_custom_package_name(self, temp_docs_dir, tmp_path, capsys):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk"),
            "--package-name", "custom_canvas_sdk"
        ]
        
        spec_file = tmp_path / "output" / "canvas_api.openapi.json"
        spec_file.parent.mkdir(parents=True)
        spec_file.write_text('{"openapi": "3.1.0"}')
        
        with patch('generate_sdk.shutil.which', return_value="/usr/bin/openapi-python-client"):
            with patch('generate_sdk.run_command', return_value=True):
                with patch.object(sys, 'argv', test_args):
                    with patch('generate_sdk.Path.cwd', return_value=tmp_path):
                        generate_sdk.main()
                        
        captured = capsys.readouterr()
        assert "Package: custom_canvas_sdk" in captured.out
        assert "from custom_canvas_sdk import Client" in captured.out
        
    def test_main_prints_quick_start_info(self, temp_docs_dir, tmp_path, capsys):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk")
        ]
        
        spec_file = tmp_path / "output" / "canvas_api.openapi.json"
        spec_file.parent.mkdir(parents=True)
        spec_file.write_text('{"openapi": "3.1.0"}')
        
        with patch('generate_sdk.shutil.which', return_value="/usr/bin/openapi-python-client"):
            with patch('generate_sdk.run_command', return_value=True):
                with patch.object(sys, 'argv', test_args):
                    with patch('generate_sdk.Path.cwd', return_value=tmp_path):
                        generate_sdk.main()
                        
        captured = capsys.readouterr()
        assert "Quick start:" in captured.out
        assert "Install: pip install -e" in captured.out
        assert "Import: from canvas_sdk import Client" in captured.out
        assert "Use: client = Client(base_url=" in captured.out
        
    def test_main_prints_development_info_when_pyproject_exists(self, temp_docs_dir, tmp_path, capsys):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk")
        ]
        
        spec_file = tmp_path / "output" / "canvas_api.openapi.json"
        spec_file.parent.mkdir(parents=True)
        spec_file.write_text('{"openapi": "3.1.0"}')
        
        output_dir = tmp_path / "sdk"
        output_dir.mkdir()
        (output_dir / "pyproject.toml").write_text("[project]\nname = 'test'")
        
        with patch('generate_sdk.shutil.which', return_value="/usr/bin/openapi-python-client"):
            with patch('generate_sdk.run_command', return_value=True):
                with patch.object(sys, 'argv', test_args):
                    with patch('generate_sdk.Path.cwd', return_value=tmp_path):
                        generate_sdk.main()
                        
        captured = capsys.readouterr()
        assert "Development:" in captured.out
        assert "cd " in captured.out
        assert "pip install -e ." in captured.out
        
    def test_main_prints_readme_info_when_exists(self, temp_docs_dir, tmp_path, capsys):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk")
        ]
        
        spec_file = tmp_path / "output" / "canvas_api.openapi.json"
        spec_file.parent.mkdir(parents=True)
        spec_file.write_text('{"openapi": "3.1.0"}')
        
        output_dir = tmp_path / "sdk"
        output_dir.mkdir()
        readme_path = output_dir / "README.md"
        readme_path.write_text("# SDK Documentation")
        
        with patch('generate_sdk.shutil.which', return_value="/usr/bin/openapi-python-client"):
            with patch('generate_sdk.run_command', return_value=True):
                with patch.object(sys, 'argv', test_args):
                    with patch('generate_sdk.Path.cwd', return_value=tmp_path):
                        generate_sdk.main()
                        
        captured = capsys.readouterr()
        assert f"Documentation: {readme_path}" in captured.out
        
    def test_main_handles_exception(self, temp_docs_dir, tmp_path, capsys):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk")
        ]
        
        with patch('generate_sdk.Path', side_effect=Exception("Test error")):
            with patch.object(sys, 'argv', test_args):
                with pytest.raises(SystemExit) as exc_info:
                    generate_sdk.main()
                    
        assert exc_info.value.code == 1
        
        captured = capsys.readouterr()
        assert "Error: Test error" in captured.out
        
    def test_main_handles_exception_with_verbose(self, temp_docs_dir, tmp_path):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk"),
            "--verbose"
        ]
        
        with patch('generate_sdk.Path', side_effect=Exception("Test error")):
            with patch.object(sys, 'argv', test_args):
                with patch('traceback.print_exc') as mock_traceback:
                    with pytest.raises(SystemExit) as exc_info:
                        generate_sdk.main()
                        
        assert exc_info.value.code == 1
        mock_traceback.assert_called_once()
        
    def test_main_calls_openapi_python_client_with_correct_args(self, temp_docs_dir, tmp_path):
        test_args = [
            "generate_sdk.py",
            "--docs-dir", str(temp_docs_dir),
            "--output-dir", str(tmp_path / "sdk")
        ]
        
        spec_file = tmp_path / "output" / "canvas_api.openapi.json"
        spec_file.parent.mkdir(parents=True)
        spec_file.write_text('{"openapi": "3.1.0"}')
        
        with patch('generate_sdk.shutil.which', return_value="/usr/bin/openapi-python-client"):
            with patch('generate_sdk.run_command', return_value=True) as mock_run:
                with patch.object(sys, 'argv', test_args):
                    with patch('generate_sdk.Path.cwd', return_value=tmp_path):
                        generate_sdk.main()
                        
        generate_call = mock_run.call_args_list[-1]
        cmd = generate_call[0][0]
        
        assert "openapi-python-client" in cmd
        assert "generate" in cmd
        assert "--path" in cmd
        assert "output/canvas_api.openapi.json" in cmd
        assert "--output-path" in cmd
        assert str(tmp_path / "sdk") in cmd
        assert "--overwrite" in cmd
        
    def test_argument_parser_help(self, capsys):
        test_args = ["generate_sdk.py", "--help"]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                generate_sdk.main()
                
        assert exc_info.value.code == 0
        
        captured = capsys.readouterr()
        assert "Generate Python SDK from Canvas API OpenAPI specification" in captured.out
        assert "--docs-dir" in captured.out
        assert "--output-dir" in captured.out
        assert "--package-name" in captured.out
        assert "--regenerate-spec" in captured.out
        assert "--clean" in captured.out
        assert "--verbose" in captured.out
