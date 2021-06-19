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
    AccountName: Optional[str]
    CreateFromSnapshotResourceId: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    MountIpAddresses: Optional[Sequence[str]]
    Name: Optional[str]
    PoolName: Optional[str]
    Protocols: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    SecurityStyle: Optional[str]
    ServiceLevel: Optional[str]
    StorageQuotaInGb: Optional[float]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VolumePath: Optional[str]
    DataProtectionReplication: Optional[Sequence["_DataProtectionReplicationDefinition"]]
    ExportPolicyRule: Optional[Sequence["_ExportPolicyRuleDefinition"]]
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
            AccountName=json_data.get("AccountName"),
            CreateFromSnapshotResourceId=json_data.get("CreateFromSnapshotResourceId"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            MountIpAddresses=json_data.get("MountIpAddresses"),
            Name=json_data.get("Name"),
            PoolName=json_data.get("PoolName"),
            Protocols=json_data.get("Protocols"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecurityStyle=json_data.get("SecurityStyle"),
            ServiceLevel=json_data.get("ServiceLevel"),
            StorageQuotaInGb=json_data.get("StorageQuotaInGb"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VolumePath=json_data.get("VolumePath"),
            DataProtectionReplication=deserialize_list(json_data.get("DataProtectionReplication"), DataProtectionReplicationDefinition),
            ExportPolicyRule=deserialize_list(json_data.get("ExportPolicyRule"), ExportPolicyRuleDefinition),
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
class DataProtectionReplicationDefinition(BaseModel):
    EndpointType: Optional[str]
    RemoteVolumeLocation: Optional[str]
    RemoteVolumeResourceId: Optional[str]
    ReplicationFrequency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataProtectionReplicationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataProtectionReplicationDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointType=json_data.get("EndpointType"),
            RemoteVolumeLocation=json_data.get("RemoteVolumeLocation"),
            RemoteVolumeResourceId=json_data.get("RemoteVolumeResourceId"),
            ReplicationFrequency=json_data.get("ReplicationFrequency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataProtectionReplicationDefinition = DataProtectionReplicationDefinition


@dataclass
class ExportPolicyRuleDefinition(BaseModel):
    AllowedClients: Optional[Sequence[str]]
    CifsEnabled: Optional[bool]
    Nfsv3Enabled: Optional[bool]
    Nfsv4Enabled: Optional[bool]
    ProtocolsEnabled: Optional[Sequence[str]]
    RootAccessEnabled: Optional[bool]
    RuleIndex: Optional[float]
    UnixReadOnly: Optional[bool]
    UnixReadWrite: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ExportPolicyRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExportPolicyRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedClients=json_data.get("AllowedClients"),
            CifsEnabled=json_data.get("CifsEnabled"),
            Nfsv3Enabled=json_data.get("Nfsv3Enabled"),
            Nfsv4Enabled=json_data.get("Nfsv4Enabled"),
            ProtocolsEnabled=json_data.get("ProtocolsEnabled"),
            RootAccessEnabled=json_data.get("RootAccessEnabled"),
            RuleIndex=json_data.get("RuleIndex"),
            UnixReadOnly=json_data.get("UnixReadOnly"),
            UnixReadWrite=json_data.get("UnixReadWrite"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExportPolicyRuleDefinition = ExportPolicyRuleDefinition


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


