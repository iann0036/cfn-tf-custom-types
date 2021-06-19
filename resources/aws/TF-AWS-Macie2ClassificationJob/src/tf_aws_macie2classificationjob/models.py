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
    CreatedAt: Optional[str]
    CustomDataIdentifierIds: Optional[Sequence[str]]
    Description: Optional[str]
    Id: Optional[str]
    InitialRun: Optional[bool]
    JobArn: Optional[str]
    JobId: Optional[str]
    JobStatus: Optional[str]
    JobType: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    SamplingPercentage: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    UserPausedDetails: Optional[Sequence["_UserPausedDetailsDefinition"]]
    S3JobDefinition: Optional[Sequence["_S3JobDefinitionDefinition"]]
    ScheduleFrequency: Optional[Sequence["_ScheduleFrequencyDefinition"]]

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
            CreatedAt=json_data.get("CreatedAt"),
            CustomDataIdentifierIds=json_data.get("CustomDataIdentifierIds"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            InitialRun=json_data.get("InitialRun"),
            JobArn=json_data.get("JobArn"),
            JobId=json_data.get("JobId"),
            JobStatus=json_data.get("JobStatus"),
            JobType=json_data.get("JobType"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            SamplingPercentage=json_data.get("SamplingPercentage"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            UserPausedDetails=deserialize_list(json_data.get("UserPausedDetails"), UserPausedDetailsDefinition),
            S3JobDefinition=deserialize_list(json_data.get("S3JobDefinition"), S3JobDefinitionDefinition),
            ScheduleFrequency=deserialize_list(json_data.get("ScheduleFrequency"), ScheduleFrequencyDefinition),
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
class UserPausedDetailsDefinition(BaseModel):
    JobExpiresAt: Optional[str]
    JobImminentExpirationHealthEventArn: Optional[str]
    JobPausedAt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserPausedDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserPausedDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            JobExpiresAt=json_data.get("JobExpiresAt"),
            JobImminentExpirationHealthEventArn=json_data.get("JobImminentExpirationHealthEventArn"),
            JobPausedAt=json_data.get("JobPausedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserPausedDetailsDefinition = UserPausedDetailsDefinition


@dataclass
class S3JobDefinitionDefinition(BaseModel):
    BucketDefinitions: Optional[Sequence["_BucketDefinitionsDefinition"]]
    Scoping: Optional[Sequence["_ScopingDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_S3JobDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3JobDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketDefinitions=deserialize_list(json_data.get("BucketDefinitions"), BucketDefinitionsDefinition),
            Scoping=deserialize_list(json_data.get("Scoping"), ScopingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3JobDefinitionDefinition = S3JobDefinitionDefinition


@dataclass
class BucketDefinitionsDefinition(BaseModel):
    AccountId: Optional[str]
    Buckets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BucketDefinitionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BucketDefinitionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            Buckets=json_data.get("Buckets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BucketDefinitionsDefinition = BucketDefinitionsDefinition


@dataclass
class ScopingDefinition(BaseModel):
    Excludes: Optional[Sequence["_ExcludesDefinition"]]
    Includes: Optional[Sequence["_IncludesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScopingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScopingDefinition"]:
        if not json_data:
            return None
        return cls(
            Excludes=deserialize_list(json_data.get("Excludes"), ExcludesDefinition),
            Includes=deserialize_list(json_data.get("Includes"), IncludesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScopingDefinition = ScopingDefinition


@dataclass
class ExcludesDefinition(BaseModel):
    And: Optional[Sequence["_AndDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExcludesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcludesDefinition"]:
        if not json_data:
            return None
        return cls(
            And=deserialize_list(json_data.get("And"), AndDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcludesDefinition = ExcludesDefinition


@dataclass
class AndDefinition(BaseModel):
    SimpleScopeTerm: Optional[Sequence["_SimpleScopeTermDefinition"]]
    TagScopeTerm: Optional[Sequence["_TagScopeTermDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AndDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AndDefinition"]:
        if not json_data:
            return None
        return cls(
            SimpleScopeTerm=deserialize_list(json_data.get("SimpleScopeTerm"), SimpleScopeTermDefinition),
            TagScopeTerm=deserialize_list(json_data.get("TagScopeTerm"), TagScopeTermDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AndDefinition = AndDefinition


@dataclass
class SimpleScopeTermDefinition(BaseModel):
    Comparator: Optional[str]
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SimpleScopeTermDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SimpleScopeTermDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparator=json_data.get("Comparator"),
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SimpleScopeTermDefinition = SimpleScopeTermDefinition


@dataclass
class TagScopeTermDefinition(BaseModel):
    Comparator: Optional[str]
    Key: Optional[str]
    Target: Optional[str]
    TagValues: Optional[Sequence["_TagValuesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TagScopeTermDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagScopeTermDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparator=json_data.get("Comparator"),
            Key=json_data.get("Key"),
            Target=json_data.get("Target"),
            TagValues=deserialize_list(json_data.get("TagValues"), TagValuesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagScopeTermDefinition = TagScopeTermDefinition


@dataclass
class TagValuesDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagValuesDefinition = TagValuesDefinition


@dataclass
class IncludesDefinition(BaseModel):
    And: Optional[Sequence["_AndDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IncludesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncludesDefinition"]:
        if not json_data:
            return None
        return cls(
            And=deserialize_list(json_data.get("And"), AndDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncludesDefinition = IncludesDefinition


@dataclass
class ScheduleFrequencyDefinition(BaseModel):
    DailySchedule: Optional[bool]
    MonthlySchedule: Optional[float]
    WeeklySchedule: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleFrequencyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleFrequencyDefinition"]:
        if not json_data:
            return None
        return cls(
            DailySchedule=json_data.get("DailySchedule"),
            MonthlySchedule=json_data.get("MonthlySchedule"),
            WeeklySchedule=json_data.get("WeeklySchedule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleFrequencyDefinition = ScheduleFrequencyDefinition


