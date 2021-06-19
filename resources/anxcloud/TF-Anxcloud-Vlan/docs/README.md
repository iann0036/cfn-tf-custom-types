# TF::Anxcloud::Vlan

CloudFormation equivalent of anxcloud_vlan

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Anxcloud::Vlan",
    "Properties" : {
        "<a href="#descriptioncustomer" title="DescriptionCustomer">DescriptionCustomer</a>" : <i>String</i>,
        "<a href="#locationid" title="LocationId">LocationId</a>" : <i>String</i>,
        "<a href="#vmprovisioning" title="VmProvisioning">VmProvisioning</a>" : <i>Boolean</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Anxcloud::Vlan
Properties:
    <a href="#descriptioncustomer" title="DescriptionCustomer">DescriptionCustomer</a>: <i>String</i>
    <a href="#locationid" title="LocationId">LocationId</a>: <i>String</i>
    <a href="#vmprovisioning" title="VmProvisioning">VmProvisioning</a>: <i>Boolean</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DescriptionCustomer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmProvisioning

_Required_: No

_Type_: Boolean

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

#### DescriptionInternal

Returns the <code>DescriptionInternal</code> value.

#### Id

Returns the <code>Id</code> value.

#### Locations

Returns the <code>Locations</code> value.

#### Name

Returns the <code>Name</code> value.

#### RoleText

Returns the <code>RoleText</code> value.

#### Status

Returns the <code>Status</code> value.

