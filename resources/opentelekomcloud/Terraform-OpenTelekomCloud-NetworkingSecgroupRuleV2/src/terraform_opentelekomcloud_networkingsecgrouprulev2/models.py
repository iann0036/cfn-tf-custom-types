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
    Direction: Optional[str]
    Ethertype: Optional[str]
    Id: Optional[str]
    PortRangeMax: Optional[float]
    PortRangeMin: Optional[float]
    Protocol: Optional[str]
    Region: Optional[str]
    RemoteGroupId: Optional[str]
    RemoteIpPrefix: Optional[str]
    SecurityGroupId: Optional[str]
    TenantId: Optional[str]
    Timeouts: Optional["_Timeouts"]

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
            Direction=json_data.get("Direction"),
            Ethertype=json_data.get("Ethertype"),
            Id=json_data.get("Id"),
            PortRangeMax=json_data.get("PortRangeMax"),
            PortRangeMin=json_data.get("PortRangeMin"),
            Protocol=json_data.get("Protocol"),
            Region=json_data.get("Region"),
            RemoteGroupId=json_data.get("RemoteGroupId"),
            RemoteIpPrefix=json_data.get("RemoteIpPrefix"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            TenantId=json_data.get("TenantId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


