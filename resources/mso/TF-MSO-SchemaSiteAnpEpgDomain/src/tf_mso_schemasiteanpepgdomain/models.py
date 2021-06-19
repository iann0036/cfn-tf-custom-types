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
    AllowMicroSegmentation: Optional[bool]
    AnpName: Optional[str]
    DeployImmediacy: Optional[str]
    Dn: Optional[str]
    DomainType: Optional[str]
    EnhancedLagPolicyDn: Optional[str]
    EnhancedLagPolicyName: Optional[str]
    EpgName: Optional[str]
    Id: Optional[str]
    MicroSegVlan: Optional[float]
    MicroSegVlanType: Optional[str]
    PortEncapVlan: Optional[float]
    PortEncapVlanType: Optional[str]
    ResolutionImmediacy: Optional[str]
    SchemaId: Optional[str]
    SiteId: Optional[str]
    SwitchType: Optional[str]
    SwitchingMode: Optional[str]
    TemplateName: Optional[str]
    VlanEncapMode: Optional[str]

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
            AllowMicroSegmentation=json_data.get("AllowMicroSegmentation"),
            AnpName=json_data.get("AnpName"),
            DeployImmediacy=json_data.get("DeployImmediacy"),
            Dn=json_data.get("Dn"),
            DomainType=json_data.get("DomainType"),
            EnhancedLagPolicyDn=json_data.get("EnhancedLagPolicyDn"),
            EnhancedLagPolicyName=json_data.get("EnhancedLagPolicyName"),
            EpgName=json_data.get("EpgName"),
            Id=json_data.get("Id"),
            MicroSegVlan=json_data.get("MicroSegVlan"),
            MicroSegVlanType=json_data.get("MicroSegVlanType"),
            PortEncapVlan=json_data.get("PortEncapVlan"),
            PortEncapVlanType=json_data.get("PortEncapVlanType"),
            ResolutionImmediacy=json_data.get("ResolutionImmediacy"),
            SchemaId=json_data.get("SchemaId"),
            SiteId=json_data.get("SiteId"),
            SwitchType=json_data.get("SwitchType"),
            SwitchingMode=json_data.get("SwitchingMode"),
            TemplateName=json_data.get("TemplateName"),
            VlanEncapMode=json_data.get("VlanEncapMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


