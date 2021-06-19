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
    AuthenticationKey: Optional[str]
    ConnectionId: Optional[str]
    DeviceId: Optional[str]
    Id: Optional[str]
    LocalAsn: Optional[float]
    LocalIpAddress: Optional[str]
    ProvisioningStatus: Optional[str]
    RemoteAsn: Optional[float]
    RemoteIpAddress: Optional[str]
    State: Optional[str]
    Uuid: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AuthenticationKey=json_data.get("AuthenticationKey"),
            ConnectionId=json_data.get("ConnectionId"),
            DeviceId=json_data.get("DeviceId"),
            Id=json_data.get("Id"),
            LocalAsn=json_data.get("LocalAsn"),
            LocalIpAddress=json_data.get("LocalIpAddress"),
            ProvisioningStatus=json_data.get("ProvisioningStatus"),
            RemoteAsn=json_data.get("RemoteAsn"),
            RemoteIpAddress=json_data.get("RemoteIpAddress"),
            State=json_data.get("State"),
            Uuid=json_data.get("Uuid"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


