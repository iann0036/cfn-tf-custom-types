# TF::Anxcloud::NetworkPrefix

CloudFormation equivalent of anxcloud_network_prefix

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Anxcloud::NetworkPrefix",
    "Properties" : {
        "<a href="#descriptioncustomer" title="DescriptionCustomer">DescriptionCustomer</a>" : <i>String</i>,
        "<a href="#ipversion" title="IpVersion">IpVersion</a>" : <i>Double</i>,
        "<a href="#locationid" title="LocationId">LocationId</a>" : <i>String</i>,
        "<a href="#netmask" title="Netmask">Netmask</a>" : <i>Double</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>,
        "<a href="#routerredundancy" title="RouterRedundancy">RouterRedundancy</a>" : <i>Boolean</i>,
        "<a href="#type" title="Type">Type</a>" : <i>Double</i>,
        "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Anxcloud::NetworkPrefix
Properties:
    <a href="#descriptioncustomer" title="DescriptionCustomer">DescriptionCustomer</a>: <i>String</i>
    <a href="#ipversion" title="IpVersion">IpVersion</a>: <i>Double</i>
    <a href="#locationid" title="LocationId">LocationId</a>: <i>String</i>
    <a href="#netmask" title="Netmask">Netmask</a>: <i>Double</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
    <a href="#routerredundancy" title="RouterRedundancy">RouterRedundancy</a>: <i>Boolean</i>
    <a href="#type" title="Type">Type</a>: <i>Double</i>
    <a href="#vlanid" title="VlanId">VlanId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DescriptionCustomer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpVersion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterRedundancy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

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

#### Cidr

Returns the <code>Cidr</code> value.

#### DescriptionInternal

Returns the <code>DescriptionInternal</code> value.

#### Id

Returns the <code>Id</code> value.

#### Locations

Returns the <code>Locations</code> value.

#### RoleText

Returns the <code>RoleText</code> value.

#### Status

Returns the <code>Status</code> value.

