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
    ExceptionTag: Optional[str]
    FloodOnEncap: Optional[str]
    FwdCtrl: Optional[str]
    HasMcastSource: Optional[str]
    Id: Optional[str]
    IsAttrBasedEpg: Optional[str]
    MatchT: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    PcEnfPref: Optional[str]
    PrefGrMemb: Optional[str]
    Prio: Optional[str]
    RelationFvRsAepgMonPol: Optional[str]
    RelationFvRsBd: Optional[str]
    RelationFvRsCons: Optional[Sequence[str]]
    RelationFvRsConsIf: Optional[Sequence[str]]
    RelationFvRsCustQosPol: Optional[str]
    RelationFvRsDppPol: Optional[str]
    RelationFvRsFcPathAtt: Optional[Sequence[str]]
    RelationFvRsGraphDef: Optional[Sequence[str]]
    RelationFvRsIntraEpg: Optional[Sequence[str]]
    RelationFvRsNodeAtt: Optional[Sequence[str]]
    RelationFvRsProtBy: Optional[Sequence[str]]
    RelationFvRsProv: Optional[Sequence[str]]
    RelationFvRsProvDef: Optional[Sequence[str]]
    RelationFvRsSecInherited: Optional[Sequence[str]]
    RelationFvRsTrustCtrl: Optional[str]
    Shutdown: Optional[str]

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
            ExceptionTag=json_data.get("ExceptionTag"),
            FloodOnEncap=json_data.get("FloodOnEncap"),
            FwdCtrl=json_data.get("FwdCtrl"),
            HasMcastSource=json_data.get("HasMcastSource"),
            Id=json_data.get("Id"),
            IsAttrBasedEpg=json_data.get("IsAttrBasedEpg"),
            MatchT=json_data.get("MatchT"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            PcEnfPref=json_data.get("PcEnfPref"),
            PrefGrMemb=json_data.get("PrefGrMemb"),
            Prio=json_data.get("Prio"),
            RelationFvRsAepgMonPol=json_data.get("RelationFvRsAepgMonPol"),
            RelationFvRsBd=json_data.get("RelationFvRsBd"),
            RelationFvRsCons=json_data.get("RelationFvRsCons"),
            RelationFvRsConsIf=json_data.get("RelationFvRsConsIf"),
            RelationFvRsCustQosPol=json_data.get("RelationFvRsCustQosPol"),
            RelationFvRsDppPol=json_data.get("RelationFvRsDppPol"),
            RelationFvRsFcPathAtt=json_data.get("RelationFvRsFcPathAtt"),
            RelationFvRsGraphDef=json_data.get("RelationFvRsGraphDef"),
            RelationFvRsIntraEpg=json_data.get("RelationFvRsIntraEpg"),
            RelationFvRsNodeAtt=json_data.get("RelationFvRsNodeAtt"),
            RelationFvRsProtBy=json_data.get("RelationFvRsProtBy"),
            RelationFvRsProv=json_data.get("RelationFvRsProv"),
            RelationFvRsProvDef=json_data.get("RelationFvRsProvDef"),
            RelationFvRsSecInherited=json_data.get("RelationFvRsSecInherited"),
            RelationFvRsTrustCtrl=json_data.get("RelationFvRsTrustCtrl"),
            Shutdown=json_data.get("Shutdown"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


