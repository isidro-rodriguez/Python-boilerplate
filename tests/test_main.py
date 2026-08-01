from _pytest.capture import CaptureFixture

from python_boilerplate.main import main


def test_main_output(capsys: CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert "¡Boilerplate listo y funcionando!" in captured.out
