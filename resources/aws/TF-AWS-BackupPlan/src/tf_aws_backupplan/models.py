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
    Arn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Version: Optional[str]
    AdvancedBackupSetting: Optional[Sequence["_AdvancedBackupSettingDefinition"]]
    Rule: Optional[Sequence["_RuleDefinition"]]

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
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Version=json_data.get("Version"),
            AdvancedBackupSetting=deserialize_list(json_data.get("AdvancedBackupSetting"), AdvancedBackupSettingDefinition),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class AdvancedBackupSettingDefinition(BaseModel):
    BackupOptions: Optional[Sequence["_BackupOptionsDefinition"]]
    ResourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedBackupSettingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedBackupSettingDefinition"]:
        if not json_data:
            return None
        return cls(
            BackupOptions=deserialize_list(json_data.get("BackupOptions"), BackupOptionsDefinition),
            ResourceType=json_data.get("ResourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedBackupSettingDefinition = AdvancedBackupSettingDefinition


@dataclass
class BackupOptionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupOptionsDefinition = BackupOptionsDefinition


@dataclass
class RuleDefinition(BaseModel):
    CompletionWindow: Optional[float]
    EnableContinuousBackup: Optional[bool]
    RecoveryPointTags: Optional[Sequence["_RecoveryPointTagsDefinition"]]
    RuleName: Optional[str]
    Schedule: Optional[str]
    StartWindow: Optional[float]
    TargetVaultName: Optional[str]
    CopyAction: Optional[Sequence["_CopyActionDefinition"]]
    Lifecycle: Optional[Sequence["_LifecycleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            CompletionWindow=json_data.get("CompletionWindow"),
            EnableContinuousBackup=json_data.get("EnableContinuousBackup"),
            RecoveryPointTags=deserialize_list(json_data.get("RecoveryPointTags"), RecoveryPointTagsDefinition),
            RuleName=json_data.get("RuleName"),
            Schedule=json_data.get("Schedule"),
            StartWindow=json_data.get("StartWindow"),
            TargetVaultName=json_data.get("TargetVaultName"),
            CopyAction=deserialize_list(json_data.get("CopyAction"), CopyActionDefinition),
            Lifecycle=deserialize_list(json_data.get("Lifecycle"), LifecycleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class RecoveryPointTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecoveryPointTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecoveryPointTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecoveryPointTagsDefinition = RecoveryPointTagsDefinition


@dataclass
class CopyActionDefinition(BaseModel):
    DestinationVaultArn: Optional[str]
    Lifecycle: Optional[Sequence["_LifecycleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CopyActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CopyActionDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationVaultArn=json_data.get("DestinationVaultArn"),
            Lifecycle=deserialize_list(json_data.get("Lifecycle"), LifecycleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CopyActionDefinition = CopyActionDefinition


@dataclass
class LifecycleDefinition(BaseModel):
    ColdStorageAfter: Optional[float]
    DeleteAfter: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleDefinition"]:
        if not json_data:
            return None
        return cls(
            ColdStorageAfter=json_data.get("ColdStorageAfter"),
            DeleteAfter=json_data.get("DeleteAfter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleDefinition = LifecycleDefinition


