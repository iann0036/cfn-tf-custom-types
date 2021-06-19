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
    Id: Optional[str]
    NameAlias: Optional[str]
    RelationVmmRsVswitchOverrideCdpIfPol: Optional[str]
    RelationVmmRsVswitchOverrideFwPol: Optional[str]
    RelationVmmRsVswitchOverrideLacpPol: Optional[str]
    RelationVmmRsVswitchOverrideLldpIfPol: Optional[str]
    RelationVmmRsVswitchOverrideMcpIfPol: Optional[str]
    RelationVmmRsVswitchOverrideMtuPol: Optional[str]
    RelationVmmRsVswitchOverrideStpPol: Optional[str]
    VmmDomainDn: Optional[str]
    RelationVmmRsVswitchExporterPol: Optional[Sequence["_RelationVmmRsVswitchExporterPolDefinition"]]

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
            Id=json_data.get("Id"),
            NameAlias=json_data.get("NameAlias"),
            RelationVmmRsVswitchOverrideCdpIfPol=json_data.get("RelationVmmRsVswitchOverrideCdpIfPol"),
            RelationVmmRsVswitchOverrideFwPol=json_data.get("RelationVmmRsVswitchOverrideFwPol"),
            RelationVmmRsVswitchOverrideLacpPol=json_data.get("RelationVmmRsVswitchOverrideLacpPol"),
            RelationVmmRsVswitchOverrideLldpIfPol=json_data.get("RelationVmmRsVswitchOverrideLldpIfPol"),
            RelationVmmRsVswitchOverrideMcpIfPol=json_data.get("RelationVmmRsVswitchOverrideMcpIfPol"),
            RelationVmmRsVswitchOverrideMtuPol=json_data.get("RelationVmmRsVswitchOverrideMtuPol"),
            RelationVmmRsVswitchOverrideStpPol=json_data.get("RelationVmmRsVswitchOverrideStpPol"),
            VmmDomainDn=json_data.get("VmmDomainDn"),
            RelationVmmRsVswitchExporterPol=deserialize_list(json_data.get("RelationVmmRsVswitchExporterPol"), RelationVmmRsVswitchExporterPolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RelationVmmRsVswitchExporterPolDefinition(BaseModel):
    ActiveFlowTimeOut: Optional[str]
    IdleFlowTimeOut: Optional[str]
    SamplingRate: Optional[str]
    TargetDn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationVmmRsVswitchExporterPolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationVmmRsVswitchExporterPolDefinition"]:
        if not json_data:
            return None
        return cls(
            ActiveFlowTimeOut=json_data.get("ActiveFlowTimeOut"),
            IdleFlowTimeOut=json_data.get("IdleFlowTimeOut"),
            SamplingRate=json_data.get("SamplingRate"),
            TargetDn=json_data.get("TargetDn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationVmmRsVswitchExporterPolDefinition = RelationVmmRsVswitchExporterPolDefinition


