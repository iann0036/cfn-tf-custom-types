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
    AcceptAuthByCert: Optional[str]
    AuthorizationRequestType: Optional[str]
    Certificate: Optional[str]
    ConfigurationSync: Optional[str]
    DynamicSortSubtable: Optional[str]
    FabricObjectUnification: Optional[str]
    FixedKey: Optional[str]
    GroupName: Optional[str]
    GroupPassword: Optional[str]
    Id: Optional[str]
    ManagementIp: Optional[str]
    ManagementPort: Optional[float]
    SamlConfigurationSync: Optional[str]
    Status: Optional[str]
    UpstreamIp: Optional[str]
    UpstreamPort: Optional[float]
    Vdomparam: Optional[str]
    FabricDevice: Optional[Sequence["_FabricDeviceDefinition"]]
    TrustedList: Optional[Sequence["_TrustedListDefinition"]]

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
            AcceptAuthByCert=json_data.get("AcceptAuthByCert"),
            AuthorizationRequestType=json_data.get("AuthorizationRequestType"),
            Certificate=json_data.get("Certificate"),
            ConfigurationSync=json_data.get("ConfigurationSync"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            FabricObjectUnification=json_data.get("FabricObjectUnification"),
            FixedKey=json_data.get("FixedKey"),
            GroupName=json_data.get("GroupName"),
            GroupPassword=json_data.get("GroupPassword"),
            Id=json_data.get("Id"),
            ManagementIp=json_data.get("ManagementIp"),
            ManagementPort=json_data.get("ManagementPort"),
            SamlConfigurationSync=json_data.get("SamlConfigurationSync"),
            Status=json_data.get("Status"),
            UpstreamIp=json_data.get("UpstreamIp"),
            UpstreamPort=json_data.get("UpstreamPort"),
            Vdomparam=json_data.get("Vdomparam"),
            FabricDevice=deserialize_list(json_data.get("FabricDevice"), FabricDeviceDefinition),
            TrustedList=deserialize_list(json_data.get("TrustedList"), TrustedListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FabricDeviceDefinition(BaseModel):
    AccessToken: Optional[str]
    DeviceIp: Optional[str]
    DeviceType: Optional[str]
    HttpsPort: Optional[float]
    Login: Optional[str]
    Name: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FabricDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FabricDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessToken=json_data.get("AccessToken"),
            DeviceIp=json_data.get("DeviceIp"),
            DeviceType=json_data.get("DeviceType"),
            HttpsPort=json_data.get("HttpsPort"),
            Login=json_data.get("Login"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FabricDeviceDefinition = FabricDeviceDefinition


@dataclass
class TrustedListDefinition(BaseModel):
    Action: Optional[str]
    AuthorizationType: Optional[str]
    Certificate: Optional[str]
    DownstreamAuthorization: Optional[str]
    HaMembers: Optional[str]
    Name: Optional[str]
    Serial: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrustedListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustedListDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            AuthorizationType=json_data.get("AuthorizationType"),
            Certificate=json_data.get("Certificate"),
            DownstreamAuthorization=json_data.get("DownstreamAuthorization"),
            HaMembers=json_data.get("HaMembers"),
            Name=json_data.get("Name"),
            Serial=json_data.get("Serial"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustedListDefinition = TrustedListDefinition


