# TF::BIGIP::As3

CloudFormation equivalent of bigip_as3

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::As3",
    "Properties" : {
        "<a href="#applicationlist" title="ApplicationList">ApplicationList</a>" : <i>String</i>,
        "<a href="#as3json" title="As3Json">As3Json</a>" : <i>String</i>,
        "<a href="#ignoremetadata" title="IgnoreMetadata">IgnoreMetadata</a>" : <i>Boolean</i>,
        "<a href="#tenantfilter" title="TenantFilter">TenantFilter</a>" : <i>String</i>,
        "<a href="#tenantlist" title="TenantList">TenantList</a>" : <i>String</i>,
        "<a href="#tenantname" title="TenantName">TenantName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::As3
Properties:
    <a href="#applicationlist" title="ApplicationList">ApplicationList</a>: <i>String</i>
    <a href="#as3json" title="As3Json">As3Json</a>: <i>String</i>
    <a href="#ignoremetadata" title="IgnoreMetadata">IgnoreMetadata</a>: <i>Boolean</i>
    <a href="#tenantfilter" title="TenantFilter">TenantFilter</a>: <i>String</i>
    <a href="#tenantlist" title="TenantList">TenantList</a>: <i>String</i>
    <a href="#tenantname" title="TenantName">TenantName</a>: <i>String</i>
</pre>

## Properties

#### ApplicationList

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### As3Json

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreMetadata

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantList

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantName

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

