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
    AllowDeployInExistingRg: Optional[bool]
    BackupVolumesToCbs: Optional[bool]
    CapacityTier: Optional[str]
    Cidr: Optional[str]
    ClientId: Optional[str]
    CloudProviderAccount: Optional[str]
    DataEncryptionType: Optional[str]
    DiskSize: Optional[float]
    DiskSizeUnit: Optional[str]
    EnableCompliance: Optional[bool]
    EnableMonitoring: Optional[bool]
    Id: Optional[str]
    InstanceType: Optional[str]
    IsHa: Optional[bool]
    LicenseType: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    NssAccount: Optional[str]
    OntapVersion: Optional[str]
    PlatformSerialNumberNode1: Optional[str]
    PlatformSerialNumberNode2: Optional[str]
    ResourceGroup: Optional[str]
    SecurityGroupId: Optional[str]
    SerialNumber: Optional[str]
    StorageType: Optional[str]
    SubnetId: Optional[str]
    SubscriptionId: Optional[str]
    SvmPassword: Optional[str]
    TierLevel: Optional[str]
    UseLatestVersion: Optional[bool]
    VnetId: Optional[str]
    VnetResourceGroup: Optional[str]
    WorkspaceId: Optional[str]
    WritingSpeedState: Optional[str]
    AzureTag: Optional[Sequence["_AzureTagDefinition"]]

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
            AllowDeployInExistingRg=json_data.get("AllowDeployInExistingRg"),
            BackupVolumesToCbs=json_data.get("BackupVolumesToCbs"),
            CapacityTier=json_data.get("CapacityTier"),
            Cidr=json_data.get("Cidr"),
            ClientId=json_data.get("ClientId"),
            CloudProviderAccount=json_data.get("CloudProviderAccount"),
            DataEncryptionType=json_data.get("DataEncryptionType"),
            DiskSize=json_data.get("DiskSize"),
            DiskSizeUnit=json_data.get("DiskSizeUnit"),
            EnableCompliance=json_data.get("EnableCompliance"),
            EnableMonitoring=json_data.get("EnableMonitoring"),
            Id=json_data.get("Id"),
            InstanceType=json_data.get("InstanceType"),
            IsHa=json_data.get("IsHa"),
            LicenseType=json_data.get("LicenseType"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NssAccount=json_data.get("NssAccount"),
            OntapVersion=json_data.get("OntapVersion"),
            PlatformSerialNumberNode1=json_data.get("PlatformSerialNumberNode1"),
            PlatformSerialNumberNode2=json_data.get("PlatformSerialNumberNode2"),
            ResourceGroup=json_data.get("ResourceGroup"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SerialNumber=json_data.get("SerialNumber"),
            StorageType=json_data.get("StorageType"),
            SubnetId=json_data.get("SubnetId"),
            SubscriptionId=json_data.get("SubscriptionId"),
            SvmPassword=json_data.get("SvmPassword"),
            TierLevel=json_data.get("TierLevel"),
            UseLatestVersion=json_data.get("UseLatestVersion"),
            VnetId=json_data.get("VnetId"),
            VnetResourceGroup=json_data.get("VnetResourceGroup"),
            WorkspaceId=json_data.get("WorkspaceId"),
            WritingSpeedState=json_data.get("WritingSpeedState"),
            AzureTag=deserialize_list(json_data.get("AzureTag"), AzureTagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AzureTagDefinition(BaseModel):
    TagKey: Optional[str]
    TagValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureTagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureTagDefinition"]:
        if not json_data:
            return None
        return cls(
            TagKey=json_data.get("TagKey"),
            TagValue=json_data.get("TagValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureTagDefinition = AzureTagDefinition


