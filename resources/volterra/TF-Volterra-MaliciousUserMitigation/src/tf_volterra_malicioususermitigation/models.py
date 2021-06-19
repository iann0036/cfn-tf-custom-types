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
    Description: Optional[str]
    Disable: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    MitigationType: Optional[Sequence["_MitigationTypeDefinition"]]

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
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            MitigationType=deserialize_list(json_data.get("MitigationType"), MitigationTypeDefinition),
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
class MitigationTypeDefinition(BaseModel):
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MitigationTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MitigationTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MitigationTypeDefinition = MitigationTypeDefinition


@dataclass
class RulesDefinition(BaseModel):
    MitigationAction: Optional[Sequence["_MitigationActionDefinition"]]
    ThreatLevel: Optional[Sequence["_ThreatLevelDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            MitigationAction=deserialize_list(json_data.get("MitigationAction"), MitigationActionDefinition),
            ThreatLevel=deserialize_list(json_data.get("ThreatLevel"), ThreatLevelDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class MitigationActionDefinition(BaseModel):
    AlertOnly: Optional[bool]
    BlockTemporarily: Optional[bool]
    CaptchaChallenge: Optional[bool]
    JavascriptChallenge: Optional[bool]
    None: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MitigationActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MitigationActionDefinition"]:
        if not json_data:
            return None
        return cls(
            AlertOnly=json_data.get("AlertOnly"),
            BlockTemporarily=json_data.get("BlockTemporarily"),
            CaptchaChallenge=json_data.get("CaptchaChallenge"),
            JavascriptChallenge=json_data.get("JavascriptChallenge"),
            None=json_data.get("None"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MitigationActionDefinition = MitigationActionDefinition


@dataclass
class ThreatLevelDefinition(BaseModel):
    High: Optional[bool]
    Low: Optional[bool]
    Medium: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ThreatLevelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreatLevelDefinition"]:
        if not json_data:
            return None
        return cls(
            High=json_data.get("High"),
            Low=json_data.get("Low"),
            Medium=json_data.get("Medium"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreatLevelDefinition = ThreatLevelDefinition


