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
    AuthProfile: Optional[str]
    BfdProfile: Optional[str]
    DeadCounts: Optional[float]
    Enable: Optional[bool]
    GraceRestartDelay: Optional[float]
    HelloInterval: Optional[float]
    Id: Optional[str]
    LinkType: Optional[str]
    Metric: Optional[float]
    Name: Optional[str]
    Neighbors: Optional[Sequence[str]]
    OspfArea: Optional[str]
    Passive: Optional[bool]
    Priority: Optional[float]
    RetransmitInterval: Optional[float]
    Template: Optional[str]
    TemplateStack: Optional[str]
    TransitDelay: Optional[float]
    VirtualRouter: Optional[str]

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
            AuthProfile=json_data.get("AuthProfile"),
            BfdProfile=json_data.get("BfdProfile"),
            DeadCounts=json_data.get("DeadCounts"),
            Enable=json_data.get("Enable"),
            GraceRestartDelay=json_data.get("GraceRestartDelay"),
            HelloInterval=json_data.get("HelloInterval"),
            Id=json_data.get("Id"),
            LinkType=json_data.get("LinkType"),
            Metric=json_data.get("Metric"),
            Name=json_data.get("Name"),
            Neighbors=json_data.get("Neighbors"),
            OspfArea=json_data.get("OspfArea"),
            Passive=json_data.get("Passive"),
            Priority=json_data.get("Priority"),
            RetransmitInterval=json_data.get("RetransmitInterval"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            TransitDelay=json_data.get("TransitDelay"),
            VirtualRouter=json_data.get("VirtualRouter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


