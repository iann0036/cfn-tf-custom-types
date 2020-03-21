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
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    EnableFlowLogs: Optional[bool]
    Fingerprint: Optional[str]
    GatewayAddress: Optional[str]
    IpCidrRange: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    PrivateIpGoogleAccess: Optional[bool]
    Project: Optional[str]
    Region: Optional[str]
    SecondaryIpRange: Optional[Sequence["_SecondaryIpRange"]]
    SelfLink: Optional[str]
    LogConfig: Optional[Sequence["_LogConfig"]]
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
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            EnableFlowLogs=json_data.get("EnableFlowLogs"),
            Fingerprint=json_data.get("Fingerprint"),
            GatewayAddress=json_data.get("GatewayAddress"),
            IpCidrRange=json_data.get("IpCidrRange"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            PrivateIpGoogleAccess=json_data.get("PrivateIpGoogleAccess"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            SecondaryIpRange=json_data.get("SecondaryIpRange"),
            SelfLink=json_data.get("SelfLink"),
            LogConfig=json_data.get("LogConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SecondaryIpRange:
    IpCidrRange: Optional[str]
    RangeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryIpRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryIpRange"]:
        if not json_data:
            return None
        return cls(
            IpCidrRange=json_data.get("IpCidrRange"),
            RangeName=json_data.get("RangeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryIpRange = SecondaryIpRange


@dataclass
class LogConfig:
    AggregationInterval: Optional[str]
    FlowSampling: Optional[float]
    Metadata: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfig"]:
        if not json_data:
            return None
        return cls(
            AggregationInterval=json_data.get("AggregationInterval"),
            FlowSampling=json_data.get("FlowSampling"),
            Metadata=json_data.get("Metadata"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfig = LogConfig


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


