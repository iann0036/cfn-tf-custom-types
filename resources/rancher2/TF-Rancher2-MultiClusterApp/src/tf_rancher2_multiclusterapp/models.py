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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    CatalogName: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    RevisionHistoryLimit: Optional[float]
    RevisionId: Optional[str]
    Roles: Optional[Sequence[str]]
    TemplateName: Optional[str]
    TemplateVersion: Optional[str]
    TemplateVersionId: Optional[str]
    Wait: Optional[bool]
    Answers: Optional[Sequence["_AnswersDefinition"]]
    Members: Optional[Sequence["_MembersDefinition"]]
    Targets: Optional[Sequence["_TargetsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    UpgradeStrategy: Optional[Sequence["_UpgradeStrategyDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            CatalogName=json_data.get("CatalogName"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            RevisionHistoryLimit=json_data.get("RevisionHistoryLimit"),
            RevisionId=json_data.get("RevisionId"),
            Roles=json_data.get("Roles"),
            TemplateName=json_data.get("TemplateName"),
            TemplateVersion=json_data.get("TemplateVersion"),
            TemplateVersionId=json_data.get("TemplateVersionId"),
            Wait=json_data.get("Wait"),
            Answers=deserialize_list(json_data.get("Answers"), AnswersDefinition),
            Members=deserialize_list(json_data.get("Members"), MembersDefinition),
            Targets=deserialize_list(json_data.get("Targets"), TargetsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            UpgradeStrategy=deserialize_list(json_data.get("UpgradeStrategy"), UpgradeStrategyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class AnswersDefinition(BaseModel):
    ClusterId: Optional[str]
    ProjectId: Optional[str]
    Values: Optional[Sequence["_ValuesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AnswersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnswersDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterId=json_data.get("ClusterId"),
            ProjectId=json_data.get("ProjectId"),
            Values=deserialize_list(json_data.get("Values"), ValuesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnswersDefinition = AnswersDefinition


@dataclass
class ValuesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValuesDefinition = ValuesDefinition


@dataclass
class MembersDefinition(BaseModel):
    AccessType: Optional[str]
    GroupPrincipalId: Optional[str]
    UserPrincipalId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MembersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembersDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessType=json_data.get("AccessType"),
            GroupPrincipalId=json_data.get("GroupPrincipalId"),
            UserPrincipalId=json_data.get("UserPrincipalId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembersDefinition = MembersDefinition


@dataclass
class TargetsDefinition(BaseModel):
    ProjectId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetsDefinition"]:
        if not json_data:
            return None
        return cls(
            ProjectId=json_data.get("ProjectId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetsDefinition = TargetsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class UpgradeStrategyDefinition(BaseModel):
    RollingUpdate: Optional[Sequence["_RollingUpdateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UpgradeStrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpgradeStrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            RollingUpdate=deserialize_list(json_data.get("RollingUpdate"), RollingUpdateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpgradeStrategyDefinition = UpgradeStrategyDefinition


@dataclass
class RollingUpdateDefinition(BaseModel):
    BatchSize: Optional[float]
    Interval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RollingUpdateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollingUpdateDefinition"]:
        if not json_data:
            return None
        return cls(
            BatchSize=json_data.get("BatchSize"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollingUpdateDefinition = RollingUpdateDefinition


