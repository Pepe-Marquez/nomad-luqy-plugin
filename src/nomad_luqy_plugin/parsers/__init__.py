from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field  # type: ignore


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_luqy_plugin.parsers.parser import NewParser  # noqa: PLC0415

        return NewParser(**self.dict())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re='.*\.newmainfilename',
)
