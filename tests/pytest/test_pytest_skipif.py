import pytest

SYSTEM_VERSION = "1.0.0"

@pytest.mark.skipif(
    SYSTEM_VERSION=="1.1.0",
    reason="Тест не может быть запущен на версии системы 1.1.0"
)

def test_system_version_valid():
    ...

@pytest.mark.skipif(
    SYSTEM_VERSION=="1.0.0",
    reason="Тест не может быть запущен на версии системы 1.0.0"
)
def test_system_version_invalid():
    ...