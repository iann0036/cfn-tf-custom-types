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
    ApplyImmediately: Optional[bool]
    Arn: Optional[str]
    AutoMinorVersionUpgrade: Optional[bool]
    AvailabilityZone: Optional[str]
    CaCertIdentifier: Optional[str]
    ClusterIdentifier: Optional[str]
    CopyTagsToSnapshot: Optional[bool]
    DbParameterGroupName: Optional[str]
    DbSubnetGroupName: Optional[str]
    DbiResourceId: Optional[str]
    Endpoint: Optional[str]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    Id: Optional[str]
    Identifier: Optional[str]
    IdentifierPrefix: Optional[str]
    InstanceClass: Optional[str]
    KmsKeyId: Optional[str]
    MonitoringInterval: Optional[float]
    MonitoringRoleArn: Optional[str]
    PerformanceInsightsEnabled: Optional[bool]
    PerformanceInsightsKmsKeyId: Optional[str]
    Port: Optional[float]
    PreferredBackupWindow: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    PromotionTier: Optional[float]
    PubliclyAccessible: Optional[bool]
    StorageEncrypted: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Writer: Optional[bool]
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
            ApplyImmediately=json_data.get("ApplyImmediately"),
            Arn=json_data.get("Arn"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CaCertIdentifier=json_data.get("CaCertIdentifier"),
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
            CopyTagsToSnapshot=json_data.get("CopyTagsToSnapshot"),
            DbParameterGroupName=json_data.get("DbParameterGroupName"),
            DbSubnetGroupName=json_data.get("DbSubnetGroupName"),
            DbiResourceId=json_data.get("DbiResourceId"),
            Endpoint=json_data.get("Endpoint"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            Identifier=json_data.get("Identifier"),
            IdentifierPrefix=json_data.get("IdentifierPrefix"),
            InstanceClass=json_data.get("InstanceClass"),
            KmsKeyId=json_data.get("KmsKeyId"),
            MonitoringInterval=json_data.get("MonitoringInterval"),
            MonitoringRoleArn=json_data.get("MonitoringRoleArn"),
            PerformanceInsightsEnabled=json_data.get("PerformanceInsightsEnabled"),
            PerformanceInsightsKmsKeyId=json_data.get("PerformanceInsightsKmsKeyId"),
            Port=json_data.get("Port"),
            PreferredBackupWindow=json_data.get("PreferredBackupWindow"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            PromotionTier=json_data.get("PromotionTier"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            StorageEncrypted=json_data.get("StorageEncrypted"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Writer=json_data.get("Writer"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


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


