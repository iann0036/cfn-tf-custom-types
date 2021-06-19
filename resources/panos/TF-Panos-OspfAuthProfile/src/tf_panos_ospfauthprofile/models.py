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
    AuthType: Optional[str]
    Id: Optional[str]
    Md5KeysEnc: Optional[Sequence["_Md5KeysEncDefinition"]]
    Name: Optional[str]
    Password: Optional[str]
    PasswordEnc: Optional[str]
    Template: Optional[str]
    TemplateStack: Optional[str]
    VirtualRouter: Optional[str]
    Md5Key: Optional[Sequence["_Md5KeyDefinition"]]

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
            AuthType=json_data.get("AuthType"),
            Id=json_data.get("Id"),
            Md5KeysEnc=deserialize_list(json_data.get("Md5KeysEnc"), Md5KeysEncDefinition),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PasswordEnc=json_data.get("PasswordEnc"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            VirtualRouter=json_data.get("VirtualRouter"),
            Md5Key=deserialize_list(json_data.get("Md5Key"), Md5KeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Md5KeysEncDefinition(BaseModel):
    Enc: Optional[str]
    Raw: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Md5KeysEncDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Md5KeysEncDefinition"]:
        if not json_data:
            return None
        return cls(
            Enc=json_data.get("Enc"),
            Raw=json_data.get("Raw"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Md5KeysEncDefinition = Md5KeysEncDefinition


@dataclass
class Md5KeyDefinition(BaseModel):
    Key: Optional[str]
    KeyId: Optional[float]
    Preferred: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Md5KeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Md5KeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            KeyId=json_data.get("KeyId"),
            Preferred=json_data.get("Preferred"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Md5KeyDefinition = Md5KeyDefinition


