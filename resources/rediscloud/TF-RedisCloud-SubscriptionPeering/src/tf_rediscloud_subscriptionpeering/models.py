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
    AwsAccountId: Optional[str]
    AwsPeeringId: Optional[str]
    GcpNetworkName: Optional[str]
    GcpPeeringId: Optional[str]
    GcpProjectId: Optional[str]
    GcpRedisNetworkName: Optional[str]
    GcpRedisProjectId: Optional[str]
    Id: Optional[str]
    ProviderName: Optional[str]
    Region: Optional[str]
    Status: Optional[str]
    SubscriptionId: Optional[str]
    VpcCidr: Optional[str]
    VpcId: Optional[str]
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
            AwsAccountId=json_data.get("AwsAccountId"),
            AwsPeeringId=json_data.get("AwsPeeringId"),
            GcpNetworkName=json_data.get("GcpNetworkName"),
            GcpPeeringId=json_data.get("GcpPeeringId"),
            GcpProjectId=json_data.get("GcpProjectId"),
            GcpRedisNetworkName=json_data.get("GcpRedisNetworkName"),
            GcpRedisProjectId=json_data.get("GcpRedisProjectId"),
            Id=json_data.get("Id"),
            ProviderName=json_data.get("ProviderName"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            SubscriptionId=json_data.get("SubscriptionId"),
            VpcCidr=json_data.get("VpcCidr"),
            VpcId=json_data.get("VpcId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


