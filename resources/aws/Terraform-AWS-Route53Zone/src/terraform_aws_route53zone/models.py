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
    Comment: Optional[str]
    DelegationSetId: Optional[str]
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    NameServers: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    VpcId: Optional[str]
    VpcRegion: Optional[str]
    ZoneId: Optional[str]
    Vpc: Optional[Sequence["_Vpc"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Comment=json_data.get("Comment"),
            DelegationSetId=json_data.get("DelegationSetId"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NameServers=json_data.get("NameServers"),
            Tags=json_data.get("Tags"),
            VpcId=json_data.get("VpcId"),
            VpcRegion=json_data.get("VpcRegion"),
            ZoneId=json_data.get("ZoneId"),
            Vpc=json_data.get("Vpc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Vpc:
    VpcId: Optional[str]
    VpcRegion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Vpc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Vpc"]:
        if not json_data:
            return None
        return cls(
            VpcId=json_data.get("VpcId"),
            VpcRegion=json_data.get("VpcRegion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Vpc = Vpc


