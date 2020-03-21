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
    AdminStateUp: Optional[bool]
    AllTags: Optional[Sequence[str]]
    AvailabilityZoneHints: Optional[Sequence[str]]
    Description: Optional[str]
    Distributed: Optional[bool]
    EnableSnat: Optional[bool]
    ExternalGateway: Optional[str]
    ExternalNetworkId: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    Tags: Optional[Sequence[str]]
    TenantId: Optional[str]
    ValueSpecs: Optional[Sequence["_ValueSpecs"]]
    ExternalFixedIp: Optional[Sequence["_ExternalFixedIp"]]
    Timeouts: Optional["_Timeouts"]
    VendorOptions: Optional[Sequence["_VendorOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdminStateUp=json_data.get("AdminStateUp"),
            AllTags=json_data.get("AllTags"),
            AvailabilityZoneHints=json_data.get("AvailabilityZoneHints"),
            Description=json_data.get("Description"),
            Distributed=json_data.get("Distributed"),
            EnableSnat=json_data.get("EnableSnat"),
            ExternalGateway=json_data.get("ExternalGateway"),
            ExternalNetworkId=json_data.get("ExternalNetworkId"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Tags=json_data.get("Tags"),
            TenantId=json_data.get("TenantId"),
            ValueSpecs=json_data.get("ValueSpecs"),
            ExternalFixedIp=json_data.get("ExternalFixedIp"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            VendorOptions=json_data.get("VendorOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ValueSpecs:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValueSpecs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueSpecs"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueSpecs = ValueSpecs


@dataclass
class ExternalFixedIp:
    IpAddress: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalFixedIp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalFixedIp"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalFixedIp = ExternalFixedIp


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class VendorOptions:
    SetRouterGatewayAfterCreate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VendorOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VendorOptions"]:
        if not json_data:
            return None
        return cls(
            SetRouterGatewayAfterCreate=json_data.get("SetRouterGatewayAfterCreate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VendorOptions = VendorOptions


