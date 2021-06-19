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
    AccessMode: Optional[str]
    Annotation: Optional[str]
    ArpLearning: Optional[str]
    AveTimeOut: Optional[str]
    ConfigInfraPg: Optional[str]
    CtrlKnob: Optional[str]
    Delimiter: Optional[str]
    Description: Optional[str]
    EnableAve: Optional[str]
    EnableTag: Optional[str]
    EncapMode: Optional[str]
    EnfPref: Optional[str]
    EpInventoryType: Optional[str]
    EpRetTime: Optional[str]
    HvAvailMonitor: Optional[str]
    Id: Optional[str]
    McastAddr: Optional[str]
    Mode: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    PrefEncapMode: Optional[str]
    ProviderProfileDn: Optional[str]
    RelationInfraRsDomVxlanNsDef: Optional[str]
    RelationInfraRsVipAddrNs: Optional[str]
    RelationInfraRsVlanNs: Optional[str]
    RelationInfraRsVlanNsDef: Optional[str]
    RelationVmmRsDefaultCdpIfPol: Optional[str]
    RelationVmmRsDefaultFwPol: Optional[str]
    RelationVmmRsDefaultL2InstPol: Optional[str]
    RelationVmmRsDefaultLacpLagPol: Optional[str]
    RelationVmmRsDefaultLldpIfPol: Optional[str]
    RelationVmmRsDefaultStpIfPol: Optional[str]
    RelationVmmRsDomMcastAddrNs: Optional[str]
    RelationVmmRsPrefEnhancedLagPol: Optional[str]

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
            AccessMode=json_data.get("AccessMode"),
            Annotation=json_data.get("Annotation"),
            ArpLearning=json_data.get("ArpLearning"),
            AveTimeOut=json_data.get("AveTimeOut"),
            ConfigInfraPg=json_data.get("ConfigInfraPg"),
            CtrlKnob=json_data.get("CtrlKnob"),
            Delimiter=json_data.get("Delimiter"),
            Description=json_data.get("Description"),
            EnableAve=json_data.get("EnableAve"),
            EnableTag=json_data.get("EnableTag"),
            EncapMode=json_data.get("EncapMode"),
            EnfPref=json_data.get("EnfPref"),
            EpInventoryType=json_data.get("EpInventoryType"),
            EpRetTime=json_data.get("EpRetTime"),
            HvAvailMonitor=json_data.get("HvAvailMonitor"),
            Id=json_data.get("Id"),
            McastAddr=json_data.get("McastAddr"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            PrefEncapMode=json_data.get("PrefEncapMode"),
            ProviderProfileDn=json_data.get("ProviderProfileDn"),
            RelationInfraRsDomVxlanNsDef=json_data.get("RelationInfraRsDomVxlanNsDef"),
            RelationInfraRsVipAddrNs=json_data.get("RelationInfraRsVipAddrNs"),
            RelationInfraRsVlanNs=json_data.get("RelationInfraRsVlanNs"),
            RelationInfraRsVlanNsDef=json_data.get("RelationInfraRsVlanNsDef"),
            RelationVmmRsDefaultCdpIfPol=json_data.get("RelationVmmRsDefaultCdpIfPol"),
            RelationVmmRsDefaultFwPol=json_data.get("RelationVmmRsDefaultFwPol"),
            RelationVmmRsDefaultL2InstPol=json_data.get("RelationVmmRsDefaultL2InstPol"),
            RelationVmmRsDefaultLacpLagPol=json_data.get("RelationVmmRsDefaultLacpLagPol"),
            RelationVmmRsDefaultLldpIfPol=json_data.get("RelationVmmRsDefaultLldpIfPol"),
            RelationVmmRsDefaultStpIfPol=json_data.get("RelationVmmRsDefaultStpIfPol"),
            RelationVmmRsDomMcastAddrNs=json_data.get("RelationVmmRsDomMcastAddrNs"),
            RelationVmmRsPrefEnhancedLagPol=json_data.get("RelationVmmRsPrefEnhancedLagPol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


