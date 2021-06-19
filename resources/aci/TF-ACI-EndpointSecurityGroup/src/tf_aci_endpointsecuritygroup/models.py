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
    Annotation: Optional[str]
    ApplicationProfileDn: Optional[str]
    Description: Optional[str]
    FloodOnEncap: Optional[str]
    Id: Optional[str]
    MatchT: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    PcEnfPref: Optional[str]
    PrefGrMemb: Optional[str]
    Prio: Optional[str]
    RelationFvRsCustQosPol: Optional[str]
    RelationFvRsIntraEpg: Optional[Sequence[str]]
    RelationFvRsProtBy: Optional[Sequence[str]]
    RelationFvRsScope: Optional[str]
    RelationFvRsSecInherited: Optional[Sequence[str]]
    RelationFvRsCons: Optional[Sequence["_RelationFvRsConsDefinition"]]
    RelationFvRsConsIf: Optional[Sequence["_RelationFvRsConsIfDefinition"]]
    RelationFvRsProv: Optional[Sequence["_RelationFvRsProvDefinition"]]

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
            Annotation=json_data.get("Annotation"),
            ApplicationProfileDn=json_data.get("ApplicationProfileDn"),
            Description=json_data.get("Description"),
            FloodOnEncap=json_data.get("FloodOnEncap"),
            Id=json_data.get("Id"),
            MatchT=json_data.get("MatchT"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            PcEnfPref=json_data.get("PcEnfPref"),
            PrefGrMemb=json_data.get("PrefGrMemb"),
            Prio=json_data.get("Prio"),
            RelationFvRsCustQosPol=json_data.get("RelationFvRsCustQosPol"),
            RelationFvRsIntraEpg=json_data.get("RelationFvRsIntraEpg"),
            RelationFvRsProtBy=json_data.get("RelationFvRsProtBy"),
            RelationFvRsScope=json_data.get("RelationFvRsScope"),
            RelationFvRsSecInherited=json_data.get("RelationFvRsSecInherited"),
            RelationFvRsCons=deserialize_list(json_data.get("RelationFvRsCons"), RelationFvRsConsDefinition),
            RelationFvRsConsIf=deserialize_list(json_data.get("RelationFvRsConsIf"), RelationFvRsConsIfDefinition),
            RelationFvRsProv=deserialize_list(json_data.get("RelationFvRsProv"), RelationFvRsProvDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RelationFvRsConsDefinition(BaseModel):
    Prio: Optional[str]
    TargetDn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationFvRsConsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationFvRsConsDefinition"]:
        if not json_data:
            return None
        return cls(
            Prio=json_data.get("Prio"),
            TargetDn=json_data.get("TargetDn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationFvRsConsDefinition = RelationFvRsConsDefinition


@dataclass
class RelationFvRsConsIfDefinition(BaseModel):
    Prio: Optional[str]
    TargetDn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationFvRsConsIfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationFvRsConsIfDefinition"]:
        if not json_data:
            return None
        return cls(
            Prio=json_data.get("Prio"),
            TargetDn=json_data.get("TargetDn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationFvRsConsIfDefinition = RelationFvRsConsIfDefinition


@dataclass
class RelationFvRsProvDefinition(BaseModel):
    MatchT: Optional[str]
    Prio: Optional[str]
    TargetDn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationFvRsProvDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationFvRsProvDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchT=json_data.get("MatchT"),
            Prio=json_data.get("Prio"),
            TargetDn=json_data.get("TargetDn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationFvRsProvDefinition = RelationFvRsProvDefinition


