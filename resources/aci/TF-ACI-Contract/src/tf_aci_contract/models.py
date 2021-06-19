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
    FilterEntryIds: Optional[Sequence[str]]
    FilterIds: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    Prio: Optional[str]
    RelationVzRsGraphAtt: Optional[str]
    Scope: Optional[str]
    TargetDscp: Optional[str]
    TenantDn: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

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
            FilterEntryIds=json_data.get("FilterEntryIds"),
            FilterIds=json_data.get("FilterIds"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            Prio=json_data.get("Prio"),
            RelationVzRsGraphAtt=json_data.get("RelationVzRsGraphAtt"),
            Scope=json_data.get("Scope"),
            TargetDscp=json_data.get("TargetDscp"),
            TenantDn=json_data.get("TenantDn"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FilterDefinition(BaseModel):
    Annotation: Optional[str]
    Description: Optional[str]
    FilterName: Optional[str]
    NameAlias: Optional[str]
    FilterEntry: Optional[Sequence["_FilterEntryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Annotation=json_data.get("Annotation"),
            Description=json_data.get("Description"),
            FilterName=json_data.get("FilterName"),
            NameAlias=json_data.get("NameAlias"),
            FilterEntry=deserialize_list(json_data.get("FilterEntry"), FilterEntryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class FilterEntryDefinition(BaseModel):
    ApplyToFrag: Optional[str]
    ArpOpc: Optional[str]
    DFromPort: Optional[str]
    DToPort: Optional[str]
    EntryAnnotation: Optional[str]
    EntryDescription: Optional[str]
    EntryNameAlias: Optional[str]
    EtherT: Optional[str]
    FilterEntryName: Optional[str]
    Icmpv4T: Optional[str]
    Icmpv6T: Optional[str]
    MatchDscp: Optional[str]
    Prot: Optional[str]
    SFromPort: Optional[str]
    SToPort: Optional[str]
    Stateful: Optional[str]
    TcpRules: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterEntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterEntryDefinition"]:
        if not json_data:
            return None
        return cls(
            ApplyToFrag=json_data.get("ApplyToFrag"),
            ArpOpc=json_data.get("ArpOpc"),
            DFromPort=json_data.get("DFromPort"),
            DToPort=json_data.get("DToPort"),
            EntryAnnotation=json_data.get("EntryAnnotation"),
            EntryDescription=json_data.get("EntryDescription"),
            EntryNameAlias=json_data.get("EntryNameAlias"),
            EtherT=json_data.get("EtherT"),
            FilterEntryName=json_data.get("FilterEntryName"),
            Icmpv4T=json_data.get("Icmpv4T"),
            Icmpv6T=json_data.get("Icmpv6T"),
            MatchDscp=json_data.get("MatchDscp"),
            Prot=json_data.get("Prot"),
            SFromPort=json_data.get("SFromPort"),
            SToPort=json_data.get("SToPort"),
            Stateful=json_data.get("Stateful"),
            TcpRules=json_data.get("TcpRules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterEntryDefinition = FilterEntryDefinition


