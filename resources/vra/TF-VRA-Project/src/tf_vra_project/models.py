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
    Administrators: Optional[Sequence[str]]
    CustomProperties: Optional[Sequence["_CustomPropertiesDefinition"]]
    Description: Optional[str]
    Id: Optional[str]
    MachineNamingTemplate: Optional[str]
    Members: Optional[Sequence[str]]
    Name: Optional[str]
    OperationTimeout: Optional[float]
    SharedResources: Optional[bool]
    Viewers: Optional[Sequence[str]]
    Constraints: Optional[Sequence["_ConstraintsDefinition"]]
    ZoneAssignments: Optional[Sequence["_ZoneAssignmentsDefinition"]]

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
            Administrators=json_data.get("Administrators"),
            CustomProperties=deserialize_list(json_data.get("CustomProperties"), CustomPropertiesDefinition),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            MachineNamingTemplate=json_data.get("MachineNamingTemplate"),
            Members=json_data.get("Members"),
            Name=json_data.get("Name"),
            OperationTimeout=json_data.get("OperationTimeout"),
            SharedResources=json_data.get("SharedResources"),
            Viewers=json_data.get("Viewers"),
            Constraints=deserialize_list(json_data.get("Constraints"), ConstraintsDefinition),
            ZoneAssignments=deserialize_list(json_data.get("ZoneAssignments"), ZoneAssignmentsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomPropertiesDefinition = CustomPropertiesDefinition


@dataclass
class ConstraintsDefinition(BaseModel):
    Extensibility: Optional[Sequence["_ExtensibilityDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    Storage: Optional[Sequence["_StorageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Extensibility=deserialize_list(json_data.get("Extensibility"), ExtensibilityDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Storage=deserialize_list(json_data.get("Storage"), StorageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConstraintsDefinition = ConstraintsDefinition


@dataclass
class ExtensibilityDefinition(BaseModel):
    Expression: Optional[str]
    Mandatory: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ExtensibilityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtensibilityDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Mandatory=json_data.get("Mandatory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtensibilityDefinition = ExtensibilityDefinition


@dataclass
class NetworkDefinition(BaseModel):
    Expression: Optional[str]
    Mandatory: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Mandatory=json_data.get("Mandatory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class StorageDefinition(BaseModel):
    Expression: Optional[str]
    Mandatory: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_StorageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Mandatory=json_data.get("Mandatory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageDefinition = StorageDefinition


@dataclass
class ZoneAssignmentsDefinition(BaseModel):
    CpuLimit: Optional[float]
    MaxInstances: Optional[float]
    MemoryLimitMb: Optional[float]
    Priority: Optional[float]
    StorageLimitGb: Optional[float]
    ZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZoneAssignmentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZoneAssignmentsDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuLimit=json_data.get("CpuLimit"),
            MaxInstances=json_data.get("MaxInstances"),
            MemoryLimitMb=json_data.get("MemoryLimitMb"),
            Priority=json_data.get("Priority"),
            StorageLimitGb=json_data.get("StorageLimitGb"),
            ZoneId=json_data.get("ZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZoneAssignmentsDefinition = ZoneAssignmentsDefinition


