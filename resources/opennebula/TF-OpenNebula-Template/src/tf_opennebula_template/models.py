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
    Context: Optional[Sequence["_ContextDefinition"]]
    Cpu: Optional[float]
    Gid: Optional[float]
    Gname: Optional[str]
    Group: Optional[str]
    Id: Optional[str]
    Memory: Optional[float]
    Name: Optional[str]
    Permissions: Optional[str]
    RegTime: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Template: Optional[str]
    Uid: Optional[float]
    Uname: Optional[str]
    Vcpu: Optional[float]
    Disk: Optional[Sequence["_DiskDefinition"]]
    Graphics: Optional[Sequence["_GraphicsDefinition"]]
    Nic: Optional[Sequence["_NicDefinition"]]
    Os: Optional[Sequence["_OsDefinition"]]
    Vmgroup: Optional[Sequence["_VmgroupDefinition"]]

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
            Context=deserialize_list(json_data.get("Context"), ContextDefinition),
            Cpu=json_data.get("Cpu"),
            Gid=json_data.get("Gid"),
            Gname=json_data.get("Gname"),
            Group=json_data.get("Group"),
            Id=json_data.get("Id"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
            Permissions=json_data.get("Permissions"),
            RegTime=json_data.get("RegTime"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Template=json_data.get("Template"),
            Uid=json_data.get("Uid"),
            Uname=json_data.get("Uname"),
            Vcpu=json_data.get("Vcpu"),
            Disk=deserialize_list(json_data.get("Disk"), DiskDefinition),
            Graphics=deserialize_list(json_data.get("Graphics"), GraphicsDefinition),
            Nic=deserialize_list(json_data.get("Nic"), NicDefinition),
            Os=deserialize_list(json_data.get("Os"), OsDefinition),
            Vmgroup=deserialize_list(json_data.get("Vmgroup"), VmgroupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ContextDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContextDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContextDefinition = ContextDefinition


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
class DiskDefinition(BaseModel):
    Driver: Optional[str]
    ImageId: Optional[float]
    Size: Optional[float]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDefinition"]:
        if not json_data:
            return None
        return cls(
            Driver=json_data.get("Driver"),
            ImageId=json_data.get("ImageId"),
            Size=json_data.get("Size"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDefinition = DiskDefinition


@dataclass
class GraphicsDefinition(BaseModel):
    Keymap: Optional[str]
    Listen: Optional[str]
    Port: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GraphicsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GraphicsDefinition"]:
        if not json_data:
            return None
        return cls(
            Keymap=json_data.get("Keymap"),
            Listen=json_data.get("Listen"),
            Port=json_data.get("Port"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GraphicsDefinition = GraphicsDefinition


@dataclass
class NicDefinition(BaseModel):
    Ip: Optional[str]
    Mac: Optional[str]
    Model: Optional[str]
    NetworkId: Optional[float]
    PhysicalDevice: Optional[str]
    SecurityGroups: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_NicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NicDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Mac=json_data.get("Mac"),
            Model=json_data.get("Model"),
            NetworkId=json_data.get("NetworkId"),
            PhysicalDevice=json_data.get("PhysicalDevice"),
            SecurityGroups=json_data.get("SecurityGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NicDefinition = NicDefinition


@dataclass
class OsDefinition(BaseModel):
    Arch: Optional[str]
    Boot: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsDefinition"]:
        if not json_data:
            return None
        return cls(
            Arch=json_data.get("Arch"),
            Boot=json_data.get("Boot"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsDefinition = OsDefinition


@dataclass
class VmgroupDefinition(BaseModel):
    Role: Optional[str]
    VmgroupId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VmgroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmgroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Role=json_data.get("Role"),
            VmgroupId=json_data.get("VmgroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmgroupDefinition = VmgroupDefinition


