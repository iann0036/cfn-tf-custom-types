# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    AdminEnabled: Optional[bool]
    Bandwidth: Optional[str]
    CandidateSubnets: Optional[Sequence[str]]
    CloudRouterIpAddress: Optional[str]
    CreationTimestamp: Optional[str]
    CustomerRouterIpAddress: Optional[str]
    Description: Optional[str]
    EdgeAvailabilityDomain: Optional[str]
    Encryption: Optional[str]
    GoogleReferenceId: Optional[str]
    Id: Optional[str]
    Interconnect: Optional[str]
    IpsecInternalAddresses: Optional[Sequence[str]]
    Mtu: Optional[str]
    Name: Optional[str]
    PairingKey: Optional[str]
    PartnerAsn: Optional[str]
    PrivateInterconnectInfo: Optional[Sequence["_PrivateInterconnectInfoDefinition"]]
    Project: Optional[str]
    Region: Optional[str]
    Router: Optional[str]
    SelfLink: Optional[str]
    State: Optional[str]
    Type: Optional[str]
    VlanTag8021q: Optional[float]
    Timeouts: Optional["_TimeoutsDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
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
            Encryption=json_data.get("Encryption"),
            GoogleReferenceId=json_data.get("GoogleReferenceId"),
            Id=json_data.get("Id"),
            Interconnect=json_data.get("Interconnect"),
            IpsecInternalAddresses=json_data.get("IpsecInternalAddresses"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            PairingKey=json_data.get("PairingKey"),
            PartnerAsn=json_data.get("PartnerAsn"),
            PrivateInterconnectInfo=deserialize_list(json_data.get("PrivateInterconnectInfo"), PrivateInterconnectInfoDefinition),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Router=json_data.get("Router"),
            SelfLink=json_data.get("SelfLink"),
            State=json_data.get("State"),
            Type=json_data.get("Type"),
            VlanTag8021q=json_data.get("VlanTag8021q"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PrivateInterconnectInfoDefinition(BaseModel):
    Tag8021q: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateInterconnectInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateInterconnectInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Tag8021q=json_data.get("Tag8021q"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateInterconnectInfoDefinition = PrivateInterconnectInfoDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


