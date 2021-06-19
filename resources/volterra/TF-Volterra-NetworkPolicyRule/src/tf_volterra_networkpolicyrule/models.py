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
    Description: Optional[str]
    Disable: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    Ports: Optional[Sequence[str]]
    Protocol: Optional[str]
    AdvancedAction: Optional[Sequence["_AdvancedActionDefinition"]]
    IpPrefixSet: Optional[Sequence["_IpPrefixSetDefinition"]]
    LabelMatcher: Optional[Sequence["_LabelMatcherDefinition"]]
    Prefix: Optional[Sequence["_PrefixDefinition"]]
    PrefixSelector: Optional[Sequence["_PrefixSelectorDefinition"]]

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
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Ports=json_data.get("Ports"),
            Protocol=json_data.get("Protocol"),
            AdvancedAction=deserialize_list(json_data.get("AdvancedAction"), AdvancedActionDefinition),
            IpPrefixSet=deserialize_list(json_data.get("IpPrefixSet"), IpPrefixSetDefinition),
            LabelMatcher=deserialize_list(json_data.get("LabelMatcher"), LabelMatcherDefinition),
            Prefix=deserialize_list(json_data.get("Prefix"), PrefixDefinition),
            PrefixSelector=deserialize_list(json_data.get("PrefixSelector"), PrefixSelectorDefinition),
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
class AdvancedActionDefinition(BaseModel):
    Action: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedActionDefinition = AdvancedActionDefinition


@dataclass
class IpPrefixSetDefinition(BaseModel):
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpPrefixSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpPrefixSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpPrefixSetDefinition = IpPrefixSetDefinition


@dataclass
class RefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RefDefinition = RefDefinition


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


@dataclass
class PrefixDefinition(BaseModel):
    Prefix: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixDefinition = PrefixDefinition


@dataclass
class PrefixSelectorDefinition(BaseModel):
    Expressions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Expressions=json_data.get("Expressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixSelectorDefinition = PrefixSelectorDefinition


