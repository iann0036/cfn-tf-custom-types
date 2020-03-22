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
    Environment: Optional[Sequence["_Environment"]]
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
    Tags: Optional[Sequence["_Tags"]]
    Timeout: Optional[float]
    TriggerInfo: Optional[Sequence["_TriggerInfo"]]
    Vip: Optional[str]
    VpcId: Optional[str]
    ZipFile: Optional[str]
    Triggers: Optional[Sequence["_Triggers"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Environment=json_data.get("Environment"),
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
            Tags=json_data.get("Tags"),
            Timeout=json_data.get("Timeout"),
            TriggerInfo=json_data.get("TriggerInfo"),
            Vip=json_data.get("Vip"),
            VpcId=json_data.get("VpcId"),
            ZipFile=json_data.get("ZipFile"),
            Triggers=json_data.get("Triggers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Environment:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Environment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environment"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environment = Environment


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
class TriggerInfo:
    CreateTime: Optional[str]
    CustomArgument: Optional[str]
    Enable: Optional[bool]
    ModifyTime: Optional[str]
    Name: Optional[str]
    TriggerDesc: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TriggerInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggerInfo"]:
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
_TriggerInfo = TriggerInfo


@dataclass
class Triggers:
    CosRegion: Optional[str]
    Name: Optional[str]
    TriggerDesc: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Triggers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Triggers"]:
        if not json_data:
            return None
        return cls(
            CosRegion=json_data.get("CosRegion"),
            Name=json_data.get("Name"),
            TriggerDesc=json_data.get("TriggerDesc"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Triggers = Triggers


