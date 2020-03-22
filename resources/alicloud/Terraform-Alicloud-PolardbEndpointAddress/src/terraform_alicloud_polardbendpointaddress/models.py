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
    ConnectionPrefix: Optional[str]
    ConnectionString: Optional[str]
    DbClusterId: Optional[str]
    DbEndpointId: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    NetType: Optional[str]
    Port: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ConnectionPrefix=json_data.get("ConnectionPrefix"),
            ConnectionString=json_data.get("ConnectionString"),
            DbClusterId=json_data.get("DbClusterId"),
            DbEndpointId=json_data.get("DbEndpointId"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            NetType=json_data.get("NetType"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


