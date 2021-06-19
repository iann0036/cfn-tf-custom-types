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
    AltNames: Optional[Sequence[str]]
    Backend: Optional[str]
    CommonName: Optional[str]
    Country: Optional[str]
    Csr: Optional[str]
    ExcludeCnFromSans: Optional[bool]
    Format: Optional[str]
    Id: Optional[str]
    IpSans: Optional[Sequence[str]]
    KeyBits: Optional[float]
    KeyType: Optional[str]
    Locality: Optional[str]
    Organization: Optional[str]
    OtherSans: Optional[Sequence[str]]
    Ou: Optional[str]
    PostalCode: Optional[str]
    PrivateKey: Optional[str]
    PrivateKeyFormat: Optional[str]
    PrivateKeyType: Optional[str]
    Province: Optional[str]
    StreetAddress: Optional[str]
    Type: Optional[str]
    UriSans: Optional[Sequence[str]]

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
            AltNames=json_data.get("AltNames"),
            Backend=json_data.get("Backend"),
            CommonName=json_data.get("CommonName"),
            Country=json_data.get("Country"),
            Csr=json_data.get("Csr"),
            ExcludeCnFromSans=json_data.get("ExcludeCnFromSans"),
            Format=json_data.get("Format"),
            Id=json_data.get("Id"),
            IpSans=json_data.get("IpSans"),
            KeyBits=json_data.get("KeyBits"),
            KeyType=json_data.get("KeyType"),
            Locality=json_data.get("Locality"),
            Organization=json_data.get("Organization"),
            OtherSans=json_data.get("OtherSans"),
            Ou=json_data.get("Ou"),
            PostalCode=json_data.get("PostalCode"),
            PrivateKey=json_data.get("PrivateKey"),
            PrivateKeyFormat=json_data.get("PrivateKeyFormat"),
            PrivateKeyType=json_data.get("PrivateKeyType"),
            Province=json_data.get("Province"),
            StreetAddress=json_data.get("StreetAddress"),
            Type=json_data.get("Type"),
            UriSans=json_data.get("UriSans"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


