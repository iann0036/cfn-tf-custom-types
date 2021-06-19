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
    Name: Optional[str]
    NameAlias: Optional[str]
    RelationInfraRsAttEntP: Optional[str]
    RelationInfraRsCdpIfPol: Optional[str]
    RelationInfraRsCoppIfPol: Optional[str]
    RelationInfraRsDwdmIfPol: Optional[str]
    RelationInfraRsFcIfPol: Optional[str]
    RelationInfraRsHIfPol: Optional[str]
    RelationInfraRsL2IfPol: Optional[str]
    RelationInfraRsL2InstPol: Optional[str]
    RelationInfraRsL2PortAuthPol: Optional[str]
    RelationInfraRsL2PortSecurityPol: Optional[str]
    RelationInfraRsLldpIfPol: Optional[str]
    RelationInfraRsMacsecIfPol: Optional[str]
    RelationInfraRsMcpIfPol: Optional[str]
    RelationInfraRsMonIfInfraPol: Optional[str]
    RelationInfraRsPoeIfPol: Optional[str]
    RelationInfraRsQosDppIfPol: Optional[str]
    RelationInfraRsQosEgressDppIfPol: Optional[str]
    RelationInfraRsQosIngressDppIfPol: Optional[str]
    RelationInfraRsQosPfcIfPol: Optional[str]
    RelationInfraRsQosSdIfPol: Optional[str]
    RelationInfraRsSpanVDestGrp: Optional[Sequence[str]]
    RelationInfraRsSpanVSrcGrp: Optional[Sequence[str]]
    RelationInfraRsStormctrlIfPol: Optional[str]
    RelationInfraRsStpIfPol: Optional[str]
    RelationInfraRsNetflowMonitorPol: Optional[Sequence["_RelationInfraRsNetflowMonitorPolDefinition"]]

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
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            RelationInfraRsAttEntP=json_data.get("RelationInfraRsAttEntP"),
            RelationInfraRsCdpIfPol=json_data.get("RelationInfraRsCdpIfPol"),
            RelationInfraRsCoppIfPol=json_data.get("RelationInfraRsCoppIfPol"),
            RelationInfraRsDwdmIfPol=json_data.get("RelationInfraRsDwdmIfPol"),
            RelationInfraRsFcIfPol=json_data.get("RelationInfraRsFcIfPol"),
            RelationInfraRsHIfPol=json_data.get("RelationInfraRsHIfPol"),
            RelationInfraRsL2IfPol=json_data.get("RelationInfraRsL2IfPol"),
            RelationInfraRsL2InstPol=json_data.get("RelationInfraRsL2InstPol"),
            RelationInfraRsL2PortAuthPol=json_data.get("RelationInfraRsL2PortAuthPol"),
            RelationInfraRsL2PortSecurityPol=json_data.get("RelationInfraRsL2PortSecurityPol"),
            RelationInfraRsLldpIfPol=json_data.get("RelationInfraRsLldpIfPol"),
            RelationInfraRsMacsecIfPol=json_data.get("RelationInfraRsMacsecIfPol"),
            RelationInfraRsMcpIfPol=json_data.get("RelationInfraRsMcpIfPol"),
            RelationInfraRsMonIfInfraPol=json_data.get("RelationInfraRsMonIfInfraPol"),
            RelationInfraRsPoeIfPol=json_data.get("RelationInfraRsPoeIfPol"),
            RelationInfraRsQosDppIfPol=json_data.get("RelationInfraRsQosDppIfPol"),
            RelationInfraRsQosEgressDppIfPol=json_data.get("RelationInfraRsQosEgressDppIfPol"),
            RelationInfraRsQosIngressDppIfPol=json_data.get("RelationInfraRsQosIngressDppIfPol"),
            RelationInfraRsQosPfcIfPol=json_data.get("RelationInfraRsQosPfcIfPol"),
            RelationInfraRsQosSdIfPol=json_data.get("RelationInfraRsQosSdIfPol"),
            RelationInfraRsSpanVDestGrp=json_data.get("RelationInfraRsSpanVDestGrp"),
            RelationInfraRsSpanVSrcGrp=json_data.get("RelationInfraRsSpanVSrcGrp"),
            RelationInfraRsStormctrlIfPol=json_data.get("RelationInfraRsStormctrlIfPol"),
            RelationInfraRsStpIfPol=json_data.get("RelationInfraRsStpIfPol"),
            RelationInfraRsNetflowMonitorPol=deserialize_list(json_data.get("RelationInfraRsNetflowMonitorPol"), RelationInfraRsNetflowMonitorPolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RelationInfraRsNetflowMonitorPolDefinition(BaseModel):
    FltType: Optional[str]
    TnNetflowMonitorPolName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationInfraRsNetflowMonitorPolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationInfraRsNetflowMonitorPolDefinition"]:
        if not json_data:
            return None
        return cls(
            FltType=json_data.get("FltType"),
            TnNetflowMonitorPolName=json_data.get("TnNetflowMonitorPolName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationInfraRsNetflowMonitorPolDefinition = RelationInfraRsNetflowMonitorPolDefinition


