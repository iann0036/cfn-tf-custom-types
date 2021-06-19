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
    DvsVersion: Optional[str]
    HostOrIp: Optional[str]
    Id: Optional[str]
    InventoryTrigSt: Optional[str]
    Mode: Optional[str]
    MsftConfigErrMsg: Optional[str]
    MsftConfigIssues: Optional[Sequence[str]]
    N1kvStatsMode: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    Port: Optional[str]
    RelationVmmRsAcc: Optional[str]
    RelationVmmRsCtrlrPMonPol: Optional[str]
    RelationVmmRsMcastAddrNs: Optional[str]
    RelationVmmRsMgmtEPg: Optional[str]
    RelationVmmRsToExtDevMgr: Optional[Sequence[str]]
    RelationVmmRsVxlanNs: Optional[str]
    RelationVmmRsVxlanNsDef: Optional[str]
    RootContName: Optional[str]
    Scope: Optional[str]
    SeqNum: Optional[str]
    StatsMode: Optional[str]
    VmmDomainDn: Optional[str]
    VxlanDeplPref: Optional[str]
    RelationVmmRsVmmCtrlrP: Optional[Sequence["_RelationVmmRsVmmCtrlrPDefinition"]]

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
            DvsVersion=json_data.get("DvsVersion"),
            HostOrIp=json_data.get("HostOrIp"),
            Id=json_data.get("Id"),
            InventoryTrigSt=json_data.get("InventoryTrigSt"),
            Mode=json_data.get("Mode"),
            MsftConfigErrMsg=json_data.get("MsftConfigErrMsg"),
            MsftConfigIssues=json_data.get("MsftConfigIssues"),
            N1kvStatsMode=json_data.get("N1kvStatsMode"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            Port=json_data.get("Port"),
            RelationVmmRsAcc=json_data.get("RelationVmmRsAcc"),
            RelationVmmRsCtrlrPMonPol=json_data.get("RelationVmmRsCtrlrPMonPol"),
            RelationVmmRsMcastAddrNs=json_data.get("RelationVmmRsMcastAddrNs"),
            RelationVmmRsMgmtEPg=json_data.get("RelationVmmRsMgmtEPg"),
            RelationVmmRsToExtDevMgr=json_data.get("RelationVmmRsToExtDevMgr"),
            RelationVmmRsVxlanNs=json_data.get("RelationVmmRsVxlanNs"),
            RelationVmmRsVxlanNsDef=json_data.get("RelationVmmRsVxlanNsDef"),
            RootContName=json_data.get("RootContName"),
            Scope=json_data.get("Scope"),
            SeqNum=json_data.get("SeqNum"),
            StatsMode=json_data.get("StatsMode"),
            VmmDomainDn=json_data.get("VmmDomainDn"),
            VxlanDeplPref=json_data.get("VxlanDeplPref"),
            RelationVmmRsVmmCtrlrP=deserialize_list(json_data.get("RelationVmmRsVmmCtrlrP"), RelationVmmRsVmmCtrlrPDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RelationVmmRsVmmCtrlrPDefinition(BaseModel):
    EpgDeplPref: Optional[str]
    TargetDn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationVmmRsVmmCtrlrPDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationVmmRsVmmCtrlrPDefinition"]:
        if not json_data:
            return None
        return cls(
            EpgDeplPref=json_data.get("EpgDeplPref"),
            TargetDn=json_data.get("TargetDn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationVmmRsVmmCtrlrPDefinition = RelationVmmRsVmmCtrlrPDefinition


