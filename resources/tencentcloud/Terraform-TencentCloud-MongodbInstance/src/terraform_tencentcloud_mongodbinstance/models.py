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
    AvailableZone: Optional[str]
    CreateTime: Optional[str]
    EngineVersion: Optional[str]
    Id: Optional[str]
    InstanceName: Optional[str]
    MachineType: Optional[str]
    Memory: Optional[float]
    Password: Optional[str]
    ProjectId: Optional[float]
    SecurityGroups: Optional[Sequence[str]]
    Status: Optional[float]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Vip: Optional[str]
    Volume: Optional[float]
    VpcId: Optional[str]
    Vport: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailableZone=json_data.get("AvailableZone"),
            CreateTime=json_data.get("CreateTime"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            InstanceName=json_data.get("InstanceName"),
            MachineType=json_data.get("MachineType"),
            Memory=json_data.get("Memory"),
            Password=json_data.get("Password"),
            ProjectId=json_data.get("ProjectId"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Status=json_data.get("Status"),
            SubnetId=json_data.get("SubnetId"),
            Tags=json_data.get("Tags"),
            Vip=json_data.get("Vip"),
            Volume=json_data.get("Volume"),
            VpcId=json_data.get("VpcId"),
            Vport=json_data.get("Vport"),
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


