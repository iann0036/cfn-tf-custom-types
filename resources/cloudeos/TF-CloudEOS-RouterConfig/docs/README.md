# TF::CloudEOS::RouterConfig

The `cloudeos_router_config` resource should be created before the CloudEOS Router is deployed. It sends deployment
information to CVaaS, which returns the bootstrap configuration with which the router
will be deployed. After the CloudEOS Router boots up, it will start streaming to CVaaS and register itself.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CloudEOS::RouterConfig",
    "Properties" : {
        "<a href="#ami" title="Ami">Ami</a>" : <i>String</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#cloudprovider" title="CloudProvider">CloudProvider</a>" : <i>String</i>,
        "<a href="#cnps" title="Cnps">Cnps</a>" : <i>String</i>,
        "<a href="#intfname" title="IntfName">IntfName</a>" : <i>[ String, ... ]</i>,
        "<a href="#intfprivateip" title="IntfPrivateIp">IntfPrivateIp</a>" : <i>[ String, ... ]</i>,
        "<a href="#intftype" title="IntfType">IntfType</a>" : <i>[ String, ... ]</i>,
        "<a href="#isrr" title="IsRr">IsRr</a>" : <i>Boolean</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#topologyname" title="TopologyName">TopologyName</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CloudEOS::RouterConfig
Properties:
    <a href="#ami" title="Ami">Ami</a>: <i>String</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#cloudprovider" title="CloudProvider">CloudProvider</a>: <i>String</i>
    <a href="#cnps" title="Cnps">Cnps</a>: <i>String</i>
    <a href="#intfname" title="IntfName">IntfName</a>: <i>
      - String</i>
    <a href="#intfprivateip" title="IntfPrivateIp">IntfPrivateIp</a>: <i>
      - String</i>
    <a href="#intftype" title="IntfType">IntfType</a>: <i>
      - String</i>
    <a href="#isrr" title="IsRr">IsRr</a>: <i>Boolean</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#topologyname" title="TopologyName">TopologyName</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Ami

CloudEOS image. ( AWS only ).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

Availability Zone of VPC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProvider

Cloud Provider for this deployment. Supports only aws or azure.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cnps

Cloud Network Private Segments Name. ( VRF name ).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntfName

List of interface names.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntfPrivateIp

List of interface private IPs. Currently, only supports 1 IP address per interface.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntfType

List of Interface type (public, private, internal). A `public` interface has a public IP
associated with it. An `internal` interface is the interface which connects the Leaf and Edge routers.
And a `private` interface is the default GW interface for all host traffic.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsRr

true if this CloudEOS acts as a Route Reflector.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

keypair name ( AWS only ).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Region of deployment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

CloudEdge or CloudLeaf (Same as VPC role).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopologyName

Name of the topology in which this CloudEOS router is deployed in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

VPC/VNET ID in which this CloudEOS is deployed.

_Required_: Yes

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

#### BootstrapCfg

Returns the <code>BootstrapCfg</code> value.

#### HaRtrId

Returns the <code>HaRtrId</code> value.

#### Id

Returns the <code>Id</code> value.

#### InternalRtTableId

Returns the <code>InternalRtTableId</code> value.

#### PeerRoutetableId

Returns the <code>PeerRoutetableId</code> value.

#### Peerroutetableid1

Returns the <code>Peerroutetableid1</code> value.

#### PrivateRtTableId

Returns the <code>PrivateRtTableId</code> value.

#### PublicRtTableId

Returns the <code>PublicRtTableId</code> value.

#### TfId

Returns the <code>TfId</code> value.

