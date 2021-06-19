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
    BdEnforcedEnable: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IpDataPlaneLearning: Optional[str]
    KnwMcastAct: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    PcEnfDir: Optional[str]
    PcEnfPref: Optional[str]
    RelationFvRsBgpCtxPol: Optional[str]
    RelationFvRsCtxMcastTo: Optional[Sequence[str]]
    RelationFvRsCtxMonPol: Optional[str]
    RelationFvRsCtxToEpRet: Optional[str]
    RelationFvRsCtxToExtRouteTagPol: Optional[str]
    RelationFvRsOspfCtxPol: Optional[str]
    RelationFvRsVrfValidationPol: Optional[str]
    TenantDn: Optional[str]
    RelationFvRsCtxToBgpCtxAfPol: Optional[Sequence["_RelationFvRsCtxToBgpCtxAfPolDefinition"]]
    RelationFvRsCtxToEigrpCtxAfPol: Optional[Sequence["_RelationFvRsCtxToEigrpCtxAfPolDefinition"]]
    RelationFvRsCtxToOspfCtxPol: Optional[Sequence["_RelationFvRsCtxToOspfCtxPolDefinition"]]

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
            BdEnforcedEnable=json_data.get("BdEnforcedEnable"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IpDataPlaneLearning=json_data.get("IpDataPlaneLearning"),
            KnwMcastAct=json_data.get("KnwMcastAct"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            PcEnfDir=json_data.get("PcEnfDir"),
            PcEnfPref=json_data.get("PcEnfPref"),
            RelationFvRsBgpCtxPol=json_data.get("RelationFvRsBgpCtxPol"),
            RelationFvRsCtxMcastTo=json_data.get("RelationFvRsCtxMcastTo"),
            RelationFvRsCtxMonPol=json_data.get("RelationFvRsCtxMonPol"),
            RelationFvRsCtxToEpRet=json_data.get("RelationFvRsCtxToEpRet"),
            RelationFvRsCtxToExtRouteTagPol=json_data.get("RelationFvRsCtxToExtRouteTagPol"),
            RelationFvRsOspfCtxPol=json_data.get("RelationFvRsOspfCtxPol"),
            RelationFvRsVrfValidationPol=json_data.get("RelationFvRsVrfValidationPol"),
            TenantDn=json_data.get("TenantDn"),
            RelationFvRsCtxToBgpCtxAfPol=deserialize_list(json_data.get("RelationFvRsCtxToBgpCtxAfPol"), RelationFvRsCtxToBgpCtxAfPolDefinition),
            RelationFvRsCtxToEigrpCtxAfPol=deserialize_list(json_data.get("RelationFvRsCtxToEigrpCtxAfPol"), RelationFvRsCtxToEigrpCtxAfPolDefinition),
            RelationFvRsCtxToOspfCtxPol=deserialize_list(json_data.get("RelationFvRsCtxToOspfCtxPol"), RelationFvRsCtxToOspfCtxPolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RelationFvRsCtxToBgpCtxAfPolDefinition(BaseModel):
    Af: Optional[str]
    TnBgpCtxAfPolName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationFvRsCtxToBgpCtxAfPolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationFvRsCtxToBgpCtxAfPolDefinition"]:
        if not json_data:
            return None
        return cls(
            Af=json_data.get("Af"),
            TnBgpCtxAfPolName=json_data.get("TnBgpCtxAfPolName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationFvRsCtxToBgpCtxAfPolDefinition = RelationFvRsCtxToBgpCtxAfPolDefinition


@dataclass
class RelationFvRsCtxToEigrpCtxAfPolDefinition(BaseModel):
    Af: Optional[str]
    TnEigrpCtxAfPolName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationFvRsCtxToEigrpCtxAfPolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationFvRsCtxToEigrpCtxAfPolDefinition"]:
        if not json_data:
            return None
        return cls(
            Af=json_data.get("Af"),
            TnEigrpCtxAfPolName=json_data.get("TnEigrpCtxAfPolName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationFvRsCtxToEigrpCtxAfPolDefinition = RelationFvRsCtxToEigrpCtxAfPolDefinition


@dataclass
class RelationFvRsCtxToOspfCtxPolDefinition(BaseModel):
    Af: Optional[str]
    TnOspfCtxPolName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationFvRsCtxToOspfCtxPolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationFvRsCtxToOspfCtxPolDefinition"]:
        if not json_data:
            return None
        return cls(
            Af=json_data.get("Af"),
            TnOspfCtxPolName=json_data.get("TnOspfCtxPolName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationFvRsCtxToOspfCtxPolDefinition = RelationFvRsCtxToOspfCtxPolDefinition


