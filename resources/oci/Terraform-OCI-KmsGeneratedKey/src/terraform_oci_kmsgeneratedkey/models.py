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
    AssociatedData: Optional[Sequence["_AssociatedData"]]
    Ciphertext: Optional[str]
    CryptoEndpoint: Optional[str]
    Id: Optional[str]
    IncludePlaintextKey: Optional[bool]
    KeyId: Optional[str]
    LoggingContext: Optional[Sequence["_LoggingContext"]]
    Plaintext: Optional[str]
    PlaintextChecksum: Optional[str]
    KeyShape: Optional[Sequence["_KeyShape"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AssociatedData=json_data.get("AssociatedData"),
            Ciphertext=json_data.get("Ciphertext"),
            CryptoEndpoint=json_data.get("CryptoEndpoint"),
            Id=json_data.get("Id"),
            IncludePlaintextKey=json_data.get("IncludePlaintextKey"),
            KeyId=json_data.get("KeyId"),
            LoggingContext=json_data.get("LoggingContext"),
            Plaintext=json_data.get("Plaintext"),
            PlaintextChecksum=json_data.get("PlaintextChecksum"),
            KeyShape=json_data.get("KeyShape"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AssociatedData:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssociatedData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssociatedData"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssociatedData = AssociatedData


@dataclass
class LoggingContext:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingContext"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingContext = LoggingContext


@dataclass
class KeyShape:
    Algorithm: Optional[str]
    Length: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_KeyShape"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyShape"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Length=json_data.get("Length"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyShape = KeyShape


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


