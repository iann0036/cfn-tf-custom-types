# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Excludes: Optional[Sequence[str]]
    Id: Optional[str]
    OutputBase64sha256: Optional[str]
    OutputFileMode: Optional[str]
    OutputMd5: Optional[str]
    OutputPath: Optional[str]
    OutputSha: Optional[str]
    OutputSize: Optional[float]
    SourceContent: Optional[str]
    SourceContentFilename: Optional[str]
    SourceDir: Optional[str]
    SourceFile: Optional[str]
    Type: Optional[str]
    Source: Optional[Sequence["_SourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Excludes=json_data.get("Excludes"),
            Id=json_data.get("Id"),
            OutputBase64sha256=json_data.get("OutputBase64sha256"),
            OutputFileMode=json_data.get("OutputFileMode"),
            OutputMd5=json_data.get("OutputMd5"),
            OutputPath=json_data.get("OutputPath"),
            OutputSha=json_data.get("OutputSha"),
            OutputSize=json_data.get("OutputSize"),
            SourceContent=json_data.get("SourceContent"),
            SourceContentFilename=json_data.get("SourceContentFilename"),
            SourceDir=json_data.get("SourceDir"),
            SourceFile=json_data.get("SourceFile"),
            Type=json_data.get("Type"),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SourceDefinition(BaseModel):
    Content: Optional[str]
    Filename: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Filename=json_data.get("Filename"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


