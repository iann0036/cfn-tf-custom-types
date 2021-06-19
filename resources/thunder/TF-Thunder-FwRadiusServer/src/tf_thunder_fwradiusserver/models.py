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
    AccountingInterimUpdate: Optional[str]
    AccountingOn: Optional[str]
    AccountingStart: Optional[str]
    AccountingStop: Optional[str]
    AttributeName: Optional[str]
    CustomAttributeName: Optional[str]
    Encrypted: Optional[str]
    Id: Optional[str]
    ListenPort: Optional[float]
    Secret: Optional[float]
    SecretString: Optional[str]
    Uuid: Optional[str]
    Vrid: Optional[float]
    Attribute: Optional[Sequence["_AttributeDefinition"]]
    Remote: Optional[Sequence["_RemoteDefinition"]]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

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
            AccountingInterimUpdate=json_data.get("AccountingInterimUpdate"),
            AccountingOn=json_data.get("AccountingOn"),
            AccountingStart=json_data.get("AccountingStart"),
            AccountingStop=json_data.get("AccountingStop"),
            AttributeName=json_data.get("AttributeName"),
            CustomAttributeName=json_data.get("CustomAttributeName"),
            Encrypted=json_data.get("Encrypted"),
            Id=json_data.get("Id"),
            ListenPort=json_data.get("ListenPort"),
            Secret=json_data.get("Secret"),
            SecretString=json_data.get("SecretString"),
            Uuid=json_data.get("Uuid"),
            Vrid=json_data.get("Vrid"),
            Attribute=deserialize_list(json_data.get("Attribute"), AttributeDefinition),
            Remote=deserialize_list(json_data.get("Remote"), RemoteDefinition),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttributeDefinition(BaseModel):
    AttributeValue: Optional[str]
    CustomNumber: Optional[float]
    CustomVendor: Optional[float]
    Name: Optional[str]
    Number: Optional[float]
    PrefixLength: Optional[str]
    PrefixNumber: Optional[float]
    PrefixVendor: Optional[float]
    Value: Optional[str]
    Vendor: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeDefinition"]:
        if not json_data:
            return None
        return cls(
            AttributeValue=json_data.get("AttributeValue"),
            CustomNumber=json_data.get("CustomNumber"),
            CustomVendor=json_data.get("CustomVendor"),
            Name=json_data.get("Name"),
            Number=json_data.get("Number"),
            PrefixLength=json_data.get("PrefixLength"),
            PrefixNumber=json_data.get("PrefixNumber"),
            PrefixVendor=json_data.get("PrefixVendor"),
            Value=json_data.get("Value"),
            Vendor=json_data.get("Vendor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeDefinition = AttributeDefinition


@dataclass
class RemoteDefinition(BaseModel):
    IpList: Optional[Sequence["_IpListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteDefinition"]:
        if not json_data:
            return None
        return cls(
            IpList=deserialize_list(json_data.get("IpList"), IpListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteDefinition = RemoteDefinition


@dataclass
class IpListDefinition(BaseModel):
    IpListEncrypted: Optional[str]
    IpListName: Optional[str]
    IpListSecret: Optional[float]
    IpListSecretString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpListDefinition"]:
        if not json_data:
            return None
        return cls(
            IpListEncrypted=json_data.get("IpListEncrypted"),
            IpListName=json_data.get("IpListName"),
            IpListSecret=json_data.get("IpListSecret"),
            IpListSecretString=json_data.get("IpListSecretString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpListDefinition = IpListDefinition


@dataclass
class SamplingEnableDefinition(BaseModel):
    Counters1: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SamplingEnableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamplingEnableDefinition"]:
        if not json_data:
            return None
        return cls(
            Counters1=json_data.get("Counters1"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamplingEnableDefinition = SamplingEnableDefinition


