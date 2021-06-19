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
    BufferInterval: Optional[float]
    BufferSize: Optional[float]
    CompressType: Optional[str]
    CsvConfigColumns: Optional[Sequence[str]]
    CsvConfigDelimiter: Optional[str]
    CsvConfigHeader: Optional[bool]
    CsvConfigLinefeed: Optional[str]
    CsvConfigNullidentifier: Optional[str]
    CsvConfigQuote: Optional[str]
    Format: Optional[str]
    Id: Optional[str]
    JsonEnableTag: Optional[bool]
    LogstoreName: Optional[str]
    OssBucket: Optional[str]
    OssPrefix: Optional[str]
    PathFormat: Optional[str]
    ProjectName: Optional[str]
    RoleArn: Optional[str]
    ShipperName: Optional[str]
    ParquetConfig: Optional[Sequence["_ParquetConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            BufferInterval=json_data.get("BufferInterval"),
            BufferSize=json_data.get("BufferSize"),
            CompressType=json_data.get("CompressType"),
            CsvConfigColumns=json_data.get("CsvConfigColumns"),
            CsvConfigDelimiter=json_data.get("CsvConfigDelimiter"),
            CsvConfigHeader=json_data.get("CsvConfigHeader"),
            CsvConfigLinefeed=json_data.get("CsvConfigLinefeed"),
            CsvConfigNullidentifier=json_data.get("CsvConfigNullidentifier"),
            CsvConfigQuote=json_data.get("CsvConfigQuote"),
            Format=json_data.get("Format"),
            Id=json_data.get("Id"),
            JsonEnableTag=json_data.get("JsonEnableTag"),
            LogstoreName=json_data.get("LogstoreName"),
            OssBucket=json_data.get("OssBucket"),
            OssPrefix=json_data.get("OssPrefix"),
            PathFormat=json_data.get("PathFormat"),
            ProjectName=json_data.get("ProjectName"),
            RoleArn=json_data.get("RoleArn"),
            ShipperName=json_data.get("ShipperName"),
            ParquetConfig=deserialize_list(json_data.get("ParquetConfig"), ParquetConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ParquetConfigDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParquetConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParquetConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParquetConfigDefinition = ParquetConfigDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


