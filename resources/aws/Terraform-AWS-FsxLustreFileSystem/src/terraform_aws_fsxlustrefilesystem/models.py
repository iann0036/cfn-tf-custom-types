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
    Arn: Optional[str]
    DnsName: Optional[str]
    ExportPath: Optional[str]
    Id: Optional[str]
    ImportPath: Optional[str]
    ImportedFileChunkSize: Optional[float]
    NetworkInterfaceIds: Optional[Sequence[str]]
    OwnerId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    StorageCapacity: Optional[float]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    VpcId: Optional[str]
    WeeklyMaintenanceStartTime: Optional[str]
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
            Arn=json_data.get("Arn"),
            DnsName=json_data.get("DnsName"),
            ExportPath=json_data.get("ExportPath"),
            Id=json_data.get("Id"),
            ImportPath=json_data.get("ImportPath"),
            ImportedFileChunkSize=json_data.get("ImportedFileChunkSize"),
            NetworkInterfaceIds=json_data.get("NetworkInterfaceIds"),
            OwnerId=json_data.get("OwnerId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            StorageCapacity=json_data.get("StorageCapacity"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
            VpcId=json_data.get("VpcId"),
            WeeklyMaintenanceStartTime=json_data.get("WeeklyMaintenanceStartTime"),
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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


