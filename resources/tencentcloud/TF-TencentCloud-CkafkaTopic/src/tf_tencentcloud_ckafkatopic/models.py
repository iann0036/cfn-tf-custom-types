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
    CleanUpPolicy: Optional[str]
    CreateTime: Optional[str]
    EnableWhiteList: Optional[bool]
    ForwardCosBucket: Optional[str]
    ForwardInterval: Optional[float]
    ForwardStatus: Optional[float]
    Id: Optional[str]
    InstanceId: Optional[str]
    IpWhiteList: Optional[Sequence[str]]
    MaxMessageBytes: Optional[float]
    MessageStorageLocation: Optional[str]
    Note: Optional[str]
    PartitionNum: Optional[float]
    ReplicaNum: Optional[float]
    Retention: Optional[float]
    Segment: Optional[float]
    SegmentBytes: Optional[float]
    SyncReplicaMinNum: Optional[float]
    TopicName: Optional[str]
    UncleanLeaderElectionEnable: Optional[bool]

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
            CleanUpPolicy=json_data.get("CleanUpPolicy"),
            CreateTime=json_data.get("CreateTime"),
            EnableWhiteList=json_data.get("EnableWhiteList"),
            ForwardCosBucket=json_data.get("ForwardCosBucket"),
            ForwardInterval=json_data.get("ForwardInterval"),
            ForwardStatus=json_data.get("ForwardStatus"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            IpWhiteList=json_data.get("IpWhiteList"),
            MaxMessageBytes=json_data.get("MaxMessageBytes"),
            MessageStorageLocation=json_data.get("MessageStorageLocation"),
            Note=json_data.get("Note"),
            PartitionNum=json_data.get("PartitionNum"),
            ReplicaNum=json_data.get("ReplicaNum"),
            Retention=json_data.get("Retention"),
            Segment=json_data.get("Segment"),
            SegmentBytes=json_data.get("SegmentBytes"),
            SyncReplicaMinNum=json_data.get("SyncReplicaMinNum"),
            TopicName=json_data.get("TopicName"),
            UncleanLeaderElectionEnable=json_data.get("UncleanLeaderElectionEnable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


