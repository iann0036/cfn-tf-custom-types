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
    DnsDomain: Optional[str]
    External: Optional[bool]
    Mtu: Optional[float]
    Name: Optional[str]
    PortSecurityEnabled: Optional[bool]
    QosPolicyId: Optional[str]
    Region: Optional[str]
    Shared: Optional[bool]
    Tags: Optional[Sequence[str]]
    TenantId: Optional[str]
    TransparentVlan: Optional[bool]
    ValueSpecs: Optional[Sequence["_ValueSpecs"]]
    Segments: Optional[Sequence["_Segments"]]
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
            AdminStateUp=json_data.get("AdminStateUp"),
            AllTags=json_data.get("AllTags"),
            AvailabilityZoneHints=json_data.get("AvailabilityZoneHints"),
            Description=json_data.get("Description"),
            DnsDomain=json_data.get("DnsDomain"),
            External=json_data.get("External"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            PortSecurityEnabled=json_data.get("PortSecurityEnabled"),
            QosPolicyId=json_data.get("QosPolicyId"),
            Region=json_data.get("Region"),
            Shared=json_data.get("Shared"),
            Tags=json_data.get("Tags"),
            TenantId=json_data.get("TenantId"),
            TransparentVlan=json_data.get("TransparentVlan"),
            ValueSpecs=json_data.get("ValueSpecs"),
            Segments=json_data.get("Segments"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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
class Segments:
    NetworkType: Optional[str]
    PhysicalNetwork: Optional[str]
    SegmentationId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Segments"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Segments"]:
        if not json_data:
            return None
        return cls(
            NetworkType=json_data.get("NetworkType"),
            PhysicalNetwork=json_data.get("PhysicalNetwork"),
            SegmentationId=json_data.get("SegmentationId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Segments = Segments


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


