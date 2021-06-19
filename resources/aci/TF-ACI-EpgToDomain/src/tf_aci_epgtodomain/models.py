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
    AllowMicroSeg: Optional[bool]
    Annotation: Optional[str]
    ApplicationEpgDn: Optional[str]
    BindingType: Optional[str]
    Delimiter: Optional[str]
    Description: Optional[str]
    Encap: Optional[str]
    EncapMode: Optional[str]
    EpgCos: Optional[str]
    EpgCosPref: Optional[str]
    Id: Optional[str]
    InstrImedcy: Optional[str]
    LagPolicyName: Optional[str]
    NetflowDir: Optional[str]
    NetflowPref: Optional[str]
    NumPorts: Optional[str]
    PortAllocation: Optional[str]
    PrimaryEncap: Optional[str]
    PrimaryEncapInner: Optional[str]
    ResImedcy: Optional[str]
    SecondaryEncapInner: Optional[str]
    SwitchingMode: Optional[str]
    Tdn: Optional[str]
    VmmAllowPromiscuous: Optional[str]
    VmmForgedTransmits: Optional[str]
    VmmId: Optional[str]
    VmmMacChanges: Optional[str]

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
            AllowMicroSeg=json_data.get("AllowMicroSeg"),
            Annotation=json_data.get("Annotation"),
            ApplicationEpgDn=json_data.get("ApplicationEpgDn"),
            BindingType=json_data.get("BindingType"),
            Delimiter=json_data.get("Delimiter"),
            Description=json_data.get("Description"),
            Encap=json_data.get("Encap"),
            EncapMode=json_data.get("EncapMode"),
            EpgCos=json_data.get("EpgCos"),
            EpgCosPref=json_data.get("EpgCosPref"),
            Id=json_data.get("Id"),
            InstrImedcy=json_data.get("InstrImedcy"),
            LagPolicyName=json_data.get("LagPolicyName"),
            NetflowDir=json_data.get("NetflowDir"),
            NetflowPref=json_data.get("NetflowPref"),
            NumPorts=json_data.get("NumPorts"),
            PortAllocation=json_data.get("PortAllocation"),
            PrimaryEncap=json_data.get("PrimaryEncap"),
            PrimaryEncapInner=json_data.get("PrimaryEncapInner"),
            ResImedcy=json_data.get("ResImedcy"),
            SecondaryEncapInner=json_data.get("SecondaryEncapInner"),
            SwitchingMode=json_data.get("SwitchingMode"),
            Tdn=json_data.get("Tdn"),
            VmmAllowPromiscuous=json_data.get("VmmAllowPromiscuous"),
            VmmForgedTransmits=json_data.get("VmmForgedTransmits"),
            VmmId=json_data.get("VmmId"),
            VmmMacChanges=json_data.get("VmmMacChanges"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


