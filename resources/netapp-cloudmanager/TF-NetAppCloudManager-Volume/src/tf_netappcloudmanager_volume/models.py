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
    AggregateName: Optional[str]
    CapacityTier: Optional[str]
    ClientId: Optional[str]
    EnableCompression: Optional[bool]
    EnableDeduplication: Optional[bool]
    EnableThinProvisioning: Optional[bool]
    ExportPolicyIp: Optional[Sequence[str]]
    ExportPolicyName: Optional[str]
    ExportPolicyNfsVersion: Optional[Sequence[str]]
    ExportPolicyType: Optional[str]
    Id: Optional[str]
    Igroups: Optional[Sequence[str]]
    Iops: Optional[float]
    Name: Optional[str]
    OsName: Optional[str]
    Permission: Optional[str]
    ProviderVolumeType: Optional[str]
    ShareName: Optional[str]
    Size: Optional[float]
    SnapshotPolicyName: Optional[str]
    SvmName: Optional[str]
    Throughput: Optional[float]
    TieringPolicy: Optional[str]
    Unit: Optional[str]
    Users: Optional[Sequence[str]]
    VolumeProtocol: Optional[str]
    WorkingEnvironmentId: Optional[str]
    WorkingEnvironmentName: Optional[str]
    Initiator: Optional[Sequence["_InitiatorDefinition"]]

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
            AggregateName=json_data.get("AggregateName"),
            CapacityTier=json_data.get("CapacityTier"),
            ClientId=json_data.get("ClientId"),
            EnableCompression=json_data.get("EnableCompression"),
            EnableDeduplication=json_data.get("EnableDeduplication"),
            EnableThinProvisioning=json_data.get("EnableThinProvisioning"),
            ExportPolicyIp=json_data.get("ExportPolicyIp"),
            ExportPolicyName=json_data.get("ExportPolicyName"),
            ExportPolicyNfsVersion=json_data.get("ExportPolicyNfsVersion"),
            ExportPolicyType=json_data.get("ExportPolicyType"),
            Id=json_data.get("Id"),
            Igroups=json_data.get("Igroups"),
            Iops=json_data.get("Iops"),
            Name=json_data.get("Name"),
            OsName=json_data.get("OsName"),
            Permission=json_data.get("Permission"),
            ProviderVolumeType=json_data.get("ProviderVolumeType"),
            ShareName=json_data.get("ShareName"),
            Size=json_data.get("Size"),
            SnapshotPolicyName=json_data.get("SnapshotPolicyName"),
            SvmName=json_data.get("SvmName"),
            Throughput=json_data.get("Throughput"),
            TieringPolicy=json_data.get("TieringPolicy"),
            Unit=json_data.get("Unit"),
            Users=json_data.get("Users"),
            VolumeProtocol=json_data.get("VolumeProtocol"),
            WorkingEnvironmentId=json_data.get("WorkingEnvironmentId"),
            WorkingEnvironmentName=json_data.get("WorkingEnvironmentName"),
            Initiator=deserialize_list(json_data.get("Initiator"), InitiatorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InitiatorDefinition(BaseModel):
    Alias: Optional[str]
    Iqn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitiatorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitiatorDefinition"]:
        if not json_data:
            return None
        return cls(
            Alias=json_data.get("Alias"),
            Iqn=json_data.get("Iqn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitiatorDefinition = InitiatorDefinition


