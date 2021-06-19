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
    ClusterAdminPassword: Optional[str]
    ClusterDetails: Optional[Sequence["_ClusterDetailsDefinition"]]
    ClusterPublicKey: Optional[str]
    ClusterVersion: Optional[str]
    CompartmentId: Optional[str]
    CreatedBy: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsCloudSqlConfigured: Optional[bool]
    IsHighAvailability: Optional[bool]
    IsSecure: Optional[bool]
    Nodes: Optional[Sequence["_NodesDefinition2"]]
    NumberOfNodes: Optional[float]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    CloudSqlDetails: Optional[Sequence["_CloudSqlDetailsDefinition"]]
    MasterNode: Optional[Sequence["_MasterNodeDefinition"]]
    NetworkConfig: Optional[Sequence["_NetworkConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    UtilNode: Optional[Sequence["_UtilNodeDefinition"]]
    WorkerNode: Optional[Sequence["_WorkerNodeDefinition"]]

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
            ClusterAdminPassword=json_data.get("ClusterAdminPassword"),
            ClusterDetails=deserialize_list(json_data.get("ClusterDetails"), ClusterDetailsDefinition),
            ClusterPublicKey=json_data.get("ClusterPublicKey"),
            ClusterVersion=json_data.get("ClusterVersion"),
            CompartmentId=json_data.get("CompartmentId"),
            CreatedBy=json_data.get("CreatedBy"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsCloudSqlConfigured=json_data.get("IsCloudSqlConfigured"),
            IsHighAvailability=json_data.get("IsHighAvailability"),
            IsSecure=json_data.get("IsSecure"),
            Nodes=deserialize_list(json_data.get("Nodes"), NodesDefinition2),
            NumberOfNodes=json_data.get("NumberOfNodes"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            CloudSqlDetails=deserialize_list(json_data.get("CloudSqlDetails"), CloudSqlDetailsDefinition),
            MasterNode=deserialize_list(json_data.get("MasterNode"), MasterNodeDefinition),
            NetworkConfig=deserialize_list(json_data.get("NetworkConfig"), NetworkConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            UtilNode=deserialize_list(json_data.get("UtilNode"), UtilNodeDefinition),
            WorkerNode=deserialize_list(json_data.get("WorkerNode"), WorkerNodeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClusterDetailsDefinition(BaseModel):
    BdCellVersion: Optional[str]
    BdaVersion: Optional[str]
    BdmVersion: Optional[str]
    BdsVersion: Optional[str]
    BigDataManagerUrl: Optional[str]
    ClouderaManagerUrl: Optional[str]
    CsqlCellVersion: Optional[str]
    DbVersion: Optional[str]
    HueServerUrl: Optional[str]
    OsVersion: Optional[str]
    TimeCreated: Optional[str]
    TimeRefreshed: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            BdCellVersion=json_data.get("BdCellVersion"),
            BdaVersion=json_data.get("BdaVersion"),
            BdmVersion=json_data.get("BdmVersion"),
            BdsVersion=json_data.get("BdsVersion"),
            BigDataManagerUrl=json_data.get("BigDataManagerUrl"),
            ClouderaManagerUrl=json_data.get("ClouderaManagerUrl"),
            CsqlCellVersion=json_data.get("CsqlCellVersion"),
            DbVersion=json_data.get("DbVersion"),
            HueServerUrl=json_data.get("HueServerUrl"),
            OsVersion=json_data.get("OsVersion"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeRefreshed=json_data.get("TimeRefreshed"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterDetailsDefinition = ClusterDetailsDefinition


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
class NodesDefinition2(BaseModel):
    AttachedBlockVolumes: Optional[Sequence["_NodesDefinition"]]
    AvailabilityDomain: Optional[str]
    DisplayName: Optional[str]
    FaultDomain: Optional[str]
    Hostname: Optional[str]
    ImageId: Optional[str]
    InstanceId: Optional[str]
    IpAddress: Optional[str]
    NodeType: Optional[str]
    Shape: Optional[str]
    SshFingerprint: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]
    TimeCreated: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition2"]:
        if not json_data:
            return None
        return cls(
            AttachedBlockVolumes=deserialize_list(json_data.get("AttachedBlockVolumes"), NodesDefinition),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            DisplayName=json_data.get("DisplayName"),
            FaultDomain=json_data.get("FaultDomain"),
            Hostname=json_data.get("Hostname"),
            ImageId=json_data.get("ImageId"),
            InstanceId=json_data.get("InstanceId"),
            IpAddress=json_data.get("IpAddress"),
            NodeType=json_data.get("NodeType"),
            Shape=json_data.get("Shape"),
            SshFingerprint=json_data.get("SshFingerprint"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            TimeCreated=json_data.get("TimeCreated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition2 = NodesDefinition2


@dataclass
class NodesDefinition(BaseModel):
    VolumeAttachmentId: Optional[str]
    VolumeSizeInGbs: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition"]:
        if not json_data:
            return None
        return cls(
            VolumeAttachmentId=json_data.get("VolumeAttachmentId"),
            VolumeSizeInGbs=json_data.get("VolumeSizeInGbs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition = NodesDefinition


@dataclass
class CloudSqlDetailsDefinition(BaseModel):
    BlockVolumeSizeInGbs: Optional[str]
    Shape: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudSqlDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudSqlDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            BlockVolumeSizeInGbs=json_data.get("BlockVolumeSizeInGbs"),
            Shape=json_data.get("Shape"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudSqlDetailsDefinition = CloudSqlDetailsDefinition


@dataclass
class MasterNodeDefinition(BaseModel):
    BlockVolumeSizeInGbs: Optional[str]
    NumberOfNodes: Optional[float]
    Shape: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MasterNodeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterNodeDefinition"]:
        if not json_data:
            return None
        return cls(
            BlockVolumeSizeInGbs=json_data.get("BlockVolumeSizeInGbs"),
            NumberOfNodes=json_data.get("NumberOfNodes"),
            Shape=json_data.get("Shape"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterNodeDefinition = MasterNodeDefinition


@dataclass
class NetworkConfigDefinition(BaseModel):
    CidrBlock: Optional[str]
    IsNatGatewayRequired: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CidrBlock=json_data.get("CidrBlock"),
            IsNatGatewayRequired=json_data.get("IsNatGatewayRequired"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfigDefinition = NetworkConfigDefinition


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


@dataclass
class UtilNodeDefinition(BaseModel):
    BlockVolumeSizeInGbs: Optional[str]
    NumberOfNodes: Optional[float]
    Shape: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UtilNodeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UtilNodeDefinition"]:
        if not json_data:
            return None
        return cls(
            BlockVolumeSizeInGbs=json_data.get("BlockVolumeSizeInGbs"),
            NumberOfNodes=json_data.get("NumberOfNodes"),
            Shape=json_data.get("Shape"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UtilNodeDefinition = UtilNodeDefinition


@dataclass
class WorkerNodeDefinition(BaseModel):
    BlockVolumeSizeInGbs: Optional[str]
    NumberOfNodes: Optional[float]
    Shape: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerNodeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerNodeDefinition"]:
        if not json_data:
            return None
        return cls(
            BlockVolumeSizeInGbs=json_data.get("BlockVolumeSizeInGbs"),
            NumberOfNodes=json_data.get("NumberOfNodes"),
            Shape=json_data.get("Shape"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerNodeDefinition = WorkerNodeDefinition


