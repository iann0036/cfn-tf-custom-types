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
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    AnalyticsCluster: Optional[Sequence["_AnalyticsClusterDefinition"]]
    AvailabilityDomain: Optional[str]
    Channels: Optional[Sequence["_ChannelsDefinition6"]]
    CompartmentId: Optional[str]
    ConfigurationId: Optional[str]
    CurrentPlacement: Optional[Sequence["_CurrentPlacementDefinition"]]
    DataStorageSizeInGb: Optional[float]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    Description: Optional[str]
    DisplayName: Optional[str]
    Endpoints: Optional[Sequence["_EndpointsDefinition"]]
    FaultDomain: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    HeatWaveCluster: Optional[Sequence["_HeatWaveClusterDefinition"]]
    HostnameLabel: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    IsAnalyticsClusterAttached: Optional[bool]
    IsHeatWaveClusterAttached: Optional[bool]
    IsHighlyAvailable: Optional[bool]
    LifecycleDetails: Optional[str]
    MysqlVersion: Optional[str]
    Port: Optional[float]
    PortX: Optional[float]
    ShapeName: Optional[str]
    ShutdownType: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    BackupPolicy: Optional[Sequence["_BackupPolicyDefinition"]]
    Maintenance: Optional[Sequence["_MaintenanceDefinition"]]
    Source: Optional[Sequence["_SourceDefinition"]]
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
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
            AnalyticsCluster=deserialize_list(json_data.get("AnalyticsCluster"), AnalyticsClusterDefinition),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            Channels=deserialize_list(json_data.get("Channels"), ChannelsDefinition6),
            CompartmentId=json_data.get("CompartmentId"),
            ConfigurationId=json_data.get("ConfigurationId"),
            CurrentPlacement=deserialize_list(json_data.get("CurrentPlacement"), CurrentPlacementDefinition),
            DataStorageSizeInGb=json_data.get("DataStorageSizeInGb"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Endpoints=deserialize_list(json_data.get("Endpoints"), EndpointsDefinition),
            FaultDomain=json_data.get("FaultDomain"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            HeatWaveCluster=deserialize_list(json_data.get("HeatWaveCluster"), HeatWaveClusterDefinition),
            HostnameLabel=json_data.get("HostnameLabel"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            IsAnalyticsClusterAttached=json_data.get("IsAnalyticsClusterAttached"),
            IsHeatWaveClusterAttached=json_data.get("IsHeatWaveClusterAttached"),
            IsHighlyAvailable=json_data.get("IsHighlyAvailable"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            MysqlVersion=json_data.get("MysqlVersion"),
            Port=json_data.get("Port"),
            PortX=json_data.get("PortX"),
            ShapeName=json_data.get("ShapeName"),
            ShutdownType=json_data.get("ShutdownType"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            BackupPolicy=deserialize_list(json_data.get("BackupPolicy"), BackupPolicyDefinition),
            Maintenance=deserialize_list(json_data.get("Maintenance"), MaintenanceDefinition),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnalyticsClusterDefinition(BaseModel):
    ClusterSize: Optional[float]
    ShapeName: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnalyticsClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalyticsClusterDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterSize=json_data.get("ClusterSize"),
            ShapeName=json_data.get("ShapeName"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalyticsClusterDefinition = AnalyticsClusterDefinition


@dataclass
class ChannelsDefinition6(BaseModel):
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_ChannelsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_ChannelsDefinition2"]]
    Id: Optional[str]
    IsEnabled: Optional[bool]
    LifecycleDetails: Optional[str]
    Source: Optional[Sequence["_ChannelsDefinition4"]]
    State: Optional[str]
    Target: Optional[Sequence["_ChannelsDefinition5"]]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ChannelsDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChannelsDefinition6"]:
        if not json_data:
            return None
        return cls(
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), ChannelsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), ChannelsDefinition2),
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Source=deserialize_list(json_data.get("Source"), ChannelsDefinition4),
            State=json_data.get("State"),
            Target=deserialize_list(json_data.get("Target"), ChannelsDefinition5),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChannelsDefinition6 = ChannelsDefinition6


@dataclass
class ChannelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ChannelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChannelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChannelsDefinition = ChannelsDefinition


@dataclass
class ChannelsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ChannelsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChannelsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChannelsDefinition2 = ChannelsDefinition2


@dataclass
class ChannelsDefinition4(BaseModel):
    Hostname: Optional[str]
    Port: Optional[float]
    SourceType: Optional[str]
    SslCaCertificate: Optional[Sequence["_ChannelsDefinition3"]]
    SslMode: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ChannelsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChannelsDefinition4"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Port=json_data.get("Port"),
            SourceType=json_data.get("SourceType"),
            SslCaCertificate=deserialize_list(json_data.get("SslCaCertificate"), ChannelsDefinition3),
            SslMode=json_data.get("SslMode"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChannelsDefinition4 = ChannelsDefinition4


@dataclass
class ChannelsDefinition3(BaseModel):
    CertificateType: Optional[str]
    Contents: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ChannelsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChannelsDefinition3"]:
        if not json_data:
            return None
        return cls(
            CertificateType=json_data.get("CertificateType"),
            Contents=json_data.get("Contents"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChannelsDefinition3 = ChannelsDefinition3


@dataclass
class ChannelsDefinition5(BaseModel):
    ApplierUsername: Optional[str]
    ChannelName: Optional[str]
    DbSystemId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ChannelsDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChannelsDefinition5"]:
        if not json_data:
            return None
        return cls(
            ApplierUsername=json_data.get("ApplierUsername"),
            ChannelName=json_data.get("ChannelName"),
            DbSystemId=json_data.get("DbSystemId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChannelsDefinition5 = ChannelsDefinition5


@dataclass
class CurrentPlacementDefinition(BaseModel):
    AvailabilityDomain: Optional[str]
    FaultDomain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CurrentPlacementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CurrentPlacementDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            FaultDomain=json_data.get("FaultDomain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CurrentPlacementDefinition = CurrentPlacementDefinition


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
class EndpointsDefinition(BaseModel):
    Hostname: Optional[str]
    IpAddress: Optional[str]
    Modes: Optional[Sequence[str]]
    Port: Optional[float]
    PortX: Optional[float]
    Status: Optional[str]
    StatusDetails: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointsDefinition"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            IpAddress=json_data.get("IpAddress"),
            Modes=json_data.get("Modes"),
            Port=json_data.get("Port"),
            PortX=json_data.get("PortX"),
            Status=json_data.get("Status"),
            StatusDetails=json_data.get("StatusDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointsDefinition = EndpointsDefinition


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
class HeatWaveClusterDefinition(BaseModel):
    ClusterSize: Optional[float]
    ShapeName: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeatWaveClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeatWaveClusterDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterSize=json_data.get("ClusterSize"),
            ShapeName=json_data.get("ShapeName"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeatWaveClusterDefinition = HeatWaveClusterDefinition


@dataclass
class BackupPolicyDefinition(BaseModel):
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition2"]]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition2"]]
    IsEnabled: Optional[bool]
    RetentionInDays: Optional[float]
    WindowStartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition2),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition2),
            IsEnabled=json_data.get("IsEnabled"),
            RetentionInDays=json_data.get("RetentionInDays"),
            WindowStartTime=json_data.get("WindowStartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupPolicyDefinition = BackupPolicyDefinition


@dataclass
class DefinedTagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition2 = DefinedTagsDefinition2


@dataclass
class FreeformTagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition2 = FreeformTagsDefinition2


@dataclass
class MaintenanceDefinition(BaseModel):
    WindowStartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceDefinition"]:
        if not json_data:
            return None
        return cls(
            WindowStartTime=json_data.get("WindowStartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceDefinition = MaintenanceDefinition


@dataclass
class SourceDefinition(BaseModel):
    BackupId: Optional[str]
    SourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            BackupId=json_data.get("BackupId"),
            SourceType=json_data.get("SourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


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


