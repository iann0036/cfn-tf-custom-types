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
    ActivationKey: Optional[str]
    Arn: Optional[str]
    CloudwatchLogGroupArn: Optional[str]
    GatewayId: Optional[str]
    GatewayIpAddress: Optional[str]
    GatewayName: Optional[str]
    GatewayTimezone: Optional[str]
    GatewayType: Optional[str]
    Id: Optional[str]
    MediumChangerType: Optional[str]
    SmbGuestPassword: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TapeDriveType: Optional[str]
    SmbActiveDirectorySettings: Optional[Sequence["_SmbActiveDirectorySettings"]]
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
            ActivationKey=json_data.get("ActivationKey"),
            Arn=json_data.get("Arn"),
            CloudwatchLogGroupArn=json_data.get("CloudwatchLogGroupArn"),
            GatewayId=json_data.get("GatewayId"),
            GatewayIpAddress=json_data.get("GatewayIpAddress"),
            GatewayName=json_data.get("GatewayName"),
            GatewayTimezone=json_data.get("GatewayTimezone"),
            GatewayType=json_data.get("GatewayType"),
            Id=json_data.get("Id"),
            MediumChangerType=json_data.get("MediumChangerType"),
            SmbGuestPassword=json_data.get("SmbGuestPassword"),
            Tags=json_data.get("Tags"),
            TapeDriveType=json_data.get("TapeDriveType"),
            SmbActiveDirectorySettings=json_data.get("SmbActiveDirectorySettings"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class SmbActiveDirectorySettings:
    DomainName: Optional[str]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmbActiveDirectorySettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmbActiveDirectorySettings"]:
        if not json_data:
            return None
        return cls(
            DomainName=json_data.get("DomainName"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmbActiveDirectorySettings = SmbActiveDirectorySettings


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


