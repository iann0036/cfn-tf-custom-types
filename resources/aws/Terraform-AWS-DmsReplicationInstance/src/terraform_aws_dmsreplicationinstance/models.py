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
    AllocatedStorage: Optional[float]
    ApplyImmediately: Optional[bool]
    AutoMinorVersionUpgrade: Optional[bool]
    AvailabilityZone: Optional[str]
    EngineVersion: Optional[str]
    Id: Optional[str]
    KmsKeyArn: Optional[str]
    MultiAz: Optional[bool]
    PreferredMaintenanceWindow: Optional[str]
    PubliclyAccessible: Optional[bool]
    ReplicationInstanceArn: Optional[str]
    ReplicationInstanceClass: Optional[str]
    ReplicationInstanceId: Optional[str]
    ReplicationInstancePrivateIps: Optional[Sequence[str]]
    ReplicationInstancePublicIps: Optional[Sequence[str]]
    ReplicationSubnetGroupId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VpcSecurityGroupIds: Optional[Sequence[str]]
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
            AllocatedStorage=json_data.get("AllocatedStorage"),
            ApplyImmediately=json_data.get("ApplyImmediately"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            MultiAz=json_data.get("MultiAz"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            ReplicationInstanceArn=json_data.get("ReplicationInstanceArn"),
            ReplicationInstanceClass=json_data.get("ReplicationInstanceClass"),
            ReplicationInstanceId=json_data.get("ReplicationInstanceId"),
            ReplicationInstancePrivateIps=json_data.get("ReplicationInstancePrivateIps"),
            ReplicationInstancePublicIps=json_data.get("ReplicationInstancePublicIps"),
            ReplicationSubnetGroupId=json_data.get("ReplicationSubnetGroupId"),
            Tags=json_data.get("Tags"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


