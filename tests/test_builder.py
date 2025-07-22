import pytest
from infinit.core.builder import build

def test_builder(tmp_path):
    project_path = tmp_path / "myproj"

    build(project_path, folders="loot,scans,exploits", files="scans/README.md:# Findings")

    assert project_path.exists()
    assert (project_path / "scans").exists()
    assert (project_path / "loot").exists()
    assert (project_path / "exploits").exists()
    readme_path = project_path / "scans" / "README.md"
    assert readme_path.exists()
    assert "# Findings" in readme_path.read_text()

def test_builder_with_missing_dir(tmp_path):
    project_path = tmp_path / "myproj"

    build(project_path, folders="loot,scans,exploits", files="missing_dir/README.md:# Findings")

    assert project_path.exists()
    assert (project_path / "scans").exists()
    assert (project_path / "loot").exists()
    assert (project_path / "exploits").exists()
    readme_path = project_path / "missing_dir" / "README.md"
    assert readme_path.exists()
    assert "# Findings" in readme_path.read_text()


def test_invalid_file_syntax():
    with pytest.raises(ValueError):
        build("badproj", files="file_without_colon")
        
