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
    LogicalNodeProfileDn: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    Prio: Optional[str]
    RelationL3extRsArpIfPol: Optional[str]
    RelationL3extRsEgressQosDppPol: Optional[str]
    RelationL3extRsIngressQosDppPol: Optional[str]
    RelationL3extRsLIfPCustQosPol: Optional[str]
    RelationL3extRsNdIfPol: Optional[str]
    Tag: Optional[str]
    RelationL3extRsLIfPToNetflowMonitorPol: Optional[Sequence["_RelationL3extRsLIfPToNetflowMonitorPolDefinition"]]

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
            LogicalNodeProfileDn=json_data.get("LogicalNodeProfileDn"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            Prio=json_data.get("Prio"),
            RelationL3extRsArpIfPol=json_data.get("RelationL3extRsArpIfPol"),
            RelationL3extRsEgressQosDppPol=json_data.get("RelationL3extRsEgressQosDppPol"),
            RelationL3extRsIngressQosDppPol=json_data.get("RelationL3extRsIngressQosDppPol"),
            RelationL3extRsLIfPCustQosPol=json_data.get("RelationL3extRsLIfPCustQosPol"),
            RelationL3extRsNdIfPol=json_data.get("RelationL3extRsNdIfPol"),
            Tag=json_data.get("Tag"),
            RelationL3extRsLIfPToNetflowMonitorPol=deserialize_list(json_data.get("RelationL3extRsLIfPToNetflowMonitorPol"), RelationL3extRsLIfPToNetflowMonitorPolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RelationL3extRsLIfPToNetflowMonitorPolDefinition(BaseModel):
    FltType: Optional[str]
    TnNetflowMonitorPolName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationL3extRsLIfPToNetflowMonitorPolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationL3extRsLIfPToNetflowMonitorPolDefinition"]:
        if not json_data:
            return None
        return cls(
            FltType=json_data.get("FltType"),
            TnNetflowMonitorPolName=json_data.get("TnNetflowMonitorPolName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationL3extRsLIfPToNetflowMonitorPolDefinition = RelationL3extRsLIfPToNetflowMonitorPolDefinition


