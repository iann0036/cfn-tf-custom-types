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
    Destination: Optional[str]
    FicGwId: Optional[str]
    GcpGwId: Optional[str]
    Id: Optional[str]
    InterdcGwId: Optional[str]
    InternetGwId: Optional[str]
    Name: Optional[str]
    Nexthop: Optional[str]
    Region: Optional[str]
    ServiceType: Optional[str]
    TenantId: Optional[str]
    VpnGwId: Optional[str]
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
            Destination=json_data.get("Destination"),
            FicGwId=json_data.get("FicGwId"),
            GcpGwId=json_data.get("GcpGwId"),
            Id=json_data.get("Id"),
            InterdcGwId=json_data.get("InterdcGwId"),
            InternetGwId=json_data.get("InternetGwId"),
            Name=json_data.get("Name"),
            Nexthop=json_data.get("Nexthop"),
            Region=json_data.get("Region"),
            ServiceType=json_data.get("ServiceType"),
            TenantId=json_data.get("TenantId"),
            VpnGwId=json_data.get("VpnGwId"),
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


