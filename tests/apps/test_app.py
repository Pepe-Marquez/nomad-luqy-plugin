def test_importing_app():
    # this will raise an exception if pydantic model validation fails for th app
    from nomad_luqy_plugin.apps import app_entry_point  # type: ignore # noqa: PLC0415

    assert app_entry_point.app.label == 'Absolute Luminescence'
