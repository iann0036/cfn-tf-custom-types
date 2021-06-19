# TF::Alicloud::PolardbEndpoint

Provides a PolarDB endpoint resource to allocate an Internet endpoint string for PolarDB instance.

-> **NOTE:** Available in v1.80.0+. Each PolarDB instance will allocate a intranet connection string automatically and its prefix is Cluster ID.
 To avoid unnecessary conflict, please specified a internet connection prefix before applying the resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::PolardbEndpoint",
    "Properties" : {
        "<a href="#autoaddnewnodes" title="AutoAddNewNodes">AutoAddNewNodes</a>" : <i>String</i>,
        "<a href="#dbclusterid" title="DbClusterId">DbClusterId</a>" : <i>String</i>,
        "<a href="#endpointconfig" title="EndpointConfig">EndpointConfig</a>" : <i>[ <a href="endpointconfigdefinition.md">EndpointConfigDefinition</a>, ... ]</i>,
        "<a href="#endpointtype" title="EndpointType">EndpointType</a>" : <i>String</i>,
        "<a href="#nettype" title="NetType">NetType</a>" : <i>String</i>,
        "<a href="#nodes" title="Nodes">Nodes</a>" : <i>[ String, ... ]</i>,
        "<a href="#readwritemode" title="ReadWriteMode">ReadWriteMode</a>" : <i>String</i>,
        "<a href="#sslenabled" title="SslEnabled">SslEnabled</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::PolardbEndpoint
Properties:
    <a href="#autoaddnewnodes" title="AutoAddNewNodes">AutoAddNewNodes</a>: <i>String</i>
    <a href="#dbclusterid" title="DbClusterId">DbClusterId</a>: <i>String</i>
    <a href="#endpointconfig" title="EndpointConfig">EndpointConfig</a>: <i>
      - <a href="endpointconfigdefinition.md">EndpointConfigDefinition</a></i>
    <a href="#endpointtype" title="EndpointType">EndpointType</a>: <i>String</i>
    <a href="#nettype" title="NetType">NetType</a>: <i>String</i>
    <a href="#nodes" title="Nodes">Nodes</a>: <i>
      - String</i>
    <a href="#readwritemode" title="ReadWriteMode">ReadWriteMode</a>: <i>String</i>
    <a href="#sslenabled" title="SslEnabled">SslEnabled</a>: <i>String</i>
</pre>

## Properties

#### AutoAddNewNodes

Whether the new node automatically joins the default cluster address. Valid values are `Enable`, `Disable`. Default to `Disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbClusterId

The Id of cluster that can run database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointConfig

Advanced configuration of the cluster address.

_Required_: No

_Type_: List of <a href="endpointconfigdefinition.md">EndpointConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointType

Type of endpoint. Valid value: `Custom`. Currently supported only `Custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nodes

Node id list for endpoint configuration. At least 2 nodes if specified, or if the cluster has more than 3 nodes, read-only endpoint is allowed to mount only one node. Default is all nodes.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadWriteMode

Read or write mode. Valid values are `ReadWrite`, `ReadOnly`. Default to `ReadOnly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslEnabled

_Required_: No

_Type_: String

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

#### SslConnectionString

Returns the <code>SslConnectionString</code> value.

#### SslExpireTime

Returns the <code>SslExpireTime</code> value.

