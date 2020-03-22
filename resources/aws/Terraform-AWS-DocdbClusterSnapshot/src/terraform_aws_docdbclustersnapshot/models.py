# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    AvailabilityZones: Optional[Sequence[str]]
    DbClusterIdentifier: Optional[str]
    DbClusterSnapshotArn: Optional[str]
    DbClusterSnapshotIdentifier: Optional[str]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    Port: Optional[float]
    SnapshotType: Optional[str]
    SourceDbClusterSnapshotArn: Optional[str]
    Status: Optional[str]
    StorageEncrypted: Optional[bool]
    VpcId: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            DbClusterIdentifier=json_data.get("DbClusterIdentifier"),
            DbClusterSnapshotArn=json_data.get("DbClusterSnapshotArn"),
            DbClusterSnapshotIdentifier=json_data.get("DbClusterSnapshotIdentifier"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Port=json_data.get("Port"),
            SnapshotType=json_data.get("SnapshotType"),
            SourceDbClusterSnapshotArn=json_data.get("SourceDbClusterSnapshotArn"),
            Status=json_data.get("Status"),
            StorageEncrypted=json_data.get("StorageEncrypted"),
            VpcId=json_data.get("VpcId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


