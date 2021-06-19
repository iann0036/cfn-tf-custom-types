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
    AccountId: Optional[str]
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    AssociatePublicIpAddress: Optional[bool]
    ClientId: Optional[str]
    Company: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    NetworkSecurityGroupName: Optional[str]
    NetworkSecurityResourceGroup: Optional[str]
    ProxyCertificates: Optional[Sequence[str]]
    ProxyPassword: Optional[str]
    ProxyUrl: Optional[str]
    ProxyUserName: Optional[str]
    ResourceGroup: Optional[str]
    SubnetId: Optional[str]
    SubscriptionId: Optional[str]
    VirtualMachineSize: Optional[str]
    VnetId: Optional[str]
    VnetResourceGroup: Optional[str]

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
            AccountId=json_data.get("AccountId"),
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            ClientId=json_data.get("ClientId"),
            Company=json_data.get("Company"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NetworkSecurityGroupName=json_data.get("NetworkSecurityGroupName"),
            NetworkSecurityResourceGroup=json_data.get("NetworkSecurityResourceGroup"),
            ProxyCertificates=json_data.get("ProxyCertificates"),
            ProxyPassword=json_data.get("ProxyPassword"),
            ProxyUrl=json_data.get("ProxyUrl"),
            ProxyUserName=json_data.get("ProxyUserName"),
            ResourceGroup=json_data.get("ResourceGroup"),
            SubnetId=json_data.get("SubnetId"),
            SubscriptionId=json_data.get("SubscriptionId"),
            VirtualMachineSize=json_data.get("VirtualMachineSize"),
            VnetId=json_data.get("VnetId"),
            VnetResourceGroup=json_data.get("VnetResourceGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


