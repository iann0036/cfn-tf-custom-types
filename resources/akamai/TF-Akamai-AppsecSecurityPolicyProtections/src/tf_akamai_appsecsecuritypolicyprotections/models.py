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
    ApplyApiConstraints: Optional[bool]
    ApplyApplicationLayerControls: Optional[bool]
    ApplyBotmanControls: Optional[bool]
    ApplyNetworkLayerControls: Optional[bool]
    ApplyRateControls: Optional[bool]
    ApplyReputationControls: Optional[bool]
    ApplySlowPostControls: Optional[bool]
    ConfigId: Optional[float]
    Id: Optional[str]
    SecurityPolicyId: Optional[str]
    Version: Optional[float]

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
            ApplyApiConstraints=json_data.get("ApplyApiConstraints"),
            ApplyApplicationLayerControls=json_data.get("ApplyApplicationLayerControls"),
            ApplyBotmanControls=json_data.get("ApplyBotmanControls"),
            ApplyNetworkLayerControls=json_data.get("ApplyNetworkLayerControls"),
            ApplyRateControls=json_data.get("ApplyRateControls"),
            ApplyReputationControls=json_data.get("ApplyReputationControls"),
            ApplySlowPostControls=json_data.get("ApplySlowPostControls"),
            ConfigId=json_data.get("ConfigId"),
            Id=json_data.get("Id"),
            SecurityPolicyId=json_data.get("SecurityPolicyId"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


