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
    AwsGwId: Optional[str]
    AzureGwId: Optional[str]
    Description: Optional[str]
    FicGwId: Optional[str]
    GcpGwId: Optional[str]
    GwVipv4: Optional[str]
    GwVipv6: Optional[str]
    Id: Optional[str]
    InterdcGwId: Optional[str]
    InternetGwId: Optional[str]
    Name: Optional[str]
    Netmask: Optional[float]
    NetworkId: Optional[str]
    PrimaryIpv4: Optional[str]
    PrimaryIpv6: Optional[str]
    Region: Optional[str]
    SecondaryIpv4: Optional[str]
    SecondaryIpv6: Optional[str]
    ServiceType: Optional[str]
    TenantId: Optional[str]
    VpnGwId: Optional[str]
    Vrid: Optional[float]
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
            AwsGwId=json_data.get("AwsGwId"),
            AzureGwId=json_data.get("AzureGwId"),
            Description=json_data.get("Description"),
            FicGwId=json_data.get("FicGwId"),
            GcpGwId=json_data.get("GcpGwId"),
            GwVipv4=json_data.get("GwVipv4"),
            GwVipv6=json_data.get("GwVipv6"),
            Id=json_data.get("Id"),
            InterdcGwId=json_data.get("InterdcGwId"),
            InternetGwId=json_data.get("InternetGwId"),
            Name=json_data.get("Name"),
            Netmask=json_data.get("Netmask"),
            NetworkId=json_data.get("NetworkId"),
            PrimaryIpv4=json_data.get("PrimaryIpv4"),
            PrimaryIpv6=json_data.get("PrimaryIpv6"),
            Region=json_data.get("Region"),
            SecondaryIpv4=json_data.get("SecondaryIpv4"),
            SecondaryIpv6=json_data.get("SecondaryIpv6"),
            ServiceType=json_data.get("ServiceType"),
            TenantId=json_data.get("TenantId"),
            VpnGwId=json_data.get("VpnGwId"),
            Vrid=json_data.get("Vrid"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


