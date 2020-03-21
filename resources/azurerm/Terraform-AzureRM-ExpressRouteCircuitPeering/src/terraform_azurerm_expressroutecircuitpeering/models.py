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
    AzureAsn: Optional[float]
    ExpressRouteCircuitName: Optional[str]
    PeerAsn: Optional[float]
    PeeringType: Optional[str]
    PrimaryAzurePort: Optional[str]
    PrimaryPeerAddressPrefix: Optional[str]
    ResourceGroupName: Optional[str]
    SecondaryAzurePort: Optional[str]
    SecondaryPeerAddressPrefix: Optional[str]
    SharedKey: Optional[str]
    VlanId: Optional[float]
    MicrosoftPeeringConfig: Optional[Sequence["_MicrosoftPeeringConfig"]]
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
            AzureAsn=json_data.get("AzureAsn"),
            ExpressRouteCircuitName=json_data.get("ExpressRouteCircuitName"),
            PeerAsn=json_data.get("PeerAsn"),
            PeeringType=json_data.get("PeeringType"),
            PrimaryAzurePort=json_data.get("PrimaryAzurePort"),
            PrimaryPeerAddressPrefix=json_data.get("PrimaryPeerAddressPrefix"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryAzurePort=json_data.get("SecondaryAzurePort"),
            SecondaryPeerAddressPrefix=json_data.get("SecondaryPeerAddressPrefix"),
            SharedKey=json_data.get("SharedKey"),
            VlanId=json_data.get("VlanId"),
            MicrosoftPeeringConfig=json_data.get("MicrosoftPeeringConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MicrosoftPeeringConfig:
    AdvertisedPublicPrefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MicrosoftPeeringConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MicrosoftPeeringConfig"]:
        if not json_data:
            return None
        return cls(
            AdvertisedPublicPrefixes=json_data.get("AdvertisedPublicPrefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MicrosoftPeeringConfig = MicrosoftPeeringConfig


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


