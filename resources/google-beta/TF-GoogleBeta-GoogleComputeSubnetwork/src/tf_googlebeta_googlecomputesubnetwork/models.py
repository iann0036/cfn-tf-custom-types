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
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    Fingerprint: Optional[str]
    GatewayAddress: Optional[str]
    Id: Optional[str]
    IpCidrRange: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    PrivateIpGoogleAccess: Optional[bool]
    PrivateIpv6GoogleAccess: Optional[str]
    Project: Optional[str]
    Purpose: Optional[str]
    Region: Optional[str]
    Role: Optional[str]
    SecondaryIpRange: Optional[Sequence["_SecondaryIpRangeDefinition"]]
    SelfLink: Optional[str]
    LogConfig: Optional[Sequence["_LogConfigDefinition"]]
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
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            Fingerprint=json_data.get("Fingerprint"),
            GatewayAddress=json_data.get("GatewayAddress"),
            Id=json_data.get("Id"),
            IpCidrRange=json_data.get("IpCidrRange"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            PrivateIpGoogleAccess=json_data.get("PrivateIpGoogleAccess"),
            PrivateIpv6GoogleAccess=json_data.get("PrivateIpv6GoogleAccess"),
            Project=json_data.get("Project"),
            Purpose=json_data.get("Purpose"),
            Region=json_data.get("Region"),
            Role=json_data.get("Role"),
            SecondaryIpRange=deserialize_list(json_data.get("SecondaryIpRange"), SecondaryIpRangeDefinition),
            SelfLink=json_data.get("SelfLink"),
            LogConfig=deserialize_list(json_data.get("LogConfig"), LogConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SecondaryIpRangeDefinition(BaseModel):
    IpCidrRange: Optional[str]
    RangeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryIpRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryIpRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            IpCidrRange=json_data.get("IpCidrRange"),
            RangeName=json_data.get("RangeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryIpRangeDefinition = SecondaryIpRangeDefinition


@dataclass
class LogConfigDefinition(BaseModel):
    AggregationInterval: Optional[str]
    FilterExpr: Optional[str]
    FlowSampling: Optional[float]
    Metadata: Optional[str]
    MetadataFields: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AggregationInterval=json_data.get("AggregationInterval"),
            FilterExpr=json_data.get("FilterExpr"),
            FlowSampling=json_data.get("FlowSampling"),
            Metadata=json_data.get("Metadata"),
            MetadataFields=json_data.get("MetadataFields"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfigDefinition = LogConfigDefinition


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


