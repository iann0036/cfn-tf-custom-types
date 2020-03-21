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
    CreatedOn: Optional[str]
    Data: Optional[Sequence["_Data"]]
    Hostname: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    ModifiedOn: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    Proxiable: Optional[bool]
    Proxied: Optional[bool]
    Ttl: Optional[float]
    Type: Optional[str]
    Value: Optional[str]
    ZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreatedOn=json_data.get("CreatedOn"),
            Data=json_data.get("Data"),
            Hostname=json_data.get("Hostname"),
            Metadata=json_data.get("Metadata"),
            ModifiedOn=json_data.get("ModifiedOn"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Proxiable=json_data.get("Proxiable"),
            Proxied=json_data.get("Proxied"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
            ZoneId=json_data.get("ZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Data:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Data"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Data"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Data = Data


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


