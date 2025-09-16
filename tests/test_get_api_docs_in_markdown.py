import hashlib
from pathlib import Path
from unittest.mock import patch, Mock
import pytest
import requests
import requests_mock
from get_api_docs_in_markdown import (
    fetch_text, extract_md_links, identical, download_resources, main,
    INDEX_URL, BASE_URL, TIMEOUT
)


class TestFetchText:
    
    def test_fetch_text_success(self, requests_mock):
        url = "https://example.com/test.md"
        expected_content = "# Test Content\n\nThis is a test."
        requests_mock.get(url, text=expected_content)
        
        result = fetch_text(url)
        
        assert result == expected_content
        assert requests_mock.last_request.timeout == TIMEOUT
    
    def test_fetch_text_http_error(self, requests_mock):
        url = "https://example.com/notfound.md"
        requests_mock.get(url, status_code=404)
        
        with pytest.raises(requests.HTTPError):
            fetch_text(url)
    
    def test_fetch_text_timeout(self, requests_mock):
        url = "https://example.com/slow.md"
        requests_mock.get(url, exc=requests.Timeout)
        
        with pytest.raises(requests.Timeout):
            fetch_text(url)


class TestExtractMdLinks:
    
    def test_extract_md_links_markdown_format(self):
        md_content = """
        # API Documentation
        
        See [Courses API](courses.md) and [Users API](users.md) for details.
        Also check [Assignments](assignments.md).
        """
        base_url = "https://example.com/"
        
        result = extract_md_links(md_content, base_url)
        
        expected = {
            "courses.md": "https://example.com/courses.md",
            "users.md": "https://example.com/users.md", 
            "assignments.md": "https://example.com/assignments.md"
        }
        assert result == expected
    
    def test_extract_md_links_html_format(self):
        md_content = """
        <p>Check out these APIs:</p>
        <a href="courses.md">Courses</a>
        <a href="users.md">Users</a>
        <a href="https://external.com/other.md">External</a>
        """
        base_url = "https://example.com/"
        
        result = extract_md_links(md_content, base_url)
        
        expected = {
            "courses.md": "https://example.com/courses.md",
            "users.md": "https://example.com/users.md",
            "other.md": "https://external.com/other.md"
        }
        assert result == expected
    
    def test_extract_md_links_mixed_format(self):
        md_content = """
        # Mixed Format
        
        [Markdown link](courses.md)
        <a href="users.md">HTML link</a>
        [Another markdown](assignments.md)
        """
        base_url = "https://example.com/"
        
        result = extract_md_links(md_content, base_url)
        
        expected = {
            "courses.md": "https://example.com/courses.md",
            "users.md": "https://example.com/users.md",
            "assignments.md": "https://example.com/assignments.md"
        }
        assert result == expected
    
    def test_extract_md_links_no_links(self):
        md_content = """
        # No Links Here
        
        Just some regular content without any markdown links.
        """
        base_url = "https://example.com/"
        
        result = extract_md_links(md_content, base_url)
        
        assert result == {}
    
    def test_extract_md_links_relative_paths(self):
        md_content = """
        [Relative](../api/courses.md)
        [Subdirectory](resources/users.md)
        """
        base_url = "https://example.com/docs/"
        
        result = extract_md_links(md_content, base_url)
        
        expected = {
            "courses.md": "https://example.com/api/courses.md",
            "users.md": "https://example.com/docs/resources/users.md"
        }
        assert result == expected


class TestIdentical:
    
    def test_identical_file_not_exists(self, tmp_path):
        non_existent_file = tmp_path / "nonexistent.md"
        new_bytes = b"test content"
        
        result = identical(non_existent_file, new_bytes)
        
        assert result is False
    
    def test_identical_same_content(self, tmp_path):
        test_file = tmp_path / "test.md"
        content = b"test content"
        test_file.write_bytes(content)
        
        result = identical(test_file, content)
        
        assert result is True
    
    def test_identical_different_content(self, tmp_path):
        test_file = tmp_path / "test.md"
        original_content = b"original content"
        new_content = b"new content"
        test_file.write_bytes(original_content)
        
        result = identical(test_file, new_content)
        
        assert result is False
    
    def test_identical_empty_files(self, tmp_path):
        test_file = tmp_path / "empty.md"
        empty_content = b""
        test_file.write_bytes(empty_content)
        
        result = identical(test_file, empty_content)
        
        assert result is True


