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
    AnalyticsInstanceId: Optional[str]
    DisplayName: Optional[str]
    EgressSourceIpAddresses: Optional[Sequence[str]]
    Id: Optional[str]
    IpAddress: Optional[str]
    Key: Optional[str]
    SubnetId: Optional[str]
    VcnId: Optional[str]
    PrivateSourceDnsZones: Optional[Sequence["_PrivateSourceDnsZonesDefinition"]]
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
            AnalyticsInstanceId=json_data.get("AnalyticsInstanceId"),
            DisplayName=json_data.get("DisplayName"),
            EgressSourceIpAddresses=json_data.get("EgressSourceIpAddresses"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            Key=json_data.get("Key"),
            SubnetId=json_data.get("SubnetId"),
            VcnId=json_data.get("VcnId"),
            PrivateSourceDnsZones=deserialize_list(json_data.get("PrivateSourceDnsZones"), PrivateSourceDnsZonesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PrivateSourceDnsZonesDefinition(BaseModel):
    Description: Optional[str]
    DnsZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateSourceDnsZonesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateSourceDnsZonesDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DnsZone=json_data.get("DnsZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateSourceDnsZonesDefinition = PrivateSourceDnsZonesDefinition


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


