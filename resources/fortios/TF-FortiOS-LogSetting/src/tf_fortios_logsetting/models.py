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
    BriefTrafficFormat: Optional[str]
    DaemonLog: Optional[str]
    DynamicSortSubtable: Optional[str]
    ExpolicyImplicitLog: Optional[str]
    FazOverride: Optional[str]
    Fwpolicy6ImplicitLog: Optional[str]
    FwpolicyImplicitLog: Optional[str]
    Id: Optional[str]
    LocalInAllow: Optional[str]
    LocalInDenyBroadcast: Optional[str]
    LocalInDenyUnicast: Optional[str]
    LocalOut: Optional[str]
    LogInvalidPacket: Optional[str]
    LogPolicyComment: Optional[str]
    LogPolicyName: Optional[str]
    LogUserInUpper: Optional[str]
    NeighborEvent: Optional[str]
    ResolveIp: Optional[str]
    ResolvePort: Optional[str]
    SyslogOverride: Optional[str]
    UserAnonymize: Optional[str]
    Vdomparam: Optional[str]
    CustomLogFields: Optional[Sequence["_CustomLogFieldsDefinition"]]

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
            BriefTrafficFormat=json_data.get("BriefTrafficFormat"),
            DaemonLog=json_data.get("DaemonLog"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            ExpolicyImplicitLog=json_data.get("ExpolicyImplicitLog"),
            FazOverride=json_data.get("FazOverride"),
            Fwpolicy6ImplicitLog=json_data.get("Fwpolicy6ImplicitLog"),
            FwpolicyImplicitLog=json_data.get("FwpolicyImplicitLog"),
            Id=json_data.get("Id"),
            LocalInAllow=json_data.get("LocalInAllow"),
            LocalInDenyBroadcast=json_data.get("LocalInDenyBroadcast"),
            LocalInDenyUnicast=json_data.get("LocalInDenyUnicast"),
            LocalOut=json_data.get("LocalOut"),
            LogInvalidPacket=json_data.get("LogInvalidPacket"),
            LogPolicyComment=json_data.get("LogPolicyComment"),
            LogPolicyName=json_data.get("LogPolicyName"),
            LogUserInUpper=json_data.get("LogUserInUpper"),
            NeighborEvent=json_data.get("NeighborEvent"),
            ResolveIp=json_data.get("ResolveIp"),
            ResolvePort=json_data.get("ResolvePort"),
            SyslogOverride=json_data.get("SyslogOverride"),
            UserAnonymize=json_data.get("UserAnonymize"),
            Vdomparam=json_data.get("Vdomparam"),
            CustomLogFields=deserialize_list(json_data.get("CustomLogFields"), CustomLogFieldsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomLogFieldsDefinition(BaseModel):
    FieldId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomLogFieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomLogFieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomLogFieldsDefinition = CustomLogFieldsDefinition


