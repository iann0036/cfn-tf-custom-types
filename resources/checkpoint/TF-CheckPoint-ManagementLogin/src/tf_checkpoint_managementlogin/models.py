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
    ContinueLastSession: Optional[bool]
    Domain: Optional[str]
    EnterLastPublishedSession: Optional[bool]
    Id: Optional[str]
    Password: Optional[str]
    ReadOnly: Optional[bool]
    SessionComments: Optional[str]
    SessionDescription: Optional[str]
    SessionName: Optional[str]
    SessionTimeout: Optional[float]
    User: Optional[str]

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
            ContinueLastSession=json_data.get("ContinueLastSession"),
            Domain=json_data.get("Domain"),
            EnterLastPublishedSession=json_data.get("EnterLastPublishedSession"),
            Id=json_data.get("Id"),
            Password=json_data.get("Password"),
            ReadOnly=json_data.get("ReadOnly"),
            SessionComments=json_data.get("SessionComments"),
            SessionDescription=json_data.get("SessionDescription"),
            SessionName=json_data.get("SessionName"),
            SessionTimeout=json_data.get("SessionTimeout"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


