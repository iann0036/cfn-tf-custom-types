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
    GwName: Optional[str]
    Id: Optional[str]
    SyncToHa: Optional[bool]
    DnatPolicy: Optional[Sequence["_DnatPolicyDefinition"]]

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
            GwName=json_data.get("GwName"),
            Id=json_data.get("Id"),
            SyncToHa=json_data.get("SyncToHa"),
            DnatPolicy=deserialize_list(json_data.get("DnatPolicy"), DnatPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DnatPolicyDefinition(BaseModel):
    Connection: Optional[str]
    DnatIps: Optional[str]
    DnatPort: Optional[str]
    DstCidr: Optional[str]
    DstPort: Optional[str]
    ExcludeRtb: Optional[str]
    Interface: Optional[str]
    Mark: Optional[str]
    Protocol: Optional[str]
    SrcCidr: Optional[str]
    SrcPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnatPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnatPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Connection=json_data.get("Connection"),
            DnatIps=json_data.get("DnatIps"),
            DnatPort=json_data.get("DnatPort"),
            DstCidr=json_data.get("DstCidr"),
            DstPort=json_data.get("DstPort"),
            ExcludeRtb=json_data.get("ExcludeRtb"),
            Interface=json_data.get("Interface"),
            Mark=json_data.get("Mark"),
            Protocol=json_data.get("Protocol"),
            SrcCidr=json_data.get("SrcCidr"),
            SrcPort=json_data.get("SrcPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnatPolicyDefinition = DnatPolicyDefinition


