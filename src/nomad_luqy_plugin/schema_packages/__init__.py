from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field  # type: ignore


class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_luqy_plugin.schema_packages.schema_package import (  # noqa: PLC0415
            m_package,  # noqa: PLC0415
        )

        return m_package


schema_package_entry_point = NewSchemaPackageEntryPoint(
    name='NewSchemaPackage',
    description='New schema package entry point configuration.',
)
