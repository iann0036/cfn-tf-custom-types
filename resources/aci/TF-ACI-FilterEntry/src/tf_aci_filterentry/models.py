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
    ApplyToFrag: Optional[str]
    ArpOpc: Optional[str]
    DFromPort: Optional[str]
    DToPort: Optional[str]
    Description: Optional[str]
    EtherT: Optional[str]
    FilterDn: Optional[str]
    Icmpv4T: Optional[str]
    Icmpv6T: Optional[str]
    Id: Optional[str]
    MatchDscp: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    Prot: Optional[str]
    SFromPort: Optional[str]
    SToPort: Optional[str]
    Stateful: Optional[str]
    TcpRules: Optional[str]

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
            ApplyToFrag=json_data.get("ApplyToFrag"),
            ArpOpc=json_data.get("ArpOpc"),
            DFromPort=json_data.get("DFromPort"),
            DToPort=json_data.get("DToPort"),
            Description=json_data.get("Description"),
            EtherT=json_data.get("EtherT"),
            FilterDn=json_data.get("FilterDn"),
            Icmpv4T=json_data.get("Icmpv4T"),
            Icmpv6T=json_data.get("Icmpv6T"),
            Id=json_data.get("Id"),
            MatchDscp=json_data.get("MatchDscp"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            Prot=json_data.get("Prot"),
            SFromPort=json_data.get("SFromPort"),
            SToPort=json_data.get("SToPort"),
            Stateful=json_data.get("Stateful"),
            TcpRules=json_data.get("TcpRules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


