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
    AdminKey: Optional[float]
    Id: Optional[str]
    Ifnum: Optional[float]
    Mode: Optional[str]
    PortPriority: Optional[float]
    Timeout: Optional[str]
    TrunkNumber: Optional[float]
    Type: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    UdldTimeoutCfg: Optional[Sequence["_UdldTimeoutCfgDefinition"]]

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
            AdminKey=json_data.get("AdminKey"),
            Id=json_data.get("Id"),
            Ifnum=json_data.get("Ifnum"),
            Mode=json_data.get("Mode"),
            PortPriority=json_data.get("PortPriority"),
            Timeout=json_data.get("Timeout"),
            TrunkNumber=json_data.get("TrunkNumber"),
            Type=json_data.get("Type"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            UdldTimeoutCfg=deserialize_list(json_data.get("UdldTimeoutCfg"), UdldTimeoutCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UdldTimeoutCfgDefinition(BaseModel):
    Fast: Optional[float]
    Slow: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UdldTimeoutCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdldTimeoutCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Fast=json_data.get("Fast"),
            Slow=json_data.get("Slow"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdldTimeoutCfgDefinition = UdldTimeoutCfgDefinition


