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
    DnsName: Optional[str]
    Enabled: Optional[bool]
    HostedZoneId: Optional[str]
    Id: Optional[str]
    IpAddressType: Optional[str]
    IpSets: Optional[Sequence["_IpSets"]]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Attributes: Optional[Sequence["_Attributes"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DnsName=json_data.get("DnsName"),
            Enabled=json_data.get("Enabled"),
            HostedZoneId=json_data.get("HostedZoneId"),
            Id=json_data.get("Id"),
            IpAddressType=json_data.get("IpAddressType"),
            IpSets=json_data.get("IpSets"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Attributes=json_data.get("Attributes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpSets:
    IpAddresses: Optional[Sequence[str]]
    IpFamily: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpSets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpSets"]:
        if not json_data:
            return None
        return cls(
            IpAddresses=json_data.get("IpAddresses"),
            IpFamily=json_data.get("IpFamily"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpSets = IpSets


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Attributes:
    FlowLogsEnabled: Optional[bool]
    FlowLogsS3Bucket: Optional[str]
    FlowLogsS3Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attributes"]:
        if not json_data:
            return None
        return cls(
            FlowLogsEnabled=json_data.get("FlowLogsEnabled"),
            FlowLogsS3Bucket=json_data.get("FlowLogsS3Bucket"),
            FlowLogsS3Prefix=json_data.get("FlowLogsS3Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attributes = Attributes


