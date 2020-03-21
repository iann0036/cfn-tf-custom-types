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
    AvailabilityZone: Optional[Sequence[str]]
    Created: Optional[str]
    Flavor: Optional[str]
    HaReplicationMode: Optional[str]
    Name: Optional[str]
    Nodes: Optional[Sequence["_Nodes"]]
    ParamGroupId: Optional[str]
    PrivateIps: Optional[Sequence[str]]
    PublicIps: Optional[Sequence[str]]
    SecurityGroupId: Optional[str]
    SubnetId: Optional[str]
    VpcId: Optional[str]
    BackupStrategy: Optional[Sequence["_BackupStrategy"]]
    Db: Optional[Sequence["_Db"]]
    Timeouts: Optional["_Timeouts"]
    Volume: Optional[Sequence["_Volume"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Created=json_data.get("Created"),
            Flavor=json_data.get("Flavor"),
            HaReplicationMode=json_data.get("HaReplicationMode"),
            Name=json_data.get("Name"),
            Nodes=json_data.get("Nodes"),
            ParamGroupId=json_data.get("ParamGroupId"),
            PrivateIps=json_data.get("PrivateIps"),
            PublicIps=json_data.get("PublicIps"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SubnetId=json_data.get("SubnetId"),
            VpcId=json_data.get("VpcId"),
            BackupStrategy=json_data.get("BackupStrategy"),
            Db=json_data.get("Db"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Volume=json_data.get("Volume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Nodes:
    AvailabilityZone: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Role: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nodes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nodes"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Role=json_data.get("Role"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nodes = Nodes


@dataclass
class BackupStrategy:
    KeepDays: Optional[float]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupStrategy"]:
        if not json_data:
            return None
        return cls(
            KeepDays=json_data.get("KeepDays"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupStrategy = BackupStrategy


@dataclass
class Db:
    Password: Optional[str]
    Port: Optional[float]
    Type: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Db"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Db"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Db = Db


@dataclass
class Timeouts:
    Create: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class Volume:
    DiskEncryptionId: Optional[str]
    Size: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volume"]:
        if not json_data:
            return None
        return cls(
            DiskEncryptionId=json_data.get("DiskEncryptionId"),
            Size=json_data.get("Size"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volume = Volume


