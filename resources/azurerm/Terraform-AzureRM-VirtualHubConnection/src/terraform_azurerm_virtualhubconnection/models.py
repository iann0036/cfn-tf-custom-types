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
    HubToVitualNetworkTrafficAllowed: Optional[bool]
    Id: Optional[str]
    InternetSecurityEnabled: Optional[bool]
    Name: Optional[str]
    RemoteVirtualNetworkId: Optional[str]
    VirtualHubId: Optional[str]
    VitualNetworkToHubGatewaysTrafficAllowed: Optional[bool]
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
            HubToVitualNetworkTrafficAllowed=json_data.get("HubToVitualNetworkTrafficAllowed"),
            Id=json_data.get("Id"),
            InternetSecurityEnabled=json_data.get("InternetSecurityEnabled"),
            Name=json_data.get("Name"),
            RemoteVirtualNetworkId=json_data.get("RemoteVirtualNetworkId"),
            VirtualHubId=json_data.get("VirtualHubId"),
            VitualNetworkToHubGatewaysTrafficAllowed=json_data.get("VitualNetworkToHubGatewaysTrafficAllowed"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


