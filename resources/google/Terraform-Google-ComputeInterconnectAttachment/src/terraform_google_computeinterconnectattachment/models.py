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
    AdminEnabled: Optional[bool]
    Bandwidth: Optional[str]
    CandidateSubnets: Optional[Sequence[str]]
    CloudRouterIpAddress: Optional[str]
    CreationTimestamp: Optional[str]
    CustomerRouterIpAddress: Optional[str]
    Description: Optional[str]
    EdgeAvailabilityDomain: Optional[str]
    GoogleReferenceId: Optional[str]
    Id: Optional[str]
    Interconnect: Optional[str]
    Name: Optional[str]
    PairingKey: Optional[str]
    PartnerAsn: Optional[str]
    PrivateInterconnectInfo: Optional[Sequence["_PrivateInterconnectInfo"]]
    Project: Optional[str]
    Region: Optional[str]
    Router: Optional[str]
    SelfLink: Optional[str]
    State: Optional[str]
    Type: Optional[str]
    VlanTag8021q: Optional[float]
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
            AdminEnabled=json_data.get("AdminEnabled"),
            Bandwidth=json_data.get("Bandwidth"),
            CandidateSubnets=json_data.get("CandidateSubnets"),
            CloudRouterIpAddress=json_data.get("CloudRouterIpAddress"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            CustomerRouterIpAddress=json_data.get("CustomerRouterIpAddress"),
            Description=json_data.get("Description"),
            EdgeAvailabilityDomain=json_data.get("EdgeAvailabilityDomain"),
            GoogleReferenceId=json_data.get("GoogleReferenceId"),
            Id=json_data.get("Id"),
            Interconnect=json_data.get("Interconnect"),
            Name=json_data.get("Name"),
            PairingKey=json_data.get("PairingKey"),
            PartnerAsn=json_data.get("PartnerAsn"),
            PrivateInterconnectInfo=json_data.get("PrivateInterconnectInfo"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Router=json_data.get("Router"),
            SelfLink=json_data.get("SelfLink"),
            State=json_data.get("State"),
            Type=json_data.get("Type"),
            VlanTag8021q=json_data.get("VlanTag8021q"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PrivateInterconnectInfo:
    Tag8021q: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateInterconnectInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateInterconnectInfo"]:
        if not json_data:
            return None
        return cls(
            Tag8021q=json_data.get("Tag8021q"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateInterconnectInfo = PrivateInterconnectInfo


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


