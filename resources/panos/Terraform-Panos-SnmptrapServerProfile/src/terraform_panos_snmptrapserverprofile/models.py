# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    AuthPasswordEnc: Optional[Sequence["_AuthPasswordEnc"]]
    AuthPasswordRaw: Optional[Sequence["_AuthPasswordRaw"]]
    Name: Optional[str]
    PrivPasswordEnc: Optional[Sequence["_PrivPasswordEnc"]]
    PrivPasswordRaw: Optional[Sequence["_PrivPasswordRaw"]]
    Vsys: Optional[str]
    V2cServer: Optional[Sequence["_V2cServer"]]
    V3Server: Optional[Sequence["_V3Server"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthPasswordEnc=json_data.get("AuthPasswordEnc"),
            AuthPasswordRaw=json_data.get("AuthPasswordRaw"),
            Name=json_data.get("Name"),
            PrivPasswordEnc=json_data.get("PrivPasswordEnc"),
            PrivPasswordRaw=json_data.get("PrivPasswordRaw"),
            Vsys=json_data.get("Vsys"),
            V2cServer=json_data.get("V2cServer"),
            V3Server=json_data.get("V3Server"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthPasswordEnc:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthPasswordEnc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthPasswordEnc"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthPasswordEnc = AuthPasswordEnc


@dataclass
class AuthPasswordRaw:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthPasswordRaw"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthPasswordRaw"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthPasswordRaw = AuthPasswordRaw


@dataclass
class PrivPasswordEnc:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivPasswordEnc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivPasswordEnc"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivPasswordEnc = PrivPasswordEnc


@dataclass
class PrivPasswordRaw:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivPasswordRaw"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivPasswordRaw"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivPasswordRaw = PrivPasswordRaw


@dataclass
class V2cServer:
    Community: Optional[str]
    Manager: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_V2cServer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_V2cServer"]:
        if not json_data:
            return None
        return cls(
            Community=json_data.get("Community"),
            Manager=json_data.get("Manager"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_V2cServer = V2cServer


@dataclass
class V3Server:
    AuthPassword: Optional[str]
    EngineId: Optional[str]
    Manager: Optional[str]
    Name: Optional[str]
    PrivPassword: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_V3Server"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_V3Server"]:
        if not json_data:
            return None
        return cls(
            AuthPassword=json_data.get("AuthPassword"),
            EngineId=json_data.get("EngineId"),
            Manager=json_data.get("Manager"),
            Name=json_data.get("Name"),
            PrivPassword=json_data.get("PrivPassword"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_V3Server = V3Server


