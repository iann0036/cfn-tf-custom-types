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
    AcceptReplies: Optional[bool]
    AggressiveAging: Optional[Sequence["_AggressiveAgingDefinition"]]
    Color: Optional[str]
    Comments: Optional[str]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    KeepConnectionsOpenAfterPolicyInstallation: Optional[bool]
    MatchByProtocolSignature: Optional[bool]
    MatchForAny: Optional[bool]
    Name: Optional[str]
    OverrideDefaultSettings: Optional[bool]
    Port: Optional[str]
    Protocol: Optional[str]
    SessionTimeout: Optional[float]
    SourcePort: Optional[str]
    SyncConnectionsOnCluster: Optional[bool]
    Tags: Optional[Sequence[str]]
    UseDefaultSessionTimeout: Optional[bool]

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
            AcceptReplies=json_data.get("AcceptReplies"),
            AggressiveAging=deserialize_list(json_data.get("AggressiveAging"), AggressiveAgingDefinition),
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            KeepConnectionsOpenAfterPolicyInstallation=json_data.get("KeepConnectionsOpenAfterPolicyInstallation"),
            MatchByProtocolSignature=json_data.get("MatchByProtocolSignature"),
            MatchForAny=json_data.get("MatchForAny"),
            Name=json_data.get("Name"),
            OverrideDefaultSettings=json_data.get("OverrideDefaultSettings"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            SessionTimeout=json_data.get("SessionTimeout"),
            SourcePort=json_data.get("SourcePort"),
            SyncConnectionsOnCluster=json_data.get("SyncConnectionsOnCluster"),
            Tags=json_data.get("Tags"),
            UseDefaultSessionTimeout=json_data.get("UseDefaultSessionTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AggressiveAgingDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AggressiveAgingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggressiveAgingDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggressiveAgingDefinition = AggressiveAgingDefinition


