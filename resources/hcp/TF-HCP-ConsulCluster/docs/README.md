# TF::HCP::ConsulCluster

CloudFormation equivalent of hcp_consul_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::HCP::ConsulCluster",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#connectenabled" title="ConnectEnabled">ConnectEnabled</a>" : <i>Boolean</i>,
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#hvnid" title="HvnId">HvnId</a>" : <i>String</i>,
        "<a href="#minconsulversion" title="MinConsulVersion">MinConsulVersion</a>" : <i>String</i>,
        "<a href="#primarylink" title="PrimaryLink">PrimaryLink</a>" : <i>String</i>,
        "<a href="#publicendpoint" title="PublicEndpoint">PublicEndpoint</a>" : <i>Boolean</i>,
        "<a href="#size" title="Size">Size</a>" : <i>String</i>,
        "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::HCP::ConsulCluster
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#connectenabled" title="ConnectEnabled">ConnectEnabled</a>: <i>Boolean</i>
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#hvnid" title="HvnId">HvnId</a>: <i>String</i>
    <a href="#minconsulversion" title="MinConsulVersion">MinConsulVersion</a>: <i>String</i>
    <a href="#primarylink" title="PrimaryLink">PrimaryLink</a>: <i>String</i>
    <a href="#publicendpoint" title="PublicEndpoint">PublicEndpoint</a>: <i>Boolean</i>
    <a href="#size" title="Size">Size</a>: <i>String</i>
    <a href="#tier" title="Tier">Tier</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ClusterId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datacenter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HvnId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinConsulVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryLink

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicEndpoint

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier

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

#### CloudProvider

Returns the <code>CloudProvider</code> value.

#### ConsulAutomaticUpgrades

Returns the <code>ConsulAutomaticUpgrades</code> value.

#### ConsulCaFile

Returns the <code>ConsulCaFile</code> value.

#### ConsulConfigFile

Returns the <code>ConsulConfigFile</code> value.

#### ConsulPrivateEndpointUrl

Returns the <code>ConsulPrivateEndpointUrl</code> value.

#### ConsulPublicEndpointUrl

Returns the <code>ConsulPublicEndpointUrl</code> value.

#### ConsulRootTokenAccessorId

Returns the <code>ConsulRootTokenAccessorId</code> value.

#### ConsulRootTokenSecretId

Returns the <code>ConsulRootTokenSecretId</code> value.

#### ConsulSnapshotInterval

Returns the <code>ConsulSnapshotInterval</code> value.

#### ConsulSnapshotRetention

Returns the <code>ConsulSnapshotRetention</code> value.

#### ConsulVersion

Returns the <code>ConsulVersion</code> value.

#### Id

Returns the <code>Id</code> value.

#### OrganizationId

Returns the <code>OrganizationId</code> value.

#### ProjectId

Returns the <code>ProjectId</code> value.

#### Region

Returns the <code>Region</code> value.

#### Scale

Returns the <code>Scale</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

