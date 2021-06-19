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
    ActivationKey: Optional[str]
    Arn: Optional[str]
    AverageDownloadRateLimitInBitsPerSec: Optional[float]
    AverageUploadRateLimitInBitsPerSec: Optional[float]
    CloudwatchLogGroupArn: Optional[str]
    Ec2InstanceId: Optional[str]
    EndpointType: Optional[str]
    GatewayId: Optional[str]
    GatewayIpAddress: Optional[str]
    GatewayName: Optional[str]
    GatewayNetworkInterface: Optional[Sequence["_GatewayNetworkInterfaceDefinition"]]
    GatewayTimezone: Optional[str]
    GatewayType: Optional[str]
    GatewayVpcEndpoint: Optional[str]
    HostEnvironment: Optional[str]
    Id: Optional[str]
    MediumChangerType: Optional[str]
    SmbFileShareVisibility: Optional[bool]
    SmbGuestPassword: Optional[str]
    SmbSecurityStrategy: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TapeDriveType: Optional[str]
    SmbActiveDirectorySettings: Optional[Sequence["_SmbActiveDirectorySettingsDefinition"]]
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
            ActivationKey=json_data.get("ActivationKey"),
            Arn=json_data.get("Arn"),
            AverageDownloadRateLimitInBitsPerSec=json_data.get("AverageDownloadRateLimitInBitsPerSec"),
            AverageUploadRateLimitInBitsPerSec=json_data.get("AverageUploadRateLimitInBitsPerSec"),
            CloudwatchLogGroupArn=json_data.get("CloudwatchLogGroupArn"),
            Ec2InstanceId=json_data.get("Ec2InstanceId"),
            EndpointType=json_data.get("EndpointType"),
            GatewayId=json_data.get("GatewayId"),
            GatewayIpAddress=json_data.get("GatewayIpAddress"),
            GatewayName=json_data.get("GatewayName"),
            GatewayNetworkInterface=deserialize_list(json_data.get("GatewayNetworkInterface"), GatewayNetworkInterfaceDefinition),
            GatewayTimezone=json_data.get("GatewayTimezone"),
            GatewayType=json_data.get("GatewayType"),
            GatewayVpcEndpoint=json_data.get("GatewayVpcEndpoint"),
            HostEnvironment=json_data.get("HostEnvironment"),
            Id=json_data.get("Id"),
            MediumChangerType=json_data.get("MediumChangerType"),
            SmbFileShareVisibility=json_data.get("SmbFileShareVisibility"),
            SmbGuestPassword=json_data.get("SmbGuestPassword"),
            SmbSecurityStrategy=json_data.get("SmbSecurityStrategy"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TapeDriveType=json_data.get("TapeDriveType"),
            SmbActiveDirectorySettings=deserialize_list(json_data.get("SmbActiveDirectorySettings"), SmbActiveDirectorySettingsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GatewayNetworkInterfaceDefinition(BaseModel):
    Ipv4Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayNetworkInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayNetworkInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4Address=json_data.get("Ipv4Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayNetworkInterfaceDefinition = GatewayNetworkInterfaceDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class SmbActiveDirectorySettingsDefinition(BaseModel):
    DomainControllers: Optional[Sequence[str]]
    DomainName: Optional[str]
    OrganizationalUnit: Optional[str]
    Password: Optional[str]
    TimeoutInSeconds: Optional[float]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmbActiveDirectorySettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmbActiveDirectorySettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DomainControllers=json_data.get("DomainControllers"),
            DomainName=json_data.get("DomainName"),
            OrganizationalUnit=json_data.get("OrganizationalUnit"),
            Password=json_data.get("Password"),
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmbActiveDirectorySettingsDefinition = SmbActiveDirectorySettingsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


