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
    Aggregation: Optional[str]
    Confidential: Optional[bool]
    DataType: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Normalization: Optional[str]
    SkipPersonalDataMasking: Optional[bool]
    Unknowns: Optional[str]
    DataSources: Optional[Sequence["_DataSourcesDefinition"]]

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
            Aggregation=json_data.get("Aggregation"),
            Confidential=json_data.get("Confidential"),
            DataType=json_data.get("DataType"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Normalization=json_data.get("Normalization"),
            SkipPersonalDataMasking=json_data.get("SkipPersonalDataMasking"),
            Unknowns=json_data.get("Unknowns"),
            DataSources=deserialize_list(json_data.get("DataSources"), DataSourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DataSourcesDefinition(BaseModel):
    CapturingAndStorageLocation: Optional[str]
    Enabled: Optional[bool]
    IibNodeType: Optional[str]
    ParameterName: Optional[str]
    SessionAttributeTechnology: Optional[str]
    Source: Optional[str]
    Technology: Optional[str]
    Unknowns: Optional[str]
    CicsSdkMethodNodeCondition: Optional[Sequence["_CicsSdkMethodNodeConditionDefinition"]]
    IibLabelMethodNodeCondition: Optional[Sequence["_IibLabelMethodNodeConditionDefinition"]]
    IibMethodNodeCondition: Optional[Sequence["_IibMethodNodeConditionDefinition"]]
    Methods: Optional[Sequence["_MethodsDefinition"]]
    Scope: Optional[Sequence["_ScopeDefinition"]]
    ValueProcessing: Optional[Sequence["_ValueProcessingDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DataSourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            CapturingAndStorageLocation=json_data.get("CapturingAndStorageLocation"),
            Enabled=json_data.get("Enabled"),
            IibNodeType=json_data.get("IibNodeType"),
            ParameterName=json_data.get("ParameterName"),
            SessionAttributeTechnology=json_data.get("SessionAttributeTechnology"),
            Source=json_data.get("Source"),
            Technology=json_data.get("Technology"),
            Unknowns=json_data.get("Unknowns"),
            CicsSdkMethodNodeCondition=deserialize_list(json_data.get("CicsSdkMethodNodeCondition"), CicsSdkMethodNodeConditionDefinition),
            IibLabelMethodNodeCondition=deserialize_list(json_data.get("IibLabelMethodNodeCondition"), IibLabelMethodNodeConditionDefinition),
            IibMethodNodeCondition=deserialize_list(json_data.get("IibMethodNodeCondition"), IibMethodNodeConditionDefinition),
            Methods=deserialize_list(json_data.get("Methods"), MethodsDefinition),
            Scope=deserialize_list(json_data.get("Scope"), ScopeDefinition),
            ValueProcessing=deserialize_list(json_data.get("ValueProcessing"), ValueProcessingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSourcesDefinition = DataSourcesDefinition


@dataclass
class CicsSdkMethodNodeConditionDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CicsSdkMethodNodeConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CicsSdkMethodNodeConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CicsSdkMethodNodeConditionDefinition = CicsSdkMethodNodeConditionDefinition


@dataclass
class IibLabelMethodNodeConditionDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IibLabelMethodNodeConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IibLabelMethodNodeConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IibLabelMethodNodeConditionDefinition = IibLabelMethodNodeConditionDefinition


@dataclass
class IibMethodNodeConditionDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IibMethodNodeConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IibMethodNodeConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IibMethodNodeConditionDefinition = IibMethodNodeConditionDefinition


@dataclass
class MethodsDefinition(BaseModel):
    ArgumentIndex: Optional[float]
    Capture: Optional[str]
    DeepObjectAccess: Optional[str]
    Unknowns: Optional[str]
    Method: Optional[Sequence["_MethodDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MethodsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MethodsDefinition"]:
        if not json_data:
            return None
        return cls(
            ArgumentIndex=json_data.get("ArgumentIndex"),
            Capture=json_data.get("Capture"),
            DeepObjectAccess=json_data.get("DeepObjectAccess"),
            Unknowns=json_data.get("Unknowns"),
            Method=deserialize_list(json_data.get("Method"), MethodDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MethodsDefinition = MethodsDefinition


@dataclass
class MethodDefinition(BaseModel):
    ArgumentTypes: Optional[Sequence[str]]
    ClassName: Optional[str]
    FileName: Optional[str]
    FileNameMatcher: Optional[str]
    MethodName: Optional[str]
    Modifiers: Optional[Sequence[str]]
    ReturnType: Optional[str]
    Unknowns: Optional[str]
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MethodDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MethodDefinition"]:
        if not json_data:
            return None
        return cls(
            ArgumentTypes=json_data.get("ArgumentTypes"),
            ClassName=json_data.get("ClassName"),
            FileName=json_data.get("FileName"),
            FileNameMatcher=json_data.get("FileNameMatcher"),
            MethodName=json_data.get("MethodName"),
            Modifiers=json_data.get("Modifiers"),
            ReturnType=json_data.get("ReturnType"),
            Unknowns=json_data.get("Unknowns"),
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MethodDefinition = MethodDefinition


@dataclass
class ScopeDefinition(BaseModel):
    HostGroup: Optional[str]
    ProcessGroup: Optional[str]
    ServiceTechnology: Optional[str]
    TagOfProcessGroup: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScopeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScopeDefinition"]:
        if not json_data:
            return None
        return cls(
            HostGroup=json_data.get("HostGroup"),
            ProcessGroup=json_data.get("ProcessGroup"),
            ServiceTechnology=json_data.get("ServiceTechnology"),
            TagOfProcessGroup=json_data.get("TagOfProcessGroup"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScopeDefinition = ScopeDefinition


@dataclass
class ValueProcessingDefinition(BaseModel):
    SplitAt: Optional[str]
    Trim: Optional[bool]
    Unknowns: Optional[str]
    ValueExtractorRegex: Optional[str]
    ExtractSubstring: Optional[Sequence["_ExtractSubstringDefinition"]]
    ValueCondition: Optional[Sequence["_ValueConditionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ValueProcessingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueProcessingDefinition"]:
        if not json_data:
            return None
        return cls(
            SplitAt=json_data.get("SplitAt"),
            Trim=json_data.get("Trim"),
            Unknowns=json_data.get("Unknowns"),
            ValueExtractorRegex=json_data.get("ValueExtractorRegex"),
            ExtractSubstring=deserialize_list(json_data.get("ExtractSubstring"), ExtractSubstringDefinition),
            ValueCondition=deserialize_list(json_data.get("ValueCondition"), ValueConditionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueProcessingDefinition = ValueProcessingDefinition


@dataclass
class ExtractSubstringDefinition(BaseModel):
    Delimiter: Optional[str]
    EndDelimiter: Optional[str]
    Position: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtractSubstringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtractSubstringDefinition"]:
        if not json_data:
            return None
        return cls(
            Delimiter=json_data.get("Delimiter"),
            EndDelimiter=json_data.get("EndDelimiter"),
            Position=json_data.get("Position"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtractSubstringDefinition = ExtractSubstringDefinition


@dataclass
class ValueConditionDefinition(BaseModel):
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValueConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueConditionDefinition = ValueConditionDefinition


