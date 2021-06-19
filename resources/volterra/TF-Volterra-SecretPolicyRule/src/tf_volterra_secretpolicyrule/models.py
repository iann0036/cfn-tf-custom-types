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
    Action: Optional[str]
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    ClientName: Optional[str]
    Description: Optional[str]
    Disable: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    ClientNameMatcher: Optional[Sequence["_ClientNameMatcherDefinition"]]
    ClientSelector: Optional[Sequence["_ClientSelectorDefinition"]]
    LabelMatcher: Optional[Sequence["_LabelMatcherDefinition"]]

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
            Action=json_data.get("Action"),
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            ClientName=json_data.get("ClientName"),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            ClientNameMatcher=deserialize_list(json_data.get("ClientNameMatcher"), ClientNameMatcherDefinition),
            ClientSelector=deserialize_list(json_data.get("ClientSelector"), ClientSelectorDefinition),
            LabelMatcher=deserialize_list(json_data.get("LabelMatcher"), LabelMatcherDefinition),
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
class ClientNameMatcherDefinition(BaseModel):
    ExactValues: Optional[Sequence[str]]
    RegexValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientNameMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientNameMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValues=json_data.get("ExactValues"),
            RegexValues=json_data.get("RegexValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientNameMatcherDefinition = ClientNameMatcherDefinition


@dataclass
class ClientSelectorDefinition(BaseModel):
    Expressions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Expressions=json_data.get("Expressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientSelectorDefinition = ClientSelectorDefinition


@dataclass
class LabelMatcherDefinition(BaseModel):
    Keys: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LabelMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            Keys=json_data.get("Keys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelMatcherDefinition = LabelMatcherDefinition


