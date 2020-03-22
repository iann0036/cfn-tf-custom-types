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
    Accessor: Optional[str]
    DefaultLeaseTtlSeconds: Optional[float]
    Description: Optional[str]
    Id: Optional[str]
    Local: Optional[bool]
    MaxLeaseTtlSeconds: Optional[float]
    Options: Optional[Sequence["_Options"]]
    Path: Optional[str]
    SealWrap: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Accessor=json_data.get("Accessor"),
            DefaultLeaseTtlSeconds=json_data.get("DefaultLeaseTtlSeconds"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Local=json_data.get("Local"),
            MaxLeaseTtlSeconds=json_data.get("MaxLeaseTtlSeconds"),
            Options=json_data.get("Options"),
            Path=json_data.get("Path"),
            SealWrap=json_data.get("SealWrap"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Options:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Options"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Options"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Options = Options


