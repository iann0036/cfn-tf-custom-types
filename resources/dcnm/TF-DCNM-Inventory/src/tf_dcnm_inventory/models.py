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
    AuthProtocol: Optional[float]
    ConfigTimeout: Optional[float]
    Deploy: Optional[bool]
    FabricName: Optional[str]
    Id: Optional[str]
    Ips: Optional[Sequence[str]]
    MaxHops: Optional[float]
    Password: Optional[str]
    Platform: Optional[str]
    PreserveConfig: Optional[str]
    SecondTimeout: Optional[float]
    Username: Optional[str]
    SwitchConfig: Optional[Sequence["_SwitchConfigDefinition"]]

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
            AuthProtocol=json_data.get("AuthProtocol"),
            ConfigTimeout=json_data.get("ConfigTimeout"),
            Deploy=json_data.get("Deploy"),
            FabricName=json_data.get("FabricName"),
            Id=json_data.get("Id"),
            Ips=json_data.get("Ips"),
            MaxHops=json_data.get("MaxHops"),
            Password=json_data.get("Password"),
            Platform=json_data.get("Platform"),
            PreserveConfig=json_data.get("PreserveConfig"),
            SecondTimeout=json_data.get("SecondTimeout"),
            Username=json_data.get("Username"),
            SwitchConfig=deserialize_list(json_data.get("SwitchConfig"), SwitchConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SwitchConfigDefinition(BaseModel):
    Ip: Optional[str]
    Mode: Optional[str]
    Model: Optional[str]
    Role: Optional[str]
    SerialNumber: Optional[str]
    SwitchDbId: Optional[str]
    SwitchName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SwitchConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SwitchConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Mode=json_data.get("Mode"),
            Model=json_data.get("Model"),
            Role=json_data.get("Role"),
            SerialNumber=json_data.get("SerialNumber"),
            SwitchDbId=json_data.get("SwitchDbId"),
            SwitchName=json_data.get("SwitchName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SwitchConfigDefinition = SwitchConfigDefinition


