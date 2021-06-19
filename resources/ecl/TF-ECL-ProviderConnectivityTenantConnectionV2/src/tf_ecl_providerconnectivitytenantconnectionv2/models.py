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
    Description: Optional[str]
    DeviceId: Optional[str]
    DeviceInterfaceId: Optional[str]
    DeviceType: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    PortId: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TenantConnectionRequestId: Optional[str]
    TenantId: Optional[str]
    TenantIdOther: Optional[str]
    AttachmentOptsBaremetal: Optional[Sequence["_AttachmentOptsBaremetalDefinition"]]
    AttachmentOptsCompute: Optional[Sequence["_AttachmentOptsComputeDefinition"]]
    AttachmentOptsVna: Optional[Sequence["_AttachmentOptsVnaDefinition"]]

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
            Description=json_data.get("Description"),
            DeviceId=json_data.get("DeviceId"),
            DeviceInterfaceId=json_data.get("DeviceInterfaceId"),
            DeviceType=json_data.get("DeviceType"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            PortId=json_data.get("PortId"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TenantConnectionRequestId=json_data.get("TenantConnectionRequestId"),
            TenantId=json_data.get("TenantId"),
            TenantIdOther=json_data.get("TenantIdOther"),
            AttachmentOptsBaremetal=deserialize_list(json_data.get("AttachmentOptsBaremetal"), AttachmentOptsBaremetalDefinition),
            AttachmentOptsCompute=deserialize_list(json_data.get("AttachmentOptsCompute"), AttachmentOptsComputeDefinition),
            AttachmentOptsVna=deserialize_list(json_data.get("AttachmentOptsVna"), AttachmentOptsVnaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class AttachmentOptsBaremetalDefinition(BaseModel):
    SegmentationId: Optional[float]
    SegmentationType: Optional[str]
    AllowedAddressPairs: Optional[Sequence["_AllowedAddressPairsDefinition"]]
    FixedIps: Optional[Sequence["_FixedIpsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AttachmentOptsBaremetalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachmentOptsBaremetalDefinition"]:
        if not json_data:
            return None
        return cls(
            SegmentationId=json_data.get("SegmentationId"),
            SegmentationType=json_data.get("SegmentationType"),
            AllowedAddressPairs=deserialize_list(json_data.get("AllowedAddressPairs"), AllowedAddressPairsDefinition),
            FixedIps=deserialize_list(json_data.get("FixedIps"), FixedIpsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachmentOptsBaremetalDefinition = AttachmentOptsBaremetalDefinition


@dataclass
class AllowedAddressPairsDefinition(BaseModel):
    IpAddress: Optional[str]
    MacAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedAddressPairsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedAddressPairsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedAddressPairsDefinition = AllowedAddressPairsDefinition


@dataclass
class FixedIpsDefinition(BaseModel):
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FixedIpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedIpsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedIpsDefinition = FixedIpsDefinition


@dataclass
class AttachmentOptsComputeDefinition(BaseModel):
    AllowedAddressPairs: Optional[Sequence["_AllowedAddressPairsDefinition"]]
    FixedIps: Optional[Sequence["_FixedIpsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AttachmentOptsComputeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachmentOptsComputeDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedAddressPairs=deserialize_list(json_data.get("AllowedAddressPairs"), AllowedAddressPairsDefinition),
            FixedIps=deserialize_list(json_data.get("FixedIps"), FixedIpsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachmentOptsComputeDefinition = AttachmentOptsComputeDefinition


@dataclass
class AttachmentOptsVnaDefinition(BaseModel):
    FixedIps: Optional[Sequence["_FixedIpsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AttachmentOptsVnaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachmentOptsVnaDefinition"]:
        if not json_data:
            return None
        return cls(
            FixedIps=deserialize_list(json_data.get("FixedIps"), FixedIpsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachmentOptsVnaDefinition = AttachmentOptsVnaDefinition


