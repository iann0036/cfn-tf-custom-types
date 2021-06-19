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
    AvailabilityStatus: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DeployPluginsId: Optional[Sequence[str]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Host: Optional[str]
    Id: Optional[str]
    InstallKeyId: Optional[str]
    InstallPath: Optional[str]
    IsAgentAutoUpgradable: Optional[bool]
    LifecycleDetails: Optional[str]
    ManagedAgentId: Optional[str]
    PlatformName: Optional[str]
    PlatformType: Optional[str]
    PlatformVersion: Optional[str]
    PluginList: Optional[Sequence["_PluginListDefinition"]]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeLastHeartbeat: Optional[str]
    TimeUpdated: Optional[str]
    Version: Optional[str]
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
            AvailabilityStatus=json_data.get("AvailabilityStatus"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DeployPluginsId=json_data.get("DeployPluginsId"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            InstallKeyId=json_data.get("InstallKeyId"),
            InstallPath=json_data.get("InstallPath"),
            IsAgentAutoUpgradable=json_data.get("IsAgentAutoUpgradable"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            ManagedAgentId=json_data.get("ManagedAgentId"),
            PlatformName=json_data.get("PlatformName"),
            PlatformType=json_data.get("PlatformType"),
            PlatformVersion=json_data.get("PlatformVersion"),
            PluginList=deserialize_list(json_data.get("PluginList"), PluginListDefinition),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeLastHeartbeat=json_data.get("TimeLastHeartbeat"),
            TimeUpdated=json_data.get("TimeUpdated"),
            Version=json_data.get("Version"),
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
class PluginListDefinition(BaseModel):
    PluginDisplayName: Optional[str]
    PluginId: Optional[str]
    PluginName: Optional[str]
    PluginVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PluginListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PluginListDefinition"]:
        if not json_data:
            return None
        return cls(
            PluginDisplayName=json_data.get("PluginDisplayName"),
            PluginId=json_data.get("PluginId"),
            PluginName=json_data.get("PluginName"),
            PluginVersion=json_data.get("PluginVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PluginListDefinition = PluginListDefinition


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


