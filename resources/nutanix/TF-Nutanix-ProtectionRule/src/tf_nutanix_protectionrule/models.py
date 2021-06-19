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
    ApiVersion: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    StartTime: Optional[str]
    State: Optional[str]
    AvailabilityZoneConnectivityList: Optional[Sequence["_AvailabilityZoneConnectivityListDefinition"]]
    Categories: Optional[Sequence["_CategoriesDefinition"]]
    CategoryFilter: Optional[Sequence["_CategoryFilterDefinition"]]
    OrderedAvailabilityZoneList: Optional[Sequence["_OrderedAvailabilityZoneListDefinition"]]
    OwnerReference: Optional[Sequence["_OwnerReferenceDefinition"]]
    ProjectReference: Optional[Sequence["_ProjectReferenceDefinition"]]

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
            ApiVersion=json_data.get("ApiVersion"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            StartTime=json_data.get("StartTime"),
            State=json_data.get("State"),
            AvailabilityZoneConnectivityList=deserialize_list(json_data.get("AvailabilityZoneConnectivityList"), AvailabilityZoneConnectivityListDefinition),
            Categories=deserialize_list(json_data.get("Categories"), CategoriesDefinition),
            CategoryFilter=deserialize_list(json_data.get("CategoryFilter"), CategoryFilterDefinition),
            OrderedAvailabilityZoneList=deserialize_list(json_data.get("OrderedAvailabilityZoneList"), OrderedAvailabilityZoneListDefinition),
            OwnerReference=deserialize_list(json_data.get("OwnerReference"), OwnerReferenceDefinition),
            ProjectReference=deserialize_list(json_data.get("ProjectReference"), ProjectReferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class AvailabilityZoneConnectivityListDefinition(BaseModel):
    DestinationAvailabilityZoneIndex: Optional[float]
    SourceAvailabilityZoneIndex: Optional[float]
    SnapshotScheduleList: Optional[Sequence["_SnapshotScheduleListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AvailabilityZoneConnectivityListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailabilityZoneConnectivityListDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationAvailabilityZoneIndex=json_data.get("DestinationAvailabilityZoneIndex"),
            SourceAvailabilityZoneIndex=json_data.get("SourceAvailabilityZoneIndex"),
            SnapshotScheduleList=deserialize_list(json_data.get("SnapshotScheduleList"), SnapshotScheduleListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailabilityZoneConnectivityListDefinition = AvailabilityZoneConnectivityListDefinition


@dataclass
class SnapshotScheduleListDefinition(BaseModel):
    AutoSuspendTimeoutSecs: Optional[float]
    RecoveryPointObjectiveSecs: Optional[float]
    SnapshotType: Optional[str]
    LocalSnapshotRetentionPolicy: Optional[Sequence["_LocalSnapshotRetentionPolicyDefinition"]]
    RemoteSnapshotRetentionPolicy: Optional[Sequence["_RemoteSnapshotRetentionPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotScheduleListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotScheduleListDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoSuspendTimeoutSecs=json_data.get("AutoSuspendTimeoutSecs"),
            RecoveryPointObjectiveSecs=json_data.get("RecoveryPointObjectiveSecs"),
            SnapshotType=json_data.get("SnapshotType"),
            LocalSnapshotRetentionPolicy=deserialize_list(json_data.get("LocalSnapshotRetentionPolicy"), LocalSnapshotRetentionPolicyDefinition),
            RemoteSnapshotRetentionPolicy=deserialize_list(json_data.get("RemoteSnapshotRetentionPolicy"), RemoteSnapshotRetentionPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotScheduleListDefinition = SnapshotScheduleListDefinition


@dataclass
class LocalSnapshotRetentionPolicyDefinition(BaseModel):
    NumSnapshots: Optional[float]
    RollupRetentionPolicyMultiple: Optional[float]
    RollupRetentionPolicySnapshotIntervalType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalSnapshotRetentionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalSnapshotRetentionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            NumSnapshots=json_data.get("NumSnapshots"),
            RollupRetentionPolicyMultiple=json_data.get("RollupRetentionPolicyMultiple"),
            RollupRetentionPolicySnapshotIntervalType=json_data.get("RollupRetentionPolicySnapshotIntervalType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalSnapshotRetentionPolicyDefinition = LocalSnapshotRetentionPolicyDefinition


@dataclass
class RemoteSnapshotRetentionPolicyDefinition(BaseModel):
    NumSnapshots: Optional[float]
    RollupRetentionPolicyMultiple: Optional[float]
    RollupRetentionPolicySnapshotIntervalType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteSnapshotRetentionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteSnapshotRetentionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            NumSnapshots=json_data.get("NumSnapshots"),
            RollupRetentionPolicyMultiple=json_data.get("RollupRetentionPolicyMultiple"),
            RollupRetentionPolicySnapshotIntervalType=json_data.get("RollupRetentionPolicySnapshotIntervalType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteSnapshotRetentionPolicyDefinition = RemoteSnapshotRetentionPolicyDefinition


@dataclass
class CategoriesDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CategoriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoriesDefinition = CategoriesDefinition


@dataclass
class CategoryFilterDefinition(BaseModel):
    KindList: Optional[Sequence[str]]
    Type: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CategoryFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoryFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            KindList=json_data.get("KindList"),
            Type=json_data.get("Type"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoryFilterDefinition = CategoryFilterDefinition


@dataclass
class ParamsDefinition(BaseModel):
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition = ParamsDefinition


@dataclass
class OrderedAvailabilityZoneListDefinition(BaseModel):
    AvailabilityZoneUrl: Optional[str]
    ClusterUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrderedAvailabilityZoneListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrderedAvailabilityZoneListDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZoneUrl=json_data.get("AvailabilityZoneUrl"),
            ClusterUuid=json_data.get("ClusterUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrderedAvailabilityZoneListDefinition = OrderedAvailabilityZoneListDefinition


@dataclass
class OwnerReferenceDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerReferenceDefinition = OwnerReferenceDefinition


@dataclass
class ProjectReferenceDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectReferenceDefinition = ProjectReferenceDefinition


