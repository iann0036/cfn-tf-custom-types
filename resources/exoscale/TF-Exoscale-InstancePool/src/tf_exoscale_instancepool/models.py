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
    AffinityGroupIds: Optional[Sequence[str]]
    DeployTargetId: Optional[str]
    Description: Optional[str]
    DiskSize: Optional[float]
    ElasticIpIds: Optional[Sequence[str]]
    Id: Optional[str]
    InstancePrefix: Optional[str]
    Ipv6: Optional[bool]
    KeyPair: Optional[str]
    Name: Optional[str]
    NetworkIds: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]
    ServiceOffering: Optional[str]
    Size: Optional[float]
    State: Optional[str]
    TemplateId: Optional[str]
    UserData: Optional[str]
    VirtualMachines: Optional[Sequence[str]]
    Zone: Optional[str]
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
            AffinityGroupIds=json_data.get("AffinityGroupIds"),
            DeployTargetId=json_data.get("DeployTargetId"),
            Description=json_data.get("Description"),
            DiskSize=json_data.get("DiskSize"),
            ElasticIpIds=json_data.get("ElasticIpIds"),
            Id=json_data.get("Id"),
            InstancePrefix=json_data.get("InstancePrefix"),
            Ipv6=json_data.get("Ipv6"),
            KeyPair=json_data.get("KeyPair"),
            Name=json_data.get("Name"),
            NetworkIds=json_data.get("NetworkIds"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            ServiceOffering=json_data.get("ServiceOffering"),
            Size=json_data.get("Size"),
            State=json_data.get("State"),
            TemplateId=json_data.get("TemplateId"),
            UserData=json_data.get("UserData"),
            VirtualMachines=json_data.get("VirtualMachines"),
            Zone=json_data.get("Zone"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


