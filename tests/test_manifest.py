from typing import Any

from invoco.core.registry.registry import registry


def test_manifest_includes_echo() -> None:
    """
    Test that the task manifest includes the Echo task with correct metadata.

    Verifies:
    - "echo" entry exists in manifest.
    - Basic fields (`name`, `description`, `available`) are set.
    - Metadata fields (`schema`, `version`, `tags`) are present.
    """
    manifest: dict[str, dict[str, Any]] = registry.manifest()
    assert "echo" in manifest

    echo_entry: dict[str, Any] = manifest["echo"]

    assert echo_entry["name"] == "echo"
    assert echo_entry["description"] == "Echo back input text."
    assert echo_entry["available"] is True

    # Metadata from @task_metadata decorator
    assert "schema" in echo_entry
    assert echo_entry["version"] == "1.0"
    assert "utility" in echo_entry["tags"]
    assert "demo" in echo_entry["tags"]