class TestDownloadResources:
    
    def test_download_resources_new_files(self, tmp_path, requests_mock):
        link_map = {
            "courses.md": "https://example.com/courses.md",
            "users.md": "https://example.com/users.md"
        }
        
        requests_mock.get("https://example.com/courses.md", text="Courses content")
        requests_mock.get("https://example.com/users.md", text="Users content")
        
        download_resources(link_map, tmp_path)
        
        courses_file = tmp_path / "courses.md"
        users_file = tmp_path / "users.md"
        
        assert courses_file.exists()
        assert users_file.exists()
        assert courses_file.read_text() == "Courses content"
        assert users_file.read_text() == "Users content"
    
    def test_download_resources_unchanged_files(self, tmp_path, requests_mock):
        link_map = {
            "courses.md": "https://example.com/courses.md"
        }
        
        existing_content = "Existing courses content"
        courses_file = tmp_path / "courses.md"
        courses_file.write_text(existing_content)
        
        requests_mock.get("https://example.com/courses.md", text=existing_content)
        
        with patch('get_api_docs_in_markdown.logging') as mock_logging:
            download_resources(link_map, tmp_path)
            
        mock_logging.debug.assert_called_with("Unchanged: %s", "courses.md")
    
    def test_download_resources_updated_files(self, tmp_path, requests_mock):
        link_map = {
            "courses.md": "https://example.com/courses.md"
        }
        
        old_content = "Old courses content"
        new_content = "New courses content"
        courses_file = tmp_path / "courses.md"
        courses_file.write_text(old_content)
        
        requests_mock.get("https://example.com/courses.md", text=new_content)
        
        download_resources(link_map, tmp_path)
        
        assert courses_file.read_text() == new_content
    
    def test_download_resources_http_error(self, tmp_path, requests_mock):
        link_map = {
            "courses.md": "https://example.com/courses.md"
        }
        
        requests_mock.get("https://example.com/courses.md", status_code=404)
        
        with pytest.raises(requests.HTTPError):
            download_resources(link_map, tmp_path)
    
    def test_download_resources_creates_directory(self, tmp_path, requests_mock):
        nested_dir = tmp_path / "nested" / "directory"
        link_map = {
            "test.md": "https://example.com/test.md"
        }
        
        requests_mock.get("https://example.com/test.md", text="test content")
        
        download_resources(link_map, nested_dir)
        
        assert nested_dir.exists()
        assert (nested_dir / "test.md").exists()


class TestMain:
    
    @patch('get_api_docs_in_markdown.download_resources')
    @patch('get_api_docs_in_markdown.extract_md_links')
    @patch('get_api_docs_in_markdown.fetch_text')
    @patch('get_api_docs_in_markdown.logging')
    def test_main_success(self, mock_logging, mock_fetch, mock_extract, mock_download):
        mock_fetch.return_value = "# Index content"
        mock_extract.return_value = {
            "courses.md": "https://example.com/courses.md",
            "users.md": "https://example.com/users.md"
        }
        
        main()
        
        mock_fetch.assert_called_once_with(INDEX_URL)
        mock_extract.assert_called_once_with("# Index content", BASE_URL)
        mock_download.assert_called_once()
        
        mock_logging.info.assert_any_call("Fetching index: %s", INDEX_URL)
        mock_logging.info.assert_any_call("Found %d markdown resources", 2)
    
    @patch('get_api_docs_in_markdown.download_resources')
    @patch('get_api_docs_in_markdown.extract_md_links')
    @patch('get_api_docs_in_markdown.fetch_text')
    def test_main_no_links_found(self, mock_fetch, mock_extract, mock_download):
        mock_fetch.return_value = "# Index with no links"
        mock_extract.return_value = {}
        
        main()
        
        mock_download.assert_called_once_with({}, Path(__file__).parent.parent / "data" / "canvas_api_resources")
    
    @patch('get_api_docs_in_markdown.fetch_text')
    def test_main_fetch_error(self, mock_fetch):
        mock_fetch.side_effect = requests.HTTPError("404 Not Found")
        
        with pytest.raises(requests.HTTPError):
            main()


class TestConstants:
    
    def test_constants_defined(self):
        assert INDEX_URL == "https://developerdocs.instructure.com/services/canvas/resources.md"
        assert BASE_URL == "https://developerdocs.instructure.com/services/canvas/"
        assert TIMEOUT == 10
        assert isinstance(Path(__file__).parent.parent / "data" / "canvas_api_resources", Path)
