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
    ArpFlag: Optional[str]
    DestinationFrom: Optional[str]
    DestinationTo: Optional[str]
    DisplayName: Optional[str]
    EntryDescription: Optional[str]
    EntryDisplayName: Optional[str]
    EntryName: Optional[str]
    EtherType: Optional[str]
    Id: Optional[str]
    IpProtocol: Optional[str]
    MatchOnlyFragments: Optional[bool]
    Name: Optional[str]
    SchemaId: Optional[str]
    SourceFrom: Optional[str]
    SourceTo: Optional[str]
    Stateful: Optional[bool]
    TcpSessionRules: Optional[Sequence[str]]
    TemplateName: Optional[str]

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
            ArpFlag=json_data.get("ArpFlag"),
            DestinationFrom=json_data.get("DestinationFrom"),
            DestinationTo=json_data.get("DestinationTo"),
            DisplayName=json_data.get("DisplayName"),
            EntryDescription=json_data.get("EntryDescription"),
            EntryDisplayName=json_data.get("EntryDisplayName"),
            EntryName=json_data.get("EntryName"),
            EtherType=json_data.get("EtherType"),
            Id=json_data.get("Id"),
            IpProtocol=json_data.get("IpProtocol"),
            MatchOnlyFragments=json_data.get("MatchOnlyFragments"),
            Name=json_data.get("Name"),
            SchemaId=json_data.get("SchemaId"),
            SourceFrom=json_data.get("SourceFrom"),
            SourceTo=json_data.get("SourceTo"),
            Stateful=json_data.get("Stateful"),
            TcpSessionRules=json_data.get("TcpSessionRules"),
            TemplateName=json_data.get("TemplateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


