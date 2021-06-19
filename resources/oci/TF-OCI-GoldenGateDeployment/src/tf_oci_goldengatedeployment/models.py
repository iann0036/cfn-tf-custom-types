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
    CompartmentId: Optional[str]
    CpuCoreCount: Optional[float]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DeploymentBackupId: Optional[str]
    DeploymentType: Optional[str]
    DeploymentUrl: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Fqdn: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsAutoScalingEnabled: Optional[bool]
    IsHealthy: Optional[bool]
    IsLatestVersion: Optional[bool]
    IsPublic: Optional[bool]
    LicenseModel: Optional[str]
    LifecycleDetails: Optional[str]
    NsgIds: Optional[Sequence[str]]
    PrivateIpAddress: Optional[str]
    PublicIpAddress: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]
    SystemTags: Optional[Sequence["_SystemTagsDefinition"]]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    OggData: Optional[Sequence["_OggDataDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            CpuCoreCount=json_data.get("CpuCoreCount"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DeploymentBackupId=json_data.get("DeploymentBackupId"),
            DeploymentType=json_data.get("DeploymentType"),
            DeploymentUrl=json_data.get("DeploymentUrl"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Fqdn=json_data.get("Fqdn"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsAutoScalingEnabled=json_data.get("IsAutoScalingEnabled"),
            IsHealthy=json_data.get("IsHealthy"),
            IsLatestVersion=json_data.get("IsLatestVersion"),
            IsPublic=json_data.get("IsPublic"),
            LicenseModel=json_data.get("LicenseModel"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            NsgIds=json_data.get("NsgIds"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            PublicIpAddress=json_data.get("PublicIpAddress"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            SystemTags=deserialize_list(json_data.get("SystemTags"), SystemTagsDefinition),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            OggData=deserialize_list(json_data.get("OggData"), OggDataDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class SystemTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemTagsDefinition = SystemTagsDefinition


@dataclass
class OggDataDefinition(BaseModel):
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    Certificate: Optional[str]
    DeploymentName: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OggDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OggDataDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
            Certificate=json_data.get("Certificate"),
            DeploymentName=json_data.get("DeploymentName"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OggDataDefinition = OggDataDefinition


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


