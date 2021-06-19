# TF::CloudEOS::RouterStatus

The `cloudeos_router_status` resource should be created after a CloudEOS router has been deployed. It sends all the information
about the deployed CloudEOS router to CVaaS. Unlike `cloudeos_router_config` which takes minimal input about how the
CloudEOS router should be deployed, `cloudeos_router_status` provides detailed deployment information after the router
is deployed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CloudEOS::RouterStatus",
    "Properties" : {
        "<a href="#availabilitysetid" title="AvailabilitySetId">AvailabilitySetId</a>" : <i>String</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#cloudprovider" title="CloudProvider">CloudProvider</a>" : <i>String</i>,
        "<a href="#cnps" title="Cnps">Cnps</a>" : <i>String</i>,
        "<a href="#cvcontainer" title="CvContainer">CvContainer</a>" : <i>String</i>,
        "<a href="#deploymentstatus" title="DeploymentStatus">DeploymentStatus</a>" : <i>String</i>,
        "<a href="#haname" title="HaName">HaName</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#internalrttableids" title="InternalRtTableIds">InternalRtTableIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#intfid" title="IntfId">IntfId</a>" : <i>[ String, ... ]</i>,
        "<a href="#intfname" title="IntfName">IntfName</a>" : <i>[ String, ... ]</i>,
        "<a href="#intfprivateip" title="IntfPrivateIp">IntfPrivateIp</a>" : <i>[ String, ... ]</i>,
        "<a href="#intfsubnetid" title="IntfSubnetId">IntfSubnetId</a>" : <i>[ String, ... ]</i>,
        "<a href="#intftype" title="IntfType">IntfType</a>" : <i>[ String, ... ]</i>,
        "<a href="#isrr" title="IsRr">IsRr</a>" : <i>Boolean</i>,
        "<a href="#primarynetworkinterfaceid" title="PrimaryNetworkInterfaceId">PrimaryNetworkInterfaceId</a>" : <i>String</i>,
        "<a href="#privaterttableids" title="PrivateRtTableIds">PrivateRtTableIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#publicip" title="PublicIp">PublicIp</a>" : <i>String</i>,
        "<a href="#publicrttableids" title="PublicRtTableIds">PublicRtTableIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#rglocation" title="RgLocation">RgLocation</a>" : <i>String</i>,
        "<a href="#rgname" title="RgName">RgName</a>" : <i>String</i>,
        "<a href="#routerbgpasn" title="RouterBgpAsn">RouterBgpAsn</a>" : <i>String</i>,
        "<a href="#routingresourceinfo" title="RoutingResourceInfo">RoutingResourceInfo</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tfid" title="TfId">TfId</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CloudEOS::RouterStatus
Properties:
    <a href="#availabilitysetid" title="AvailabilitySetId">AvailabilitySetId</a>: <i>String</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#cloudprovider" title="CloudProvider">CloudProvider</a>: <i>String</i>
    <a href="#cnps" title="Cnps">Cnps</a>: <i>String</i>
    <a href="#cvcontainer" title="CvContainer">CvContainer</a>: <i>String</i>
    <a href="#deploymentstatus" title="DeploymentStatus">DeploymentStatus</a>: <i>String</i>
    <a href="#haname" title="HaName">HaName</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#internalrttableids" title="InternalRtTableIds">InternalRtTableIds</a>: <i>
      - String</i>
    <a href="#intfid" title="IntfId">IntfId</a>: <i>
      - String</i>
    <a href="#intfname" title="IntfName">IntfName</a>: <i>
      - String</i>
    <a href="#intfprivateip" title="IntfPrivateIp">IntfPrivateIp</a>: <i>
      - String</i>
    <a href="#intfsubnetid" title="IntfSubnetId">IntfSubnetId</a>: <i>
      - String</i>
    <a href="#intftype" title="IntfType">IntfType</a>: <i>
      - String</i>
    <a href="#isrr" title="IsRr">IsRr</a>: <i>Boolean</i>
    <a href="#primarynetworkinterfaceid" title="PrimaryNetworkInterfaceId">PrimaryNetworkInterfaceId</a>: <i>String</i>
    <a href="#privaterttableids" title="PrivateRtTableIds">PrivateRtTableIds</a>: <i>
      - String</i>
    <a href="#publicip" title="PublicIp">PublicIp</a>: <i>String</i>
    <a href="#publicrttableids" title="PublicRtTableIds">PublicRtTableIds</a>: <i>
      - String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#rglocation" title="RgLocation">RgLocation</a>: <i>String</i>
    <a href="#rgname" title="RgName">RgName</a>: <i>String</i>
    <a href="#routerbgpasn" title="RouterBgpAsn">RouterBgpAsn</a>: <i>String</i>
    <a href="#routingresourceinfo" title="RoutingResourceInfo">RoutingResourceInfo</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tfid" title="TfId">TfId</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AvailabilitySetId

Availability Set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

Availability Zone in which the router is deployed in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProvider

CloudProvider type. Supports only aws or azure.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cnps

Cloud Network Private Segments ( VRF name ).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CvContainer

Container in CVaaS to which the router will be added to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaName

Cloud HA pair name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

Instance ID of deployed CloudEOS.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalRtTableIds

List of internal interface route table IDs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntfId

List of interface IDs attached to the routers.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntfName

List of interface names for the routers.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntfPrivateIp

List of private IPs attached to the interfaces.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntfSubnetId

List of subnet IDs of interfaces.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntfType

List of interface types. Values supported : public, internal, private.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsRr

true if this CloudEOS acts as a Route Reflector.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryNetworkInterfaceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateRtTableIds

List of private interface route table IDs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIp

Public IP of interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicRtTableIds

List of public route table IDs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Region of deployment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RgLocation

Resource group location, only for Azure.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RgName

Resource group name, only for Azure.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterBgpAsn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingResourceInfo

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TfId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

VPC/VNET ID of the VPC in which the CloudEOS is deployed in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

