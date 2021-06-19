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
    ClientProfiles: Optional[Sequence[str]]
    DefaultPersistenceProfile: Optional[str]
    Description: Optional[str]
    Destination: Optional[str]
    FallbackPersistenceProfile: Optional[str]
    Id: Optional[str]
    IpProtocol: Optional[str]
    Irules: Optional[Sequence[str]]
    Mask: Optional[str]
    Name: Optional[str]
    PersistenceProfiles: Optional[Sequence[str]]
    Policies: Optional[Sequence[str]]
    Pool: Optional[str]
    Port: Optional[float]
    Profiles: Optional[Sequence[str]]
    ServerProfiles: Optional[Sequence[str]]
    Snatpool: Optional[str]
    Source: Optional[str]
    SourceAddressTranslation: Optional[str]
    State: Optional[str]
    TranslateAddress: Optional[str]
    TranslatePort: Optional[str]
    Vlans: Optional[Sequence[str]]
    VlansEnabled: Optional[bool]

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
            ClientProfiles=json_data.get("ClientProfiles"),
            DefaultPersistenceProfile=json_data.get("DefaultPersistenceProfile"),
            Description=json_data.get("Description"),
            Destination=json_data.get("Destination"),
            FallbackPersistenceProfile=json_data.get("FallbackPersistenceProfile"),
            Id=json_data.get("Id"),
            IpProtocol=json_data.get("IpProtocol"),
            Irules=json_data.get("Irules"),
            Mask=json_data.get("Mask"),
            Name=json_data.get("Name"),
            PersistenceProfiles=json_data.get("PersistenceProfiles"),
            Policies=json_data.get("Policies"),
            Pool=json_data.get("Pool"),
            Port=json_data.get("Port"),
            Profiles=json_data.get("Profiles"),
            ServerProfiles=json_data.get("ServerProfiles"),
            Snatpool=json_data.get("Snatpool"),
            Source=json_data.get("Source"),
            SourceAddressTranslation=json_data.get("SourceAddressTranslation"),
            State=json_data.get("State"),
            TranslateAddress=json_data.get("TranslateAddress"),
            TranslatePort=json_data.get("TranslatePort"),
            Vlans=json_data.get("Vlans"),
            VlansEnabled=json_data.get("VlansEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


