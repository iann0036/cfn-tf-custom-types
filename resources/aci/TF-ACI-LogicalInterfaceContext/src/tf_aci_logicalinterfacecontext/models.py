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
    ConnNameOrLbl: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    L3Dest: Optional[str]
    LogicalDeviceContextDn: Optional[str]
    NameAlias: Optional[str]
    PermitLog: Optional[str]
    RelationVnsRsLIfCtxToBd: Optional[str]
    RelationVnsRsLIfCtxToCustQosPol: Optional[str]
    RelationVnsRsLIfCtxToInstP: Optional[str]
    RelationVnsRsLIfCtxToLIf: Optional[str]
    RelationVnsRsLIfCtxToOut: Optional[str]
    RelationVnsRsLIfCtxToOutDef: Optional[str]
    RelationVnsRsLIfCtxToSvcEPgPol: Optional[str]
    RelationVnsRsLIfCtxToSvcRedirectPol: Optional[str]

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
            ConnNameOrLbl=json_data.get("ConnNameOrLbl"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            L3Dest=json_data.get("L3Dest"),
            LogicalDeviceContextDn=json_data.get("LogicalDeviceContextDn"),
            NameAlias=json_data.get("NameAlias"),
            PermitLog=json_data.get("PermitLog"),
            RelationVnsRsLIfCtxToBd=json_data.get("RelationVnsRsLIfCtxToBd"),
            RelationVnsRsLIfCtxToCustQosPol=json_data.get("RelationVnsRsLIfCtxToCustQosPol"),
            RelationVnsRsLIfCtxToInstP=json_data.get("RelationVnsRsLIfCtxToInstP"),
            RelationVnsRsLIfCtxToLIf=json_data.get("RelationVnsRsLIfCtxToLIf"),
            RelationVnsRsLIfCtxToOut=json_data.get("RelationVnsRsLIfCtxToOut"),
            RelationVnsRsLIfCtxToOutDef=json_data.get("RelationVnsRsLIfCtxToOutDef"),
            RelationVnsRsLIfCtxToSvcEPgPol=json_data.get("RelationVnsRsLIfCtxToSvcEPgPol"),
            RelationVnsRsLIfCtxToSvcRedirectPol=json_data.get("RelationVnsRsLIfCtxToSvcRedirectPol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


