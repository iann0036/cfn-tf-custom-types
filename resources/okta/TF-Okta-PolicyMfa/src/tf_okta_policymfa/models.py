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
    Description: Optional[str]
    Duo: Optional[Sequence["_DuoDefinition"]]
    FidoU2f: Optional[Sequence["_FidoU2fDefinition"]]
    FidoWebauthn: Optional[Sequence["_FidoWebauthnDefinition"]]
    GoogleOtp: Optional[Sequence["_GoogleOtpDefinition"]]
    GroupsIncluded: Optional[Sequence[str]]
    Hotp: Optional[Sequence["_HotpDefinition"]]
    Id: Optional[str]
    Name: Optional[str]
    OktaCall: Optional[Sequence["_OktaCallDefinition"]]
    OktaEmail: Optional[Sequence["_OktaEmailDefinition"]]
    OktaOtp: Optional[Sequence["_OktaOtpDefinition"]]
    OktaPassword: Optional[Sequence["_OktaPasswordDefinition"]]
    OktaPush: Optional[Sequence["_OktaPushDefinition"]]
    OktaQuestion: Optional[Sequence["_OktaQuestionDefinition"]]
    OktaSms: Optional[Sequence["_OktaSmsDefinition"]]
    Priority: Optional[float]
    RsaToken: Optional[Sequence["_RsaTokenDefinition"]]
    Status: Optional[str]
    SymantecVip: Optional[Sequence["_SymantecVipDefinition"]]
    YubikeyToken: Optional[Sequence["_YubikeyTokenDefinition"]]

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
            Description=json_data.get("Description"),
            Duo=deserialize_list(json_data.get("Duo"), DuoDefinition),
            FidoU2f=deserialize_list(json_data.get("FidoU2f"), FidoU2fDefinition),
            FidoWebauthn=deserialize_list(json_data.get("FidoWebauthn"), FidoWebauthnDefinition),
            GoogleOtp=deserialize_list(json_data.get("GoogleOtp"), GoogleOtpDefinition),
            GroupsIncluded=json_data.get("GroupsIncluded"),
            Hotp=deserialize_list(json_data.get("Hotp"), HotpDefinition),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OktaCall=deserialize_list(json_data.get("OktaCall"), OktaCallDefinition),
            OktaEmail=deserialize_list(json_data.get("OktaEmail"), OktaEmailDefinition),
            OktaOtp=deserialize_list(json_data.get("OktaOtp"), OktaOtpDefinition),
            OktaPassword=deserialize_list(json_data.get("OktaPassword"), OktaPasswordDefinition),
            OktaPush=deserialize_list(json_data.get("OktaPush"), OktaPushDefinition),
            OktaQuestion=deserialize_list(json_data.get("OktaQuestion"), OktaQuestionDefinition),
            OktaSms=deserialize_list(json_data.get("OktaSms"), OktaSmsDefinition),
            Priority=json_data.get("Priority"),
            RsaToken=deserialize_list(json_data.get("RsaToken"), RsaTokenDefinition),
            Status=json_data.get("Status"),
            SymantecVip=deserialize_list(json_data.get("SymantecVip"), SymantecVipDefinition),
            YubikeyToken=deserialize_list(json_data.get("YubikeyToken"), YubikeyTokenDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DuoDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DuoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DuoDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DuoDefinition = DuoDefinition


@dataclass
class FidoU2fDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FidoU2fDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FidoU2fDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FidoU2fDefinition = FidoU2fDefinition


@dataclass
class FidoWebauthnDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FidoWebauthnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FidoWebauthnDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FidoWebauthnDefinition = FidoWebauthnDefinition


@dataclass
class GoogleOtpDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleOtpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleOtpDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleOtpDefinition = GoogleOtpDefinition


@dataclass
class HotpDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HotpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HotpDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HotpDefinition = HotpDefinition


@dataclass
class OktaCallDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OktaCallDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OktaCallDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OktaCallDefinition = OktaCallDefinition


@dataclass
class OktaEmailDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OktaEmailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OktaEmailDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OktaEmailDefinition = OktaEmailDefinition


@dataclass
class OktaOtpDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OktaOtpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OktaOtpDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OktaOtpDefinition = OktaOtpDefinition


@dataclass
class OktaPasswordDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OktaPasswordDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OktaPasswordDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OktaPasswordDefinition = OktaPasswordDefinition


@dataclass
class OktaPushDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OktaPushDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OktaPushDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OktaPushDefinition = OktaPushDefinition


@dataclass
class OktaQuestionDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OktaQuestionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OktaQuestionDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OktaQuestionDefinition = OktaQuestionDefinition


@dataclass
class OktaSmsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OktaSmsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OktaSmsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OktaSmsDefinition = OktaSmsDefinition


@dataclass
class RsaTokenDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RsaTokenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RsaTokenDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RsaTokenDefinition = RsaTokenDefinition


@dataclass
class SymantecVipDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SymantecVipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SymantecVipDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SymantecVipDefinition = SymantecVipDefinition


@dataclass
class YubikeyTokenDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_YubikeyTokenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_YubikeyTokenDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_YubikeyTokenDefinition = YubikeyTokenDefinition


