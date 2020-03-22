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
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    LogicalRouterId: Optional[str]
    Network: Optional[str]
    Revision: Optional[float]
    NextHop: Optional[Sequence["_NextHop"]]
    Tag: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            LogicalRouterId=json_data.get("LogicalRouterId"),
            Network=json_data.get("Network"),
            Revision=json_data.get("Revision"),
            NextHop=json_data.get("NextHop"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NextHop:
    AdministrativeDistance: Optional[float]
    IpAddress: Optional[str]
    LogicalRouterPortId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NextHop"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NextHop"]:
        if not json_data:
            return None
        return cls(
            AdministrativeDistance=json_data.get("AdministrativeDistance"),
            IpAddress=json_data.get("IpAddress"),
            LogicalRouterPortId=json_data.get("LogicalRouterPortId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NextHop = NextHop


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


