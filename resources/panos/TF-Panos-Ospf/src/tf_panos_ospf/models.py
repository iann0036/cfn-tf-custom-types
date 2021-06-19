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
    AllowRedistributeDefaultRoute: Optional[bool]
    BfdProfile: Optional[str]
    Enable: Optional[bool]
    EnableGracefulRestart: Optional[bool]
    GracePeriod: Optional[float]
    HelperEnable: Optional[bool]
    Id: Optional[str]
    LsaInterval: Optional[float]
    MaxNeighborRestartTime: Optional[float]
    RejectDefaultRoute: Optional[bool]
    Rfc1583: Optional[bool]
    RouterId: Optional[str]
    SpfCalculationDelay: Optional[float]
    StrictLsaChecking: Optional[bool]
    Template: Optional[str]
    TemplateStack: Optional[str]
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
            AllowRedistributeDefaultRoute=json_data.get("AllowRedistributeDefaultRoute"),
            BfdProfile=json_data.get("BfdProfile"),
            Enable=json_data.get("Enable"),
            EnableGracefulRestart=json_data.get("EnableGracefulRestart"),
            GracePeriod=json_data.get("GracePeriod"),
            HelperEnable=json_data.get("HelperEnable"),
            Id=json_data.get("Id"),
            LsaInterval=json_data.get("LsaInterval"),
            MaxNeighborRestartTime=json_data.get("MaxNeighborRestartTime"),
            RejectDefaultRoute=json_data.get("RejectDefaultRoute"),
            Rfc1583=json_data.get("Rfc1583"),
            RouterId=json_data.get("RouterId"),
            SpfCalculationDelay=json_data.get("SpfCalculationDelay"),
            StrictLsaChecking=json_data.get("StrictLsaChecking"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            VirtualRouter=json_data.get("VirtualRouter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


