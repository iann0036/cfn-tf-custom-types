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
    Description: Optional[str]
    Encap: Optional[str]
    ExceptionTag: Optional[str]
    FloodOnEncap: Optional[str]
    Id: Optional[str]
    ManagementProfileDn: Optional[str]
    MatchT: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    PrefGrMemb: Optional[str]
    Prio: Optional[str]
    RelationFvRsCons: Optional[Sequence[str]]
    RelationFvRsConsIf: Optional[Sequence[str]]
    RelationFvRsCustQosPol: Optional[str]
    RelationFvRsIntraEpg: Optional[Sequence[str]]
    RelationFvRsProtBy: Optional[Sequence[str]]
    RelationFvRsProv: Optional[Sequence[str]]
    RelationFvRsSecInherited: Optional[Sequence[str]]
    RelationMgmtRsInBStNode: Optional[Sequence[str]]
    RelationMgmtRsMgmtBd: Optional[str]
    RelationMgmtRsOoBCtx: Optional[str]
    RelationMgmtRsOoBProv: Optional[Sequence[str]]
    RelationMgmtRsOoBStNode: Optional[Sequence[str]]
    Type: Optional[str]

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
            Description=json_data.get("Description"),
            Encap=json_data.get("Encap"),
            ExceptionTag=json_data.get("ExceptionTag"),
            FloodOnEncap=json_data.get("FloodOnEncap"),
            Id=json_data.get("Id"),
            ManagementProfileDn=json_data.get("ManagementProfileDn"),
            MatchT=json_data.get("MatchT"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            PrefGrMemb=json_data.get("PrefGrMemb"),
            Prio=json_data.get("Prio"),
            RelationFvRsCons=json_data.get("RelationFvRsCons"),
            RelationFvRsConsIf=json_data.get("RelationFvRsConsIf"),
            RelationFvRsCustQosPol=json_data.get("RelationFvRsCustQosPol"),
            RelationFvRsIntraEpg=json_data.get("RelationFvRsIntraEpg"),
            RelationFvRsProtBy=json_data.get("RelationFvRsProtBy"),
            RelationFvRsProv=json_data.get("RelationFvRsProv"),
            RelationFvRsSecInherited=json_data.get("RelationFvRsSecInherited"),
            RelationMgmtRsInBStNode=json_data.get("RelationMgmtRsInBStNode"),
            RelationMgmtRsMgmtBd=json_data.get("RelationMgmtRsMgmtBd"),
            RelationMgmtRsOoBCtx=json_data.get("RelationMgmtRsOoBCtx"),
            RelationMgmtRsOoBProv=json_data.get("RelationMgmtRsOoBProv"),
            RelationMgmtRsOoBStNode=json_data.get("RelationMgmtRsOoBStNode"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


