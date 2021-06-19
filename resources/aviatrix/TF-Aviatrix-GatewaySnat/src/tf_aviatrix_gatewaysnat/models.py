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
    SnatMode: Optional[str]
    SyncToHa: Optional[bool]
    SnatPolicy: Optional[Sequence["_SnatPolicyDefinition"]]

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
            SnatMode=json_data.get("SnatMode"),
            SyncToHa=json_data.get("SyncToHa"),
            SnatPolicy=deserialize_list(json_data.get("SnatPolicy"), SnatPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SnatPolicyDefinition(BaseModel):
    Connection: Optional[str]
    DstCidr: Optional[str]
    DstPort: Optional[str]
    ExcludeRtb: Optional[str]
    Interface: Optional[str]
    Mark: Optional[str]
    Protocol: Optional[str]
    SnatIps: Optional[str]
    SnatPort: Optional[str]
    SrcCidr: Optional[str]
    SrcPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnatPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnatPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Connection=json_data.get("Connection"),
            DstCidr=json_data.get("DstCidr"),
            DstPort=json_data.get("DstPort"),
            ExcludeRtb=json_data.get("ExcludeRtb"),
            Interface=json_data.get("Interface"),
            Mark=json_data.get("Mark"),
            Protocol=json_data.get("Protocol"),
            SnatIps=json_data.get("SnatIps"),
            SnatPort=json_data.get("SnatPort"),
            SrcCidr=json_data.get("SrcCidr"),
            SrcPort=json_data.get("SrcPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnatPolicyDefinition = SnatPolicyDefinition


