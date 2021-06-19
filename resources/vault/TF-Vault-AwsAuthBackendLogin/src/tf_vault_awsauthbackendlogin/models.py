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
    Accessor: Optional[str]
    AuthType: Optional[str]
    Backend: Optional[str]
    ClientToken: Optional[str]
    IamHttpRequestMethod: Optional[str]
    IamRequestBody: Optional[str]
    IamRequestHeaders: Optional[str]
    IamRequestUrl: Optional[str]
    Id: Optional[str]
    Identity: Optional[str]
    LeaseDuration: Optional[float]
    LeaseStartTime: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Nonce: Optional[str]
    Pkcs7: Optional[str]
    Policies: Optional[Sequence[str]]
    Renewable: Optional[bool]
    Role: Optional[str]
    Signature: Optional[str]

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
            Accessor=json_data.get("Accessor"),
            AuthType=json_data.get("AuthType"),
            Backend=json_data.get("Backend"),
            ClientToken=json_data.get("ClientToken"),
            IamHttpRequestMethod=json_data.get("IamHttpRequestMethod"),
            IamRequestBody=json_data.get("IamRequestBody"),
            IamRequestHeaders=json_data.get("IamRequestHeaders"),
            IamRequestUrl=json_data.get("IamRequestUrl"),
            Id=json_data.get("Id"),
            Identity=json_data.get("Identity"),
            LeaseDuration=json_data.get("LeaseDuration"),
            LeaseStartTime=json_data.get("LeaseStartTime"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Nonce=json_data.get("Nonce"),
            Pkcs7=json_data.get("Pkcs7"),
            Policies=json_data.get("Policies"),
            Renewable=json_data.get("Renewable"),
            Role=json_data.get("Role"),
            Signature=json_data.get("Signature"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


