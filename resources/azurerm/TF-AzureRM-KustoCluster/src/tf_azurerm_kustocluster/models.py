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
    DataIngestionUri: Optional[str]
    DoubleEncryptionEnabled: Optional[bool]
    EnableDiskEncryption: Optional[bool]
    EnablePurge: Optional[bool]
    EnableStreamingIngest: Optional[bool]
    Engine: Optional[str]
    Id: Optional[str]
    LanguageExtensions: Optional[Sequence[str]]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TrustedExternalTenants: Optional[Sequence[str]]
    Uri: Optional[str]
    Zones: Optional[Sequence[str]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    OptimizedAutoScale: Optional[Sequence["_OptimizedAutoScaleDefinition"]]
    Sku: Optional[Sequence["_SkuDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VirtualNetworkConfiguration: Optional[Sequence["_VirtualNetworkConfigurationDefinition"]]

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
            DataIngestionUri=json_data.get("DataIngestionUri"),
            DoubleEncryptionEnabled=json_data.get("DoubleEncryptionEnabled"),
            EnableDiskEncryption=json_data.get("EnableDiskEncryption"),
            EnablePurge=json_data.get("EnablePurge"),
            EnableStreamingIngest=json_data.get("EnableStreamingIngest"),
            Engine=json_data.get("Engine"),
            Id=json_data.get("Id"),
            LanguageExtensions=json_data.get("LanguageExtensions"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TrustedExternalTenants=json_data.get("TrustedExternalTenants"),
            Uri=json_data.get("Uri"),
            Zones=json_data.get("Zones"),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            OptimizedAutoScale=deserialize_list(json_data.get("OptimizedAutoScale"), OptimizedAutoScaleDefinition),
            Sku=deserialize_list(json_data.get("Sku"), SkuDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VirtualNetworkConfiguration=deserialize_list(json_data.get("VirtualNetworkConfiguration"), VirtualNetworkConfigurationDefinition),
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
class IdentityDefinition(BaseModel):
    IdentityIds: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            IdentityIds=json_data.get("IdentityIds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


@dataclass
class OptimizedAutoScaleDefinition(BaseModel):
    MaximumInstances: Optional[float]
    MinimumInstances: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OptimizedAutoScaleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptimizedAutoScaleDefinition"]:
        if not json_data:
            return None
        return cls(
            MaximumInstances=json_data.get("MaximumInstances"),
            MinimumInstances=json_data.get("MinimumInstances"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptimizedAutoScaleDefinition = OptimizedAutoScaleDefinition


@dataclass
class SkuDefinition(BaseModel):
    Capacity: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SkuDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SkuDefinition"]:
        if not json_data:
            return None
        return cls(
            Capacity=json_data.get("Capacity"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SkuDefinition = SkuDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class VirtualNetworkConfigurationDefinition(BaseModel):
    DataManagementPublicIpId: Optional[str]
    EnginePublicIpId: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNetworkConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNetworkConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            DataManagementPublicIpId=json_data.get("DataManagementPublicIpId"),
            EnginePublicIpId=json_data.get("EnginePublicIpId"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNetworkConfigurationDefinition = VirtualNetworkConfigurationDefinition


