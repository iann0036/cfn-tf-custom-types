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
    AssociatePublicIp: Optional[bool]
    ClientId: Optional[str]
    Company: Optional[str]
    FirewallTags: Optional[bool]
    Id: Optional[str]
    MachineType: Optional[str]
    Name: Optional[str]
    NetworkProjectId: Optional[str]
    ProjectId: Optional[str]
    ProxyCertificates: Optional[Sequence[str]]
    ProxyPassword: Optional[str]
    ProxyUrl: Optional[str]
    ProxyUserName: Optional[str]
    ServiceAccountEmail: Optional[str]
    ServiceAccountPath: Optional[str]
    SubnetId: Optional[str]
    Zone: Optional[str]

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
            AssociatePublicIp=json_data.get("AssociatePublicIp"),
            ClientId=json_data.get("ClientId"),
            Company=json_data.get("Company"),
            FirewallTags=json_data.get("FirewallTags"),
            Id=json_data.get("Id"),
            MachineType=json_data.get("MachineType"),
            Name=json_data.get("Name"),
            NetworkProjectId=json_data.get("NetworkProjectId"),
            ProjectId=json_data.get("ProjectId"),
            ProxyCertificates=json_data.get("ProxyCertificates"),
            ProxyPassword=json_data.get("ProxyPassword"),
            ProxyUrl=json_data.get("ProxyUrl"),
            ProxyUserName=json_data.get("ProxyUserName"),
            ServiceAccountEmail=json_data.get("ServiceAccountEmail"),
            ServiceAccountPath=json_data.get("ServiceAccountPath"),
            SubnetId=json_data.get("SubnetId"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


