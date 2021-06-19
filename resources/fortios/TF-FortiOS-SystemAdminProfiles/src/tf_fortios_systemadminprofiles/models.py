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
    AdmintimeoutOverride: Optional[str]
    Authgrp: Optional[str]
    Comments: Optional[str]
    Ftviewgrp: Optional[str]
    Fwgrp: Optional[str]
    Id: Optional[str]
    Loggrp: Optional[str]
    Name: Optional[str]
    Netgrp: Optional[str]
    Scope: Optional[str]
    Secfabgrp: Optional[str]
    Sysgrp: Optional[str]
    Utmgrp: Optional[str]
    Vpngrp: Optional[str]
    Wanoptgrp: Optional[str]
    Wifi: Optional[str]

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
            AdmintimeoutOverride=json_data.get("AdmintimeoutOverride"),
            Authgrp=json_data.get("Authgrp"),
            Comments=json_data.get("Comments"),
            Ftviewgrp=json_data.get("Ftviewgrp"),
            Fwgrp=json_data.get("Fwgrp"),
            Id=json_data.get("Id"),
            Loggrp=json_data.get("Loggrp"),
            Name=json_data.get("Name"),
            Netgrp=json_data.get("Netgrp"),
            Scope=json_data.get("Scope"),
            Secfabgrp=json_data.get("Secfabgrp"),
            Sysgrp=json_data.get("Sysgrp"),
            Utmgrp=json_data.get("Utmgrp"),
            Vpngrp=json_data.get("Vpngrp"),
            Wanoptgrp=json_data.get("Wanoptgrp"),
            Wifi=json_data.get("Wifi"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


