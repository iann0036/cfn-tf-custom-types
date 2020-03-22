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
    Id: Optional[str]
    JumpStart: Optional[bool]
    Meta: Optional[Sequence["_Meta"]]
    NameServers: Optional[Sequence[str]]
    Paused: Optional[bool]
    Plan: Optional[str]
    Status: Optional[str]
    Type: Optional[str]
    VanityNameServers: Optional[Sequence[str]]
    VerificationKey: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            JumpStart=json_data.get("JumpStart"),
            Meta=json_data.get("Meta"),
            NameServers=json_data.get("NameServers"),
            Paused=json_data.get("Paused"),
            Plan=json_data.get("Plan"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            VanityNameServers=json_data.get("VanityNameServers"),
            VerificationKey=json_data.get("VerificationKey"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Meta:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Meta"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Meta"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Meta = Meta


