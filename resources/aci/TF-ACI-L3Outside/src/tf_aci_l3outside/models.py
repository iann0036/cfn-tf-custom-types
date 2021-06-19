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
    EnforceRtctrl: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    RelationL3extRsEctx: Optional[str]
    RelationL3extRsInterleakPol: Optional[str]
    RelationL3extRsL3DomAtt: Optional[str]
    RelationL3extRsOutToBdPublicSubnetHolder: Optional[Sequence[str]]
    TargetDscp: Optional[str]
    TenantDn: Optional[str]
    RelationL3extRsDampeningPol: Optional[Sequence["_RelationL3extRsDampeningPolDefinition"]]

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
            EnforceRtctrl=json_data.get("EnforceRtctrl"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            RelationL3extRsEctx=json_data.get("RelationL3extRsEctx"),
            RelationL3extRsInterleakPol=json_data.get("RelationL3extRsInterleakPol"),
            RelationL3extRsL3DomAtt=json_data.get("RelationL3extRsL3DomAtt"),
            RelationL3extRsOutToBdPublicSubnetHolder=json_data.get("RelationL3extRsOutToBdPublicSubnetHolder"),
            TargetDscp=json_data.get("TargetDscp"),
            TenantDn=json_data.get("TenantDn"),
            RelationL3extRsDampeningPol=deserialize_list(json_data.get("RelationL3extRsDampeningPol"), RelationL3extRsDampeningPolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RelationL3extRsDampeningPolDefinition(BaseModel):
    Af: Optional[str]
    TnRtctrlProfileName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationL3extRsDampeningPolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationL3extRsDampeningPolDefinition"]:
        if not json_data:
            return None
        return cls(
            Af=json_data.get("Af"),
            TnRtctrlProfileName=json_data.get("TnRtctrlProfileName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationL3extRsDampeningPolDefinition = RelationL3extRsDampeningPolDefinition


