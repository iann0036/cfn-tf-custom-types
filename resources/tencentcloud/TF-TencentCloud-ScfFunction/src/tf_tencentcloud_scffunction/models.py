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
    ClsLogsetId: Optional[str]
    ClsTopicId: Optional[str]
    CodeError: Optional[str]
    CodeResult: Optional[str]
    CodeSize: Optional[float]
    CosBucketName: Optional[str]
    CosBucketRegion: Optional[str]
    CosObjectName: Optional[str]
    Description: Optional[str]
    EipFixed: Optional[bool]
    Eips: Optional[Sequence[str]]
    Environment: Optional[Sequence["_EnvironmentDefinition"]]
    ErrNo: Optional[float]
    Handler: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    InstallDependency: Optional[bool]
    L5Enable: Optional[bool]
    MemSize: Optional[float]
    ModifyTime: Optional[str]
    Name: Optional[str]
    Namespace: Optional[str]
    Role: Optional[str]
    Runtime: Optional[str]
    Status: Optional[str]
    StatusDesc: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Timeout: Optional[float]
    TriggerInfo: Optional[Sequence["_TriggerInfoDefinition"]]
    Vip: Optional[str]
    VpcId: Optional[str]
    ZipFile: Optional[str]
    Triggers: Optional[Sequence["_TriggersDefinition"]]

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
            ClsLogsetId=json_data.get("ClsLogsetId"),
            ClsTopicId=json_data.get("ClsTopicId"),
            CodeError=json_data.get("CodeError"),
            CodeResult=json_data.get("CodeResult"),
            CodeSize=json_data.get("CodeSize"),
            CosBucketName=json_data.get("CosBucketName"),
            CosBucketRegion=json_data.get("CosBucketRegion"),
            CosObjectName=json_data.get("CosObjectName"),
            Description=json_data.get("Description"),
            EipFixed=json_data.get("EipFixed"),
            Eips=json_data.get("Eips"),
            Environment=deserialize_list(json_data.get("Environment"), EnvironmentDefinition),
            ErrNo=json_data.get("ErrNo"),
            Handler=json_data.get("Handler"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            InstallDependency=json_data.get("InstallDependency"),
            L5Enable=json_data.get("L5Enable"),
            MemSize=json_data.get("MemSize"),
            ModifyTime=json_data.get("ModifyTime"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Role=json_data.get("Role"),
            Runtime=json_data.get("Runtime"),
            Status=json_data.get("Status"),
            StatusDesc=json_data.get("StatusDesc"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Timeout=json_data.get("Timeout"),
            TriggerInfo=deserialize_list(json_data.get("TriggerInfo"), TriggerInfoDefinition),
            Vip=json_data.get("Vip"),
            VpcId=json_data.get("VpcId"),
            ZipFile=json_data.get("ZipFile"),
            Triggers=deserialize_list(json_data.get("Triggers"), TriggersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnvironmentDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentDefinition = EnvironmentDefinition


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
class TriggerInfoDefinition(BaseModel):
    CreateTime: Optional[str]
    CustomArgument: Optional[str]
    Enable: Optional[bool]
    ModifyTime: Optional[str]
    Name: Optional[str]
    TriggerDesc: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TriggerInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggerInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            CreateTime=json_data.get("CreateTime"),
            CustomArgument=json_data.get("CustomArgument"),
            Enable=json_data.get("Enable"),
            ModifyTime=json_data.get("ModifyTime"),
            Name=json_data.get("Name"),
            TriggerDesc=json_data.get("TriggerDesc"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggerInfoDefinition = TriggerInfoDefinition


@dataclass
class TriggersDefinition(BaseModel):
    CosRegion: Optional[str]
    Name: Optional[str]
    TriggerDesc: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TriggersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggersDefinition"]:
        if not json_data:
            return None
        return cls(
            CosRegion=json_data.get("CosRegion"),
            Name=json_data.get("Name"),
            TriggerDesc=json_data.get("TriggerDesc"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggersDefinition = TriggersDefinition


