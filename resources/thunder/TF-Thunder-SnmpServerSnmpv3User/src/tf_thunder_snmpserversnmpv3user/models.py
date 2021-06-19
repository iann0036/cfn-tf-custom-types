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
    AuthVal: Optional[str]
    Encpasswd: Optional[str]
    Group: Optional[str]
    Id: Optional[str]
    Passwd: Optional[str]
    Priv: Optional[str]
    PrivPwEncrypted: Optional[str]
    PwEncrypted: Optional[str]
    Username: Optional[str]
    Uuid: Optional[str]
    V3: Optional[str]

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
            AuthVal=json_data.get("AuthVal"),
            Encpasswd=json_data.get("Encpasswd"),
            Group=json_data.get("Group"),
            Id=json_data.get("Id"),
            Passwd=json_data.get("Passwd"),
            Priv=json_data.get("Priv"),
            PrivPwEncrypted=json_data.get("PrivPwEncrypted"),
            PwEncrypted=json_data.get("PwEncrypted"),
            Username=json_data.get("Username"),
            Uuid=json_data.get("Uuid"),
            V3=json_data.get("V3"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


