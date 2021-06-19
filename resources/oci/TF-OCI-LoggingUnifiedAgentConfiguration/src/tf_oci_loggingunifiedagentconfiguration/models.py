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
    CompartmentId: Optional[str]
    ConfigurationState: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    Description: Optional[str]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsEnabled: Optional[bool]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeLastModified: Optional[str]
    GroupAssociation: Optional[Sequence["_GroupAssociationDefinition"]]
    ServiceConfiguration: Optional[Sequence["_ServiceConfigurationDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            CompartmentId=json_data.get("CompartmentId"),
            ConfigurationState=json_data.get("ConfigurationState"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeLastModified=json_data.get("TimeLastModified"),
            GroupAssociation=deserialize_list(json_data.get("GroupAssociation"), GroupAssociationDefinition),
            ServiceConfiguration=deserialize_list(json_data.get("ServiceConfiguration"), ServiceConfigurationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class GroupAssociationDefinition(BaseModel):
    GroupList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GroupAssociationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupAssociationDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupList=json_data.get("GroupList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupAssociationDefinition = GroupAssociationDefinition


@dataclass
class ServiceConfigurationDefinition(BaseModel):
    ConfigurationType: Optional[str]
    Destination: Optional[Sequence["_DestinationDefinition"]]
    Sources: Optional[Sequence["_SourcesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigurationType=json_data.get("ConfigurationType"),
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
            Sources=deserialize_list(json_data.get("Sources"), SourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceConfigurationDefinition = ServiceConfigurationDefinition


@dataclass
class DestinationDefinition(BaseModel):
    LogObjectId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            LogObjectId=json_data.get("LogObjectId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


@dataclass
class SourcesDefinition(BaseModel):
    Channels: Optional[Sequence[str]]
    Name: Optional[str]
    Paths: Optional[Sequence[str]]
    SourceType: Optional[str]
    Parser: Optional[Sequence["_ParserDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            Channels=json_data.get("Channels"),
            Name=json_data.get("Name"),
            Paths=json_data.get("Paths"),
            SourceType=json_data.get("SourceType"),
            Parser=deserialize_list(json_data.get("Parser"), ParserDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourcesDefinition = SourcesDefinition


@dataclass
class ParserDefinition(BaseModel):
    Delimiter: Optional[str]
    Expression: Optional[str]
    FieldTimeKey: Optional[str]
    Format: Optional[Sequence[str]]
    FormatFirstline: Optional[str]
    GrokFailureKey: Optional[str]
    GrokNameKey: Optional[str]
    IsEstimateCurrentEvent: Optional[bool]
    IsKeepTimeKey: Optional[bool]
    IsNullEmptyString: Optional[bool]
    IsSupportColonlessIdent: Optional[bool]
    IsWithPriority: Optional[bool]
    Keys: Optional[Sequence[str]]
    MessageFormat: Optional[str]
    MessageKey: Optional[str]
    MultiLineStartRegexp: Optional[str]
    NullValuePattern: Optional[str]
    ParserType: Optional[str]
    Rfc5424timeFormat: Optional[str]
    SyslogParserType: Optional[str]
    TimeFormat: Optional[str]
    TimeType: Optional[str]
    TimeoutInMilliseconds: Optional[float]
    Types: Optional[Sequence["_TypesDefinition"]]
    Patterns: Optional[Sequence["_PatternsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ParserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParserDefinition"]:
        if not json_data:
            return None
        return cls(
            Delimiter=json_data.get("Delimiter"),
            Expression=json_data.get("Expression"),
            FieldTimeKey=json_data.get("FieldTimeKey"),
            Format=json_data.get("Format"),
            FormatFirstline=json_data.get("FormatFirstline"),
            GrokFailureKey=json_data.get("GrokFailureKey"),
            GrokNameKey=json_data.get("GrokNameKey"),
            IsEstimateCurrentEvent=json_data.get("IsEstimateCurrentEvent"),
            IsKeepTimeKey=json_data.get("IsKeepTimeKey"),
            IsNullEmptyString=json_data.get("IsNullEmptyString"),
            IsSupportColonlessIdent=json_data.get("IsSupportColonlessIdent"),
            IsWithPriority=json_data.get("IsWithPriority"),
            Keys=json_data.get("Keys"),
            MessageFormat=json_data.get("MessageFormat"),
            MessageKey=json_data.get("MessageKey"),
            MultiLineStartRegexp=json_data.get("MultiLineStartRegexp"),
            NullValuePattern=json_data.get("NullValuePattern"),
            ParserType=json_data.get("ParserType"),
            Rfc5424timeFormat=json_data.get("Rfc5424timeFormat"),
            SyslogParserType=json_data.get("SyslogParserType"),
            TimeFormat=json_data.get("TimeFormat"),
            TimeType=json_data.get("TimeType"),
            TimeoutInMilliseconds=json_data.get("TimeoutInMilliseconds"),
            Types=deserialize_list(json_data.get("Types"), TypesDefinition),
            Patterns=deserialize_list(json_data.get("Patterns"), PatternsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParserDefinition = ParserDefinition


@dataclass
class TypesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TypesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TypesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TypesDefinition = TypesDefinition


@dataclass
class PatternsDefinition(BaseModel):
    FieldTimeFormat: Optional[str]
    FieldTimeKey: Optional[str]
    FieldTimeZone: Optional[str]
    Name: Optional[str]
    Pattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PatternsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PatternsDefinition"]:
        if not json_data:
            return None
        return cls(
            FieldTimeFormat=json_data.get("FieldTimeFormat"),
            FieldTimeKey=json_data.get("FieldTimeKey"),
            FieldTimeZone=json_data.get("FieldTimeZone"),
            Name=json_data.get("Name"),
            Pattern=json_data.get("Pattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PatternsDefinition = PatternsDefinition


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


