# Terraform::Vault::GenericSecret

CloudFormation equivalent of vault_generic_secret

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::GenericSecret",
    "Properties" : {
        "<a href="#allowread" title="AllowRead">AllowRead</a>" : <i>Boolean</i>,
        "<a href="#datajson" title="DataJson">DataJson</a>" : <i>String</i>,
        "<a href="#disableread" title="DisableRead">DisableRead</a>" : <i>Boolean</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::GenericSecret
Properties:
    <a href="#allowread" title="AllowRead">AllowRead</a>: <i>Boolean</i>
    <a href="#datajson" title="DataJson">DataJson</a>: <i>String</i>
    <a href="#disableread" title="DisableRead">DisableRead</a>: <i>Boolean</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
</pre>

## Properties

#### AllowRead

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataJson

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableRead

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: Yes

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

#### Data

Returns the <code>Data</code> value.

