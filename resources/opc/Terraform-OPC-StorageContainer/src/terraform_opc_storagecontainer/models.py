# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    AllowedOrigins: Optional[Sequence[str]]
    ExposedHeaders: Optional[Sequence[str]]
    Id: Optional[str]
    MaxAge: Optional[float]
    Metadata: Optional[Sequence["_Metadata"]]
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
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            ExposedHeaders=json_data.get("ExposedHeaders"),
            Id=json_data.get("Id"),
            MaxAge=json_data.get("MaxAge"),
            Metadata=json_data.get("Metadata"),
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
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


