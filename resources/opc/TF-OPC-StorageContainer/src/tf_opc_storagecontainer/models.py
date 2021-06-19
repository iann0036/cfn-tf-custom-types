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
    AllowedOrigins: Optional[Sequence[str]]
    ExposedHeaders: Optional[Sequence[str]]
    Id: Optional[str]
    MaxAge: Optional[float]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    PrimaryKey: Optional[str]
    QuotaBytes: Optional[float]
    QuotaCount: Optional[float]
    ReadAcls: Optional[Sequence[str]]
    SecondaryKey: Optional[str]
    WriteAcls: Optional[Sequence[str]]

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
            AllowedOrigins=json_data.get("AllowedOrigins"),
            ExposedHeaders=json_data.get("ExposedHeaders"),
            Id=json_data.get("Id"),
            MaxAge=json_data.get("MaxAge"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            PrimaryKey=json_data.get("PrimaryKey"),
            QuotaBytes=json_data.get("QuotaBytes"),
            QuotaCount=json_data.get("QuotaCount"),
            ReadAcls=json_data.get("ReadAcls"),
            SecondaryKey=json_data.get("SecondaryKey"),
            WriteAcls=json_data.get("WriteAcls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


